# OpenOSINT Architecture Review & Adoption

Reviewed upstream: [OpenOSINT/OpenOSINT](https://github.com/OpenOSINT/OpenOSINT)  
Observed release: **v2.29.0**, published 2026-09-17.

OSINT4ALL does **not** attempt to clone OpenOSINT. The projects solve different problems:

- **OpenOSINT** executes investigation tools.
- **OSINT4ALL** maps resources, jurisdictions, evidence practices and analyst workflows.

## Patterns adopted

1. **Input → capability routing** — analysts start from what they have.
2. **Declarative playbooks** — repeatable plans live in data, not hidden prompts.
3. **Bounded automation** — budgets and stopping conditions must be explicit.
4. **Explicit step state** — success, empty, error and not-configured are different outcomes.
5. **Statement-level provenance** — facts are observations tied to sources and collection runs.
6. **Append-oriented evidence** — repeated observations do not silently overwrite history.
7. **Structured identity only** — deterministic IDs should rely on strong identifiers, not free-text names.
8. **Human-reviewed resolution** — similarity can suggest `same_as`; only a human may accept it.
9. **Separate confidence scales** — tool confidence, similarity and analytical confidence are not interchangeable.
10. **FollowTheMoney compatibility** — prefer an established entity model over inventing one casually.
11. **Local-first graph UX** — visualization must not leak case data just because someone wanted prettier JavaScript.
12. **`llms.txt` discoverability** — machine-facing documentation is a first-class surface.

## Intentionally not adopted

OSINT4ALL remains a **catalog and methodology layer**. It does not add automatic target collection, access-control/CAPTCHA bypass, credential-dump acquisition, unbounded recursive pivots or automatic identity merging.

The upstream may support capabilities that are appropriate in authorized professional environments; inclusion here does not turn them into default OSINT4ALL behavior.

## Architectural result

```text
Analyst requirement
      ↓
input / jurisdiction / discipline
      ↓
read-only resource router
      ↓
declarative source-selection playbook
      ↓
analyst-controlled collection
      ↓
capture + statement + provenance
      ↓
entity candidates
      ↓
similarity suggestion
      ↓
HUMAN review
      ↓
assessment + confidence
```
