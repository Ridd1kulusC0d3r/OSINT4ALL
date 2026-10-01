# Lifecycle Intelligence

OSINT4ALL applies intelligence lifecycle ideas to the catalogue itself.

## Signals

- upstream HEAD changed;
- repository archived/unarchived;
- default branch changed;
- canonical link changed;
- link health changed;
- resource promoted, changed or marked historical;
- new project enters the emerging watchlist.

## Baseline

Tracked upstream heads live in `data/upstream-snapshots.json`.

The scheduled workflow runs `scripts/check_upstreams.py` and publishes an artifact report. It deliberately does not auto-promote or auto-delete resources.

## Why human review remains required

A commit can fix documentation, introduce a breaking rewrite, change ownership, or do nothing relevant to analysts. Automation detects **change**; curation determines **meaning**.

## Next stage

Planned lifecycle intelligence should add release/tag monitoring, maintenance scoring, source-level diffing for structured upstream datasets, and review SLAs for stale entries.
