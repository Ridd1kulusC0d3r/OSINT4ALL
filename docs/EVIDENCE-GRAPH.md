# Evidence Graph Model

OSINT4ALL now distinguishes **resources**, **observations**, **entities**, **resolution hypotheses** and **analytical assessments**.

## Statement layer

A statement is the smallest evidentiary assertion:

```text
entity_id + property + value
        ↓
source_id
capture_id
assertion_label
        ↓
provenance record(s)
```

Re-observing the same fact should create another provenance observation, not erase the earlier one.

## Entity identity

Deterministic entity identifiers should use structured identifiers where possible: a domain, registry number, account/service pair, document identifier or another stable key.

**Do not key identity from a free-text name.** Two people or organizations can share a name. Name similarity belongs in the resolution layer, never in silent pre-merge logic.

## Resolution queue

```text
entity A ─┐
          ├─ similarity candidate → judgement=unsure
entity B ─┘
                           ↓
                    human review
                    ↙          ↘
                positive      negative
```

Machine scoring may create only an **unsure candidate**. Positive identity resolution requires an explicit human decision.

## Provenance

Every important statement should retain:

- source URL and source class;
- capture identifier and timestamp;
- collection method;
- run identifier;
- assertion label;
- observation-confidence label;
- archive URL/hash where available.

See `schema/evidence-bundle.schema.json` and `examples/evidence-bundle.synthetic.json`.

## Privacy and erasure

Persistent graphs can contain personal data. A production implementation must support retention controls, targeted erasure, access controls and auditability. Deleting the display node while leaving identifying statements, hashes or relationship rows is not meaningful erasure.

The repository currently defines the portable evidence model. It does **not** yet ship a persistent personal-data case database.
