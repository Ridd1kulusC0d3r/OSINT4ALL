# Environmental OSINT

> Focus: deforestation, land-use change, fires, environmental crime, wildlife, remote sensing and reproducible geospatial evidence.

## Curated references

| Resource | Focus | Status |
|---|---|---|
| Bellingcat Online Investigation Toolkit — Environment & Wildlife | Environmental/wildlife investigation tools | 🟡 |
| The-OSINT-Newsletter / OSINT Tools Library | Environmental and geospatial tools | 🟡 |
| ECOSINT / RSF | Environmental investigation methodology using open sources | 🟡 |
| Jieyab89/OSINT-Cheat-sheet | Satellite/geospatial resources | 🟡 |

## Forest and land monitoring

| Platform | Use | Status |
|---|---|---|
| Global Forest Watch | Forest loss, fires, land-use context and alert layers | 🟡 |
| Earth Index / Earth Genome | Visual-similarity search across satellite imagery | 🟡 |
| MapBiomas Alerta | Brazilian deforestation-alert validation | 🟡 |
| TerraBrasilis / INPE | PRODES, DETER and Brazilian environmental data | 🟡 |
| Open Foris / FAO | Open forest/land monitoring tools | 🟡 |

## Alert systems

| System | Use | Status |
|---|---|---|
| DETER / INPE | Near-real-time deforestation/degradation alerts for enforcement support | 🟡 |
| DETER Não Floresta | Monitoring of non-forest vegetation and land-use disturbance; verify current coverage | 🟡 |
| GLAD | Forest-loss alert ecosystem | 🟡 |
| RADD | Radar-based forest-disturbance alerts | 🟡 |
| DIST-ALERT | Vegetation disturbance alert layer | 🟡 |

## SAR and cloud-resistant monitoring

| Resource | Use | Status |
|---|---|---|
| ICEYE | Commercial SAR imagery/monitoring | 🟡 |
| Sentinel-1 | Open SAR Earth-observation data | 🟡 |

SAR is especially valuable where persistent cloud cover limits optical imagery, but interpretation still requires sensor-aware analysis and corroboration.

## Analysis and processing

| Tool | Use | Status |
|---|---|---|
| Google Earth Engine | Large-scale geospatial processing | 🟡 |
| QGIS | Desktop GIS | 🟡 |
| PostgreSQL/PostGIS | Spatial storage and analysis | 🟡 |
| LandTrendr | Time-series disturbance/recovery analysis | 🟡 |
| CCDC | Continuous change-detection methodology/tooling | 🟡 |
| SATVeg / Embrapa | Vegetation time-series analysis in Brazil | 🟡 |

## Data and APIs

| Resource | Use | Status |
|---|---|---|
| Global Forest Watch Data API | Programmatic environmental datasets | 🟡 |
| TerraBrasilis API | Brazilian deforestation/fire datasets | 🟡 |
| GFW Scraper / Apify | Third-party access wrapper; verify terms and current implementation | 🟡 |
| EUDR Parcel Screener / JRC | Deforestation-regulation parcel screening context | 🟡 |

## Brazil-specific resources

| Resource | Focus | Status |
|---|---|---|
| PRODES / INPE | Annual deforestation monitoring | 🟡 |
| DETER / INPE | Enforcement-support alerts | 🟡 |
| Censipam | Amazon protection/situational-awareness systems | 🟡 |
| Imazon | Amazon research and monitoring | 🟡 |
| MADES / Imasul-MS | Mato Grosso do Sul deforestation alerts | 🟡 |
| SCCON / Planet ecosystem | Commercial imagery/monitoring context | 🟡 |
| MapBiomas Alerta | National multi-biome alert validation | 🟡 |

## Investigation workflow

1. **Discovery** — identify an area of interest using alerts or public reports.
2. **Baseline** — establish historical imagery and land-cover context.
3. **Time series** — compare before/after imagery and change-detection outputs.
4. **Cloud problem** — add SAR where optical imagery is blocked.
5. **Ownership/context** — correlate with lawful land, company, permit and public-record data.
6. **Field corroboration** — use local reporting, official notices and other independent sources.
7. **Evidence package** — preserve coordinates, imagery dates, layers, queries, exports and analytical caveats.

## Key limitations

- Resolution limits can hide small-scale change.
- Alerts indicate possible disturbance, not automatically cause or responsibility.
- Cloud, smoke and sensor artifacts can mislead.
- Ownership/cadastre data may be incomplete or contested.
- Commercial imagery access can change.
- A geospatial correlation is not, by itself, proof of legal responsibility.
