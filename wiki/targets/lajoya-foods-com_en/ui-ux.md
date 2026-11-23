---
title: "UI & UX Architecture: lajoya-foods-com_en"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: lajoya-foods-com_en

## Overview & Design Identity
- **Target**: `lajoya-foods-com_en` (**LAJOYA GOURMET**)
- **Production URL**: [https://lajoya-foods.com/en](https://lajoya-foods.com/en)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#00ef84` / `#ea3323`)
- **Summary**: Optimal preservation of porcelain interior
- **Total Clean CSS Variables Extracted**: `13` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Ambiant Light Sans`
- **Body Font Stack**: `Maison Neue`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 68px`, `line-height: 68px`, `font-weight: 400`, `letter-spacing: -1.5px`)
- **Section Heading (`H2`)**: live computed `h3 (primary section heading)` (`font-size: 68px`, `line-height: 48px`, `font-weight: 400`)
- **Body Copy**: live computed `body` (`font-size: 10px`, `line-height: 10px`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 68px`, `line-height: 68px`, `font-weight: 400`, `letter-spacing: -1.5px`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#00ef84` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `var(--background-color)` in `:root` |
| **Interactive Accent / Highlight** | `#ea3323` | `.header__button-cart-quantity { background-color: #ea3323 }` |
| **Secondary / Muted Copy** | `#ea3323` | `var(--color-secondary)` in `:root` |
| **Structural Hairline Border** | `#ffffff` | `on.loading>.loading-overlay__sp... { stroke: #ffffff }` |
| **Variable Token (`--color-tertiary`)** | `#ffff54` | `var(--color-tertiary)` in `:root` |
| **Variable Token (`--swiper-theme-color`)** | `#007aff` | `var(--swiper-theme-color)` in stylesheet |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-primary` | `#00EF84` | Brand / Palette Token |
| `--color-secondary` | `#EA3323` | Brand / Palette Token |
| `--color-tertiary` | `#FFFF54` | Brand / Palette Token |
| `--font-primary` | `"Maison Neue"` | Brand / Palette Token |
| `--font-support` | `"Ambiant Light Spiky"` | Typography / Scale Token |
| `--font-support-s` | `"Ambiant Light Sans"` | Typography / Scale Token |
| `--text-reveal-bleed` | `.2em` | Typography Ink Token |
| `--space` | `4vw` | Layout / Spatial Grid Token |
| `--star-direction` | `reverse` | Design System Custom Token |
| `--height` | `790` | Layout / Spatial Grid Token |
| `--background` | `#ea3323` | Canvas / Surface Token |
| `--text-color` | `#000000` | Typography Ink Token |
| `--background-color` | `#ffffff` | Canvas / Surface Token |
| `--swiper-theme-color` | `#007aff` | Brand / Palette Token |
| `--lajoya-foods-com-bg` | `#00ef84` | Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) |
| `--lajoya-foods-com-ink` | `#000000` | Primary Typography Ink (computed-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `lajoya-foods-com_en`)**:
   - Landmark `<header class="header">` (`1440x92px`) hosting `LAJOYA GOURMET` navigation (`Contact · About · Shop · Shop Shop`), DOM attributes (`data-source-attribution="shopify.exit_intersti..."`, `data-shop-id="57685803183"`, `data-venmo-supported="false"`, `data-environment="production"`), and stylesheet rule `root { --swiper-theme-color:007aff }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Lajoya Gourmet`)**:
   - Landmark `<section class="hero">` presenting display lead `Lajoya Gourmet` and copy excerpt *"Chopped Peeled Tomato"* over `#00ef84` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.tiles> — `Chopped Peeled Tomato Chopped Peel`)**:
   - Landmark `<section class="tiles">` rendering section `Chopped Peeled Tomato Chopped Peeled Tomato Chopp...` with copy *"Whole Peeled Tomato"*, asset references (`171ed732002c6631efbca8f91.js`, `klaviyo.js`, `1349771745561073`, `fbevents.js`), and grid rule `host { position:relative;display:block;margin-left:auto;margin-right:auto;z-ind... }`.
4. **Interactive Detail & Feature Matrix (<section.tiles:nth(2)> — `Whole Peeled Tomato Whole Peeled T`)**:
   - Landmark `<section class="tiles">` framing `Whole Peeled Tomato Whole Peeled Tomato Whole Pee...` and `Artichoke Hearts Artichoke Hearts Artichoke Heart...` (*"Optimal preservation of porcelain interior"*) with `#ffffff` surface cards, `#ea3323` accents, and `.swiper { margin-left:auto;margin-right:auto;position:relative;overflow:hidden;lis... }`.
5. **Colophon & Global Directory Footer (<footer.header--mobile> — `https://lajoya-foods.com/en`)**:
   - Landmark `<footer class="header--mobile">` anchoring `LAJOYA GOURMET` footer links (`Contact · About · Shop · Shop Shop`), copy *"Extra virgin olive oil"*, and `#ffffff` structural dividers.
