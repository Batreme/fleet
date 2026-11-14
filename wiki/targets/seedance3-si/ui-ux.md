---
title: "UI & Design System: seedance3-si"
date: 2026-11-14
target: "[[overview|seedance3-si]]"
---

# UI Architecture & Design Tokens: seedance3-si

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--theme-promotion` | `#d3ff02` |
| `--theme-promotion-text` | `#d3ff02` |
| `--theme-discount` | `var(--theme-promotion-text)` |
| `--theme-primary` | `#d3ff02` |
| `--theme-primary-text` | `var(--theme-promotion-text)` |
| `--theme-logo-gradient` | `linear-gradient(var(--theme-promotion-text),var(--theme-prom` |
| `--theme-highlight` | `var(--theme-primary)` |
| `--theme-promo-background` | `#111113` |
| `--theme-promo-foreground` | `#e4e4e7` |
| `--brand-from` | `var(--theme-highlight)` |
| `--brand-via` | `var(--theme-highlight)` |
| `--brand-to` | `var(--theme-secondary)` |
| `--brand-accent` | `var(--theme-primary)` |
| `--brand-accent-strong` | `var(--theme-primary-strong)` |
| `--brand-accent-soft` | `var(--theme-primary-soft)` |
| `--theme-secondary` | `var(--theme-primary)` |
| `--theme-primary-strong` | `#b5df00` |
| `--theme-primary-foreground` | `#171719` |
| `--theme-primary-soft` | `color-mix(in srgb,var(--theme-primary)10%,transparent)` |
| `--theme-primary-border` | `color-mix(in srgb,var(--theme-primary)30%,transparent)` |
| `--theme-heading-gradient` | `linear-gradient(var(--foreground),var(--foreground))` |
| `--theme-action-gradient` | `linear-gradient(var(--theme-primary),var(--theme-primary))` |
| `--theme-icon-gradient` | `linear-gradient(var(--theme-primary),var(--theme-primary))` |
| `--theme-edge-gradient` | `linear-gradient(var(--theme-primary),var(--theme-primary))` |
| `--theme-section-aura` | `none` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `hidden md:flex items-center justify-center gap-8 flex-1 no-rtl-reverse` |
| `<nav>` | `-` | `` |
| `<header>` | `-` | `tool-header fixed inset-x-0 z-50 border-b bg-background transition-[top] duration-200 top-12 sm:top-` |
| `<header>` | `-` | `mb-6 md:mb-8` |
| `<header>` | `-` | `max-w-3xl mb-10 md:mb-14` |
| `<header>` | `-` | `mb-9 grid items-end gap-5 md:mb-12 lg:grid-cols-[minmax(0,1fr)_minmax(0,0.55fr)] lg:gap-16` |
| `<header>` | `-` | `text-start lg:row-span-2` |
| `<aside>` | `-` | `mt-10 py-4 sm:py-6 md:mt-12` |
| `<main>` | `-` | `flex-1 overflow-x-hidden w-full` |
| `<footer>` | `-` | `` |
