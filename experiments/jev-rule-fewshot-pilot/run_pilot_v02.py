#!/usr/bin/env python3
"""Run Jev v0.2 closed-schema TCM classification pilot.

Output space is intentionally closed:
- qi: 寒/凉/平/温/热 (forced choice)
- tastes: 酸/苦/甘/辛/咸 (five independent Noul fields)
- meridians: 心/肝/脾/肺/肾 (five independent Noul fields)

No abstention and no post-hoc probability calibration.
"""

from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

API_BASE = "https://api.typesafe.ai"
DEFAULT_MODEL = "jev-latest"
PROMPT_VERSION = "jev-tcm-rule-fewshot-v0.2"
THRESHOLD = 0.5

ROOT = Path(__file__).resolve().parent
FIXTURE_PATH = ROOT / "fixtures-v0.2.json"
RESULTS_PATH = ROOT / "results-v0.2.json"

QI_VALUES = ["寒", "凉", "平", "温", "热"]
TASTE_KEY = {
    "酸": "sour",
    "苦": "bitter",
    "甘": "sweet",
    "辛": "pungent",
    "咸": "salty",
}
MERIDIAN_KEY = {
    "心": "heart",
    "肝": "liver",
    "脾": "spleen",
    "肺": "lung",
    "肾": "kidney",
}

QI_CRITERIA = {
    "寒": "在寒/凉/平/温/热五个固定类别中，整体传统功能与主治最符合寒性。大寒、寒统一投影到寒。",
    "凉": "在五个固定类别中，整体最符合较缓和的凉性。凉、微寒统一投影到凉。",
    "平": "在五个固定类别中，整体最符合平性。",
    "温": "在五个固定类别中，整体最符合温性。微温、温统一投影到温。",
    "热": "在五个固定类别中，整体最符合热性。热、大热统一投影到热。",
}


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def api_json(method: str, path: str, api_key: str, payload: dict[str, Any] | None = None) -> dict[str, Any]:
    body = None if payload is None else json.dumps(payload, ensure_ascii=False).encode("utf-8")
    request = urllib.request.Request(
        f"{API_BASE}{path}",
        data=body,
        method=method,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "User-Agent": "home-materia-medica-jev-pilot/0.2",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Jev API HTTP {exc.code}: {detail}") from exc


def validate_fixture_schema(fixtures: dict[str, Any]) -> None:
    schema = fixtures["output_schema"]
    if schema["qi"] != QI_VALUES:
        raise AssertionError(f"Unexpected qi schema: {schema['qi']}")
    if schema["tastes"] != list(TASTE_KEY):
        raise AssertionError(f"Unexpected taste schema: {schema['tastes']}")
    if schema["meridians"] != list(MERIDIAN_KEY):
        raise AssertionError(f"Unexpected meridian schema: {schema['meridians']}")

    demo_herbs = {d["meta"]["herb"] for d in fixtures["reference_examples"]}
    test_herbs = {c["meta"]["herb"] for c in fixtures["test_cases"]}
    overlap = demo_herbs & test_herbs
    if overlap:
        raise AssertionError(f"Few-shot/test herb overlap: {sorted(overlap)}")


def build_reference_examples(fixtures: dict[str, Any]) -> list[dict[str, Any]]:
    # Intentionally omit meta/herb/source from state.
    return [
        {
            "demo_id": demo["demo_id"],
            "packet": demo["packet"],
            "correct_answer": demo["answer_projected"],
        }
        for demo in fixtures["reference_examples"]
    ]


def build_state(fixtures: dict[str, Any], case: dict[str, Any]) -> dict[str, Any]:
    return {
        "task": "在预先限定的四气、五味、五脏归经字段中，对 target 强制分类。",
        "closed_output_schema": fixtures["output_schema"],
        "rules": [
            "只评估 target；reference_examples 只展示本项目分类方式。",
            "不得尝试恢复被隐藏的药名，也不得把可能猜出的身份当作证据。",
            "四气没有证据不足、未知或其他类别；必须在寒、凉、平、温、热中选择一个。",
            "四气归一：大寒/寒→寒；凉/微寒→凉；平→平；微温/温→温；热/大热→热。",
            "五味输出字段只能是酸、苦、甘、辛、咸；没有淡、涩或其他字段。",
            "organoleptic_sensory 是实际感官，不等于传统五味，不能仅凭入口味觉决定五味。",
            "五味五个字段均需判断；每个字段独立，不要求只选一种。",
            "归经输出字段只能是心、肝、脾、肺、肾；没有胃、胆、大肠、小肠、膀胱、三焦、心包等字段。",
            "五脏归经五个字段均需判断；每个字段独立，不要求只选一种。",
            "传统功能和主治中的脏腑词是证据，但不能仅凭词面机械复制成归经。",
            "没有 abstention。即使资料不充分，也要在封闭字段内给出相对概率与强制分类结果。",
            "保留 Jev 原生概率；不进行任何事后概率校准或修正。",
        ],
        "reference_examples": build_reference_examples(fixtures),
        "target": {
            "sample_id": case["sample_id"],
            "packet": case["packet"],
        },
    }


def build_questions() -> dict[str, Any]:
    questions: dict[str, Any] = {
        "qi": {
            "type": "choice",
            "instructions": {
                "task": "仅判断 target 的四气；必须在五个固定类别中选择一个，不允许拒答。",
                "allowed_values": QI_VALUES,
            },
            "criteria": QI_CRITERIA,
        }
    }

    for taste, slug in TASTE_KEY.items():
        questions[f"taste_{slug}"] = {
            "type": "noul",
            "instructions": {
                "task": f"仅判断 target 的传统五味固定字段“{taste}”是否成立。",
                "closed_schema": "五味只允许酸、苦、甘、辛、咸五个字段；本字段必须返回概率。",
            },
            "criteria": {
                "true": f"按传统功能、主治和 few-shot 分类方式，应将“{taste}”标为 true。",
                "false": f"按传统功能、主治和 few-shot 分类方式，应将“{taste}”标为 false。",
            },
        }

    for meridian, slug in MERIDIAN_KEY.items():
        questions[f"meridian_{slug}"] = {
            "type": "noul",
            "instructions": {
                "task": f"仅判断 target 的五脏归经固定字段“{meridian}”是否成立。",
                "closed_schema": "归经只允许心、肝、脾、肺、肾五个字段；本字段必须返回概率。",
            },
            "criteria": {
                "true": f"按传统功能、主治和 few-shot 分类方式，应将“{meridian}”标为 true。",
                "false": f"按传统功能、主治和 few-shot 分类方式，应将“{meridian}”标为 false。",
            },
        }

    return questions


def expected_answer_keys() -> set[str]:
    return (
        {"qi"}
        | {f"taste_{slug}" for slug in TASTE_KEY.values()}
        | {f"meridian_{slug}" for slug in MERIDIAN_KEY.values()}
    )


def assert_closed_questions(questions: dict[str, Any]) -> None:
    expected = expected_answer_keys()
    if set(questions) != expected:
        raise AssertionError(
            f"Question keys are not exact closed schema. expected={sorted(expected)} actual={sorted(questions)}"
        )

    if set(questions["qi"]["criteria"]) != set(QI_VALUES):
        raise AssertionError("Qi criteria must be exactly 寒/凉/平/温/热.")

    serialized = json.dumps(questions, ensure_ascii=False)
    forbidden_output_labels = ["证据不足", "未知", "其他", "淡", "涩", "胃经", "胆经", "大肠经", "小肠经", "膀胱经", "三焦经", "心包经"]
    for label in forbidden_output_labels:
        if label in serialized:
            raise AssertionError(f"Forbidden output label present in question schema: {label}")


def assert_no_target_leakage(state: dict[str, Any], fixtures: dict[str, Any]) -> None:
    serialized = json.dumps(state, ensure_ascii=False)

    for forbidden_key in ['"gold_source_raw"', '"gold_projected"']:
        if forbidden_key in serialized:
            raise AssertionError(f"Gold leaked into Jev state: {forbidden_key}")

    for case in fixtures["test_cases"]:
        herb = case["meta"]["herb"]
        source = case["meta"]["source"]
        if herb in serialized:
            raise AssertionError(f"Held-out herb name leaked into Jev state: {herb}")
        if source in serialized:
            raise AssertionError(f"Held-out source URL leaked into Jev state: {source}")


def validate_answers(answers: dict[str, Any]) -> None:
    expected = expected_answer_keys()
    if set(answers) != expected:
        raise AssertionError(
            f"Answer keys are not exact closed schema. expected={sorted(expected)} actual={sorted(answers)}"
        )

    qi = answers["qi"]
    if qi.get("type") != "choice":
        raise AssertionError("qi answer is not choice.")
    if qi.get("choice") not in QI_VALUES:
        raise AssertionError(f"qi choice outside closed schema: {qi.get('choice')}")
    probs = qi.get("probabilities", {})
    if set(probs) != set(QI_VALUES):
        raise AssertionError(f"qi probability keys outside closed schema: {sorted(probs)}")

    for key in expected - {"qi"}:
        answer = answers[key]
        if answer.get("type") != "noul":
            raise AssertionError(f"{key} answer is not noul.")
        value = answer.get("noul")
        if not isinstance(value, (int, float)) or not (0 <= value <= 1):
            raise AssertionError(f"{key} noul out of range: {value}")


def labels_from_answers(answers: dict[str, Any]) -> tuple[list[str], list[str]]:
    tastes = [
        taste for taste, slug in TASTE_KEY.items()
        if answers[f"taste_{slug}"]["noul"] >= THRESHOLD
    ]
    meridians = [
        meridian for meridian, slug in MERIDIAN_KEY.items()
        if answers[f"meridian_{slug}"]["noul"] >= THRESHOLD
    ]
    return tastes, meridians


def set_counts(predicted: set[str], gold: set[str]) -> tuple[int, int, int]:
    return (
        len(predicted & gold),
        len(predicted - gold),
        len(gold - predicted),
    )


def prf(tp: int, fp: int, fn: int) -> dict[str, float]:
    precision = tp / (tp + fp) if tp + fp else 1.0
    recall = tp / (tp + fn) if tp + fn else 1.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    return {
        "precision": round(precision, 4),
        "recall": round(recall, 4),
        "f1": round(f1, 4),
    }


def run_once(
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
    taste_exact = 0
    meridian_exact = 0
    total_input_tokens = 0
    total_output_tokens = 0

    for case in fixtures["test_cases"]:
        state = build_state(fixtures, case)
        assert_no_target_leakage(state, fixtures)

        response = api_json(
            "POST",
            "/v1/systemone",
            api_key,
            {
                "state": state,
                "model": requested_model,
                "questions": questions,
            },
        )
        answers = response["answers"]
        validate_answers(answers)

        actual_models.add(response["model"])
        total_input_tokens += response["usage"]["input_tokens"]
        total_output_tokens += response["usage"]["output_tokens"]

        predicted_tastes, predicted_meridians = labels_from_answers(answers)
        predicted_qi = answers["qi"]["choice"]
        gold = case["gold_projected"]

        qi_ok = predicted_qi == gold["qi"]
        qi_correct += int(qi_ok)

        pred_tastes = set(predicted_tastes)
        gold_tastes = set(gold["tastes"])
        ttp, tfp, tfn = set_counts(pred_tastes, gold_tastes)
        taste_tp += ttp
        taste_fp += tfp
        taste_fn += tfn
        taste_exact += int(pred_tastes == gold_tastes)

        pred_meridians = set(predicted_meridians)
        gold_meridians = set(gold["meridians"])
        mtp, mfp, mfn = set_counts(pred_meridians, gold_meridians)
        meridian_tp += mtp
        meridian_fp += mfp
        meridian_fn += mfn
        meridian_exact += int(pred_meridians == gold_meridians)

        cases_out.append(
            {
                "sample_id": case["sample_id"],
                "herb": case["meta"]["herb"],
                "source": case["meta"]["source"],
                "gold_source_raw": case["gold_source_raw"],
                "gold_projected": gold,
                "predicted": {
                    "qi": predicted_qi,
                    "tastes_at_0_5": predicted_tastes,
                    "meridians_at_0_5": predicted_meridians,
                },
                "correct": {
                    "qi": qi_ok,
                    "taste_exact_set": pred_tastes == gold_tastes,
                    "meridian_exact_set": pred_meridians == gold_meridians,
                },
                "native_answers": answers,
                "usage": response["usage"],
            }
        )

    if len(actual_models) != 1:
        raise AssertionError(f"Multiple actual models returned in one repeat: {sorted(actual_models)}")

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
                "counts": {"tp": taste_tp, "fp": taste_fp, "fn": taste_fn},
            },
            "meridian": {
                "exact_set_matches": meridian_exact,
                "total": n,
                "micro": prf(meridian_tp, meridian_fp, meridian_fn),
                "counts": {"tp": meridian_tp, "fp": meridian_fp, "fn": meridian_fn},
            },
            "usage": {
                "input_tokens": total_input_tokens,
                "output_tokens": total_output_tokens,
            },
        },
    }


def aggregate_ranges(repeats: list[dict[str, Any]]) -> dict[str, Any]:
    def values(path: tuple[str, ...]) -> list[float]:
        out: list[float] = []
        for repeat in repeats:
            cur: Any = repeat["summary"]
            for part in path:
                cur = cur[part]
            out.append(float(cur))
        return out

    def rng(vals: list[float]) -> dict[str, float]:
        return {"min": min(vals), "max": max(vals)}

    return {
        "n_repeats": len(repeats),
        "qi_accuracy": rng(values(("qi", "accuracy"))),
        "taste_exact_set_matches": rng(values(("taste", "exact_set_matches"))),
        "taste_micro_f1": rng(values(("taste", "micro", "f1"))),
        "meridian_exact_set_matches": rng(values(("meridian", "exact_set_matches"))),
        "meridian_micro_f1": rng(values(("meridian", "micro", "f1"))),
    }


def main() -> int:
    api_key = os.environ.get("JEV_API_KEY")
    if not api_key:
        print("ERROR: JEV_API_KEY is missing.", file=sys.stderr)
        return 2

    fixtures = load_json(FIXTURE_PATH)
    validate_fixture_schema(fixtures)

    questions = build_questions()
    assert_closed_questions(questions)

    requested_model = os.environ.get("JEV_MODEL", DEFAULT_MODEL)
    repeat_count = int(os.environ.get("JEV_REPEATS", "3"))
    if repeat_count < 1:
        raise ValueError("JEV_REPEATS must be >= 1")

    models = api_json("GET", "/v1/models", api_key)
    available = {item["name"] for item in models["models"]}
    if requested_model not in available:
        raise RuntimeError(
            f"Requested model alias {requested_model!r} is unavailable. Available models: {sorted(available)}"
        )

    repeats = [
        run_once(fixtures, questions, api_key, requested_model, idx)
        for idx in range(1, repeat_count + 1)
    ]

    actual_models = {r["actual_model"] for r in repeats}
    result = {
        "run_timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "prompt_version": PROMPT_VERSION,
        "fixture_version": fixtures["fixture_version"],
        "requested_model": requested_model,
        "actual_models": sorted(actual_models),
        "closed_output_schema": fixtures["output_schema"],
        "noul_scoring_threshold": THRESHOLD,
        "classification_policy": "Forced closed-schema classification; no abstention.",
        "probability_policy": "Native Jev probabilities stored unchanged; no post-hoc calibration transform.",
        "repeats": repeats,
        "stability": aggregate_ranges(repeats),
    }

    RESULTS_PATH.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print(json.dumps(result["stability"], ensure_ascii=False, indent=2))
    for repeat in repeats:
        print(f"repeat {repeat['repeat_index']}:")
        print(json.dumps(repeat["summary"], ensure_ascii=False, indent=2))
    print(f"Results written to {RESULTS_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
