---
name: reverse-engineer
description: Reverse engineer web applications, analyze API schemas, capture client state/design tokens, and query extracted production patterns to avoid AI slop.
---

# Reverse-Engineer Skill

This skill allows agents to inspect real-world production web applications (and general security/CTF targets), extract their APIs, data models, and UI design tokens, store structured dossiers in `fleet/wiki/targets/`, and semantically search the SQLite+Vector index.

The heavy capture and indexing engine lives adjacent to Fleet at `../reverse-harness`.

---

## 1. When to Use This Skill

- **Before Building a New App / Feature**: Query `fleet/wiki/targets/` or the vector database to see how real-world production apps (e.g. Linear, Notion, Figma) structure their domain models, optimistic UI, keyboard shortcuts, or APIs.
- **When Reverse Engineering a Web App**: When asked to inspect a website, capture network traffic (HAR), unpack source maps, extract API schemas, or de-obfuscate client code.
- **When Handling Binary, Mobile, or CTF Tasks**: When given an APK, ELF binary, or security challenge, route through the upstream `reverse-skill` framework.

---

## 2. Command Reference

All commands are executed via `uv` in `../reverse-harness`:

### 🌐 Web Capture & Extraction

```bash
# 1. Login session (for protected/authenticated web apps - opens visible browser)
uv run --directory ../reverse-harness reverse-harness auth login <profile-name> --url "https://app.example.com/login"

# 2. Automated headless capture (captures HAR, JS/CSS bundles, DOM, and storage)
uv run --directory ../reverse-harness reverse-harness capture "https://app.example.com" --name <target-name>
# With auth session:
uv run --directory ../reverse-harness reverse-harness capture "https://app.example.com/dashboard" --name <target-name> --auth <profile-name>

# 3. Analyze raw capture and generate Obsidian dossier into fleet/wiki/targets/<target-name>/
uv run --directory ../reverse-harness reverse-harness analyze <target-name> --wiki-dir ../fleet/wiki/targets
```

---

### 🔍 Querying Extracted Production Patterns (Anti-AI-Slop Engine)

Before scaffolding generic boilerplate, query existing production targets:

```bash
# Semantic + keyword search across all analyzed endpoints, schemas, and UI patterns
uv run --directory ../reverse-harness reverse-harness query "optimistic updates kanban board"
uv run --directory ../reverse-harness reverse-harness query "workspace organization permissions schema"
```

To re-index when new dossiers are manually edited or added:
```bash
uv run --directory ../reverse-harness reverse-harness index --wiki-dir ../fleet/wiki/targets
```

---

### 🛡️ Upstream Security & Binary Reverse Engineering (`reverse-skill`)

For mobile APKs, native binaries, or general penetration testing:
```bash
# Classify and route arbitrary tasks through upstream reverse-skill R0-R45 ladders
uv run --directory ../reverse-harness reverse-harness route "<description of target or file>"
```

Or execute directly inside `../reverse-harness/upstream/reverse-skill/`:
```bash
bash ../reverse-harness/upstream/reverse-skill/skills/scripts/master-route.sh --hint "<task>"
```

---

## 3. Obsidian Dossier Layout

Each analyzed application creates a standardized dossier in `fleet/wiki/targets/<target-name>/`:
- `overview.md`: Tech stack fingerprint, framework, auth, hosting, summary.
- `apis.md`: Discovered REST/GraphQL/WebSocket endpoints and payload schemas.
- `data-models.md`: Inferred client/server entity models and local storage (IndexedDB).
- `ui-ux.md`: Component primitives, tokens (colors, typography, spacing), interactions.
- `source-maps.md`: Unpacked source trees and recovered client code.
