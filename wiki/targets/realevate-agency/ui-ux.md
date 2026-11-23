---
title: "UI & UX Architecture: realevate-agency"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: realevate-agency

## Overview & Design Identity
- **Target**: `realevate-agency` (**Realevate · Exceptional Real Estate Investments in Cyprus, Montenegro &...**)
- **Production URL**: [https://realevate.agency/](https://realevate.agency/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#1f2b5e` ink, `#000080` accent)
- **Summary**: Realevate is a global real estate agency specializing in unique properties and exceptional developments in high-demand markets, offering...
- **Total Clean CSS Variables Extracted**: `305` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Google Sans`
- **Body Font Stack**: `Google Sans`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 23.6827px`, `line-height: 30.7875px`, `font-weight: 500`, `letter-spacing: -0.236827px`); CSS variables `--display-font: "Roslindale Display", Georgia, "Times New Roman", serif`, `--desktop-h1-size: 16vw`, `--desktop-h1-line-height: 1`; rule `h1` (`font-size: 5.5vw`)
- **Section Heading (`H2`)**: CSS variables `--desktop-h2-size: 5.2vw`, `--desktop-h2-line-height: .94`, `--desktop-h2-letter-spacing: -.03em`; rule `h2` (`font-weight: 200`)
- **Body Copy**: live computed `body` (`font-size: 16.3705px`, `line-height: normal`, `font-weight: 500`, `letter-spacing: -0.163705px`); CSS variables `--body-leading: 1.35`; rule `,body` (`font-size: var(--text-size)`, `letter-spacing: -.01em`, `font-weight: 500`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16.3705px`, `line-height: normal`, `font-weight: 500`, `letter-spacing: -0.163705px`); CSS variables `--desktop-h1-letter-spacing: -.02em`, `--desktop-h2-letter-spacing: -.03em`, `--desktop-h3-letter-spacing: -.05em`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#1f2b5e` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#e3e5eb` | live computed `nav` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#000080` | `body.home-logo-transition.conta... { color: navy }` (`#000080`) |
| **Secondary / Muted Copy** | `#80988e` | `var(--category-evergreen-muted)` in `:root` |
| **Structural Hairline Border** | `#d7d9e2` | `.contact-form-tabs { border-bottom: #d7d9e2 }` |
| **Variable Token (`--muted`)** | `#626c95` | `var(--muted)` in `:root` |
| **Variable Token (`--category-by-the-sea-color`)** | `#222a4c` | `var(--category-by-the-sea-color)` in `:root` |
| **Variable Token (`--category-by-the-sea-muted`)** | `#5d668d` | `var(--category-by-the-sea-muted)` in `:root` |
| **Variable Token (`--category-evergreen-color`)** | `#36614d` | `var(--category-evergreen-color)` in `:root` |
| **Variable Token (`--category-urban-living-color`)** | `#2d1c2d` | `var(--category-urban-living-color)` in `:root` |
| **Variable Token (`--category-urban-living-muted`)** | `#6b5a6b` | `var(--category-urban-living-muted)` in `:root` |
| **Variable Token (`--category-rare-gems-color`)** | `#1c181d` | `var(--category-rare-gems-color)` in `:root` |
| **Variable Token (`--category-rare-gems-muted`)** | `#5c585d` | `var(--category-rare-gems-muted)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--brand-navy` | `#1F2B5E` | Brand / Palette Token |
| `--navy` | `var(--brand-navy)` | Layout / Spatial Grid Token |
| `--muted` | `#626C95` | Color / Atmospheric Token |
| `--white` | `#FFFFFF` | Canvas / Surface Token |
| `--category-color-light` | `var(--white)` | Canvas / Surface Token |
| `--category-by-the-sea-color` | `#222A4C` | Brand / Palette Token |
| `--category-by-the-sea-muted` | `#5D668D` | Color / Atmospheric Token |
| `--category-evergreen-color` | `#36614D` | Brand / Palette Token |
| `--category-evergreen-muted` | `#80988E` | Color / Atmospheric Token |
| `--category-urban-living-color` | `#2D1C2D` | Brand / Palette Token |
| `--category-urban-living-muted` | `#6B5A6B` | Color / Atmospheric Token |
| `--category-rare-gems-color` | `#1C181D` | Brand / Palette Token |
| `--category-rare-gems-muted` | `#5C585D` | Color / Atmospheric Token |
| `--custom-scrollbar-thumb-color` | `var(--muted)` | Brand / Palette Token |
| `--sans-font` | `"Google Sans", Arial, Helvetica, sans-serif` | Typography / Scale Token |
| `--display-font` | `"Roslindale Display", Georgia, "Times New Roman", serif` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.logo> — `realevate-agency`)**:
   - Landmark `<header class="logo">` (`273x19px`) hosting `Realevate · Exceptional Real Estate ` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-category="home"`, `data-selection-cover="assets/women-monteneg..."`, `data-category="by-the-sea"`, `data-selection-cover="assets/bythesea-card-..."`), and stylesheet rule `after { box-sizing:border-box;-webkit-user-select:none;-moz-user-select:none;-ms... }`.
2. **Hero Stage & Focal Lead (<main.site-preloader-counter-init> — `Invest in Exceptional Real Estate `)**:
   - Landmark `<main class="site-preloader-counter-init">` presenting display lead `Invest in Exceptional Real Estate Properties in C...` and copy excerpt *"STARTING FROM 100,000€"* over `#ffffff` canvas and `#1f2b5e` ink.
3. **Primary Showcase & Content Grid (<main.is-ready> — `STARTING FROM 100,000€`)**:
   - Landmark `<main class="is-ready">` rendering section `STARTING FROM 100,000€` with copy *"Starting from 100,000€"*, asset references (`4532996743652549`, `fbevents.js`, `compat-bootstrap.js`, `favicon.png`), and grid rule `root { --category-hero-scroll-grow-scale: 1.2 }`.
4. **Interactive Detail & Feature Matrix (<main.rotate-phone-overlay> — `Starting from 100,000€`)**:
   - Landmark `<main class="rotate-phone-overlay">` framing `Starting from 100,000€` and `Please rotate your device` (*"Please rotate your device"*) with `#e3e5eb` surface cards, `#000080` accents, and `html { scrollbar-width:none;width:100%;height:100svh }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://realevate.agency/`)**:
   - Landmark `<footer class="site-footer">` anchoring `Realevate · Exceptional Real Est` footer links (`Overview · Index · Archive · About · Contact`), copy *"Homepage Invest in Cyprus, Montenegro and Georgia"*, and `#d7d9e2` structural dividers.
