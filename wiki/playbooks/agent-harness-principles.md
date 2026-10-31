---
title: "Playbook: Agent Harness Principles"
date: 2026-10-31
tags:
  - playbook
  - architecture
  - agent-harness
summary: "Core design guidelines for building and maintaining agent skills and harnesses."
---

# Playbook: Agent Harness Principles

## Overview
Guidelines for building, extending, and organizing tools and skills for autonomous AI agents (such as Antigravity `agy`, Claude Code, and Codex).

## Recommended Patterns

1. **Native Skills Over Custom Wrappers**:
   - Modern agent runtimes are their own dispatchers.
   - Use declarative `SKILL.md` documents rather than external Python/Node runner scripts.
   - Let the agent's progressive disclosure load tools and instructions on demand.

2. **Decoupled Repositories & Isolated Projects**:
   - Keep the agent harness repository (`fleet`) strictly for skills and the knowledge base. Never build application code inside `fleet`.
   - Every application or client project must be created in its own directory and separate Git repository outside `fleet` (e.g. `../<project-name>`).
   - Mount or symlink skills from `fleet/skills` into target projects (`.agents/skills/` or `~/.claude/skills/`).
   - Log venture outcomes and lessons back into `fleet/wiki/ventures/`.

3. **Obsidian-Compatible Knowledge**:
   - Store lessons, venture outcomes, and playbooks in clean Markdown with YAML frontmatter.
   - Use `[[wikilinks]]` for relationships between ventures and playbooks.

## Anti-Patterns & Pitfalls

- **Premature Automation**: Writing custom orchestrators or complex wrapper CLIs before determining if native skills suffice.
- **Heavy Database Dependencies**: Using opaque SQLite/vector databases for small-to-medium documentation when simple Markdown and grep suffice.
- **Unstructured Agent Logs**: Leaving lessons trapped in ephemeral agent conversation transcripts instead of documenting them in the wiki.
