---
title: "UI & Design System: lpas-com"
date: 2026-11-14
target: "[[overview|lpas-com]]"
---

# UI Architecture & Design Tokens: lpas-com

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--row-gap` | `0` |
| `--column-gap` | `1rem` |
| `--xxlSpace` | `8.5rem}[data-grid=grid-template]{display:grid` |
| `--marketMainColor` | `rgb(98, 86, 83)` |
| `--marketSecondaryColor` | `rgb(123, 105, 100)` |
| `--marketContentColor` | `rgb(255, 255, 255)` |
| `--marketContentContrast` | `rgb(38, 38, 38)}[data-marketcolor=interiors]{--marketMainCol` |
| `--marketSecondaryColor` | `rgb(178, 113, 80)` |
| `--marketContentColor` | `rgb(255, 255, 255)` |
| `--marketContentContrast` | `rgb(38, 38, 38)}[data-marketcolor=higherEducation]{--marketM` |
| `--marketSecondaryColor` | `rgb(222, 231, 243)` |
| `--marketContentColor` | `rgb(38, 38, 38)` |
| `--marketContentContrast` | `rgb(255, 255, 255)}[data-marketcolor=civic]{--marketMainColo` |
| `--marketSecondaryColor` | `rgb(180, 198, 184)` |
| `--marketContentColor` | `rgb(255, 255, 255)` |
| `--marketContentContrast` | `rgb(38, 38, 38)}[data-marketcolor=commercial]{--marketMainCo` |
| `--marketSecondaryColor` | `rgb(241, 214, 196)` |
| `--marketContentColor` | `rgb(38, 38, 38)` |
| `--marketContentContrast` | `rgb(255, 255, 255)}[data-marketcolor=sand]{--marketMainColor` |
| `--marketSecondaryColor` | `rgb(235, 205, 180)` |
| `--marketContentColor` | `rgb(38, 38, 38)` |
| `--marketContentContrast` | `rgb(255, 255, 255)}[data-color=black]{background-color:#000}` |
| `--scrollbarWidth` | `0px` |
| `--ctaBarHeight` | `0px` |
| `--viewportWidth` | `calc(100vw - var(--scrollbarWidth))` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `` |
| `<nav>` | `mainNavigation` | `navigationMain__dropDown` |
| `<nav>` | `-` | `` |
| `<header>` | `-` | `mainHeader` |
| `<header>` | `-` | `homeHero__title` |
| `<header>` | `-` | `blockProjectsHighlight__header` |
| `<main>` | `swup` | `mainContent` |
| `<footer>` | `swupFooter` | `navigationFooter` |
