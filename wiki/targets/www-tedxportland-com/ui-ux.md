---
title: "UI & UX Architecture: www-tedxportland-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-tedxportland-com

## Overview & Design Identity
- **Target**: `www-tedxportland-com` (**TEDxPortland**)
- **Production URL**: [https://www.tedxportland.com/](https://www.tedxportland.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#ff0000`)
- **Summary**: TEDxPortland is a nonprofit organization in Portland, OR that seeks to build community and provide a platform for every discipline and cu...
- **Total Clean CSS Variables Extracted**: `85` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Helvetica Neue`
- **Body Font Stack**: `Helvetica Neue`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 36px`, `line-height: 45px`, `font-weight: 700`); CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 36px`, `line-height: 45px`, `font-weight: 700`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`font-size: 1.5rem`)
- **Body Copy**: live computed `body` (`font-size: 20px`, `line-height: 29px`, `font-weight: 400`); CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`; rule `body` (`font-size: clamp(1.05rem, 0.95rem + 0.35...`, `line-height: 1.45`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 20px`, `line-height: 29px`, `font-weight: 400`); CSS variables `--font-mono: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono",`, `--text-xs: 0.75rem`, `--text-xs--line-height: calc(1 / 0.75)`; rule `small` (`font-size: 80%`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#151515` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#808080` | `.bg-dark-grey { background-color: grey }` (`#808080`) |
| **Interactive Accent / Highlight** | `#ff0000` | `.bg-ted-red { background-color: red }` (`#ff0000`) |
| **Secondary / Muted Copy** | `#808080` | `.text-dark-grey { color: grey }` (`#808080`) |
| **Structural Hairline Border** | `#000000` | `.border-ted-black { border-color: #000000 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-sans` | `'Helvetica Neue', Helvetica, Inter, Arial, sans-serif` | Typography / Scale Token |
| `--font-mono` | `ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono",` | Typography / Scale Token |
| `--color-amber-50` | `oklch(98.7% 0.022 95.277)` | Brand / Palette Token |
| `--color-amber-300` | `oklch(87.9% 0.169 91.605)` | Brand / Palette Token |
| `--color-amber-800` | `oklch(47.3% 0.137 46.201)` | Brand / Palette Token |
| `--color-green-600` | `oklch(62.7% 0.194 149.214)` | Brand / Palette Token |
| `--color-sky-50` | `oklch(97.7% 0.013 236.62)` | Brand / Palette Token |
| `--color-sky-300` | `oklch(82.8% 0.111 230.318)` | Brand / Palette Token |
| `--color-sky-800` | `oklch(44.3% 0.11 240.79)` | Brand / Palette Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `0.25rem` | Layout / Spatial Grid Token |
| `--container-md` | `28rem` | Layout / Spatial Grid Token |
| `--container-2xl` | `42rem` | Layout / Spatial Grid Token |
| `--container-3xl` | `48rem` | Layout / Spatial Grid Token |
| `--container-4xl` | `56rem` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `www-tedxportland-com`)**:
   - Landmark `<header class="site-header top-0">` (`1425x72px`) hosting `TEDxPortland` navigation (`About · Gallery · Films · Salons · Patron Society`), DOM attributes (`data-nav="wide"`, `data-header-row`, `data-primary-nav`, `data-evt-event="Tickets on sale for M..."`), and stylesheet rule `file-selector-button { box-sizing: border-box; margin: 0; padding: 0; border: 0 solid; }`.
2. **Hero Stage & Focal Lead (<section.relative> — `Our Legacy`)**:
   - Landmark `<section class="relative z-30">` presenting display lead `Our Legacy` and copy excerpt *"Since 1984, TED has brought together bold innovators, creators, a"* over `#ffffff` canvas and `#151515` ink.
3. **Primary Showcase & Content Grid (<section.scroll-mt-20> — `Tickets On Sale Now:`)**:
   - Landmark `<section class="scroll-mt-20 px-3">` rendering section `Tickets On Sale Now:` with copy *"Tickets on sale for May 29, 2027"*, asset references (`0f458eb0-7b6e-4fd8-8afb-49134387e...`, `favicon-16x16.png`, `favicon-32x32.png`, `favicon-96x96.png`), and grid rule `hr { height: 0; color: inherit; border-top-width: 1px; }`.
4. **Interactive Detail & Feature Matrix (<section.bg-white> — `TEDxPortland Salons & Special Even`)**:
   - Landmark `<section class="scroll-mt-20 bg-white">` framing `TEDxPortland Salons & Special Events` and `Support TEDxPortland` (*"May 29th, 2027 Year 15 - THEME-NOT-YET-REVEALED Portland Art Muse"*) with `#808080` surface cards, `#ff0000` accents, and `h6 { font-size: inherit; font-weight: inherit; }`.
5. **Colophon & Global Directory Footer (<footer.mt-16> — `https://www.tedxportland.com/`)**:
   - Landmark `<footer class="mt-16 bg-ted-black">` anchoring `TEDxPortland` footer links (`About · Gallery · Films · Salons · Patron Society`), copy *"The TEDx movement began in 2009, extending that spirit to lo"*, and `#000000` structural dividers.
