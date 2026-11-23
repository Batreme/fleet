---
title: "UI & UX Architecture: key-co"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: key-co

## Overview & Design Identity
- **Target**: `key-co` (**KEY.co · Luxury Vacation Home Rentals + Concierge Services**)
- **Production URL**: [https://key.co/](https://key.co/)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#020817` ink, `#1a73e8` accent)
- **Summary**: Find your perfect getaway with KEY.co. Explore curated vacation homes with in-home services like pre-arrival groceries and private chefs.
- **Total Clean CSS Variables Extracted**: `2` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `adobe-caslon-pro`
- **Body Font Stack**: `proxima-nova`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 72px`, `line-height: 92px`, `font-weight: 400`, `letter-spacing: -1.44px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 32px`, `line-height: 40px`, `font-weight: 400`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#020817` | live computed `body` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#fbf9f2` | live computed `footer` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#1a73e8` | `.hSRGPd { color: #1a73e8 }` |
| **Secondary / Muted Copy** | `#1a73e8` | `.hSRGPd { color: #1a73e8 }` |
| **Structural Hairline Border** | `#4285f4` | `.fFW7wc-ibnC6b>.aZ2wEe>div { border-color: #4285f4 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-geist-sans` | `'GeistSans', 'GeistSans Fallback'` | Typography / Scale Token |
| `--top-banner-height` | `41px` | Layout / Spatial Grid Token |
| `--key-co-bg` | `#ffffff` | Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) |
| `--key-co-ink` | `#020817` | Primary Typography Ink (computed-derived) |
| `--key-co-surface` | `#fbf9f2` | Surface Substrate (computed-derived) |
| `--key-co-accent` | `#1a73e8` | Interactive Accent (computed-derived) |
| `--key-co-muted` | `#1a73e8` | Secondary Ink (computed-derived) |
| `--key-co-border` | `#4285f4` | Structural Border (computed-derived) |
| `--key-co-container` | `1440px` | Container Bound (computed-derived) |
| `--key-co-gap` | `0px` | Grid Gutter (computed-derived) |
| `--key-co-pad` | `10px` | Lateral Padding (computed-derived) |
| `--key-co-ease` | `cubic-bezier(0.25,0.1,0.25,1)` | Primary Easing Function |
| `--key-co-radius` | `1.2px` | Corner Radius (computed-derived) |
| `--key-co-fs-base` | `72px` | Observed Font Size Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.max-w-max> — `key-co`)**:
   - Landmark `<nav class="max-w-max flex-1">` (`1120x68px`) hosting `KEY.co · Luxury Vacation Home Rental` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-theme="light"`), and stylesheet rule `.tk-proxima-nova { font-family: "proxima-nova",sans-serif; }`.
2. **Hero Stage & Focal Lead (<section.navbar-section> — `Pack your bags, we’ll do the rest`)**:
   - Landmark `<section class="navbar-section">` presenting display lead `Pack your bags, we’ll do the rest` and copy excerpt *"$500 off $10k+ stays w/ HOLIDAYSAREHERE - ends 12/31"* over `#ffffff` canvas and `#020817` ink.
3. **Primary Showcase & Content Grid (<article.wf-proximanova-n4-active> — `$500 off $10k+ stays w/ HOLIDAYSAR`)**:
   - Landmark `<article class="wf-proximanova-n4-active">` rendering section `$500 off $10k+ stays w/ HOLIDAYSAREHERE - ends 1` with copy *"Curated Vacation Homes + Luxury Services"*, asset references (`oaiq.min.js`, `283498678855975`, `fbevents.js`, `gtm.js`), and grid rule `.tk-adobe-caslon-pro { font-family: "adobe-caslon-pro",serif; }`.
4. **Interactive Detail & Feature Matrix (<section.video-fit> — `Curated Vacation Homes + Luxury Se`)**:
   - Landmark `<section class="video-fit no-gsap-animation">` framing `Curated Vacation Homes + Luxury Services` and `Explore our selection of premium homes—each chos` (*"Explore our selection of premium homes—each chosen for style, com"*) with `#fbf9f2` surface cards, `#1a73e8` accents, and `.tk-futura-pt { font-family: "futura-pt",sans-serif; }`.
5. **Colophon & Global Directory Footer (<footer.bg-brand-beige> — `https://key.co/`)**:
   - Landmark `<footer class="bg-brand-beige">` anchoring `KEY.co · Luxury Vacation Home Re` footer links (`Overview · Index · Archive · About · Contact`), copy *"Professionally managed and vetted for comfort and style, our"*, and `#4285f4` structural dividers.
