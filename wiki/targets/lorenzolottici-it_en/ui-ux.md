---
title: "UI & UX Architecture: lorenzolottici-it_en"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: lorenzolottici-it_en

## Overview & Design Identity
- **Target**: `lorenzolottici-it_en` (**Lorenzo Lottici · Order in chaos**)
- **Production URL**: [https://lorenzolottici.it/en](https://lorenzolottici.it/en)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×844px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#070707` / `#0000ff`)
- **Summary**: I bring order to the chaos in your business. Outside, a site people recognize at first glance. Inside, automations and AI agents that wor...
- **Total Clean CSS Variables Extracted**: `211` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `archivo`
- **Body Font Stack**: `jetbrainsMono`
- **Monospace / Technical Font Stack**: `jetbrainsMono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 61.92px`, `line-height: 59.4432px`, `font-weight: 600`, `letter-spacing: -1.2384px`); CSS variables `--tipo-display: clamp(2.75rem,calc(1.2708rem + 6.5741vw),7.1875rem)`, `--lh-display: .98`, `--ls-display: -.03em`; rule `h1` (`font-size: var(--tipo-titolo)`, `line-height: var(--lh-titolo)`, `letter-spacing: var(--ls-titolo)`, `font-weight: var(--peso-di...`)
- **Section Heading (`H2`)**: live computed `h3 (primary section heading)` (`font-size: 23.92px`, `line-height: 38.272px`, `font-weight: 600`, `letter-spacing: 0.2392px`); rule `h2` (`font-size: var(--tipo-label)`, `line-height: var(--lh-label)`, `letter-spacing: var(--ls-label)`, `font-weight: var(--peso-la...`)
- **Body Copy**: live computed `body` (`font-size: 16.5005px`, `line-height: 26.4008px`, `font-weight: 400`, `letter-spacing: 1.15503px`); rule `p` (`line-height: var(--lh-corpo)`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 14.016px`, `line-height: 18.9216px`, `font-weight: 400`, `letter-spacing: 1.12128px`); CSS variables `--tipo-label: clamp(.75rem,calc(.7083rem + .1852vw),.875rem)`, `--lh-label: 1.4`, `--ls-label: .18em`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#070707` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#f0ede8` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f0ede8` | live computed `button` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#0000ff` | `.text-blue-500 { color: blue }` (`#0000ff`) |
| **Secondary / Muted Copy** | `#0000ff` | `.text-blue-500 { color: blue }` (`#0000ff`) |
| **Structural Hairline Border** | `#4b2a18` | `30 { border-color: #4b2a18 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--z-banda` | `8000` | Elevation / Border Token |
| `--z-parliamone` | `9000` | Elevation / Border Token |
| `--z-voce-cabina` | `9100` | Elevation / Border Token |
| `--z-passaggio` | `10000` | Elevation / Border Token |
| `--z-velo-scritta` | `10001` | Elevation / Border Token |
| `--z-indice` | `2147480000` | Elevation / Border Token |
| `--z-salta` | `2147480000` | Elevation / Border Token |
| `--gutter` | `clamp(1.25rem,3.4vw,4rem)` | Layout / Spatial Grid Token |
| `--corsia-bordo` | `4rem` | Dimension / Scale Token |
| `--tipo-marchio` | `clamp(6rem,calc(1.3958rem + 20.463vw),19.8125rem)` | Dimension / Scale Token |
| `--tipo-display` | `clamp(2.75rem,calc(1.2708rem + 6.5741vw),7.1875rem)` | Dimension / Scale Token |
| `--tipo-titolo` | `clamp(2.125rem,calc(1.3125rem + 3.6111vw),4.5625rem)` | Dimension / Scale Token |
| `--tipo-sottotitolo` | `clamp(1.625rem,calc(.8542rem + 3.4259vw),3.9375rem)` | Dimension / Scale Token |
| `--tipo-servizio` | `clamp(1.25rem,calc(1.1042rem + .6481vw),1.6875rem)` | Dimension / Scale Token |
| `--tipo-lead` | `var(--tipo-corpo)` | Design System Custom Token |
| `--tipo-corpo` | `clamp(1rem,calc(.9792rem + .0926vw),1.0625rem)` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.indice-home> — `lorenzolottici-it_en`)**:
   - Landmark `<header class="indice-home indice-testata">` (`1440x77px`) hosting `Lorenzo Lottici · Order in chaos` navigation (`What I do · Path · Work · Thinking · Let’s talk`), DOM attributes (`data-testata="1"`, `data-caricamento="1"`, `data-tre="1"`, `data-precedence="next"`), and stylesheet rule `.iLAgaa_colonna { max-width:80rem;margin:0 auto;position:relative }`.
2. **Hero Stage & Focal Lead (<section.dark> — `ORDER IN THE CHAOS OF YOUR PROCESS`)**:
   - Landmark `<section class="dark">` presenting display lead `ORDER IN THE CHAOS OF YOUR PROCESSES. ORDER IN TH...` and copy excerpt *"Creative Developer & Automation Architect"* over `#070707` canvas and `#f0ede8` ink.
3. **Primary Showcase & Content Grid (<section.js> — `Order in the chaos of your process`)**:
   - Landmark `<section class="js">` rendering section `Order in the chaos of your processes. Order in th...` with copy *"Order in the chaos of your processes."*, asset references (`archivo_latin_var-s.p.3b1_7etm2gp...`, `jetbrains_mono_latin_var.p.0gbvn7...`, `polvere-carta.webp`, `420u9fgvjqgpl.js`), and grid rule `.iLAgaa_stelle { border-radius:50%;width:1px;height:1px;position:absolute;top:0;left:0 }`.
4. **Interactive Detail & Feature Matrix (<section.scroll-fermo> — `What I do`)**:
   - Landmark `<section class="scroll-fermo">` framing `What I do` and `Work` (*"Order in the chaos"*) with `#f0ede8` surface cards, `#0000ff` accents, and `.iLAgaa_pianeta { width:120vw;top:-74vw;right:-62vw }`.
5. **Colophon & Global Directory Footer (<footer.su-piede> — `https://lorenzolottici.it/en`)**:
   - Landmark `<footer class="su-piede indice-home">` anchoring `Lorenzo Lottici · Order in chaos` footer links (`What I do · Path · Work · Thinking · Let’s talk`), copy *"of your processes."*, and `#4b2a18` structural dividers.
