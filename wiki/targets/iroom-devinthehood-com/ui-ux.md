---
title: "UI & UX Architecture: iroom-devinthehood-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: iroom-devinthehood-com

## Overview & Design Identity
- **Target**: `iroom-devinthehood-com` (**iRoom framework 3 · Get started**)
- **Production URL**: [https://iroom.devinthehood.com/](https://iroom.devinthehood.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×4140px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#14181f` ink, `#1f72c7` accent)
- **Summary**: iRoom, the flex CSS framework: a twelve columns grid, 30+ components, light and dark themes driven by CSS custom properties, parallax, a...
- **Total Clean CSS Variables Extracted**: `113` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Poppins`
- **Body Font Stack**: `Segoe UI`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 76px`, `line-height: 79.04px`, `font-weight: 700`, `letter-spacing: -2.66px`); rule `,.h1` (`font-size: clamp(2rem,1.55rem + 1.9vw,2....`, `letter-spacing: -0.02em`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 32px`, `line-height: 38.4px`, `font-weight: 600`, `letter-spacing: -0.48px`); rule `,.h2` (`font-size: clamp(1.5rem,1.3rem + .9vw,2rem)`, `letter-spacing: -0.015em`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 25.6px`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 25.6px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#14181f` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f6f7f9` | `var(--ir-surface-2)` in `:root` |
| **Interactive Accent / Highlight** | `#1f72c7` | `var(--ir-primary)` in `:root` |
| **Secondary / Muted Copy** | `#8b93a1` | `var(--ir-text-subtle)` in `:root` |
| **Structural Hairline Border** | `#e3e6eb` | `var(--ir-border)` in `:root` |
| **Variable Token (`--ir-surface-3`)** | `#eceef2` | `var(--ir-surface-3)` in `:root` |
| **Variable Token (`--ir-border-strong`)** | `#cdd2da` | `var(--ir-border-strong)` in `:root` |
| **Variable Token (`--ir-text-muted`)** | `#5d6675` | `var(--ir-text-muted)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--btn-bg` | `rgb(255 255 255 / .1)` | Canvas / Surface Token |
| `--btn-fg` | `#ffffff` | Typography Ink Token |
| `--btn-border` | `rgb(255 255 255 / .35)` | Elevation / Border Token |
| `--btn-bg-hover` | `rgb(255 255 255 / .2)` | Canvas / Surface Token |
| `--ir-sticky-top` | `calc(var(--ir-navbar-height) + 1.5rem)` | Dimension / Scale Token |
| `--ir-bg` | `#ffffff` | Canvas / Surface Token |
| `--ir-surface` | `#ffffff` | Canvas / Surface Token |
| `--ir-surface-2` | `#f6f7f9` | Canvas / Surface Token |
| `--ir-surface-3` | `#eceef2` | Canvas / Surface Token |
| `--ir-border` | `#e3e6eb` | Elevation / Border Token |
| `--ir-border-strong` | `#cdd2da` | Elevation / Border Token |
| `--ir-text` | `#14181f` | Typography Ink Token |
| `--ir-text-muted` | `#5d6675` | Typography Ink Token |
| `--ir-text-subtle` | `#8b93a1` | Typography Ink Token |
| `--ir-inverse-bg` | `#14181f` | Canvas / Surface Token |
| `--ir-inverse-fg` | `#f6f7f9` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.navbar> — `iroom-devinthehood-com`)**:
   - Landmark `<header class="navbar navbar-sticky">` (`1440x65px`) hosting `iRoom framework 3 · Get started` navigation (`Get started · Components · CSS · JavaScript · Download`), DOM attributes (`data-theme="auto"`, `data-theme-toggle`, `data-tooltip="Dark theme"`, `data-tooltip-position="bottom"`), and stylesheet rule `.demo-brand { font-family: 'Libre Barcode 128 Text', cursive; font-size: 2.75rem; font... }`.
2. **Hero Stage & Focal Lead (<section.demo-hero> — `The flex one, in a flex world.`)**:
   - Landmark `<section class="demo-hero parallax">` presenting display lead `The flex one, in a flex world.` and copy excerpt *"A CSS framework built on flexbox, cascade layers and custom prope"* over `#ffffff` canvas and `#14181f` ink.
3. **Primary Showcase & Content Grid (<section.demo-section> — `Everything a page needs, nothing i`)**:
   - Landmark `<section class="demo-section">` rendering section `Everything a page needs, nothing it does not` with copy *"Classes that read like what they do, a grid that bends to every s"*, asset references (`iroom.ico`, `favicon.png`, `iroom.min.css`, `demo.css`), and grid rule `.demo-logo-pending .demo-hero-bar... { visibility: hidden; }`.
4. **Interactive Detail & Feature Matrix (<section.bg-subtle> — `A real flex grid`)**:
   - Landmark `<section class="demo-section bg-subtle">` framing `A real flex grid` and `Cascade layers` (*"Twelve columns, four sizes, true gaps instead of negative margins"*) with `#f6f7f9` surface cards, `#1f72c7` accents, and `.demo-hero .lead { max-width: 40rem; color: rgb(255 255 255 / .88); text-shadow: 0 1px 12px... }`.
5. **Colophon & Global Directory Footer (<footer.demo-footer> — `https://iroom.devinthehood.com/`)**:
   - Landmark `<footer class="demo-footer">` anchoring `iRoom framework 3 · Get started` footer links (`Get started · Components · CSS · JavaScript · Download`), copy *"Reset, tokens, base, layout, components, utilities: an utili"*, and `#e3e6eb` structural dividers.
