---
title: "UI & Design System: www-east64films-com"
date: 2026-11-14
target: "[[overview|www-east64films-com]]"
---

# UI Architecture & Design Tokens: www-east64films-com

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--cl-blue` | `#4eaebf` |
| `--cl-yellow` | `#f6b000` |
| `--cl-green` | `#00a44d` |
| `--cl-red` | `#e43936` |
| `--cl-orange` | `#f46f2c` |
| `--cl-dark` | `#151515` |
| `--cl-white` | `#ffffff` |
| `--cl-whitegray` | `#eeeeee` |
| `--cl-black` | `#1a1a1a` |
| `--cl-blackgray` | `#222222` |
| `--cl-lightgray` | `#b9b9b9` |
| `--cl-base` | `var(--cl-white)` |
| `--cl-bg` | `var(--cl-blackgray)` |
| `--fw-regular` | `400` |
| `--fw-medium` | `500` |
| `--fw-bold` | `700` |
| `--fw-black` | `900` |
| `--zindex-header` | `10` |
| `--ff-jp` | `"Noto Sans JP", sans-serif` |
| `--ff-en` | `"helvetica-neue-lt-pro", sans-serif` |
| `--ff-en2` | `"matrix-ii-ext-semi-narrow", sans-serif` |
| `--torem` | `calc(1rem / 16)` |
| `--font-size-xs` | `calc(12 * var(--torem))` |
| `--font-size-sm` | `calc(14 * var(--torem))` |
| `--font-size-md` | `calc(16 * var(--torem))` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `` |
| `<header>` | `masthead` | `site-header` |
| `<main>` | `main` | `site-main` |
| `<footer>` | `colophon` | `l-footer` |
