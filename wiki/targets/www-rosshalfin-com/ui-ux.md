---
title: "UI & UX Architecture: www-rosshalfin-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-rosshalfin-com

## Overview & Design Identity
- **Target**: `www-rosshalfin-com` (**Ross Halfin Photography · Music Images + Fine Art Prints**)
- **Production URL**: [https://www.rosshalfin.com](https://www.rosshalfin.com)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×5796px`, Mobile `390×2616px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#161618` canvas, `#c1c5cb` ink, `#0073e6` accent)
- **Summary**: Unparalleled music photography by Ross Halfin - Limited edition Fine-Art prints, signed & embossed. Worldwide shipping
- **Total Clean CSS Variables Extracted**: `67` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Barlow Semi Condensed`
- **Body Font Stack**: `Barlow`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: rule `h1` (`font-size: 30px`, `letter-spacing: -.01em`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 40px`, `line-height: 56px`, `font-weight: 500`, `letter-spacing: 1.2px`); rule `h2` (`font-size: clamp(1.375rem,.9939rem + 1.2...`, `letter-spacing: -.01em`)
- **Body Copy**: live computed `body` (`font-size: 14px`, `line-height: 19.6px`, `font-weight: 400`, `letter-spacing: 0.7px`); CSS variables `--wp--custom--line-height--body: 1.618`, `--cmplz_category_body_font_size: 12px`; rule `p` (`font-size: 12px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 14px`, `line-height: 19.6px`, `font-weight: 400`, `letter-spacing: 0.7px`); rule `small` (`font-size: 11px`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#161618` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#c1c5cb` | live computed `a` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#222222` | `.menu-toggle .bar { background-color: #222222 }` |
| **Interactive Accent / Highlight** | `#0073e6` | `var(--wc-stripe-accent-color)` in `:root` |
| **Secondary / Muted Copy** | `#333333` | `var(--cmplz_button_settings_text_color)` in `:root` |
| **Structural Hairline Border** | `#e6e6e6` | `var(--wc-stripe-saved-token-border-color)` in `:root` |
| **Variable Token (`--wp-block-synced-color`)** | `#7a00df` | `var(--wp-block-synced-color)` in `:root` |
| **Variable Token (`--wp-editor-canvas-background`)** | `#dddddd` | `var(--wp-editor-canvas-background)` in `:root` |
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
| `--wp--custom--line-height--none` | `1` | Typography / Scale Token |
| `--wp--custom--line-height--tight` | `1.1` | Typography / Scale Token |
| `--wp--custom--line-height--snug` | `1.2` | Typography / Scale Token |
| `--wp--custom--line-height--normal` | `1.5` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `www-rosshalfin-com`)**:
   - Landmark `<header class="site-header">` (`234x50px`) hosting `Ross Halfin Photography · Music Imag` navigation (`€ 0.00 0`), DOM attributes (`data-partner-attribution-id="PaymentPlugins_PCP"`, `data-uid-auto="uid_znuqasiucahxrfuik..."`, `data-wp-strategy="defer"`, `data-wp-strategy="defer"`), and stylesheet rule `before { box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<section.pageSection> — `Welcome To Ross Halfin Photography`)**:
   - Landmark `<section class="pageSection home__sec__hl">` presenting display lead `Welcome To Ross Halfin Photography` and copy excerpt *"No products in the basket."* over `#161618` canvas and `#c1c5cb` ink.
3. **Primary Showcase & Content Grid (<section.home__sec__latest_news> — `No products in the basket.`)**:
   - Landmark `<section class="pageSection home__sec__latest_news">` rendering section `No products in the basket.` with copy *"Functional Always active"*, asset references (`recaptcha__en.js`, `xmlrpc.php`, `banner-2-optin.css`, `banner-2-optout.css`), and grid rule `strong { font-weight:bolder }`.
4. **Interactive Detail & Feature Matrix (<section.home__sec__text> — `Functional Always active`)**:
   - Landmark `<section class="pageSection home__sec__text">` framing `Functional Always active` and `Required to enable core site functionality and s` (*"Required to enable core site functionality and services you reque"*) with `#222222` surface cards, `#0073e6` accents, and `samp { font-family:ui-monospace,SFMono-Regular,Consolas,'Liberation Mono',Menlo... }`.
5. **Colophon & Global Directory Footer (<footer.page-template-template-homepage> — `https://www.rosshalfin.com`)**:
   - Landmark `<footer class="page-template-template-homepage">` anchoring `Ross Halfin Photography · Music ` footer links (`€ 0.00 0`), copy *"Used to store your preferences, such as language or display "*, and `#e6e6e6` structural dividers.
