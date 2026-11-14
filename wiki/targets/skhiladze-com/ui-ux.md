---
title: "UI & Design System: skhiladze-com"
date: 2026-11-14
target: "[[overview|skhiladze-com]]"
---

# UI Architecture & Design Tokens: skhiladze-com

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--bg` | `#090c12` |
| `--bg-2` | `#11151c` |
| `--ink` | `#f2f2ef` |
| `--muted` | `#9aa0aa` |
| `--accent` | `#fb5e28` |
| `--accent-hi` | `#ff7a4d` |
| `--accent-ink` | `#090c12` |
| `--inv-bg` | `#f2f2ef` |
| `--inv-ink` | `#090c12` |
| `--inv-muted` | `#4d525b` |
| `--scrim` | `rgba(9, 12, 18, .64)` |
| `--m` | `clamp(16px, 2.2vw, 32px)` |
| `--g` | `clamp(12px, 1.4vw, 24px)` |
| `--r` | `clamp(12px, 1.35vw, 22px)` |
| `--clear` | `calc(80px + env(safe-area-inset-bottom, 0px))` |
| `--s-small` | `14px` |
| `--s-body` | `clamp(16px, .15vw + 15.4px, 17px)` |
| `--s-lead` | `clamp(20px, .9vw + 12px, 26px)` |
| `--s-head` | `clamp(30px, 2.2vw + 14px, 46px)` |
| `--s-display` | `clamp(58px, 9.4vw, 180px)` |
| `--ease-out` | `cubic-bezier(.23, 1, .32, 1)` |
| `--ease-io` | `cubic-bezier(.77, 0, .175, 1)` |
| `--ease-soft` | `cubic-bezier(.33, 1, .68, 1)` |
| `--t-press` | `.14s` |
| `--t-hover` | `.18s` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `menu__nav` |
| `<nav>` | `-` | `bar__nav` |
| `<nav>` | `-` | `back` |
| `<nav>` | `-` | `dock__lang` |
| `<header>` | `-` | `bar` |
| `<aside>` | `-` | `view is-set` |
| `<aside>` | `-` | `dock` |
| `<aside>` | `-` | `fab-a` |
| `<main>` | `-` | `` |
| `<dialog>` | `-` | `viewer` |
