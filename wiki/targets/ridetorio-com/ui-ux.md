---
title: "UI & Design System: ridetorio-com"
date: 2026-11-14
target: "[[overview|ridetorio-com]]"
---

# UI Architecture & Design Tokens: ridetorio-com

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--paper` | `#F4EAD0` |
| `--paper-2` | `#FBF4DF` |
| `--ink` | `#1E1B16` |
| `--ink-soft` | `#4A4337` |
| `--olive` | `#8C9A4A` |
| `--forest` | `#2F4A2C` |
| `--mustard` | `#D9A93B` |
| `--teal` | `#2F8F8B` |
| `--red` | `#C8452C` |
| `--sky` | `#A9D3DE` |
| `--dusk` | `#F2A27C` |
| `--night` | `#16233A` |
| `--sky-top` | `var(--paper)` |
| `--sky-bot` | `var(--paper)` |
| `--stars` | `0` |
| `--font-body` | `"Fraunces", "Iowan Old Style", Georgia, serif` |
| `--font-stamp` | `"Alfa Slab One", "Rockwell", Georgia, serif` |
| `--font-hand` | `"Caveat", "Bradley Hand", cursive` |
| `--gutter` | `clamp(1.1rem, 4vw, 3.5rem)` |
| `--measure` | `34rem` |
| `--radius` | `26px` |
| `--shadow` | `4px 4px 0 var(--ink)` |
| `--ease` | `cubic-bezier(.2, .8, .2, 1)` |
| `--ghost` | `hover { box-shadow: none` |
| `--ridge-h` | `clamp(64px, 12vw, 190px)` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `nav__links` |
| `<nav>` | `-` | `panel__nav` |
| `<nav>` | `-` | `finish__nav` |
| `<header>` | `-` | `nav` |
| `<header>` | `-` | `story__head` |
| `<header>` | `-` | `journey__intro` |
| `<header>` | `-` | `film__head` |
| `<aside>` | `-` | `panel` |
| `<main>` | `-` | `` |
| `<footer>` | `-` | `` |
| `<footer>` | `-` | `` |
| `<footer>` | `-` | `` |
| `<footer>` | `-` | `` |
| `<footer>` | `-` | `` |
| `<footer>` | `-` | `` |
