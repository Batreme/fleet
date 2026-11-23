---
title: "UI & UX Architecture: uimaven-art"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: uimaven-art

## Overview & Design Identity
- **Target**: `uimaven-art` (**uimaven.art**)
- **Production URL**: [https://uimaven.art](https://uimaven.art)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f3670e` / `#fe0000`)
- **Summary**: UI/UX design portfolio of Leila Abbassova.
- **Total Clean CSS Variables Extracted**: `101` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Jost`
- **Body Font Stack**: `Jost`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: CSS variables `--text-display: 64px`, `--text-display--line-height: .95`, `--text-display-phone: 40px`
- **Section Heading (`H2`)**: observed font-size ladder: `16px`, `1em`, `80%`, `75%`, `var(--text-heading)`
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5/1)`, `--text-body: 16px`
- **Metadata & Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1/.75)`, `--text-sm: .875rem`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f3670e` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#4a4a4a` | `.bg-neutral-900 { background-color: #4a4a4a }` |
| **Interactive Accent / Highlight** | `#fe0000` | `var(--color-red-accent)` in `:root` |
| **Secondary / Muted Copy** | `#002af0` | `var(--color-secondary-300)` in `:root` |
| **Structural Hairline Border** | `#000000` | `var(--color-border-dark)` in `:root` |
| **Variable Token (`--color-red-100`)** | `#fb3748` | `var(--color-red-100)` in `:root` |
| **Variable Token (`--color-red-500`)** | `#fb2c36` | `var(--color-red-500)` in `:root` |
| **Variable Token (`--color-red-800`)** | `#9f0712` | `var(--color-red-800)` in `:root` |
| **Variable Token (`--color-yellow-100`)** | `#ffdb43` | `var(--color-yellow-100)` in `:root` |
| **Variable Token (`--color-yellow-200`)** | `#dfb400` | `var(--color-yellow-200)` in `:root` |
| **Variable Token (`--color-yellow-500`)** | `#edb200` | `var(--color-yellow-500)` in `:root` |
| **Variable Token (`--color-green-200`)** | `#1fc16b` | `var(--color-green-200)` in `:root` |
| **Variable Token (`--color-neutral-100`)** | `#ffffff` | `var(--color-neutral-100)` in `:root` |
| **Variable Token (`--color-neutral-200`)** | `#e8e8e8` | `var(--color-neutral-200)` in `:root` |
| **Variable Token (`--color-neutral-300`)** | `#d2d2d2` | `var(--color-neutral-300)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--site-header-h` | `60px` | Layout / Spatial Grid Token |
| `--font-jost` | `"Jost","Jost Fallback"` | Typography / Scale Token |
| `--type-weight` | `initial` | Typography / Scale Token |
| `--color-red-100` | `#fb3748` | Brand / Palette Token |
| `--color-red-500` | `#fb2c36` | Brand / Palette Token |
| `--color-red-800` | `#9f0712` | Brand / Palette Token |
| `--color-yellow-100` | `#ffdb43` | Brand / Palette Token |
| `--color-yellow-200` | `#dfb400` | Brand / Palette Token |
| `--color-yellow-500` | `#edb200` | Brand / Palette Token |
| `--color-green-200` | `#1fc16b` | Brand / Palette Token |
| `--color-neutral-100` | `#fff` | Brand / Palette Token |
| `--color-neutral-200` | `#e8e8e8` | Brand / Palette Token |
| `--color-neutral-300` | `#d2d2d2` | Brand / Palette Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.shrink-0> — `uimaven-art`)**:
   - Landmark `<header class="shrink-0 relative">` (`1440x0px`) hosting `uimaven.art` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-home`), and stylesheet rule `jost_bd43172b-module__QzW_JW__cla... { font-family:Jost,Jost Fallback;font-style:normal }`.
2. **Hero Stage & Focal Lead (<main.mobile-stripes> — `uimaven.art`)**:
   - Landmark `<main class="mobile-stripes bg-primary-300">` presenting display lead `uimaven.art` and copy excerpt *"UI/UX design portfolio of Leila Abbassova."* over `#f3670e` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<main.bg-primary-300> — `Featured Work & Interactive Showca`)**:
   - Landmark `<main class="mobile-stripes bg-primary-300">` rendering section `Featured Work & Interactive Showcase` with copy *"uimaven.art"*, asset references (`81cef6a21128489e-s.p.6cf41120.woff2`, `d7f27077a988d3d1.css`, `e48a17b7f69aeb46.js`, `2677990b2b1206f6.js`), and grid rule `.jost_bd43172b-module__QzW_JW__va... { --font-jost:"Jost","Jost Fallback" }`.
4. **Interactive Detail & Feature Matrix (<main.mobile-stripes:nth(2)> — `Technical Architecture & Narrative`)**:
   - Landmark `<main class="mobile-stripes bg-primary-300">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Featured Work & Interactive Showcase"*) with `#4a4a4a` surface cards, `#fe0000` accents, and `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
5. **Colophon & Global Directory Footer (<footer.bg-primary-300> — `https://uimaven.art`)**:
   - Landmark `<footer class="bg-primary-300">` anchoring `uimaven.art` footer links (`Overview · Index · Archive · About · Contact`), copy *"Technical Architecture & Narrative"*, and `#000000` structural dividers.
