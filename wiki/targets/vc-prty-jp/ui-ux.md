---
title: "UI & Design System: vc-prty-jp"
date: 2026-11-14
target: "[[overview|vc-prty-jp]]"
---

# UI Architecture & Design Tokens: vc-prty-jp

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--font-inter` | `"Inter", "Inter Fallback"}
@layer properties{@supports (((-w` |
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
| `--tw-border-style` | `solid` |
| `--tw-leading` | `initial` |
| `--tw-font-weight` | `initial` |
| `--tw-tracking` | `initial` |
| `--tw-shadow` | `0 0 #0000` |
| `--tw-shadow-color` | `initial` |
| `--tw-shadow-alpha` | `100%` |
| `--tw-inset-shadow` | `0 0 #0000` |
| `--tw-inset-shadow-color` | `initial` |
| `--tw-inset-shadow-alpha` | `100%` |
| `--tw-ring-color` | `initial` |
| `--tw-ring-shadow` | `0 0 #0000` |
| `--tw-inset-ring-color` | `initial` |
| `--tw-inset-ring-shadow` | `0 0 #0000` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `fixed bottom-[calc(14*var(--vw))] left-0 right-0 z-nav flex items-center gap-[calc(10*var(--vw))] px` |
| `<footer>` | `-` | `relative border-t border-black` |
