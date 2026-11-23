---
title: "UI & UX Architecture: edisonfangworkshop-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: edisonfangworkshop-com

## Overview & Design Identity
- **Target**: `edisonfangworkshop-com` (**Edison Fang Workshop**)
- **Production URL**: [https://edisonfangworkshop.com](https://edisonfangworkshop.com)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×1795px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#d8ed42`)
- **Summary**: Edison Fang Workshop is a spatial design practice in Taichung, Taiwan, working across interiors, exhibitions, visual identity and spatial...
- **Total Clean CSS Variables Extracted**: `125` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Source Code Variable`
- **Body Font Stack**: `Noto Sans TC`
- **Monospace / Technical Font Stack**: `Source Code Variable`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 144px`, `line-height: 155.52px`, `font-weight: 300`, `letter-spacing: -7.92px`); rule `h1` (`letter-spacing: -.045em`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); rule `h2` (`letter-spacing: -.06em`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--font-body: Arial, "Noto Sans TC", "PingFang TC", "Microsoft JhengHei", sans-serif`, `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`; rule `p` (`font-size: 12px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 99.6795px`, `line-height: 109.647px`, `font-weight: 300`); CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`; rule `small` (`font-size: 9px`, `letter-spacing: .08em`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#090909` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#dfddd5` | `var(--paper)` in `:root` |
| **Interactive Accent / Highlight** | `#d8ed42` | `var(--fourth-accent)` in `:root` |
| **Secondary / Muted Copy** | `#8b8982` | `var(--muted)` in `:root` |
| **Structural Hairline Border** | `#f7f7f5` | `var(--line)` in `:root` (`dfddd53d`) |
| **Variable Token (`--ink`)** | `#080808` | `var(--ink)` in `:root` |
| **Variable Token (`--ink-soft`)** | `#101010` | `var(--ink-soft)` in `:root` |
| **Variable Token (`--paper-bright`)** | `#f1efe8` | `var(--paper-bright)` in `:root` |
| **Variable Token (`--red`)** | `#3b0d0d` | `var(--red)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--menu-control-gap` | `10px` | Layout / Spatial Grid Token |
| `--menu-control-stop` | `calc(var(--menu-control-gap) - 1px)` | Dimension / Scale Token |
| `--font-editorial` | `"Iowan Old Style", "Baskerville", "Times New Roman", "Noto Serif TC", serif` | Typography / Scale Token |
| `--font-body` | `Arial, "Noto Sans TC", "PingFang TC", "Microsoft JhengHei", sans-serif` | Typography / Scale Token |
| `--ink` | `#080808` | Typography Ink Token |
| `--ink-soft` | `#101010` | Typography Ink Token |
| `--paper` | `#dfddd5` | Canvas / Surface Token |
| `--paper-bright` | `#f1efe8` | Canvas / Surface Token |
| `--muted` | `#8b8982` | Color / Atmospheric Token |
| `--line` | `#dfddd53d` | Color / Atmospheric Token |
| `--red` | `#3b0d0d` | Color / Atmospheric Token |
| `--page-pad` | `clamp(1.25rem, 4vw, 4.5rem)` | Layout / Spatial Grid Token |
| `--desktop-media-max` | `min(68rem, 126svh)` | Dimension / Scale Token |
| `--lightningcss-light` | `initial` | Canvas / Surface Token |
| `--size` | `340px` | Layout / Spatial Grid Token |
| `--case-depth` | `11.9px` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.portfolio-header> — `edisonfangworkshop-com`)**:
   - Landmark `<header class="portfolio-header smart-header">` (`1425x100px`) hosting `Edison Fang Workshop` navigation (`H O M E Introduction`), DOM attributes (`data-mood="true"`, `data-overture-boot="true"`, `data-precedence="vite-rsc/client-refer..."`, `data-precedence="vite-rsc/client-refer..."`), and stylesheet rule `._word_1rad1_1 { display:inline-block;position:relative;overflow:visible }`.
2. **Hero Stage & Focal Lead (<section.unreleased-home-intro> — `Let’s give it form.`)**:
   - Landmark `<section class="unreleased-home-intro home-formation">` presenting display lead `Let’s give it form.` and copy excerpt *"EDISON FANG WORKSHOP"* over `#ffffff` canvas and `#090909` ink.
3. **Primary Showcase & Content Grid (<section.home-form-poster> — `Spatial & graphic design`)**:
   - Landmark `<section class="home-form-poster home-train-poster">` rendering section `Spatial & graphic design` with copy *"MENU CLOSE MENU CLOSE"*, asset references (`source-code-pro-variable-latin.woff2`, `workshop-shell-qHtOR3l2.css`, `page-Cg2bIiDZ.css`, `index-CHG0PVT-.css`), and grid rule `._original_1rad1_2 { display:inline-block }`.
4. **Interactive Detail & Feature Matrix (<section.portfolio-contact> — `MENU CLOSE MENU CLOSE`)**:
   - Landmark `<section class="portfolio-contact home-contact-invitation">` framing `MENU CLOSE MENU CLOSE` and `COLLECTION INDEX SPATIAL / GRAPHIC` (*"COLLECTION INDEX SPATIAL / GRAPHIC"*) with `#dfddd5` surface cards, `#d8ed42` accents, and `._code_1rad1_5 { text-align:center;font:inherit;letter-spacing:inherit;pointer-events:non... }`.
5. **Colophon & Global Directory Footer (<footer.collection-menu-footer> — `https://edisonfangworkshop.com`)**:
   - Landmark `<footer class="collection-menu-footer">` anchoring `Edison Fang Workshop` footer links (`H O M E Introduction`), copy *"H O M E Introduction"*, and `#f7f7f5` structural dividers.
