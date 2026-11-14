---
title: "UI & Design System: labellavista-es"
date: 2026-11-14
target: "[[overview|labellavista-es]]"
---

# UI Architecture & Design Tokens: labellavista-es

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--font-archivo` | `"Archivo", "Archivo Fallback"}
@font-face{font-family:DM Mon` |
| `--font-dm-mono` | `"DM Mono", "DM Mono Fallback"}
@font-face{font-family:Alfa S` |
| `--font-slab` | `"Alfa Slab One", "Alfa Slab One Fallback"}
:root{--black:#0a` |
| `--paper` | `#eee9de` |
| `--ink` | `#111` |
| `--white` | `#fff` |
| `--blue` | `#2f4a8a` |
| `--blue-lift` | `#6e8fd6` |
| `--cream` | `#e2d6c0` |
| `--font-sans` | `var(--font-archivo), system-ui, -apple-system, "Segoe UI", s` |
| `--font-mono` | `var(--font-dm-mono), ui-monospace, "Courier New", monospace` |
| `--display` | `clamp(64px, 9vw, 160px)` |
| `--section` | `clamp(32px, 2.8vw, 40px)` |
| `--body` | `clamp(15px, 1.1vw, 17px)` |
| `--ui` | `11px` |
| `--margin` | `24px` |
| `--gutter` | `24px` |
| `--bar` | `48px` |
| `--ease` | `cubic-bezier(.16, 1, .3, 1)}@media (min-width:1440px){:root{` |
| `--gutter` | `16px}}[data-room=dark]{--bg:var(--blue)` |
| `--fg` | `var(--cream)` |
| `--grey` | `#e2d6c0d9` |
| `--line` | `#e2d6c04d` |
| `--hover` | `currentColor` |
| `--focus` | `var(--cream)` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `bar__nav` |
| `<nav>` | `-` | `` |
| `<header>` | `-` | `bar` |
| `<main>` | `content` | `` |
| `<footer>` | `-` | `foot ui` |
| `<dialog>` | `-` | `menu` |
