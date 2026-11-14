---
title: "UI & Design System: nakagawa-corp-com"
date: 2026-11-14
target: "[[overview|nakagawa-corp-com]]"
---

# UI Architecture & Design Tokens: nakagawa-corp-com

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--leap-project-main` | `var(--clr-primary-default, #0073aa)` |
| `--leap-project-text-primary` | `var(--clr-text-primary, #404044)` |
| `--leap-project-wh` | `var(--clr-wht, #fff)` |
| `--leap-project-bg` | `var(--clr-bg-01, #F7F7F4)` |
| `--leap-project-mono-01` | `var(--clr-mono-01, #F2F2F2)` |
| `--leap-project-mono-02` | `var(--clr-mono-03, #BABDC4)` |
| `--leap-project-bold` | `var(--font-weight-bold, 600)` |
| `--leap-project-radius-none` | `0` |
| `--leap-project-radius-default` | `var(--border-radius-primary, .5rem)` |
| `--leap-project-radius-max` | `var(--border-radius-max, 100vmax)` |
| `--ttl` | `has(+ .blog_card--txt) {
    margin-bottom: 8px !important` |
| `--fz` | `16` |
| `--fz` | `14` |
| `--rem` | `calc(1 / var(--fz) * 1rem)` |
| `--header-hgt` | `96` |
| `--header-hgt-fx` | `80` |
| `--header-hgt` | `64` |
| `--header-hgt-fx` | `64` |
| `--inner-xs` | `720` |
| `--inner-sm` | `1080` |
| `--inner-md` | `1600` |
| `--inner-lg` | `1600` |
| `--inner-xl` | `1760` |
| `--section_pdg-sm` | `120` |
| `--section_pdg-md` | `160` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `fnav` |
| `<nav>` | `-` | `modal__nav` |
| `<header>` | `-` | `header header-main header-sp-top` |
| `<aside>` | `-` | `sns_area` |
| `<aside>` | `-` | `sns_area` |
| `<main>` | `-` | `` |
| `<footer>` | `-` | `footer` |
