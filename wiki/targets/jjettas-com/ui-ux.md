---
title: "UI & UX Architecture: jjettas-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: jjettas-com

## Overview & Design Identity
- **Target**: `jjettas-com` (**Justin Jefferson**)
- **Production URL**: [https://jjettas.com](https://jjettas.com)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#0b0a0f` / `#eeac1a`)
- **Summary**: Justin Jefferson, wide receiver for the Minnesota Vikings. Records, career stats, partnerships, the JJets Foundation and his journal.
- **Total Clean CSS Variables Extracted**: `180` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `fontBody`
- **Body Font Stack**: `fontBody`
- **Monospace / Technical Font Stack**: `fontMono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 15.12px`, `line-height: 23.436px`, `font-weight: 800`, `letter-spacing: 0.1512px`); CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 313.344px`, `line-height: 260.076px`, `font-weight: 700`, `letter-spacing: -9.40032px`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`font-size: calc(20.5 * var(--pu))`)
- **Body Copy**: live computed `body` (`font-size: 15.12px`, `line-height: 23.436px`, `font-weight: 400`, `letter-spacing: 0.1512px`); CSS variables `--font-body-family: "fontBody","fontBody Fallback"`, `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 15.12px`, `line-height: 23.436px`, `font-weight: 400`, `letter-spacing: 0.1512px`); CSS variables `--font-mono-family: "fontMono","fontMono Fallback"`, `--font-numono: "fontNuMono","fontNuMono Fallback"`, `--font-mono: var(--font-mono-family),ui-monospace,SFMono-Regular,Menlo,monospace`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#0b0a0f` | live computed `html` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#f4efe6` | live computed `footer` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#000000` | `.bg-black { background-color: black }` (`#000000`) |
| **Interactive Accent / Highlight** | `#eeac1a` | `var(--color-cta-yellow)` in `:root` |
| **Secondary / Muted Copy** | `#a9a1b5` | `var(--color-purple-muted)` in `:root` |
| **Structural Hairline Border** | `#242327` | `10 { border-color: #242327 }` |
| **Variable Token (`--logo-color`)** | `#f6f3ef` | `var(--logo-color)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--theme-bg` | `var(--color-ink)` | Canvas / Surface Token |
| `--theme-fg` | `var(--color-bone)` | Typography Ink Token |
| `--theme-accent` | `var(--color-gold)` | Brand / Palette Token |
| `--theme-surface` | `var(--color-smoke)` | Canvas / Surface Token |
| `--logo-color` | `#f6f3ef` | Brand / Palette Token |
| `--hamburger-halo` | `drop-shadow(0 1px 5px #0b0a0f8c)` | Color / Atmospheric Token |
| `--pebble-multiply-opacity` | `1` | Design System Custom Token |
| `--pebble-screen-opacity` | `0` | Design System Custom Token |
| `--marquee-opacity` | `0` | Design System Custom Token |
| `--min-h` | `700px` | Dimension / Scale Token |
| `--min-h-phone` | `640px` | Dimension / Scale Token |
| `--content-max` | `1728px` | Dimension / Scale Token |
| `--page-w` | `min(100vw,var(--content-max))` | Dimension / Scale Token |
| `--page-x` | `max(0px,calc((100vw - var(--content-max)) / 2))` | Dimension / Scale Token |
| `--vu` | `min(calc(var(--page-w) / 100),calc(1.8 * max(1vh, var(--min-h) / 100)))` | Dimension / Scale Token |
| `--pu` | `min(1vw,calc(.5 * max(1lvh, var(--min-h-phone) / 100)))` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.pointer-events-none> — `jjettas-com`)**:
   - Landmark `<header class="pointer-events-none inset-x-0">` (`1440x104px`) hosting `Justin Jefferson` navigation (`Home · On-Field On-Field · Off-Field Off-Field · Journal Journal · Inquiries Inquiries`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `.__className_cf619f { font-family:fontBody,fontBody Fallback }`.
2. **Hero Stage & Focal Lead (<section.relative> — `Justin Jefferson`)**:
   - Landmark `<section class="relative w-full">` presenting display lead `Justin Jefferson` and copy excerpt *"From a St. Rose, Louisiana to the Met Gala runway. Every move Jus"* over `#0b0a0f` canvas and `#f4efe6` ink.
3. **Primary Showcase & Content Grid (<section.items-end> — `Signature Moments`)**:
   - Landmark `<section class="items-end relative">` rendering section `Signature Moments` with copy *"F r o m a S t . R o s e , L o u i s i a n a t o t h e M e t G a l"*, asset references (`0ad3faa61cd26fd6-s.p.woff2`, `34310d7f0559b2f8-s.p.woff2`, `45f4bf9bd5d902fa-s.p.woff2`, `c39007f2e37cc928-s.p.otf`), and grid rule `.__variable_cf619f { --font-body-family:"fontBody","fontBody Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.w-full> — `Building something that lasts`)**:
   - Landmark `<section class="relative w-full">` framing `Building something that lasts` and `The JJets Foundation` (*"The 2020 first-round pick out of LSU who rewrote the record books"*) with `#000000` surface cards, `#eeac1a` accents, and `.__className_b92fdb { font-family:fontMono,fontMono Fallback;font-weight:500 }`.
5. **Colophon & Global Directory Footer (<footer.h-auto> — `https://jjettas.com`)**:
   - Landmark `<footer class="h-auto relative">` anchoring `Justin Jefferson` footer links (`Home · On-Field On-Field · Off-Field Off-Field · Journal Journal · Inquiries Inquiries`), copy *"14 REC · 227 YDS · 4 TD"*, and `#242327` structural dividers.
