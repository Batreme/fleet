---
title: "UI & Design System: almirakho-com"
date: 2026-10-31
target: "[[overview|almirakho-com]]"
---

# UI Architecture & Design Tokens: almirakho-com

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--vw` | `100vw` |
| `--vh` | `100vh` |
| `--ivh` | `100dvh` |
| `--rem` | `1px` |
| `--main-font-name` | `"Archivo"` |
| `--display-font-name` | `"Archivo"` |
| `--main-font` | `var(--main-font-name), "Helvetica Neue", "Arial", sans-serif` |
| `--display-font` | `var(--display-font-name), "Helvetica Neue", "Arial", sans-se` |
| `--color-black` | `#0a0a0a` |
| `--color-white` | `#fafafa` |
| `--color-white-50` | `#ffffff80` |
| `--color-white-5` | `#ffffff0d` |
| `--color-red` | `#e45050` |
| `--grid-margin` | `20rem` |
| `--grid-gutter` | `20rem` |
| `--grid-column` | `calc(var(--vw)/10 - var(--grid-gutter)*9/10 - var(--grid-mar` |
| `--gap-xs` | `5rem` |
| `--gap-s` | `10rem` |
| `--gap-m` | `20rem` |
| `--gap-l` | `40rem` |
| `--gap-xl` | `60rem` |
| `--gap-xxl` | `100rem` |
| `--gap-xxxl` | `140rem` |
| `--radius-xs` | `4rem` |
| `--radius-s` | `8rem` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<header>` | `-` | `header` |
| `<main>` | `-` | `` |
