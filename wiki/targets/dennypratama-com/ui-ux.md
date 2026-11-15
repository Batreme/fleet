---
title: "UI & Design System: dennypratama-com"
date: 2026-11-15
target: "dennypratama-com"
---

# UI Architecture & Design Tokens: dennypratama-com

> Ground-truth CSS custom properties and DOM layout primitives extracted from `dennypratama-com` (`Denny Pratama · Product Designer & Design Engineer Portfolio`). All values are sanitized, deduplicated, and mapped to their semantic UI roles. Also see [UI Prompt Blueprint](prompt-blueprint.md).

## 🎨 Design Tokens (CSS Variables)

| Token Name | Extracted Value | Semantic UI Role |
|---|---|---|
| `--font-archivo` | `"Archivo", "Archivo Fallback"` | Primary display & UI sans font family |
| `--sans` | `var(--font-archivo),"Archivo","Helvetica Neue",Helvetica,Arial,sans-serif` | Global sans-serif stack |
| `--ink` | `#0c0c0b` | Primary carbon substrate |
| `--ink-2` | `#151514` | Secondary elevated card surface |
| `--ink-3` | `#1f1f1d` | Interactive hover/chip surface |
| `--bone` | `#eceae4` | Primary limestone bone ink & light section bg |
| `--bone-2` | `#c9c6be` | Secondary body copy ink |
| `--mute` | `#8c8a84` | Muted index & metadata ink |
| `--line` | `#eceae424` | 1px hairline divider on dark substrate |
| `--line-2` | `#eceae447` | Hovered hairline border on dark substrate |
| `--lp` | `#0c0c0b24` | 1px hairline divider on `.on-bone` sections |
| `--red` | `#ff4f2b` | Signal orange-red accent token |
| `--ok` | `#3ccf7d` | Live availability status indicator |
| `--e-out` | `cubic-bezier(.16,1,.3,1)` | Primary mechanical ease-out curve |
| `--e-io` | `cubic-bezier(.83,0,.17,1)` | Symmetric ease-in-out curtain curve |
| `--wrap` | `1680px` | Maximum layout container width |
| `--pad` | `48px` | Desktop horizontal container padding |
| `--r-s` | `4px` | Small component border radius |
| `--r-m` | `8px` | Medium card border radius |
| `--r-full` | `999px` | Pill badge border radius |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<header>` | `-` | `nav` |
| `<nav>` | `-` | `nav-links` |
| `<nav>` | `-` | `menu-l` |
| `<nav>` | `-` | `ct-col` |
| `<main>` | `-` | `-` |
| `<section>` | `-` | `hero` |
| `<section>` | `work` | `work on-bone` |
| `<section>` | `-` | `con` |
| `<section>` | `both` | `both` |
| `<section>` | `-` | `proof on-bone` |
| `<footer>` | `contact` | `ct` |
