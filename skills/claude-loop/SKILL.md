---
name: claude-loop
description: Anthropic Claude-powered review loop modeled on sol-loop. Runs autonomous multi-round reviews using Claude Sonnet 5.5 / Opus 5.5 via the native Swarm to verify code, blueprints, UI prompts, and documentation against strict quality rubrics.
---

# claude-loop

This is an autonomous review workflow modeled directly on `sol-loop`, using Anthropic's Claude models (`claude-sonnet-5-5-high` or `claude-opus-5-5-high`) to review code, architectural blueprints, UI design prompts, and documentation in a rigorous loop.

Reviewers enforce the highest standard of technical craft, precision, and alignment with user intent.

## Budget

- **Default**: Up to 3 rounds total. Round 1 inspects the full scope; subsequent rounds verify only changed files and open findings.
- **Extension**: Extend to 5 rounds only for security, data loss, state corruptions, or upon explicit user request.
- **Early Exit**: If a round returns only nits or `VERDICT: APPROVE`, the loop completes immediately.
- **One Reviewer Only**: Launch one dedicated Swarm reviewer worker per round. Keep an immutable findings ledger throughout.

---

## 1. Review Scope & Briefing

Before dispatching Claude, establish a clean, well-bounded scope:
1. Identify modified files using `git status --short` and `git diff --stat <base>`.
2. Clearly formulate the intent, out-of-scope boundaries, and covering checks.
3. Supply exact paths to the documentation or code under review, along with any relevant evaluation scores or trace logs.

### Review Brief Template (Round 1)

```
Review only. Do not edit files, commit, push, or start background subagents.
Target Batch: <batch description / paths>
Intent: <purpose and criteria>
Out of Scope: <what should not be scrutinized>
Automated Evals: <eval scores and script results>

Review Instructions:
1. Read the provided prompt-blueprint.md, tokens, and visual assets.
2. Verify adherence to the 7-part UI Prompt Designer schema:
   - Visual Persona & Anti-AI-slop Differentiators
   - Spatial Grid & Viewport Clamping (Desktop + Mobile)
   - Color, Materiality & Lighting Tokens (Grounded in source CSS)
   - Typographic Hierarchy & Fluid Scales
   - Motion Choreography & Exact Bézier Curves
   - Component Wireframe & DOM Structural Map
   - Master Zero-Shot AI Generation Prompt (Self-contained, >= 80 lines)
3. Evaluate against the 5-Point Quality Rubric (0-5 per metric):
   - Token Precision & Grounding
   - Layout Geometry & Responsive Math
   - Motion & Interaction Physics
   - Component Wireframe Completeness
   - Master Prompt Generability & Fidelity
4. Classify each finding by severity:
   - blocker: Incomplete required section, missing/broken screenshot, hallucinated token, or unusable master prompt.
   - should: Missing responsive mobile transition, omitted motion easing curve, or weak component DOM mapping.
   - nit: Minor formatting, styling, or typographic phrasing suggestion.

Reply strictly in this format:
VERDICT: APPROVE or CHANGES
SCORE: <total>/25
C1 [blocker|should|nit] <file>:<line> <claim>. Fix: <concrete suggestion>
C2 [blocker|should|nit] <file>:<line> <claim>. Fix: <concrete suggestion>
```

---

## 2. Launching Claude via Swarm

In Antigravity, invoke `swarm(action="add", name="claude-reviewer", model="claude-sonnet-5-5-high", brief=...)` to post the brief on the shared message board.

1. Pin to `claude-sonnet-5-5-high` (or `claude-opus-5-5-high` if deeply complex reasoning is required).
2. Use `workspace: "inherit"` so the reviewer reads the files directly in place.
3. Wait for the reviewer's analysis using `swarm_wait` or read the board using `read_board`.

---

## 3. Resolving Findings & Ledger Management

Maintain a persistent review ledger in the trace file (`round-XX-trace.md`):
- **Agree**: Implement the minimal, precise fix. Re-run local evaluation checks.
- **Disagree / Push Back**: Provide clear technical evidence (DOM selector, CSS variable table, line number, or browser screenshot) explaining why the existing implementation is correct.
- **Nit / Follow-up**: Address if trivial, or record as a non-blocking backlog note.

### Follow-up Round Brief (Rounds 2+)

```
Round <N> Review.
Base files: <paths>
Ledger of Actions:
- C1: FIXED in <file>:<line> - <summary of fix>
- C2: DISAGREED with evidence: <explanation>
- C3: RESOLVED / DECLINED: <reason>

Please verify open items and updated files.
Reply with:
VERDICT: APPROVE or CHANGES
SCORE: <total>/25
```

---

## 4. Completion & Sign-off

The loop terminates when:
- Claude returns `VERDICT: APPROVE` with zero blockers or unresolved shoulds.
- Or maximum budget is reached (with unresolved items documented for human decision).

Upon approval, update the central dashboard (`wiki/UI_EVALS_DASHBOARD.md`), log the audit trail, and commit the verified artifacts.
