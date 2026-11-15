---
title: "UI & Design System: www-avilus-com"
date: 2026-11-15
target: "[[overview|www-avilus-com]]"
---

# UI Architecture & Design Tokens: www-avilus-com

> Ground-truth CSS custom properties and DOM layout primitives extracted from `www-avilus-com` (`Avilus · Dual-Use Uncrewed Aircraft for Evacuation, Logistics and Surveillance`). All values are sanitized, deduplicated, and mapped to their semantic UI roles. Also see [[prompt-blueprint|UI Prompt Blueprint]].

## 🎨 Design Tokens (CSS Variables)

| Token Name | Extracted Value | Semantic UI Role |
|---|---|---|
| `--swatch--light-200` | `#f7f7f7` | Primary technical light gray canvas (`--_theme---background`) |
| `--swatch--light-100` | `white` | Secondary elevated surface (`--_theme---background-2`) |
| `--swatch--dark-900` | `#183032` | Primary deep petrol-teal ink & border color (`--_theme---text`) |
| `--swatch--dark-800` | `#2f2b2d` | Dark tactical section surface |
| `--swatch--brand-500` | `#ddff2c` | High-visibility aviation chartreuse accent (`--_theme---button-primary--background`) |
| `--_theme---error` | `#b3261e` | Medical evacuation rescue red indicator |
| `--_typography---font--primary-family` | `Inter,Verdana,sans-serif` | Primary structural UI & heading sans stack |
| `--_typography---font--secondary-family` | `Robotomono,Impact,sans-serif` | Technical monospace callout & spec font stack |
| `--_typography---letter-spacing--tight` | `-.03em` | Tight display headline tracking |
| `--site--column-count` | `12` | Master 12-column layout grid count |
| `--site--viewport-max` | `90` | Max container width in rem (90rem = 1440px) |
| `--max-width--small` | `50rem` | Narrative & spec block max-width (800px) |
| `--bar-height` | `3.125rem` | Fixed navigation bar height (50px) |
| `--closed-width` | `min(90vw, 27.375rem)` | Compact floating navbar width (438px) |
| `--nav--menu-open-duration` | `400ms` | Navigation drawer open duration |
| `--border-width--main` | `.125rem` | 2px structural engineering border width |
| `--radius--main` | `.5rem` | 8px primary component border radius |
| `--button-size--medium` | `2.5rem` | Standard 40px tactical button height |
| `--button-size--large` | `5rem` | Large 80px primary mission CTA height |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<header>` | `-` | `nav_desktop_wrap` |
| `<nav>` | `-` | `nav_links_component w-variant-23049969-09ac-2789-520b-3c6ae8` |
| `<nav>` | `w-dropdown-list-0` | `dropdown_list w-variant-23049969-09ac-2789-520b-3c6ae895bbc6` |
| `<nav>` | `-` | `nav_links_component` |
| `<nav>` | `w-dropdown-list-1` | `dropdown_list w-dropdown-list` |
| `<main>` | `main` | `page_main` |
| `<section>` | `-` | `u-section u-min-height-screen u-padding-bottom-sitemargin u-` |
| `<section>` | `-` | `u-section u-padding-top-small u-padding-bottom-small u-radiu` |
| `<section>` | `-` | `u-section u-padding-top-small u-padding-bottom-small u-backg` |
| `<section>` | `-` | `u-section u-padding-top-small u-padding-bottom-small` |
| `<footer>` | `-` | `footer_inner` |
