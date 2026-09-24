#!/usr/bin/env python3
"""Run Jev v0.3: narrative documents + reasoning rules + five-shot."""

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
PROMPT_VERSION = "jev-tcm-rule-fewshot-v0.3"
THRESHOLD = 0.5

ROOT = Path(__file__).resolve().parent
FIXTURE_PATH = ROOT / "fixtures-v0.3.json"
RESULTS_PATH = ROOT / "results-v0.3.json"

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

REASONING_RULES = """请只根据资料说明本身进行判断。先理解整段说明所描述的证候、功能和部位关系，再判断四气、五味和五脏归经。不要把某一个词机械地直接翻译成标签。

一、总的阅读顺序

1. 从说明文档中识别三类线索：感官特征、传统功能、传统主治/症状。
2. 把主治和功能先翻译成较高一层的证候与功能群，例如热证、寒证、中焦脾胃、肺系咳喘、肝胆湿热、心神/心火、肾阳/水液等。
3. 看是否有多个线索反复指向同一方向；重复且相互一致的线索权重大于单个词。
4. 同一个症状可以同时参与不同判断。例如“黄疸”既可提示肝胆功能群，若明确属于湿热，也可同时加强寒凉方向；“呕吐吞酸”既可提示中焦脾胃，也要结合寒热上下文参与四气判断。

二、四气的推理

先判断资料主要在纠正热证还是寒证，再判断这种纠偏的强弱与深浅。

寒凉方向：
- 清热、泻火、凉血、解毒、除烦，以及高热、烦渴、血热、火毒、湿热、目赤等，支持寒凉方向。
- 若里热较深、火热较盛、血热或湿热内盛反复出现，更偏“寒”。
- 若主要是偏表、偏轻的风热、头目、咽喉热象，更偏“凉”。

温热方向：
- 散寒、温中、温经、温肺、助阳、回阳，以及冷痛、肢冷、寒饮、寒湿、五更泄泻、阳虚等，支持温热方向。
- 一般解表散寒、温中、温肺、温通，更偏“温”。
- 回阳、助阳、救逆、明显阳虚寒盛、强烈寒凝冷痛、五更泄泻等深寒表现，更偏“热”。

平：
- 资料以补益、调和、健运、利水、滋养等为主，寒热纠偏方向不突出，也没有持续强烈的寒证或热证时，更偏“平”。

入口的清凉、辛辣、温热感只能辅助，不覆盖传统功能与主治形成的整体方向。

三、五味的推理

五味同时参考感官与功能模式；入口味觉是直接线索，但传统五味不等同于字面味觉。

- 辛：常与发散、解表、行气、活血、通窍、温通等“散、行、通”的方向一致。
- 苦：常与清泄、泻火、燥湿、降逆、泄降等“清、泻、降、燥”的方向一致。
- 甘：常与补益、和中、缓急、调和、生津等“补、和、缓、生”的方向一致。
- 酸：常与收敛、固涩、生津、敛汗、止泻等“收”的方向一致。
- 咸：常与软坚、散结、润下、泻下等方向一致。

感官味与功能方向一致时互相加强；不一致时不要机械按入口味觉赋值。一种材料可以同时有多个味。

四、五脏归经的推理

不要查“症状词=某经”的单一对应表，而要先把多个症状和功能聚成脏腑功能群，再分别评估心、肝、脾、肺、肾得到多少支持。

心：
- 心悸、怔忡、胸痹心痛；
- 心烦、不寐、神志异常；
- 心火、心阳、血脉相关描述。
例如“心火亢盛、心烦不寐、心悸不宁”会形成相互加强的心系证据。

肝：
- 胸胁胀痛、情志郁滞；
- 月经、经行腹痛等疏泄相关表现；
- 目系、眩晕、筋脉；
- 黄疸、胆腑湿热等肝胆功能群；
- 厥阴相关描述。
例如“黄疸”可形成肝胆湿热方向的肝系支持，但仍需结合全文。

脾：
- 食少、腹胀、便溏、泄泻；
- 呕吐、吞酸、脘腹不适等中焦脾胃功能群；
- 湿浊中阻、运化失常；
- 中气下陷、升举无力。
例如“呕吐、吞酸、脘腹”先识别为中焦脾胃问题，再作为脾系支持，而不是看文本中有没有“脾”字。

肺：
- 咳嗽、喘、痰、胸闷；
- 鼻、咽喉、声音；
- 外感表证、宣发肃降；
- 肺热、肺寒、肺燥等明确肺系表现。

肾：
- 腰膝、骨、生殖；
- 遗精、尿频、小便异常；
- 水肿和水液代谢；
- 阳痿、宫冷、肾阳虚；
- 五更泄泻；
- 肾不纳气一类喘证。

五、症状的双重作用

- “目赤、牙痛”首先是火热/阳亢的强度线索，可以加强寒凉判断；是否支持某一脏要看上下文。
- “呕吐吞酸”支持中焦脾胃，也会随寒热上下文参与四气判断。
- “黄疸”可支持肝胆功能群；若说明是湿热黄疸，也同时加强寒凉方向。
- “肢冷脉微”是强寒/阳虚线索；若同时出现回阳、心阳或肾阳等描述，再据上下文分配到心或肾。
"""


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
            "User-Agent": "home-materia-medica-jev-pilot/0.3",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Jev API HTTP {exc.code}: {detail}") from exc


def render_examples(fixtures: dict[str, Any]) -> str:
    chunks: list[str] = []
    for idx, demo in enumerate(fixtures["reference_examples"], start=1):
        answer = demo["answer"]
        chunks.append(
            f"""### 参考示例 {idx}

资料说明：

{demo["document"]}

标准结果：
- 四气：{answer["qi"]}
- 五味：{"、".join(answer["tastes"])}
- 五脏归经：{"、".join(answer["meridians"])}
"""
        )
    return "\n".join(chunks)


def build_state(fixtures: dict[str, Any], case: dict[str, Any]) -> str:
    return f"""# 判定方法

{REASONING_RULES}

# 参考示例

{render_examples(fixtures)}

# 待判断说明文档

{case["document"]}
"""


def build_questions() -> dict[str, Any]:
    questions: dict[str, Any] = {
        "qi": {
            "type": "choice",
            "instructions": "根据 state 中的判定方法、参考示例和待判断说明文档，判断其四气。",
            "criteria": {
                "寒": "综合说明文档后，证候与功能方向最符合寒性。",
                "凉": "综合说明文档后，证候与功能方向最符合凉性。",
                "平": "综合说明文档后，证候与功能方向最符合平性。",
                "温": "综合说明文档后，证候与功能方向最符合温性。",
                "热": "综合说明文档后，证候与功能方向最符合热性。",
            },
        }
    }

    for taste, slug in TASTE_KEY.items():
        questions[f"taste_{slug}"] = {
            "type": "noul",
            "instructions": f"根据 state 中的推理方法，判断待判断说明文档是否支持传统五味中的“{taste}”。",
            "criteria": {
                "true": f"综合感官、传统功能和主治后，支持“{taste}”。",
                "false": f"综合感官、传统功能和主治后，不支持“{taste}”。",
            },
        }

    meridian_criteria = {
        "心": "综合症状、功能和脏腑功能群后，支持心系归经。",
        "肝": "综合症状、功能和脏腑功能群后，支持肝系归经。",
        "脾": "综合症状、功能和脏腑功能群后，支持脾系归经。",
        "肺": "综合症状、功能和脏腑功能群后，支持肺系归经。",
        "肾": "综合症状、功能和脏腑功能群后，支持肾系归经。",
    }
    for meridian, slug in MERIDIAN_KEY.items():
        questions[f"meridian_{slug}"] = {
            "type": "noul",
            "instructions": f"根据 state 中的推理方法，判断待判断说明文档是否支持归“{meridian}”经。",
            "criteria": {
                "true": meridian_criteria[meridian],
                "false": f"综合症状、功能和脏腑功能群后，缺少足够支持归“{meridian}”经的线索。",
            },
        }

    return questions


def expected_answer_keys() -> set[str]:
    return (
        {"qi"}
        | {f"taste_{slug}" for slug in TASTE_KEY.values()}
        | {f"meridian_{slug}" for slug in MERIDIAN_KEY.values()}
    )


def validate_fixture_separation(fixtures: dict[str, Any]) -> None:
    demo_herbs = {d["meta"]["herb"] for d in fixtures["reference_examples"]}
    test_herbs = {c["meta"]["herb"] for c in fixtures["test_cases"]}
    overlap = demo_herbs & test_herbs
    if overlap:
        raise AssertionError(f"Few-shot/test herb overlap: {sorted(overlap)}")


def assert_no_target_leakage(state: str, fixtures: dict[str, Any]) -> None:
    for case in fixtures["test_cases"]:
        herb = case["meta"]["herb"]
        source = case["meta"]["source"]
        if herb in state:
            raise AssertionError(f"Held-out herb name leaked into Jev state: {herb}")
        if source in state:
            raise AssertionError(f"Held-out source URL leaked into Jev state: {source}")


def validate_answers(answers: dict[str, Any]) -> None:
    expected = expected_answer_keys()
    if set(answers) != expected:
        raise AssertionError(
            f"Answer keys changed. expected={sorted(expected)} actual={sorted(answers)}"
        )

    qi = answers["qi"]
    if qi.get("type") != "choice" or qi.get("choice") not in QI_VALUES:
        raise AssertionError(f"Invalid qi answer: {qi}")
    if set(qi.get("probabilities", {})) != set(QI_VALUES):
        raise AssertionError("Qi probabilities do not match the five categories.")

    for key in expected - {"qi"}:
        answer = answers[key]
        if answer.get("type") != "noul":
            raise AssertionError(f"{key} is not noul.")
        value = answer.get("noul")
        if not isinstance(value, (int, float)) or not 0 <= value <= 1:
            raise AssertionError(f"{key} noul invalid: {value}")


def labels_from_answers(answers: dict[str, Any]) -> tuple[list[str], list[str]]:
    tastes = [
        taste
        for taste, slug in TASTE_KEY.items()
        if answers[f"taste_{slug}"]["noul"] >= THRESHOLD
    ]
    meridians = [
        meridian
        for meridian, slug in MERIDIAN_KEY.items()
        if answers[f"meridian_{slug}"]["noul"] >= THRESHOLD
    ]
    return tastes, meridians


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
    total_input_tokens = total_output_tokens = 0

    for case in fixtures["test_cases"]:
        state = build_state(fixtures, case)
        assert_no_target_leakage(state, fixtures)

        response = api_json(
            "POST",
            "/v1/systemone",
            api_key,
            {"state": state, "model": requested_model, "questions": questions},
        )
        answers = response["answers"]
        validate_answers(answers)

        actual_models.add(response["model"])
        total_input_tokens += response["usage"]["input_tokens"]
        total_output_tokens += response["usage"]["output_tokens"]

        predicted_tastes, predicted_meridians = labels_from_answers(answers)
        predicted_qi = answers["qi"]["choice"]
        gold = case["gold"]

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

        cases_out.append(
            {
                "sample_id": case["sample_id"],
                "herb": case["meta"]["herb"],
                "source": case["meta"]["source"],
                "document": case["document"],
                "gold": gold,
                "predicted": {
                    "qi": predicted_qi,
                    "tastes_at_0_5": predicted_tastes,
                    "meridians_at_0_5": predicted_meridians,
                },
                "correct": {
                    "qi": qi_ok,
                    "taste_exact_set": pt == gt,
                    "meridian_exact_set": pm == gm,
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
            "qi": {"correct": qi_correct, "total": n, "accuracy": round(qi_correct / n, 4)},
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
            "usage": {"input_tokens": total_input_tokens, "output_tokens": total_output_tokens},
        },
    }


def aggregate_ranges(repeats: list[dict[str, Any]]) -> dict[str, Any]:
    def vals(*path: str) -> list[float]:
        out = []
        for repeat in repeats:
            cur: Any = repeat["summary"]
            for p in path:
                cur = cur[p]
            out.append(float(cur))
        return out

    def rng(xs: list[float]) -> dict[str, float]:
        return {"min": min(xs), "max": max(xs)}

    return {
        "n_repeats": len(repeats),
        "qi_accuracy": rng(vals("qi", "accuracy")),
        "taste_exact_set_matches": rng(vals("taste", "exact_set_matches")),
        "taste_micro_f1": rng(vals("taste", "micro", "f1")),
        "meridian_exact_set_matches": rng(vals("meridian", "exact_set_matches")),
        "meridian_micro_f1": rng(vals("meridian", "micro", "f1")),
    }


def main() -> int:
    api_key = os.environ.get("JEV_API_KEY")
    if not api_key:
        print("ERROR: JEV_API_KEY is missing.", file=sys.stderr)
        return 2

    fixtures = load_json(FIXTURE_PATH)
    validate_fixture_separation(fixtures)
    questions = build_questions()

    requested_model = os.environ.get("JEV_MODEL", DEFAULT_MODEL)
    repeat_count = int(os.environ.get("JEV_REPEATS", "3"))

    models = api_json("GET", "/v1/models", api_key)
    available = {item["name"] for item in models["models"]}
    if requested_model not in available:
        raise RuntimeError(
            f"Requested model alias {requested_model!r} unavailable. Available: {sorted(available)}"
        )

    repeats = [
        run_once(fixtures, questions, api_key, requested_model, i)
        for i in range(1, repeat_count + 1)
    ]

    result = {
        "run_timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "prompt_version": PROMPT_VERSION,
        "fixture_version": fixtures["fixture_version"],
        "reasoning_version": fixtures["reasoning_version"],
        "requested_model": requested_model,
        "actual_models": sorted({r["actual_model"] for r in repeats}),
        "state_format": "single narrative markdown string: reasoning rules + narrative five-shot + narrative target document",
        "noul_scoring_threshold": THRESHOLD,
        "probability_policy": "Native Jev probabilities unchanged; no post-hoc calibration.",
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
