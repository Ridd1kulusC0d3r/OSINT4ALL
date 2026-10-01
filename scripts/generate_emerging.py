#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "emerging.json"
OUT = ROOT / "catalog" / "EMERGING.generated.md"

def render():
    payload = json.loads(DATA.read_text(encoding="utf-8"))
    rank = {"high": 0, "medium": 1, "low": 2}
    rows = sorted(payload["candidates"], key=lambda x: (rank[x["priority"]], x["name"].casefold()))
    lines = [
        "# Emerging OSINT Watchlist",
        "",
        "> Generated from `data/emerging.json`. **Watchlist ≠ recommendation.** Promotion requires direct review.",
        "",
        "**Reviewed:** {}  ".format(payload["reviewed_on"]),
        "**Candidates:** {}".format(len(rows)),
        "",
        "| Project | Priority | Source | Why watch it |",
        "|---|---|---|---|",
    ]
    for item in rows:
        lines.append("| [{}]({}) | {} | {} | {} |".format(
            item["name"], item["url"], item["priority"], item["source"], item["reason"]
        ))
    lines += [
        "",
        "## Promotion gate",
        "",
        "A project moves from watchlist to the canonical resource catalog only after direct source review, canonical-URL confirmation, capability validation, safety/legal review, taxonomy mapping and an explicit validation state.",
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
            raise SystemExit("catalog/EMERGING.generated.md is stale")
        print("OK: emerging watchlist is current.")
        return
    OUT.write_text(rendered, encoding="utf-8")

if __name__ == "__main__":
    main()
