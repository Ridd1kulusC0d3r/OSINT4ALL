# Investigation Workbenches

Tool lists answer **where can I search?** Workbenches answer **how do I organize the investigation after I start finding things?**

## Selected projects

| Resource | Analyst value | Status |
|---|---|---|
| [OpenTrace](https://github.com/Gacut/OpenTrace) | Offline case organization, relationships, sources, hypotheses and integrity metadata | 🟢 |
| [FollowTheMoney](https://github.com/alephdata/followthemoney) | Investigative entity/data model for people, companies, assets, payments and cases | 🟢 |
| [Timesketch](https://github.com/google/timesketch) | Collaborative timeline search and annotation | 🟡 |
| [Flowsint](https://github.com/reconurge/flowsint) | Graph-based entity investigation and enrichment | 🟡 |
| [Maltego](https://www.maltego.com/) | Link analysis and entity correlation | 🟡 |

## Desired OSINT4ALL case model

    Case
      ├── Intelligence Requirement
      ├── Scope / Red Lines
      ├── Entities
      ├── Relationships
      ├── Sources
      ├── Evidence
      ├── Timeline
      ├── Hypotheses
      ├── Alternative Hypotheses
      ├── Confidence
      └── Dissemination

## Design lesson

The strongest idea surfaced by OSINT Shifu's investigation category is that collection and case management should be separate layers.

A tool can find a lead. The workbench should preserve **why that lead matters, where it came from, how it relates to other evidence, and how confident the analyst is**.
