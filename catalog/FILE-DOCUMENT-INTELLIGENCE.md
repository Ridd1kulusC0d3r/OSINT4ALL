# File & Document Intelligence

Selected resources:

| Resource | Role | Status |
|---|---|---|
| [FileGrail](https://github.com/osintshifu/filegrail) | File provenance, metadata, timeline, pivots and evidence relationships | 🟢 |
| [unmasker](https://github.com/osintshifu/unmasker) | Hidden/residual content and failed-redaction detection | 🟢 |
| [ICIJ Datashare](https://github.com/ICIJ/datashare) | Large-scale document search, OCR, metadata and entity extraction | 🟢 |
| [ExifTool](https://exiftool.org/) | Embedded metadata analysis | 🟡 |
| [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) | OCR | 🟡 |
| [Dangerzone](https://github.com/freedomofpress/dangerzone) | Safer handling of untrusted documents | 🟡 |
| [OpenRefine](https://github.com/OpenRefine/OpenRefine) | Dataset cleaning and normalization | 🟡 |

Workflow: preserve original → hash/identify → safer inspection → metadata/structure/OCR → candidate pivots → exact provenance → external corroboration → report + confidence.

A hidden string, metadata value or OCR result is a finding to validate, not a truth oracle.
