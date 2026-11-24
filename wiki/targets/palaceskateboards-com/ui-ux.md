---
title: "UI & UX Architecture: palaceskateboards-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: palaceskateboards-com

## Overview & Design Identity
- **Target**: `palaceskateboards-com` (**PALACE SKATEBOARDS**)
- **Production URL**: [https://palaceskateboards.com/](https://palaceskateboards.com/)
- **Final Redirected URL**: [https://eu.palaceskateboards.com/](https://eu.palaceskateboards.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×828px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#b47c57` accent)
- **Summary**: GULLY SH*T
- **Total Clean CSS Variables Extracted**: `81` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Neue Helvetica W01`
- **Body Font Stack**: `Neue Helvetica W01`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 24px`, `line-height: 24px`, `font-weight: 700`); CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`; rule `h1` (`font-size: 2.25rem`, `font-weight: 700`)
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 60px`, `--text-2xl--line-height: 60px`, `--text-3xl: 72px`; rule `h2` (`font-size: 1.5rem`, `font-weight: 700`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-base: 16px`, `--text-base--line-height: 16px`; rule `p` (`font-size: .875rem`, `line-height: 1.625`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-xs: 10px`, `--text-xs--line-height: 10px`, `--text-sm: 12px`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `browser-default` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffa500` | `.bg-orange { background-color: orange }` (`#ffa500`) |
| **Interactive Accent / Highlight** | `#b47c57` | live computed `button` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#b47c57` | live computed `button` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#808080` | `.border-grey-100 { border-color: #808080 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--container-lg` | `32rem` | Layout / Spatial Grid Token |
| `--container-2xl` | `42rem` | Layout / Spatial Grid Token |
| `--text-xs` | `10px` | Typography Ink Token |
| `--text-xs--line-height` | `10px` | Typography Ink Token |
| `--text-sm` | `12px` | Typography Ink Token |
| `--text-sm--line-height` | `12px` | Typography Ink Token |
| `--text-base` | `16px` | Typography Ink Token |
| `--text-base--line-height` | `16px` | Typography Ink Token |
| `--text-lg` | `32px` | Typography Ink Token |
| `--text-lg--line-height` | `32px` | Typography Ink Token |
| `--text-xl` | `45px` | Typography Ink Token |
| `--text-xl--line-height` | `45px` | Typography Ink Token |
| `--text-2xl` | `60px` | Typography Ink Token |
| `--text-2xl--line-height` | `60px` | Typography Ink Token |
| `--text-3xl` | `72px` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.pointer-events-none> — `palaceskateboards-com`)**:
   - Landmark `<header class="pointer-events-none left-0">` (`1440x80px`) hosting `PALACE SKATEBOARDS` navigation (`Web Shop · Shops · Advice`), DOM attributes (`data-application="hydrogen"`, `data-shop-id="26755399868"`, `data-storefront-id="2163011"`, `data-monorail-region="global"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<main.min-h-dvh> — `PALACE LIVING PROOFPALACE HOLIDAY `)**:
   - Landmark `<main class="min-h-dvh flex">` presenting display lead `PALACE LIVING PROOFPALACE HOLIDAY 2026 LOOKBOOKPA...` and copy excerpt *"© PALACE SKATEBOARDS LIMITED 2026"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<main.flex> — `PALACE HOLIDAY 2026 LOOKBOOK`)**:
   - Landmark `<main class="min-h-dvh flex">` rendering section `PALACE HOLIDAY 2026 LOOKBOOK` with copy *"PALACE HOLIDAY 2026 LOOKBOOK"*, asset references (`favicon.svg`, `neue-helvetica-w01-v2-Del-pFKJ.woff2`, `neue-helvetica-w01-CykExj90.woff2`, `cdn.shopify.com`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<main.flex-col> — `PALACE LONDON`)**:
   - Landmark `<main class="min-h-dvh flex">` framing `PALACE LONDON` and `PALACE LIVING PROOF` (*"PALACE LIVING PROOF"*) with `#ffa500` surface cards, `#b47c57` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.z-1> — `https://palaceskateboards.com/`)**:
   - Landmark `<footer class="z-1 pt-20">` anchoring `PALACE SKATEBOARDS` footer links (`Web Shop · Shops · Advice`), copy *"Delivery Information"*, and `#808080` structural dividers.
