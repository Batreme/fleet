---
title: "UI & UX Architecture: bespokegroup-io"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: bespokegroup-io

## Overview & Design Identity
- **Target**: `bespokegroup-io` (**Bespoke Group · Private Wealth & Estate Planning Advisory**)
- **Production URL**: [https://bespokegroup.io/](https://bespokegroup.io/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#ffa500` accent)
- **Summary**: Bespoke Group provides expert wealth management, estate planning, and advisory services for HNWIs and families. Tailored strategies for a...
- **Total Clean CSS Variables Extracted**: `23` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Booton`
- **Body Font Stack**: `Segoe UI`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 78px`, `line-height: 94px`, `font-weight: 300`, `letter-spacing: -1.56px`); rule `h1` (`font-size: 42px`, `line-height: 50px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 56px`, `line-height: 67px`, `font-weight: 300`, `letter-spacing: -1.12px`); rule `h2` (`letter-spacing: -.02em`, `font-weight: 300`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 18.4px`, `font-weight: 400`); rule `p` (`letter-spacing: 0`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 18.4px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `browser-default` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#fef7f3` | `var(--color-seashell)` in `:root` |
| **Interactive Accent / Highlight** | `#ffa500` | `.socialButton:hover { background: orange }` (`#ffa500`) |
| **Secondary / Muted Copy** | `#0000ee` | live computed `a` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#808080` | `.border-grey-300 { border-color: #808080 }` |
| **Variable Token (`--color-off-white`)** | `#f4f5f2` | `var(--color-off-white)` in `:root` |
| **Variable Token (`--color-grey-300`)** | `#cdcdcd` | `var(--color-grey-300)` in `:root` |
| **Variable Token (`--color-grey-400`)** | `#9c9c9c` | `var(--color-grey-400)` in `:root` |
| **Variable Token (`--color-grey-600`)** | `#636363` | `var(--color-grey-600)` in `:root` |
| **Variable Token (`--color-grey-700`)** | `#474747` | `var(--color-grey-700)` in `:root` |
| **Variable Token (`--color-grey-900`)** | `#2a2a2a` | `var(--color-grey-900)` in `:root` |
| **Variable Token (`--color-grey-1000`)** | `#0d0d0d` | `var(--color-grey-1000)` in `:root` |
| **Variable Token (`--color-off-black`)** | `#333333` | `var(--color-off-black)` in `:root` |
| **Variable Token (`--color-linen`)** | `#f7e9e0` | `var(--color-linen)` in `:root` |
| **Variable Token (`--color-champagne`)** | `#dac9be` | `var(--color-champagne)` in `:root` |
| **Variable Token (`--color-beige`)** | `#ebcfbc` | `var(--color-beige)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--cubic-easing` | `cubic-bezier(0.215,0.61,0.355,1)` | Motion / Easing Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--color-off-white` | `#f4f5f2` | Canvas / Surface Token |
| `--color-grey-300` | `#cdcdcd` | Brand / Palette Token |
| `--color-grey-400` | `#9c9c9c` | Brand / Palette Token |
| `--color-grey-500` | `grey` | Brand / Palette Token |
| `--color-grey-600` | `#636363` | Brand / Palette Token |
| `--color-grey-700` | `#474747` | Brand / Palette Token |
| `--color-grey-800` | `#474747` | Brand / Palette Token |
| `--color-grey-900` | `#2a2a2a` | Brand / Palette Token |
| `--color-grey-1000` | `#0d0d0d` | Brand / Palette Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-off-black` | `#333` | Canvas / Surface Token |
| `--color-linen` | `#f7e9e0` | Brand / Palette Token |
| `--color-champagne` | `#dac9be` | Brand / Palette Token |
| `--color-beige` | `#ebcfbc` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `bespokegroup-io`)**:
   - Landmark `<header class="header header--dark">` (`1440x93px`) hosting `Bespoke Group · Private Wealth & Est` navigation (`S e r v i c e s · A d v i s o r y · A b o u t · P e o p l e · R e s o u r c e s`), DOM attributes (`data-cfasync="false"`, `data-pagespeed-no-defer`, `data-cfasync="false"`, `data-cfasync="false"`), and stylesheet rule `.cfm-episodes-grid:before { content:"";display:table;clear:both }`.
2. **Hero Stage & Focal Lead (<section.acf_hero-scene> — `Bespoke Wealth Operating Systems`)**:
   - Landmark `<section class="acf_hero-scene">` presenting display lead `Bespoke Wealth Operating Systems` and copy excerpt *"Transformational philanthropy"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.acf_text-animation> — `Transform Chaos into Order`)**:
   - Landmark `<section class="acf_text-animation">` rendering section `Transform Chaos into Order` with copy *"Comprehensive Bitcoin wealth strategies"*, asset references (`gtm.js`, `www.googletagmanager.com`, `hero.home_.webp`, `logomark.png`), and grid rule `episodes-grid .cfm-episode-wrap:b... { content:"";display:table;clear:both }`.
4. **Interactive Detail & Feature Matrix (<article.acf_text-animation__content> — `We help the world’s most successfu`)**:
   - Landmark `<article class="acf_text-animation__content grid">` framing `We help the world’s most successful entrepreneurs...` and `Tailored and Integrated Wealth Systems` (*"Strengthen privacy in life and finance"*) with `#fef7f3` surface cards, `#ffa500` accents, and `d.cfm-episodes-cols-2 .cfm-episod... { width:50%;-webkit-box-flex:0;-ms-flex:0 1 50%;flex:0 1 50% }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://bespokegroup.io/`)**:
   - Landmark `<footer class="footer footer--no-newsletter">` anchoring `Bespoke Group · Private Wealth &` footer links (`S e r v i c e s · A d v i s o r y · A b o u t · P e o p l e · R e s o u r c e s`), copy *"Minimize and manage tax exposure"*, and `#808080` structural dividers.
