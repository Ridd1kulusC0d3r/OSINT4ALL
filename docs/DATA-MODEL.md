# OSINT4ALL Data Model

Version **0.2** introduces a machine-readable canonical catalog.

## Source of truth

`data/resources.json` is the canonical structured dataset.

Human-oriented Markdown pages remain useful for explanation and methodology, but generated indexes should derive from the structured catalog whenever possible.

## Resource identity

Each resource receives a stable lowercase ID:

`<scope>-<resource-name>`

Examples:

- `global-maigret`
- `br-terrabrasilis`
- `global-opencti`

IDs should survive display-name changes when possible.

## Core fields

| Field | Purpose |
|---|---|
| `id` | Stable resource identifier |
| `name` | Human-readable canonical name |
| `canonical_url` | Preferred HTTPS URL |
| `jurisdictions` | GLOBAL, ISO alpha-2 or ISO-like subdivision tag |
| `disciplines` | OSINT, SOCMINT, GEOINT, CTI, etc. |
| `domains` | Analytical/application domains |
| `use_cases` | Tasks the resource supports |
| `source_type` | official, academic, nonprofit, commercial, community, open-source |
| `access` | free, freemium, paid, account, api-key, local or mixed |
| `languages` | Human-facing language tags |
| `status` | validation state |
| `last_verified` | human verification date or null |

## Validation philosophy

Machine validation can detect malformed IDs, duplicate URLs, missing fields and stale generated files.

It cannot determine whether a tool's marketing claim is true, whether a dataset is appropriate evidence, or whether use is lawful in a specific investigation. Those remain analyst responsibilities.

## AI-assisted content

AI-assisted imports must default to `needs-review`.

Only human review can promote an entry to `verified`, and verified entries require `last_verified`.

## Generated artifacts

`scripts/generate_catalog.py` produces:

`catalog/INDEX.generated.md`

The CI workflow fails when the generated index no longer matches the machine-readable source.

## Future extensions

Planned fields include:

- evidence/provenance URLs;
- archived URL;
- replacement resource ID;
- license;
- API availability;
- authentication requirements;
- intelligence-cycle stage;
- strategic/operational/tactical level;
- privacy sensitivity;
- legal notes;
- maintenance/activity metadata;
- aliases and former names.
