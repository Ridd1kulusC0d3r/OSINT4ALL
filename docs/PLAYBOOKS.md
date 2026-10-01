# Evidence-First Source-Selection Playbooks

Inspired by OpenOSINT's declarative recipes, OSINT4ALL playbooks deliberately stop **before target execution**.

Each playbook defines:

- accepted input classes;
- jurisdiction;
- resource filters;
- evidence requirement for every stage;
- stop condition;
- prohibited automation.

Current playbooks:

| Playbook | Focus |
|---|---|
| `domain` | Domain context, web history and preservation |
| `organization` | Corporate/public-record research |
| `document` | Safe file/document intelligence |
| `image-geolocation` | Media verification and GEOINT |
| `cti-indicator` | Defensive CTI enrichment |
| `br-company` | Brazil company/CNPJ-oriented source planning |

Use the read-only router:

```bash
python scripts/osint4all_router.py --playbook domain
python scripts/osint4all_router.py --input domain --status verified
python scripts/osint4all_router.py --local-input BR:cnpj --jurisdiction BR
```

The router receives **metadata classes**, not target values. It never queries the network.
