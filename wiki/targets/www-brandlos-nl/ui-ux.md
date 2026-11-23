---
title: "UI & UX Architecture: www-brandlos-nl"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-brandlos-nl

## Overview & Design Identity
- **Target**: `www-brandlos-nl` (**Brandlos · Het creatieve bureau van Limburg**)
- **Production URL**: [https://www.brandlos.nl](https://www.brandlos.nl)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f4f4f4` canvas, `#040404` ink, `#0082f3` accent)
- **Summary**: Creatief bureau in Limburg. Wij bouwen merken met lef en karakter: van strategie en identiteit tot campagnes die opvallen. Geen grijze mu...
- **Total Clean CSS Variables Extracted**: `11` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Vastagogrotesk`
- **Body Font Stack**: `Vastagogrotesk`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 74.88px`, `line-height: 104.832px`, `font-weight: 600`); rule `h1` (`font-size: 2em`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 54px`, `line-height: 70.2px`, `font-weight: 600`); rule `h2` (`font-size: 32px`, `line-height: 36px`)
- **Body Copy**: live computed `body` (`font-size: 14px`, `line-height: 18.2px`, `font-weight: 400`); rule `body` (`font-size: 14px`, `line-height: 20px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 14px`, `line-height: 18.2px`, `font-weight: 400`); rule `small` (`font-size: 80%`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f4f4f4` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#040404` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffff00` | `mark { background: #ffff00 }` |
| **Interactive Accent / Highlight** | `#0082f3` | `.w-dropdown-link.w--current { color: #0082f3 }` |
| **Secondary / Muted Copy** | `#0000ee` | live computed `a` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#e2e2e2` | `blockquote { border-left: #e2e2e2 }` |
| **Variable Token (`--_global-vars---accent-1`)** | `#fbd050` | `var(--_global-vars---accent-1)` in `:root` |
| **Variable Token (`--_global-vars---accent-2`)** | `#3a39ff` | `var(--_global-vars---accent-2)` in `:root` |
| **Variable Token (`--_global-vars---accent-5`)** | `#ff5b23` | `var(--_global-vars---accent-5)` in `:root` |
| **Variable Token (`--_global-vars---accent-3`)** | `#ade6ed` | `var(--_global-vars---accent-3)` in `:root` |
| **Variable Token (`--_global-vars---accent-4`)** | `#e9a2e4` | `var(--_global-vars---accent-4)` in `:root` |
| **Variable Token (`--_global-vars---grey`)** | `#b7b7b7` | `var(--_global-vars---grey)` in `:root` |
| **Variable Token (`--swiper-theme-color`)** | `#007aff` | `var(--swiper-theme-color)` in stylesheet |
| **Variable Token (`--swiper-preloader-color`)** | `#ffffff` | `var(--swiper-preloader-color)` in stylesheet |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--_global-vars---light` | `#f4f4f4` | Canvas / Surface Token |
| `--_global-vars---dark` | `#040404` | Canvas / Surface Token |
| `--_global-vars---accent-1` | `#fbd050` | Brand / Palette Token |
| `--_global-vars---accent-2` | `#3a39ff` | Brand / Palette Token |
| `--_global-vars---accent-5` | `#ff5b23` | Brand / Palette Token |
| `--_global-vars---accent-3` | `#ade6ed` | Brand / Palette Token |
| `--_global-vars---accent-4` | `#e9a2e4` | Brand / Palette Token |
| `--_global-vars---grey` | `#b7b7b7` | Color / Atmospheric Token |
| `--w-backdrop-animation` | `initial` | Motion / Easing Token |
| `--underline-scale` | `1` | Design System Custom Token |
| `--pt-color` | `#fbd050` | Brand / Palette Token |
| `--swiper-theme-color` | `#007aff` | Brand / Palette Token |
| `--swiper-preloader-color` | `#fff` | Brand / Palette Token |
| `--swiper-navigation-size` | `44px` | Layout / Spatial Grid Token |
| `--www-brandlos-nl-bg` | `#f4f4f4` | Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) |
| `--www-brandlos-nl-ink` | `#040404` | Primary Typography Ink (computed-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.w-mod-js> — `www-brandlos-nl`)**:
   - Landmark `<header class="w-mod-js">` (`1440px`) hosting `Brandlos · Het creatieve bureau van ` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-wf-domain="www.brandlos.nl"`, `data-wf-page="6a60a2741f0d39e46e0880df"`, `data-wf-site="6a60a2731f0d39e46e0880dc"`, `data-nosnippet`), and stylesheet rule `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`.
2. **Hero Stage & Focal Lead (<section.home-hero> — `Omdat gewoon te gewoontjes is`)**:
   - Landmark `<section class="home-hero">` presenting display lead `Omdat gewoon te gewoontjes is` and copy excerpt *"Grijze muizen zijn er al genoeg. Wij bouwen merken met lef, karak"* over `#f4f4f4` canvas and `#040404` ink.
3. **Primary Showcase & Content Grid (<section.home-showreel> — `Grijze muizen zijn er al genoeg. W`)**:
   - Landmark `<section class="home-showreel">` rendering section `Grijze muizen zijn er al genoeg. Wij bouwen merk` with copy *"L a a t m a a r e e n s z i e n d a n !"*, asset references (`cdn.prod.website-files.com`, `brandlos-nl.webflow.shared.3ea0ad...`, `widgetIcon.min.js`, `state.js`), and grid rule `body { margin: 0; }`.
4. **Interactive Detail & Feature Matrix (<section.home-about> — `L a a t m a a r e e n s z i e n d `)**:
   - Landmark `<section class="home-about">` framing `L a a t m a a r e e n s z i e n d a n !` and `Wij zijn Brandlos®. Een creatief bureau in Limbu` (*"Wij zijn Brandlos®. Een creatief bureau in Limburg. We gaan altij"*) with `#ffff00` surface cards, `#0082f3` accents, and `summary { display: block; }`.
5. **Colophon & Global Directory Footer (<footer.CybotCookiebotScrollAreaSide> — `https://www.brandlos.nl`)**:
   - Landmark `<footer class="CybotCookiebotScrollAreaSide">` anchoring `Brandlos · Het creatieve bureau ` footer links (`Overview · Index · Archive · About · Contact`), copy *"T e l l m e m o o o o o o r e"*, and `#e2e2e2` structural dividers.
