---
title: "UI & UX Architecture: aryabhangybuilders-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: aryabhangybuilders-com

## Overview & Design Identity
- **Target**: `aryabhangybuilders-com` (**Premium Builders In Kochi · Flats & Apartments · Arya Bhangy**)
- **Production URL**: [https://aryabhangybuilders.com/](https://aryabhangybuilders.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f7f8f9` canvas, `#222222` ink, `#375efb` accent)
- **Summary**: RERA-registered 2.5, 3 & 4 BHK apartments in Vyttila and Kumbalam, Kochi, from a family group building since 1969. Book a site visit.
- **Total Clean CSS Variables Extracted**: `171` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `CS Alpha`
- **Body Font Stack**: `Segoe UI`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 40px`, `line-height: 46px`, `font-weight: 400`, `letter-spacing: -0.6px`); CSS variables `--page-title-display: block`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 40px`, `line-height: 46px`, `font-weight: 400`, `letter-spacing: -0.6px`); rule `h2` (`font-size: 36px`)
- **Body Copy**: live computed `body` (`font-size: 17px`, `line-height: 25.5px`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 17px`, `line-height: 25.5px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f7f8f9` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#222222` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#5bc0de` | `nt.elementor-button-info .eleme... { background-color: #5bc0de }` |
| **Interactive Accent / Highlight** | `#375efb` | `.elementor .e-button-base { background-color: #375efb }` |
| **Secondary / Muted Copy** | `#7a7a7a` | `var(--e-global-color-text)` in `:root` |
| **Structural Hairline Border** | `#69727d` | `entor-field-group .elementor-fi... { border: #69727d }` |
| **Variable Token (`--contrast-2`)** | `#575760` | `var(--contrast-2)` in `:root` |
| **Variable Token (`--contrast-3`)** | `#b2b2be` | `var(--contrast-3)` in `:root` |
| **Variable Token (`--base`)** | `#f0f0f0` | `var(--base)` in `:root` |
| **Variable Token (`--base-3`)** | `#ffffff` | `var(--base-3)` in `:root` |
| **Variable Token (`--accent`)** | `#1e73be` | `var(--accent)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--contrast` | `#222222` | Color / Atmospheric Token |
| `--contrast-2` | `#575760` | Color / Atmospheric Token |
| `--contrast-3` | `#b2b2be` | Color / Atmospheric Token |
| `--base` | `#f0f0f0` | Color / Atmospheric Token |
| `--base-2` | `#f7f8f9` | Color / Atmospheric Token |
| `--base-3` | `#ffffff` | Color / Atmospheric Token |
| `--accent` | `#1e73be` | Brand / Palette Token |
| `--gp-search-modal-bg-color` | `var(--base-3)` | Canvas / Surface Token |
| `--gp-search-modal-text-color` | `var(--contrast)` | Typography Ink Token |
| `--gp-search-modal-overlay-bg-color` | `rgba(0,0,0,0.2)` | Canvas / Surface Token |
| `--e-global-color-v4-white` | `var(--white)` | Canvas / Surface Token |
| `--e-global-color-v4-black` | `var(--black)` | Canvas / Surface Token |
| `--e-global-color-v4-cream-50` | `var(--cream-50)` | Brand / Palette Token |
| `--e-global-color-v4-cream-100` | `var(--cream-100)` | Brand / Palette Token |
| `--e-global-color-v4-cream-150` | `var(--cream-150)` | Brand / Palette Token |
| `--e-global-color-v4-cream-200` | `var(--cream-200)` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.elementor> — `aryabhangybuilders-com`)**:
   - Landmark `<header class="elementor elementor-5070">` (`1440x0px`) hosting `Premium Builders In Kochi · Flats & ` navigation (`Home · Residential · Commercial · Our Legacy · Testimonials`), DOM attributes (`data-elementor-device-mode="desktop"`, `data-opened="1"`, `data-elementor-type="header"`, `data-elementor-id="5070"`), and stylesheet rule `root { --direction-multiplier:1 }`.
2. **Hero Stage & Focal Lead (<article.post-2414> — `Premium Apartments in Kochi, by Ar`)**:
   - Landmark `<article class="post-2414 page">` presenting display lead `Premium Apartments in Kochi, by Arya Bhangy Builders` and copy excerpt *"Est. 1969 · Kochi, Kerala"* over `#f7f8f9` canvas and `#222222` ink.
3. **Primary Showcase & Content Grid (<article.page> — `Years in Business`)**:
   - Landmark `<article class="post-2414 page">` rendering section `Years in Business` with copy *"F o r u s , r e a l e s t a t e i s m o r e t h a n c o n s t r u"*, asset references (`1806948866520083`, `fbevents.js`, `gtm.js`, `embed`), and grid rule `.elementor-hidden { display:none }`.
4. **Interactive Detail & Feature Matrix (<article.type-page> — `sq.ft. Developed in Kochi`)**:
   - Landmark `<article class="post-2414 page">` framing `sq.ft. Developed in Kochi` and `Transparent Transactions` (*"Apartments across Kochi, in the areas people are actually looking"*) with `#5bc0de` surface cards, `#375efb` accents, and `.elementor-visibility-hidden { visibility:hidden }`.
5. **Colophon & Global Directory Footer (<footer.elementor> — `https://aryabhangybuilders.com/`)**:
   - Landmark `<footer class="elementor elementor-6448">` anchoring `Premium Builders In Kochi · Flat` footer links (`Home · Residential · Commercial · Our Legacy · Testimonials`), copy *"Commercial spaces built for the businesses inside them. Prac"*, and `#69727d` structural dividers.
