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

    ids, urls = set(), set()

    for index, r in enumerate(resources, start=1):
        prefix = f"resource[{index}]"
        required = [
            "id","name","canonical_url","jurisdictions","disciplines","domains",
            "use_cases","source_type","access","languages","status","last_verified"
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
                unknown_inputs = set(inputs) - allowed_inputs
                if unknown_inputs:
                    errors.append(f"{prefix}: unknown target_inputs: {sorted(unknown_inputs)}")

        impl = r.get("implementation_type")
        if impl is not None and impl not in allowed_impl:
            errors.append(f"{prefix}: unknown implementation_type {impl!r}")

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
        if verified is not None and not re.match(r"^\d{4}-\d{2}-\d{2}$", verified):
            errors.append(f"{prefix}: last_verified must be YYYY-MM-DD or null")

    if errors:
        fail(errors)

    with_inputs = sum(1 for r in resources if r.get("target_inputs"))
    print(
        f"OK: {len(resources)} resources validated; {with_inputs} have target-input metadata; "
        "IDs/URLs unique; taxonomies canonical."
    )

if __name__ == "__main__":
    main()
