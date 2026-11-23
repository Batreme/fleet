---
title: "UI & UX Architecture: www-anduril-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-anduril-com

## Overview & Design Identity
- **Target**: `www-anduril-com` (**Transforming U.S. Defense Capabilities with Advanced Technology · Anduril**)
- **Production URL**: [https://www.anduril.com/](https://www.anduril.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#ff3535`)
- **Summary**: Anduril Industries builds advanced autonomous systems and defense technology to protect US and allied forces. Creating the future of nati...
- **Total Clean CSS Variables Extracted**: `30` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `HelveticaNowDisplay`
- **Body Font Stack**: `Elios`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 12px`, `line-height: 12.6px`, `font-weight: 500`, `letter-spacing: 0.48px`); rule `.title` (`font-size: 3rem`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 24px`, `line-height: 27.6px`, `font-weight: 700`, `letter-spacing: -0.24px`); rule `h2` (`font-size: 8.75rem`, `line-height: 95%`, `letter-spacing: -.0875rem`, `font-weight: 500`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: 1.5rem`, `line-height: 115%`, `letter-spacing: -.015rem`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `.label` (`font-size: .75rem`, `line-height: 105%`, `letter-spacing: .03rem`, `font-weight: 500`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#010101` | `var(--theme-color-background)` in `:root` |
| **Interactive Accent / Highlight** | `#ff3535` | `FormInput.FormInput .errorMessa... { color: #ff3535 }` |
| **Secondary / Muted Copy** | `#010101` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#010101` | `.AlgoliaPagination .next { border: #010101 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--is-mob` | `0` | Design System Custom Token |
| `--theme-color-background` | `#010101` | Canvas / Surface Token |
| `--theme-color-text` | `#fff` | Typography Ink Token |
| `--base-color` | `black` | Brand / Palette Token |
| `--contrast-color` | `white` | Brand / Palette Token |
| `--linkbutton-color` | `#fff` | Typography Ink Token |
| `--linkbutton-hover-color` | `#010101` | Typography Ink Token |
| `--roller-scale` | `1` | Motion / Easing Token |
| `--roller-font-size` | `calc(3rem*var(--roller-scale))` | Typography / Scale Token |
| `--roller-column-height` | `calc(2.5rem*var(--roller-scale))` | Layout / Spatial Grid Token |
| `--roller-digit-width` | `calc(1.8rem*var(--roller-scale))` | Layout / Spatial Grid Token |
| `--links-height` | `0px` | Typography Ink Token |
| `--frosted` | `0` | Design System Custom Token |
| `--backgroundOpacity` | `0` | Canvas / Surface Token |
| `--in-production-h` | `max(505px,100vw*505/403)` | Dimension / Scale Token |
| `--focus-ring-color` | `currentColor` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.header> — `www-anduril-com`)**:
   - Landmark `<header class="header">` (`1440px`) hosting `Transforming U.S. Defense Capabiliti` navigation (`Anduril Logo · Subterranean · Space · Arsenal · Seapower`), DOM attributes (`data-path="/"`, `data-path="subterranean/future-s..."`, `data-label="Subterranean"`, `data-domain="Sea"`), and stylesheet rule `root { --is-mob:0 }`.
2. **Hero Stage & Focal Lead (<main.GLA11y> — `@[shortTitle]`)**:
   - Landmark `<main class="GLA11y">` presenting display lead `@[shortTitle]` and copy excerpt *"Anduril, U.S. Navy Invest $6.6 Billion to Expand America's Submar"* over `#000000` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<main.Header> — `@[title]`)**:
   - Landmark `<main class="Header">` rendering section `@[title]` with copy *"Please enable javascript"*, asset references (`feed.xml`, `favicon.xxWKiVhdqu.ico`, `favicon.xxQR7xb3fo.svg`, `apple-touch-icon.xxx1TpF2gg.png`), and grid rule `Stage { width:100%;height:100%;margin:0;padding:0;overflow-x:clip }`.
4. **Interactive Detail & Feature Matrix (<main.HeaderDesktop> — `Please enable javascript`)**:
   - Landmark `<main class="HeaderDesktop">` framing `Please enable javascript` and `Tactical Reconnaissance & Strike` (*"Tactical Reconnaissance & Strike"*) with `#010101` surface cards, `#ff3535` accents, and `html { scrollbar-gutter:stable }`.
5. **Colophon & Global Directory Footer (<footer.Footer> — `https://www.anduril.com/`)**:
   - Landmark `<footer class="Footer">` anchoring `Transforming U.S. Defense Capabi` footer links (`Anduril Logo · Subterranean · Space · Arsenal · Seapower`), copy *"Air Dominance & Strike"*, and `#010101` structural dividers.
