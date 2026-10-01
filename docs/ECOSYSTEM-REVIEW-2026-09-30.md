# Ecosystem Review — 2026-09-30

Reviewed public repositories: **OSINT Shifu, K2SOsint, OSINT Brazuca and jivoi**.

## Decisions

### OSINT Shifu
**Incorporated:** awesome-osint-repos, QueryTool, FileGrail, unmasker, Cyber Intelligence Toolkit.  
**Reviewed but not primary:** Cyber-Intelligence-GPT (model output is not evidence), awesome-osint (overlaps tracked awesome-list upstreams).

### K2SOsint
**Incorporated:** Legendary_OSINT, Legendary_Crypto, Bookmarklets.  
**Canonicalized:** deepdarkCTI → fastfire/deepdarkCTI; WhatsMyName → WebBreacher/WhatsMyName.  
**Not primary:** DocuFinderJS, OSINT_CSI, Basic-Chromium-Extensionv3.

### OSINT Brazuca
The main repository documented **510 sources, 1,258 flattened links, 31 input types, 41 output types and 14 source-nature classes** at review time.

**Incorporated:** osint-brazuca, osint-brazuca-regex, osint-papers, SimpleReconURL, SimpleReconDorking.  
**Not primary:** SimpleReconDomain and osint-brazuca-nuclei-templates because they extend beyond passive/evidence-first OSINT into scanner or active-recon workflows.

### jivoi
**Incorporated:** awesome-osint and awesome-ml-for-cybersecurity.  
Most remaining repositories are pentest, exploit-development, DevOps or general security projects and were intentionally not imported.

## Architectural lessons
- OSINT Shifu → target-input discovery, emerging state, agentic/MCP separation, catalogue timeline.
- OSINT Brazuca → jurisdiction identifiers, input/output mapping and source nature.
- K2SOsint → blockchain, railways, reporting/visualization, OSINT-for-good and browser utilities.
- jivoi → classical OSINT taxonomy plus adjacent ML/security research.

OSINT4ALL records rejection and canonicalization decisions so obsolete forks do not repeatedly return wearing a fake moustache.
