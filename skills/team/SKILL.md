---
name: team
description: >
  Use when the user wants multiple AI chat windows or agents to self-organize as
  an AI team with minimal typing. Trigger on "/team", "$team", "项目：",
  "身份：", "团队：", "组队", "AI团队", "多Agent协作", "多 agent 协作", or requests
  to make agents register themselves, discover teammates, claim tasks, execute,
  review, and hand off through shared files. The `审核官` role may use
  `/neat-freak` for knowledge cleanup, documentation consistency, and clean
  handoff review.
metadata:
  short-description: Minimal self-organizing AI team
---

# Team

Use this skill to turn two or more AI chat windows into a self-organizing team.

The user should only need to type one of these:

```text
项目：<目标>
```

or:

```text
/team 项目：<目标>
```

After the team shell exists, the first role prompt must be a self-contained
copy block:

```text
/team 规划师
团队：<team_id>
```

If no identity is specified, `/team` means `规划师`.
Do not output only `/team` as the next prompt after creating a project shell;
that forces the user and future agents to rely on hidden current-team state.

## Core Principle

Agents do not rely on hidden chat history to coordinate. They coordinate through
a shared team folder. Every agent must:

1. register itself;
2. scan teammates;
3. read the task board;
4. claim suitable work;
5. update shared state;
6. hand off to the next useful role.

If only one chat window is active, say that the workflow is being simulated by
one agent. Do not claim that multiple agents collaborated unless multiple agent
profiles or handoffs exist in the shared files.

The shared folder is the durable record, but it is not always enough to trigger
work. When a teammate already has a real chat window/thread, assigning work only
by editing `inbox/` is insufficient. Work must move through the packet protocol;
the responsible sender, normally `协调师`, sends the one-to-one direct message
when thread-messaging tools are available.

## Default Team Root

Use the current workspace by default:

```text
teams/
  .current
  <team_id>/
    team.md
    board.md
    status.md
    decisions.md
    feedback.md
    planner-feedback.md
    review.md
    handoff.md
    message-queue.md
    agents/
    inbox/
    packets/
    artifacts/
```

If the current workspace is unclear, use the current shell working directory. If
the user provides an explicit path, use that path.

## Role Management

Do not delete `协调师` by default. Keep `协调师` when there are three or more
active roles, when direct thread routing is available, when multiple receivers
need packets, or when work can be blocked by stale claims, missing
acknowledgements, or parallel execution.

`协调师` may be folded into another role only in small-team mode:

- one agent simulating the whole team;
- two roles only, such as `规划师 + 执行人`;
- no direct thread routing tools are available;
- the next action has exactly one receiver and no fan-out.

When folded, the acting role must write:

```text
acting_coordinator: yes
```

in the relevant handoff or packet. Folding is a temporary operating mode, not a
change to the role model.

The clean separation is:

- `规划师` owns plan state and plan changes.
- `协调师` owns message state and delivery state.
- `执行人` owns implementation state.
- `审核官` owns review state and cleanup verdicts.

No role should own two states unless explicitly acting in small-team mode.

## Startup Flow

The first active identity is always `规划师`.

`项目：<目标>` or `/team 项目：<目标>` creates only the team shell and a ready
task for `规划师`. It must not tell the user to create `协调师`, `执行人`, or
`审核官` yet. The reply must give one next prompt only, and that prompt must
be self-contained:

```text
/team 规划师
团队：<team_id>
```

Always include the team id in this first next-role prompt. The user should be
able to copy the block into a new chat window without adding context.

When the user sends `/team` without an explicit role, treat it as:

```text
身份：规划师
```

When `规划师` joins for the first time, it must:

1. register itself as the first active role;
2. mark the planner identity as established;
3. create `artifacts/project-instructions.md`;
4. create `artifacts/plan.md`;
5. create `artifacts/dispatch.md`;
6. update `board.md`, `status.md`, and `handoff.md`;
7. generate the next-role prompts for the user.

The next-role prompts must be separate, copyable blocks, in this order:

- 协调师：

  ```text
  /team 协调师
  团队：<team_id>
  ```

- 执行人：

  ```text
  /team 执行人
  团队：<team_id>
  ```

- 审核官：

  ```text
  /team 审核官
  团队：<team_id>
  ```

Do not ask the user to invent role prompts or write `身份：...` manually. The
`规划师` must output all three standard prompts after the initial plan exists.
The prompt text should stay short so the user can copy and paste it directly
into new chat windows.

## Goal-Until-Done Mode

When the user defines what counts as good, successful, acceptable, or finished
for a team project, the team enters goal-until-done mode. The specific project
goal and quality criteria become the stop condition for the whole process.

This applies to any project type, not only the examples below. Different
projects may have different success criteria. The user's stated criteria are
the source of truth.

In this mode:

- `规划师` records the criteria in `artifacts/project-instructions.md` and
  turns them into observable evidence gates, review checks, and an exploration
  matrix of safe runnable paths.
- `协调师` keeps routing the next useful packet after each execution or review
  result. It must not close the loop merely because one prototype, one plan, or
  one attempt exists.
- `执行人` runs every safe runnable path that could plausibly satisfy the
  criteria, compares outputs, records attempts, and keeps iterating until a path
  meets the gates or no safe runnable path remains.
- `审核官` reviews against the user's criteria, not against effort spent. If the
  output is partial, generic, unstable, aesthetically weak, or missing evidence,
  the verdict is `needs-revision` and routes back through `协调师`.

"Every safe runnable path" means every path that is available in the local
environment or approved project scope without missing credentials, new paid
external services, irreversible actions, broad destructive rewrites, or
high-risk/high-cost work. If a path needs unavailable keys, accounts, paid
services, user decisions, or unsafe actions, record it as blocked or unrunnable;
do not count it as success.

The team may stop only when one of these is true:

- `审核官` accepts that the user's criteria are met and cites concrete evidence;
- no safe runnable path remains and the blocker is written to `feedback.md`,
  `status.md`, and a blocker packet;
- the user explicitly stops, changes the goal, or changes the criteria.

Default project-type examples:

- Video projects: if the standard is "能做出非常好看的简笔画视频", success
  requires an actually rendered playable video, final file path, duration,
  resolution, frame rate, visual/aesthetic review, and evidence that the useful
  rendering/animation paths were attempted or ruled out.
- Article generation projects: if the standard is "稳定性强、AI 味非常低",
  success requires multiple sample generations, consistency checks across
  samples, style/humanization review, and rejection of generic AI phrasing,
  empty structure, slogan-like transitions, or unstable tone.
- Other project types: `规划师` must derive domain-specific evidence gates from
  the user's stated target and treat those gates as the finish line.

## Information Flow Protocol

Information movement is a first-class task. Do not treat shared files and direct
chat messages as the same thing:

- shared files are the durable source of truth;
- direct thread messages are one-to-one wakeups or requests to act;
- every direct message should point back to a durable packet.

### Packet Rule

Every meaningful handoff must create one packet under:

```text
packets/<packet_id>.md
```

Packet format:

```markdown
# <packet_id>

- from: <agent_id>
- to: <one canonical identity or one agent_id>
- source_task: <board task id>
- purpose: <plan|execute|review|decision|notice|blocker>
- action_required: <yes|no>
- status: queued
- created_at: <ISO time>
- source_refs:
  - <paths to plan/status/artifacts/etc>

## Summary

## Recipient-Specific Instructions

## Required Response
```

Each packet has exactly one intended receiver. No packet may target two agents.

### One-To-One Message Rule

An agent may send one direct thread message to one receiver at a time. If the
same information must reach two receivers, it is not a broadcast. It is a
fan-out.

Fan-out requires:

1. one source packet that records the full durable information;
2. one child packet per receiver;
3. one queue row per child packet;
4. one direct message per receiver, sent sequentially.

### Who Owns The Content Split

The content owner decides what each receiver needs to know.

- If `规划师` creates a plan, `规划师` must write the work packages and
  recipient-specific instructions in `artifacts/dispatch.md`.
- If `执行人` creates a result, `执行人` must write the evidence and what needs
  review.
- If `审核官` creates a verdict, `审核官` must write the accepted issues,
  revision requests, and cleanup notes.
- `协调师` may split delivery into one-to-one packets, but must not invent
  planning content, acceptance criteria, implementation details, or review
  verdicts.

If a packet needs different content for two receivers and the content owner did
not provide receiver-specific sections, `协调师` asks the content owner to
prepare them. `协调师` may still send a short notice that points to the source
packet, but must not fabricate the missing slice.

### Message Queue

Track packet delivery in `message-queue.md`:

```markdown
| packet | from | to | status | direct_thread | ack | next |
| --- | --- | --- | --- | --- | --- | --- |
| P1 | 规划师-... | 执行人 | queued |  | no | send |
```

Allowed queue statuses:

- `queued`
- `sent`
- `acknowledged`
- `blocked`
- `closed`

### Default Routing Chain

Use this chain unless a packet says otherwise:

```text
规划师 -> 协调师 -> 执行人 -> 审核官 -> 协调师
```

Meaning:

- `规划师` sends plan and dispatch packets to `协调师`, not directly to everyone.
- `协调师` assigns and sends one execution packet to one `执行人`.
- `执行人` sends completed work to one `审核官`.
- `审核官` sends accept/revise verdict to `协调师`.
- `协调师` sends the next one-to-one packet to `执行人`, `规划师`, or the user.

Blockers use the same one-to-one rule. If `执行人` needs a planning decision, it
sends a blocker packet to `协调师`; `协调师` routes it to `规划师`.

### Planner Feedback Loop

`规划师` must receive feedback that can change the plan. The rule is not "send
everything to `规划师`"; the rule is "send plan-affecting feedback to
`规划师`".

Feedback categories:

- `execution_evidence`: proof of work done. Default receiver is `审核官`.
- `execution_blocker`: cannot proceed because something is unclear or broken.
  Default receiver is `协调师`, who routes to `规划师` only if the blocker affects
  the plan.
- `review_accept`: work passed. Default receiver is `协调师`.
- `review_revision_execution`: implementation needs fixing but plan is still
  valid. Default receiver is `协调师`, then `执行人`.
- `review_revision_plan`: plan, scope, task split, or acceptance criteria are
  wrong. Default receiver is `协调师`, then `规划师`.
- `plan_change_request`: explicit request to alter plan. Receiver is `规划师`.

Whenever feedback affects the plan:

1. create a packet with purpose `plan_feedback`;
2. append a concise entry to `planner-feedback.md`;
3. include source refs to evidence, review notes, or blocker details;
4. route it to `规划师` through `协调师` unless small-team mode is active;
5. `规划师` updates `artifacts/project-instructions.md`,
   `artifacts/plan.md`, or `artifacts/dispatch.md` and emits a new packet.

`规划师` should not monitor every raw status update. It should process curated
plan feedback. This keeps it informed without turning it into the team router.

## Direct Thread Routing

Use direct thread routing only as the push layer for a packet.

Actions:

1. Create or locate the packet first.
2. Check `agents/` for the target teammate profile and any recorded
   `thread_id`.
3. If no `thread_id` is recorded, search recent Codex threads by project name,
   team_id, role name, recent task id, or evidence files the teammate edited.
4. Read the likely thread before sending. Confirm it is the target teammate by
   matching role, team folder, task board, cwd, or recent handoff content.
5. Send one concise direct message to that one thread. Include `packet_id`,
   action required, and source file paths.
6. Also write the packet link or summary to `inbox/<target-identity>.md` for
   durability.
7. Update `message-queue.md`, `handoff.md`, and `status.md`, including the
   target `thread_id`.

If the target teammate's thread cannot be found, do not say the teammate has
been notified. Write the packet and inbox message, mark the queue row
`blocked`, and tell the user direct routing failed.

## Commands

### `项目：<目标>` or `/team 项目：<目标>`

Create a new team shell. Do not create detailed project instructions here.
Project instructions are owned by `规划师`.

Actions:

1. Generate a short `team_id`, for example:

   ```text
   team-YYYYMMDD-short-goal-001
   ```

2. Create the default team folder.
3. Write `teams/.current` with the active `team_id`.
4. Write `team.md` with:
   - raw project goal exactly as given by the user;
   - any raw success, quality, or finish criteria exactly as given by the user;
   - team_id;
   - created time;
   - default roles;
   - collaboration rules.
5. Write `board.md` with initial tasks:
   - `确立规划师身份`
   - `建立项目指示`
   - `制定执行计划`
   - `执行第一步`
   - `审核结果`
   - `整理交接`
   Set only `确立规划师身份` to `ready`. Later tasks should stay `blocked` until
   `规划师` registers, writes project instructions, and creates an execution
   plan.
6. Write `status.md` with the current phase.
7. Write empty `planner-feedback.md` with a heading and no entries.
8. Write empty `message-queue.md` with the queue table header.
9. Create `packets/`.
10. Reply briefly with:
   - team_id;
   - team folder path;
   - one self-contained copyable prompt for `规划师` only, including the
     explicit role and `团队：<team_id>`.

`项目：<目标>` must not decide the full project plan, acceptance criteria, or
implementation path. If the user includes success or quality criteria, record
them verbatim as raw criteria only. `规划师` owns turning them into evidence
gates and an exploration matrix in `artifacts/project-instructions.md`.

Do not ask follow-up questions unless the project goal is unusably vague or the
next step is risky.

### `/team [中文身份]` or `身份：<中文身份>`

Join the current team and start working.

Supported identities:

- `规划师`
- `执行人`
- `审核官`
- `协调师`

Preferred invocation:

```text
/team
```

means `规划师`.

```text
/team 协调师
/team 执行人
/team 审核官
```

means the named role.

Legacy `身份：<中文身份>` still works, but do not require the user to type it.

Identity inference:

Infer the canonical identity from the user's wording and the function implied by
that wording. Use the role's function, not exact spelling.

- planning words or functions -> `规划师`
  - examples: `规划`, `计划`, `策划`, `项目指示`, `方案`, `架构`, `拆解`, `路线`, `规划师`, `计划师`
- execution words or functions -> `执行人`
  - examples: `执行`, `干活`, `实现`, `开发`, `制作`, `操作`, `修复`, `落地`, `执行人`, `开发者`
- review words or functions -> `审核官`
  - examples: `审核`, `检查`, `评审`, `审查`, `测试`, `验收`, `挑错`, `QA`, `审核官`, `测试官`, `洁癖`, `/neat-freak`, `整理文档`, `同步记忆`
- coordination words or functions -> `协调师`
  - examples: `协调`, `主控`, `统筹`, `调度`, `组织`, `收口`, `仲裁`, `协调师`, `项目经理`

If no identity is specified, choose `规划师`. If a phrase mixes functions, choose
the dominant action the user asks this agent to perform now. If still ambiguous
after an explicit but mixed role phrase, prefer `协调师`.

Actions:

1. Locate the active team:
   - if the prompt includes `团队：<team_id>`, use `teams/<team_id>`;
   - otherwise read `teams/.current`;
   - if missing, use the newest folder under `teams/`;
   - if no team exists, ask the user to first say `/team 项目：<目标>`.
2. Generate an `agent_id`:

   ```text
   <规范身份>-YYYYMMDD-HHMMSS
   ```

3. Register in `agents/<agent_id>.md`.
4. Read:
   - `team.md`
   - `board.md`
   - `status.md`
   - `message-queue.md`
   - all files under `agents/`
   - relevant files under `inbox/`
   - relevant files under `packets/`
5. Identify teammates and open work.
6. Claim exactly one suitable task or packet by updating `board.md` or
   `message-queue.md`.
7. If the canonical identity is `规划师` and planner identity has not been
   established yet, complete the startup flow in the same turn: register,
   create the first planning artifacts, and generate the next-role prompts.
8. Work according to the identity rules.
9. Update the shared files.
10. End with:
   - claimed task;
   - completed work;
   - blockers;
   - files updated;
   - next recommended `/team` prompt.

If the current chat thread id is visible or discoverable through available
tools, record it in the agent profile. If it cannot be discovered, leave
`thread_id` blank rather than inventing one.

### `继续`

Continue the active team.

Actions:

1. Locate the active team.
2. Read team state, board, and message queue.
3. Infer the next best identity:
   - if no `artifacts/project-instructions.md` exists, act as `规划师`;
   - if no plan exists, act as `规划师`;
   - if unsent packet queue rows exist, act as `协调师`;
   - if goal-until-done criteria exist and accepted evidence is missing, choose
     the role that advances the next exploration, execution, or review loop;
   - if ready work exists, act as `执行人`;
   - if completed work needs checking, act as `审核官`;
   - if conflicts exist, act as `协调师`.
4. Register or update the current agent profile.
5. Claim and process one task.

### `状态`

Summarize the active team.

Actions:

1. Read `team.md`, `board.md`, `message-queue.md`, `status.md`,
   `feedback.md`, `planner-feedback.md`, and `review.md`.
2. Report:
   - current phase;
   - active agents;
   - claimed tasks;
   - queued or blocked packets;
   - blockers;
   - next recommended `/team` prompt.

### `收口`

Finalize the active team task.

Actions:

1. Check board completion.
2. Check review results.
3. Check whether the user's success criteria have accepted evidence, or whether
   a true blocker/no-runnable-path state is documented.
4. Summarize artifacts.
5. Update `status.md` and `handoff.md`.
6. Clearly state remaining risks.

Do not finalize a goal-until-done project merely because a phase, prototype, or
first attempt is complete. Finalize only after the criteria are accepted or the
team has documented a real blocker that prevents further safe progress.

## Identity Rules

### 协调师

Purpose: move information and keep state consistent.

Responsibilities:

- maintain `message-queue.md`;
- create one child packet per receiver when fan-out is needed;
- send one direct thread message at a time;
- track acknowledgement for sent packets;
- maintain board locks and ownership fields;
- resolve duplicate claims or stale claimed tasks;
- keep `status.md` accurate after delivery and acknowledgements;
- route packets to the next identity based on existing plan, review, or blocker
  content.
- classify feedback as plan-affecting or not, using the feedback categories
  above.
- in goal-until-done mode, keep the execution/review loop moving until accepted
  evidence meets the user's criteria or a true blocker/no-runnable-path state is
  documented.

Non-responsibilities:

- do not create project instructions;
- do not design the plan;
- do not define acceptance criteria;
- do not choose implementation details;
- do not decide whether completed work is good.
- do not edit `artifacts/plan.md` or `artifacts/project-instructions.md`.

Do not perform large execution work unless no `执行人` agent exists and the user
needs progress immediately.

### 规划师

Purpose: turn the raw project goal into project instructions and an executable
plan.

Responsibilities:

- read `team.md`;
- establish itself as `规划师` when `/team` is used without a role;
- create or update `artifacts/project-instructions.md`;
- create or update `artifacts/plan.md`;
- create or update `artifacts/dispatch.md`;
- generate copyable `/team 协调师`, `/team 执行人`, and `/team 审核官`
  prompts after the initial plan exists;
- read and resolve entries in `planner-feedback.md`;
- split work into board tasks;
- define what each role needs to know for each work package;
- define acceptance criteria;
- convert user-defined success criteria into observable evidence gates;
- create an exploration matrix of safe runnable paths and stop conditions;
- list risks and dependencies.

Project instructions must include:

- clarified project objective;
- assumptions;
- scope and non-goals;
- expected artifacts;
- acceptance criteria;
- evidence gates for the user's success criteria;
- exploration matrix of safe runnable paths, blocked paths, and stop conditions;
- initial role/task split.

Do not execute implementation tasks. If execution is trivial, still update the
board and recommend `执行人`.

On the first `规划师` turn, do not stop after registration. Complete these in
one response when possible:

1. mark `确立规划师身份` as done;
2. create the first project instructions, plan, and dispatch files;
3. unblock the first useful downstream task;
4. give the user the three next-role prompts as copyable blocks.

`artifacts/dispatch.md` must include recipient-specific slices, for example:

```markdown
| package | receiver | what they need | source refs | expected response |
| --- | --- | --- | --- | --- |
| W1 | 执行人 | implementation task | plan.md#W1 | evidence + files changed |
| W1-review | 审核官 | acceptance checklist | plan.md#acceptance | accept/revise verdict |
```

When a ready `协调师` exists, `规划师` sends one plan packet to `协调师`.
`规划师` must not direct-message `执行人` and `审核官` separately unless no
`协调师` exists and progress would otherwise stop. If forced to use this
fallback, record it in `handoff.md`.

When `规划师` receives a `plan_feedback` packet, it must either:

- update the plan and emit a new dispatch packet;
- reject the feedback with a written rationale in `planner-feedback.md`; or
- ask one clarifying question through `协调师`.

It must not silently ignore plan-affecting feedback.

### 执行人

Purpose: complete ready tasks.

Responsibilities:

- read `artifacts/project-instructions.md` if present;
- read `artifacts/plan.md` if present;
- read the packet assigned to this agent;
- claim one ready task;
- execute the task;
- in goal-until-done mode, run the safe runnable paths assigned by the plan or
  packet, continue to the next plausible path after failures, and record why
  each path passed, failed, or was blocked;
- write evidence into `status.md`;
- write blockers into `feedback.md`;
- create outputs under `artifacts/` when useful.

If the plan is missing or unclear, do not improvise a large plan. Write the
blocker and recommend `规划师`.

When completing assigned work, `执行人` creates one completion packet for
`审核官`. If no `审核官` exists, create the packet for `协调师`. Do not report
the same result to multiple roles directly.

If blocked by unclear requirements, create one blocker packet for `协调师`.
`执行人` does not decide whether the blocker should go to `规划师` or another
role.

### 审核官

Purpose: check quality and completion.

Responsibilities:

- read project goal, plan, board, status, and artifacts;
- read the completion packet assigned to this agent;
- inspect completed work;
- compare completed work against the user's success criteria and evidence gates;
- write findings into `review.md`;
- mark the reviewed task as accepted or needs revision;
- create one verdict packet for `协调师`.

Prioritize concrete defects, missing acceptance criteria, unverifiable claims,
unhandled blockers, unexplored safe runnable paths, and outputs that do not
actually meet the stated goal.

`审核官` owns the `/neat-freak` integration.

Use `/neat-freak` when the review concerns:

- final handoff quality;
- stale or missing README / AGENTS / CLAUDE / docs content;
- project knowledge cleanup;
- memory or documentation consistency;
- milestone closeout;
- whether a newcomer can understand the project from the docs.

When `/neat-freak` is available, `审核官` should invoke it as the deep cleanup
layer after ordinary task review. When it is unavailable, not readable, or not
appropriate for the current task, `审核官` must not pretend it ran. Instead,
perform a lightweight documentation and handoff checklist and record that
`/neat-freak` was not applied.

Do not make every minor review a full `/neat-freak` cleanup. Use it for
milestones, handoffs, docs, memory, or "clean enough for the next agent" checks.

`审核官` does not route revision work directly to `执行人` or plan changes
directly to `规划师`. It sends one verdict packet to `协调师`; `协调师` routes
the next action.

## Board Format

Use a compact Markdown table in `board.md`:

```markdown
| id | task | owner | status | evidence | next |
| --- | --- | --- | --- | --- | --- |
| T1 | 确立规划师身份 |  | ready |  | 规划师 |
| T2 | 建立项目指示 |  | blocked |  | 规划师 |
```

Allowed statuses:

- `ready`
- `claimed`
- `blocked`
- `done`
- `accepted`
- `needs-revision`

Before claiming, re-read `board.md`. Claim only one task by setting:

```text
owner = <agent_id>
status = claimed
```

## Agent Profile Format

Each agent profile should use:

```markdown
# <agent_id>

- 原始身份: <the exact words the user typed>
- 规范身份: <规划师|执行人|审核官|协调师>
- 加入时间: <ISO time>
- 当前状态: active
- 擅长: <short capabilities>
- 正在处理: <task id or none>
- 最近更新: <ISO time>
- thread_id: <Codex thread id if known, otherwise blank>
- thread_title: <thread title if known, otherwise blank>
- last_direct_message_at: <ISO time or blank>
```

## Handoff Rules

When ending a turn, update `handoff.md` as a chronological log:

```markdown
## <timestamp> <agent_id>

- 已完成:
- 未完成:
- 阻塞:
- 建议下一个身份:
- 证据:
```

`handoff.md` does not make another agent act. If a specific role should act
next, create a packet and queue row. If that role has a known or discoverable
chat thread, send exactly one direct message for that packet and mark the queue
row `sent`.

## Minimal Replies

The user wants low typing. Keep replies short unless asked for details.

For `项目：` or `/team 项目：`, reply with only:

- team_id;
- folder path;
- one self-contained copyable prompt for `规划师`, not the bare `/team` alias.

For `/team` as `规划师` on first join, reply with only:

- joined identity;
- plan files created;
- blocked items or assumptions;
- copyable prompts for `协调师`, `执行人`, and `审核官`.

For `/team <identity>` or `身份：`, reply with only:

- joined identity;
- claimed task;
- result;
- next `/team` prompt.

## Safety

- Do not overwrite another agent's claimed task unless acting as `协调师` and the
  original agent is clearly inactive or blocked.
- Do not hide blockers. Write them to `feedback.md`.
- Do not claim completion without evidence.
- Do not create extra projects when an active team exists unless the user says
  `项目：<新目标>` or `/team 项目：<新目标>`.
