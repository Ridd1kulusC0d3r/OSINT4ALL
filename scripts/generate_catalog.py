#!/usr/bin/env python3
import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "resources.json"
OUT = ROOT / "catalog" / "INDEX.generated.md"

def render():
    payload = json.loads(DATA.read_text(encoding="utf-8"))
    resources = sorted(payload["resources"], key=lambda r: r["name"].casefold())

    by_domain = defaultdict(list)
    jurisdiction_counts = Counter()

    for r in resources:
        for domain in r["domains"]:
            by_domain[domain].append(r)
        for jurisdiction in r["jurisdictions"]:
            jurisdiction_counts[jurisdiction] += 1

    lines = [
        "# Generated Resource Index",
        "",
        "> Generated from `data/resources.json`. Do not edit manually.",
        "",
        f"**Catalog version:** {payload['catalog_version']}  ",
        f"**Resources:** {len(resources)}",
        "",
        "## Jurisdiction coverage",
        "",
        "| Jurisdiction | Resources |",
        "|---|---:|",
    ]

    for jurisdiction, count in sorted(jurisdiction_counts.items()):
        lines.append(f"| {jurisdiction} | {count} |")

    lines += ["", "## By domain", ""]

    for domain in sorted(by_domain):
        lines += [f"### {domain}", "", "| Resource | Jurisdiction | Disciplines | Access | Status |", "|---|---|---|---|---|"]
        for r in by_domain[domain]:
            name = f"[{r['name']}]({r['canonical_url']})"
            lines.append(
                f"| {name} | {', '.join(r['jurisdictions'])} | {', '.join(r['disciplines'])} | "
                f"{r['access']} | {r['status']} |"
            )
        lines.append("")

    lines += [
        "## Status policy",
        "",
        "AI-assisted imports default to **needs-review**. Promotion to **verified** requires a human validation date.",
        ""
    ]
    return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Fail if generated index is stale")
    args = parser.parse_args()
    rendered = render()

    if args.check:
        current = OUT.read_text(encoding="utf-8") if OUT.exists() else ""
        if current != rendered:
            raise SystemExit("catalog/INDEX.generated.md is stale. Run: python scripts/generate_catalog.py")
        print("OK: generated catalog index is current.")
        return

    OUT.write_text(rendered, encoding="utf-8")
    print(f"Wrote {OUT}")

if __name__ == "__main__":
    main()
