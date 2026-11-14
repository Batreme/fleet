---
title: "UI & Design System: vault-hyperiux-com"
date: 2026-11-14
target: "[[overview|vault-hyperiux-com]]"
---

# UI Architecture & Design Tokens: vault-hyperiux-com

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--g-shift` | `0px}*,::backdrop,:after,:before{--tw-translate-x:0` |
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
| `--tw-pan-x` | `initial` |
| `--tw-pan-y` | `initial` |
| `--tw-pinch-zoom` | `initial` |
| `--tw-space-y-reverse` | `0` |
| `--tw-space-x-reverse` | `0` |
| `--tw-border-style` | `solid` |
| `--tw-gradient-position` | `initial` |
| `--tw-gradient-from` | `#0000` |
| `--tw-gradient-via` | `#0000` |
| `--tw-gradient-to` | `#0000` |
| `--tw-gradient-stops` | `initial` |
| `--tw-gradient-via-stops` | `initial` |
| `--tw-gradient-from-position` | `0%` |
| `--tw-gradient-via-position` | `50%` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `[--nav-h:3.65vw] py-[calc(var(--hx-vw,1vw)*2)] flex max-lg:hidden items-center justify-between w-ful` |
| `<nav>` | `-` | `sticky top-[40svh] grid gap-[calc(var(--cvw)*1.2)] self-start max-md:hidden` |
| `<main>` | `hero-v3` | `relative w-full overflow-x-clip` |
| `<footer>` | `footer` | `relative z-200 py-[calc(var(--cvw)*7)] max-lg:py-[10vw] w-full overflow-x-clip section-x max-md:py-[` |
