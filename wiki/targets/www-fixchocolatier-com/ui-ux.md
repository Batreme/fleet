---
title: "UI & Design System: www-fixchocolatier-com"
date: 2026-11-14
target: "[[overview|www-fixchocolatier-com]]"
---

# UI Architecture & Design Tokens: www-fixchocolatier-com

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--font-sharpsans` | `"sharpSans", "sharpSans Fallback"}
@font-face{font-family:sy` |
| `--time` | `not(.react-datepicker__header--time--only){border-top-left-r` |
| `--next--with-time` | `not(.react-datepicker__navigation--next--with-today-button){` |
| `--next` | `before{left:-7px` |
| `--previous` | `before{right:-7px` |
| `--selected` | `hover{background-color:#216ba5}.react-datepicker__time-conta` |
| `--clickable` | `not(.react-datepicker__week-number--selected):hover{backgrou` |
| `--selected` | `hover{background-color:#1d5d90}.react-datepicker__day-names{` |
| `--highlighted` | `not([aria-disabled=true]):hover,.react-datepicker__month-tex` |
| `--holidays` | `not([aria-disabled=true]):hover,.react-datepicker__month-tex` |
| `--selected` | `not([aria-disabled=true]):hover,.react-datepicker__day--in-s` |
| `--keyboard-selected` | `not([aria-disabled=true]):hover,.react-datepicker__month-tex` |
| `--disabled` | `after{cursor:default` |
| `--tw-border-spacing-x` | `0` |
| `--tw-border-spacing-y` | `0` |
| `--tw-translate-x` | `0` |
| `--tw-translate-y` | `0` |
| `--tw-rotate` | `0` |
| `--tw-skew-x` | `0` |
| `--tw-skew-y` | `0` |
| `--tw-scale-x` | `1` |
| `--tw-scale-y` | `1` |
| `--tw-pan-x` | `` |
| `--tw-pan-y` | `` |
| `--tw-pinch-zoom` | `` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `secPad-x pointer-events-none flex items-center justify-between py-8 text-beige` |
| `<nav>` | `-` | `transition-transfrom-opacity absolute left-16 top-48 z-[999] flex origin-top-left items-stretch roun` |
| `<header>` | `-` | `pointer-events-none absolute left-0 top-0 z-9 w-screen transition-opacity duration-300 opacity-0` |
| `<main>` | `-` | `home-main relative flex w-full flex-col text-white` |
