#!/usr/bin/env python3
"""Domain-transfer test for Jev v0.4 dominant yin/yang direction Choices."""

from __future__ import annotations

import importlib.util
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
V04_RUNNER = ROOT / "run_pilot_v04.py"
V04_FIXTURES = ROOT / "fixtures-v0.4.json"
DOMAIN_FIXTURES = ROOT / "domain-transfer-fixtures-v0.1.json"
RESULTS_PATH = ROOT / "domain-transfer-results-v0.4.json"
THRESHOLD = 0.5


def load_module(path: Path):
    spec = importlib.util.spec_from_file_location("jev_v04", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot import runner: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def assert_no_boundary_leakage(state: str, domain: dict[str, Any]) -> None:
    for phrase in ["M-0", "M-IV", "M-II", "暂不归经", "dossier_boundary"]:
        if phrase in state:
            raise AssertionError(f"Boundary/result phrase leaked into state: {phrase}")
    for case in domain["test_cases"]:
        dossier = case["meta"]["dossier"]
        if dossier in state:
            raise AssertionError(f"Dossier path leaked into state: {dossier}")


def case_summary(v04, answers: dict[str, Any]) -> dict[str, Any]:
    base = v04.load_module(v04.BASE_RUNNER)
    tastes, meridians = base.labels_from_answers(answers)

    meridian_details = {}
    for meridian, slug in base.MERIDIAN_KEY.items():
        meridian_details[meridian] = {
            "score": answers[f"meridian_{slug}"]["noul"],
            "direction": answers[f"{slug}_direction"]["choice"],
            "direction_probabilities": answers[f"{slug}_direction"]["probabilities"],
            "primary_meridian_at_0_5": answers[f"meridian_{slug}"]["noul"] >= THRESHOLD,
        }

    return {
        "qi": {
            "choice": answers["qi"]["choice"],
            "probabilities": answers["qi"]["probabilities"],
        },
        "tastes_at_0_5": tastes,
        "meridians_at_0_5": meridians,
        "meridians": meridian_details,
    }


def main() -> int:
    api_key = os.environ.get("JEV_API_KEY")
    if not api_key:
        print("ERROR: JEV_API_KEY is missing.", file=sys.stderr)
        return 2

    v04 = load_module(V04_RUNNER)
    base = v04.load_module(v04.BASE_RUNNER)
    fixtures = load_json(V04_FIXTURES)
    domain = load_json(DOMAIN_FIXTURES)
    questions = v04.build_questions(base)

    requested_model = os.environ.get("JEV_MODEL", base.DEFAULT_MODEL)
    repeat_count = int(os.environ.get("JEV_REPEATS", "3"))

    models = base.api_json("GET", "/v1/models", api_key)
    available = {item["name"] for item in models["models"]}
    if requested_model not in available:
        raise RuntimeError(
            f"Requested model alias {requested_model!r} unavailable. Available: {sorted(available)}"
        )

    repeats = []
    actual_models: set[str] = set()

    for repeat_index in range(1, repeat_count + 1):
        cases = []
        for case in domain["test_cases"]:
            state = v04.build_state(fixtures, case)
            assert_no_boundary_leakage(state, domain)

            response = base.api_json(
                "POST",
                "/v1/systemone",
                api_key,
                {"state": state, "model": requested_model, "questions": questions},
            )
            v04.validate_answers(base, response["answers"])
            actual_models.add(response["model"])

            cases.append(
                {
                    "sample_id": case["sample_id"],
                    "food": case["meta"]["food"],
                    "summary": case_summary(v04, response["answers"]),
                    "native_answers": response["answers"],
                    "usage": response["usage"],
                }
            )
        repeats.append({"repeat_index": repeat_index, "cases": cases})

    result = {
        "run_timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "experiment_version": "jev-food-domain-transfer-v0.4",
        "prompt_version": v04.PROMPT_VERSION,
        "requested_model": requested_model,
        "actual_models": sorted(actual_models),
        "repeat_count": repeat_count,
        "architecture": "semantic cascade; computationally synchronous",
        "scoring_policy": "No gold accuracy. Preserve native Jev outputs and compare to dossier boundaries.",
        "cases": [
            {
                "sample_id": c["sample_id"],
                "food": c["meta"]["food"],
                "dossier": c["meta"]["dossier"],
                "dossier_boundary": c["dossier_boundary"],
                "document": c["document"],
            }
            for c in domain["test_cases"]
        ],
        "repeats": repeats,
    }

    RESULTS_PATH.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    for repeat in repeats:
        print(f"repeat {repeat['repeat_index']}:")
        for case in repeat["cases"]:
            primary = {
                m: f"{d['score']:.2f}/{d['direction']}"
                for m, d in case["summary"]["meridians"].items()
                if d["primary_meridian_at_0_5"]
            }
            print(
                json.dumps(
                    {
                        "food": case["food"],
                        "qi": case["summary"]["qi"]["choice"],
                        "tastes": case["summary"]["tastes_at_0_5"],
                        "primary_meridians": primary,
                    },
                    ensure_ascii=False,
                )
            )
    print(f"Results written to {RESULTS_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
