#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch-id", required=True)
    args = ap.parse_args()
    cfg = json.loads((ROOT / "scripts" / "entry_batches" / f"{args.batch_id}.json").read_text(encoding="utf-8"))
    data = cfg["entries"]
    snaps = ROOT / "qa" / "jev-entry-batches" / args.batch_id / "pre-freeze"
    snaps.mkdir(parents=True, exist_ok=True)
    manifest = ROOT / "qa" / "entry-batches" / f"{args.batch_id}-summary-sha256.txt"
    lines = []
    for entry_id in data:
        ref = f"references/entries/{entry_id}/summary.md"
        raw = (ROOT / ref).read_bytes()
        sha = hashlib.sha256(raw).hexdigest()
        text = raw.decode("utf-8")
        lines.append(f"{sha}  {ref}")
        snap = {
            "batch_id": args.batch_id,
            "entry_id": entry_id,
            "summary_ref": ref,
            "summary_sha256": sha,
            "reasoning_version": cfg["batch"]["reasoning_version"],
            "five_shot_version": cfg["batch"]["five_shot_version"],
            "snapshot_date": cfg["batch"]["research_cutoff"],
            "summary_text": text,
        }
        (snaps / f"{entry_id}.json").write_text(
            json.dumps(snap, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
    manifest.parent.mkdir(parents=True, exist_ok=True)
    manifest.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Froze {len(data)} summaries for {args.batch_id}.")

if __name__ == "__main__":
    main()
