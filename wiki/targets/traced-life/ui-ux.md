---
title: "UI & UX Architecture: traced-life"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: traced-life

## Overview & Design Identity
- **Target**: `traced-life` (**At-Home Environmental Exposure Test · Traced**)
- **Production URL**: [https://traced.life/](https://traced.life/)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#615e50` canvas, `#ffffff` ink, `#1990c6` accent)
- **Summary**: Trace 15 environmental elements from one strand of hair. A personal 30-day timeline, percentile rankings against a global database, and g...
- **Total Clean CSS Variables Extracted**: `232` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Serrif`
- **Body Font Stack**: `Saans`
- **Monospace / Technical Font Stack**: `Saans Semi Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 48px`, `line-height: 48px`, `font-weight: 400`); rule `h1` (`font-size: 2.5rem`, `line-height: 100%`)
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`; rule `h2` (`font-size: 1.5rem`, `line-height: 110%`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`, `--oke-bodyText-fontWeight: 400`; rule `p` (`font-size: 1rem`, `line-height: 120%`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--oke-text-small: 12px`, `--font-mono: "Saans Semi Mono",monospace`, `--default-mono-font-family: var(--font-mono)`; rule `small` (`font-size: calc(var(--kl-reviews-reviews...`, `font-weight: var(--kl-revi...`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#615e50` | live computed `section` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `a` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#000000` | live computed `a` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#1990c6` | `.shopify-payment-button__button... { background-color: #1990c6 }` |
| **Secondary / Muted Copy** | `#bdbdbd` | `var(--foreground-disabled)` in `:root` |
| **Structural Hairline Border** | `#e5e5eb` | `var(--oke-border-color)` in `:root` |
| **Variable Token (`--oke-button-backgroundColor`)** | `#f7f7f8` | `var(--oke-button-backgroundColor)` in `:root` |
| **Variable Token (`--oke-button-backgroundColorHover`)** | `#f4f4f6` | `var(--oke-button-backgroundColorHover)` in `:root` |
| **Variable Token (`--oke-button-backgroundColorActive`)** | `#676986` | `var(--oke-button-backgroundColorActive)` in `:root` |
| **Variable Token (`--oke-button-textColor`)** | `#272d45` | `var(--oke-button-textColor)` in `:root` |
| **Variable Token (`--oke-button-borderColor`)** | `#dbdde4` | `var(--oke-button-borderColor)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--oke-widget-spaceAbove` | `20px` | Layout / Spatial Grid Token |
| `--oke-widget-spaceBelow` | `20px` | Layout / Spatial Grid Token |
| `--oke-starRating-spaceAbove` | `0` | Layout / Spatial Grid Token |
| `--oke-starRating-spaceBelow` | `0` | Layout / Spatial Grid Token |
| `--oke-button-backgroundColor` | `#f7f7f8` | Canvas / Surface Token |
| `--oke-button-backgroundColorHover` | `#f4f4f6` | Canvas / Surface Token |
| `--oke-button-backgroundColorActive` | `#676986` | Canvas / Surface Token |
| `--oke-button-textColor` | `#272d45` | Typography Ink Token |
| `--oke-button-textColorHover` | `#272d45` | Typography Ink Token |
| `--oke-button-textColorActive` | `#fff` | Typography Ink Token |
| `--oke-button-borderColor` | `#dbdde4` | Brand / Palette Token |
| `--oke-button-borderColorHover` | `#dbdde4` | Brand / Palette Token |
| `--oke-button-borderColorActive` | `#676986` | Brand / Palette Token |
| `--oke-button-borderRadius` | `4px` | Elevation / Border Token |
| `--oke-button-borderWidth` | `1px` | Layout / Spatial Grid Token |
| `--oke-button-fontWeight` | `700` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.contents> — `traced-life`)**:
   - Landmark `<header class="contents">` (`1440px`) hosting `At-Home Environmental Exposure Test ` navigation (`Shop · What we test · Report · Science · Our story`), DOM attributes (`data-source-attribution="shopify.exit_intersti..."`, `data-shop-id="70566805578"`, `data-venmo-supported="false"`, `data-environment="production"`), and stylesheet rule `before { border:0 solid;box-sizing:border-box;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.text-light-50> — `Time leaves traces. Now you can re`)**:
   - Landmark `<section class="text-light-50 bg-background-4">` presenting display lead `Time leaves traces. Now you can read them.` and copy excerpt *"At-home hair analysis test"* over `#615e50` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.text-dark-secondary> — `The difference`)**:
   - Landmark `<section class="text-dark-secondary w-full">` rendering section `The difference` with copy *"Nickel contaminants"*, asset references (`awin-shopify-integration-code.js`, `loader.js`, `sealsubscriptions.js`, `990232790301153`), and grid rule `webkit-file-upload-button { border:0 solid;box-sizing:border-box;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.bg-light> — `How It Works`)**:
   - Landmark `<section class="text-dark-secondary bg-light">` framing `How It Works` and `our expertise` (*"15 environmental elements"*) with `#000000` surface cards, `#1990c6` accents, and `file-selector-button { border:0 solid;box-sizing:border-box;margin:0;padding:0 }`.
5. **Colophon & Global Directory Footer (<footer.contents> — `https://traced.life/`)**:
   - Landmark `<footer class="contents">` anchoring `At-Home Environmental Exposure T` footer links (`Shop · What we test · Report · Science · Our story`), copy *"30-day exposure timeline"*, and `#e5e5eb` structural dividers.
