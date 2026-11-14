---
title: "UI & Design System: www-iamsunnywang-com"
date: 2026-11-14
target: "[[overview|www-iamsunnywang-com]]"
---

# UI Architecture & Design Tokens: www-iamsunnywang-com

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--title-font` | `"Quicksand",var(--body-font)` |
| `--body-font` | `"Source Sans 3",ui-sans-serif,system-ui,-apple-system,BlinkM` |
| `--kicker-font` | `"IBM Plex Mono",ui-monospace,SFMono-Regular,Menlo,Monaco,Con` |
| `--text-highlight-color` | `#62d6dc` |
| `--google-text-highlight-color` | `#62d6dc` |
| `--text-highlight-color` | `var(--google-text-highlight-color)` |
| `--airbnb-section-kicker-size-value` | `1.4` |
| `--airbnb-section-title-size-value` | `4.9` |
| `--airbnb-section-body-size-value` | `1.9` |
| `--portfolio-rail` | `clamp(40px, 5vw, 62px)` |
| `--portfolio-offset` | `clamp(106px, 12vw, 154px)` |
| `--portfolio-dot-top` | `50%` |
| `--portfolio-hover-image-scale` | `1.24` |
| `--portfolio-hover-image-scale` | `1.13` |
| `--portfolio-hover-image-scale` | `1.12` |
| `--portfolio-hover-image-scale` | `1.11` |
| `--poster-slider-height` | `clamp(320px, 36cqw, 520px)` |
| `--poster-slider-peek` | `clamp(24px, 3.2cqw, 46px)` |
| `--poster-slider-fade-width` | `clamp(56px, 6cqw, 96px)` |
| `--airbnb-section-body-size-value` | `2.05` |
| `--poster-slider-height` | `clamp(430px, calc(100vh - var(--image-stack-panel-top) - 250` |
| `--poster-slider-peek` | `clamp(34px, 5vw, 76px)` |
| `--poster-slider-fade-width` | `clamp(82px, 8.6vw, 136px)` |
| `--portfolio-lightbox-top` | `clamp(64px, 8vh, 96px)` |
| `--portfolio-phone-width` | `clamp(150px, 17vw, 220px)` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `journey-actions` |
| `<nav>` | `-` | `journey-route` |
| `<nav>` | `-` | `reflection-nav` |
| `<nav>` | `skillInventoryFilters` | `skill-inventory-filters` |
| `<header>` | `-` | `journey-header` |
| `<aside>` | `journeyOnboardingToast` | `journey-onboarding-toast is-visible` |
| `<aside>` | `-` | `ask-sunny-machine` |
| `<main>` | `top` | `` |
