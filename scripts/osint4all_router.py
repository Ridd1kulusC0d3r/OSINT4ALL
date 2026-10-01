#!/usr/bin/env python3
"""Read-only OSINT4ALL resource router.

This script filters catalogue metadata. It performs no network requests and
does not accept target values.
"""
import argparse
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
RESOURCES=ROOT/"data"/"resources.json"
PLAYBOOKS=ROOT/"playbooks"

def load_resources():
    return json.loads(RESOURCES.read_text(encoding="utf-8"))["resources"]

def matches(r,args):
    if args.input and args.input not in r.get("target_inputs",[]): return False
    if args.local_input and args.local_input not in r.get("jurisdiction_inputs",[]): return False
    if args.jurisdiction and args.jurisdiction not in r.get("jurisdictions",[]): return False
    if args.discipline and args.discipline not in r.get("disciplines",[]): return False
    if args.domain and args.domain not in r.get("domains",[]): return False
    if args.status and r.get("status") != args.status: return False
    if args.execution_class and r.get("execution_class") != args.execution_class: return False
    return True

def filter_for_step(resources,filters):
    def any_overlap(field):
        wanted=filters.get(field)
        if not wanted: return True
        return bool(set(wanted)&set(field_value(field)))
    def field_value(field):
        mapping={
          "target_inputs":"target_inputs",
          "jurisdiction_inputs":"jurisdiction_inputs",
          "jurisdictions":"jurisdictions",
          "disciplines":"disciplines",
          "domains":"domains"
        }
        return current.get(mapping[field],[])
    out=[]
    for current in resources:
        ok=True
        for f in ("target_inputs","jurisdiction_inputs","jurisdictions","disciplines","domains"):
            wanted=filters.get(f)
            if wanted and not (set(wanted)&set(current.get(f,[]))):
                ok=False; break
        if ok and filters.get("statuses") and current.get("status") not in filters["statuses"]: ok=False
        if ok and filters.get("execution_classes") and current.get("execution_class") not in filters["execution_classes"]: ok=False
        if ok: out.append(current)
    return out

def show_table(items):
    print("| Resource | Status | Jurisdiction | Inputs | Type |")
    print("|---|---|---|---|---|")
    for r in items:
        print("| [{}]({}) | {} | {} | {} | {} |".format(
            r["name"],r["canonical_url"],r["status"],
            ", ".join(r["jurisdictions"]),
            ", ".join(r.get("target_inputs",[]) or ["—"]),
            r.get("implementation_type","—")
        ))

def run_playbook(name,resources):
    path=PLAYBOOKS/(name+".json")
    if not path.exists(): raise SystemExit("Unknown playbook: "+name)
    p=json.loads(path.read_text(encoding="utf-8"))
    result={"playbook":p["name"],"label":p["label"],"purpose":p["purpose"],"steps":[]}
    for step in p["steps"]:
        hits=filter_for_step(resources,step.get("resource_filters",{}))
        result["steps"].append({
          "id":step["id"],"goal":step["goal"],
          "state":"success" if hits else "empty",
          "resources":[{"id":r["id"],"name":r["name"],"url":r["canonical_url"],"status":r["status"]} for r in hits],
          "evidence_requirement":step["evidence_requirement"],
          "stop_condition":step["stop_condition"]
        })
    return result

def main():
    ap=argparse.ArgumentParser(description="Filter OSINT4ALL catalogue metadata without querying targets.")
    ap.add_argument("--input")
    ap.add_argument("--local-input")
    ap.add_argument("--jurisdiction")
    ap.add_argument("--discipline")
    ap.add_argument("--domain")
    ap.add_argument("--status")
    ap.add_argument("--execution-class")
    ap.add_argument("--playbook")
    ap.add_argument("--format",choices=["table","json"],default="table")
    args=ap.parse_args()
    resources=load_resources()
    if args.playbook:
        result=run_playbook(args.playbook,resources)
        print(json.dumps(result,ensure_ascii=False,indent=2))
        return
    items=[r for r in resources if matches(r,args)]
    items.sort(key=lambda r:(r.get("status")!="verified",r["name"].casefold()))
    if args.format=="json": print(json.dumps(items,ensure_ascii=False,indent=2))
    else: show_table(items)

if __name__=="__main__":
    main()
