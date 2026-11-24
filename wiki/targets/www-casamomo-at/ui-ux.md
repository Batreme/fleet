---
title: "UI & UX Architecture: www-casamomo-at"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-casamomo-at

## Overview & Design Identity
- **Target**: `www-casamomo-at` (**Casa Momo • Boutique Apartments in Graz**)
- **Production URL**: [https://www.casamomo.at/](https://www.casamomo.at/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×1744px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#0e1201` canvas, `#fff0ca` ink, `#ffffff` accent)
- **Summary**: Personally designed apartments for short and longer stays, between quiet minimalism and warm coziness. Discover boutique, garden, loft an...
- **Total Clean CSS Variables Extracted**: `36` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `Lay Grotesk Regular`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 16px`, `line-height: 19.2px`, `font-weight: 400`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 135px`, `line-height: 135px`, `font-weight: 400`, `letter-spacing: -2.7px`)
- **Body Copy**: live computed `body` (`font-size: 12px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: 13px`, `line-height: 100%`, `letter-spacing: 0px`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 12px`, `line-height: normal`, `font-weight: 400`); CSS variables `--letter-spacing: var(--framer-letter-spacing)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#0e1201` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#fff0ca` | live computed `p` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#964317` | live computed `footer` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#ffffff` | `#__framer-editorbar-button { color: #ffffff }` |
| **Secondary / Muted Copy** | `#000000` | live computed `nav` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#000000` | hairline divider derived from live computed `nav` `color` (`computed_styles.json`) |
| **Variable Token (`--token-11878163-64ae-441d-8311-9e9d670023d9`)** | `#ffe3d4` | `var(--token-11878163-64ae-441d-8311-9e9d670023d9)` in `:root` |
| **Variable Token (`--token-419394a1-565d-4952-8ba3-b4f1eb92339c`)** | `#050505` | `var(--token-419394a1-565d-4952-8ba3-b4f1eb92339c)` in `:root` |
| **Variable Token (`--token-bf966309-2582-4df8-98f4-f091ce81e703`)** | `#131415` | `var(--token-bf966309-2582-4df8-98f4-f091ce81e703)` in `:root` |
| **Variable Token (`--token-86299043-b8f8-4618-9585-4835ac76e9b7`)** | `#bc6f45` | `var(--token-86299043-b8f8-4618-9585-4835ac76e9b7)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--casa-p1-size` | `calc(var(--casa-page-w, 100vw) * 0.020000)` | Layout / Spatial Grid Token |
| `--casa-p1-lh` | `1.2em` | Dimension / Scale Token |
| `--casa-p1-ls` | `-0.2px` | Dimension / Scale Token |
| `--token-8ecd7124-9686-4bd8-bf72-4f81314652d2` | `#fff0ca` | Color / Atmospheric Token |
| `--token-a0f3f7f0-2bee-4607-a7b2-647fda358cb3` | `#0e1201` | Color / Atmospheric Token |
| `--token-11878163-64ae-441d-8311-9e9d670023d9` | `#ffe3d4` | Color / Atmospheric Token |
| `--token-419394a1-565d-4952-8ba3-b4f1eb92339c` | `#050505` | Color / Atmospheric Token |
| `--token-bf966309-2582-4df8-98f4-f091ce81e703` | `#131415` | Color / Atmospheric Token |
| `--token-86299043-b8f8-4618-9585-4835ac76e9b7` | `#bc6f45` | Color / Atmospheric Token |
| `--token-0da0c5a6-8028-40b0-8315-7bce946c6731` | `#131415` | Color / Atmospheric Token |
| `--token-20608b9f-0145-4a1e-b971-ee948ebbb015` | `#fff` | Color / Atmospheric Token |
| `--token-e00ea664-9c78-44de-bf9c-6839d671d9c2` | `#050505` | Color / Atmospheric Token |
| `--token-31f69385-9489-4b68-a801-60367d4b1ac3` | `#0e1201` | Color / Atmospheric Token |
| `--text-decoration-skip-ink` | `var(--framer-text-decoration-skip-ink)` | Typography Ink Token |
| `--text-underline-offset` | `var(--framer-text-decoration-offset)` | Typography Ink Token |
| `--font-family` | `var(--framer-font-family)` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.framer-bg7hsc> — `www-casamomo-at`)**:
   - Landmark `<header class="framer-bg7hsc">` (`1440x110px`) hosting `Casa Momo • Boutique Apartments in G` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-redirect-timezone="1"`, `data-framer-generated-canonical`, `data-framer-font-css`, `data-framer-breakpoint-css`), and stylesheet rule `.hidden-72rtr7 { display:none!important }`.
2. **Hero Stage & Focal Lead (<section.framer-1xtxml1> — `Casa Momo – Designer Apartments in`)**:
   - Landmark `<section class="framer-1xtxml1">` presenting display lead `Casa Momo – Designer Apartments in Graz` and copy excerpt *"I am the head and heart behind Casa Momo and hosting is what I lo"* over `#0e1201` canvas and `#fff0ca` ink.
3. **Primary Showcase & Content Grid (<section.framer-chahzh> — `Boutique N°1`)**:
   - Landmark `<section class="framer-chahzh">` rendering section `Boutique N°1` with copy *"Book Your Stay B B B o o o o o o k k k Y Y Y o o o u u u r r r S "*, asset references (`1i2kLqAOiU4EMx2iRruplpXhvgs.png`, `SaAMBRSDzmk41xPyN78AdKzfnM.png`, `NVhSQp5HYf1e4Zkg5QjllUhdYXM.png`, `eegZ1ZoVjnHyJtxDMTEhJ2Bhf4.woff2`), and grid rule `.hidden-p8zd8m { display:none!important }`.
4. **Interactive Detail & Feature Matrix (<section.framer-mefgjz> — `Boutique N°2`)**:
   - Landmark `<section class="framer-mefgjz">` framing `Boutique N°2` and `Boutique N°3` (*"5.00 / 5 “Moritz is such a gentle and wonderful host! The apartme"*) with `#964317` surface cards, `#ffffff` accents, and `.hidden-o5o8qi { display:none!important }`.
5. **Colophon & Global Directory Footer (<footer.framer-18na9ah> — `https://www.casamomo.at/`)**:
   - Landmark `<footer class="framer-18na9ah">` anchoring `Casa Momo • Boutique Apartments ` footer links (`Overview · Index · Archive · About · Contact`), copy *"“Moritz is such a gentle and wonderful host! The apartment i"*, and `#000000` structural dividers.
