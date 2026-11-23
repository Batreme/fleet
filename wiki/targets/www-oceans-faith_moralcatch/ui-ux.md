---
title: "UI & UX Architecture: www-oceans-faith_moralcatch"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: www-oceans-faith_moralcatch

## Overview & Design Identity
- **Target**: `www-oceans-faith_moralcatch` (**The Moral Catch: Fisheries & Ocean Justice — Faiths for Oceans**)
- **Production URL**: [https://www.oceans.faith/moralcatch](https://www.oceans.faith/moralcatch)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f3ede1` canvas, `#000000` ink, `#ffffff` accent)
- **Summary**: Explore fisheries, ocean life and workers’ rights. Read The Moral Catch report, take the two-minute meal test, and use the faith institut...
- **Total Clean CSS Variables Extracted**: `30` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Merriweather Sans`
- **Body Font Stack**: `Lato`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 40px`, `line-height: 40px`, `font-weight: 700`); rule `h1` (`line-height: 1em`)
- **Section Heading (`H2`)**: observed font-size ladder: `40px`, `16px`, `22.912px`, `15px`, `12px`
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: 16px`, `line-height: 22px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 16px`, `font-weight: 400`); rule `.caption` (`font-size: 12px`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f3ede1` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#e7e7e7` | `.commerce-mini-cart-item-image-... { background-color: #e7e7e7 }` |
| **Interactive Accent / Highlight** | `#ffffff` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#0f4157` | live computed `h1` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#999999` | `orm-wrapper .field-list .sectio... { border-bottom: #999999 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--commerce-mini-cart-image-size` | `60px` | Layout / Spatial Grid Token |
| `--commerce-mini-cart-image-placeholder-size` | `22px` | Layout / Spatial Grid Token |
| `--grid-gutter` | `calc(var(--sqs-mobile-site-gutter, 6vw) - 11.0px)` | Layout / Spatial Grid Token |
| `--cell-max-width` | `calc( ( var(--sqs-site-max-width, 1500px) - (11.0px * (8 - 1)) ) / 8 )` | Layout / Spatial Grid Token |
| `--inset-padding` | `calc(var(--sqs-site-gutter) * 2)` | Layout / Spatial Grid Token |
| `--row-height-scaling-factor` | `0.0215` | Layout / Spatial Grid Token |
| `--opacity` | `100%` | Dimension / Scale Token |
| `--translate-x` | `0px` | Dimension / Scale Token |
| `--translate-y` | `0px` | Dimension / Scale Token |
| `--rotation` | `0deg` | Design System Custom Token |
| `--scale-x` | `100%` | Dimension / Scale Token |
| `--scale-y` | `100%` | Dimension / Scale Token |
| `--skew-x` | `0deg` | Design System Custom Token |
| `--skew-y` | `0deg` | Design System Custom Token |
| `--origin-x` | `50%` | Dimension / Scale Token |
| `--origin-y` | `50%` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.bright-inverse> — `www-oceans-faith_moralcatch`)**:
   - Landmark `<header class="bright-inverse header">` (`1440px`) hosting `The Moral Catch: Fisheries & Ocean J` navigation (`EVENTS · SIGN THE DECLARATION · SIGNATORIES · PUBLICATIONS · GLOSSARY`), DOM attributes (`data-sqsp-font-ids="6a3136d96307d35684222..."`, `data-name="static-context"`, `data-animation-state="booted"`, `data-test="header"`), and stylesheet rule `.uppercase { text-transform:uppercase }`.
2. **Hero Stage & Focal Lead (<article.page-regions> — `Stay Connected`)**:
   - Landmark `<article class="page-regions">` presenting display lead `Stay Connected` and copy excerpt *"Faiths for Oceans © 2026"* over `#f3ede1` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.region> — `Faiths for Oceans © 2026`)**:
   - Landmark `<section class="region">` rendering section `Faiths for Oceans © 2026` with copy *"MULTI-FAITH DECLARATION"*, asset references (`popup-overlay-f39ec8cdc95ccd84-mi...`, `popup-overlay-eb69d574e194d111-mi...`, `favicon.ico`, `moralcatch`), and grid rule `rce-reserved-cart-container--anim... { animation:.4s cubic-bezier(.23,1,.32,1) 1s both commerce-reserved-cart-s... }`.
4. **Interactive Detail & Feature Matrix (<section.page-section> — `MULTI-FAITH DECLARATION`)**:
   - Landmark `<section class="page-section full-bleed-section">` framing `MULTI-FAITH DECLARATION` and `The illustrated story needs JavaScript. You can ` (*"The illustrated story needs JavaScript. You can download the repo"*) with `#e7e7e7` surface cards, `#ffffff` accents, and `mmerce-reserved-cart-container--c... { animation:.35s cubic-bezier(.23,1,.32,1) forwards commerce-reserved-cart... }`.
5. **Colophon & Global Directory Footer (<footer.sections> — `https://www.oceans.faith/moralcatch`)**:
   - Landmark `<footer class="sections">` anchoring `The Moral Catch: Fisheries & Oce` footer links (`EVENTS · SIGN THE DECLARATION · SIGNATORIES · PUBLICATIONS · GLOSSARY`), copy *"Join our mailing list to receive the latest news, updates an"*, and `#999999` structural dividers.
