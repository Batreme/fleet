# Fleet: Agent Skills & Harness

A lightweight, native agent skills harness inspired by [`tstack`](https://github.com/t3dotgg/tstack).

In modern agent environments (**Antigravity `agy`**, **Claude Code**, and **Codex**), you do not need an external runner script or Python wrapper. The agent runtime itself is the runner: it discovers, loads, and executes skills directly from declarative markdown specifications (`SKILL.md`).

This repository contains our core fleet of skills.

---

## Skills

| Skill | Trigger / Say | What it does |
|---|---|---|
| `grill-me` | "grill me" | Relentless interactive interview to sharpen a plan, architecture, or design tree before writing code. |
| `grilling` | (engine) | Decision-tree interrogation engine that uncovers hidden assumptions in structured rounds. |
| `full-send` | "full send" | Drives a change all the way to a merged PR: proves it, reviews it, files it, babysits it, merges it. |
| `full-stop` | "full stop" | Same as `full-send`, but pauses when the PR is green and ready for human review/merge. |
| `council` | "council" | Solicits reviews from multiple models/providers and loops until they achieve consensus. |
| `sol-loop` | "sol loop" | Reviews a change with GPT Sol in a loop until both agents agree. |
| `file-pr` | "file a PR" | Files a concise, issue-first pull request via GitHub CLI (`gh`). |
| `takeover` | "take over" | Picks up and finishes someone else's branch, PR, or thread while preserving attribution. |
| `babysit-pr` | "babysit" | Monitors a PR through CI and review bots, fixing genuine issues until green. |
| `modernize` | "modernize" | Rebases an older PR and evaluates whether it should still exist or be superseded. |
| `leaving-pr-comments` | (automatic) | Standardizes the format and tone of automated comments posted on pull requests. |
| `kb` | "consult kb", "record venture" | Searches past ventures and playbooks before a task, and logs outcomes/lessons afterward. |
| `reverse-engineer` | "reverse engineer" | Captures web applications, extracts schemas/APIs/design tokens, and queries the vector index. |
| `ui-prompt-designer` | "ui prompt designer" | Reverse-engineers web properties, design tokens, DOM hierarchies, and visual assets into production-grade AI prompt blueprints. |
| `claude-loop` | "claude loop" | Anthropic Claude-powered review loop modeled on `sol-loop`. Runs autonomous multi-round reviews against strict quality rubrics. |

### Skill Dependencies

Several skills work together as a pipeline:
- `grill-me` calls `grilling`.
- `full-send` uses `sol-loop`, `file-pr`, and `babysit-pr`.
- `full-stop` uses `full-send`.
- `takeover` uses `modernize`, `file-pr`, `babysit-pr`, and `leaving-pr-comments`.
- `file-pr`, `babysit-pr`, and `modernize` use `leaving-pr-comments`.
- `ui-prompt-designer` uses `claude-loop` for autonomous blueprint and rubric verification.

---

## Knowledge Base (Wiki)

The `wiki/` directory is an Obsidian-compatible Markdown vault that serves as long-term agent memory across projects:
- **`wiki/ventures/`**: Historical logs of tasks and projects—the intended outcome, obstacles faced, lessons learned, and final result.
- **`wiki/playbooks/`**: Proven patterns and best practices extracted from past ventures.
- **`wiki/templates/`**: Templates for standardizing new venture logs and playbooks.
- **`wiki/INDEX.md`**: Central Map of Content (MOC) linking all entries.
- **[`wiki/UI_EVALS_DASHBOARD.md`](wiki/UI_EVALS_DASHBOARD.md)**: Master 58-round / 575-target UI Prompt Blueprint & Evaluation Dashboard (with direct clickable links to every target's zero-shot prompt).
- **`wiki/targets/<slug>/prompt-blueprint.md`**: 7-part UI Prompt Blueprints and Section 7 Master Zero-Shot AI Generation Prompts (`#7-master-zero-shot-ai-generation-prompt`), paired with `ui-ux.md` design tokens and `assets/desktop.png` (`1440px`) + `assets/mobile.png` (`390px`).
- **`wiki/traces/`**: 58 round execution traces (`round-01-trace.md` .. `round-58-trace.md`) and `claude-loop-ledger.json`.

---

## Installation & Usage

### 1. In Antigravity (`agy`)

Skills are automatically discovered from `.agents/skills` (which symlinks to `./skills` in this repo).

To install into a target project:
```bash
# Link all skills into your project's .agents directory:
mkdir -p /path/to/project/.agents
ln -s "$(pwd)/skills" /path/to/project/.agents/skills
```

Or install globally for `agy`:
```bash
mkdir -p ~/.gemini/config/skills
cp -R skills/* ~/.gemini/config/skills/
```

### 2. In Claude Code

```bash
mkdir -p ~/.claude/skills
cp -R skills/* ~/.claude/skills/
```

### 3. In Codex

```bash
mkdir -p ~/.codex/skills
cp -R skills/* ~/.codex/skills/
```

---

## Requirements

- **GitHub CLI (`gh`)**: Required for `file-pr`, `babysit-pr`, `takeover`, and `modernize`.
- **Python 3**: Used by `skills/babysit-pr/scripts/pr-wait` to watch PR event streams.
- **Subagents / Multi-model**: `council` and `sol-loop` delegate reviews to subagents or external models.

---

## License

Non-Commercial Software License. Copyright (c) 2026 Jakub Szkop (Batreme). All rights reserved.  
See [`LICENSE`](LICENSE) for complete terms. For commercial licensing inquiries, contact: Jakub Szkop `<szkopjakub@gmail.com>`.
