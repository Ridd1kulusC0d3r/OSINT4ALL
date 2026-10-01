# AI Execution Contract

This contract defines what an AI assistant may do with OSINT4ALL.

## Allowed by default

- read the catalogue;
- filter resources by input, jurisdiction, discipline, domain and validation state;
- propose a source-selection plan;
- select a declarative playbook;
- explain why a source is relevant;
- transform analyst-supplied evidence into the evidence-bundle model;
- identify missing provenance;
- suggest candidate entity relationships as **unresolved**.

## Required constraints

- AI output is not evidence.
- Every factual finding in an evidence bundle must reference a source/capture.
- Automated entity resolution may only produce `judgement=unsure`.
- Positive or negative identity resolution is a human decision.
- Automation must have explicit scope and stopping conditions.
- A failure, empty result and missing configuration are distinct states.
- The router is read-only and makes no network requests.

## Not provided by OSINT4ALL automation

- target execution or automatic collection;
- access-control or CAPTCHA bypass;
- acquisition of stolen credentials or illicit datasets;
- unbounded recursive pivots;
- automatic identity merges;
- instructions for harmful targeting.

## Agent output contract

A compliant agent should return:

```text
Requirement
Scope / jurisdiction
Selected playbook
Selected resources + reasons
Collection steps for the analyst
Evidence fields required
Known gaps
Stop condition
```

If evidence is supplied, it may additionally return statements, provenance gaps, unresolved candidates and analytical confidence with rationale.
