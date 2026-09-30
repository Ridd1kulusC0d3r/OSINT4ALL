# OSINT4ALL Analyst-Centered Evolution Roadmap

This roadmap is written from the perspective of an analyst doing real investigative work. The unit of progress is not “more links”; it is **more reliable decisions with less friction and better provenance**.

## Maturity model

### Level 0 — Link collection

**Question:** Where can I search?

Capabilities:

- thematic lists;
- meta-indexes;
- basic country links.

Risk: lots of discovery, little trust.

### Level 1 — Trusted resource catalog

**Question:** Which source should I use, and can I trust that the entry is current?

Capabilities:

- canonical IDs;
- structured metadata;
- access model;
- jurisdiction;
- validation state;
- last-verified date;
- deduplication;
- link health.

Acceptance criteria:

- every machine-readable entry passes schema validation;
- duplicates are blocked;
- verified entries carry a human review date;
- stale/broken resources are automatically surfaced.

### Level 2 — Jurisdiction-aware atlas

**Question:** Which authoritative sources apply here?

Capabilities:

- national/federal sources;
- states/provinces/regions;
- municipal/local data;
- courts;
- companies;
- property;
- procurement;
- elections/civic data;
- environment;
- archives/media;
- cyber/public infrastructure.

Acceptance criteria:

- Brazil covers federal + all 27 UFs;
- each country page distinguishes official from commercial/community sources;
- legal/privacy notes are visible at point of use.

### Level 3 — Evidence-first investigation

**Question:** Can another analyst reproduce what I saw?

Capabilities:

- provenance template;
- capture/archive workflow;
- timestamps;
- hashes where appropriate;
- evidence labels: observed / claimed / corroborated / inferred / unresolved;
- confidence model;
- evidence bundles.

Acceptance criteria:

- every playbook includes preservation;
- important findings can be traced to a source and capture event;
- generated reports distinguish evidence from inference.

### Level 4 — Analyst playbooks

**Question:** What sequence should I follow?

Playbooks:

- people/identity;
- missing persons;
- company/ownership;
- GEOINT verification;
- image/video verification;
- CTI enrichment;
- conflict verification;
- environmental investigation;
- transport/maritime/aviation;
- web history;
- public-record research.

Each playbook should include:

1. intelligence requirement;
2. scope/red lines;
3. source map;
4. collection;
5. preservation;
6. validation;
7. pivots;
8. alternative hypotheses;
9. confidence;
10. dissemination/stop condition.

### Level 5 — Searchable analyst workbench

**Question:** Can I find the right source in seconds?

Capabilities:

- GitHub Pages;
- full-text search;
- filters by country, discipline, use case, access and validation;
- resource cards;
- direct catalog permalinks;
- mobile-first interface;
- English / Portuguese;
- saved filter URLs.

Acceptance criteria:

- no analyst needs to browse the repository tree to find a source;
- every resource page shows jurisdiction, purpose, validation and caveats.

### Level 6 — Intelligence knowledge graph

**Question:** How do resources, entities, evidence and cases connect?

Model:

    Resource ↔ Jurisdiction ↔ Discipline ↔ Use Case
        ↕
      Entity ↔ Relationship ↔ Evidence
        ↕
       Case ↔ Hypothesis ↔ Assessment

Capabilities:

- entity IDs;
- typed relationships;
- evidence provenance;
- confidence per assertion;
- graph export;
- STIX where appropriate for CTI;
- analyst case graph separated from public resource graph.

### Level 7 — Change intelligence & monitoring

**Question:** What changed since yesterday?

Capabilities:

- source freshness;
- redirect/ownership changes;
- GitHub archive/release detection;
- RSS monitoring;
- government/regulatory updates;
- environmental alerts;
- CTI advisories;
- diff reports;
- stale-source queue.

Principle: alerts identify change; analysts decide significance.

### Level 8 — AI-assisted analysis with provenance

**Question:** Can automation reduce repetitive work without inventing facts?

Capabilities:

- entity extraction;
- tagging;
- translation;
- summarization with citations;
- duplicate/entity candidate detection;
- timeline normalization;
- query expansion;
- source triage.

Guardrails:

- AI output is never a source;
- candidate identity is never identity proof;
- every material model-assisted transformation is traceable.

### Level 9 — Training & community

**Question:** Can a new analyst learn the tradecraft safely?

Capabilities:

- sanitized challenges;
- progressive missions;
- solution writeups;
- methodology reviews;
- evidence-quality exercises;
- contributor onboarding;
- reviewer calibration.

Trace Labs is the primary inspiration for this layer.

### Level 10 — OSINT4ALL 1.0

Definition of done:

- global discovery atlas + deep jurisdiction packs;
- structured catalog/API;
- evidence-first playbooks;
- searchable UI;
- provenance-aware graph;
- quality automation;
- analyst training;
- documented governance;
- clear separation of collection, evidence and analysis.

## Priority order

1. Finish catalog coverage and provenance.
2. Build Brazil federal + 27 UF atlas.
3. Add evidence templates and playbooks.
4. Build searchable GitHub Pages.
5. Add lifecycle/change monitoring.
6. Add knowledge graph.
7. Add Academy/challenges.
8. Expand country coverage systematically.

That order is intentional. A graph of bad data is just a faster way to be wrong.
