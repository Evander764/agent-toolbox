# Mental Models Router

This file is the call protocol, not the full library. The full 100-card
Munger-style operating library lives in `references/mental-models-100.md`.

Use mental models as decision lenses. Do not decorate an answer with model
names. A selected model must change at least one of:

- the diagnosis;
- the recommended action;
- a hard standard;
- the next experiment;
- the evidence needed before deciding.

## When To Use

Use this router for any non-trivial judgment, strategy, business, product,
learning, investment, life, system design, or project decision.

Skip the full 100-model scan only when the task is trivial, purely mechanical,
or already answered by a direct local fact.

## Full Candidate Pool

For every non-trivial run, treat all 100 cards in
`references/mental-models-100.md` as the candidate pool. Do not rely on memory
or free association when the library is available.

The library is original/paraphrased and grouped by:

- Core rationality, 12;
- Probability and math, 14;
- Incentives and economics, 14;
- Systems and engineering, 14;
- Psychology and bias, 22;
- Biology and evolution, 8;
- Strategy and competition, 8;
- Learning, execution, and organizations, 8.

## Selection Protocol

1. Classify the problem domain:
   - decision under uncertainty;
   - human behavior or incentives;
   - system design or operations;
   - strategy or competition;
   - learning, execution, or organization;
   - personal life, health, or career;
   - mixed/unclear.
2. Scan all 100 model cards as candidates.
3. Shortlist 10-15 models whose `when_to_use` or `diagnostic_question` matches
   the problem.
4. Select 3-9 models that materially change the answer.
5. Record 2-5 tempting-but-rejected models and why they did not change the
   decision.
6. Convert selected models into evidence, standards, or experiments.

## Selection Tests

A model is selected only if at least one sentence can complete this pattern:

```text
Model -> what it changes -> implication -> evidence/experiment
```

Reject the model if it only restates the obvious, names a bias without changing
behavior, or produces no evidence requirement.

## Required Output File

For every non-trivial `$think` run, write `mental-models-selected.md` in the run
folder.

Use this template:

```markdown
# Mental Models Selected: <topic>

- status: draft | accepted | needs-revision | blocked
- source_library: references/mental-models-100.md
- candidate_pool: 100
- selected_count:
- problem_domain:

## Selection Method

How the domain was classified and how the full 100-card library was scanned.

## Selected Models

| id | model | family | what it changes | implication | evidence or experiment |
| --- | --- | --- | --- | --- | --- |
| M001 |  |  |  |  |  |

## Tempting Rejected Models

| id | model | why rejected |
| --- | --- | --- |

## Standards And Experiment Changes

- Hard standards changed:
- Experiments changed:
- Decision card changes:
```

## Judge Rule

The Standards Judge must reject any final synthesis that:

- does not show the full library was treated as the candidate pool;
- selects fewer than 3 or more than 9 models for a non-trivial run without a
  recorded reason;
- lists models without implications;
- has no tempting rejected models;
- fails to translate selected models into a standard, experiment, or evidence
  requirement.
