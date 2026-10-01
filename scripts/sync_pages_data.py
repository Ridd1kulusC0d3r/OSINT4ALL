#!/usr/bin/env python3
import argparse
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/"data"/"resources.json"
DST=ROOT/"docs"/"data"/"resources.json"

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--check",action="store_true")
    args=ap.parse_args()
    content=SRC.read_text(encoding="utf-8")
    if args.check:
        current=DST.read_text(encoding="utf-8") if DST.exists() else ""
        if current != content:
            raise SystemExit("docs/data/resources.json is stale. Run: python scripts/sync_pages_data.py")
        print("OK: GitHub Pages data mirror is current.")
        return
    DST.parent.mkdir(parents=True,exist_ok=True)
    DST.write_text(content,encoding="utf-8")
    print(f"Wrote {DST}")

if __name__=="__main__":
    main()
