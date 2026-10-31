---
title: "UI & Design System: vadimcarazan-com"
date: 2026-10-31
target: "[[overview|vadimcarazan-com]]"
---

# UI Architecture & Design Tokens: vadimcarazan-com

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--bg` | `#0a0a0b` |
| `--ink` | `#f2f2f2` |
| `--mute` | `rgba(242, 242, 242, 0.55)` |
| `--line` | `rgba(255, 255, 255, 0.12)` |
| `--serif` | `"Editorial Old Italic", "Instrument Serif", "Times New Roman` |
| `--sans` | `"Inter Tight", "Inter", -apple-system, "Helvetica Neue", Ari` |
| `--pad` | `clamp(16px, 2vw, 32px)` |
| `--box-open` | `clamp(460px, 42vw, 780px)` |
| `--ease` | `cubic-bezier(0.22, 1, 0.36, 1)` |
| `--bp` | `28px` |
| `--bp` | `18px` |
| `--bp` | `14px` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `mnav-links` |
| `<header>` | `-` | `topbar` |
| `<aside>` | `box` | `box` |
| `<aside>` | `-` | `p-cta` |
| `<aside>` | `-` | `p-cta about-cta` |
