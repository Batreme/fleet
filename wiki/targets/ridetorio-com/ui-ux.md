---
title: "UI & UX Architecture: ridetorio-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: ridetorio-com

## Overview & Design Identity
- **Target**: `ridetorio-com` (**The Ride to Rio · Bicycle documentary, Los Angeles to Rio**)
- **Production URL**: [https://ridetorio.com/](https://ridetorio.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f4ead0` / `#ff0000`)
- **Summary**: A documentary about five friends who cycled 10,000 miles from Los Angeles to Rio de Janeiro. Watch the trailers and full film, and follow...
- **Total Clean CSS Variables Extracted**: `25` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Alfa Slab One`
- **Body Font Stack**: `Fraunces`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 242.4px`, `line-height: 208.464px`, `font-weight: 400`, `letter-spacing: -2.424px`)
- **Section Heading (`H2`)**: live computed `h3 (primary section heading)` (`font-size: 40px`, `line-height: 48px`, `font-weight: 400`, `letter-spacing: 2.4px`)
- **Body Copy**: live computed `body` (`font-size: 20.48px`, `line-height: 31.744px`, `font-weight: 400`); CSS variables `--font-body: "Fraunces", "Iowan Old Style", Georgia, serif`; rule `body` (`font-size: clamp(1.06rem, 0.98rem + 0.34...`, `line-height: 1.55`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 20.48px`, `line-height: 31.744px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f4ead0` | live computed `html` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#1e1b16` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#fbf4df` | `var(--paper-2)` in `:root` |
| **Interactive Accent / Highlight** | `#ff0000` | `.btn--primary { background: red }` (`#ff0000`) |
| **Secondary / Muted Copy** | `#c8452c` | live computed `h2` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#fff6e4` | `.btn--ghost { border-color: #fff6e4 }` |
| **Variable Token (`--ink-soft`)** | `#4a4337` | `var(--ink-soft)` in `:root` |
| **Variable Token (`--olive`)** | `#8c9a4a` | `var(--olive)` in `:root` |
| **Variable Token (`--forest`)** | `#2f4a2c` | `var(--forest)` in `:root` |
| **Variable Token (`--mustard`)** | `#d9a93b` | `var(--mustard)` in `:root` |
| **Variable Token (`--teal`)** | `#2f8f8b` | `var(--teal)` in `:root` |
| **Variable Token (`--sky`)** | `#a9d3de` | `var(--sky)` in `:root` |
| **Variable Token (`--dusk`)** | `#f2a27c` | `var(--dusk)` in `:root` |
| **Variable Token (`--night`)** | `#16233a` | `var(--night)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--paper` | `#F4EAD0` | Canvas / Surface Token |
| `--paper-2` | `#FBF4DF` | Canvas / Surface Token |
| `--ink` | `#1E1B16` | Typography Ink Token |
| `--ink-soft` | `#4A4337` | Typography Ink Token |
| `--olive` | `#8C9A4A` | Color / Atmospheric Token |
| `--forest` | `#2F4A2C` | Color / Atmospheric Token |
| `--mustard` | `#D9A93B` | Color / Atmospheric Token |
| `--teal` | `#2F8F8B` | Color / Atmospheric Token |
| `--red` | `#C8452C` | Color / Atmospheric Token |
| `--sky` | `#A9D3DE` | Color / Atmospheric Token |
| `--dusk` | `#F2A27C` | Color / Atmospheric Token |
| `--night` | `#16233A` | Color / Atmospheric Token |
| `--sky-top` | `var(--paper)` | Design System Custom Token |
| `--sky-bot` | `var(--paper)` | Design System Custom Token |
| `--stars` | `0` | Design System Custom Token |
| `--font-body` | `"Fraunces", "Iowan Old Style", Georgia, serif` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.nav> — `ridetorio-com`)**:
   - Landmark `<header class="nav">` (`502x49px`) hosting `The Ride to Rio · Bicycle documentar` navigation (`Trailers · Story · Journey · Film · Contact`), DOM attributes (`data-nav`, `data-hero-video`, `data-play="trailer-2"`, `data-reveal`), and stylesheet rule `after { box-sizing: border-box; }`.
2. **Hero Stage & Focal Lead (<section.hero> — `The RIDE to RIO`)**:
   - Landmark `<section class="hero">` presenting display lead `The RIDE to RIO` and copy excerpt *"LOS ANGELES → TO RIO DE JANEIRO · 2012–13"* over `#f4ead0` canvas and `#1e1b16` ink.
3. **Primary Showcase & Content Grid (<section.reel> — `The Ride to Rio`)**:
   - Landmark `<section class="reel">` rendering section `The Ride to Rio` with copy *"Los Angeles → to Rio de Janeiro · 2012–13"*, asset references (`favicon.svg`, `apple-touch-icon.png`, `site.webmanifest`, `fraunces-normal-latin.woff2`), and grid rule `html { background: var(--paper); -webkit-text-size-adjust: 100%; scroll-padding... }`.
4. **Interactive Detail & Feature Matrix (<section.story> — `Also showing`)**:
   - Landmark `<section class="story">` framing `Also showing` and `How to cycle to Brazil without really knowing how...` (*"Four friends (five, by Panama), thirteen countries and ten thousa"*) with `#fbf4df` surface cards, `#ff0000` accents, and `canvas { display: block; max-width: 100%; }`.
5. **Colophon & Global Directory Footer (<footer.atmos__sky> — `https://ridetorio.com/`)**:
   - Landmark `<footer class="atmos__sky">` anchoring `The Ride to Rio · Bicycle docume` footer links (`Trailers · Story · Journey · Film · Contact`), copy *"2012 The Teaser Made in Los Angeles four months before we le"*, and `#fff6e4` structural dividers.
