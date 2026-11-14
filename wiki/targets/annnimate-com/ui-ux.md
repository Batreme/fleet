---
title: "UI & Design System: annnimate-com"
date: 2026-11-14
target: "[[overview|annnimate-com]]"
---

# UI Architecture & Design Tokens: annnimate-com

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--sl-foreground` | `#171717` |
| `--sl-background` | `#fafafa` |
| `--sl-comment` | `#737373` |
| `--sl-comment-delimiter` | `#737373` |
| `--sl-punctuation` | `#525252` |
| `--sl-property` | `#65a30d` |
| `--sl-tag` | `#65a30d` |
| `--sl-constant` | `#ea580c` |
| `--sl-number` | `#ea580c` |
| `--sl-string` | `#0891b2` |
| `--sl-attribute` | `#0891b2` |
| `--sl-keyword` | `#84cc16` |
| `--sl-function` | `#84cc16` |
| `--sl-class` | `#84cc16` |
| `--sl-variable` | `#a3e635` |
| `--sl-regex` | `#db2777` |
| `--sl-operator` | `#525252}:root:not(.dark) .pl-c,:root:not(.dark) .pl-c1,:root` |
| `--sl-background` | `#0a0a0a` |
| `--sl-comment` | `#6b7280` |
| `--sl-comment-delimiter` | `#6b7280` |
| `--sl-punctuation` | `#9ca3af` |
| `--sl-property` | `#84cc16` |
| `--sl-tag` | `#84cc16` |
| `--sl-constant` | `#fb923c` |
| `--sl-number` | `#fb923c` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `relative hidden h-full items-center justify-center lg:col-span-4 lg:col-start-5 lg:flex` |
| `<nav>` | `-` | `hidden lg:col-span-2 lg:block lg:col-start-7` |
| `<nav>` | `-` | `hidden lg:col-span-2 lg:block` |
| `<nav>` | `-` | `hidden lg:col-span-2 lg:block` |
| `<header>` | `-` | `v2-header inset-x-0 top-0 z-[300] pt-[var(--v2-header-gap)] fixed` |
| `<main>` | `-` | `flex-1 relative z-[2] bg-background` |
| `<footer>` | `-` | `annnimate-footer relative bg-background px-8 pb-8 lg:px-32 lg:pb-32` |
