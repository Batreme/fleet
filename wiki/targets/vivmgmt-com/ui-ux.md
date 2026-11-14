---
title: "UI & Design System: vivmgmt-com"
date: 2026-11-14
target: "[[overview|vivmgmt-com]]"
---

# UI Architecture & Design Tokens: vivmgmt-com

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--color-page-bg` | `#ffffff` |
| `--color-page-text` | `#000000` |
| `--space-xs` | `clamp(.3125rem, .2344rem + .3906vw, .625rem)` |
| `--space-s` | `clamp(.625rem, .4688rem + .7813vw, 1.25rem)` |
| `--space-m` | `clamp(1.25rem, .9375rem + 1.5625vw, 2.5rem)` |
| `--space-l` | `clamp(1.875rem, 1.4063rem + 2.3438vw, 3.75rem)` |
| `--space-xl` | `clamp(2.5rem, 1.875rem + 3.125vw, 5rem)` |
| `--space-2xl` | `clamp(3.125rem, 2.3438rem + 3.9063vw, 6.25rem)` |
| `--space-3xl` | `clamp(3.75rem, 2.8125rem + 4.6875vw, 7.5rem)` |
| `--space-4xl` | `clamp(4.375rem, 3.2813rem + 5.4688vw, 8.75rem)` |
| `--space-5xl` | `clamp(5rem, 3.75rem + 6.25vw, 10rem)` |
| `--space-xs-s` | `clamp(.3125rem, .0781rem + 1.1719vw, 1.25rem)` |
| `--space-s-m` | `clamp(.625rem, .1563rem + 2.3438vw, 2.5rem)` |
| `--space-m-l` | `clamp(1.25rem, .625rem + 3.125vw, 3.75rem)` |
| `--space-l-xl` | `clamp(1.875rem, 1.0938rem + 3.9063vw, 5rem)` |
| `--space-xl-2xl` | `clamp(2.5rem, 1.5625rem + 4.6875vw, 6.25rem)` |
| `--space-2xl-3xl` | `clamp(3.125rem, 2.0313rem + 5.4688vw, 7.5rem)` |
| `--space-3xl-4xl` | `clamp(3.75rem, 2.5rem + 6.25vw, 8.75rem)` |
| `--space-4xl-5xl` | `clamp(4.375rem, 2.9688rem + 7.0313vw, 10rem)}html{-moz-osx-f` |
| `--media-seek-backward-button-display` | `none` |
| `--seek-backward-button` | `none` |
| `--bottom-seek-backward-button` | `none` |
| `--media-seek-forward-button-display` | `none` |
| `--seek-forward-button` | `none` |
| `--bottom-seek-forward-button` | `none` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `js-navbar` | `c-navbar` |
| `<main>` | `main-content` | `lenis` |
| `<footer>` | `-` | `c-footer` |
