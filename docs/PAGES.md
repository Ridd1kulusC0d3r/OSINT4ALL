# GitHub Pages UI

The static interface in this folder is intentionally dependency-free and performs no tracking or external JavaScript calls.

It reads `docs/data/resources.json`, which must remain byte-for-byte synchronized with the canonical `data/resources.json`.

Before committing catalogue changes:

```bash
python scripts/sync_pages_data.py
```

CI checks this mirror.

The interface provides:

- full-text search;
- jurisdiction filter;
- discipline filter;
- target-input filter;
- validation-state filter;
- execution-class filter;
- resource permalinks;
- generated catalogue statistics;
- English / Portuguese UI;
- mobile layout.

It is a **resource discovery UI**, not a target-execution console.
