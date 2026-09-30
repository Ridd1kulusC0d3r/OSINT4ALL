# Cyber Threat Intelligence & OT/ICS OSINT

> Focus: defensive research, threat intelligence, exposure awareness and authorized environments.
>
> Tools that can actively probe systems must only be used on infrastructure you own or are explicitly authorized to assess.

## CTI repositories and collections

| Resource | Focus | Status |
|---|---|---|
| hslatman/awesome-threat-intelligence | CTI feeds, platforms, standards and learning | 🟡 |
| Chick3nHawk01/Open_Source-CTI-Tooling | Operational/tactical/strategic CTI resources | 🟡 |
| ARPSyndicate/awesome-intelligence | Tagged intelligence resources | 🟡 |
| fastfire/deepdarkCTI | Deep/dark-web CTI source collection | 🟡 |
| The-OSINT-Newsletter/OSINT-Tools-Library | CTI-oriented OSINT resources | 🟡 |

## CTI platforms and enrichment

| Tool | Use | Status |
|---|---|---|
| MISP | Threat-intelligence sharing and structured events | 🟡 |
| OpenCTI | Knowledge graph / STIX-oriented CTI platform | 🟡 |
| IntelOwl | IOC enrichment and analysis orchestration | 🟡 |
| SpiderFoot | Automated infrastructure/entity correlation | 🟡 |
| dnstwist | Domain permutation and brand-impersonation research | 🟡 |
| Aperture | Browser workbench integrating public threat-intel services; verify current extension | 🟡 |
| Nuclei | Template-based exposure/vulnerability validation in authorized environments | 🟡 |
| goosint-cyber-toolkit | Cyber-oriented OSINT utilities | 🟡 |
| Associated-Threat-Analyzer | Domain/IP threat-association analysis; verify current project | 🟡 |

## Common external intelligence services referenced by CTI workflows

- VirusTotal
- AbuseIPDB
- urlscan.io
- Shodan
- Censys
- AlienVault OTX
- IBM X-Force Exchange
- MalwareBazaar
- GreyNoise
- Have I Been Pwned

Access, rate limits and terms change frequently. Validate before integrating.

## OT / ICS exposure and defensive research

| Tool / resource | Purpose | Status |
|---|---|---|
| Censys | Search/measurement of internet-exposed systems, including industrial technology visibility | 🟡 |
| Shodan | Internet-exposure research with ICS-relevant filters | 🟡 |
| GRASSMARLIN | Passive ICS/SCADA network situational awareness | 🟡 |
| plcscan | PLC discovery/scanning in authorized lab or owned environments only | 🟡 |
| smod | Modbus security-testing framework for isolated/authorized labs only | 🟡 |
| mbtget | Modbus communication utility for lab/owned systems | 🟡 |
| ModbusPal | Modbus simulator for training/lab use | 🟡 |
| Digital Bond Redpoint / ICS enumeration research | Industrial protocol enumeration research; authorized use only | 🟡 |
| CSET | CISA Cyber Security Evaluation Tool | 🟡 |

## OT / ICS learning resources

- hslatman/awesome-industrial-control-system-security
- biero-el-corridor/OT_ICS_ressource_list
- utilsec/Industrial_ICS_OT_Cyber_Security_Resources
- Mike Holcomb — OSINT for ICS and OT course/reference
- CERT.br materials related to MISP/Maltego and threat intelligence
- osintbrazuca/osint-brazuca for Brazilian context

## Defensive workflow

1. Define the protected organization/sector.
2. Build an asset and supplier hypothesis from public sources.
3. Use passive internet-measurement/search services first.
4. Correlate domains, certificates, IP space, vendors and exposed technologies.
5. Map threat actors, campaigns, malware and TTPs in MISP/OpenCTI.
6. Validate exposure only with authorization.
7. Feed defensible findings into detection engineering, threat hunting and risk reduction.

OSINT4ALL intentionally does not provide operational instructions for interacting with live industrial control systems.
