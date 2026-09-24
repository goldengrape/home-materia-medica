#!/usr/bin/env python3
"""Run the current Jev v0.4 contract on ten frozen entry summaries.

Requires JEV_API_KEY. Raw responses are saved without M annotations or score edits.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPERIMENT = ROOT / "experiments/jev-rule-fewshot-pilot"
MANIFEST = ROOT / "qa/ten-entry-summary-sha256.txt"
RESULTS = ROOT / "qa/jev-ten-batch/raw"


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    key = os.environ.get("JEV_API_KEY")
    if not key:
        print("JEV_API_KEY unavailable; no Jev results were produced.", file=sys.stderr)
        return 2

    v04 = load_module(EXPERIMENT / "run_pilot_v04.py", "jev_v04_batch")
    base = v04.load_module(v04.BASE_RUNNER)
    fixtures = v04.load_json(v04.FIXTURE_PATH)
    questions = v04.build_questions(base)
    model = os.environ.get("JEV_MODEL", "jev-latest")
    repeat_count = int(os.environ.get("JEV_REPEATS", "1"))
    if not 1 <= repeat_count <= 3:
        raise ValueError("JEV_REPEATS must be 1 to 3")

    manifest = []
    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        digest, relative = line.split("  ", 1)
        summary = ROOT / relative
        actual = hashlib.sha256(summary.read_bytes()).hexdigest()
        if actual != digest:
            raise ValueError(f"Summary changed after manifest: {relative}")
        manifest.append((digest, summary))
    if len(manifest) != 10:
        raise ValueError("Expected exactly ten frozen summaries")

    # Validate all local input before the first paid API call.
    cases = [(digest, path, v04.build_state(fixtures, {"document": path.read_text(encoding="utf-8")}))
             for digest, path in manifest]
    RESULTS.mkdir(parents=True, exist_ok=True)
    for digest, path, state in cases:
        entry_id = path.parent.name
        output = RESULTS / f"{entry_id}.json"
        if output.exists():
            raise FileExistsError(f"Existing raw output; preserve it before rerunning: {output}")
        runs = []
        for index in range(1, repeat_count + 1):
            response = base.api_json("POST", "/v1/systemone", key,
                                     {"state": state, "model": model, "questions": questions})
            v04.validate_answers(base, response["answers"])
            runs.append({"index": index, "actual_model": response["model"],
                         "native_answers": response["answers"], "usage": response.get("usage")})
        record = {"entry_id": entry_id, "summary_ref": str(path.relative_to(ROOT)),
                  "summary_sha256": digest, "reasoning_version": "jev-tcm-reasoning-v0.4",
                  "five_shot_version": "jev-tcm-pilot-fixtures-v0.4", "requested_model": model,
                  "run_timestamp_utc": datetime.now(timezone.utc).isoformat(), "runs": runs}
        output.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"Saved {entry_id}: {output.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
