---
title: "UI & UX Architecture: www-mbidirectmail-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-mbidirectmail-com

## Overview & Design Identity
- **Target**: `www-mbidirectmail-com` (**Direct Mail & Digital Marketing · Customer Acquisition · MBI**)
- **Production URL**: [https://www.mbidirectmail.com/](https://www.mbidirectmail.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×844px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#06070a` / `#ff0000`)
- **Summary**: MBI Direct Mail + Digital helps businesses find, reach, and win new customers: direct mail, print, digital, and seminar marketing from on...
- **Total Clean CSS Variables Extracted**: `137` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 24.0005px`, `line-height: 33.6007px`, `font-weight: 300`, `letter-spacing: 1.20002px`); rule `h1` (`font-size: 22px`, `line-height: 1.25`, `letter-spacing: .05em`, `font-weight: 400`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 34.56px`, `line-height: 38.7072px`, `font-weight: 200`, `letter-spacing: -0.62208px`); rule `h2` (`font-size: clamp(38px,11.6vw,48px)`, `line-height: 1.0`, `letter-spacing: -.035em`, `font-weight: 100`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `.body` (`font-size: 18px`, `line-height: 1.55`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#06070a` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `button` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#151515` | live computed `a` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#ff0000` | `#campaign-report .cr-delta.down { color: red }` (`#ff0000`) |
| **Secondary / Muted Copy** | `#6b7689` | `var(--cr-ink-soft)` in `:root` |
| **Structural Hairline Border** | `#1f2022` | `var(--line)` in `:root` (`rgba(255,255,255,0.10)`) |
| **Variable Token (`--surface`)** | `#111113` | `var(--surface)` in `:root` |
| **Variable Token (`--surface-soft`)** | `#1c1c20` | `var(--surface-soft)` in `:root` |
| **Variable Token (`--ink`)** | `#f0f0f2` | `var(--ink)` in `:root` |
| **Variable Token (`--muted`)** | `#6e6e78` | `var(--muted)` in `:root` |
| **Variable Token (`--honey`)** | `#9a9aa2` | `var(--honey)` in `:root` |
| **Variable Token (`--honey-bright`)** | `#c8c8d0` | `var(--honey-bright)` in `:root` |
| **Variable Token (`--honey-deep`)** | `#5a5a62` | `var(--honey-deep)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bg` | `#06070A` | Canvas / Surface Token |
| `--surface` | `#111113` | Canvas / Surface Token |
| `--surface-soft` | `#1c1c20` | Canvas / Surface Token |
| `--ink` | `#f0f0f2` | Typography Ink Token |
| `--muted` | `#6e6e78` | Color / Atmospheric Token |
| `--line` | `rgba(255,255,255,0.10)` | Color / Atmospheric Token |
| `--tunnel-line` | `rgba(255,255,255,0.12)` | Color / Atmospheric Token |
| `--tunnel-line-strong` | `rgba(255,255,255,0.18)` | Color / Atmospheric Token |
| `--tunnel-line-soft` | `rgba(255,255,255,0.04)` | Color / Atmospheric Token |
| `--tunnel-glow` | `rgba(255,255,255,0.10)` | Color / Atmospheric Token |
| `--honey` | `#9a9aa2` | Color / Atmospheric Token |
| `--honey-bright` | `#c8c8d0` | Color / Atmospheric Token |
| `--honey-deep` | `#5a5a62` | Color / Atmospheric Token |
| `--honey-soft` | `rgba(255,255,255,0.14)` | Color / Atmospheric Token |
| `--azure` | `#9a9aa2` | Color / Atmospheric Token |
| `--azure-deep` | `#5a5a62` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.hn-links> — `www-mbidirectmail-com`)**:
   - Landmark `<nav class="hn-links">` (`718x24px`) hosting `Direct Mail & Digital Marketing · Cu` navigation (`About · Capabilities · All capabilities → · Industries · Automotive 6`), DOM attributes (`data-tier="lite:cores2,mem4"`, `data-site-reveal`, `data-v-page-load-overlay="none"`, `data-v-hero-logo="wide"`), and stylesheet rule `revealed-section { display: none !important; }`.
2. **Hero Stage & Focal Lead (<section.solutions-section> — `Customer Acquisition Helping Busin`)**:
   - Landmark `<section class="solutions-section">` presenting display lead `Customer Acquisition Helping Businesses Find, Rea...` and copy excerpt *"8 0 0 - 3 5 9 - 4 7 8 0"* over `#06070a` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.skip-link> — `A Marketing Partner.`)**:
   - Landmark `<section class="skip-link">` rendering section `A Marketing Partner.` with copy *"Printing Commercial and variable-data printing, in-house."*, asset references (`favicon.svg`, `favicon.ico`, `lenis.min.js`, `d3-array.min.js`), and grid rule `mbe { display: none !important; }`.
4. **Interactive Detail & Feature Matrix (<section.plo-overlay> — `We find the right audience. We are`)**:
   - Landmark `<section class="plo-overlay">` framing `We find the right audience. We are experts at kno...` and `One partner. One team. Strategy to delivery.` (*"Commercial and variable-data printing, in-house."*) with `#151515` surface cards, `#ff0000` accents, and `html.mbe-lock body { overflow: hidden !important; }`.
5. **Colophon & Global Directory Footer (<footer.print-signoff> — `https://www.mbidirectmail.com/`)**:
   - Landmark `<footer class="print-signoff">` anchoring `Direct Mail & Digital Marketing ` footer links (`About · Capabilities · All capabilities → · Industries · Automotive 6`), copy *"Direct Mail Targeted campaigns, lists, and postal entry unde"*, and `#1f2022` structural dividers.
