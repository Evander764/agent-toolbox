# Think Skill

`$think` is a Codex second-brain skill for multi-window reasoning rooms,
hard-standard extraction, adversarial review, project dispatch, mental-model
selection, logic orchestration, and engineering governance.

## Key Files

- `SKILL.md`: skill entrypoint and operating contract.
- `references/logic-orchestration.md`: state machine, dependencies, handoffs,
  recovery ledger, and open-loop handling.
- `references/engineering-governance.md`: scope, ownership, validation,
  rollback, drift, and maintenance rules.
- `scripts/new_session.py`: creates run folders and required artifacts.
- `scripts/validate_models.py`: validates the skill package and model library.

## Validate

```bash
python3 scripts/validate_models.py --self-test
```
