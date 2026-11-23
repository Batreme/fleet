---
title: "UI & UX Architecture: kingriver-com-au"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: kingriver-com-au

## Overview & Design Identity
- **Target**: `kingriver-com-au` (**Australian Wagyu Beef · King River Legendary Wagyu**)
- **Production URL**: [https://kingriver.com.au/](https://kingriver.com.au/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#e5240a`)
- **Summary**: Explore the exquisite taste of King River Australian Wagyu beef and its unique quality that sets it apart in the culinary world.
- **Total Clean CSS Variables Extracted**: `51` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `sweet-sans-pro`
- **Body Font Stack**: `feijoa`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 32px`, `line-height: 40px`, `font-weight: 700`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 32px`, `line-height: 40px`, `font-weight: 700`); rule `,h2` (`font-size: 1.375rem`, `font-weight: 700`)
- **Body Copy**: live computed `body` (`font-size: 14px`, `line-height: 22.75px`, `font-weight: 500`); rule `p` (`font-size: .75rem`, `line-height: 2`, `letter-spacing: .05em`, `font-weight: 700`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 14px`, `line-height: 22.75px`, `font-weight: 500`); CSS variables `--chain-meta: 1rem`, `--chain-meta-gap: 1.25rem`, `--chain-caption-gap: 0px`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | `.wp-block-button__link { color: #ffffff }` |
| **Elevated Surface / Card Substrate** | `#3b1013` | live computed `footer` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#e5240a` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#e5240a` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#e5240a` | `var(--field-rule)` in `:root` |
| **Variable Token (`--wp-block-synced-color`)** | `#7a00df` | `var(--wp-block-synced-color)` in `:root` |
| **Variable Token (`--wp-editor-canvas-background`)** | `#dddddd` | `var(--wp-editor-canvas-background)` in `:root` |
| **Variable Token (`--wp-admin-theme-color`)** | `#007cba` | `var(--wp-admin-theme-color)` in `:root` |
| **Variable Token (`--wp-admin-theme-color-darker-10`)** | `#006ba1` | `var(--wp-admin-theme-color-darker-10)` in `:root` |
| **Variable Token (`--wp-admin-theme-color-darker-20`)** | `#005a87` | `var(--wp-admin-theme-color-darker-20)` in `:root` |
| **Variable Token (`--button-base`)** | `#f6ede8` | `var(--button-base)` in `:root` |

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
| `--button-base` | `#f6ede8` | Color / Atmospheric Token |
| `--button-ink` | `#3b1013` | Typography Ink Token |
| `--button-fill` | `#f6ede8` | Color / Atmospheric Token |
| `--marker-size` | `12px` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.top-0> — `kingriver-com-au`)**:
   - Landmark `<header class="top-0 text-gum-light">` (`1440x59px`) hosting `Australian Wagyu Beef · King River L` navigation (`Our Properties · Our Story · Our Beef · Jewel · Partners`), DOM attributes (`data-template="base.twig"`, `data-transition`, `data-transition-shade`, `data-transition-panel`), and stylesheet rule `.tk-sweet-sans-pro { font-family: "sweet-sans-pro",sans-serif; }`.
2. **Hero Stage & Focal Lead (<section.remove-section-padding> — `KING RIVER`)**:
   - Landmark `<section class="remove-section-padding h-svh">` presenting display lead `KING RIVER` and copy excerpt *"FIFTH-GENERATION AUSTRALIAN WAGYU"* over `#000000` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.bg-maroon-dark> — `King River`)**:
   - Landmark `<section class="bg-maroon-dark relative">` rendering section `King River` with copy *"Queensland, Australia"*, asset references (`clarity.js`, `yxd9a243r4`, `gtm.js`, `humans.txt`), and grid rule `before { border:0 solid e5e7eb;box-sizing:border-box }`.
4. **Interactive Detail & Feature Matrix (<section.yoast-schema-graph> — `From our family to yours.`)**:
   - Landmark `<section class="yoast-schema-graph">` framing `From our family to yours.` and `AUSTRALIA’S FINEST LUXURY WAGYU. RAISED ON PURE P...` (*"Fifth-generation Australian Wagyu"*) with `#3b1013` surface cards, `#e5240a` accents, and `body { line-height:inherit;margin:0 }`.
5. **Colophon & Global Directory Footer (<footer.bg-maroon-dark> — `https://kingriver.com.au/`)**:
   - Landmark `<footer class="bg-maroon-dark text-scarlet">` anchoring `Australian Wagyu Beef · King Riv` footer links (`Our Properties · Our Story · Our Beef · Jewel · Partners`), copy *"King River is a fifth-generation family business producing A"*, and `#e5240a` structural dividers.
