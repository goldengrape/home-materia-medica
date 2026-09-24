#!/usr/bin/env python3
"""Run Jev v0.4: synchronous meridian + dominant yin/yang direction Choice pilot."""

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
DIRECTION_VALUES = ["阴-", "阴+", "阳-", "阳+"]


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
        direction_lines = [
            f"- {meridian}经主方向：{direction}"
            for meridian, direction in answer.get("directions", {}).items()
        ]
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

    criteria = {
        "阴-": "主要作用是减少该经阴侧的偏盛、停聚、积滞或壅滞，如化湿、燥湿、化痰、利水、消食、消积。",
        "阴+": "主要作用是增加该经滋养、津液、血、精、濡润或收摄，如养阴、生津、润燥、补血、益精。",
        "阳-": "主要作用是减少该经热、火、亢进、升越或过强活动，如清热、泻火、平亢；项目约定中疏肝归入肝阳-。",
        "阳+": "主要作用是增加该经温煦、推动、运化或功能性活动，如温、助阳、回阳、健脾、健胃、助运。",
    }

    for meridian, mslug in base.MERIDIAN_KEY.items():
        questions[f"{mslug}_direction"] = {
            "type": "choice",
            "instructions": (
                f"判断待判断说明文档对“{meridian}经”的主要阴阳增减作用方向。"
                "先区分病机状态与食材/药物实际作用；如果有多个方向，选择全文中更主要、直接、重复支持更多的一项。"
            ),
            "criteria": criteria,
        }

    return questions


def expected_answer_keys(base) -> set[str]:
    return set(base.expected_answer_keys()) | {
        f"{slug}_direction" for slug in base.MERIDIAN_KEY.values()
    }


def validate_answers(base, answers: dict[str, Any]) -> None:
    expected = expected_answer_keys(base)
    if set(answers) != expected:
        raise AssertionError(
            f"Answer keys changed. expected={sorted(expected)} actual={sorted(answers)}"
        )

    original = {k: v for k, v in answers.items() if k in base.expected_answer_keys()}
    base.validate_answers(original)

    for slug in base.MERIDIAN_KEY.values():
        key = f"{slug}_direction"
        answer = answers[key]
        if answer.get("type") != "choice":
            raise AssertionError(f"{key} is not choice.")
        if answer.get("choice") not in DIRECTION_VALUES:
            raise AssertionError(f"Invalid {key} choice: {answer}")
        if set(answer.get("probabilities", {})) != set(DIRECTION_VALUES):
            raise AssertionError(f"{key} probabilities do not match direction values.")


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
    taste_exact = meridian_exact = 0

    direction_correct = 0
    direction_total = 0

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
        gold = case["gold"]

        qi_ok = predicted_qi == gold["qi"]
        qi_correct += int(qi_ok)

        pt, gt = set(predicted_tastes), set(gold["tastes"])
        ttp, tfp, tfn = base.set_counts(pt, gt)
        taste_tp += ttp
        taste_fp += tfp
        taste_fn += tfn
        taste_exact += int(pt == gt)

        pm, gm = set(predicted_meridians), set(gold["meridians"])
        mtp, mfp, mfn = base.set_counts(pm, gm)
        meridian_tp += mtp
        meridian_fp += mfp
        meridian_fn += mfn
        meridian_exact += int(pm == gm)

        direction_results: dict[str, Any] = {}
        for meridian, gold_direction in gold.get("directions", {}).items():
            slug = base.MERIDIAN_KEY[meridian]
            answer = answers[f"{slug}_direction"]
            choice = answer["choice"]
            probs = answer["probabilities"]
            ok = choice == gold_direction
            direction_correct += int(ok)
            direction_total += 1
            sorted_probs = sorted(
                ((label, float(p)) for label, p in probs.items()),
                key=lambda x: x[1],
                reverse=True,
            )
            margin = (
                sorted_probs[0][1] - sorted_probs[1][1]
                if len(sorted_probs) > 1
                else sorted_probs[0][1]
            )
            direction_results[meridian] = {
                "gold": gold_direction,
                "choice": choice,
                "correct": ok,
                "probabilities": probs,
                "top_margin": round(margin, 4),
            }

        all_direction_choices = {
            meridian: {
                "choice": answers[f"{slug}_direction"]["choice"],
                "probabilities": answers[f"{slug}_direction"]["probabilities"],
            }
            for meridian, slug in base.MERIDIAN_KEY.items()
        }

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
                    "directions_for_gold_meridians": direction_results,
                    "all_direction_choices": all_direction_choices,
                },
                "correct": {
                    "qi": qi_ok,
                    "taste_exact_set": pt == gt,
                    "meridian_exact_set": pm == gm,
                    "direction_gold_meridians_all_correct": all(
                        x["correct"] for x in direction_results.values()
                    ),
                },
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
                "micro": base.prf(taste_tp, taste_fp, taste_fn),
            },
            "meridian": {
                "exact_set_matches": meridian_exact,
                "total": n,
                "micro": base.prf(meridian_tp, meridian_fp, meridian_fn),
            },
            "direction": {
                "correct": direction_correct,
                "total": direction_total,
                "accuracy": round(direction_correct / direction_total, 4)
                if direction_total
                else 0.0,
            },
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
        "direction_schema": "one 4-way Choice per meridian: 阴-/阴+/阳-/阳+",
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
