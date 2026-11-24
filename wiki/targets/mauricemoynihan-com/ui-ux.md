---
title: "UI & UX Architecture: mauricemoynihan-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: mauricemoynihan-com

## Overview & Design Identity
- **Target**: `mauricemoynihan-com` (**Maurice Moynihan**)
- **Production URL**: [https://mauricemoynihan.com](https://mauricemoynihan.com)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×828px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#efede6` / `#ff0000`)
- **Summary**: Advertising creative director, Melbourne. A portfolio. Some of it won things. It also has an album, which hasn’t.
- **Total Clean CSS Variables Extracted**: `25` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Archivo`
- **Body Font Stack**: `Archivo`
- **Monospace / Technical Font Stack**: `Space Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 117.36px`, `line-height: 100.93px`, `font-weight: 900`, `letter-spacing: -4.45968px`); rule `h1` (`font-size: clamp(1.9rem,5.2vw,4.4rem)`, `line-height: 1.02`, `letter-spacing: -.02em`, `font-weight: 900`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(2rem,7vw,5.2rem)`, `line-height: .92`, `letter-spacing: -.02em`, `font-weight: 900`)
- **Body Copy**: live computed `body` (`font-size: 17px`, `line-height: 26.35px`, `font-weight: 400`); rule `body` (`font-size: 1.0625rem`, `line-height: 1.55`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 17px`, `line-height: 26.35px`, `font-weight: 400`); CSS variables `--mono: "Space Mono","Courier New",monospace`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#efede6` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#161511` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `var(--paper)` in `:root` |
| **Interactive Accent / Highlight** | `#ff0000` | `.nav a:hover { color: red }` (`#ff0000`) |
| **Secondary / Muted Copy** | `#4c4a43` | `var(--ink-soft)` in `:root` |
| **Structural Hairline Border** | `#a3a19b` | `.about-hero h1 a { border-bottom: #a3a19b }` |
| **Variable Token (`--bone-deep`)** | `#e6e3d9` | `var(--bone-deep)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bone` | `#EFEDE6` | Color / Atmospheric Token |
| `--bone-deep` | `#E6E3D9` | Color / Atmospheric Token |
| `--ink` | `#161511` | Typography Ink Token |
| `--ink-soft` | `#4c4a43` | Typography Ink Token |
| `--red` | `#161511` | Color / Atmospheric Token |
| `--red-deep` | `#161511` | Color / Atmospheric Token |
| `--red-lift` | `#EFEDE6` | Color / Atmospheric Token |
| `--paper` | `#FFFFFF` | Canvas / Surface Token |
| `--sans` | `"Archivo","Helvetica Neue",Helvetica,Arial,sans-serif` | Typography / Scale Token |
| `--mono` | `"Space Mono","Courier New",monospace` | Typography / Scale Token |
| `--serif` | `"Archivo","Helvetica Neue",Helvetica,Arial,sans-serif` | Typography / Scale Token |
| `--pad` | `clamp(1rem, 3.4vw, 3rem)` | Layout / Spatial Grid Token |
| `--hair` | `1.5px solid var(--ink)` | Dimension / Scale Token |
| `--card` | `clamp(7rem,13.2vw,11.5rem)` | Dimension / Scale Token |
| `--shelf-pad` | `clamp(1rem,3vh,2.4rem)` | Layout / Spatial Grid Token |
| `--shelf` | `calc(var(--card) * 1.22 + var(--shelf-pad) + var(--nav-h) + 1.6rem + 1.8vw)` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.nav> — `mauricemoynihan-com`)**:
   - Landmark `<header class="nav nav--home">` (`1440x49px`) hosting `Maurice Moynihan` navigation (`Advertising · adnauseum.ai · Music · About`), DOM attributes (`data-src="assets/koi/koi_a.webp"`, `data-src2="assets/koi/koi_b.webp"`, `data-panel`, `data-ink-top="0.7539"`), and stylesheet rule `html { scroll-behavior:smooth; }`.
2. **Hero Stage & Focal Lead (<section.hero> — `MAURICE MOYNIHAN`)**:
   - Landmark `<section class="hero">` presenting display lead `MAURICE MOYNIHAN` and copy excerpt *"is a Creative Director, Songwriter and Governor of the Central Ba"* over `#efede6` canvas and `#161511` ink.
3. **Primary Showcase & Content Grid (<section.hero:nth(2)> — `Maurice Moynihan`)**:
   - Landmark `<section class="hero">` rendering section `Maurice Moynihan` with copy *"is a Creative Director, Songwriter and Governor of the Central Ba"*, asset references (`apple-touch-icon.png`, `fonts.googleapis.com`, `fonts.gstatic.com`, `css2`), and grid rule `video { max-width:100%;display:block; }`.
4. **Interactive Detail & Feature Matrix (<section.hero:nth(3)> — `is a Creative Director, Songwriter`)**:
   - Landmark `<section class="hero">` framing `is a Creative Director, Songwriter and Governor ` and `Things that made people buy other things.` (*"Things that made people buy other things."*) with `#ffffff` surface cards, `#ff0000` accents, and `selection { background:var(--red);color:var(--bone); }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://mauricemoynihan.com`)**:
   - Landmark `<footer class="footer">` anchoring `Maurice Moynihan` footer links (`Advertising · adnauseum.ai · Music · About`), copy *"It's not stealing if they put it in an award annual."*, and `#a3a19b` structural dividers.
