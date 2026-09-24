#!/usr/bin/env python3
"""Freeze ten tea/coffee stage-2 summaries and preserve exact pre-Jev snapshots."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ENTRY_IDS = [
    "cold-brew-tea", "sparkling-tea", "espresso", "americano", "hand-pour-coffee",
    "cold-brew-coffee", "nitro-cold-brew", "latte", "cappuccino", "mocha",
]
MANIFEST = ROOT / "qa/tea-coffee-summary-sha256.txt"
SNAPSHOT_DIR = ROOT / "qa/jev-tea-coffee-batch/pre-freeze"


def main() -> None:
    lines = []
    SNAPSHOT_DIR.mkdir(parents=True, exist_ok=True)
    for entry_id in ENTRY_IDS:
        relative = f"references/entries/{entry_id}/summary.md"
        path = ROOT / relative
        raw = path.read_bytes()
        digest = hashlib.sha256(raw).hexdigest()
        text = raw.decode("utf-8")
        lines.append(f"{digest}  {relative}")
        snapshot = {
            "entry_id": entry_id,
            "summary_ref": relative,
            "summary_sha256": digest,
            "reasoning_version": "jev-tcm-reasoning-v0.4",
            "five_shot_version": "jev-tcm-pilot-fixtures-v0.4",
            "snapshot_date": "2026-09-24",
            "summary_text": text,
        }
        (SNAPSHOT_DIR / f"{entry_id}.json").write_text(
            json.dumps(snapshot, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
    MANIFEST.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Froze {len(ENTRY_IDS)} summary snapshots.")


if __name__ == "__main__":
    main()
