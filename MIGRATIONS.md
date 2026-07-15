# Migration provenance

This file records how former standalone repositories were incorporated into the toolbox. It is an audit trail, not authorization to delete a source repository.

## 2026-07-15 repository consolidation

| Source repository | Source HEAD | Destination | Result |
| --- | --- | --- | --- |
| `Evander764/think-skill` | `236a5d25f78a0c113930d3d87154f3fd6c4bdb06` | `skills/think/` | All 16 committed blobs already matched the toolbox exactly; no file copy was needed. |
| `Evander764/team-skill` | `0a180cda4c722a31ae5f3bc42459bea7105035d0` | `skills/team/` | README matched. The toolbox `SKILL.md` contains the newer explicit thread-creation and routing rule, so the toolbox version was retained. |
| `Evander764/xhs-auto-deploy` | `2a1848e22629080f4917ce191720141c3c1289fa` | `skills/xhs-auto-deploy/` | Imported with Git subtree history; five source files were new at this prefix. |

Before any source repository is archived or deleted, verify the destination paths, the recorded source HEAD, and the external backup manifest maintained by the repository-governance project.
