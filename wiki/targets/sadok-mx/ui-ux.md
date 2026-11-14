---
title: "UI & Design System: sadok-mx"
date: 2026-11-14
target: "[[overview|sadok-mx]]"
---

# UI Architecture & Design Tokens: sadok-mx

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--back-bottom` | `calc(2 * (var(--gutter) + env(safe-area-inset-top)) + 46px)` |
| `--back-bottom` | `calc(2 * (var(--gutter) + env(safe-area-inset-top)) + 38px)` |
| `--back-bottom` | `calc(2 * (clamp(16px, .8vw, 32px) + env(safe-area-inset-top)` |
| `--px` | `2px` |
| `--sep` | `2.8em` |
| `--px` | `3px` |
| `--px` | `4px` |
| `--bg-0` | `#0f1110` |
| `--bg-1` | `#171a18` |
| `--bg-2` | `#232724` |
| `--bone` | `#e8e6dc` |
| `--bone-dim` | `#9a9a90` |
| `--accent` | `#2e8b8b` |
| `--accent-ink` | `#1f6a6a` |
| `--led` | `#e23b3b` |
| `--ink` | `#1c2420` |
| `--moss` | `#45604f` |
| `--sage` | `#9fbf8e` |
| `--paper` | `#e3ead1` |
| `--page` | `#f4f2ea` |
| `--text` | `#1a1c1a` |
| `--text-dim` | `#555a55` |
| `--text-faint` | `#8b908b` |
| `--rule` | `#d9d6ca` |
| `--font-display` | `Handjet, system-ui, sans-serif` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `back-nav` |
| `<header>` | `-` | `meta` |
| `<aside>` | `-` | `keyhint` |
| `<main>` | `-` | `` |
