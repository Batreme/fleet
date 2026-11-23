---
title: "UI & UX Architecture: concretaceramiche-it"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: concretaceramiche-it

## Overview & Design Identity
- **Target**: `concretaceramiche-it` (**Concreta Ceramiche Artigianali Fatte a Mano**)
- **Production URL**: [https://concretaceramiche.it/](https://concretaceramiche.it/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#2d0d01` canvas, `#c0d2cc` ink, `#ff0000` accent)
- **Summary**: Ceramiche artigianali uniche, realizzate a mano nei Castelli Romani. Gres, stampa 3D e tradizione familiare in ogni pezzo. Scopri la coll...
- **Total Clean CSS Variables Extracted**: `68` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Elgoc`
- **Body Font Stack**: `Elgoc`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 16px`, `line-height: 16px`, `font-weight: 400`); rule `h1` (`font-size: 25px`, `line-height: 32px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 40px`, `line-height: 40px`, `font-weight: 400`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 16px`, `font-weight: 400`); CSS variables `--cmplz_category_body_font_size: 12px`; rule `p` (`font-weight: 500`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 16px`, `font-weight: 400`); rule `small` (`font-size: 15px`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#2d0d01` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#c0d2cc` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#cd2653` | `d__products .wc-block-grid__pro... { background: #cd2653 }` |
| **Interactive Accent / Highlight** | `#ff0000` | `.woocommerce a.remove { color: red }` (`#ff0000`) |
| **Secondary / Muted Copy** | `#767676` | `var(--wc-subtext)` in `:root` |
| **Structural Hairline Border** | `#230806` | `var(--wc-form-border-color)` in `:root` (`rgba(32, 7, 7, 0.8)`) |
| **Variable Token (`--wp-block-synced-color`)** | `#7a00df` | `var(--wp-block-synced-color)` in `:root` |
| **Variable Token (`--wp-editor-canvas-background`)** | `#dddddd` | `var(--wp-editor-canvas-background)` in `:root` |
| **Variable Token (`--wp-admin-theme-color`)** | `#007cba` | `var(--wp-admin-theme-color)` in `:root` |
| **Variable Token (`--wp-admin-theme-color-darker-10`)** | `#006ba1` | `var(--wp-admin-theme-color-darker-10)` in `:root` |
| **Variable Token (`--wp-admin-theme-color-darker-20`)** | `#005a87` | `var(--wp-admin-theme-color-darker-20)` in `:root` |
| **Variable Token (`--woocommerce`)** | `#720eec` | `var(--woocommerce)` in `:root` |
| **Variable Token (`--wc-green`)** | `#008a20` | `var(--wc-green)` in `:root` |

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
| `--drawer-width` | `480px` | Layout / Spatial Grid Token |
| `--neg-drawer-width` | `calc(var(--drawer-width) * -1)` | Layout / Spatial Grid Token |
| `--woocommerce` | `#720eec` | Color / Atmospheric Token |
| `--wc-green` | `#008a20` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.negative> — `concretaceramiche-it`)**:
   - Landmark `<header class="negative fixed">` (`1425x78px`) hosting `Concreta Ceramiche Artigianali Fatte` navigation (`h o m e h o m e · c o r s i c o r s i · S h o p S h o p · EN · Home`), DOM attributes (`data-wp-strategy="defer"`, `data-wp-strategy="defer"`, `data-wp-strategy="defer"`, `data-wp-strategy="defer"`), and stylesheet rule `body.wc-modal--open { overflow:hidden }`.
2. **Hero Stage & Focal Lead (<section.rank-math-schema> — `ConCreta ceramiche artigianali Rom`)**:
   - Landmark `<section class="rank-math-schema">` presenting display lead `ConCreta ceramiche artigianali Roma` and copy excerpt *"Nel cuore dei Castelli Romani, diamo forma a oggetti che uniscono"* over `#2d0d01` canvas and `#c0d2cc` ink.
3. **Primary Showcase & Content Grid (<section.logo> — `La ceramica artigianale prende for`)**:
   - Landmark `<section class="logo">` rendering section `La ceramica artigianale prende forma tra gesti an...` with copy *"l a b o r a t o r i o l a b o r a t o r i o"*, asset references (`Elgoc-Bold.woff2`, `Elgoc-Regular.woff2`, `Inter28pt-Medium.woff2`, `Inter28pt-Regular.woff2`), and grid rule `products .wc-block-grid__product-... { display:block;position:relative;text-decoration:none }`.
4. **Interactive Detail & Feature Matrix (<section.wp-singular> — `Oggetti in ceramica nati dall’inco`)**:
   - Landmark `<section class="wp-singular">` framing `Oggetti in ceramica nati dall’incontro tra tecnic...` and `Un luogo dove la terra diventa forma e prende vita` (*"l a b o r a t o r i o"*) with `#cd2653` surface cards, `#ff0000` accents, and `roducts .wc-block-grid__product-i... { border:0;box-shadow:none;outline:0;text-decoration:none }`.
5. **Colophon & Global Directory Footer (<footer.page-template> — `https://concretaceramiche.it/`)**:
   - Landmark `<footer class="page-template">` anchoring `Concreta Ceramiche Artigianali F` footer links (`h o m e h o m e · c o r s i c o r s i · S h o p S h o p · EN · Home`), copy *"c o s a r e a l i z z i a m o c o s a r e a l i z z i a m o"*, and `#230806` structural dividers.
