---
title: "UI & Design System: velourproductions-com"
date: 2026-10-31
target: "[[overview|velourproductions-com]]"
---

# UI Architecture & Design Tokens: velourproductions-com

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--color-red` | `#fe2f00` |
| `--color-blue` | `#3a70e6` |
| `--color-paper` | `#f4f0e5` |
| `--color-ink` | `#1a1a1a` |
| `--color-ink-soft` | `#202020` |
| `--color-taupe` | `#a59b87` |
| `--font-display` | `"Velour Display", "Arial Narrow", "Helvetica Neue", sans-ser` |
| `--font-mono` | `"Velour Mono", "Courier New", monospace` |
| `--type-meta` | `clamp(.625rem, .72vw, .6875rem)` |
| `--type-small` | `clamp(.75rem, .9vw, .8125rem)` |
| `--type-body` | `clamp(.875rem, 1.2vw, 1rem)` |
| `--leading-body` | `1.3` |
| `--type-display-caption` | `clamp(1.25rem, 1.55vw, 1.75rem)` |
| `--type-work-filter` | `clamp(1.875rem, 3.6vw, 3.5rem)` |
| `--type-display-xs` | `clamp(2.25rem, 3vw, 3rem)` |
| `--type-display-sm` | `clamp(2.75rem, 6.4vw, 6.5rem)` |
| `--type-footer-cta` | `clamp(5rem, 7.05vw, 6.375rem)` |
| `--type-display-md` | `clamp(4rem, 10.4vw, 11rem)` |
| `--type-display-lg` | `clamp(4.8rem, 13.5vw, 14rem)` |
| `--type-display-mobile-route` | `clamp(5.5rem, 24vw, 10.75rem)` |
| `--type-display-hero` | `clamp(5rem, min(18.4vw, 28svh), 17rem)` |
| `--type-photo-booth-headline` | `clamp(3.75rem, 7.05vw, 6.375rem)` |
| `--type-photo-booth-action` | `clamp(.75rem, .88vw, .8rem)` |
| `--type-photo-booth-privacy` | `.625rem` |
| `--type-photo-booth-countdown` | `clamp(4rem, 15vw, 7rem)` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `site-footer__nav` |
| `<nav>` | `-` | `site-header__nav` |
| `<header>` | `-` | `site-header` |
| `<main>` | `-` | `` |
| `<footer>` | `contact` | `site-footer` |
| `<dialog>` | `-` | `photo-booth` |
| `<dialog>` | `-` | `floating-reel__dialog` |
