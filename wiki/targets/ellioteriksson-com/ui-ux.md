---
title: "UI & UX Architecture: ellioteriksson-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: ellioteriksson-com

## Overview & Design Identity
- **Target**: `ellioteriksson-com` (**Elliot Eriksson — UI/UX, web & brand design, Stockholm & Åland**)
- **Production URL**: [https://ellioteriksson.com/](https://ellioteriksson.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×1744px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#0c0c0c` ink, `#c6f432` accent)
- **Summary**: Elliot Eriksson is a design technologist in Stockholm, designing clear, accessible websites and interfaces from first sketch to final pol...
- **Total Clean CSS Variables Extracted**: `45` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Geist`
- **Body Font Stack**: `Geist`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 37.44px`, `line-height: 38.9376px`, `font-weight: 400`, `letter-spacing: -1.3104px`); CSS variables `--fs-display: clamp(36px, 4vw, 72px)`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 57.6px`, `line-height: 59.904px`, `font-weight: 400`, `letter-spacing: -2.592px`); CSS variables `--fs-lg: clamp(24px, 2.4vw, 40px)`
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 23.2px`, `font-weight: 400`, `letter-spacing: -0.16px`); CSS variables `--fs-body: 16px`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 23.2px`, `font-weight: 400`, `letter-spacing: -0.16px`); CSS variables `--font-mono: var(--font-mono-face,"Geist Mono"), ui-monospace, Menlo, monospace`, `--font-mono-face: "Geist Mono", "Geist Mono Fallback"`; rule `,.mono` (`font-size: 12px`, `line-height: 1.4`, `letter-spacing: .02em`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#0c0c0c` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f3f3f3` | `var(--surface)` in `:root` |
| **Interactive Accent / Highlight** | `#c6f432` | `var(--accent)` in `:root` |
| **Secondary / Muted Copy** | `#6b6b6b` | `var(--muted)` in `:root` |
| **Structural Hairline Border** | `#e1e1e1` | `var(--rule)` in `:root` (`0c0c0c1f`) |
| **Variable Token (`--kind-client`)** | `#ff6fae` | `var(--kind-client)` in `:root` |
| **Variable Token (`--kind-personal`)** | `#ff5a36` | `var(--kind-personal)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--accent` | `#c6f432` | Brand / Palette Token |
| `--on-accent` | `#0c0c0c` | Brand / Palette Token |
| `--highlight` | `#c6f432` | Canvas / Surface Token |
| `--on-highlight` | `#0c0c0c` | Canvas / Surface Token |
| `--kind-agency` | `var(--highlight)` | Design System Custom Token |
| `--kind-client` | `#ff6fae` | Color / Atmospheric Token |
| `--kind-personal` | `#ff5a36` | Color / Atmospheric Token |
| `--font-wordmark` | `var(--font-wordmark-face,"Gossip"), Georgia, serif` | Typography / Scale Token |
| `--font-mono` | `var(--font-mono-face,"Geist Mono"), ui-monospace, Menlo, monospace` | Typography / Scale Token |
| `--gutter` | `3vw` | Layout / Spatial Grid Token |
| `--gap` | `11px` | Layout / Spatial Grid Token |
| `--header-h` | `52px` | Layout / Spatial Grid Token |
| `--section` | `clamp(96px, 11vw, 180px)` | Dimension / Scale Token |
| `--fs-body` | `16px` | Dimension / Scale Token |
| `--fs-md` | `clamp(20px, 1.8vw, 30px)` | Dimension / Scale Token |
| `--fs-lg` | `clamp(24px, 2.4vw, 40px)` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `ellioteriksson-com`)**:
   - Landmark `<header class="site-header">` (`1440x53px`) hosting `Elliot Eriksson — UI/UX, web & brand` navigation (`Home H o m e · Cases C a s e s · EN E N – English · SV S V – Svenska`), DOM attributes (`data-precedence="next"`, `data-href="/_next/static/immutab..."`, `data-sdkn="@vercel/analytics/next"`, `data-sdkv="2.0.1"`), and stylesheet rule `after { box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<section.hero> — `I’m elliot, an award winning desig`)**:
   - Landmark `<section class="hero">` presenting display lead `I’m elliot, an award winning design technologist...` and copy excerpt *"CURRENTLY IN STOCKHOLM14:22"* over `#ffffff` canvas and `#0c0c0c` ink.
3. **Primary Showcase & Content Grid (<section.showcase> — `I’m Elliot , an award winning desi`)**:
   - Landmark `<section class="showcase showcase--roomy">` rendering section `I’m Elliot , an award winning design technologist...` with copy *"Design technologist"*, asset references (`1dm-4pi_h5ujm.js`, `41lrt_djk18al.js`, `1x62cbew_54xo.js`, `2jqd0dpb7brv_.js`), and grid rule `img { max-width:100%;height:auto;display:block }`.
4. **Interactive Detail & Feature Matrix (<section.projects> — `Selected work Selected work`)**:
   - Landmark `<section class="projects">` framing `Selected work Selected work` and `More projects` (*"Based in Stockholm B a s e d i n S t o c k h o l m"*) with `#f3f3f3` surface cards, `#c6f432` accents, and `button { font:inherit;letter-spacing:inherit;color:inherit;cursor:pointer;backgro... }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://ellioteriksson.com/`)**:
   - Landmark `<footer class="site-footer">` anchoring `Elliot Eriksson — UI/UX, web & b` footer links (`Home H o m e · Cases C a s e s · EN E N – English · SV S V – Svenska`), copy *"Based in Stockholm"*, and `#e1e1e1` structural dividers.
