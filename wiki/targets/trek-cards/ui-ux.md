---
title: "UI & Design System: trek-cards"
date: 2026-11-14
target: "[[overview|trek-cards]]"
---

# UI Architecture & Design Tokens: trek-cards

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--ground` | `#18001A` |
| `--bg` | `#1A0A2E` |
| `--surface` | `#221041` |
| `--surface-2` | `#2E1650` |
| `--purple` | `#6A00FF` |
| `--pink` | `#FF00EE` |
| `--lilac` | `#B176FF` |
| `--ink` | `#FFFFFF` |
| `--muted` | `#B6A6D6` |
| `--soft` | `rgba(255, 255, 255, 0.72)` |
| `--stroke` | `rgba(255, 255, 255, 0.08)` |
| `--green` | `#68FF8E` |
| `--title` | `'Rubik One', 'Rubik', sans-serif` |
| `--body` | `'Rubik', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans` |
| `--brand` | `linear-gradient(55deg, #7B22FF 0%, #C215F6 38%, #FF00EE 82%)` |
| `--ease` | `cubic-bezier(.2, .8, .2, 1)` |
| `--pad` | `clamp(20px, 5vw, 72px)` |
| `--t` | `900px` |
| `--glass` | `:after { content: ''` |
| `--glass` | `hover::after, .btn--glass.is-hot::after { opacity: 1` |
| `--glass` | `hover { transform: translateY(-2px)` |
| `--play` | `hover { transform: translateY(-2px) scale(1.03)` |
| `--nav` | `hover { transform: scale(1.05)` |
| `--u` | `calc(var(--w, 300px) / 352)` |
| `--pw` | `260px` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `nav__links` |
| `<nav>` | `-` | `foot__links` |
| `<header>` | `nav` | `nav` |
| `<header>` | `-` | `ch-head` |
| `<header>` | `-` | `ch-head ch-head--center` |
| `<header>` | `-` | `ch-head ch-head--center ch-head--legacy` |
| `<header>` | `-` | `ch-head ch-head--center` |
| `<main>` | `top` | `` |
| `<footer>` | `-` | `foot` |
