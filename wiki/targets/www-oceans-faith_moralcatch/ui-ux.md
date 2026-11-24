---
title: "UI & UX Architecture: www-oceans-faith_moralcatch"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-oceans-faith_moralcatch

## Overview & Design Identity
- **Target**: `www-oceans-faith_moralcatch` (**The Moral Catch: Fisheries & Ocean Justice — Faiths for Oceans**)
- **Production URL**: [https://www.oceans.faith/moralcatch](https://www.oceans.faith/moralcatch)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×872px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f3ede1` canvas, `#000000` ink, `#e4351e` accent)
- **Summary**: Explore fisheries, ocean life and workers’ rights. Read The Moral Catch report, take the two-minute meal test, and use the faith institut...
- **Total Clean CSS Variables Extracted**: `1004` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Merriweather Sans`
- **Body Font Stack**: `Lato`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 40px`, `line-height: 40px`, `font-weight: 700`); CSS variables `--heading-1-size: 4rem`, `--heading-1-size-value: 4`; rule `.title` (`font-size: 1rem`, `line-height: 1.4`, `font-weight: 500`)
- **Section Heading (`H2`)**: CSS variables `--heading-2-size: 2.8rem`, `--heading-2-size-value: 2.8`
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--body-font-font-family: "Lato"`, `--body-font-font-style: normal`, `--body-font-font-weight: 400`; rule `p` (`line-height: 1.68em`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 16px`, `font-weight: 400`); CSS variables `--heading-font-letter-spacing: 0em`, `--body-font-letter-spacing: 0em`, `--meta-font-font-family: "Poppins"`; rule `.caption` (`font-size: 12px`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f3ede1` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `d .sqs-site-style-form .form-it... { background-color: white }` (`#ffffff`) |
| **Interactive Accent / Highlight** | `#e4351e` | `ontent .buttons .confirmation-b... { background-color: #e4351e }` |
| **Secondary / Muted Copy** | `#0f4157` | live computed `h1` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#e7e7e7` | `rapper .InlineWidgetDropDown-No... { border-right: #e7e7e7 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--tweak-form-block-title-color-on-background` | `#000` | Canvas / Surface Token |
| `--tweak-form-block-caption-color-on-background` | `#000` | Canvas / Surface Token |
| `--tweak-form-block-option-color-on-background` | `#000` | Canvas / Surface Token |
| `--overlap-image-width-flex-offset` | `calc((var(--image-block-overlap-image-width) - 50%) * 2)` | Layout / Spatial Grid Token |
| `--overlap-title-width-offset` | `50%` | Layout / Spatial Grid Token |
| `--collage-image-width-flex-offset` | `calc((var(--image-block-collage-image-width) - 50%) * 2)` | Layout / Spatial Grid Token |
| `--collage-content-width-flex-offset` | `calc((var(--image-block-collage-image-content-width) - 50%) * 2)` | Layout / Spatial Grid Token |
| `--fallback-white-hsl` | `0, 0%, 98%` | Canvas / Surface Token |
| `--fallback-black-hsl` | `0, 0%, 0%` | Canvas / Surface Token |
| `--solid-alpha-modifier` | `1` | Design System Custom Token |
| `--solid-hover-alpha-modifier` | `0.6` | Design System Custom Token |
| `--outline-hover-alpha-modifier` | `0.4` | Elevation / Border Token |
| `--inverted-solid-hover-alpha-modifier` | `var(--solid-hover-alpha-modifier)` | Design System Custom Token |
| `--inverted-outline-hover-alpha-modifier` | `var(--outline-hover-alpha-modifier)` | Elevation / Border Token |
| `--solid-focus-alpha-modifier` | `1` | Design System Custom Token |
| `--outline-focus-alpha-modifier` | `0.4` | Elevation / Border Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.bright-inverse> — `www-oceans-faith_moralcatch`)**:
   - Landmark `<header class="bright-inverse header">` (`1440px`) hosting `The Moral Catch: Fisheries & Ocean J` navigation (`EVENTS · SIGN THE DECLARATION · SIGNATORIES · PUBLICATIONS · GLOSSARY`), DOM attributes (`data-sqsp-font-ids="6a3137d3494e3c6626e63..."`, `data-name="static-context"`, `data-animation-state="booted"`, `data-test="header"`), and stylesheet rule `dgetWrapper .TockInlineButton-con... { border-radius:3px }`.
2. **Hero Stage & Focal Lead (<article.page-regions> — `Stay Connected`)**:
   - Landmark `<article class="page-regions">` presenting display lead `Stay Connected` and copy excerpt *"Faiths for Oceans © 2026"* over `#f3ede1` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.region> — `Faiths for Oceans © 2026`)**:
   - Landmark `<section class="region">` rendering section `Faiths for Oceans © 2026` with copy *"MULTI-FAITH DECLARATION"*, asset references (`popup-overlay-f39ec8cdc95ccd84-mi...`, `tc.min.js`, `popup-overlay-eb69d574e194d111-mi...`, `favicon.ico`), and grid rule `hover { opacity:.8 }`.
4. **Interactive Detail & Feature Matrix (<section.page-section> — `MULTI-FAITH DECLARATION`)**:
   - Landmark `<section class="page-section full-bleed-section">` framing `MULTI-FAITH DECLARATION` and `The illustrated story needs JavaScript. You can ` (*"The illustrated story needs JavaScript. You can download the repo"*) with `#ffffff` surface cards, `#e4351e` accents, and `.btn:hover { background-color:transparent!important }`.
5. **Colophon & Global Directory Footer (<footer.sections> — `https://www.oceans.faith/moralcatch`)**:
   - Landmark `<footer class="sections">` anchoring `The Moral Catch: Fisheries & Oce` footer links (`EVENTS · SIGN THE DECLARATION · SIGNATORIES · PUBLICATIONS · GLOSSARY`), copy *"Join our mailing list to receive the latest news, updates an"*, and `#e7e7e7` structural dividers.
