---
title: "UI & UX Architecture: seedjewelry-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: seedjewelry-com

## Overview & Design Identity
- **Target**: `seedjewelry-com` (**Seed Jewelry · Lab-Grown Diamond High Jewelry, Dubai**)
- **Production URL**: [https://seedjewelry.com/](https://seedjewelry.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#1990c6` accent)
- **Summary**: Lab-grown diamond jewelry and transformable designs, crafted in the UAE. Explore Be Free, Kohana, Be True and Always Be, with a tree plan...
- **Total Clean CSS Variables Extracted**: `271` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Aire Pro`
- **Body Font Stack**: `Poppins`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 60px`, `line-height: 60px`, `font-weight: 400`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 77.23px`, `line-height: 94px`, `font-weight: 400`); rule `h2` (`font-size: 120%`, `font-weight: bold`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 26.4px`, `font-weight: 400`); CSS variables `--text-base: 1.0rem`, `--modal-body-padding-block: 1.25rem`, `--modal-body-padding-inline: 1.25rem`; rule `,body` (`line-height: 1.5rem`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 26.4px`, `font-weight: 400`); CSS variables `--heading-letter-spacing: 0.0em`, `--text-letter-spacing: 0.0em`, `--button-letter-spacing: 0.0em`; rule `.label` (`font-size: 14px`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f3f0eb` | `var(--seed-pdp-bg)` in `:root` |
| **Interactive Accent / Highlight** | `#1990c6` | `.shopify-payment-button__button... { background-color: #1990c6 }` |
| **Secondary / Muted Copy** | `#808080` | live computed `hr` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#e3e0d8` | `var(--seed-pdp-border)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--container-max-width` | `100%` | Layout / Spatial Grid Token |
| `--container-xxs-max-width` | `27.5rem` | Layout / Spatial Grid Token |
| `--container-xs-max-width` | `42.5rem` | Layout / Spatial Grid Token |
| `--container-sm-max-width` | `61.25rem` | Layout / Spatial Grid Token |
| `--container-md-max-width` | `71.875rem` | Layout / Spatial Grid Token |
| `--container-lg-max-width` | `90rem` | Layout / Spatial Grid Token |
| `--container-xl-max-width` | `1920px` | Layout / Spatial Grid Token |
| `--container-gutter` | `1.25rem` | Layout / Spatial Grid Token |
| `--section-vertical-spacing` | `2.5rem` | Layout / Spatial Grid Token |
| `--section-vertical-spacing-tight` | `2.5rem` | Layout / Spatial Grid Token |
| `--section-stack-gap` | `2.25rem` | Layout / Spatial Grid Token |
| `--section-stack-gap-tight` | `2.25rem` | Layout / Spatial Grid Token |
| `--form-gap` | `1.25rem` | Layout / Spatial Grid Token |
| `--fieldset-gap` | `1rem` | Layout / Spatial Grid Token |
| `--form-control-gap` | `0.625rem` | Layout / Spatial Grid Token |
| `--checkbox-control-gap` | `0.75rem` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.analytics> — `seedjewelry-com`)**:
   - Landmark `<header class="analytics">` (`1440x91px`) hosting `Seed Jewelry · Lab-Grown Diamond Hig` navigation (`Search Search`), DOM attributes (`data-source-attribution="shopify.exit_intersti..."`, `data-source-attribution="shopify.loadfeatures"`, `data-source-attribution="shopify.dynamic_check..."`, `data-source-attribution="shopify.dynamic_check..."`), and stylesheet rule `.page-width { max-width:var(--container-xl-max-width);margin:0 auto;padding:0 25px }`.
2. **Hero Stage & Focal Lead (<section.shopify-section> — `Born from the earth, refined by ar`)**:
   - Landmark `<section class="shopify-section seed-hero-section">` presenting display lead `Born from the earth, refined by art` and copy excerpt *"Celebrating our launch: 20% off every piece until 30 November."* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.seed-hero> — `Best Sellers`)**:
   - Landmark `<section class="seed-hero">` rendering section `Best Sellers` with copy *"Lab-grown diamonds, transformable designs, and sustainable luxury"*, asset references (`2113812439524310`, `fbevents.js`, `clarity.js`, `zcz4nln3tx`), and grid rule `.page-width-lg { max-width:var(--container-lg-max-width);margin:0 auto;padding:0 25px }`.
4. **Interactive Detail & Feature Matrix (<section.seed-product-grid-section> — `Kohana Ring , Big Size, Reverse`)**:
   - Landmark `<section class="shopify-section seed-product-grid-section">` framing `Kohana Ring , Big Size, Reverse` and `Always Be Round Cut Earrings with Removable Halo` (*"Kohana Ring , Big Size, Reverse 18K (750) White Gold · 1 total ca"*) with `#f3f0eb` surface cards, `#1990c6` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.color-scheme--scheme-1> — `https://seedjewelry.com/`)**:
   - Landmark `<footer class="color-scheme--scheme-1">` anchoring `Seed Jewelry · Lab-Grown Diamond` footer links (`Search Search`), copy *"18K (750) White Gold · 1 total carat weight ·..."*, and `#e3e0d8` structural dividers.
