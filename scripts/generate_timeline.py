#!/usr/bin/env python3
import argparse
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HISTORY = ROOT / "data" / "history.json"
RESOURCES = ROOT / "data" / "resources.json"
OUT = ROOT / "catalog" / "TIMELINE.generated.md"

def render():
    history = json.loads(HISTORY.read_text(encoding="utf-8"))
    payload = json.loads(RESOURCES.read_text(encoding="utf-8"))
    counts = Counter(r["catalog_added"] for r in payload["resources"])

    lines = [
        "# OSINT4ALL Catalogue Timeline",
        "",
        "> Generated from `data/history.json` and `data/resources.json`.",
        "",
        "## Project evolution",
        "",
        "| Date | Version | Event | Detail |",
        "|---|---|---|---|",
    ]
    for event in history["events"]:
        lines.append("| {} | {} | {} | {} |".format(
            event["date"], event["version"], event["event"], event["detail"]
        ))

    lines += ["", "## Resource additions", "", "| Date | Resources added |", "|---|---:|"]
    for date in sorted(counts):
        lines.append("| {} | {} |".format(date, counts[date]))
    lines += [
        "",
        "Future additions will retain their own `catalog_added` date so the catalogue can be reconstructed chronologically.",
        "",
    ]
    return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    rendered = render()
    if args.check:
        current = OUT.read_text(encoding="utf-8") if OUT.exists() else ""
        if current != rendered:
            raise SystemExit("catalog/TIMELINE.generated.md is stale")
        print("OK: catalogue timeline is current.")
        return
    OUT.write_text(rendered, encoding="utf-8")

if __name__ == "__main__":
    main()
