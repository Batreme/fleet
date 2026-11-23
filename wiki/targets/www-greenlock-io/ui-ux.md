---
title: "UI & UX Architecture: www-greenlock-io"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-greenlock-io

## Overview & Design Identity
- **Target**: `www-greenlock-io` (**Independent Wealth Oversight for Family Offices · GreenLock**)
- **Production URL**: [https://www.greenlock.io](https://www.greenlock.io)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#0a1516` ink, `#0000ff` accent)
- **Summary**: GreenLock is a Swiss-based platform offering objective, independent oversight for Single Family Offices. Expose hidden costs, optimize pe...
- **Total Clean CSS Variables Extracted**: `62` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Reckless Neue Licensed`
- **Body Font Stack**: `Manrope`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 54.5058px`, `line-height: 59.6676px`, `font-weight: 500`); rule `h1` (`font-size: 2.5rem`, `line-height: 3.375rem`, `font-weight: 600`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 54.5058px`, `line-height: 59.6676px`, `font-weight: 500`); rule `h2` (`font-size: 2.5rem`, `line-height: 3.375rem`, `font-weight: 600`)
- **Body Copy**: live computed `body` (`font-size: 20.6238px`, `line-height: 23.5701px`, `font-weight: 400`); rule `p` (`font-size: 1.75rem`, `line-height: 3rem`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 20.6238px`, `line-height: 23.5701px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `browser-default` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#0a1516` | live computed `p` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffff00` | `mark { background: #ffff00 }` |
| **Interactive Accent / Highlight** | `#0000ff` | `.button.is-text.w--current { color: blue }` (`#0000ff`) |
| **Secondary / Muted Copy** | `#333333` | live computed `a` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#e2e2e2` | `blockquote { border-left: #e2e2e2 }` |
| **Variable Token (`--green-700`)** | `#0c221b` | `var(--green-700)` in `:root` |
| **Variable Token (`--green-100`)** | `#e0faef` | `var(--green-100)` in `:root` |
| **Variable Token (`--green-200`)** | `#99f4c0` | `var(--green-200)` in `:root` |
| **Variable Token (`--green-600`)** | `#0f3026` | `var(--green-600)` in `:root` |
| **Variable Token (`--gray-300`)** | `#94a8a2` | `var(--gray-300)` in `:root` |
| **Variable Token (`--green-250`)** | `#5d9c78` | `var(--green-250)` in `:root` |
| **Variable Token (`--transparent`)** | `#0000` | `var(--transparent)` in `:root` |
| **Variable Token (`--gray-500`)** | `#132526` | `var(--gray-500)` in `:root` |
| **Variable Token (`--yellow-200`)** | `#fcf89c` | `var(--yellow-200)` in `:root` |
| **Variable Token (`--purple-400`)** | `#3f328d` | `var(--purple-400)` in `:root` |
| **Variable Token (`--gray-400`)** | `#1f3f32` | `var(--gray-400)` in `:root` |
| **Variable Token (`--gray-100`)** | `#f4f5f3` | `var(--gray-100)` in `:root` |
| **Variable Token (`--green-400`)** | `#18975a` | `var(--green-400)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--green-700` | `#0c221b` | Color / Atmospheric Token |
| `--manrope-grotesk` | `Manrope,sans-serif` | Design System Custom Token |
| `--green-100` | `#e0faef` | Color / Atmospheric Token |
| `--white` | `white` | Canvas / Surface Token |
| `--reckless-antiqua` | `"Reckless Neue Licensed",sans-serif` | Design System Custom Token |
| `--green-200` | `#99f4c0` | Color / Atmospheric Token |
| `--green-600` | `#0f3026` | Color / Atmospheric Token |
| `--gray-300` | `#94a8a2` | Color / Atmospheric Token |
| `--green-250` | `#5d9c78` | Color / Atmospheric Token |
| `--transparent` | `#0000` | Color / Atmospheric Token |
| `--gray-500` | `#132526` | Color / Atmospheric Token |
| `--yellow-200` | `#fcf89c` | Color / Atmospheric Token |
| `--purple-400` | `#3f328d` | Color / Atmospheric Token |
| `--gray-400` | `#1f3f32` | Color / Atmospheric Token |
| `--gray-100` | `#f4f5f3` | Color / Atmospheric Token |
| `--green-400` | `#18975a` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.w-mod-js> — `www-greenlock-io`)**:
   - Landmark `<header class="w-mod-js">` (`1440px`) hosting `Independent Wealth Oversight for Fam` navigation (`Pricing · Insights · About us · Client portal`), DOM attributes (`data-wf-domain="www.greenlock.io"`, `data-wf-page="6816540e936df6252569dd87"`, `data-wf-site="63fca69523dfba725518d390"`, `data-domain="greenlock.io"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
2. **Hero Stage & Focal Lead (<section.v2-header-section> — `Your Wealth. Fully Accounted.`)**:
   - Landmark `<section class="v2-header-section">` presenting display lead `Your Wealth. Fully Accounted.` and copy excerpt *"Fee Benchmarking & Reduction"* over `#ffffff` canvas and `#0a1516` ink.
3. **Primary Showcase & Content Grid (<section.v2-hero-section> — `Fee`)**:
   - Landmark `<section class="v2-hero-section full-height-fix">` rendering section `Fee` with copy *"Investment Performance Audit"*, asset references (`cdn.prod.website-files.com`, `greenlock-site.webflow.shared.26f...`, `fonts.googleapis.com`, `fonts.gstatic.com`), and grid rule `summary { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.v2-ticker-section> — `Benchmarking`)**:
   - Landmark `<section class="v2-ticker-section">` framing `Benchmarking` and `& Reduction` (*"PE/VC Portfolio Optimization"*) with `#ffff00` surface cards, `#0000ff` accents, and `video { vertical-align:baseline;display:inline-block }`.
5. **Colophon & Global Directory Footer (<footer.wf-manrope-n6-active> — `https://www.greenlock.io`)**:
   - Landmark `<footer class="wf-manrope-n6-active">` anchoring `Independent Wealth Oversight for` footer links (`Pricing · Insights · About us · Client portal`), copy *"Real Estate Assets Monitoring"*, and `#e2e2e2` structural dividers.
