# Target Input Taxonomy

Version 0.3.2 adds an optional `target_inputs` field inspired by the input-oriented catalogue model used by OSINT Shifu.

## Why it matters

Analysts usually do not begin with a category. They begin with **something observable**.

Examples:

- username;
- email;
- phone number;
- name;
- domain;
- IP address;
- URL;
- repository URL;
- image;
- video;
- document;
- file hash;
- coordinates;
- organization name;
- event data.

The useful question is therefore:

> **What can I do with the thing I already have?**

rather than:

> Which folder did someone put the tool in?

## Canonical values

The current controlled vocabulary lives in `data/taxonomies.json`.

It includes:

`aircraft-id · asn · audio · bssid-ssid · cidr · coordinates · crypto-address · cve-id · dataset · document · domain · email · event-data · file · file-hash · image · ip-address · keyword · location · name · onion-service · organization-name · phone-number · repository-url · text · url · username · video · no-fixed-input`

## Implementation type

Version 0.3.2 also adds optional `implementation_type` metadata:

`cli · desktop · library · web-app · browser-extension · framework · platform · dataset-tool · skill · skill-pack · plugin · mcp-server · agent · agent-plus-mcp · service · meta-index`

This prevents a hosted website, Python library, MCP server and desktop case manager from looking like interchangeable things merely because all four are links.

## Generated view

See [catalog/INPUTS.generated.md](../catalog/INPUTS.generated.md).

Input coverage is incremental. Missing `target_inputs` values are treated as a classification backlog, not silently guessed.
