# Code Repository OSINT

Public source-code platforms are valuable OSINT surfaces because they expose repositories, commits, contributor identities, organizations, release history, issues and other public metadata.

## Core references

| Resource | Focus | Status |
|---|---|---|
| [Bellingcat Octosuite](https://github.com/bellingcat/octosuite) | GitHub user, repository, organization and search analysis | 🟢 |
| [GitFive](https://github.com/mxrch/GitFive) | GitHub identity correlation | 🟡 |
| [GitHub](https://github.com/) | Primary source for public repository metadata | primary source |

## Analyst questions

- Which account or organization owns the repository?
- What is the commit/release chronology?
- Which public identities contributed?
- Which public repositories share names, organizations or observable patterns?
- Did a project rename, transfer ownership, archive or move?
- Which finding comes directly from GitHub versus a third-party interpretation?

## Evidence rule

A repository username, email in Git history or shared naming pattern is **not sufficient identity proof**. Treat it as a candidate association and corroborate independently.

## Safety boundary

This catalog focuses on public metadata, provenance, history and identity research. It does not turn exposed secrets or credentials into an operational playbook.
