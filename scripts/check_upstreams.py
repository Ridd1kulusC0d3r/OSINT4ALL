#!/usr/bin/env python3
import json
import os
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASELINE = ROOT / "data" / "upstream-snapshots.json"
REPORT = ROOT / "artifacts" / "upstream-diff.md"

def github_json(path):
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "OSINT4ALL-upstream-intelligence/0.1",
    }
    token = os.getenv("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = "Bearer " + token
    req = urllib.request.Request("https://api.github.com" + path, headers=headers)
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.load(resp)

def main():
    baseline = json.loads(BASELINE.read_text(encoding="utf-8"))
    rows = []
    changed = 0
    REPORT.parent.mkdir(parents=True, exist_ok=True)

    for item in baseline["repositories"]:
        repo = item["repo"]
        branch_name = item["branch"]
        meta = github_json("/repos/" + repo)
        branch = github_json("/repos/" + repo + "/branches/" + branch_name)
        current_sha = branch["commit"]["sha"]
        archived = bool(meta.get("archived"))
        default_branch = meta.get("default_branch")
        signals = []

        if current_sha != item["head_sha"]:
            signals.append("HEAD changed")
        if archived != item.get("archived", False):
            signals.append("archived=" + str(archived))
        if default_branch != branch_name:
            signals.append("default branch=" + str(default_branch))
        if signals:
            changed += 1

        rows.append((repo, item["head_sha"], current_sha, "; ".join(signals) or "no baseline change"))

    lines = [
        "# OSINT4ALL Upstream Intelligence Report",
        "",
        "A change is a **review signal**, not proof that the upstream became better or worse.",
        "",
        "| Upstream | Baseline | Current | Signal |",
        "|---|---|---|---|",
    ]
    for repo, old, new, signal in rows:
        lines.append("| {} | `{}` | `{}` | {} |".format(repo, old[:12], new[:12], signal))
    lines += ["", "**Repositories requiring review:** {}".format(changed), ""]
    REPORT.write_text("\n".join(lines), encoding="utf-8")
    print("Checked {} upstreams; {} changed since baseline.".format(len(rows), changed))

if __name__ == "__main__":
    main()
