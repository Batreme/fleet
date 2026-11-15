# UI & UX Architecture: www-terrenohotel-com_en

## Overview & Design Identity
- **Target**: `www-terrenohotel-com_en` (**Terreno Barrio Hotel · Boutique hotel in Palma de Mallorca**)
- **Production URL**: [https://www.terrenohotel.com/en/](https://www.terrenohotel.com/en/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ecffb3` canvas, `#570007` ink, `#fff` accent)
- **Summary**: Boutique hotel in Palma de Mallorca with Mediterranean design, local character, rooftop moments and direct booking benefits on the offici...
- **Total Clean CSS Variables Extracted**: `492` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `PP Monument Extended`
- **Body Font Stack**: `Tiempos Text`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `.title` (`font-size: 3.6rem`, `line-height: 3.6rem`, `letter-spacing: 2.4%`, `font-weight: 700`)
- **Section Heading (`H2`)**: CSS variables `--subtitle-fs: 1.8rem`, `--subtitle-lh: 2.6rem`, `--subtitle-g: 0.8rem`
- **Body Copy**: CSS variables `--mirai-ui-font-size-paragraph: 16px`, `--mirai-ui-line-height-paragraph: 20px`, `--experiencias-body-bg: #ecffb3`; rule `body` (`font-weight: 400`)
- **Metadata & Labels**: CSS variables `--mirai-ui-font-size-small: 12px`, `--mirai-ui-line-height-small: 16px`, `--mirai-ui-button-small-height: calc(var(--mirai-ui-space-XL) - var(--mirai-ui-space-M))`; rule `small` (`font-size: 12px`, `line-height: 14px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#ecffb3` | `var(--hover-c)` in `:root` |
| **Primary Typography Ink** | `#570007` | `var(--home-active-color)` in `:root` |
| **Elevated Surface / Card Substrate** | `#334155` | `var(--fancybox-color)` in `:root` |
| **Interactive Accent / Highlight** | `#fff` | `var(--fancybox-bg)` in `:root` |
| **Secondary / Muted Copy** | `#6b7280` | `var(--fancybox-content-color)` in `:root` |
| **Structural Hairline Border** | `#e5e7eb` | `var(--carousel-button-bg)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--icon-w` | `1.6rem` | Dimension / Scale Token |
| `--px` | `1rem` | Dimension / Scale Token |
| `--bg-c` | `transparent` | Canvas / Surface Token |
| `--border-c` | `var(--c)` | Elevation / Border Token |
| `--hover-c` | `#ecffb3` | Color / Atmospheric Token |
| `--gap` | `0.8rem` | Layout / Spatial Grid Token |
| `--hover-bg-c` | `var(--c)` | Canvas / Surface Token |
| `--size` | `4rem` | Layout / Spatial Grid Token |
| `--home-active-bg` | `#ecffb3` | Canvas / Surface Token |
| `--home-active-color` | `#570007` | Brand / Palette Token |
| `--home-active-altcolor` | `#ecffb3` | Brand / Palette Token |
| `--current-scheme-color` | `var(--home-active-color)` | Brand / Palette Token |
| `--current-scheme-bgcolor` | `var(--home-active-bg)` | Canvas / Surface Token |
| `--current-scheme-altcolor` | `var(--home-active-altcolor)` | Brand / Palette Token |
| `--home-cta-overlap` | `18rem` | Brand / Palette Token |
| `--home-rotate-progress` | `0` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.mdl-header> — `www-terrenohotel-com_en`)**:
   - Landmark `<header class="mdl-header color-scheme-burgundy">` hosting `Terreno Barrio Hotel · Boutique hote` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-mirai-id="100380929"`, `data-type="hotel"`, `data-role="view"`, `data-title="Header"`), and stylesheet rule `root { --swiper-theme-color:007aff }`.
2. **Hero Stage & Focal Lead (<section.m-experiencias> — `a hotel with a neighborhood soul`)**:
   - Landmark `<section class="m-experiencias color-scheme-burgundy">` presenting display lead `a hotel with a neighborhood soul` and copy excerpt *"LIVE BARRIO AGENDA SPA"* over `#ecffb3` canvas and `#570007` ink.
3. **Primary Showcase & Content Grid (<article.e-slide> — `TERRENO IS PART OF THE NEIGHBOURHO`)**:
   - Landmark `<article class="e-slide swiper-slide">` rendering section `TERRENO IS PART OF THE NEIGHBOURHOOD. THE NEIGHBO...` with copy *"DRINK EL TERRADO Club"*, asset references (`favicon-ios-7f1277496f8279e6f805a...`, `favicon-ios-3a0235b9e158e0432cb3d...`, `ed9704c669f04d459f5fd2ad1e298a56.js`, `gtm.js`), and grid rule `host { display:block;margin-left:auto;margin-right:auto;position:relative;z-ind... }`.
4. **Interactive Detail & Feature Matrix (<article.e-slide> — `OUR ROOMS`)**:
   - Landmark `<article class="e-slide swiper-slide">` framing `OUR ROOMS` and `THE PLACE TO STAY` (*"24 HOURS IN TERRENO"*) with `#334155` surface cards, `#fff` accents, and `.swiper { display:block;list-style:none;margin-left:auto;margin-right:auto;overflo... }`.
5. **Colophon & Global Directory Footer (<footer.module-footer> — `https://www.terrenohotel.com/en/`)**:
   - Landmark `<footer class="module-footer">` anchoring `Terreno Barrio Hotel · Boutique ` footer links (`Overview · Index · Archive · About · Contact`), copy *"descubre 24h en el barrio"*, and `#e5e7eb` structural dividers.
