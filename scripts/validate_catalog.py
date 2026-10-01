#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "resources.json"
TAXONOMY = ROOT / "data" / "taxonomies.json"

ID_RE = re.compile(r"^[a-z0-9][a-z0-9-]+$")
TAG_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")
JUR_RE = re.compile(r"^(GLOBAL|[A-Z]{2}(-[A-Z0-9]{1,3})?)$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

def fail(errors):
    for item in errors:
        print(f"ERROR: {item}", file=sys.stderr)
    sys.exit(1)

def main():
    payload = json.loads(DATA.read_text(encoding="utf-8"))
    taxonomy = json.loads(TAXONOMY.read_text(encoding="utf-8"))
    resources = payload.get("resources")
    errors = []
    if not isinstance(resources, list) or not resources:
        fail(["resources must be a non-empty list"])

    allowed_disciplines = set(taxonomy["disciplines"])
    allowed_status = set(taxonomy["statuses"])
    allowed_source_types = set(taxonomy["source_types"])
    allowed_access = set(taxonomy["access_models"])
    allowed_inputs = set(taxonomy.get("target_inputs", []))
    allowed_impl = set(taxonomy.get("implementation_types", []))
    allowed_outputs = set(taxonomy.get("output_types", []))
    allowed_authority = set(taxonomy.get("authority_scopes", []))
    allowed_interfaces = set(taxonomy.get("interface_modes", []))
    allowed_network = set(taxonomy.get("network_modes", []))
    allowed_handling = set(taxonomy.get("data_handling_modes", []))
    allowed_execution = set(taxonomy.get("execution_classes", []))
    allowed_local_inputs = {
        country + ":" + value
        for country, values in taxonomy.get("jurisdiction_inputs", {}).items()
        for value in values
    }

    ids, urls = set(), set()
    for index, r in enumerate(resources, start=1):
        prefix = f"resource[{index}]"
        required = [
            "id","name","canonical_url","jurisdictions","disciplines","domains",
            "use_cases","source_type","access","languages","status","last_verified","catalog_added"
        ]
        for key in required:
            if key not in r:
                errors.append(f"{prefix}: missing {key}")

        rid = r.get("id", "")
        if not ID_RE.match(rid):
            errors.append(f"{prefix}: invalid id {rid!r}")
        if rid in ids:
            errors.append(f"{prefix}: duplicate id {rid}")
        ids.add(rid)

        url = r.get("canonical_url", "")
        parsed = urlparse(url)
        if parsed.scheme != "https" or not parsed.netloc:
            errors.append(f"{prefix}: canonical_url must be absolute HTTPS")
        normalized = url.rstrip("/").lower()
        if normalized in urls:
            errors.append(f"{prefix}: duplicate canonical_url {url}")
        urls.add(normalized)

        jurisdictions = r.get("jurisdictions", [])
        if not jurisdictions or any(not JUR_RE.match(x) for x in jurisdictions):
            errors.append(f"{prefix}: invalid jurisdiction list")

        for field in ("disciplines","domains","use_cases","languages"):
            value = r.get(field, [])
            if not isinstance(value, list) or not value or len(value) != len(set(value)):
                errors.append(f"{prefix}: {field} must be a non-empty unique list")

        unknown_disciplines = set(r.get("disciplines", [])) - allowed_disciplines
        if unknown_disciplines:
            errors.append(f"{prefix}: unknown disciplines: {sorted(unknown_disciplines)}")

        for field in ("domains", "use_cases"):
            for value in r.get(field, []):
                if not TAG_RE.match(value):
                    errors.append(f"{prefix}: {field} value must be kebab-case: {value!r}")

        inputs = r.get("target_inputs")
        if inputs is not None:
            if not isinstance(inputs, list) or not inputs or len(inputs) != len(set(inputs)):
                errors.append(f"{prefix}: target_inputs must be a non-empty unique list when present")
            else:
                unknown = set(inputs) - allowed_inputs
                if unknown:
                    errors.append(f"{prefix}: unknown target_inputs: {sorted(unknown)}")

        local_inputs = r.get("jurisdiction_inputs")
        if local_inputs is not None:
            if not isinstance(local_inputs, list) or not local_inputs or len(local_inputs) != len(set(local_inputs)):
                errors.append(f"{prefix}: jurisdiction_inputs must be a non-empty unique list when present")
            else:
                unknown = set(local_inputs) - allowed_local_inputs
                if unknown:
                    errors.append(f"{prefix}: unknown jurisdiction_inputs: {sorted(unknown)}")

        outputs = r.get("output_types")
        if outputs is not None:
            if not isinstance(outputs, list) or len(outputs) != len(set(outputs)):
                errors.append(f"{prefix}: output_types must be a unique list")
            else:
                unknown = set(outputs) - allowed_outputs
                if unknown:
                    errors.append(f"{prefix}: unknown output_types: {sorted(unknown)}")

        impl = r.get("implementation_type")
        if impl is not None and impl not in allowed_impl:
            errors.append(f"{prefix}: unknown implementation_type {impl!r}")

        interfaces = r.get("interfaces")
        if interfaces is not None:
            if not isinstance(interfaces, list) or not interfaces or len(interfaces) != len(set(interfaces)):
                errors.append(f"{prefix}: interfaces must be a non-empty unique list when present")
            else:
                unknown = set(interfaces) - allowed_interfaces
                if unknown:
                    errors.append(f"{prefix}: unknown interfaces: {sorted(unknown)}")

        if r.get("network_mode") is not None and r["network_mode"] not in allowed_network:
            errors.append(f"{prefix}: invalid network_mode")
        if r.get("data_handling") is not None and r["data_handling"] not in allowed_handling:
            errors.append(f"{prefix}: invalid data_handling")
        if r.get("execution_class") is not None and r["execution_class"] not in allowed_execution:
            errors.append(f"{prefix}: invalid execution_class")
        if r.get("human_review_required") is not None and not isinstance(r["human_review_required"], bool):
            errors.append(f"{prefix}: human_review_required must be boolean")

        authority = r.get("authority_scope")
        if authority is not None and authority not in allowed_authority:
            errors.append(f"{prefix}: unknown authority_scope {authority!r}")

        refs = r.get("upstream_refs")
        if refs is not None:
            if not isinstance(refs, list) or len(refs) != len(set(refs)):
                errors.append(f"{prefix}: upstream_refs must be a unique list")
            elif any(not ID_RE.match(x) for x in refs):
                errors.append(f"{prefix}: upstream_refs values must be canonical IDs")

        if r.get("status") not in allowed_status:
            errors.append(f"{prefix}: invalid status")
        if r.get("source_type") not in allowed_source_types:
            errors.append(f"{prefix}: invalid source_type")
        if r.get("access") not in allowed_access:
            errors.append(f"{prefix}: invalid access")

        verified = r.get("last_verified")
        if r.get("status") == "verified" and not verified:
            errors.append(f"{prefix}: verified resources require last_verified")
        if verified is not None and not DATE_RE.match(verified):
            errors.append(f"{prefix}: last_verified must be YYYY-MM-DD or null")
        if not DATE_RE.match(r.get("catalog_added", "")):
            errors.append(f"{prefix}: catalog_added must be YYYY-MM-DD")
        if r.get("last_release") is not None and not DATE_RE.match(r["last_release"]):
            errors.append(f"{prefix}: last_release must be YYYY-MM-DD")

    if errors:
        fail(errors)

    with_inputs = sum(1 for r in resources if r.get("target_inputs"))
    with_local = sum(1 for r in resources if r.get("jurisdiction_inputs"))
    with_interfaces = sum(1 for r in resources if r.get("interfaces"))
    print(
        f"OK: {len(resources)} resources validated; {with_inputs} have target-input metadata; "
        f"{with_local} use jurisdiction-specific identifiers; {with_interfaces} declare interfaces; IDs/URLs unique."
    )

if __name__ == "__main__":
    main()
