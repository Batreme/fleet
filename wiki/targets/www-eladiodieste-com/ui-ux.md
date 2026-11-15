---
title: "UI & Design System: www-eladiodieste-com"
date: 2026-11-15
target: "www-eladiodieste-com"
---

# UI Architecture & Design Tokens: www-eladiodieste-com

> Ground-truth CSS custom properties and DOM layout primitives extracted from `www-eladiodieste-com` (`Eladio Dieste · La Intersección de Ingeniería con Arquitectura (1917–2000)`). All values are sanitized, deduplicated, and mapped to their semantic UI roles. Also see [UI Prompt Blueprint](prompt-blueprint.md).

## 🎨 Design Tokens (CSS Variables)

| Token Name | Extracted Value | Semantic UI Role |
|---|---|---|
| `--background` | `#eadfd2` | Primary warm mortar sand canvas substrate |
| `--foreground` | `#a55f2d` | Primary kiln-fired terracotta brick ink & border token |
| `--off-white` | `#f1ece8` | Secondary light archival card surface |
| `--color-accent` | `var(--foreground)` | Accent color mapped directly to terracotta `#a55f2d` |
| `--color-black` | `#000` | Black reference token |
| `--color-white` | `#fff` | White reference token |
| `--ease-out-expo` | `cubic-bezier(.19,1,.22,1)` | Primary 1.4s–1.6s character & divider reveal curve |
| `--ease-magic` | `cubic-bezier(.33,0,0,1)` | Active navigation indicator morph curve |
| `--ease-quart` | `cubic-bezier(.41,.35,.2,1)` | Scroll parallax & image reveal curve |
| `--ease-out` | `cubic-bezier(0,0,.2,1)` | Standard UI ease-out curve |
| `--default-transition-duration` | `.15s` | Base micro-interaction duration |
| `--default-transition-timing-function` | `cubic-bezier(.4,0,.2,1)` | Base timing curve |
| `--split-mask-pad` | `.08em` | Horizontal padding on split-text reveal masks |
| `--split-mask-bleed-y` | `.3em` | Vertical descender bleed allowance on text masks |
| `--container-xl` | `36rem` | 576px scholarly reading measure |
| `--tracking-tight` | `-.025em` | Display headline letter-spacing |
| `--text-5xl` | `3rem` | 48px chapter heading size (`line-height: 1`) |
| `--text-6xl` | `3.75rem` | 60px monument heading size (`line-height: 1`) |
| `--text-7xl` | `4.5rem` | 72px hero display size (`line-height: 1`) |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `flex items-center justify-between font-medium pointer-events` |
| `<nav>` | `-` | `-` |
| `<main>` | `-` | `-` |
| `<section>` | `-` | `text-background invisible relative h-[250lvh]` |
| `<section>` | `-` | `px-global pt-6` |
| `<section>` | `-` | `px-global gap-5 pt-45` |
| `<section>` | `work` | `px-global` |
| `<section>` | `vida` | `px-global pt-6 pb-40 md:pb-72` |
| `<section>` | `carrera` | `px-global` |
| `<section>` | `-` | `px-global pb-6` |
| `<footer>` | `-` | `h-dvh overflow-hidden md:h-screen` |
