# Evidence Capture & Preservation

OSINT is only useful when an analyst can explain **what was observed, where it came from, when it was captured, and what changed later**.

This catalog adds the preservation layer that many tool lists forget.

## Core references

| Resource | Primary role | Validation |
|---|---|---|
| [ArchiveBox](https://github.com/ArchiveBox/ArchiveBox) | Self-hosted web archiving | 🟡 |
| [Bellingcat auto-archiver](https://github.com/bellingcat/auto-archiver) | Automated preservation of public online material | 🟡 |
| [Internet Archive Wayback Machine](https://web.archive.org/) | Historical web snapshots | 🟡 |
| [Internet Archive CLI](https://github.com/jjjake/internetarchive) | Programmatic archive access | 🟡 |
| [gowitness](https://github.com/sensepost/gowitness) | Reproducible web screenshots | 🟡 |
| [Monolith](https://github.com/Y2Z/monolith) | Single-file page capture | 🟡 |
| [HTTrack](https://www.httrack.com/) | Offline website copies | 🟡 |
| [yt-dlp](https://github.com/yt-dlp/yt-dlp) | Public-media acquisition where lawful | 🟡 |
| [gallery-dl](https://github.com/mikf/gallery-dl) | Public image/media acquisition where lawful | 🟡 |
| [FFmpeg](https://ffmpeg.org/) | Media conversion and frame extraction | 🟡 |
| [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) | Text extraction from images/documents | 🟡 |
| [Dangerzone](https://github.com/freedomofpress/dangerzone) | Safer handling of untrusted documents | 🟡 |
| [MAT2](https://0xacab.org/jvoisin/mat2) | Metadata hygiene | 🟡 |

## Analyst workflow

    Source discovered
        ↓
    Canonical URL recorded
        ↓
    Capture / archive
        ↓
    Timestamp + provenance
        ↓
    Hash when appropriate
        ↓
    Extract metadata / OCR / frames
        ↓
    Analytical note
        ↓
    Corroboration
        ↓
    Evidence package

## Minimum provenance record

For every important finding record:

- canonical URL;
- capture time and timezone;
- original publication time if known;
- title/account/source name;
- capture method;
- archive URL when available;
- relevant metadata;
- analyst observation;
- what is fact, claim, inference or unresolved;
- relationship to the intelligence requirement.

Preservation does not prove authenticity. It preserves what was observable at a point in time.
