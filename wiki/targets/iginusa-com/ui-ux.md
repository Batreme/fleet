---
title: "UI & Design System: iginusa-com"
date: 2026-11-14
target: "[[overview|iginusa-com]]"
---

# UI Architecture & Design Tokens: iginusa-com

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--alpha-button-background` | `1` |
| `--alpha-button-border` | `1` |
| `--alpha-link` | `.85` |
| `--alpha-badge-border` | `.1` |
| `--focused-base-outline` | `.2rem solid rgba(var(--color-foreground), .5)` |
| `--focused-base-outline-offset` | `.3rem` |
| `--focused-base-box-shadow` | `0 0 0 .3rem rgb(var(--color-background)), 0 0 .5rem .4rem rg` |
| `--border-width` | `var(--product-card-border-width)` |
| `--border-opacity` | `var(--product-card-border-opacity)` |
| `--shadow-horizontal-offset` | `var(--product-card-shadow-horizontal-offset)` |
| `--shadow-vertical-offset` | `var(--product-card-shadow-vertical-offset)` |
| `--shadow-blur-radius` | `var(--product-card-shadow-blur-radius)` |
| `--shadow-opacity` | `var(--product-card-shadow-opacity)` |
| `--shadow-visible` | `var(--product-card-shadow-visible)` |
| `--image-padding` | `var(--product-card-image-padding)` |
| `--text-alignment` | `var(--product-card-text-alignment)}.collection-card-wrapper ` |
| `--border-width` | `var(--collection-card-border-width)` |
| `--border-opacity` | `var(--collection-card-border-opacity)` |
| `--shadow-horizontal-offset` | `var(--collection-card-shadow-horizontal-offset)` |
| `--shadow-vertical-offset` | `var(--collection-card-shadow-vertical-offset)` |
| `--shadow-blur-radius` | `var(--collection-card-shadow-blur-radius)` |
| `--shadow-opacity` | `var(--collection-card-shadow-opacity)` |
| `--shadow-visible` | `var(--collection-card-shadow-visible)` |
| `--image-padding` | `var(--collection-card-image-padding)` |
| `--text-alignment` | `var(--collection-card-text-alignment)}.article-card-wrapper ` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `hdr__nav` |
| `<header>` | `-` | `igin-rv hdr` |
| `<aside>` | `-` | `igCD` |
| `<main>` | `MainContent` | `content-for-layout igin-page-content focus-none` |
| `<footer>` | `-` | `igin-rv ftr` |
