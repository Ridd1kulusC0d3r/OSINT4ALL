# AI-Assisted OSINT

AI can accelerate OSINT, but it can also manufacture convincing nonsense at industrial speed.

## Appropriate roles

- query expansion;
- translation assistance;
- OCR cleanup;
- entity candidate extraction;
- tagging and classification;
- summarization with source references;
- duplicate detection;
- schema normalization;
- hypothesis generation;
- timeline drafting;
- analyst notebook assistance.

## Required guardrails

1. **AI output is not a source.**
2. Preserve the underlying source and citation.
3. Separate extracted facts from model-generated inference.
4. Never convert identity similarity into identity proof.
5. Do not silently fill missing dates, locations, relationships or motivations.
6. Revalidate high-impact claims manually.
7. Log model-assisted transformations when they materially affect an intelligence product.

## AI confidence pattern

    Source evidence
        ↓
    Machine extraction
        ↓
    Candidate entities / relationships
        ↓
    Human validation
        ↓
    Corroboration
        ↓
    Analytical judgment

## Upstream lesson

Astrosp exposes how quickly AI-related OSINT tooling is expanding. OSINT4ALL therefore treats **AI as an analytical layer**, not as a new magical intelligence discipline.
