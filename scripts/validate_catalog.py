#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "resources.json"

ALLOWED_STATUS = {"verified", "needs-review", "changed", "broken-unsafe", "historical"}
ALLOWED_SOURCE_TYPES = {"official", "academic", "nonprofit", "commercial", "community", "open-source"}
ALLOWED_ACCESS = {"free", "freemium", "paid", "account", "api-key", "local", "mixed"}
ID_RE = re.compile(r"^[a-z0-9][a-z0-9-]+$")
JUR_RE = re.compile(r"^(GLOBAL|[A-Z]{2}(-[A-Z0-9]{1,3})?)$")

def fail(errors):
    for item in errors:
        print(f"ERROR: {item}", file=sys.stderr)
    sys.exit(1)

def main():
    payload = json.loads(DATA.read_text(encoding="utf-8"))
    resources = payload.get("resources")
    errors = []

    if not isinstance(resources, list) or not resources:
        fail(["resources must be a non-empty list"])

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

        if r.get("status") not in ALLOWED_STATUS:
            errors.append(f"{prefix}: invalid status")
        if r.get("source_type") not in ALLOWED_SOURCE_TYPES:
            errors.append(f"{prefix}: invalid source_type")
        if r.get("access") not in ALLOWED_ACCESS:
            errors.append(f"{prefix}: invalid access")

        verified = r.get("last_verified")
        if r.get("status") == "verified" and not verified:
            errors.append(f"{prefix}: verified resources require last_verified")

    if errors:
        fail(errors)

    print(f"OK: {len(resources)} resources validated; IDs and canonical URLs are unique.")

if __name__ == "__main__":
    main()
