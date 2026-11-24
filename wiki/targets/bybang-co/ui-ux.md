---
title: "UI & UX Architecture: bybang-co"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: bybang-co

## Overview & Design Identity
- **Target**: `bybang-co` (**Estudio Bang · Architecture, Interiors, Objects & Digital Media**)
- **Production URL**: [https://bybang.co/](https://bybang.co/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×1656px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#141414` ink, `#c7161d` accent)
- **Summary**: Estudio Bang is a Barcelona-based architecture studio working across architecture, interiors, objects and digital media. We create spaces...
- **Total Clean CSS Variables Extracted**: `50` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Geist`
- **Body Font Stack**: `Geist`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 74px`, `line-height: 76px`, `font-weight: 500`, `letter-spacing: -2.96px`); rule `h1` (`font-size: 32px`, `line-height: .95`, `letter-spacing: -.02em`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 32px`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: 16px`, `line-height: 1.4`, `letter-spacing: -.02em`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--mono: "Geist Mono", ui-monospace, monospace`; rule `small` (`font-size: 11px`, `line-height: 1`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#141414` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f5f5f2` | `var(--bg)` in `:root` |
| **Interactive Accent / Highlight** | `#c7161d` | `.case-contact-button--error { background: #c7161d }` |
| **Secondary / Muted Copy** | `#2e2e2e` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#ececec` | `var(--border)` in `:root` (`rgba(20, 20, 20, .08)`) |
| **Variable Token (`--panel`)** | `#e1e1e1` | `var(--panel)` in `:root` |
| **Variable Token (`--panel-dark`)** | `#d7d7d0` | `var(--panel-dark)` in `:root` |
| **Variable Token (`--accent`)** | `#946ec4` | `var(--accent)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bg` | `#f5f5f2` | Canvas / Surface Token |
| `--panel` | `#e1e1e1` | Color / Atmospheric Token |
| `--panel-dark` | `#d7d7d0` | Canvas / Surface Token |
| `--text` | `#141414` | Typography Ink Token |
| `--muted` | `rgba(20, 20, 20, .3)` | Color / Atmospheric Token |
| `--border` | `rgba(20, 20, 20, .08)` | Elevation / Border Token |
| `--accent` | `#946ec4` | Brand / Palette Token |
| `--shadow` | `0 24px 80px rgba(11, 12, 11, .12)` | Elevation / Border Token |
| `--mono` | `"Geist Mono", ui-monospace, monospace` | Typography / Scale Token |
| `--sans` | `"Geist", "Helvetica Neue", Arial, sans-serif` | Typography / Scale Token |
| `--stable-viewport-height` | `100vh` | Layout / Spatial Grid Token |
| `--site-bg` | `#ffffff` | Canvas / Surface Token |
| `--site-ink` | `#141414` | Typography Ink Token |
| `--site-muted` | `rgba(20, 20, 20, .3)` | Color / Atmospheric Token |
| `--site-faint` | `rgba(20, 20, 20, .2)` | Color / Atmospheric Token |
| `--site-grid-edge` | `32px` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-chrome> — `bybang-co`)**:
   - Landmark `<header class="site-chrome">` (`1376x24px`) hosting `Estudio Bang · Architecture, Interio` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-cursor-target="logo"`, `data-cursor-target="logo"`, `data-entry-signal="0"`, `data-filter="all"`), and stylesheet rule `html.lenis body { height:auto }`.
2. **Hero Stage & Focal Lead (<main.site-home> — `estudiobang`)**:
   - Landmark `<main class="site-home site-home--ready">` presenting display lead `estudiobang` and copy excerpt *"BCN 13 : 59 BUE 09 : 59"* over `#ffffff` canvas and `#141414` ink.
3. **Primary Showcase & Content Grid (<main.site-home--ready> — `BCN 13 : 59 BUE 09 : 59`)**:
   - Landmark `<main class="site-home site-home--ready">` rendering section `BCN 13 : 59 BUE 09 : 59` with copy *"Copyright Estudio Bang® 2026 · Legal & Privacy · Made by Tremendo"*, asset references (`intro-01.webp`, `intro-02.webp`, `intro-03.webp`, `intro-04.webp`), and grid rule `.lenis-stopped { overflow:clip }`.
4. **Interactive Detail & Feature Matrix (<main.site-home:nth(2)> — `Copyright Estudio Bang® 2026 · Leg`)**:
   - Landmark `<main class="site-home site-home--ready">` framing `Copyright Estudio Bang® 2026 · Legal & Privacy ·` and `Copyright Estudio Bang® 2026` (*"Copyright Estudio Bang® 2026"*) with `#f5f5f2` surface cards, `#c7161d` accents, and `.lenis.lenis-smooth iframe { pointer-events:none }`.
5. **Colophon & Global Directory Footer (<footer.custom-cursor__label> — `https://bybang.co/`)**:
   - Landmark `<footer class="custom-cursor__label">` anchoring `Estudio Bang · Architecture, Int` footer links (`Overview · Index · Archive · About · Contact`), copy *"Copyright Estudio Bang® 2026 · Legal & Privacy ·"*, and `#ececec` structural dividers.
