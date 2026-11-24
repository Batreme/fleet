---
title: "UI & UX Architecture: www-terrenohotel-com_en"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-terrenohotel-com_en

## Overview & Design Identity
- **Target**: `www-terrenohotel-com_en` (**Terreno Barrio Hotel · Boutique hotel in Palma de Mallorca**)
- **Production URL**: [https://www.terrenohotel.com/en/](https://www.terrenohotel.com/en/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ecffb3` canvas, `#570007` ink, `#cc3224` accent)
- **Summary**: Boutique hotel in Palma de Mallorca with Mediterranean design, local character, rooftop moments and direct booking benefits on the offici...
- **Total Clean CSS Variables Extracted**: `513` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `WT Central Avenue`
- **Body Font Stack**: `Tiempos Text`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 68px`, `line-height: 60px`, `font-weight: 700`); rule `.title` (`font-size: 3.6rem`, `line-height: 3.6rem`, `letter-spacing: 2.4%`, `font-weight: 700`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 68px`, `line-height: 60px`, `font-weight: 700`); CSS variables `--subtitle-fs: 1.8rem`, `--subtitle-lh: 2.6rem`, `--subtitle-g: 0.8rem`
- **Body Copy**: live computed `body` (`font-size: 10px`, `line-height: normal`, `font-weight: 400`); CSS variables `--mirai-ui-font-size-paragraph: 16px`, `--mirai-ui-line-height-paragraph: 20px`; rule `body` (`font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 10px`, `line-height: normal`, `font-weight: 400`); CSS variables `--mirai-ui-font-size-small: 12px`, `--mirai-ui-line-height-small: 16px`, `--mirai-ui-button-small-height: calc(var(--mirai-ui-space-XL) - var(--mirai-ui-space-M))`; rule `small` (`font-size: 12px`, `line-height: 14px`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ecffb3` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#570007` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f6f6f6` | `var(--mirai-ui-content-background)` in `:root` |
| **Interactive Accent / Highlight** | `#cc3224` | `.cookiescript_vendor_name a:hover { color: #cc3224 }` |
| **Secondary / Muted Copy** | `#7d7e81` | `#capacalendario .cabeceracal .n... { color: #7d7e81 }` |
| **Structural Hairline Border** | `#dddddd` | `var(--mirai-ui-content-border)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--mirai-ui-font-weight` | `400` | Typography / Scale Token |
| `--mirai-ui-font-medium` | `var(--mirai-ui-font)` | Typography / Scale Token |
| `--mirai-ui-font-medium-weight` | `500` | Typography / Scale Token |
| `--mirai-ui-font-bold` | `var(--mirai-ui-font)` | Typography / Scale Token |
| `--mirai-ui-font-bold-weight` | `700` | Typography / Scale Token |
| `--mirai-ui-font-size-headline-1` | `32px` | Typography / Scale Token |
| `--mirai-ui-line-height-headline-1` | `40px` | Typography / Scale Token |
| `--mirai-ui-font-size-headline-2` | `24px` | Typography / Scale Token |
| `--mirai-ui-line-height-headline-2` | `32px` | Typography / Scale Token |
| `--mirai-ui-font-size-headline-3` | `20px` | Typography / Scale Token |
| `--mirai-ui-line-height-headline-3` | `24px` | Typography / Scale Token |
| `--mirai-ui-font-size-paragraph` | `16px` | Typography / Scale Token |
| `--mirai-ui-line-height-paragraph` | `20px` | Typography / Scale Token |
| `--mirai-ui-font-size-action` | `14px` | Typography / Scale Token |
| `--mirai-ui-line-height-action` | `18px` | Typography / Scale Token |
| `--mirai-ui-font-size-small` | `12px` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Persistent Left Sidebar Navigation (<aside.e-intro> — `280×752px` at `x=32`)**:
   - Fixed/sticky left rail `<aside class="e-intro">` (`280px` wide) paired with top bar `<header class="mdl-header color-scheme-burgundy">` hosting `Terreno Barrio Hotel · Boutiqu` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-ueto="ueto_d4a75505ed"`, `data-mirai-id="100380929"`, `data-type="hotel"`, `data-title="Header"`), and rule `._3qK-PW_checkbox { position:relative }`.
2. **Hero Stage & Focal Lead (<section.m-experiencias> — `A HOTEL WITH A NEIGHBORHOOD SOUL`)**:
   - Landmark `<section class="m-experiencias color-scheme-burgundy">` inside `1440px` main stage presenting display lead `A HOTEL WITH A NEIGHBORHOOD SOUL` and copy excerpt *"Some neighbourhoods have something you can’t quite put your finge"* over `#ecffb3` canvas and `#570007` ink.
3. **Primary Showcase & Content Grid (<article.e-slide> — `a hotel with a neighborhood soul`)**:
   - Landmark `<article class="e-slide swiper-slide">` rendering section `a hotel with a neighborhood soul` with copy *"LIVE BARRIO AGENDA SPA"*, asset references (`favicon-ios-7f1277496f8279e6f805a...`, `favicon-ios-3a0235b9e158e0432cb3d...`, `clientParamBuilder.bundle.js`, `0.8.77`), and grid rule `._3qK-PW_checkbox input:disabled { border-color:var(--mirai-ui-checkbox-background-disabled) }`.
4. **Interactive Detail & Feature Matrix (<article.swiper-slide> — `TERRENO IS PART OF THE NEIGHBOURHO`)**:
   - Landmark `<article class="e-slide swiper-slide">` framing `TERRENO IS PART OF THE NEIGHBOURHOOD. THE NEIGHBO...` and `THE PLACE TO STAY` (*"DRINK EL TERRADO Club"*) with `#f6f6f6` surface cards, `#cc3224` accents, and `checkbox input:disabled._3qK-PW_c... { background-color:var(--mirai-ui-checkbox-background-disabled) }`.
5. **Colophon & Global Directory Footer (<footer.module-footer> — `https://www.terrenohotel.com/en/`)**:
   - Landmark `<footer class="module-footer">` anchoring `Terreno Barrio Hotel · Boutique ` footer links (`Overview · Index · Archive · About · Contact`), copy *"24 HOURS IN TERRENO"*, and `#dddddd` structural dividers.
