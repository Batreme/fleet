---
title: "UI & UX Architecture: deltacafes-com_en"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: deltacafes-com_en

## Overview & Design Identity
- **Target**: `deltacafes-com_en` (**Delta, coffee with heart · Delta Cafés — The coffee of your life**)
- **Production URL**: [https://deltacafes.com/en](https://deltacafes.com/en)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#2b1b14` / `#f7a200`)
- **Summary**: Discover Delta Cafés: Portuguese coffee heritage, culture, sustainability, and experiences from bean to cup for every coffee lover.
- **Total Clean CSS Variables Extracted**: `264` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `delta-season`
- **Body Font Stack**: `trade-gothic`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 77.28px`, `line-height: 77.28px`, `font-weight: 300`, `letter-spacing: -1.5456px`); rule `.title` (`font-size: 16px`, `line-height: 1em`, `letter-spacing: -.03em`, `font-weight: 700`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 77.28px`, `line-height: 77.28px`, `font-weight: 300`, `letter-spacing: -1.5456px`); rule `h2` (`font-size: 12px`, `line-height: 1.3em`, `letter-spacing: -.01em`, `font-weight: 700`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 16px`, `font-weight: 400`); rule `p` (`font-size: clamp(14px,13.415px + 100vw *...`, `line-height: 1.2em`, `letter-spacing: .02em`, `font-weight: 420`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 11.84px`, `line-height: 14.208px`, `font-weight: 650`, `letter-spacing: 0.7104px`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#2b1b14` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#fcf3ed` | live computed `a` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#000000` | `:after { background-color: black }` (`#000000`) |
| **Interactive Accent / Highlight** | `#f7a200` | `var(--color-product-superior-accent-500)` in `:root` |
| **Secondary / Muted Copy** | `#e3c1ad` | live computed `h1` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#cccccc` | `var(--iti-border-color)` in `:root` |
| **Variable Token (`--color-white`)** | `#ffffff` | `var(--color-white)` in `:root` |
| **Variable Token (`--color-geral-delta-yellow`)** | `#ffd300` | `var(--color-geral-delta-yellow)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--initial-100vh` | `100vh` | Layout / Spatial Grid Token |
| `--native-scrollbar-width` | `0px` | Layout / Spatial Grid Token |
| `--computed-100vh` | `100vh` | Layout / Spatial Grid Token |
| `--computed-100vw` | `calc(100vw - var(--native-scrollbar-width))` | Layout / Spatial Grid Token |
| `--grid-columns` | `32` | Layout / Spatial Grid Token |
| `--grid-gap` | `clamp(12px, 8.412px + 100vw * .0092, 24px)` | Layout / Spatial Grid Token |
| `--grid-half-gap` | `calc(var(--grid-gap)*.5)` | Layout / Spatial Grid Token |
| `--grid-margin` | `clamp(12px, 8.412px + 100vw * .0092, 24px)` | Layout / Spatial Grid Token |
| `--grid-padding` | `calc(var(--grid-margin) - var(--grid-gap)*.5)` | Layout / Spatial Grid Token |
| `--grid-width` | `calc(var(--100vw) - var(--grid-margin)*2)` | Layout / Spatial Grid Token |
| `--modal-width` | `calc(var(--modal-row-width) + var(--grid-half-gap))` | Layout / Spatial Grid Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--color-geral-black` | `#000` | Canvas / Surface Token |
| `--color-geral-white` | `#fff` | Canvas / Surface Token |
| `--color-geral-delta-yellow` | `#ffd300` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.lenis> — `deltacafes-com_en`)**:
   - Landmark `<header class="lenis">` (`1440x1127px`) hosting `Delta, coffee with heart · Delta Caf` navigation (`About Delta · The Azores Coffee · Products · The coffee cycle · Delta Sustainability`), DOM attributes (`data-website-id="0f29d428-885f-44b8-ae..."`, `data-onload`, `data-onerror`, `data-hid="googleTagManager"`), and stylesheet rule `first-child { grid-column:1/19;grid-row:1/2;border-radius:max(23.2px,23.2px + 100vw *... }`.
2. **Hero Stage & Focal Lead (<section.main> — `Since 1961, coffee that awakens st`)**:
   - Landmark `<section class="main">` presenting display lead `Since 1961, coffee that awakens stories` and copy excerpt *"coffee that awakens"* over `#2b1b14` canvas and `#fcf3ed` ink.
3. **Primary Showcase & Content Grid (<section.scroller> — `The journey of coffee`)**:
   - Landmark `<section class="scroller">` rendering section `The journey of coffee` with copy *"Delta Cafés was born in Campo Maior from a family’s dream. Today,"*, asset references (`entry.DAMcazEw.css`, `Footer.BmMrv4ac.css`, `TransitionLogoMask.DT4Lfp-V.css`, `TagFlag.BCy09Tyz.css`), and grid rule `.svg-wrapper { position:relative;width:52px;height:22px }`.
4. **Interactive Detail & Feature Matrix (<section.is-ready> — `The Culture of Coffee`)**:
   - Landmark `<section class="is-ready">` framing `The Culture of Coffee` and `Coffee Science Centre` (*"1986 Start of activity in Spain"*) with `#000000` surface cards, `#f7a200` accents, and `path { fill:var(--item-color) }`.
5. **Colophon & Global Directory Footer (<footer.bg-mask-defs> — `https://deltacafes.com/en`)**:
   - Landmark `<footer class="bg-mask-defs">` anchoring `Delta, coffee with heart · Delta` footer links (`About Delta · The Azores Coffee · Products · The coffee cycle · Delta Sustainability`), copy *"Start of activity in Spain"*, and `#cccccc` structural dividers.
