#!/usr/bin/env python3
"""Domain-transfer test: existing food dossiers -> frozen Jev v0.3.1 judge.

No gold scoring. This runner imports the frozen v0.3.1 reasoning rules/questions
instead of copying them, then records repeatability and native probabilities.
"""

from __future__ import annotations

import importlib.util
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
FROZEN_RUNNER = ROOT / "run_pilot_v031.py"
FROZEN_FIXTURES = ROOT / "fixtures-v0.3.1.json"
DOMAIN_FIXTURES = ROOT / "domain-transfer-fixtures-v0.1.json"
RESULTS_PATH = ROOT / "domain-transfer-results-v0.1.json"

REPEAT_COUNT_DEFAULT = 3
THRESHOLD = 0.5


def load_module(path: Path):
    spec = importlib.util.spec_from_file_location("jev_v031_frozen", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot import frozen runner: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def build_state(frozen, reference_examples: list[dict[str, Any]], case: dict[str, Any]) -> str:
    fixtures = {"reference_examples": reference_examples}
    return f"""# 判定方法

{frozen.REASONING_RULES}

# 参考示例

{frozen.render_examples(fixtures)}

# 待判断说明文档

{case["document"]}
"""


def assert_no_identity_or_boundary_leakage(state: str, domain: dict[str, Any]) -> None:
    forbidden_phrases = [
        "M-0",
        "M-IV",
        "M-II",
        "暂不归经",
        "dossier_boundary",
    ]
    for phrase in forbidden_phrases:
        if phrase in state:
            raise AssertionError(f"Boundary/result phrase leaked into state: {phrase}")

    for case in domain["test_cases"]:
        dossier = case["meta"]["dossier"]
        if dossier in state:
            raise AssertionError(f"Dossier path leaked into state: {dossier}")


def summarize_case(repeat_cases: list[dict[str, Any]], frozen) -> dict[str, Any]:
    qi_choices = [x["answers"]["qi"]["choice"] for x in repeat_cases]
    qi_probs: dict[str, list[float]] = {q: [] for q in frozen.QI_VALUES}
    for x in repeat_cases:
        for q, p in x["answers"]["qi"]["probabilities"].items():
            qi_probs[q].append(float(p))

    taste_probs: dict[str, list[float]] = {taste: [] for taste in frozen.TASTE_KEY}
    for x in repeat_cases:
        for taste, slug in frozen.TASTE_KEY.items():
            taste_probs[taste].append(float(x["answers"][f"taste_{slug}"]["noul"]))

    meridian_probs: dict[str, list[float]] = {m: [] for m in frozen.MERIDIAN_KEY}
    for x in repeat_cases:
        for m, slug in frozen.MERIDIAN_KEY.items():
            meridian_probs[m].append(float(x["answers"][f"meridian_{slug}"]["noul"]))

    def ranges(values: dict[str, list[float]]) -> dict[str, Any]:
        return {
            k: {
                "values": [round(v, 4) for v in xs],
                "min": round(min(xs), 4),
                "max": round(max(xs), 4),
                "crosses_0_5": min(xs) < THRESHOLD <= max(xs),
            }
            for k, xs in values.items()
        }

    tastes_by_repeat = []
    meridians_by_repeat = []
    for x in repeat_cases:
        tastes, meridians = frozen.labels_from_answers(x["answers"])
        tastes_by_repeat.append(tastes)
        meridians_by_repeat.append(meridians)

    return {
        "qi_choices": qi_choices,
        "qi_stable": len(set(qi_choices)) == 1,
        "qi_probabilities": ranges(qi_probs),
        "tastes_at_0_5_by_repeat": tastes_by_repeat,
        "taste_probabilities": ranges(taste_probs),
        "meridians_at_0_5_by_repeat": meridians_by_repeat,
        "meridian_probabilities": ranges(meridian_probs),
    }


def main() -> int:
    api_key = os.environ.get("JEV_API_KEY")
    if not api_key:
        print("ERROR: JEV_API_KEY is missing.", file=sys.stderr)
        return 2

    frozen = load_module(FROZEN_RUNNER)
    frozen_fixtures = load_json(FROZEN_FIXTURES)
    domain = load_json(DOMAIN_FIXTURES)

    if domain["frozen_prompt_version"] != frozen.PROMPT_VERSION:
        raise AssertionError(
            f"Domain fixture expects {domain['frozen_prompt_version']} "
            f"but frozen runner is {frozen.PROMPT_VERSION}"
        )

    questions = frozen.build_questions()
    requested_model = os.environ.get("JEV_MODEL", frozen.DEFAULT_MODEL)
    repeat_count = int(os.environ.get("JEV_REPEATS", str(REPEAT_COUNT_DEFAULT)))

    models = frozen.api_json("GET", "/v1/models", api_key)
    available = {item["name"] for item in models["models"]}
    if requested_model not in available:
        raise RuntimeError(
            f"Requested model alias {requested_model!r} unavailable. Available: {sorted(available)}"
        )

    all_repeats: list[dict[str, Any]] = []
    actual_models: set[str] = set()

    for repeat_index in range(1, repeat_count + 1):
        repeat_out = {
            "repeat_index": repeat_index,
            "cases": [],
        }
        for case in domain["test_cases"]:
            state = build_state(frozen, frozen_fixtures["reference_examples"], case)
            assert_no_identity_or_boundary_leakage(state, domain)

            response = frozen.api_json(
                "POST",
                "/v1/systemone",
                api_key,
                {
                    "state": state,
                    "model": requested_model,
                    "questions": questions,
                },
            )
            frozen.validate_answers(response["answers"])
            actual_models.add(response["model"])

            repeat_out["cases"].append(
                {
                    "sample_id": case["sample_id"],
                    "answers": response["answers"],
                    "usage": response["usage"],
                }
            )
        all_repeats.append(repeat_out)

    if len(actual_models) != 1:
        raise AssertionError(f"Multiple actual models returned: {sorted(actual_models)}")

    cases_summary: list[dict[str, Any]] = []
    for case in domain["test_cases"]:
        sample_id = case["sample_id"]
        repeat_cases = []
        for repeat in all_repeats:
            found = next(x for x in repeat["cases"] if x["sample_id"] == sample_id)
            repeat_cases.append(found)

        cases_summary.append(
            {
                "sample_id": sample_id,
                "food": case["meta"]["food"],
                "dossier": case["meta"]["dossier"],
                "document": case["document"],
                "dossier_boundary": case["dossier_boundary"],
                "jev": summarize_case(repeat_cases, frozen),
            }
        )

    result = {
        "run_timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "experiment_version": domain["fixture_version"],
        "frozen_prompt_version": frozen.PROMPT_VERSION,
        "frozen_fixture_version": frozen_fixtures["fixture_version"],
        "requested_model": requested_model,
        "actual_model": next(iter(actual_models)),
        "repeat_count": repeat_count,
        "scoring_policy": "No gold accuracy. Report repeatability and compare with pre-existing dossier evidence boundaries.",
        "probability_policy": "Native Jev probabilities unchanged; 0.5 is only a reporting cut for Noul labels.",
        "cases": cases_summary,
        "raw_repeats": all_repeats,
    }

    RESULTS_PATH.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    compact = []
    for item in cases_summary:
        compact.append(
            {
                "sample_id": item["sample_id"],
                "food": item["food"],
                "qi": item["jev"]["qi_choices"],
                "tastes": item["jev"]["tastes_at_0_5_by_repeat"],
                "meridians": item["jev"]["meridians_at_0_5_by_repeat"],
            }
        )

    print(json.dumps(compact, ensure_ascii=False, indent=2))
    print(f"Results written to {RESULTS_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
