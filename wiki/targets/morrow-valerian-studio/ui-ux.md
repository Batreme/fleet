---
title: "UI & Design System: morrow-valerian-studio"
date: 2026-11-15
target: "morrow-valerian-studio"
---

# UI Architecture & Design Tokens: morrow-valerian-studio

> Ground-truth CSS custom properties and DOM layout primitives extracted from `morrow-valerian-studio` (`MORROW (by Valerian Studio) · High-Craft Editorial Knitwear & Fashion Flagship`). All values are sanitized, deduplicated, and mapped to their semantic UI roles. Also see [UI Prompt Blueprint](prompt-blueprint.md).

## 🎨 Design Tokens (CSS Variables)

| Token Name | Extracted Value | Semantic UI Role |
|---|---|---|
| `--font-pp-neue-montreal` | `"ppNeueMontreal", "ppNeueMontreal Fallback"` | Primary Neo-Grotesque UI & grid sans font |
| `--font-editorial-new` | `"editorialNew", "editorialNew Fallback"` | High-contrast editorial display serif font |
| `--font-sans` | `var(--font-pp-neue-montreal), Arial, sans-serif` | Default sans-serif font stack |
| `--color-white` | `#fff` | Primary canvas background |
| `--color-black` | `#000` | Pure black contrast token |
| `--color-neutral-50` | `#fafafa` | Porcelain soft background surface |
| `--color-neutral-100` | `#f5f5f5` | Product card backdrop surface |
| `--color-neutral-200` | `#e5e5e5` | 1px hairline border token |
| `--color-neutral-300` | `#d4d4d4` | Hover border divider token |
| `--color-neutral-400` | `#a1a1a1` | Muted index & size label ink |
| `--color-neutral-500` | `#737373` | Secondary editorial body ink |
| `--color-neutral-600` | `#525252` | Sub-heading ink |
| `--color-neutral-900` | `#171717` | Primary heading & garment title ink |
| `--color-red-800` | `#9f0712` | Deep crimson seasonal accent |
| `--color-rose-500` | `#ff2357` | Vibrant rose campaign highlight |
| `--spacing` | `.25rem` | Base 4px spatial unit |
| `--container-xs` | `20rem` | Mini cart / drawer container width (320px) |
| `--container-3xl` | `48rem` | Editorial narrative column max-width (768px) |
| `--text-xs` | `.75rem` | 12px micro-label size (`line-height: calc(1 / .75)`) |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<header>` | `-` | `site-nav col-start-1 row-start-1` |
| `<header>` | `-` | `cart-header` |
| `<nav>` | `-` | `site-nav-toolbar grid grid-cols-[1fr_auto_1fr] items-center ` |
| `<nav>` | `-` | `site-mobile-menu-content px-page` |
| `<nav>` | `-` | `col-span-4 min-w-0 self-start lg:row-start-1 lg:col-span-2 l` |
| `<nav>` | `-` | `col-span-12 lg:col-span-10` |
| `<main>` | `-` | `relative z-10 bg-white` |
| `<section>` | `-` | `relative grid h-svh grid-cols-12 gap-x-gutter overflow-hidde` |
| `<section>` | `-` | `grid grid-cols-12 gap-x-gutter px-page py-section font-sans ` |
| `<section>` | `-` | `grid grid-cols-12 pb-section lg:pb-section-lg` |
| `<section>` | `-` | `grid grid-cols-12 gap-x-gutter px-page pb-24 font-sans lg:px` |
| `<section>` | `-` | `grid grid-cols-12 gap-x-gutter px-page font-sans lg:px-page-` |
| `<section>` | `-` | `mt-section w-full lg:mt-section-lg` |
| `<footer>` | `-` | `relative z-0 flex min-h-[40svh] flex-col px-page font-sans t` |
