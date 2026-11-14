---
title: "UI & Design System: gmxdigital-com_en"
date: 2026-11-14
target: "[[overview|gmxdigital-com_en]]"
---

# UI Architecture & Design Tokens: gmxdigital-com_en

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--ink` | `#050506` |
| `--paper` | `#f2f1ed` |
| `--muted` | `rgba(244, 244, 241, .68)` |
| `--hairline` | `rgba(244, 244, 241, .18)` |
| `--violet` | `#aa91c2` |
| `--violet-deep` | `#75647f` |
| `--magenta` | `#b86b9f` |
| `--mist` | `#9fb5b7` |
| `--accent-gradient` | `linear-gradient(90deg, #bba2cf 0%, #8277a9 48%, #68899d 100%` |
| `--petrol` | `#07171b` |
| `--ease-out` | `cubic-bezier(.16, 1, .3, 1)` |
| `--ease-in-out` | `cubic-bezier(.76, 0, .24, 1)` |
| `--page-pad` | `clamp(1.25rem, 3.8vw, 4.5rem)` |
| `--hero-progress` | `0` |
| `--smoke-intensity` | `0` |
| `--smoke-x` | `-24%` |
| `--primary` | `hover, .button--primary:focus-visible { color: var(--paper)` |
| `--quiet` | `hover, .button--quiet:focus-visible { border-color: rgba(244` |
| `--experience-accent` | `#b498c4` |
| `--experience-accent` | `#c9aa66` |
| `--ultra` | `:before { inset: -12% -8% auto 28%` |
| `--ultra` | `:after { content: ""` |
| `--portrait-width` | `clamp(15.5rem, 20vw, 22rem)` |
| `--matter-field-opacity` | `.16` |
| `--matter-velocity` | `0` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `main-nav` | `site-nav` |
| `<nav>` | `-` | `production-timeline` |
| `<nav>` | `-` | `` |
| `<header>` | `-` | `site-header` |
| `<header>` | `-` | `production-head` |
| `<main>` | `conteudo` | `` |
| `<footer>` | `-` | `footer footer--signature` |
| `<dialog>` | `portfolio-film-dialog` | `video-dialog` |
