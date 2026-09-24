#!/usr/bin/env python3
"""Run Jev v0.4: synchronous meridian + yin/yang direction vector pilot."""

from __future__ import annotations

import importlib.util
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
BASE_RUNNER = ROOT / "run_pilot_v031.py"
FIXTURE_PATH = ROOT / "fixtures-v0.4.json"
RULES_PATH = ROOT.parent.parent / "skills" / "home-materia-jev-mapping" / "references" / "reasoning-rules-v0.4.md"
RESULTS_PATH = ROOT / "results-v0.4.json"

PROMPT_VERSION = "jev-tcm-rule-fewshot-v0.4"
THRESHOLD = 0.5

DIRECTION_KEY = {
    "阴-": "yin_decrease",
    "阴+": "yin_increase",
    "阳-": "yang_decrease",
    "阳+": "yang_increase",
}


def load_module(path: Path):
    spec = importlib.util.spec_from_file_location("jev_v031_base", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot import base runner: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_rules() -> str:
    return RULES_PATH.read_text(encoding="utf-8")


def render_examples(fixtures: dict[str, Any]) -> str:
    chunks: list[str] = []
    for idx, demo in enumerate(fixtures["reference_examples"], start=1):
        answer = demo["answer"]
        direction_lines: list[str] = []
        for meridian, directions in answer.get("directions", {}).items():
            direction_lines.append(f"- {meridian}经方向：{'、'.join(directions)}")
        chunks.append(
            f"""### 参考示例 {idx}

资料说明：

{demo["document"]}

标准结果：
- 四气：{answer["qi"]}
- 五味：{"、".join(answer["tastes"])}
- 五脏归经：{"、".join(answer["meridians"])}
{chr(10).join(direction_lines)}
"""
        )
    return "\n".join(chunks)


def build_state(fixtures: dict[str, Any], case: dict[str, Any]) -> str:
    return f"""# 判定方法

{load_rules()}

# 参考示例

{render_examples(fixtures)}

# 待判断说明文档

{case["document"]}
"""


def build_questions(base) -> dict[str, Any]:
    questions = base.build_questions()

    direction_semantics = {
        "阴-": (
            "判断待判断说明文档所描述的食材/药物，是否使该经阴侧的偏盛、停聚或壅滞减少。"
            "典型包括化湿、燥湿、化痰、利水等；阴-不等于损伤正常阴液。"
        ),
        "阴+": (
            "判断待判断说明文档所描述的食材/药物，是否增加该经滋养、津液、血、精、濡润或收摄等阴侧表现。"
            "典型包括养阴、生津、润燥、补血、益精。"
        ),
        "阳-": (
            "判断待判断说明文档所描述的食材/药物，是否减少该经热、火、亢进、升越或过强活动。"
            "典型包括清热、泻火、平亢、降逆；项目工作约定中疏肝可作为肝阳-的派生表达。"
        ),
        "阳+": (
            "判断待判断说明文档所描述的食材/药物，是否增加该经温煦、推动、活动或功能性阳侧表现。"
            "典型包括温、助阳、回阳、推动功能以及纠正虚寒。"
        ),
    }

    for meridian, mslug in base.MERIDIAN_KEY.items():
        for direction, dslug in DIRECTION_KEY.items():
            key = f"{mslug}_{dslug}"
            questions[key] = {
                "type": "noul",
                "instructions": (
                    f"根据 state 中的推理方法，判断待判断说明文档是否支持“{meridian}经{direction}”。"
                    "先区分被处理的病机状态与食材/药物的作用方向；本题判断的是作用方向。"
                ),
                "criteria": {
                    "true": direction_semantics[direction],
                    "false": f"综合全文后，不支持“{meridian}经{direction}”作为该对象的作用方向。",
                },
            }

    return questions


def expected_answer_keys(base) -> set[str]:
    keys = set(base.expected_answer_keys())
    for mslug in base.MERIDIAN_KEY.values():
        for dslug in DIRECTION_KEY.values():
            keys.add(f"{mslug}_{dslug}")
    return keys


def validate_answers(base, answers: dict[str, Any]) -> None:
    expected = expected_answer_keys(base)
    if set(answers) != expected:
        raise AssertionError(
            f"Answer keys changed. expected={sorted(expected)} actual={sorted(answers)}"
        )

    # Validate the original 11 fields using the v0.3.1 contract.
    original = {k: v for k, v in answers.items() if k in base.expected_answer_keys()}
    base.validate_answers(original)

    for key in expected - set(original):
        answer = answers[key]
        if answer.get("type") != "noul":
            raise AssertionError(f"{key} is not noul.")
        value = answer.get("noul")
        if not isinstance(value, (int, float)) or not 0 <= value <= 1:
            raise AssertionError(f"{key} noul invalid: {value}")


def predicted_direction_set(base, answers: dict[str, Any]) -> set[str]:
    out: set[str] = set()
    for meridian, mslug in base.MERIDIAN_KEY.items():
        for direction, dslug in DIRECTION_KEY.items():
            if answers[f"{mslug}_{dslug}"]["noul"] >= THRESHOLD:
                out.add(f"{meridian}:{direction}")
    return out


def gold_direction_set(case: dict[str, Any]) -> set[str]:
    out: set[str] = set()
    for meridian, directions in case["gold"].get("directions", {}).items():
        for direction in directions:
            out.add(f"{meridian}:{direction}")
    return out


def set_counts(predicted: set[str], gold: set[str]) -> tuple[int, int, int]:
    return len(predicted & gold), len(predicted - gold), len(gold - predicted)


def prf(tp: int, fp: int, fn: int) -> dict[str, float]:
    precision = tp / (tp + fp) if tp + fp else 1.0
    recall = tp / (tp + fn) if tp + fn else 1.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    return {
        "precision": round(precision, 4),
        "recall": round(recall, 4),
        "f1": round(f1, 4),
    }


def location_direction_disagreements(base, answers: dict[str, Any]) -> list[dict[str, Any]]:
    issues: list[dict[str, Any]] = []
    for meridian, mslug in base.MERIDIAN_KEY.items():
        meridian_score = float(answers[f"meridian_{mslug}"]["noul"])
        for direction, dslug in DIRECTION_KEY.items():
            direction_score = float(answers[f"{mslug}_{dslug}"]["noul"])
            if meridian_score < THRESHOLD <= direction_score:
                issues.append(
                    {
                        "meridian": meridian,
                        "meridian_score": meridian_score,
                        "direction": direction,
                        "direction_score": direction_score,
                    }
                )
    return issues


def run_once(
    base,
    fixtures: dict[str, Any],
    questions: dict[str, Any],
    api_key: str,
    requested_model: str,
    repeat_index: int,
) -> dict[str, Any]:
    cases_out: list[dict[str, Any]] = []
    actual_models: set[str] = set()

    qi_correct = 0
    taste_tp = taste_fp = taste_fn = 0
    meridian_tp = meridian_fp = meridian_fn = 0
    vector_tp = vector_fp = vector_fn = 0
    taste_exact = meridian_exact = vector_exact = 0
    disagreement_count = 0

    for case in fixtures["test_cases"]:
        state = build_state(fixtures, case)
        base.assert_no_target_leakage(state, fixtures)

        response = base.api_json(
            "POST",
            "/v1/systemone",
            api_key,
            {"state": state, "model": requested_model, "questions": questions},
        )
        answers = response["answers"]
        validate_answers(base, answers)
        actual_models.add(response["model"])

        predicted_tastes, predicted_meridians = base.labels_from_answers(answers)
        predicted_qi = answers["qi"]["choice"]
        predicted_vectors = predicted_direction_set(base, answers)
        gold = case["gold"]
        gold_vectors = gold_direction_set(case)

        qi_ok = predicted_qi == gold["qi"]
        qi_correct += int(qi_ok)

        pt, gt = set(predicted_tastes), set(gold["tastes"])
        ttp, tfp, tfn = set_counts(pt, gt)
        taste_tp += ttp
        taste_fp += tfp
        taste_fn += tfn
        taste_exact += int(pt == gt)

        pm, gm = set(predicted_meridians), set(gold["meridians"])
        mtp, mfp, mfn = set_counts(pm, gm)
        meridian_tp += mtp
        meridian_fp += mfp
        meridian_fn += mfn
        meridian_exact += int(pm == gm)

        vtp, vfp, vfn = set_counts(predicted_vectors, gold_vectors)
        vector_tp += vtp
        vector_fp += vfp
        vector_fn += vfn
        vector_exact += int(predicted_vectors == gold_vectors)

        disagreements = location_direction_disagreements(base, answers)
        disagreement_count += len(disagreements)

        cases_out.append(
            {
                "sample_id": case["sample_id"],
                "herb": case["meta"]["herb"],
                "document": case["document"],
                "gold": gold,
                "predicted": {
                    "qi": predicted_qi,
                    "tastes_at_0_5": predicted_tastes,
                    "meridians_at_0_5": predicted_meridians,
                    "directions_at_0_5": sorted(predicted_vectors),
                },
                "correct": {
                    "qi": qi_ok,
                    "taste_exact_set": pt == gt,
                    "meridian_exact_set": pm == gm,
                    "direction_exact_set": predicted_vectors == gold_vectors,
                },
                "location_direction_disagreements": disagreements,
                "native_answers": answers,
                "usage": response["usage"],
            }
        )

    if len(actual_models) != 1:
        raise AssertionError(f"Multiple actual models: {sorted(actual_models)}")

    n = len(cases_out)
    return {
        "repeat_index": repeat_index,
        "actual_model": next(iter(actual_models)),
        "cases": cases_out,
        "summary": {
            "n_cases": n,
            "qi": {
                "correct": qi_correct,
                "total": n,
                "accuracy": round(qi_correct / n, 4),
            },
            "taste": {
                "exact_set_matches": taste_exact,
                "total": n,
                "micro": prf(taste_tp, taste_fp, taste_fn),
            },
            "meridian": {
                "exact_set_matches": meridian_exact,
                "total": n,
                "micro": prf(meridian_tp, meridian_fp, meridian_fn),
            },
            "directions": {
                "exact_set_matches": vector_exact,
                "total": n,
                "micro": prf(vector_tp, vector_fp, vector_fn),
            },
            "location_direction_disagreement_count": disagreement_count,
        },
    }


def main() -> int:
    api_key = os.environ.get("JEV_API_KEY")
    if not api_key:
        print("ERROR: JEV_API_KEY is missing.", file=sys.stderr)
        return 2

    base = load_module(BASE_RUNNER)
    fixtures = load_json(FIXTURE_PATH)
    base.validate_fixture_separation(fixtures)
    questions = build_questions(base)

    requested_model = os.environ.get("JEV_MODEL", base.DEFAULT_MODEL)
    repeat_count = int(os.environ.get("JEV_REPEATS", "3"))

    models = base.api_json("GET", "/v1/models", api_key)
    available = {item["name"] for item in models["models"]}
    if requested_model not in available:
        raise RuntimeError(
            f"Requested model alias {requested_model!r} unavailable. Available: {sorted(available)}"
        )

    repeats = [
        run_once(base, fixtures, questions, api_key, requested_model, i)
        for i in range(1, repeat_count + 1)
    ]

    result = {
        "run_timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "prompt_version": PROMPT_VERSION,
        "fixture_version": fixtures["fixture_version"],
        "reasoning_version": fixtures["reasoning_version"],
        "requested_model": requested_model,
        "actual_models": sorted({r["actual_model"] for r in repeats}),
        "architecture": "semantic cascade; computationally synchronous single Jev request",
        "question_count": len(questions),
        "probability_policy": "Native Jev probabilities unchanged; no post-hoc calibration.",
        "repeats": repeats,
    }

    RESULTS_PATH.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    for repeat in repeats:
        print(f"repeat {repeat['repeat_index']}:")
        print(json.dumps(repeat["summary"], ensure_ascii=False, indent=2))
    print(f"Results written to {RESULTS_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
