#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, importlib.util, json, os, sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXP = ROOT / "experiments" / "jev-rule-fewshot-pilot"

def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch-id", required=True)
    args = ap.parse_args()
    cfg = json.loads((ROOT / "scripts" / "entry_batches" / f"{args.batch_id}.json").read_text(encoding="utf-8"))
    data, batch = cfg["entries"], cfg["batch"]
    if len(data) != 10:
        raise ValueError(f"Expected ten entries, found {len(data)}")
    key = os.environ.get("JEV_API_KEY")
    if not key:
        print("JEV_API_KEY unavailable; no Jev results were produced.", file=sys.stderr)
        return 2

    v04 = load_module(EXP / "run_pilot_v04.py", f"jev_v04_{args.batch_id.replace('-', '_')}")
    base = v04.load_module(v04.BASE_RUNNER)
    fixtures = v04.load_json(v04.FIXTURE_PATH)
    questions = v04.build_questions(base)
    model = os.environ.get("JEV_MODEL", "jev-latest")
    repeats = int(os.environ.get("JEV_REPEATS", "1"))
    if not 1 <= repeats <= 3:
        raise ValueError("JEV_REPEATS must be 1 to 3")

    manifest = ROOT / "qa" / "entry-batches" / f"{args.batch_id}-summary-sha256.txt"
    snaps = ROOT / "qa" / "jev-entry-batches" / args.batch_id / "pre-freeze"
    raw_dir = ROOT / "qa" / "jev-entry-batches" / args.batch_id / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)
    rows = []
    seen = set()
    for line in manifest.read_text(encoding="utf-8").splitlines():
        sha, ref = line.split("  ", 1)
        path = ROOT / ref
        entry_id = path.parent.name
        if entry_id not in data or entry_id in seen:
            raise ValueError(f"Unexpected or duplicate manifest entry: {entry_id}")
        seen.add(entry_id)
        if hashlib.sha256(path.read_bytes()).hexdigest() != sha:
            raise ValueError(f"Summary changed: {ref}")
        snap = json.loads((snaps / f"{entry_id}.json").read_text(encoding="utf-8"))
        text = path.read_text(encoding="utf-8")
        if snap.get("summary_sha256") != sha or snap.get("summary_text") != text:
            raise ValueError(f"Snapshot mismatch: {entry_id}")
        rows.append((entry_id, sha, path, v04.build_state(fixtures, {"document": text})))
    if len(rows) != 10 or seen != set(data):
        raise ValueError("Expected exactly ten frozen summaries")

    for entry_id, sha, path, state in rows:
        out = raw_dir / f"{entry_id}.json"
        if out.exists():
            existing = json.loads(out.read_text(encoding="utf-8"))
            answers = existing.get("runs", [{}])[0].get("native_answers", {})
            if existing.get("summary_sha256") != sha or len(existing.get("runs", [])) != 1 or len(answers) != 16:
                raise ValueError(f"Existing raw output is invalid; preserve and inspect: {out}")
            print(f"Resume: validated existing raw output for {entry_id}")
            continue
        runs = []
        for repeat in range(1, repeats + 1):
            response = base.api_json(
                "POST", "/v1/systemone", key,
                {"state": state, "model": model, "questions": questions}
            )
            v04.validate_answers(base, response["answers"])
            runs.append({
                "index": repeat,
                "actual_model": response["model"],
                "native_answers": response["answers"],
                "usage": response.get("usage"),
            })
        record = {
            "batch_id": args.batch_id,
            "entry_id": entry_id,
            "summary_ref": str(path.relative_to(ROOT)),
            "summary_sha256": sha,
            "reasoning_version": batch["reasoning_version"],
            "five_shot_version": batch["five_shot_version"],
            "requested_model": model,
            "run_timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "runs": runs,
        }
        out.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"Saved native Jev output for {entry_id}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
