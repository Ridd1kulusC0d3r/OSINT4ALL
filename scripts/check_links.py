#!/usr/bin/env python3
import json
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "resources.json"
REPORT = ROOT / "artifacts" / "link-health.md"
TIMEOUT = 12

def check(url):
    headers = {"User-Agent": "OSINT4ALL-link-health/0.2 (+https://github.com/Ridd1kulusC0d3r/OSINT4ALL)"}
    req = urllib.request.Request(url, headers=headers, method="HEAD")
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            return resp.status, resp.geturl(), ""
    except urllib.error.HTTPError as exc:
        if exc.code in {403, 405, 429}:
            try:
                req = urllib.request.Request(url, headers=headers, method="GET")
                with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
                    return resp.status, resp.geturl(), ""
            except Exception as inner:
                return getattr(inner, "code", 0), url, str(inner)
        return exc.code, url, str(exc)
    except Exception as exc:
        return 0, url, str(exc)

def main():
    payload = json.loads(DATA.read_text(encoding="utf-8"))
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    rows = []
    failures = 0

    for resource in payload["resources"]:
        status, final_url, error = check(resource["canonical_url"])
        ok = 200 <= status < 400
        if not ok:
            failures += 1
        rows.append((resource["id"], status, final_url, error))
        time.sleep(0.15)

    lines = [
        "# OSINT4ALL Link Health Report",
        "",
        "This report is advisory. Some sites block automated requests, so a failure is a review signal, not proof that a resource is dead.",
        "",
        "| Resource ID | HTTP | Final URL | Result |",
        "|---|---:|---|---|",
    ]
    for rid, status, final_url, error in rows:
        result = "OK" if 200 <= status < 400 else ("REVIEW: " + error.replace("|", "\\|")[:120])
        lines.append(f"| {rid} | {status or '-'} | {final_url} | {result} |")

    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Checked {len(rows)} resources; {failures} require review.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
