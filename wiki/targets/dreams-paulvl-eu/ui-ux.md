---
title: "UI & Design System: dreams-paulvl-eu"
date: 2026-11-14
target: "[[overview|dreams-paulvl-eu]]"
---

# UI Architecture & Design Tokens: dreams-paulvl-eu

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--bg` | `#050507` |
| `--ink` | `#ece6dc` |
| `--ink-dim` | `rgba(236, 230, 220, .58)` |
| `--ink-faint` | `rgba(236, 230, 220, .2)` |
| `--gold` | `#e9b95a` |
| `--gold-hi` | `#fff1c4` |
| `--red` | `#b3343f` |
| `--serif` | `"Geist", "Helvetica Neue", Arial, sans-serif` |
| `--italic` | `"Newsreader", Georgia, serif` |
| `--mono` | `"IBM Plex Mono", ui-monospace, "SFMono-Regular", Menlo, Cons` |
| `--gutter` | `clamp(16px, 3vw, 40px)` |
| `--t-note` | `15px` |
| `--t-m` | `clamp(34px, 4.3vw, 74px)` |
| `--t-l` | `clamp(44px, 8.4vw, 150px)` |
| `--t-xl` | `clamp(56px, 11.5vw, 210px)` |
| `--ease` | `cubic-bezier(.22, 1, .36, 1)` |
| `--p` | `0` |
| `--i` | `1` |
| `--i` | `2` |
| `--i` | `3` |
| `--i` | `4` |
| `--i` | `5` |
| `--tear` | `94px` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `chapters` | `chapters` |
| `<header>` | `-` | `frame frame--top` |
| `<main>` | `lines` | `lines` |
| `<footer>` | `-` | `frame frame--bottom` |
