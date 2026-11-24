---
title: "UI & UX Architecture: www-enigmascult-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-enigmascult-com

## Overview & Design Identity
- **Target**: `www-enigmascult-com` (**Enigma – Sneaker Auctions, Mystery Boxes & Reborn Customs**)
- **Production URL**: [https://www.enigmascult.com/](https://www.enigmascult.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#0a0a0a` / `#ff0000`)
- **Summary**: Enigma is the cult of authenticated streetwear: live sneaker auctions, style-coded mystery boxes and Reborn customs. Decode your style. J...
- **Total Clean CSS Variables Extracted**: `102` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Editorial Today`
- **Body Font Stack**: `Helvena`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 75px`, `line-height: 81px`, `font-weight: 200`, `letter-spacing: -3px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 90px`, `line-height: 82.8px`, `font-weight: 200`); rule `h2` (`font-size: var(--wp--preset--font-size--...`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: clamp(14px,.8854166667vw,17px)`, `line-height: 1.4`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--wpforms-field-size-sublabel-spacing: 5px`, `--wpforms-label-size-font-size: 16px`, `--wpforms-label-size-line-height: 19px`; rule `small` (`font-size: clamp(11px,.6770833333vw,13px)`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#0a0a0a` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#f9f9f9` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#000000` | live computed `section` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#ff0000` | `.woocommerce a.remove { color: red }` (`#ff0000`) |
| **Secondary / Muted Copy** | `#767676` | `var(--wc-subtext)` in `:root` |
| **Structural Hairline Border** | `#066aab` | `var(--wpforms-button-border-color)` in `:root` |
| **Variable Token (`--wp-block-synced-color`)** | `#7a00df` | `var(--wp-block-synced-color)` in `:root` |
| **Variable Token (`--wp-editor-canvas-background`)** | `#dddddd` | `var(--wp-editor-canvas-background)` in `:root` |
| **Variable Token (`--wp-admin-theme-color`)** | `#007cba` | `var(--wp-admin-theme-color)` in `:root` |
| **Variable Token (`--wp-admin-theme-color-darker-10`)** | `#006ba1` | `var(--wp-admin-theme-color-darker-10)` in `:root` |
| **Variable Token (`--wp-admin-theme-color-darker-20`)** | `#005a87` | `var(--wp-admin-theme-color-darker-20)` in `:root` |
| **Variable Token (`--woocommerce`)** | `#720eec` | `var(--woocommerce)` in `:root` |
| **Variable Token (`--wc-green`)** | `#007518` | `var(--wc-green)` in `:root` |
| **Variable Token (`--wc-red`)** | `#aa0000` | `var(--wc-red)` in `:root` |
| **Variable Token (`--wc-orange`)** | `#ffba00` | `var(--wc-orange)` in `:root` |

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
| `--woocommerce` | `#720eec` | Color / Atmospheric Token |
| `--wc-green` | `#007518` | Color / Atmospheric Token |
| `--wc-red` | `#a00` | Color / Atmospheric Token |
| `--wc-orange` | `#ffba00` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.wp-block-template-part> — `www-enigmascult-com`)**:
   - Landmark `<header class="wp-block-template-part">` (`1440x0px`) hosting `Enigma – Sneaker Auctions, Mystery B` navigation (`My Account · Cart · Wishlist`), DOM attributes (`data-wp-strategy="defer"`, `data-wp-strategy="defer"`, `data-wp-strategy="defer"`, `data-wp-strategy="defer"`), and stylesheet rule `.woocommerce-checkout main .wooco... { max-width:1000px }`.
2. **Hero Stage & Focal Lead (<section.block-hero> — `DECODE YOUR STYLE`)**:
   - Landmark `<section class="block-hero alignfull">` presenting display lead `DECODE YOUR STYLE` and copy excerpt *"CREATED FROM STUNNERS, FOR STUNNERS."* over `#0a0a0a` canvas and `#f9f9f9` ink.
3. **Primary Showcase & Content Grid (<section.manifesto> — `Decode Your Style`)**:
   - Landmark `<section class="manifesto alignfull">` rendering section `Decode Your Style` with copy *"Created from stunners, for stunners."*, asset references (`embed`, `woocommerce-blocktheme.css`, `style-index.css`, `woocommerce-layout.css`), and grid rule `.clear { clear:both }`.
4. **Interactive Detail & Feature Matrix (<section.mystery-box> — `Mini Manifesto`)**:
   - Landmark `<section class="mystery-box alignfull">` framing `Mini Manifesto` and `Honor the Grind` (*"This isn’t fashion — it’s initiation. “we don’t revive fashion. w"*) with `#000000` surface cards, `#ff0000` accents, and `hover { opacity:.5 }`.
5. **Colophon & Global Directory Footer (<footer.wp-block-template-part> — `https://www.enigmascult.com/`)**:
   - Landmark `<footer class="wp-block-template-part">` anchoring `Enigma – Sneaker Auctions, Myste` footer links (`My Account · Cart · Wishlist`), copy *"Enigma is a fashion cult that guards the flame of true hype."*, and `#066aab` structural dividers.
