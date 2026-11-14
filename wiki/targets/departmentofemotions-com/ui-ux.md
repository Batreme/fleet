---
title: "UI & Design System: departmentofemotions-com"
date: 2026-11-14
target: "[[overview|departmentofemotions-com]]"
---

# UI Architecture & Design Tokens: departmentofemotions-com

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--ink` | `oklch(28% .022 154)` |
| `--muted` | `oklch(49% .016 154)` |
| `--line` | `oklch(86% .012 125)` |
| `--paper` | `oklch(98% .008 105)` |
| `--desktop-wheel-size` | `clamp(74vw, 120svh, 92vw)` |
| `--desktop-wheel-size` | `clamp(74vw, 120dvh, 92vw)}}}@media(min-width:1024px)and (max` |
| `--mobile-wheel-size` | `min(160vw, 820px)` |
| `--mobile-wheel-size` | `min(120vw, 1100px)}.emotion-drawer .emotion-reading{max-widt` |
| `--landscape-wheel-size` | `clamp(560px, 160svh, 92vw)` |
| `--landscape-wheel-size` | `clamp(560px, 160dvh, 92vw)}}.emotion-sidebar{display:block` |
| `--lab-toolbar-height` | `0px}.wheel-lab .interactive-wheel,.wheel-lab .lab-switcher{-` |
| `--lab-toolbar-height` | `0px}.lab-switcher{position:fixed` |
| `--phone-wheel-size` | `213.75vw` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `lab-switcher` |
| `<nav>` | `-` | `emotion-family` |
| `<aside>` | `-` | `emotion-sidebar` |
| `<main>` | `explorer-main` | `explorer-main` |
| `<footer>` | `-` | `sidebar-footer` |
