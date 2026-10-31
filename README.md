# Fleet: Agent Harness

A simple, zero-dependency harness for managing and dispatching a fleet of specialized AI agents.

This repository does **not** contain application code. Instead, it serves as the central control plane and specification library for our agent fleet, structured by scope (global vs. project-oriented) and model-specific profiles (starting with Antigravity `agy`, extensible to `claude`).

---

## Core Philosophy

- **Keep It Simple (KISS)**: Minimal moving parts, standard markdown personas, zero third-party Python dependencies (runs on standard Python 3.9+).
- **Decoupled from Application Code**: Application repositories remain clean; the fleet harness can inspect, link into, or run against any target project workspace.
- **Model Agnostic**: Built today for `agy` (Gemini), architected to support `claude` (Anthropic) with drop-in configuration.

---

## Directory Layout

```text
fleet/
├── fleet                    # Executable CLI entrypoint
├── README.md                # Documentation & usage reference
├── .gitignore
├── agents/
│   ├── global/              # Universal, cross-project agents
│   │   ├── architect.md     # System architecture, interface contracts, trade-offs
│   │   └── reviewer.md      # Code quality, security audits, simplicity checks
│   ├── project/             # Project/lifecycle specific agents
│   │   ├── builder.md       # Implementation workhorse (clean, minimal code)
│   │   └── tester.md        # QA & test automation (unit, integration, boundaries)
│   └── models/              # Model-specific parameters, flags, and mappings
│       ├── agy.json         # Antigravity CLI profile (Gemini)
│       └── claude.json      # Claude Code profile (Anthropic)
└── harness/
    └── runner.py            # Zero-dependency Python manager and dispatcher
```

---

## Getting Started

### 1. List Available Agents

View all global and project-oriented agents currently in the fleet:

```bash
./fleet list
```

### 2. Inspect an Agent's Persona & System Instructions

```bash
./fleet show architect
./fleet show builder
```

### 3. Run an Agent against a Target Project Workspace

Run an agent in interactive mode using `agy` on a target application directory:

```bash
./fleet run builder --target /path/to/my-app --prompt "Implement auth middleware"
```

To test the generated command without executing:

```bash
./fleet run builder --target /path/to/my-app --prompt "Implement auth middleware" --dry-run
```

To switch to Claude:

```bash
./fleet run builder --backend claude --target /path/to/my-app --prompt "Implement auth middleware"
```

### 4. Link Fleet into a Target Workspace

Inject the fleet's agent definitions into a target repository so `agy` automatically discovers the roster via `.agents/rules/`:

```bash
./fleet link /path/to/my-app
```

### 5. Export for Claude Code

Export agent roles directly into a target workspace's `CLAUDE.md`:

```bash
./fleet export-claude --target /path/to/my-app
```

---

## Adding New Agents

To add an agent to the fleet, simply create a new markdown file in `agents/global/` or `agents/project/`:

```markdown
---
name: security-officer
role: Security Specialist
type: global
description: Audits dependencies and configurations for vulnerabilities.
tools:
  - read_file
  - run_command
---

# Security Specialist Persona

You are a security specialist...
```

The `./fleet` CLI will automatically discover and register your new agent without any configuration changes.
