# Upstream OSINT Reference Ecosystems

OSINT4ALL does not wholesale-copy upstream lists. It uses them as **discovery sources**, normalizes high-value entries into the canonical catalog, and records curatorial decisions.

Machine-readable registry: [data/upstreams.json](../data/upstreams.json)

Last reviewed: **2026-09-30**.

## jivoi/awesome-osint

Repository: https://github.com/jivoi/awesome-osint

Role: **classical OSINT taxonomy and discovery baseline**.

Observed strengths include general/meta/national search, breach and specialty search, files/code/documents, SOCMINT, people/email/phone/company research, domains and DNS, web history, language, imagery/video, academic/grey literature, geospatial analysis, news/fact checking, monitoring, data visualization, social-network analysis, maritime, threat intelligence, blogs and RSS.

## Astrosp/Awesome-OSINT-List

Repository: https://github.com/Astrosp/Awesome-OSINT-List

Role: **broad modern surface coverage and gap detection**.

Observed strengths include AI-assisted research, breach-exposure awareness, identity resolution, social/messaging platforms, media verification, metadata/file analysis, vehicles/VIN, aviation, maritime, source code, domains/IP/DNS, IoT, radio, real estate, corporations, maps/GEO, cryptocurrency/blockchain, public records, government, finance/business, conflict, academic/research resources and OSINT training.

Security/pentest-only material is not automatically imported. OSINT4ALL keeps public-source investigation distinct from exploitation.

## OSINT Shifu / awesome-osint-repos

Repository: https://github.com/osintshifu/awesome-osint-repos

Role: **repository-first structured OSINT catalogue**.

The reviewed catalogue exposes 12 main categories, 28 target-input types, a canonical CSV, an emerging-project view, a timeline, and a dedicated Agentic/MCP view. Its strongest contribution to OSINT4ALL is therefore structural: tools can be discovered by the concrete artifact an analyst already has.

Adopted concepts:

- `target_inputs`;
- implementation type;
- repository-first curation;
- emerging-project watchlist;
- Agentic/MCP as a separate analytical layer;
- catalogue timeline/change intelligence;
- machine-readable upstream provenance.

Selected project imports include Bellingcat Octosuite, ICIJ Datashare, FollowTheMoney, OpenTrace, changedetection.io, UseOSINT Skills and additional investigation/discovery tools.

## Trace Labs organization review

Organization: https://github.com/orgs/tracelabs/repositories

| Repository | Decision | Why |
|---|---|---|
| tracelabs/tlosint-vm | **Incorporated** | Current VM/workstation, tooling, capture, archiving and investigator-safety practices |
| tracelabs/awesome-osint | **Incorporated** | Missing-person-specific curated list |
| tracelabs/tofm | **Incorporated** | Ethics, passive research, planning, red lines, validation and people-centric tradecraft |
| tracelabs/tracelabs-weekly-osint-challenges | **Incorporated** | Sanitized training and methodology |
| tracelabs/searchparty-ctf-writeups | **Historical** | Archived learning/writeup material |
| tracelabs/tlosint-live | **Historical** | Legacy Kali live-build; current direction is tlosint-vm |
| tracelabs/gumshoe | **Historical concept** | Recursive investigation graph idea remains architecturally interesting; code is old WIP |
| Trace-Labs-VM-Ras-Pi-Build | Reviewed, not primary catalog | Legacy platform-specific variant |
| Trace-Labs-VM-M1-Mac-Build | Reviewed, not primary catalog | Platform-specific variant; current VM direction covers ARM64 |
| tracelabs/ctf-prep | Historical/moved | Archived; content moved to current Trace Labs docs |
| tracelabs/h8mail | Packaging-only | Prefer canonical h8mail upstream over distro packaging fork |
| Trace-Labs-Obsidian-Theme | Not cataloged | Theme/presentation asset rather than OSINT capability |
| B-Sides-Bloomington | Not cataloged | Event-specific material rather than reusable analyst capability |

## Curatorial pipeline

    Upstream discovery
        ↓
    Canonical-source check
        ↓
    Deduplication
        ↓
    Jurisdiction / discipline / use-case tagging
        ↓
    Safety + legal + maintenance review
        ↓
    needs-review
        ↓
    human validation
        ↓
    verified

The important part is that **rejection and historical classification are also data**. Otherwise the same obsolete fork gets rediscovered every six months and somebody proudly adds it again.
