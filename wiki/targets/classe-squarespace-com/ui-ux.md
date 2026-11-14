---
title: "UI & Design System: classe-squarespace-com"
date: 2026-11-14
target: "[[overview|classe-squarespace-com]]"
---

# UI Architecture & Design Tokens: classe-squarespace-com

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--tint` | `hsl(var(--accent-hsl))` |
| `--tint-a` | `.35` |
| `--gray` | `1` |
| `--lift` | `18px` |
| `--depth` | `0 2px 4px hsla(var(--darkAccent-hsl), .16), 0 calc(var(--lif` |
| `--ink` | `var(--headingLargeColor, hsl(var(--darkAccent-hsl)))` |
| `--wine` | `hsl(var(--accent-hsl))` |
| `--edge` | `hsl(var(--darkAccent-hsl))` |
| `--cream` | `hsl(var(--white-hsl))` |
| `--rose` | `hsl(var(--lightAccent-hsl))` |
| `--hi` | `hsl(var(--lightAccent-hsl))` |
| `--hi-text` | `hsl(var(--darkAccent-hsl))` |
| `--stub` | `var(--wine)` |
| `--sel-line` | `var(--edge)` |
| `--sel-fill` | `var(--cream)` |
| `--sel-size` | `11px` |
| `--sel-e` | `calc(var(--sel-size) / 2 - .75px)` |
| `--sel-in` | `calc(var(--sel-size) - 3px)` |
| `--sel-bg` | `linear-gradient(var(--sel-fill), var(--sel-fill)) 1.5px 1.5p` |
| `--card-w` | `clamp(210px, 17vw, 310px)` |
| `--text-w` | `clamp(320px, 27vw, 520px)` |
| `--gap` | `24px` |
| `--stub-w` | `calc(var(--text-w) - var(--gap))` |
| `--pad` | `clamp(26px, 2.4vw, 42px)` |
| `--top-space` | `48px` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `header-nav-list` |
| `<nav>` | `-` | `header-nav-list` |
| `<nav>` | `-` | `header-menu-nav-list` |
| `<header>` | `header` | `header theme-col--primary` |
| `<header>` | `-` | `newsletter-form-header` |
| `<main>` | `page` | `container` |
| `<footer>` | `footer-sections` | `sections` |
