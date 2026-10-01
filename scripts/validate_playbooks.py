#!/usr/bin/env python3
import json
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
TAX=json.loads((ROOT/"data"/"taxonomies.json").read_text(encoding="utf-8"))
PLAYBOOKS=ROOT/"playbooks"
errors=[]

allowed_inputs=set(TAX["target_inputs"])
allowed_local={c+":"+v for c,vals in TAX.get("jurisdiction_inputs",{}).items() for v in vals}
allowed_disc=set(TAX["disciplines"])
allowed_status=set(TAX["statuses"])
allowed_exec=set(TAX["execution_classes"])

for path in sorted(PLAYBOOKS.glob("*.json")):
    p=json.loads(path.read_text(encoding="utf-8"))
    for key in ("name","label","version","purpose","target_inputs","steps","safety"):
        if key not in p: errors.append(f"{path.name}: missing {key}")
    if p.get("name") != path.stem: errors.append(f"{path.name}: name must equal filename")
    ids=set()
    for step in p.get("steps",[]):
        sid=step.get("id")
        if not sid or sid in ids: errors.append(f"{path.name}: duplicate/missing step id {sid!r}")
        ids.add(sid)
        if "tool" in step or "target" in step or "target_value" in step:
            errors.append(f"{path.name}/{sid}: playbooks may select resources but must not execute targets")
        f=step.get("resource_filters",{})
        unknown=set(f.get("target_inputs",[]))-allowed_inputs
        if unknown: errors.append(f"{path.name}/{sid}: unknown target_inputs {sorted(unknown)}")
        unknown=set(f.get("jurisdiction_inputs",[]))-allowed_local
        if unknown: errors.append(f"{path.name}/{sid}: unknown jurisdiction_inputs {sorted(unknown)}")
        unknown=set(f.get("disciplines",[]))-allowed_disc
        if unknown: errors.append(f"{path.name}/{sid}: unknown disciplines {sorted(unknown)}")
        unknown=set(f.get("statuses",[]))-allowed_status
        if unknown: errors.append(f"{path.name}/{sid}: unknown statuses {sorted(unknown)}")
        unknown=set(f.get("execution_classes",[]))-allowed_exec
        if unknown: errors.append(f"{path.name}/{sid}: unknown execution_classes {sorted(unknown)}")

if errors:
    print("\n".join("ERROR: "+e for e in errors),file=sys.stderr)
    raise SystemExit(1)
print(f"OK: {len(list(PLAYBOOKS.glob('*.json')))} playbooks validated.")
