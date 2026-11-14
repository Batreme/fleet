---
title: "UI & Design System: giallostudio-it_en-the-experience"
date: 2026-11-14
target: "[[overview|giallostudio-it_en-the-experience]]"
---

# UI Architecture & Design Tokens: giallostudio-it_en-the-experience

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--ink` | `#050608` |
| `--paper` | `#f2f1ea` |
| `--muted` | `#f2f1eabd` |
| `--yellow` | `#f5f505` |
| `--gutter` | `clamp(1.25rem, 5vw, 5.5rem)` |
| `--xp-top` | `calc(5rem + env(safe-area-inset-top,0px) + clamp(.75rem, 3.5` |
| `--xp-bottom` | `calc(env(safe-area-inset-bottom,0px) + clamp(1.25rem, 5.5vh,` |
| `--xp-left` | `max(var(--gutter), calc(env(safe-area-inset-left,0px) + 1rem` |
| `--xp-right` | `max(var(--gutter), calc(env(safe-area-inset-right,0px) + 1re` |
| `--xp-gap` | `clamp(.7rem, 2.2vh, 1.6rem)` |
| `--xp-title` | `clamp(3.4rem, min(8.4vw, 14.5vh), 9.25rem)` |
| `--xp-title-hero` | `clamp(3.8rem, min(10.2vw, 16.5vh), 11rem)` |
| `--xp-body` | `clamp(1.02rem, min(1.25vw, 2.3vh), 1.3rem)` |
| `--sx` | `100%` |
| `--sy` | `0%}.wa6Phq_root[data-mode=immersive] .wa6Phq_chapter[data-ch` |
| `--sy` | `50%}.wa6Phq_chapter[data-place=bottom-right]{--sx:100%` |
| `--sy` | `100%}.wa6Phq_chapter[data-place=top-left]{--sx:0%` |
| `--sy` | `0%}.wa6Phq_root[data-mode=immersive] .wa6Phq_chapter[data-pl` |
| `--gutter` | `clamp(1.25rem, 5vw, 5.5rem)` |
| `--xp-title` | `clamp(2.3rem, min(7.6vw, 12.5vh), 5.75rem)` |
| `--xp-title-hero` | `clamp(2.5rem, min(8.8vw, 14.5vh), 6.75rem)` |
| `--xp-body` | `clamp(.95rem, min(1.7vw, 2.6vh), 1.1rem)}}@media (max-width:` |
| `--xp-title-hero` | `clamp(2.5rem, 13vw, 3.8rem)` |
| `--xp-body` | `.98rem}.wa6Phq_root[data-mode=immersive] .wa6Phq_chapter[dat` |
| `--sx` | `0%` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `wa6Phq_districts` |
| `<nav>` | `-` | `mt-6` |
| `<nav>` | `-` | `` |
| `<nav>` | `-` | `` |
| `<nav>` | `-` | `` |
| `<nav>` | `-` | `` |
| `<nav>` | `-` | `` |
| `<nav>` | `-` | `` |
| `<header>` | `-` | `fixed inset-x-0 top-0 z-[70] transition-colors duration-300 border-b border-transparent` |
| `<main>` | `main` | `flex-1` |
| `<footer>` | `-` | `relative overflow-hidden bg-ink text-paper` |
