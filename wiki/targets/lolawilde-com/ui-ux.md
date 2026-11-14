---
title: "UI & Design System: lolawilde-com"
date: 2026-11-14
target: "[[overview|lolawilde-com]]"
---

# UI Architecture & Design Tokens: lolawilde-com

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--encore-shortest-1` | `50ms` |
| `--encore-shortest-2` | `100ms` |
| `--encore-shortest-3` | `150ms` |
| `--encore-shortest-4` | `200ms` |
| `--encore-short-1` | `250ms` |
| `--encore-short-2` | `300ms` |
| `--encore-productive` | `cubic-bezier(0.3,0,0,1)` |
| `--encore-productive-decelerate` | `cubic-bezier(0,0,0.2,1)` |
| `--encore-productive-accelerate` | `cubic-bezier(0.8,0,1,1)` |
| `--encore-productive-exit-duration` | `var(--encore-shortest-4)` |
| `--encore-opacity-disabled` | `0.3` |
| `--encore-opacity-active` | `0.7` |
| `--encore-border-radius-rounded` | `9999px` |
| `--encore-overlay-box-shadow` | `0 4px 12px 0 #0000004d` |
| `--encore-overlay-drop-shadow` | `0 4px 6px #0000004d` |
| `--encore-focus-box-shadow` | `0 3px 0 0` |
| `--encore-sidebar-base-width` | `200px` |
| `--encore-z-index-popover` | `1060` |
| `--encore-z-index-skiplink` | `9999` |
| `--encore-z-index-dialog` | `1050` |
| `--encore-button-hover-scale` | `1.04` |
| `--encore-productive-enter` | `var(--encore-short-1) var(--encore-productive-decelerate)` |
| `--encore-productive-exit` | `var(--encore-shortest-4) var(--encore-productive-accelerate)` |
| `--origin` | `translateY(var(--encore-spacing-tighter-4))}.e-10682-overlay` |
| `--origin` | `translateY(calc(var(--encore-spacing-tighter-4)*-1))}.e-1068` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<header>` | `nav` | `nav` |
| `<main>` | `top` | `` |
| `<footer>` | `-` | `` |
