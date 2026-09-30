# Conflict OSINT

> **Purpose:** verification, journalism, human-rights documentation, research and situational awareness.
>
> **Default status:** 🟡 Needs review. Conflict data is time-sensitive, incomplete and frequently manipulated. Never treat a single feed, map, social post or tracker as definitive.

## Real-time dashboards and situational-awareness platforms

| Platform | Focus | Status |
|---|---|---|
| World Monitor | Multi-source global situational awareness across news, conflict, cyber, aviation, maritime, finance, energy and weather | 🟡 |
| ShadowBroker | Self-hosted multi-feed map with aviation, maritime, satellite and conflict context | 🟡 |
| Third-Eye | Multi-domain live OSINT layers including conflict, aviation, maritime, CCTV, weather, space and cyber | 🟡 |
| OSIRIS | Conflict and multi-domain situational-awareness dashboard | 🟡 |
| OSINT War Room / Hue-Jhan | Conflict/geopolitical dashboard concept using multiple public feeds | 🟡 |
| IRONSIGHT | Theater-oriented multi-source situational-awareness dashboard; verify current scope and sources | 🟡 |

## Aviation

| Resource | Use | Status |
|---|---|---|
| ADS-B Exchange | Public aircraft tracking including many aircraft omitted elsewhere | 🟡 |
| Flightradar24 | Commercial/public aviation tracking | 🟡 |
| FlightAware | Commercial/public aviation tracking | 🟡 |
| OpenSky Network | Research/open aviation data ecosystem | 🟡 |
| adsb.lol | Community ADS-B data source | 🟡 |

**Limitation:** absence from an ADS-B feed is not proof of absence. Aircraft may not broadcast, may be filtered, or may be outside sensor coverage.

## Maritime

| Resource | Use | Status |
|---|---|---|
| MarineTraffic | AIS-based vessel tracking | 🟡 |
| VesselFinder | AIS-based vessel tracking | 🟡 |
| FleetMon | AIS-based vessel tracking | 🟡 |
| AISStream.io | AIS data/API source | 🟡 |
| Global Fishing Watch | Vessel/fishing activity analysis | 🟡 |
| Theia / Synmax | Commercial maritime intelligence using multiple data sources | 🟡 |

**Limitation:** AIS can be absent, delayed, spoofed, intentionally disabled or misinterpreted.

## Satellite imagery and remote sensing

- Sentinel Hub / EO Browser
- Planet Labs
- Google Earth Pro
- NASA FIRMS
- MizarVision — verify current service, provenance and analytical claims

Satellite imagery should be treated with acquisition date, resolution, cloud cover, sensor type and processing limitations recorded.

## Evidence, verification and human-rights documentation

| Resource | Role | Status |
|---|---|---|
| WarTrace / 4lp1ne | Collection of verification/documentation tools | 🟡 |
| Bayanat / SJAC | Evidence/documentation platform related to Syria and regional accountability work | 🟡 |
| GeoConfirmed | Community geolocation/verification of conflict events | 🟡 |
| Berkeley Protocol | Methodological standard for digital open-source investigations | 🟡 |
| Meedan | Verification and information-integrity resources | 🟡 |
| WITNESS | Human-rights video documentation and preservation guidance | 🟡 |

## Social media and public-channel monitoring

| Resource | Use | Status |
|---|---|---|
| Third-Eye Telegram layer | Public-channel geospatial/contextual monitoring | 🟡 |
| OSIRIS Telegram layer | Public-channel monitoring/context | 🟡 |
| WarWatch | Aggregated conflict reporting and public-source context | 🟡 |
| Twint | Historical Twitter/X scraping project | ⚪ |
| TweetScraper | Twitter/X scraping ecosystem; implementation-dependent | 🟡 |
| Osintgram | Public Instagram research | 🟡 |
| HateSonar | Hate-speech detection research | 🟡 |

## Curated references

- Jieyab89/OSINT-Cheat-sheet — conflict/military-related sections
- danielrosehill/Geopolitical-And-OSINT-Index
- xksh808dsh-bit/Awesome-OSINT-List
- cognis-digital/awesome-drone-warfare-osint
- ARES / Armament Research Services

## Ukraine-focused resources included in the source inventory

| Resource | Role | Status |
|---|---|---|
| DeepState Map | Front-line/situational map; use as one source among several | 🟡 |
| eyesonrussia | Conflict event collection/verification ecosystem | 🟡 |
| ODCR Assistant | AI-assisted collection concept reported in Ukrainian defense context; verify current public information | 🟡 |
| cyberwar-tools-ua | Cyber/OSINT toolkit collection; review carefully before use | 🟡 |

## Evidence workflow

1. Preserve the original source and URL.
2. Record timestamp, account/channel identity and collection context.
3. Archive the material where lawful and appropriate.
4. Extract frames/metadata without assuming authenticity.
5. Geolocate using independent visual/geospatial references.
6. Chronolocate using shadows, weather, sequencing and corroborating posts when possible.
7. Compare against satellite, aviation, maritime and official reporting.
8. Record alternative hypotheses.
9. Separate **observed fact**, **source claim**, **analyst inference** and **confidence**.
10. For accountability work, follow an evidentiary methodology such as the Berkeley Protocol and preserve chain-of-custody information.

## Safety and ethics

Do not publish unnecessarily precise information that could expose civilians, witnesses, humanitarian workers, journalists or other vulnerable people to harm. OSINT4ALL does not provide tactical targeting guidance.
