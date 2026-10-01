# Confidence Scales — Never Mix Them

OSINT systems love producing numbers. Humans then average unrelated numbers because spreadsheets permit crimes against semantics.

OSINT4ALL separates four scales:

| Scale | Values | Meaning |
|---|---|---|
| Resource validation | verified / needs-review / changed / broken-unsafe / historical | State of the catalogue entry |
| Observation confidence | low / medium / high | Ordinal confidence in one extraction/observation |
| Resolution similarity | 0..1 | Similarity score used to prioritize human identity/entity review |
| Analytical confidence | low / medium / high + rationale | Confidence in an analyst assessment |

## Rules

1. A resolution score of `0.82` does **not** mean an 82% probability that two entities are the same.
2. Observation confidence does not prove source reliability.
3. A verified tool can return weak evidence.
4. A needs-review resource can still expose a true primary-source fact.
5. Analytical confidence must cite supporting and contradicting evidence.
6. Never average these scales.

Machine-readable definitions live in `data/taxonomies.json`.
