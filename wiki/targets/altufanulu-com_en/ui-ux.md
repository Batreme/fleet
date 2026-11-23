---
title: "UI & UX Architecture: altufanulu-com_en"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: altufanulu-com_en

## Overview & Design Identity
- **Target**: `altufanulu-com_en` (**Altufan Ulu Law Office · Istanbul Legal Counsel**)
- **Production URL**: [https://altufanulu.com/en/](https://altufanulu.com/en/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#0000ee` accent)
- **Summary**: Altufan Ulu Law Office provides trusted, fast and strategic legal services in Istanbul. Expert counsel across corporate, employment, IP,...
- **Total Clean CSS Variables Extracted**: `6` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Victor Serif`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 70px`, `line-height: 77px`, `font-weight: 400`); rule `h1` (`font-size: 5rem`, `line-height: 1.1`, `font-weight: 300`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 24px`, `line-height: normal`, `font-weight: 500`, `letter-spacing: -0.48px`); rule `h2` (`font-size: 2.4rem`, `letter-spacing: -.02em`, `font-weight: 500`)
- **Body Copy**: live computed `body` (`font-size: 10px`, `line-height: normal`, `font-weight: 400`); rule `p` (`line-height: 1.75`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 10px`, `line-height: normal`, `font-weight: 400`); rule `small` (`font-size: 2rem`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `browser-default` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f6f6f6` | live computed `footer` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#0000ee` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#0000ee` | live computed `a` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#edeef1` | `.au-pub-card__author { border-right: #edeef1 }` |
| **Variable Token (`--bg-blue`)** | `#050a34` | `var(--bg-blue)` in `:root` |
| **Variable Token (`--bg-grey`)** | `#f4f4f5` | `var(--bg-grey)` in `:root` |
| **Variable Token (`--bg`)** | `#fdfaf6` | `var(--bg)` in `:root` |
| **Variable Token (`--bg-green-1`)** | `#263a05` | `var(--bg-green-1)` in `:root` |
| **Variable Token (`--bg-green-2`)** | `#003726` | `var(--bg-green-2)` in `:root` |
| **Variable Token (`--swiper-theme-color`)** | `#007aff` | `var(--swiper-theme-color)` in stylesheet |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--white` | `#fff` | Canvas / Surface Token |
| `--bg-blue` | `#050a34` | Canvas / Surface Token |
| `--bg-grey` | `#f4f4f5` | Canvas / Surface Token |
| `--bg` | `#fdfaf6` | Canvas / Surface Token |
| `--bg-green-1` | `#263a05` | Canvas / Surface Token |
| `--bg-green-2` | `#003726` | Canvas / Surface Token |
| `--swiper-theme-color` | `#007aff` | Brand / Palette Token |
| `--swiper-navigation-size` | `44px` | Layout / Spatial Grid Token |
| `--swiper-preloader-color` | `#fff` | Brand / Palette Token |
| `--altufanulu-com-e-bg` | `#ffffff` | Canvas Substrate (from live computed `browser-default` `background-color` (`computed_styles.json`)) |
| `--altufanulu-com-e-ink` | `#000000` | Primary Typography Ink (computed-derived) |
| `--altufanulu-com-e-surface` | `#f6f6f6` | Surface Substrate (computed-derived) |
| `--altufanulu-com-e-accent` | `#0000ee` | Interactive Accent (computed-derived) |
| `--altufanulu-com-e-muted` | `#0000ee` | Secondary Ink (computed-derived) |
| `--altufanulu-com-e-border` | `#edeef1` | Structural Border (computed-derived) |
| `--altufanulu-com-e-container` | `107rem` | Container Bound (computed-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.scrollUp> — `altufanulu-com_en`)**:
   - Landmark `<header class="scrollUp">` (`1440x130px`) hosting `Altufan Ulu Law Office · Istanbul Le` navigation (`HOME · ABOUT US · PRACTICE AREAS · SECTORS · CAREER`), DOM attributes (`data-optimized="1"`, `data-optimized="1"`, `data-no-transition`, `data-barba="wrapper"`), and stylesheet rule `root { font-size:10px!important }`.
2. **Hero Stage & Focal Lead (<section.hero-content> — `Trusted, fast and strategic legal `)**:
   - Landmark `<section class="hero-content">` presenting display lead `Trusted, fast and strategic legal services.` and copy excerpt *"We give every case the focus it deserves. When needed, we bring t"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.padding> — `WHY ALTUFAN ULU?`)**:
   - Landmark `<section class="padding">` rendering section `WHY ALTUFAN ULU?` with copy *"Learn more about our approach to legal matters, our working philo"*, asset references (`apple-touch-icon.png`, `favicon-32x32.png`, `favicon-16x16.png`, `site.webmanifest`), and grid rule `pre { margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.padding:nth(2)> — `BOUTIQUE STRUCTURE, INDEPENDENT AP`)**:
   - Landmark `<section class="padding">` framing `BOUTIQUE STRUCTURE, INDEPENDENT APPROACH` and `STRATEGIC SOLUTIONS` (*"Legal matters are approached with foresight, analysis and a disci"*) with `#f6f6f6` surface cards, `#0000ee` accents, and `img { max-width:100%;height:auto }`.
5. **Colophon & Global Directory Footer (<footer.page-template-page-en-home> — `https://altufanulu.com/en/`)**:
   - Landmark `<footer class="page-template-page-en-home">` anchoring `Altufan Ulu Law Office · Istanbu` footer links (`HOME · ABOUT US · PRACTICE AREAS · SECTORS · CAREER`), copy *"01 BOUTIQUE STRUCTURE, INDEPENDENT APPROACH We give every ca"*, and `#edeef1` structural dividers.
