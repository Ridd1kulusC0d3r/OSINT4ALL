# Missing Persons OSINT

> **Specialization, not a standalone collection discipline.** This chapter groups ethical, people-centric OSINT methods useful in missing-person investigations.
>
> **Safety rule:** discovery must not become contact, harassment, public accusation or interference with an active investigation.

## Why Trace Labs matters here

Trace Labs is useful to OSINT4ALL because it treats missing-person investigations as a combination of **methodology, investigator safety, passive collection, evidence quality and training**, not merely a bag of search tools.

### Primary references

| Resource | Value to analysts | Status |
|---|---|---|
| [Trace Labs OSINT Field Manual](https://github.com/tracelabs/tofm) | Planning, ethics, safety, passive reconnaissance, enumeration, pivoting and geolocation | 🟢 |
| [Trace Labs Awesome OSINT](https://github.com/tracelabs/awesome-osint) | Curated free resources specifically relevant to missing-person searches | 🟢 |
| [Trace Labs OSINT VM](https://github.com/tracelabs/tlosint-vm) | Reproducible investigation environment plus capture, archiving, SOCMINT and OPSEC tooling | 🟢 |
| [Weekly OSINT Challenges](https://github.com/tracelabs/tracelabs-weekly-osint-challenges) | Sanitized practice material emphasizing methodology and verification | 🟢 |
| [Search Party CTF Writeups](https://github.com/tracelabs/searchparty-ctf-writeups) | Historical learning material from Search Party CTFs | ⚪ |

## Methodological principles adopted by OSINT4ALL

### 1. Define the mission before collecting

Write down the specific question, expected output, time/resource limits and what is out of scope.

A pile of facts is not automatically useful intelligence.

### 2. Define success and stopping conditions

People-centric investigations can expand indefinitely. Decide what evidence would answer the original question and when collection should stop.

### 3. Define red lines

Stop or escalate appropriately when continued research could expose vulnerable people, interfere with an investigation, reveal serious harm, or exceed the analyst's legal/ethical mandate.

### 4. Prefer passive reconnaissance

For sensitive investigations, passive research reduces risks to the subject, third parties and the integrity of the case.

Do not contact subjects, relatives, friends or unrelated accounts merely to obtain more information.

### 5. Enumeration is not validation

Finding the same username on multiple services creates **candidate associations**, not identity proof.

Validate with independent attributes, chronology, media, relationships and primary records where appropriate.

### 6. Go wide before going deep

Map the available identifiers and candidate sources before following a single attractive lead too far.

Maintain provenance so every pivot can be traced back to its origin.

### 7. Threat-model the investigation

Consider the sensitivity of the subject, platforms used, exposure of the analyst, data being retained and consequences if the investigation becomes visible.

The appropriate OPSEC level depends on the investigation, not on ritualistic use of anonymity tools.

### 8. Preserve evidence and context

Capture URLs, timestamps, screenshots or archives when lawful, and record why an item matters.

Preservation tools do not make an observation true; they only help preserve what was observed.

## Suggested workflow

    Mission
      ↓
    Known identifiers / source of truth
      ↓
    Broad enumeration
      ↓
    Candidate validation
      ↓
    Controlled pivots
      ↓
    Media / geolocation / records
      ↓
    Corroboration
      ↓
    Evidence package + confidence
      ↓
    Stop / report / escalate appropriately

## Evidence labels

For every people-centric finding, distinguish:

- **Observed** — directly visible in the source.
- **Claimed** — asserted by a source but not independently established.
- **Corroborated** — supported by independent evidence.
- **Inferred** — analytical conclusion derived from evidence.
- **Unresolved** — plausible but insufficiently supported.

## Privacy note

Do not publish unnecessary personal information about a missing person, family members, minors, witnesses or unrelated third parties. The objective is to support responsible investigation, not create a permanent public dossier.
