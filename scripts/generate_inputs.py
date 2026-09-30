#!/usr/bin/env python3
import argparse
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "resources.json"
OUT = ROOT / "catalog" / "INPUTS.generated.md"

def render():
    payload = json.loads(DATA.read_text(encoding="utf-8"))
    grouped = defaultdict(list)
    missing = []

    for resource in payload["resources"]:
        inputs = resource.get("target_inputs")
        if not inputs:
            missing.append(resource)
            continue
        for target_input in inputs:
            grouped[target_input].append(resource)

    lines = [
        "# Resources by Target Input",
        "",
        "> Generated from `data/resources.json`. Input coverage is incremental and does not yet include every resource.",
        "",
        f"**Catalog version:** {payload['catalog_version']}  ",
        f"**Resources with target-input metadata:** {sum(len(v) for v in [ [r for r in payload['resources'] if r.get('target_inputs')] ])}  ",
        f"**Resources still needing input classification:** {len(missing)}",
        "",
    ]

    for target_input in sorted(grouped):
        lines += [
            f"## {target_input}",
            "",
            "| Resource | Type | Jurisdiction | Domains | Status |",
            "|---|---|---|---|---|",
        ]
        for r in sorted(grouped[target_input], key=lambda x: x["name"].casefold()):
            lines.append(
                f"| [{r['name']}]({r['canonical_url']}) | {r.get('implementation_type','—')} | "
                f"{', '.join(r['jurisdictions'])} | {', '.join(r['domains'])} | {r['status']} |"
            )
        lines.append("")

    lines += [
        "## Why target input matters",
        "",
        "Analysts usually begin with an observable: a username, email, domain, image, document, location, repository URL or other concrete artifact. "
        "Input-oriented discovery lets the analyst start from what they actually have instead of guessing which category contains the right tool.",
        ""
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
            raise SystemExit("catalog/INPUTS.generated.md is stale. Run: python scripts/generate_inputs.py")
        print("OK: generated target-input index is current.")
        return

    OUT.write_text(rendered, encoding="utf-8")
    print(f"Wrote {OUT}")

if __name__ == "__main__":
    main()
