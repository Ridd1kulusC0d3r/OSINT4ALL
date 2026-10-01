#!/usr/bin/env python3
import json
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
path=ROOT/"examples"/"evidence-bundle.synthetic.json"
p=json.loads(path.read_text(encoding="utf-8"))
errors=[]

entities={x["entity_id"] for x in p.get("entities",[])}
sources={x["source_id"] for x in p.get("sources",[])}
captures={x["capture_id"]:x for x in p.get("captures",[])}
statements={x["statement_id"]:x for x in p.get("statements",[])}

for s in statements.values():
    if s["entity_id"] not in entities: errors.append(f"{s['statement_id']}: unknown entity")
    if s["source_id"] not in sources: errors.append(f"{s['statement_id']}: unknown source")
    if s["capture_id"] not in captures: errors.append(f"{s['statement_id']}: unknown capture")
    elif captures[s["capture_id"]]["source_id"] != s["source_id"]:
        errors.append(f"{s['statement_id']}: capture/source mismatch")

for rel in p.get("relationships",[]):
    if rel["source_entity"] not in entities or rel["target_entity"] not in entities:
        errors.append(f"{rel['relationship_id']}: unknown entity")
    if rel["source_id"] not in sources: errors.append(f"{rel['relationship_id']}: unknown source")
    if rel["capture_id"] not in captures: errors.append(f"{rel['relationship_id']}: unknown capture")

for pr in p.get("provenance",[]):
    if pr["statement_id"] not in statements: errors.append(f"provenance: unknown statement {pr['statement_id']}")
    if pr["observation_confidence"] not in {"low","medium","high"}: errors.append("invalid observation confidence")

for r in p.get("resolution_candidates",[]):
    if r["entity_a"] not in entities or r["entity_b"] not in entities: errors.append(f"{r['candidate_id']}: unknown entity")
    if not 0 <= r["similarity_score"] <= 1: errors.append(f"{r['candidate_id']}: invalid similarity score")
    if r.get("score_semantics") != "similarity-not-probability": errors.append(f"{r['candidate_id']}: ambiguous score semantics")
    if r["judgement"] in {"positive","negative"} and r["decided_by"] != "human":
        errors.append(f"{r['candidate_id']}: final resolution requires human decision")

if errors:
    print("\n".join("ERROR: "+e for e in errors),file=sys.stderr)
    raise SystemExit(1)
print("OK: synthetic evidence bundle references, typed relationships and human-review invariants validated.")
