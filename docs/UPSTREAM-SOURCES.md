# Upstream OSINT Reference Ecosystems

OSINT4ALL does not wholesale-copy upstream lists. It uses them as **discovery sources**, normalizes high-value entries into the machine-readable catalog, and records what each ecosystem contributes.

Last reviewed: **2026-09-30**.

## jivoi/awesome-osint

Repository: https://github.com/jivoi/awesome-osint

Observed strengths:

- general, meta and privacy-focused search;
- national search engines;
- data-breach and specialty search;
- document, file and code search;
- SOCMINT platform coverage;
- people, email, phone and company research;
- domains/IP/DNS;
- web history and capture;
- image/video;
- academic and grey literature;
- geospatial research;
- news, fact checking and statistics;
- monitoring, data visualization and social-network analysis;
- maritime, CTI, blogs, RSS and learning resources.

Role in OSINT4ALL: **classical tradecraft taxonomy and discovery baseline**.

## Astrosp/Awesome-OSINT-List

Repository: https://github.com/Astrosp/Awesome-OSINT-List

Observed strengths:

- very broad modern surface coverage;
- AI/search/research tooling;
- breach-exposure awareness;
- identity resolution and unified search;
- messaging/social platforms;
- media verification and metadata;
- vehicles, aviation and maritime;
- source-code/domain/IoT research;
- real estate, public records and government;
- finance, business, cryptocurrency/blockchain;
- conflict-related resources;
- academic/training resources;
- frameworks/browser tooling.

Role in OSINT4ALL: **long-tail coverage discovery and gap detection**.

Security/pentest-only material is not automatically imported. OSINT4ALL separates public-source investigation from exploitation.

## Trace Labs

Organization: https://github.com/orgs/tracelabs/repositories

High-value repositories incorporated:

- https://github.com/tracelabs/tlosint-vm
- https://github.com/tracelabs/awesome-osint
- https://github.com/tracelabs/tofm
- https://github.com/tracelabs/tracelabs-weekly-osint-challenges
- https://github.com/tracelabs/searchparty-ctf-writeups (historical)

Observed strengths:

- missing-person and people-centric methodology;
- ethics and passive reconnaissance;
- investigation planning and red lines;
- enumeration vs validation;
- analyst OPSEC/threat modeling;
- reproducible investigation workstation;
- evidence capture and archiving;
- practical training and writeups;
- explicit tooling-quality policy.

Role in OSINT4ALL: **methodology, evidence handling, training and analyst environment**.

## Import rule

An upstream mention creates a **candidate**, not an automatic recommendation.

Candidates pass through:

    Upstream discovery
        ↓
    Canonical-source check
        ↓
    Deduplication
        ↓
    Jurisdiction + discipline + use-case tagging
        ↓
    Safety / legal / maintenance review
        ↓
    needs-review
        ↓
    human validation
        ↓
    verified

This prevents the repository from becoming an unmaintainable mirror of other unmaintainable mirrors.
