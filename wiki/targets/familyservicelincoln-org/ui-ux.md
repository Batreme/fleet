---
title: "UI & UX Architecture: familyservicelincoln-org"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: familyservicelincoln-org

## Overview & Design Identity
- **Target**: `familyservicelincoln-org` (**Family Service Lincoln: Everyone Deserves the Chance to Thrive**)
- **Production URL**: [https://familyservicelincoln.org](https://familyservicelincoln.org)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×4968px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#171717` ink, `#00c2ff` accent)
- **Summary**: For over 135 years, we have adapted to meet the needs of families, serving as Lincoln's first charitable organization.
- **Total Clean CSS Variables Extracted**: `775` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Google Sans`
- **Body Font Stack**: `Google Sans`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 72px`, `line-height: 72px`, `font-weight: 700`, `letter-spacing: -1.8px`); CSS variables `--gf-field-pwd-str-ind-display: inline-block`, `--gf-local-display: block`; rule `h1` (`font-size: 3rem`, `line-height: 1`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 70px`, `line-height: 81.9px`, `font-weight: 400`, `letter-spacing: -1.4px`); rule `h2` (`font-size: clamp(32px,5vw,70px)`, `line-height: 1.17`, `letter-spacing: -1.4px`, `font-weight: 400`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); rule `,p` (`font-size: 1rem`, `line-height: 1.5rem`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--gf-label-width: 30%`, `--gf-label-req-gap: 6px`, `--gf-label-space-primary: 8px`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#171717` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#dddddd` | `var(--wp-editor-canvas-background)` in `:root` |
| **Interactive Accent / Highlight** | `#00c2ff` | `var(--gf-field-pg-prog-bar-bg-gradient-blues)` in `:root` |
| **Secondary / Muted Copy** | `#a7b0bd` | `var(--gmcc-text-muted)` in `:root` |
| **Structural Hairline Border** | `#6b7280` | `textarea { border-color: #6b7280 }` |
| **Variable Token (`--wp-block-synced-color`)** | `#7a00df` | `var(--wp-block-synced-color)` in `:root` |
| **Variable Token (`--wp-admin-theme-color`)** | `#007cba` | `var(--wp-admin-theme-color)` in `:root` |
| **Variable Token (`--wp-admin-theme-color-darker-10`)** | `#006ba1` | `var(--wp-admin-theme-color-darker-10)` in `:root` |
| **Variable Token (`--wp-admin-theme-color-darker-20`)** | `#005a87` | `var(--wp-admin-theme-color-darker-20)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--wp-block-synced-color` | `#7a00df` | Brand / Palette Token |
| `--wp-block-synced-color--rgb` | `122,0,223` | Brand / Palette Token |
| `--wp-bound-block-color` | `var(--wp-block-synced-color)` | Brand / Palette Token |
| `--wp-editor-canvas-background` | `#ddd` | Canvas / Surface Token |
| `--wp-admin-theme-color` | `#007cba` | Brand / Palette Token |
| `--wp-admin-theme-color--rgb` | `0,124,186` | Brand / Palette Token |
| `--wp-admin-theme-color-darker-10` | `#006ba1` | Canvas / Surface Token |
| `--wp-admin-theme-color-darker-10--rgb` | `0,107,160.5` | Canvas / Surface Token |
| `--wp-admin-theme-color-darker-20` | `#005a87` | Canvas / Surface Token |
| `--wp-admin-theme-color-darker-20--rgb` | `0,90,135` | Canvas / Surface Token |
| `--wp-admin-border-width-focus` | `2px` | Layout / Spatial Grid Token |
| `--wp-admin--admin-bar--position-offset` | `var(--wp-admin--admin-bar--height,0px)` | Dimension / Scale Token |
| `--header-height` | `88px` | Layout / Spatial Grid Token |
| `--admin-bar-height` | `32px` | Layout / Spatial Grid Token |
| `--gform-theme-control-shadow` | `none` | Brand / Palette Token |
| `--gform-theme-control-size` | `auto` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.top-0> — `familyservicelincoln-org`)**:
   - Landmark `<header class="top-0 left-0">` (`1440x100px`) hosting `Family Service Lincoln: Everyone Des` navigation (`About Us · Leadership Team · Annual Report · Strategic Plan · Form 990`), DOM attributes (`data-cbid="1670e8a1-465b-4331-ab..."`, `data-blockingmode="manual"`, `data-acsb-sr-alert="true"`, `data-acsb-sr-only="true"`), and stylesheet rule `before { box-sizing:border-box;border:0 solid e5e7eb }`.
2. **Hero Stage & Focal Lead (<section.module-hero> — `Everyone Deserves the Chance to Th`)**:
   - Landmark `<section class="module-hero full">` presenting display lead `Everyone Deserves the Chance to Thrive` and copy excerpt *"Join FSL for Science Saturdays at FiftyOne Commons!"* over `#ffffff` canvas and `#171717` ink.
3. **Primary Showcase & Content Grid (<section.module-program_tabs> — `Serving Thousands of Households An`)**:
   - Landmark `<section class="module-program_tabs full">` rendering section `Serving Thousands of Households Annually` with copy *"Child Care Food Program (CCFP)"*, asset references (`logconsent.ashx`, `state.js`, `widgetIcon.min.js`, `cc.js`), and grid rule `body { margin:0;line-height:inherit }`.
4. **Interactive Detail & Feature Matrix (<section.module-impact_stats> — `Together, Our Efforts Make a Measu`)**:
   - Landmark `<section class="module-impact_stats full">` framing `Together, Our Efforts Make a Measurable Difference` and `Strong Families Build Strong Communities` (*"Housing & Support Services"*) with `#dddddd` surface cards, `#00c2ff` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.full> — `https://familyservicelincoln.org`)**:
   - Landmark `<footer class="full relative">` anchoring `Family Service Lincoln: Everyone` footer links (`About Us · Leadership Team · Annual Report · Strategic Plan · Form 990`), copy *"Women, Infants, and Children (WIC)"*, and `#6b7280` structural dividers.
