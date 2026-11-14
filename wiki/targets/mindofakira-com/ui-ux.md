---
title: "UI & Design System: mindofakira-com"
date: 2026-11-14
target: "[[overview|mindofakira-com]]"
---

# UI Architecture & Design Tokens: mindofakira-com

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--bg` | `#0c0b0f` |
| `--bg-2` | `#15131a` |
| `--fg` | `#ecebe4` |
| `--muted` | `#8f8b98` |
| `--line` | `rgba(236, 235, 228, 0.14)` |
| `--accent` | `#5b6bff` |
| `--accent-ink` | `#f4f3ff` |
| `--vinyl` | `#050407` |
| `--f-display` | `"Archivo", "Arial Black", "Helvetica Neue", Arial, sans-seri` |
| `--f-body` | `"Archivo", "Helvetica Neue", Arial, sans-serif` |
| `--f-mono` | `"JetBrains Mono", ui-monospace, "SFMono-Regular", Menlo, mon` |
| `--s-1` | `clamp(0.75rem, 0.7rem + 0.2vw, 0.8125rem)` |
| `--s0` | `clamp(1rem, 0.95rem + 0.25vw, 1.125rem)` |
| `--s1` | `clamp(1.375rem, 1.1rem + 1.2vw, 2rem)` |
| `--s2` | `clamp(2rem, 1.3rem + 3.2vw, 4rem)` |
| `--s3` | `clamp(3.2rem, 1rem + 10vw, 11rem)` |
| `--gut` | `max(16px, env(safe-area-inset-left, 0px))` |
| `--gut-r` | `max(16px, env(safe-area-inset-right, 0px))` |
| `--ease` | `cubic-bezier(.2, .7, .1, 1)` |
| `--bg` | `#e9e7e1` |
| `--bg-2` | `#dedbd3` |
| `--fg` | `#131216` |
| `--muted` | `#6a6672` |
| `--line` | `rgba(19, 18, 22, 0.16)` |
| `--accent` | `#2b3bd9` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `nav` |
| `<header>` | `top` | `top` |
| `<aside>` | `-` | `studio-panel` |
| `<main>` | `-` | `` |
| `<footer>` | `-` | `foot wrap` |
