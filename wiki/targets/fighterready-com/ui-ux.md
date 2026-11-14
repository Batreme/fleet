---
title: "UI & Design System: fighterready-com"
date: 2026-11-14
target: "[[overview|fighterready-com]]"
---

# UI Architecture & Design Tokens: fighterready-com

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--ink` | `#080808` |
| `--ink-2` | `#0d0d0d` |
| `--smoke` | `#1a1a1a` |
| `--steel` | `#2b2b2b` |
| `--ash` | `#6a6a6a` |
| `--bone` | `#b8b8b8` |
| `--white` | `#f2f2f2` |
| `--flame` | `#ff6a00` |
| `--amber` | `#ffc000` |
| `--gold` | `#f5c518` |
| `--ember` | `#cc5500` |
| `--green` | `#2cc55c` |
| `--red` | `#ef5350` |
| `--display` | `"Barlow Condensed", "Arial Narrow", sans-serif` |
| `--body` | `"Inter", system-ui, -apple-system, sans-serif` |
| `--gutter` | `clamp(1.25rem, 4vw, 4rem)` |
| `--rail` | `clamp(2.5rem, 6vw, 5.5rem)` |
| `--masthead` | `clamp(4.5rem, 8vw, 6.5rem)` |
| `--ease` | `cubic-bezier(.22, 1, .36, 1)}*,*:before,*:after{box-sizing:b` |
| `--panel-inset` | `clamp(0rem, 6vw, 5.5rem)` |
| `--rail` | `0rem}.progress{left:.6rem}.round__copy{max-width:none}}@medi` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `masthead-nav` | `masthead__nav` |
| `<header>` | `masthead` | `masthead` |
| `<main>` | `rounds` | `rounds` |
| `<footer>` | `-` | `footer` |
