---
title: "UI & Design System: citadelgroup-org"
date: 2026-11-14
target: "[[overview|citadelgroup-org]]"
---

# UI Architecture & Design Tokens: citadelgroup-org

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--citadel-orange` | `#f7953e` |
| `--citadel-dark-orange` | `#f87000` |
| `--citadel-medium-grey` | `#818486` |
| `--citadel-light-grey` | `#e3e3e4` |
| `--citadel-black` | `#000000` |
| `--color-brand-orange` | `var(--citadel-orange)` |
| `--color-brand-dark-orange` | `var(--citadel-dark-orange)` |
| `--color-brand-orange-hover` | `#e17e00` |
| `--color-brand-black` | `var(--citadel-black)` |
| `--color-brand-medium-grey` | `var(--citadel-medium-grey)` |
| `--color-brand-light-grey` | `var(--citadel-light-grey)` |
| `--color-bg-dark` | `var(--citadel-black)` |
| `--color-bg-light` | `var(--citadel-light-grey)` |
| `--color-text-primary` | `var(--citadel-black)` |
| `--color-accent` | `var(--citadel-orange)` |
| `--font-citadel-heading` | `"Montserrat", system-ui, sans-serif` |
| `--font-citadel-body` | `"Montserrat", system-ui, sans-serif` |
| `--font-citadel-highlight` | `"Bebas Neue", system-ui, sans-serif` |
| `--resource-hub-page-background` | `#f4f2ee` |
| `--resource-hub-accent` | `var(--citadel-dark-orange)` |
| `--resource-hub-content-background` | `var(--citadel-light-grey)` |
| `--resource-hub-hero-background` | `#080808` |
| `--resource-hub-surface` | `#ffffff` |
| `--resource-hub-preview-background` | `var(--citadel-light-grey)` |
| `--resource-hub-text-primary` | `#111111` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `citadel-site-nav relative` |
| `<header>` | `-` | `citadel-site-header is-over-hero` |
| `<main>` | `main-content` | `citadel-homepage bg-dark` |
| `<footer>` | `-` | `site-footer-meta` |
