# OSINT4ALL 🌍

> **Open Intelligence Atlas · Atlas Aberto de Inteligência**  
> Jurisdiction-aware · evidence-first · machine-readable · bilingual · AI-assisted with human validation

[![Language](https://img.shields.io/badge/language-English%20%7C%20Portugu%C3%AAs-0A66C2)](#languages)
[![Catalog](https://img.shields.io/badge/catalog-v0.3.2-blue)](data/resources.json)
[![Resources](https://img.shields.io/badge/resources-76-informational)](catalog/INDEX.generated.md)
[![Ethics](https://img.shields.io/badge/use-ethical%20%26%20lawful-success)](ETHICS.md)
[![AI Assisted](https://img.shields.io/badge/curation-AI--assisted-orange)](#ai-assisted-curation)

## What this repository is / O que este repositório é

**OSINT4ALL** is not meant to become the longest list of links on GitHub. It is being built as a **maintainable intelligence-resource atlas** that answers:

1. **Where does a source apply? / Onde se aplica?**
2. **Which intelligence discipline does it support? / Qual disciplina apoia?**
3. **What analytical task does it solve? / Qual tarefa resolve?**
4. **How current and trustworthy is the catalog entry? / Quão atual e confiável é a entrada?**
5. **How should evidence and provenance be preserved? / Como preservar evidência e proveniência?**

The canonical data source is [data/resources.json](data/resources.json). Markdown catalogs explain methodology and use; generated views come from the structured data.

---

## Start here / Comece aqui

| Need / Necessidade | Go to / Vá para |
|---|---|
| Find any structured resource | [Generated Resource Index](catalog/INDEX.generated.md) |
| Understand intelligence disciplines | [Intelligence Disciplines](docs/INTELLIGENCE-DISCIPLINES.md) |
| Search techniques and discovery | [Search & Discovery](catalog/SEARCH-DISCOVERY.md) |
| Start from a username/email/domain/image/etc. | [Tools by Target Input](catalog/INPUTS.generated.md) |
| GitHub / public code repositories | [Code Repository OSINT](catalog/CODE-REPOSITORY-OSINT.md) |
| Organize cases, evidence and hypotheses | [Investigation Workbenches](catalog/INVESTIGATION-WORKBENCHES.md) |
| Agent/MCP-assisted workflows | [Agentic OSINT](catalog/AGENTIC-OSINT.md) |
| Preserve web/media evidence | [Evidence Capture & Preservation](catalog/EVIDENCE-PRESERVATION.md) |
| People / usernames / email / phone | [People OSINT](catalog/PEOPLE-OSINT.md) |
| Missing-person methodology | [Missing Persons OSINT](catalog/MISSING-PERSONS-OSINT.md) |
| Social platforms | [SOCMINT](catalog/SOCMINT.md) |
| Image / geolocation / maps | [IMINT & GEOINT](catalog/IMINT-GEOINT.md) |
| Companies / ownership / finance | [Corporate & Financial OSINT](catalog/CORPORATE-FINANCIAL.md) |
| Aircraft / vessels / transport | [Transport / Maritime / Aviation](catalog/TRANSPORT-MARITIME-AVIATION.md) |
| Satellite / orbital / Earth observation | [Space & Satellite](catalog/SPACE-SATELLITE.md) |
| Cyber threat intelligence | [CTI & OT](catalog/CTI-OT.md) |
| Conflict verification | [Conflict OSINT](catalog/CONFLICT-OSINT.md) |
| Environment / deforestation | [Environmental OSINT](catalog/ENVIRONMENTAL-OSINT.md) |
| Nuclear / CBRNE public-source verification | [Nuclear & CBRNE](catalog/NUCLEAR-CBRNE.md) |
| Academic / media / monitoring | [Academic, Media & Monitoring](catalog/ACADEMIC-MEDIA-MONITORING.md) |
| AI assistance | [AI-Assisted OSINT](catalog/AI-ASSISTED-OSINT.md) |
| Sources by country | [Country & Federation Atlas](countries/README.md) |
| Brazil | [Brazil Country Profile](countries/BR/README.md) |
| Upstream lists we learn from | [Upstream Reference Ecosystems](docs/UPSTREAM-SOURCES.md) |
| Project evolution | [Analyst-Centered Roadmap](docs/ANALYST-ROADMAP.md) |
| Add/correct a resource | [Contributing](CONTRIBUTING.md) |

---

## Analyst workflow / Fluxo do analista

OSINT4ALL is organized around an intelligence workflow rather than a random toolbox.

```text
Intelligence requirement
        ↓
Scope + red lines + jurisdiction
        ↓
Source mapping
        ↓
Collection
        ↓
Capture + provenance
        ↓
Normalization / entity candidates
        ↓
Verification + corroboration
        ↓
Hypotheses + alternatives
        ↓
Confidence assessment
        ↓
Intelligence product
        ↓
Feedback + revalidation
```

### Evidence language

Use explicit analytical labels:

| Label | Meaning |
|---|---|
| **Observed** | Directly visible in a source |
| **Claimed** | Asserted by a source |
| **Corroborated** | Supported by independent evidence |
| **Inferred** | Analytical conclusion derived from evidence |
| **Unresolved** | Plausible but insufficiently supported |

A username hit is a lead. A search result is a lead. An AI answer is not a source. Humanity did invent entire careers by forgetting these three sentences.

---

## Coverage map / Mapa de cobertura

### Core collection & intelligence disciplines

**OSINT · HUMINT · SIGINT · COMINT · ELINT · FISINT · GEOINT · IMINT · MASINT · TECHINT · CYBINT · CTI · MEDINT · FININT · DOMEX · WEBINT · DNINT · SOCMINT**

See [docs/INTELLIGENCE-DISCIPLINES.md](docs/INTELLIGENCE-DISCIPLINES.md) for definitions and overlap.

### Investigative domains tracked

**Search & discovery · Target-input discovery · Code repository intelligence · Investigation workbenches · Agentic OSINT · People & identity · Missing persons · SOCMINT · GEOINT · IMINT · Media verification · Evidence preservation · Web archives · Corporate intelligence · Financial intelligence · Public records · Cyber infrastructure · CTI · OT/ICS defensive research · Space & satellite · Aviation · Maritime · Transport · Environmental intelligence · Conflict verification · Nuclear/CBRNE public-source research · Academic/grey literature · News/media · Monitoring/RSS · AI-assisted analysis · Training**

### Jurisdiction model

```text
countries/<ISO-3166-1 alpha-2>/
├── README.md
├── federal.md
├── subnational/
└── sources/
```

Country packs should distinguish:

**national/federal · states/provinces/regions · municipal/local · courts · companies · property/land · procurement · elections/civic data · environment · transport · infrastructure · archives/media · privacy/legal constraints**

---

## Reference ecosystems incorporated

OSINT4ALL uses major lists as **upstream discovery ecosystems**, not as content to blindly mirror.

| Upstream | What it contributes |
|---|---|
| [jivoi/awesome-osint](https://github.com/jivoi/awesome-osint) | Classical OSINT taxonomy: search, people, SOCMINT, domains, archives, imagery, academic research, geospatial, monitoring and CTI |
| [Astrosp/Awesome-OSINT-List](https://github.com/Astrosp/Awesome-OSINT-List) | Broad modern coverage: AI, identity resolution, media verification, metadata, vehicles, aviation, maritime, finance, blockchain, government/public records and training |
| [OSINT Shifu / awesome-osint-repos](https://github.com/osintshifu/awesome-osint-repos) | Repository-first catalogue, target-input model, emerging projects, agentic/MCP integrations and investigation workbenches |
| [Trace Labs repositories](https://github.com/orgs/tracelabs/repositories) | Missing-person methodology, passive research, evidence quality, analyst safety, VM/workstation, training and tooling-selection discipline |
| [Bellingcat Toolkit](https://bellingcat.gitbook.io/toolkit) | Verification-oriented investigation resources |
| [OSINT Framework](https://osintframework.com/) | Discovery-tree approach |
| [OSINT Brazuca](https://github.com/osintbrazuca/osint-brazuca) | Brazilian OSINT ecosystem |

Detailed provenance and import policy: [docs/UPSTREAM-SOURCES.md](docs/UPSTREAM-SOURCES.md).

---

## Trace Labs lessons adopted

From the current Trace Labs ecosystem OSINT4ALL now incorporates:

- people-centric and missing-person methodology;
- mission definition and stopping conditions;
- passive-research principle for sensitive cases;
- enumeration ≠ validation;
- threat-model thinking;
- evidence capture and archiving;
- analyst workstation as a reproducible environment;
- sanitized training/challenges;
- explicit tool-selection quality criteria.

Primary references:

- [Trace Labs OSINT VM](https://github.com/tracelabs/tlosint-vm)
- [Trace Labs Awesome OSINT](https://github.com/tracelabs/awesome-osint)
- [Trace Labs OSINT Field Manual](https://github.com/tracelabs/tofm)
- [Trace Labs Weekly OSINT Challenges](https://github.com/tracelabs/tracelabs-weekly-osint-challenges)

Historical material is retained as historical, not silently promoted as current.

---

## Evidence capture & preservation

Discovery without preservation is fragile.

OSINT4ALL now tracks tools and methods for:

**web archiving · screenshots · offline copies · public-media acquisition · frame extraction · OCR · document sanitization · metadata hygiene · archive access**

See [catalog/EVIDENCE-PRESERVATION.md](catalog/EVIDENCE-PRESERVATION.md).

Minimum provenance for an important finding:

- canonical URL;
- capture timestamp + timezone;
- original publication time if known;
- source/account/author;
- capture method;
- archive URL when available;
- relevant metadata;
- analyst observation;
- fact/claim/inference label;
- link to the intelligence requirement.

---

## AI-assisted curation

This repository is **AI-assisted** for classification, normalization, translation, deduplication and drafting.

AI assistance can introduce:

- stale links;
- incorrect descriptions;
- wrong jurisdiction tags;
- duplicate identities;
- hallucinated capabilities;
- incorrect access/licensing assumptions.

Therefore:

> **AI output is never treated as a source. New AI-assisted resource entries default to 🟡 Needs review.**

See [VALIDATION.md](VALIDATION.md) and [AI-Assisted OSINT](catalog/AI-ASSISTED-OSINT.md).

---

## Resource validation

| Marker | Machine status | Meaning |
|---|---|---|
| 🟢 | `verified` | URL and core capability manually checked |
| 🟡 | `needs-review` | Candidate/useful, not yet fully validated |
| 🟠 | `changed` | Important capability/ownership/access changed |
| 🔴 | `broken-unsafe` | Dead, compromised, misleading or unsuitable |
| ⚪ | `historical` | Kept for historical/learning context |

Selection policy: [docs/TOOL-SELECTION-POLICY.md](docs/TOOL-SELECTION-POLICY.md).

---

## Machine-readable architecture

```text
data/upstreams.json  → upstream provenance + curation decisions
        │
data/resources.json
        │
        ├── validated by scripts/validate_catalog.py
        │
        ├── taxonomy → data/taxonomies.json
        │
        ├── schema → schema/resource.schema.json
        │
        ├── input taxonomy → catalog/INPUTS.generated.md
        │
        └── generated view → catalog/INDEX.generated.md
```

The CI rejects malformed IDs, duplicate canonical URLs, invalid disciplines and malformed tags. Scheduled link health raises review signals without pretending every bot-blocked website is dead. A modest concession to reality.

---

## Current project maturity

| Layer | Status |
|---|---|
| Bilingual foundation | ✅ |
| Ethics / validation / contribution policy | ✅ |
| Machine-readable catalog | ✅ |
| Schema + taxonomy + CI | ✅ |
| Link health | ✅ |
| Trace Labs methodology integration | ✅ |
| jivoi + Astrosp + OSINT Shifu upstream mapping | ✅ |
| Evidence preservation layer | ✅ |
| Thematic catalogs | ✅ growing |
| Brazil country seed | ✅ |
| Brazil federal + 27 UFs | 🚧 |
| Evidence-first playbooks | 🚧 |
| GitHub Pages searchable UI | planned |
| Knowledge graph / case graph | planned |
| Change intelligence / monitoring | planned |
| Academy / challenges | planned |

Full plan: [docs/ANALYST-ROADMAP.md](docs/ANALYST-ROADMAP.md).

---

## Ethical and lawful use

Use OSINT4ALL for lawful, ethical and authorized research.

Do not use this catalog to facilitate:

- stalking or harassment;
- doxxing;
- coercion or discrimination;
- unauthorized access;
- targeting vulnerable people;
- physical harm;
- interference with active investigations.

Sensitive domains such as people search, conflict, critical infrastructure and CBRNE are documented for **verification, defensive research and public-interest analysis**, not harm.

See [ETHICS.md](ETHICS.md).

---

## Contributing

Corrections are as valuable as additions.

Every proposed resource should identify:

**canonical URL · jurisdiction · discipline · use case · source type · access model · languages · validation state · privacy/legal caveats**

Start with [CONTRIBUTING.md](CONTRIBUTING.md).

---

## Languages

- **English** — primary global documentation language.
- **Português (pt-BR)** — first-class language for Brazil and the Lusophone community.

The machine-readable metadata uses stable canonical values; human-facing documentation may be bilingual or localized.

---

## Long-term model

```text
Resource ↔ Jurisdiction ↔ Discipline ↔ Use Case
    ↕
Entity ↔ Relationship ↔ Evidence
    ↕
 Case ↔ Hypothesis ↔ Assessment
```

The destination is an **open intelligence resource graph** where analysts can discover sources, understand applicability, preserve evidence, evaluate confidence and produce reproducible intelligence products.

## Disclaimer

OSINT4ALL is an educational and research index. Third-party resources can change, disappear, become paid, alter their terms, or simply be wrong. Inclusion is not endorsement. Responsibility for lawful and proportionate use remains with the analyst.
