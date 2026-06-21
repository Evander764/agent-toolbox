# Thread Orchestration

Use this reference when `$think` needs automatic Codex windows.

## Tool Flow

1. Call `list_projects` and choose the current project. Default for this skill:
   `/Users/evander/Documents/Agent thinking`.
2. Create the run folder with `scripts/new_session.py`.
3. Write the problem brief, draft standards, hard standards, standards package,
   logic orchestration, engineering governance, project link, project dispatch,
   and initial modules before launching role windows.
4. For each active role, call `create_thread` with:
   - target type: `project`;
   - projectId: the current project id;
   - environment: `local`;
   - no model override unless explicitly requested by the user;
   - a self-contained role prompt.
5. Rename each thread with `set_thread_title`, using:
   `think <short-topic> - <role>`.
6. Record each thread id in `thread-routing.md`.
7. Use `read_thread` to collect role status and summaries. Use
   `send_message_to_thread` for revision packets or continuation prompts.
8. Archive only temporary validation threads. Do not archive real thinking-room
   agent windows unless the user asks or the session is explicitly closed.

## Required Role Prompt Shape

Each role prompt must include:

- `$think` session path;
- exact role name;
- exact output file under `agents/`;
- for `Standards Judge`, exact authorization to write both
  `agents/standards-judge.md` and `verdict.md`;
- assigned packet or module;
- acceptance gates from `standards.md` and `hard-standards.md`;
- relevant state, dependency, recovery, and open-loop requirements from
  `logic-orchestration.md`;
- relevant validation, evidence, rollback, and ownership requirements from
  `engineering-governance.md`;
- project link and dispatch expectations when project-related;
- instruction not to edit other role files;
- required response format: file written, summary, blockers, next needed input.

## Routing State

`thread-routing.md` is the source of truth for live windows.

Required columns:

- role;
- thread_title;
- thread_id;
- output_file;
- status;
- last_prompt;
- last_read_at;

`message-queue.md` is the source of truth for work movement.

Allowed statuses:

- `queued`;
- `sent`;
- `read`;
- `needs-revision`;
- `accepted`;
- `blocked`.
- `unconfirmed`;
- `recovered`.

When a thread id is returned but title assignment or readback fails, record the
row as `unconfirmed`, add the incident to `logic-orchestration.md`, retry
readback once, and only mark it `sent` or `recovered` after the thread is
confirmed.

`project-link.md` records which existing project this run is meant to serve.
When project linkage is relevant, fill its candidate table before final
synthesis. If several candidates exist, choose the highest score and record the
reason.

`project-dispatch.md` records whether the hard standards package was handed to
the selected project. If the project has a team `message-queue.md`, dispatch by
creating exactly one project-side packet and queue row. Default receiver is
`协调师`; if no coordinator surface exists but a planner exists, use `规划师`.
If direct thread delivery cannot be confirmed, mark dispatch as blocked or
inbox-only and provide a fallback copy block. Do not claim a project thread was
notified unless it was actually messaged.

If no project is found, fill `project-start-prompt.md` instead of creating a
new project automatically.

## Default Launch Order

Launch in this order:

1. `Standards Judge`;
2. `Systems Decomposer`;
3. `Red Team Devil's Advocate`;
4. `Evidence & Mental Models Strategist`.

The judge launches first so its standards can be used as the gate for all later
work. The Conductor may still revise standards after reading the decomposer's
module split.

## Fallback

If thread tools are unavailable:

- mark `mode: simulated`;
- fill `thread-routing.md` with `unavailable`;
- record the degraded mode and recovery decision in `logic-orchestration.md`;
- record the missing tool gate in `engineering-governance.md` when the run is
  changing durable files or project state;
- run the same roles in the current thread;
- do not claim separate windows existed.
