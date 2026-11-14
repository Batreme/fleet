---
title: "UI & Design System: seedrouter-ai"
date: 2026-11-14
target: "[[overview|seedrouter-ai]]"
---

# UI Architecture & Design Tokens: seedrouter-ai

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--shimmer-angle` | `20deg}*,:before,:after,::backdrop{--tw-translate-x:0` |
| `--tw-translate-y` | `0` |
| `--tw-translate-z` | `0` |
| `--tw-scale-x` | `1` |
| `--tw-scale-y` | `1` |
| `--tw-scale-z` | `1` |
| `--tw-rotate-x` | `initial` |
| `--tw-rotate-y` | `initial` |
| `--tw-rotate-z` | `initial` |
| `--tw-skew-x` | `initial` |
| `--tw-skew-y` | `initial` |
| `--tw-space-y-reverse` | `0` |
| `--tw-space-x-reverse` | `0` |
| `--tw-divide-y-reverse` | `0` |
| `--tw-border-style` | `solid` |
| `--tw-gradient-position` | `initial` |
| `--tw-gradient-from` | `#0000` |
| `--tw-gradient-via` | `#0000` |
| `--tw-gradient-to` | `#0000` |
| `--tw-gradient-stops` | `initial` |
| `--tw-gradient-via-stops` | `initial` |
| `--tw-gradient-from-position` | `0%` |
| `--tw-gradient-via-position` | `50%` |
| `--tw-gradient-to-position` | `100%` |
| `--tw-leading` | `initial` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `hidden h-16 xl:flex xl:items-center xl:justify-between xl:gap-5 xl:pe-8` |
| `<nav>` | `-` | `group/navigation-menu relative flex max-w-max items-center justify-center ms-auto me-3 flex-none [&>` |
| `<nav>` | `-` | `flex flex-wrap items-center gap-2` |
| `<nav>` | `-` | `flex flex-wrap items-center justify-center gap-x-2.5 gap-y-3 border-t border-white/15 px-[max(0px,ca` |
| `<nav>` | `-` | `flex flex-1 flex-wrap items-center justify-center gap-x-5 gap-y-2` |
| `<header>` | `-` | `sr-chrome sticky inset-x-0 top-0 z-40 border-b border-transparent bg-[var(--sr-bg)] font-[family-nam` |
| `<main>` | `-` | `flex-1` |
| `<footer>` | `-` | `sr-chrome-dark relative border-t border-[var(--sr-line)] bg-[var(--sr-footer)] font-[family-name:var` |
