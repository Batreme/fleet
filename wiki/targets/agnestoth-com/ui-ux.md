---
title: "UI & Design System: agnestoth-com"
date: 2026-11-15
target: "[[overview|agnestoth-com]]"
---

# UI Architecture & Design Tokens: agnestoth-com

> Ground-truth CSS custom properties and DOM layout primitives extracted from `agnestoth-com` (`AGNESTOTH · House of Luxurious Embroidery`). All values are sanitized, deduplicated, and mapped to their semantic UI roles. Also see [[prompt-blueprint|UI Prompt Blueprint]].

## 🎨 Design Tokens (CSS Variables)

| Token Name | Extracted Value | Semantic UI Role |
|---|---|---|
| `--color-background` | `255,255,255` | Primary pure white canvas RGB triplet |
| `--gradient-background` | `#FFFFFF` | Root background hex surface |
| `--color-foreground` | `18,18,18` | Primary charcoal ink RGB triplet (#121212) |
| `--color-background-contrast` | `191,191,191` | Contrast border & divider RGB triplet (#bfbfbf) |
| `--color-shadow` | `18,18,18` | Elevation shadow base RGB triplet |
| `--color-button` | `18,18,18` | Primary couture CTA button fill |
| `--color-button-text` | `255,255,255` | Primary CTA button text color |
| `--color-secondary-button` | `255,255,255` | Secondary outline button surface |
| `--color-secondary-button-text` | `18,18,18` | Secondary outline button ink |
| `--color-link` | `18,18,18` | Editorial anchor link color |
| `--color-badge-foreground` | `18,18,18` | Collection badge label ink |
| `--color-badge-background` | `255,255,255` | Collection badge background |
| `--color-badge-border` | `18,18,18` | 1px collection badge border |
| `--font-body-family` | `Assistant, sans-serif` | Base body font family variable |
| `--font-heading-family` | `Assistant, sans-serif` | Base heading fallback variable (overridden by FreightBig Pro / Jost) |
| `--font-body-weight` | `400` | Regular body weight |
| `--font-body-weight-bold` | `700` | Bold emphasis weight |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<header>` | `shopify-section-sections--32190997266770__agnes-header` | `shopify-section shopify-section-group-header-group agnes-hea` |
| `<header>` | `-` | `agnes-collection__head` |
| `<header>` | `-` | `agnes-worlds__head` |
| `<header>` | `-` | `agnes-instagram__head` |
| `<header>` | `-` | `agnes-logos__head` |
| `<nav>` | `-` | `agnes-header__nav` |
| `<nav>` | `-` | `agnes-header__drawer-inner` |
| `<nav>` | `-` | `agnes-footer__columns` |
| `<main>` | `MainContent` | `content-for-layout focus-none` |
| `<section>` | `shopify-pc__banner` | `shopify-pc__banner__dialog` |
| `<section>` | `shopify-section-template--32190997561682__hero` | `shopify-section agnes-section agnes-section--hero` |
| `<section>` | `-` | `agnes-hero color-scheme-1` |
| `<section>` | `shopify-section-template--32190997561682__statement` | `shopify-section agnes-section agnes-section--statement` |
| `<section>` | `-` | `agnes-statement agnes-statement--size-large color-scheme-1 g` |
