---
title: "UI & UX Architecture: zarcerog-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: zarcerog-com

## Overview & Design Identity
- **Target**: `zarcerog-com` (**Nicolás Zarcero — Box Office**)
- **Production URL**: [https://zarcerog.com](https://zarcerog.com)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#e8b3a9` canvas, `#000000` ink, `#241417` accent)
- **Summary**: Two shows tonight: a portfolio in five acts, with an intermission; and a picture about a church that is running late. Nicolás Zarcero, en...
- **Total Clean CSS Variables Extracted**: `32` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Jost`
- **Body Font Stack**: `Jost Fallback`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 32px`, `line-height: normal`, `font-weight: 700`)
- **Section Heading (`H2`)**: observed font-size ladder: `32px`, `16px`, `30px`, `clamp(16px,1.7vw,26px)`, `12px`
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#e8b3a9` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `body` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f6ead0` | `.bx-ticket--theatre .bx-ticket_... { background: #f6ead0 }` |
| **Interactive Accent / Highlight** | `#241417` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#241417` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#ff0000` | `.bx-note path { stroke: #ff0000 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--f-sans` | `"Jost", "Jost Fallback"` | Typography / Scale Token |
| `--f-serif` | `"Bodoni Moda", "Bodoni Moda Fallback"` | Typography / Scale Token |
| `--f-type` | `"Courier Prime", "Courier Prime Fallback"` | Typography / Scale Token |
| `--f-cinzel` | `"Cinzel", "Cinzel Fallback"` | Design System Custom Token |
| `--f-anton` | `"Anton", "Anton Fallback"` | Design System Custom Token |
| `--f-shrikhand` | `"Shrikhand", "Shrikhand Fallback"` | Design System Custom Token |
| `--f-abril` | `"Abril Fatface", "Abril Fatface Fallback"` | Design System Custom Token |
| `--f-pen` | `"Nanum Pen Script", "Nanum Pen Script Fallback"` | Design System Custom Token |
| `--f-slab` | `"Alfa Slab One", "Alfa Slab One Fallback"` | Design System Custom Token |
| `--f-script` | `"Yellowtail", "Yellowtail Fallback"` | Design System Custom Token |
| `--f-marker` | `"Permanent Marker", "Permanent Marker Fallback"` | Design System Custom Token |
| `--f-marquee` | `"Limelight", "Limelight Fallback"` | Design System Custom Token |
| `--bx-sans` | `var(--f-sans,Jost), Jost, Futura, "Helvetica Neue", sans-serif` | Typography / Scale Token |
| `--bx-type` | `var(--f-type,"Courier Prime"), "Courier Prime", "Courier New", monospace` | Typography / Scale Token |
| `--bx-marquee` | `var(--f-marquee,Limelight), Limelight, var(--f-serif,"Bodoni Moda"), serif` | Design System Custom Token |
| `--bx-anton` | `var(--f-anton,Anton), Anton, Impact, "Arial Narrow", sans-serif` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.bx-layer> — `zarcerog-com`)**:
   - Landmark `<nav class="bx-layer bx-layer--tickets">` (`1440x900px`) hosting `Nicolás Zarcero — Box Office` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-sdkn="@vercel/analytics/next"`, `data-sdkv="1.6.1"`), and stylesheet rule `jost_65562e22-module__iZxnCa__cla... { font-family:Jost,Jost Fallback;font-style:normal }`.
2. **Hero Stage & Focal Lead (<main.bx-root> — `Nicolás Zarcero: box office. Two s`)**:
   - Landmark `<main class="bx-root">` presenting display lead `Nicolás Zarcero: box office. Two shows tonight —...` and copy excerpt *"The house has two shows tonight."* over `#e8b3a9` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<main.bx-root:nth(2)> — `Nicolás Zarcero : box office. Two `)**:
   - Landmark `<main class="bx-root">` rendering section `Nicolás Zarcero : box office. Two shows tonight —...` with copy *"The Zarcero Theatre presents A Portfolio in Five Acts with an int"*, asset references (`52b5d5098cb87ddd-s.p.3r2y_bth_sjs...`, `5f440d3eea613716-s.p.1xmps1tcyqv3...`, `612bd71aa396cae6-s.p.0y-3ea_6ee5g...`, `81cef6a21128489e-s.p.2csanl8cs02r...`), and grid rule `.jost_65562e22-module__iZxnCa__va... { --f-sans:"Jost", "Jost Fallback" }`.
4. **Interactive Detail & Feature Matrix (<main.bx-root:nth(3)> — `The Zarcero Theatre presents A Por`)**:
   - Landmark `<main class="bx-root">` framing `The Zarcero Theatre presents A Portfolio in Five` and `The Zarcero Theatre` (*"The Zarcero Theatre"*) with `#f6ead0` surface cards, `#241417` accents, and `moda_1acaef39-module__CjqdXa__cla... { font-family:Bodoni Moda,Bodoni Moda Fallback }`.
5. **Colophon & Global Directory Footer (<footer.bx-foot> — `https://zarcerog.com`)**:
   - Landmark `<footer class="bx-foot">` anchoring `Nicolás Zarcero — Box Office` footer links (`Overview · Index · Archive · About · Contact`), copy *"A Portfolio in Five Acts"*, and `#ff0000` structural dividers.
