---
title: "UI & Design System: peabodyhouse-com"
date: 2026-11-14
target: "[[overview|peabodyhouse-com]]"
---

# UI Architecture & Design Tokens: peabodyhouse-com

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--toast-shift` | `.25rem}.contact-action.svelte-1jkaixm{grid-row:3 / 4` |
| `--gap` | `16px` |
| `--pad` | `max(var(--col), calc((100vw - 84rem)/2) )` |
| `--cell` | `calc((100vw - 2 * var(--pad) - 3 * var(--gap)) / 4)` |
| `--m-cell` | `18rem` |
| `--card-pad` | `clamp(.75rem, calc(var(--cell) * .052), 1rem)` |
| `--card-title` | `clamp( 1.125rem, calc(var(--cell) * .078), var(--font-size-x` |
| `--send-pad` | `clamp(.75rem, calc(var(--cell) * .078), 1.5rem)` |
| `--face-ow` | `var(--cell)` |
| `--face-oh` | `var(--cell)}.tile.svelte-19icql0:nth-child(1) .split-a:where` |
| `--face-ow` | `var(--cell)` |
| `--face-oh` | `var(--cell)}.tile.svelte-19icql0:nth-child(2) .split-a:where` |
| `--face-ow` | `var(--cell)` |
| `--face-oh` | `var(--cell)}.tile.svelte-19icql0:nth-child(3) .split-a:where` |
| `--face-ow` | `var(--cell)` |
| `--face-oh` | `var(--cell)}.tile.svelte-19icql0:nth-child(4) .split-a:where` |
| `--cell` | `initial` |
| `--card-pad` | `1rem` |
| `--card-title` | `var(--font-size-xl)` |
| `--send-pad` | `1.5rem` |
| `--front` | `where(.svelte-11f2mhf){grid-area:1 / 1 / 3 / 3` |
| `--back` | `where(.svelte-11f2mhf){grid-area:2 / 2 / 4 / 4` |
| `--regular` | `where(.svelte-126o6dr){font-weight:400` |
| `--active` | `where(.svelte-126o6dr){font-weight:500` |
| `--regular` | `where(.svelte-126o6dr){opacity:0}header.svelte-126o6dr nav:w` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `svelte-126o6dr` |
| `<nav>` | `-` | `links svelte-352yma` |
| `<header>` | `-` | `svelte-126o6dr` |
| `<header>` | `-` | `header svelte-19icql0` |
| `<aside>` | `-` | `hand js-line-displacement svelte-x35jl1` |
| `<main>` | `-` | `` |
| `<footer>` | `-` | `grid js-line-displacement svelte-352yma` |
