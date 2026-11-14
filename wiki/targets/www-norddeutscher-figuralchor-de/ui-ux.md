---
title: "UI & Design System: www-norddeutscher-figuralchor-de"
date: 2026-11-14
target: "[[overview|www-norddeutscher-figuralchor-de]]"
---

# UI Architecture & Design Tokens: www-norddeutscher-figuralchor-de

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--font-sans` | `ui-sans-serif, system-ui, sans-serif, "Apple Color Emoji",
 ` |
| `--font-mono` | `ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Libe` |
| `--color-white` | `#ffffff` |
| `--font-weight-medium` | `500` |
| `--font-weight-bold` | `700` |
| `--ease-in-out` | `cubic-bezier(0.4, 0, 0.2, 1)` |
| `--default-transition-duration` | `150ms` |
| `--default-transition-timing-function` | `cubic-bezier(0.4, 0, 0.2, 1)` |
| `--default-font-family` | `var(--font-sans)` |
| `--default-mono-font-family` | `var(--font-mono)` |
| `--color-rose` | `#e6cac7` |
| `--color-gold` | `#bd7716` |
| `--color-ink` | `#000000` |
| `--color-charcoal` | `#404040` |
| `--color-conductor` | `#d3d1de` |
| `--color-silver` | `#d6d6d6` |
| `--color-sand` | `#c2b7ab` |
| `--color-wine` | `#563535` |
| `--color-greige` | `#ccc1cf` |
| `--color-mint` | `#cad7d5` |
| `--color-cdsand` | `#d9d9d5` |
| `--color-cdtile` | `#c5c6c2` |
| `--font-display` | `"Playfair Display", Georgia, serif` |
| `--font-body` | `"Syne", system-ui, sans-serif` |
| `--tw-leading` | `1.1` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `flex flex-col` |
| `<header>` | `main-content` | `bg-rose relative` |
| `<header>` | `-` | `bg-rose relative` |
| `<footer>` | `-` | `bg-ink` |
| `<footer>` | `-` | `bg-ink` |
