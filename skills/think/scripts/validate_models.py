#!/usr/bin/env python3
"""Validate the Think skill package and its 100-card mental model library."""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from collections import Counter
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_LIBRARY = SKILL_ROOT / "references" / "mental-models-100.md"
DEFAULT_SKILL_FILE = SKILL_ROOT / "SKILL.md"
DEFAULT_SESSION_SCRIPT = SKILL_ROOT / "scripts" / "new_session.py"

REQUIRED_REFERENCE_FILES = [
    "protocol.md",
    "agent-roles.md",
    "thread-orchestration.md",
    "logic-orchestration.md",
    "engineering-governance.md",
    "quality-gates.md",
    "outputs.md",
    "mental-models.md",
    "mental-models-100.md",
]

REQUIRED_SKILL_TERMS = [
    "逻辑编排",
    "工程治理",
    "logic-orchestration.md",
    "engineering-governance.md",
    "--self-test",
]

REQUIRED_TEMPLATE_ARTIFACTS = [
    "logic-orchestration.md",
    "engineering-governance.md",
]

REQUIRED_GATE_FILES = {
    "references/protocol.md": [
        "Logic Orchestration",
        "Engineering Governance",
        "logic-orchestration.md",
        "engineering-governance.md",
        "--self-test",
    ],
    "references/agent-roles.md": [
        "logic orchestration",
        "engineering governance",
        "logic-orchestration.md",
        "engineering-governance.md",
    ],
    "references/thread-orchestration.md": [
        "logic orchestration",
        "engineering governance",
        "unconfirmed",
        "recovered",
    ],
    "references/quality-gates.md": [
        "Logic Orchestration Gates",
        "Engineering Governance Gates",
        "logic-orchestration.md",
        "engineering-governance.md",
        "--self-test",
    ],
    "references/outputs.md": [
        "logic-orchestration.md",
        "engineering-governance.md",
        "Logic Orchestration",
        "Engineering Governance",
    ],
}

REQUIRED_FIELDS = {
    "id",
    "name",
    "family",
    "when_to_use",
    "diagnostic_question",
    "what_it_changes",
    "failure_mode",
    "evidence_to_seek",
    "pairs_with",
}

EXPECTED_FAMILY_COUNTS = {
    "Core rationality": 12,
    "Probability and math": 14,
    "Incentives and economics": 14,
    "Systems and engineering": 14,
    "Psychology and bias": 22,
    "Biology and evolution": 8,
    "Strategy and competition": 8,
    "Learning, execution, and organizations": 8,
}


def parse_cards(text: str) -> list[dict[str, str]]:
    cards: list[dict[str, str]] = []
    current: dict[str, str] | None = None

    for line in text.splitlines():
        heading = re.match(r"^##\s+(M\d{3})\s+-\s+(.+?)\s*$", line)
        if heading:
            if current is not None:
                cards.append(current)
            current = {"_heading_id": heading.group(1), "_heading_name": heading.group(2)}
            continue

        if current is None:
            continue

        field = re.match(r"^-\s+([a-z_]+):\s*(.*)$", line)
        if field:
            current[field.group(1)] = field.group(2).strip()

    if current is not None:
        cards.append(current)

    return cards


def validate(cards: list[dict[str, str]]) -> list[str]:
    errors: list[str] = []

    if len(cards) != 100:
        errors.append(f"expected 100 cards, found {len(cards)}")

    ids = [card.get("id", "") for card in cards]
    names = [card.get("name", "") for card in cards]
    duplicate_ids = [item for item, count in Counter(ids).items() if item and count > 1]
    duplicate_names = [item for item, count in Counter(names).items() if item and count > 1]
    if duplicate_ids:
        errors.append(f"duplicate ids: {', '.join(sorted(duplicate_ids))}")
    if duplicate_names:
        errors.append(f"duplicate names: {', '.join(sorted(duplicate_names))}")

    expected_ids = [f"M{index:03d}" for index in range(1, 101)]
    missing_ids = sorted(set(expected_ids) - set(ids))
    extra_ids = sorted(set(ids) - set(expected_ids))
    if missing_ids:
        errors.append(f"missing ids: {', '.join(missing_ids)}")
    if extra_ids:
        errors.append(f"unexpected ids: {', '.join(extra_ids)}")

    family_counts = Counter(card.get("family", "") for card in cards)
    for family, expected_count in EXPECTED_FAMILY_COUNTS.items():
        actual_count = family_counts.get(family, 0)
        if actual_count != expected_count:
            errors.append(
                f"family count mismatch for {family}: expected {expected_count}, found {actual_count}"
            )
    unknown_families = sorted(set(family_counts) - set(EXPECTED_FAMILY_COUNTS))
    if unknown_families:
        errors.append(f"unknown families: {', '.join(unknown_families)}")

    id_set = set(ids)
    for index, card in enumerate(cards, start=1):
        label = card.get("id") or card.get("_heading_id") or f"card {index}"
        missing_fields = sorted(field for field in REQUIRED_FIELDS if not card.get(field))
        if missing_fields:
            errors.append(f"{label}: missing required fields: {', '.join(missing_fields)}")

        if card.get("_heading_id") != card.get("id"):
            errors.append(f"{label}: heading id does not match id field")
        if card.get("_heading_name") != card.get("name"):
            errors.append(f"{label}: heading name does not match name field")

        if not card.get("when_to_use", "").strip():
            errors.append(f"{label}: when_to_use trigger is empty")
        if not card.get("evidence_to_seek", "").strip():
            errors.append(f"{label}: evidence_to_seek prompt is empty")

        pairs = [item.strip() for item in card.get("pairs_with", "").split(",") if item.strip()]
        if not pairs:
            errors.append(f"{label}: pairs_with must contain at least one model id")
        for pair in pairs:
            if pair not in id_set:
                errors.append(f"{label}: pairs_with references unknown id {pair}")

    return errors


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError as exc:
        raise RuntimeError(f"could not read {path}: {exc}") from exc


def validate_skill_structure() -> list[str]:
    errors: list[str] = []
    references_dir = SKILL_ROOT / "references"

    for filename in REQUIRED_REFERENCE_FILES:
        path = references_dir / filename
        if not path.exists():
            errors.append(f"missing required reference file: references/{filename}")
        elif not read_text(path).strip():
            errors.append(f"empty required reference file: references/{filename}")

    skill_text = read_text(DEFAULT_SKILL_FILE)
    for term in REQUIRED_SKILL_TERMS:
        if term not in skill_text:
            errors.append(f"SKILL.md missing required term: {term}")

    session_script_text = read_text(DEFAULT_SESSION_SCRIPT)
    for artifact in REQUIRED_TEMPLATE_ARTIFACTS:
        if artifact not in session_script_text:
            errors.append(f"new_session.py does not create or reference {artifact}")

    for relative_path, required_terms in REQUIRED_GATE_FILES.items():
        path = SKILL_ROOT / relative_path
        if not path.exists():
            errors.append(f"missing gate file: {relative_path}")
            continue
        text = read_text(path)
        for term in required_terms:
            if term not in text:
                errors.append(f"{relative_path} missing required term: {term}")

    return errors


def first_error_line(text: str) -> str:
    for line in text.splitlines():
        if line.startswith("- ") or "missing" in line or "does not" in line:
            return line
    return text.splitlines()[0] if text.splitlines() else ""


def run_negative_self_tests() -> list[str]:
    """Prove the validator fails on representative fake-compliance fixtures."""

    errors: list[str] = []

    def run_scenario(name: str, mutate) -> None:
        with tempfile.TemporaryDirectory(prefix="think-validator-negative-") as tmp:
            target = Path(tmp) / "think"
            shutil.copytree(
                SKILL_ROOT,
                target,
                ignore=shutil.ignore_patterns("__pycache__", "*.pyc"),
            )
            mutate(target)
            proc = subprocess.run(
                [sys.executable, str(target / "scripts" / "validate_models.py")],
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=False,
            )
            if proc.returncode == 0:
                errors.append(f"{name}: expected failure, got success")
                return
            print(
                f"negative self-test passed: {name}: "
                f"{first_error_line(proc.stderr + proc.stdout)}"
            )

    run_scenario(
        "missing logic reference",
        lambda root: (root / "references" / "logic-orchestration.md").unlink(),
    )

    def remove_generator_artifact(root: Path) -> None:
        path = root / "scripts" / "new_session.py"
        text = path.read_text(encoding="utf-8")
        path.write_text(
            text.replace("logic-orchestration.md", "logic-orchestration-MISSING.md"),
            encoding="utf-8",
        )

    run_scenario("missing generator artifact", remove_generator_artifact)

    def remove_quality_gate(root: Path) -> None:
        path = root / "references" / "quality-gates.md"
        text = path.read_text(encoding="utf-8")
        path.write_text(
            text.replace("Logic Orchestration Gates", "Logic Gates Removed"),
            encoding="utf-8",
        )

    run_scenario("missing quality gate heading", remove_quality_gate)

    def remove_skill_term(root: Path) -> None:
        path = root / "SKILL.md"
        text = path.read_text(encoding="utf-8")
        path.write_text(text.replace("逻辑编排", "LOGIC_TERM_REMOVED"), encoding="utf-8")

    run_scenario("missing Chinese capability term", remove_skill_term)
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Think skill package.")
    parser.add_argument("--library", default=str(DEFAULT_LIBRARY), help="Path to mental-models-100.md")
    parser.add_argument(
        "--self-test",
        action="store_true",
        help="Also run negative fixtures to prove fake compliance fails.",
    )
    args = parser.parse_args()

    library = Path(args.library).expanduser()
    text = library.read_text(encoding="utf-8")
    cards = parse_cards(text)
    errors = validate(cards)
    errors.extend(validate_skill_structure())

    if errors:
        print(f"model validation failed: {len(errors)} error(s)", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("think skill validation passed")
    print("model validation passed: 100/100 cards valid")
    for family, count in EXPECTED_FAMILY_COUNTS.items():
        print(f"- {family}: {count}")

    if args.self_test:
        self_test_errors = run_negative_self_tests()
        if self_test_errors:
            print(
                f"negative self-tests failed: {len(self_test_errors)} error(s)",
                file=sys.stderr,
            )
            for error in self_test_errors:
                print(f"- {error}", file=sys.stderr)
            return 1
        print("negative self-tests passed: 4/4 fixtures rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
