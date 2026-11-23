---
title: "UI & UX Architecture: patmos-studio"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: patmos-studio

## Overview & Design Identity
- **Target**: `patmos-studio` (**Patmos · Wahr, Gut, Schön**)
- **Production URL**: [https://patmos.studio/](https://patmos.studio/)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000000` canvas, `#e0e0e0` ink, `#ffffff` accent)
- **Summary**: A Gestalting™ practice at the intersection of business and art. Across strategy, organization, branding, design, marketing, product, arch...
- **Total Clean CSS Variables Extracted**: `72` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Patmos Serif`
- **Body Font Stack**: `Patmos Serif`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 15px`, `line-height: 28.5px`, `font-weight: 400`); rule `h1` (`font-weight: 300`)
- **Section Heading (`H2`)**: rule `h2` (`line-height: 1.6`)
- **Body Copy**: live computed `body` (`font-size: 15px`, `line-height: 28.5px`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 15px`, `line-height: 28.5px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#e0e0e0` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#777777` | `#intro .line { background-color: #777777 }` |
| **Interactive Accent / Highlight** | `#ffffff` | `main.top .hero .dom-plane-conta... { color: #ffffff }` |
| **Secondary / Muted Copy** | `#8f8f8f` | `var(--color-fg-muted)` in `:root` |
| **Structural Hairline Border** | `#f2f2f2` | `var(--color-border)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--spacing` | `.0625rem` | Layout / Spatial Grid Token |
| `--spacing-base` | `.9375rem` | Layout / Spatial Grid Token |
| `--spacing-10-11` | `clamp(.625rem,.6016rem + .0935vw,.6875rem)` | Layout / Spatial Grid Token |
| `--spacing-12-13` | `clamp(.75rem,.7266rem + .0935vw,.8125rem)` | Layout / Spatial Grid Token |
| `--spacing-14-16` | `clamp(.875rem,.8283rem + .1869vw,1rem)` | Layout / Spatial Grid Token |
| `--spacing-14-17` | `clamp(.875rem,.8049rem + .2831vw,1.0625rem)` | Layout / Spatial Grid Token |
| `--spacing-15-16` | `clamp(.9375rem,.9141rem + .0935vw,1rem)` | Layout / Spatial Grid Token |
| `--spacing-16-17` | `clamp(1rem,.9765rem + .0935vw,1.0625rem)` | Layout / Spatial Grid Token |
| `--spacing-16-18` | `clamp(1rem,.9533rem + .1869vw,1.125rem)` | Layout / Spatial Grid Token |
| `--spacing-16-19` | `clamp(1rem,.9299rem + .2804vw,1.1875rem)` | Layout / Spatial Grid Token |
| `--spacing-16-20` | `clamp(1rem,.374vw + .907rem,1.25rem)` | Layout / Spatial Grid Token |
| `--spacing-18-20` | `clamp(1.125rem,1.0783rem + .1869vw,1.25rem)` | Layout / Spatial Grid Token |
| `--spacing-20-24` | `clamp(1.25rem,1.1565rem + .3738vw,1.5rem)` | Layout / Spatial Grid Token |
| `--spacing-20-25` | `clamp(1.25rem,1.1332rem + .4673vw,1.5625rem)` | Layout / Spatial Grid Token |
| `--spacing-20-35` | `clamp(1.25rem,.8995rem + 1.4019vw,2.1875rem)` | Layout / Spatial Grid Token |
| `--spacing-25-32` | `clamp(1.5625rem,1.3989rem + .6542vw,2rem)` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.visible> — `patmos-studio`)**:
   - Landmark `<nav class="visible inset-0">` (`1440x900px`) hosting `Patmos · Wahr, Gut, Schön` navigation (`Home · Prologue · Episode · Scene · Epilogue`), DOM attributes (`data-typeface="serif"`, `data-path="/contact/"`, `data-path="/"`, `data-path="/prologue/"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<main.row-span-full> — `( Patmos ) Wahr, Gut, Schön`)**:
   - Landmark `<main class="row-span-full">` presenting display lead `( Patmos ) Wahr, Gut, Schön` and copy excerpt *"Behold, all things new."* over `#000000` canvas and `#e0e0e0` ink.
3. **Primary Showcase & Content Grid (<main.row-span-full:nth(2)> — `Behold, all things new.`)**:
   - Landmark `<main class="row-span-full">` rendering section `Behold, all things new.` with copy *"( Das Wahre, Gute, Schöne )"*, asset references (`dlr2ezd.js`, `favicon.svg`, `apple-touch-icon.png`, `fonts.googleapis.com`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<main.row-span-full:nth(3)> — `( Das Wahre, Gute, Schöne )`)**:
   - Landmark `<main class="row-span-full">` framing `( Das Wahre, Gute, Schöne )` and `patmos-studio Archive & Directory` (*"Behold, all things new."*) with `#777777` surface cards, `#ffffff` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.wf-garamond-premier-pro-n7-active> — `https://patmos.studio/`)**:
   - Landmark `<footer class="wf-garamond-premier-pro-n7-active">` anchoring `Patmos · Wahr, Gut, Schön` footer links (`Home · Prologue · Episode · Scene · Epilogue`), copy *"( Das Wahre, Gute, Schöne )"*, and `#f2f2f2` structural dividers.
