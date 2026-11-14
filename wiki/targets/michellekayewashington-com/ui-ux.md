---
title: "UI & Design System: michellekayewashington-com"
date: 2026-11-14
target: "[[overview|michellekayewashington-com]]"
---

# UI Architecture & Design Tokens: michellekayewashington-com

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--paper` | `#fffdf8` |
| `--paper-2` | `#f6f0e8` |
| `--ink` | `#120a09` |
| `--ink-2` | `#2b201d` |
| `--rose` | `#9a675c` |
| `--rose-2` | `#c68f81` |
| `--tan` | `#b7a397` |
| `--rule` | `rgb(18 10 9 / 14%)` |
| `--fg` | `var(--ink)` |
| `--bg` | `var(--paper)` |
| `--muted` | `#7a6560` |
| `--nav-w` | `clamp(190px, 15vw, 300px)` |
| `--pad` | `clamp(1.25rem, 3.2vw, 4rem)` |
| `--ease` | `cubic-bezier(0.22, 1, 0.36, 1)` |
| `--ease-io` | `cubic-bezier(0.65, 0, 0.35, 1)` |
| `--serif` | `"Cormorant", Georgia, "Times New Roman", serif` |
| `--fg` | `#f4ede4` |
| `--bg` | `#110c0b` |
| `--rule` | `rgb(244 237 228 / 16%)` |
| `--muted` | `#b9a59c` |
| `--room-title` | `var(--fg)` |
| `--fg` | `#f4ede4` |
| `--bg` | `#2b2d20` |
| `--rule` | `rgb(244 237 228 / 16%)` |
| `--muted` | `#bcb8a6` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `site-nav` | `site-nav` |
| `<nav>` | `-` | `pager` |
| `<header>` | `-` | `shell` |
| `<main>` | `stage` | `stage stage-index` |
