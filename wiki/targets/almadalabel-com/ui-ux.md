---
title: "UI & UX Architecture: almadalabel-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: almadalabel-com

## Overview & Design Identity
- **Target**: `almadalabel-com` (**ALMADA LABEL - A modern take on a seasonless wardrobe**)
- **Production URL**: [https://almadalabel.com/](https://almadalabel.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#0000ee` accent)
- **Summary**: Seasonless modern wardrobe staples designed with Scandinavian minimalism, resonating beyond trends. Responsibly crafted from high-quality...
- **Total Clean CSS Variables Extracted**: `108` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Paragraph Primary Font`
- **Body Font Stack**: `Paragraph Primary Font`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 14px`, `line-height: 18.2px`, `font-weight: 400`); rule `h1` (`font-size: 32px`, `line-height: normal`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 18px`, `line-height: 24px`, `font-weight: 400`); rule `h2` (`font-size: .875rem`, `line-height: 1.125rem`, `letter-spacing: 0`, `font-weight: 400`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 20.8px`, `font-weight: 400`); CSS variables `--type_primary_paragraph_font: 'Paragraph Primary Font'`, `--weight_paragraph_font: 400`; rule `p` (`font-size: .75rem`, `line-height: 1.125rem`, `letter-spacing: 0`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 14px`, `line-height: 18.2px`, `font-weight: 400`); CSS variables `--mobile-menu-label-gap: .375rem`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `browser-default` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f3f2f2` | `var(--background_color_2)` in `:root` |
| **Interactive Accent / Highlight** | `#0000ee` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#88847c` | `var(--secondary_gray)` in `:root` |
| **Structural Hairline Border** | `#a6a6a5` | `var(--button-border)` in `:root` |
| **Variable Token (`--primary_text`)** | `#17140f` | `var(--primary_text)` in `:root` |
| **Variable Token (`--secondary_accent`)** | `#38302e` | `var(--secondary_accent)` in `:root` |
| **Variable Token (`--primary_gray`)** | `#55534e` | `var(--primary_gray)` in `:root` |
| **Variable Token (`--loader_color`)** | `#1e242a` | `var(--loader_color)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--background_color` | `#ffffff` | Canvas / Surface Token |
| `--background_color_2` | `#f3f2f2` | Canvas / Surface Token |
| `--primary_text` | `#17140f` | Typography Ink Token |
| `--secondary_text` | `#ffffff` | Typography Ink Token |
| `--primary_accent` | `#a6a6a5` | Brand / Palette Token |
| `--secondary_accent` | `#38302e` | Brand / Palette Token |
| `--primary_gray` | `#55534e` | Brand / Palette Token |
| `--secondary_gray` | `#88847c` | Brand / Palette Token |
| `--tertiary_gray` | `#f3f2f2` | Color / Atmospheric Token |
| `--button-bg` | `#a6a6a5` | Canvas / Surface Token |
| `--button-content` | `#ffffff` | Color / Atmospheric Token |
| `--button-border` | `#a6a6a5` | Elevation / Border Token |
| `--body_color` | `#FFF` | Brand / Palette Token |
| `--loader_color` | `#1e242a` | Brand / Palette Token |
| `--submenu-position` | `54px` | Dimension / Scale Token |
| `--header-height` | `54px` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.Drawer__header> — `almadalabel-com`)**:
   - Landmark `<header class="Drawer__header">` (`1440px`) hosting `ALMADA LABEL - A modern take on a se` navigation (`Journal · New Arrivals · Coming Soon · Gift Edit New · Occasion Edit New`), DOM attributes (`data-source-attribution="shopify.exit_intersti..."`, `data-shop-id="25465225306"`, `data-venmo-supported="false"`, `data-environment="production"`), and stylesheet rule `.form-checkbox__label { display:flex;flex-direction:row;align-items:center;gap:.5rem;width:100%;... }`.
2. **Hero Stage & Focal Lead (<article.favorites-drawer__item> — `ALMADA`)**:
   - Landmark `<article class="favorites-drawer__item">` presenting display lead `ALMADA` and copy excerpt *"Free shipping to Germany on orders over 300€"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<article.favorites-drawer__item:nth(2)> — `Silk, lustrous satin and delicate `)**:
   - Landmark `<article class="favorites-drawer__item">` rendering section `Silk, lustrous satin and delicate sheer layers` with copy *"Shop occasion edit"*, asset references (`script.js`, `weglot_script_tag.js`, `storefrontattributes`, `trsdk`), and grid rule `.form-checkbox__label-text p { display:inline }`.
4. **Interactive Detail & Feature Matrix (<article.favorites-drawer__item:nth(3)> — `Search`)**:
   - Landmark `<article class="favorites-drawer__item">` framing `Search` and `Search Wishlist Cart 0` (*"Search Wishlist Cart 0"*) with `#f3f2f2` surface cards, `#0000ee` accents, and `.form-checkbox { width:100% }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://almadalabel.com/`)**:
   - Landmark `<footer class="footer colorGroup--primary">` anchoring `ALMADA LABEL - A modern take on ` footer links (`Journal · New Arrivals · Coming Soon · Gift Edit New · Occasion Edit New`), copy *"Autumn / Winter 26"*, and `#a6a6a5` structural dividers.
