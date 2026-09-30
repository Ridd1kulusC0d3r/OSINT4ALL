# OSINT4ALL Tool Selection Policy

OSINT4ALL is not an "install everything" collection. Tools and resources should earn their place.

This policy is inspired in part by the maintainability principles used by the Trace Labs OSINT VM, expanded for a global, jurisdiction-aware catalog.

## Decision classes

| Class | Meaning |
|---|---|
| **Verified** | Canonical URL and core capability manually checked |
| **Needs review** | Potentially useful, but current capability or metadata needs human validation |
| **Changed** | Resource still exists but important behavior, access, ownership or scope changed |
| **Historical** | Useful for research or learning, but no longer a primary operational recommendation |
| **Broken / unsafe** | Dead, compromised, deceptive or unsuitable |

## Admission criteria

A resource should be evaluated on:

1. **Investigative relevance** — Does it solve a concrete OSINT/intelligence problem?
2. **Jurisdiction fit** — Where does it actually apply?
3. **Redundancy** — Does it meaningfully improve on resources already listed?
4. **Source primacy** — Is there an official or canonical source instead of a mirror/fork?
5. **Legal and ethical fit** — Can it be described and used within lawful, proportionate OSINT workflows?
6. **Security** — Are there obvious supply-chain, malware, dependency or reputation concerns?
7. **Maintenance** — Is it actively maintained, stable, or intentionally complete?
8. **Documentation** — Can an analyst understand what it does and its limitations?
9. **License / terms** — Are licensing and service restrictions reasonably clear?
10. **Evidence value** — Does it produce discovery leads, contextual information or evidence, and is that distinction clear?
11. **Automation quality** — Is machine-readable access/API support available where relevant?
12. **Privacy sensitivity** — Does the resource aggregate personal or biometric data in ways requiring special caution?

## Immediate reasons not to promote a resource

A resource should not become a primary recommendation when:

- the listed project is merely a packaging fork while a canonical upstream exists;
- its core capability is abandoned or superseded;
- claims cannot be reproduced or documented;
- it primarily facilitates unauthorized access rather than open-source investigation;
- it introduces unnecessary legal, privacy or security risk;
- it duplicates an existing resource without a meaningful advantage.

## Maintenance signals

Useful signals include:

- recent commits/releases;
- responsive issue/PR activity;
- current documentation;
- working canonical URL;
- transparent ownership;
- reproducible build/install process;
- maintained dependencies.

Recent activity is a signal, not proof of quality. Old, stable datasets and finished utilities can remain valuable.

## Review cadence

- **Continuous:** corrections and broken-link reports.
- **Quarterly:** high-value tools and rapidly changing social/web resources.
- **Annually:** taxonomy, policy and slower-moving official sources.
- **Event-driven:** ownership changes, major API changes, breaches, archival or licensing changes.

## Trace Labs lesson adopted

The strongest idea worth borrowing is simple: **curation quality matters more than tool count**.

OSINT4ALL should prefer a smaller number of clearly described, jurisdiction-tagged and validated resources over thousands of links whose current status nobody understands.
