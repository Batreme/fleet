---
title: "UI & UX Architecture: www-photiu-ai"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-photiu-ai

## Overview & Design Identity
- **Target**: `www-photiu-ai` (**Remove Background, Upscale & Erase Objects – Photiu.ai**)
- **Production URL**: [https://www.photiu.ai](https://www.photiu.ai)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×1744px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#9ca3af` accent)
- **Summary**: Discover Photiu.ai's AI tools: remove backgrounds, upscale images, and erase unwanted objects. Achieve stunning photo edits online quickl...
- **Total Clean CSS Variables Extracted**: `14` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Segoe UI`
- **Body Font Stack**: `Segoe UI`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 48px`, `line-height: 48px`, `font-weight: 700`); rule `h1` (`font-size: 2.25rem`, `line-height: 2.5rem`, `font-weight: 700`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 36px`, `line-height: 42px`, `font-weight: 700`); rule `h2` (`font-size: 1.875rem`, `line-height: 2.25rem`, `font-weight: 700`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 600`); rule `p` (`line-height: 1.625`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 600`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `browser-default` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#eeeeff` | `.homebg { background: #eeeeff }` |
| **Interactive Accent / Highlight** | `#9ca3af` | `textarea::-moz-placeholder { color: #9ca3af }` |
| **Secondary / Muted Copy** | `#626262` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#c9c9fc` | `30 { border-color: #c9c9fc }` |
| **Variable Token (`--board-black-color`)** | `#f8f9f9` | `var(--board-black-color)` in `:root` |
| **Variable Token (`--termly-theme-button-background-color`)** | `#003afa` | `var(--termly-theme-button-background-color)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--container-width` | `1200px` | Layout / Spatial Grid Token |
| `--header-h` | `80px` | Layout / Spatial Grid Token |
| `--header-h-sm` | `60px` | Layout / Spatial Grid Token |
| `--footer-h` | `200px` | Dimension / Scale Token |
| `--board-black-color` | `#f8f9f9` | Canvas / Surface Token |
| `--board-white-color` | `transparent` | Canvas / Surface Token |
| `--termly-prompt-padding` | `2.5em` | Layout / Spatial Grid Token |
| `--termly-theme-background-color` | `#ffffff` | Canvas / Surface Token |
| `--termly-theme-button-background-color` | `var(--termly-override-button-background-color, #003afa)` | Canvas / Surface Token |
| `--termly-theme-button-text-color` | `var(--termly-override-button-text-color, #ffffff)` | Typography Ink Token |
| `--termly-theme-color` | `#000000` | Brand / Palette Token |
| `--termly-theme-font-family` | `Roboto, "Open Sans", Arial, Helvetica` | Brand / Palette Token |
| `--termly-theme-font-size` | `12px` | Brand / Palette Token |
| `--termly-z-index` | `var(--termly-override-z-index, 999999)` | Elevation / Border Token |
| `--www-photiu-ai-bg` | `#ffffff` | Canvas Substrate (from live computed `browser-default` `background-color` (`computed_styles.json`)) |
| `--www-photiu-ai-ink` | `#000000` | Primary Typography Ink (computed-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.flex-1> — `www-photiu-ai`)**:
   - Landmark `<nav class="flex-1 hidden">` (`1024x36px`) hosting `Remove Background, Upscale & Erase O` navigation (`AI Photo Editor · Image Generator · Image Upscale · Remove Background · Magic Eraser`), DOM attributes (`data-categories="essential"`, `data-has-derived-categories="1"`, `data-precedence="next"`, `data-termly-part="consent-banner"`), and stylesheet rule `before { box-sizing:border-box;border:0 solid e5e7eb }`.
2. **Hero Stage & Focal Lead (<section.w-full> — `Remove background`)**:
   - Landmark `<section class="w-full">` presenting display lead `Remove background` and copy excerpt *"Photiu.ai's advanced AI technology ensures precise background rem"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.w-full:nth(2)> — `Remove backgrounds instantly with `)**:
   - Landmark `<section class="w-full">` rendering section `Remove backgrounds instantly with just one click!` with copy *"AI Photo Editor Image Generator Image Upscale Remove Background M"*, asset references (`gtm.js`, `eTI4g9fAtUixpHto8YooHCfeUPdUHEz0P...`, `3b524ee0-b2d0-46e4-acf0-3df4c2d8edb5`, `www.googletagmanager.com`), and grid rule `body { margin:0;line-height:inherit }`.
4. **Interactive Detail & Feature Matrix (<section.w-full:nth(3)> — `HD Background Removal`)**:
   - Landmark `<section class="w-full">` framing `HD Background Removal` and `Erase Freely, Cut Perfectly` (*"Resize images to ideal dimensions"*) with `#eeeeff` surface cards, `#9ca3af` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.flex> — `https://www.photiu.ai`)**:
   - Landmark `<footer class="flex w-full">` anchoring `Remove Background, Upscale & Era` footer links (`AI Photo Editor · Image Generator · Image Upscale · Remove Background · Magic Eraser`), copy *"Make your images smaller"*, and `#c9c9fc` structural dividers.
