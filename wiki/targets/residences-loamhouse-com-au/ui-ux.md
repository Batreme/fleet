---
title: "UI & UX Architecture: residences-loamhouse-com-au"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: residences-loamhouse-com-au

## Overview & Design Identity
- **Target**: `residences-loamhouse-com-au` (**Loam House — Sandringham**)
- **Production URL**: [https://residences.loamhouse.com.au](https://residences.loamhouse.com.au)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f1eee7` canvas, `#1e211d` ink, `#512616` accent)
- **Summary**: Loam House — house-sized residences in Sandringham. Final release now selling.
- **Total Clean CSS Variables Extracted**: `17` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Cormorant Garamond`
- **Body Font Stack**: `DM Sans`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 122.4px`, `line-height: 90.576px`, `font-weight: 300`, `letter-spacing: -5.508px`); rule `h1` (`font-size: clamp(76px,8.5vw,138px)`, `line-height: .74`, `letter-spacing: -.045em`, `font-weight: 300`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 100.8px`, `line-height: 85.68px`, `font-weight: 400`, `letter-spacing: -3.024px`); rule `h2` (`font-size: clamp(52px,8vw,120px)`, `line-height: .9`, `letter-spacing: -.02em`, `font-weight: 400`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 300`); rule `p` (`font-size: clamp(15px,1.3vw,19px)`, `line-height: 1.6`, `font-weight: 300`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 300`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f1eee7` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#1e211d` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `.fmc-caret { background: #ffffff }` |
| **Interactive Accent / Highlight** | `#512616` | `.mbtn-text { color: #512616 }` |
| **Secondary / Muted Copy** | `#ffffff` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#cbc9c3` | `var(--line)` in `:root` (`rgba(30,33,29,.18)`) |
| **Variable Token (`--chalk`)** | `#fbfaf6` | `var(--chalk)` in `:root` |
| **Variable Token (`--clay`)** | `#8d4f36` | `var(--clay)` in `:root` |
| **Variable Token (`--olive`)** | `#626852` | `var(--olive)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ink` | `#1e211d` | Typography Ink Token |
| `--paper` | `#f1eee7` | Canvas / Surface Token |
| `--chalk` | `#fbfaf6` | Color / Atmospheric Token |
| `--clay` | `#8d4f36` | Color / Atmospheric Token |
| `--olive` | `#626852` | Color / Atmospheric Token |
| `--line` | `rgba(30,33,29,.18)` | Color / Atmospheric Token |
| `--serif` | `"Cormorant Garamond",Georgia,serif` | Typography / Scale Token |
| `--hero-serif` | `"Cormorant Garamond",Georgia,serif` | Typography / Scale Token |
| `--sans` | `"DM Sans",Arial,sans-serif` | Typography / Scale Token |
| `--hgut` | `6vw` | Dimension / Scale Token |
| `--scan` | `.2` | Design System Custom Token |
| `--mob-pos` | `36% center` | Dimension / Scale Token |
| `--pulse-period` | `4.1s` | Motion / Timing Token |
| `--ping-scale` | `4.2` | Design System Custom Token |
| `--ping-op` | `0.36` | Design System Custom Token |
| `--num-op` | `1` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `residences-loamhouse-com-au`)**:
   - Landmark `<header class="site-header">` (`1440x82px`) hosting `Loam House — Sandringham` navigation (`Proposition · Size · Storage · Finishes · Precinct`), DOM attributes (`data-preloader`, `data-pl-pct`, `data-header`, `data-open-calendly`), and stylesheet rule `stage { position:absolute;inset:0;overflow:hidden }`.
2. **Hero Stage & Focal Lead (<section.hero> — `House-sized. Bayside living.`)**:
   - Landmark `<section class="hero chapter">` presenting display lead `House-sized. Bayside living.` and copy excerpt *"FINAL RELEASE · SANDRINGHAM"* over `#f1eee7` canvas and `#1e211d` ink.
3. **Primary Showcase & Content Grid (<section.form-chapter> — `Leave the upkeep. Keep the life.`)**:
   - Landmark `<section class="form-chapter chapter">` rendering section `Leave the upkeep. Keep the life.` with copy *"Final release · Sandringham"*, asset references (`clientParamBuilder.bundle.js`, `clarity.js`, `yed6eroa3m`, `1440095636442948`), and grid rule `map { position:absolute;inset:0;width:100%;height:100%;display:block;touch-act... }`.
4. **Interactive Detail & Feature Matrix (<section.cine> — `A backyard oasis, without the mowi`)**:
   - Landmark `<section class="cine chapter">` framing `A backyard oasis, without the mowing.` and `Everything you need. Nothing you don’t.` (*"Bayside’s largest apartments. 86–275m² residences from $850,000."*) with `#ffffff` surface cards, `#512616` accents, and `.station circle { fill:fff;stroke:40453b;stroke-width:1;pointer-events:none }`.
5. **Colophon & Global Directory Footer (<footer.pl-panels> — `https://residences.loamhouse.com.au`)**:
   - Landmark `<footer class="pl-panels">` anchoring `Loam House — Sandringham` footer links (`Proposition · Size · Storage · Finishes · Precinct`), copy *"Artist’s impression"*, and `#cbc9c3` structural dividers.
