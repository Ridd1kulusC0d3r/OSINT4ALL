# Agentic OSINT

OSINT Shifu maintains a dedicated view of implementation-bearing **skills, plugins, MCP servers and agent integrations**. OSINT4ALL adopts the concept, with stricter provenance rules.

## Selected references

| Resource | Integration | Role | Status |
|---|---|---|---|
| [UseOSINT Skills](https://github.com/UseOSINT/Skills) | Skill pack | Source-grounded analyst workflows and evidence grading | 🟢 |
| [World Intel MCP](https://github.com/marc-shade/world-intel-mcp) | MCP server | Multi-source research, monitoring and situation briefs | 🟡 |

## What belongs here

Agentic tooling is useful when it:

- keeps underlying sources visible;
- records queries and pivots;
- distinguishes tool output from analyst judgment;
- can attach confidence/provenance to assertions;
- supports reproducible workflows;
- does not silently transform a candidate identity into a confirmed identity.

## What does not count as evidence

- an LLM summary;
- an agent-generated relationship;
- a generated timeline entry without a source;
- a confidence score with no evidence trail.

## Safe architecture

    Analyst requirement
          ↓
    Agent selects tools
          ↓
    Tool output + source
          ↓
    Candidate finding
          ↓
    Human / rule validation
          ↓
    Corroboration
          ↓
    Evidence graph
          ↓
    Assessment

## OSINT4ALL direction

Future agent integrations should consume the canonical resource graph and return structured findings containing source references, timestamps, evidence labels and confidence rather than prose-only answers.
