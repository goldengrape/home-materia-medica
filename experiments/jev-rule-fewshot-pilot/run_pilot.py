#!/usr/bin/env python3
"""Run the Jev rule + few-shot pilot for TCM property inference.

No third-party dependencies. The script:
1. loads fixtures,
2. builds a masked Jev state,
3. asserts held-out gold/name leakage is absent,
4. calls Jev once per test sample,
5. stores native probabilities unchanged,
6. scores the five held-out cases.
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
PROMPT_VERSION = "jev-tcm-rule-fewshot-v0.1"
THRESHOLD = 0.5

ROOT = Path(__file__).resolve().parent
FIXTURE_PATH = ROOT / "fixtures.json"
RESULTS_PATH = ROOT / "results.json"

QI_CRITERIA = {
    "寒": "整体证据最符合寒性；传统大寒、寒在本 pilot 统一归入此类。",
    "凉": "整体证据最符合较缓和的凉性；传统凉、微寒在本 pilot 统一归入此类。",
    "平": "整体证据最符合平性或寒热倾向不明显。",
    "温": "整体证据最符合温性；传统微温、温在本 pilot 统一归入此类。",
    "热": "整体证据最符合热性；传统热、大热在本 pilot 统一归入此类。",
    "证据不足": "现有去标签资料不足、冲突或存在同等合理解释，不能稳定归入前五类。",
}

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
    "胆": "gallbladder",
    "胃": "stomach",
    "大肠": "large_intestine",
    "小肠": "small_intestine",
    "膀胱": "bladder",
    "三焦": "triple_burner",
    "心包": "pericardium",
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
            "User-Agent": "home-materia-medica-jev-pilot/0.1",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Jev API HTTP {exc.code}: {detail}") from exc


def build_reference_examples(fixtures: dict[str, Any]) -> list[dict[str, Any]]:
    examples = []
    for demo in fixtures["reference_examples"]:
        examples.append(
            {
                "demo_id": demo["demo_id"],
                "packet": demo["packet"],
                "correct_answer": demo["answer"],
            }
        )
    return examples


def build_state(fixtures: dict[str, Any], case: dict[str, Any]) -> dict[str, Any]:
    return {
        "task": "依据《居家本草》pilot规则，从去标签资料推断四气、五味和归经。",
        "rules": [
            "只评估 target。reference_examples 只是 few-shot 示范，不是 target 的证据。",
            "不要尝试恢复被隐藏的药名，也不要把可能猜出的身份当作判断依据。",
            "四气按 pilot 五档归一：大寒/寒→寒，凉/微寒→凉，平→平，微温/温→温，热/大热→热。",
            "五味指传统本草属性，不等同于入口时的字面味觉；感官描述只能作为一项证据。",
            "五味是多标签，酸、苦、甘、辛、咸分别独立判断，可以同时成立。",
            "归经是多标签，各经分别独立判断；传统功能、主治、证候和脏腑语境可以支持，但不要只凭一个词面机械映射。",
            "资料不足、冲突或存在同等合理解释时降低概率；不要为了给出完整标签而强行肯定。",
            "输出使用 Jev 原生概率；本任务没有任何事后概率修正函数。",
        ],
        "reference_examples": build_reference_examples(fixtures),
        "target": {
            "sample_id": case["sample_id"],
            "packet": case["packet"],
        },
    }


def build_questions(fixtures: dict[str, Any]) -> dict[str, Any]:
    questions: dict[str, Any] = {
        "qi": {
            "type": "choice",
            "instructions": {
                "task": "依据 state 中规则和 few-shot，仅判断 target 的归一化四气分类。",
                "do_not": "不要评估 reference_examples 本身。",
            },
            "criteria": QI_CRITERIA,
        }
    }

    for taste in fixtures["tastes"]:
        key = f"taste_{TASTE_KEY[taste]}"
        questions[key] = {
            "type": "noul",
            "instructions": {
                "task": f"依据 state 中规则和 few-shot，target 的传统五味是否应包含“{taste}”？",
                "scope": "只评估 target；这是独立多标签判断。",
            },
            "criteria": {
                "true": f"现有资料足以支持 target 的传统五味包含“{taste}”。",
                "false": f"现有资料不支持 target 的传统五味包含“{taste}”，或更支持不包含。",
            },
        }

    for meridian in fixtures["meridians"]:
        key = f"meridian_{MERIDIAN_KEY[meridian]}"
        questions[key] = {
            "type": "noul",
            "instructions": {
                "task": f"依据 state 中规则和 few-shot，target 是否应归“{meridian}”经？",
                "scope": "只评估 target；各经独立，不要求概率和为1。",
            },
            "criteria": {
                "true": f"传统功能、主治与理论语境足以支持归“{meridian}”经。",
                "false": f"现有资料不足以支持归“{meridian}”经，或更支持不归该经。",
            },
        }

    return questions


def assert_no_leakage(state: dict[str, Any], fixtures: dict[str, Any]) -> None:
    serialized = json.dumps(state, ensure_ascii=False)

    if '"gold"' in serialized:
        raise AssertionError("Gold field leaked into Jev state.")

    for case in fixtures["test_cases"]:
        herb = case["meta"]["herb"]
        if herb in serialized:
            raise AssertionError(f"Held-out herb name leaked into Jev state: {herb}")

    for case in fixtures["test_cases"]:
        source = case["meta"]["source"]
        if source in serialized:
            raise AssertionError("Held-out source URL leaked into Jev state.")


def validate_answers(answers: dict[str, Any], fixtures: dict[str, Any]) -> None:
    expected = {"qi"}
    expected.update(f"taste_{TASTE_KEY[t]}" for t in fixtures["tastes"])
    expected.update(f"meridian_{MERIDIAN_KEY[m]}" for m in fixtures["meridians"])

    missing = expected - set(answers)
    if missing:
        raise AssertionError(f"Missing Jev answers: {sorted(missing)}")

    qi = answers["qi"]
    if qi.get("type") != "choice":
        raise AssertionError("qi answer is not choice.")
    probs = qi.get("probabilities", {})
    if set(QI_CRITERIA) - set(probs):
        raise AssertionError("qi probabilities missing criteria.")

    for key in expected - {"qi"}:
        answer = answers[key]
        if answer.get("type") != "noul":
            raise AssertionError(f"{key} answer is not noul.")
        value = answer.get("noul")
        if not isinstance(value, (int, float)) or not (0 <= value <= 1):
            raise AssertionError(f"{key} noul out of range: {value}")


def labels_from_answers(answers: dict[str, Any], fixtures: dict[str, Any]) -> tuple[list[str], list[str]]:
    tastes = [
        taste
        for taste in fixtures["tastes"]
        if answers[f"taste_{TASTE_KEY[taste]}"]["noul"] >= THRESHOLD
    ]
    meridians = [
        meridian
        for meridian in fixtures["meridians"]
        if answers[f"meridian_{MERIDIAN_KEY[meridian]}"]["noul"] >= THRESHOLD
    ]
    return tastes, meridians


def set_counts(predicted: set[str], gold: set[str]) -> tuple[int, int, int]:
    tp = len(predicted & gold)
    fp = len(predicted - gold)
    fn = len(gold - predicted)
    return tp, fp, fn


def prf(tp: int, fp: int, fn: int) -> dict[str, float]:
    precision = tp / (tp + fp) if tp + fp else 1.0
    recall = tp / (tp + fn) if tp + fn else 1.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    return {
        "precision": round(precision, 4),
        "recall": round(recall, 4),
        "f1": round(f1, 4),
    }


def main() -> int:
    api_key = os.environ.get("JEV_API_KEY")
    if not api_key:
        print("ERROR: JEV_API_KEY is missing.", file=sys.stderr)
        return 2

    fixtures = load_json(FIXTURE_PATH)
    requested_model = os.environ.get("JEV_MODEL", DEFAULT_MODEL)

    models = api_json("GET", "/v1/models", api_key)
    available = {item["name"] for item in models["models"]}
    if requested_model not in available:
        raise RuntimeError(
            f"Requested model alias {requested_model!r} is unavailable. "
            f"Available models: {sorted(available)}"
        )

    questions = build_questions(fixtures)
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
        assert_no_leakage(state, fixtures)

        payload = {
            "state": state,
            "model": requested_model,
            "questions": questions,
        }

        response = api_json("POST", "/v1/systemone", api_key, payload)
        answers = response["answers"]
        validate_answers(answers, fixtures)

        actual_models.add(response["model"])
        total_input_tokens += response["usage"]["input_tokens"]
        total_output_tokens += response["usage"]["output_tokens"]

        predicted_tastes, predicted_meridians = labels_from_answers(answers, fixtures)
        predicted_qi = answers["qi"]["choice"]

        gold = case["gold"]
        qi_ok = predicted_qi == gold["qi"]
        qi_correct += int(qi_ok)

        pred_taste_set = set(predicted_tastes)
        gold_taste_set = set(gold["tastes"])
        ttp, tfp, tfn = set_counts(pred_taste_set, gold_taste_set)
        taste_tp += ttp
        taste_fp += tfp
        taste_fn += tfn
        taste_exact += int(pred_taste_set == gold_taste_set)

        pred_meridian_set = set(predicted_meridians)
        gold_meridian_set = set(gold["meridians"])
        mtp, mfp, mfn = set_counts(pred_meridian_set, gold_meridian_set)
        meridian_tp += mtp
        meridian_fp += mfp
        meridian_fn += mfn
        meridian_exact += int(pred_meridian_set == gold_meridian_set)

        cases_out.append(
            {
                "sample_id": case["sample_id"],
                "herb": case["meta"]["herb"],
                "source": case["meta"]["source"],
                "gold": gold,
                "predicted": {
                    "qi": predicted_qi,
                    "tastes_at_0_5": predicted_tastes,
                    "meridians_at_0_5": predicted_meridians,
                },
                "correct": {
                    "qi": qi_ok,
                    "taste_exact_set": pred_taste_set == gold_taste_set,
                    "meridian_exact_set": pred_meridian_set == gold_meridian_set,
                },
                "native_answers": answers,
                "usage": response["usage"],
            }
        )

    if len(actual_models) != 1:
        raise AssertionError(f"Multiple actual models returned in one run: {sorted(actual_models)}")

    result = {
        "run_timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "prompt_version": PROMPT_VERSION,
        "fixture_version": fixtures["fixture_version"],
        "requested_model": requested_model,
        "actual_model": next(iter(actual_models)),
        "noul_scoring_threshold": THRESHOLD,
        "probability_policy": "Native Jev probabilities stored unchanged; no post-hoc calibration transform.",
        "cases": cases_out,
        "summary": {
            "n_cases": len(cases_out),
            "qi": {
                "correct": qi_correct,
                "total": len(cases_out),
                "accuracy": round(qi_correct / len(cases_out), 4),
            },
            "taste": {
                "exact_set_matches": taste_exact,
                "total": len(cases_out),
                "micro": prf(taste_tp, taste_fp, taste_fn),
                "counts": {"tp": taste_tp, "fp": taste_fp, "fn": taste_fn},
            },
            "meridian": {
                "exact_set_matches": meridian_exact,
                "total": len(cases_out),
                "micro": prf(meridian_tp, meridian_fp, meridian_fn),
                "counts": {"tp": meridian_tp, "fp": meridian_fp, "fn": meridian_fn},
            },
            "usage": {
                "input_tokens": total_input_tokens,
                "output_tokens": total_output_tokens,
            },
        },
    }

    RESULTS_PATH.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))
    print(f"Results written to {RESULTS_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
