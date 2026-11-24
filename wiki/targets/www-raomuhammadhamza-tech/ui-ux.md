---
title: "UI & UX Architecture: www-raomuhammadhamza-tech"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-raomuhammadhamza-tech

## Overview & Design Identity
- **Target**: `www-raomuhammadhamza-tech` (**Rao Muhammad Hamza, AI Engineer**)
- **Production URL**: [https://www.raomuhammadhamza.tech/](https://www.raomuhammadhamza.tech/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#0f1220` / `#ff9ebb`)
- **Summary**: Rao Muhammad Hamza, AI Engineer. RAG pipelines, LLM orchestration and agentic workflows, built to hold up in production.
- **Total Clean CSS Variables Extracted**: `32` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Space Grotesk`
- **Body Font Stack**: `Space Grotesk`
- **Monospace / Technical Font Stack**: `Space Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 56px`, `line-height: 50.4px`, `font-weight: 700`, `letter-spacing: -1.96px`)
- **Section Heading (`H2`)**: live computed `h3 (primary section heading)` (`font-size: 31.5px`, `line-height: 31.5px`, `font-weight: 600`, `letter-spacing: -1.1025px`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `p` (`letter-spacing: .16em`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--d-mono: "Space Mono", ui-monospace, monospace`, `--l-mono: "Space Mono", ui-monospace, monospace`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#0f1220` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#f4e7e2` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#0b0e17` | `.surface { background: #0b0e17 }` |
| **Interactive Accent / Highlight** | `#ff9ebb` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#b9b2c4` | `var(--muted)` in `:root` |
| **Structural Hairline Border** | `#1d202d` | `var(--grid-line)` in `:root` (`linear-gradient(ffffff0f, ffffff0f)`) |
| **Variable Token (`--screen-ink`)** | `#1b1f33` | `var(--screen-ink)` in `:root` |
| **Variable Token (`--tv-bg`)** | `#161a30` | `var(--tv-bg)` in `:root` |
| **Variable Token (`--tv-bg`)** | `#0c0e1c` | `var(--tv-bg)` in `:root` |
| **Variable Token (`--tv-glow`)** | `#ffffff` | `var(--tv-glow)` in `:root` |
| **Variable Token (`--tv-glow`)** | `#000000` | `var(--tv-glow)` in `:root` |
| **Variable Token (`--d-surf`)** | `#1a1a26` | `var(--d-surf)` in `:root` |
| **Variable Token (`--d-surf2`)** | `#222232` | `var(--d-surf2)` in `:root` |
| **Variable Token (`--d-ink`)** | `#e9e3ef` | `var(--d-ink)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ink` | `#0f1220` | Typography Ink Token |
| `--screen` | `#ff9ebb` | Color / Atmospheric Token |
| `--screen-ink` | `#1b1f33` | Typography Ink Token |
| `--text` | `#f4e7e2` | Typography Ink Token |
| `--muted` | `#b9b2c4` | Color / Atmospheric Token |
| `--tv-edge` | `#ff9ebb33` | Color / Atmospheric Token |
| `--tv-bg` | `linear-gradient(180deg, #161a30db, #0c0e1ce6)` | Canvas / Surface Token |
| `--tv-glow` | `inset 0 0 0 1px #ffffff08, inset 0 0 22px #ff9ebb12, 0 12px 40px #00000073` | Color / Atmospheric Token |
| `--scan` | `repeating-linear-gradient(0deg, #ffffff09 0 1px, transparent 1px 3px)` | Color / Atmospheric Token |
| `--tv-radius` | `12px` | Elevation / Border Token |
| `--grid-line` | `linear-gradient(#ffffff0f, #ffffff0f)` | Layout / Spatial Grid Token |
| `--sheet-bottom` | `84px` | Dimension / Scale Token |
| `--d-surf` | `#1a1a26` | Color / Atmospheric Token |
| `--d-surf2` | `#222232` | Color / Atmospheric Token |
| `--d-line` | `#ffffff14` | Color / Atmospheric Token |
| `--d-ink` | `#e9e3ef` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.ui> — `www-raomuhammadhamza-tech`)**:
   - Landmark `<header class="ui sig">` (`680x228px`) hosting `Rao Muhammad Hamza, AI Engineer` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-sound="on"`, `data-sound="off"`, `data-go="projects"`, `data-go="experience"`), and stylesheet rule `font-face { font-family:Space Mono;src:url(/fonts/SpaceMono-400.woff2)format("woff2"... }`.
2. **Hero Stage & Focal Lead (<section.surface> — `R A O M U H A M M A D H A M Z A`)**:
   - Landmark `<section class="surface desk">` presenting display lead `R A O M U H A M M A D H A M Z A` and copy excerpt *"I build AI that ships."* over `#0f1220` canvas and `#f4e7e2` ink.
3. **Primary Showcase & Content Grid (<article.case> — `R a o M u h a m m a d H a m z a`)**:
   - Landmark `<article class="case">` rendering section `R a o M u h a m m a d H a m z a` with copy *"Drag to look around"*, asset references (`favicon.svg`, `SpaceGrotesk-Variable.woff2`, `index.BGUfTFpU.css`, `edi-poster.webp`), and grid rule `body { color:f4e7e2;background:0f1220;height:100%;font-family:Space Grotesk,sys... }`.
4. **Interactive Detail & Feature Matrix (<article.case:nth(2)> — `ResumeWesume`)**:
   - Landmark `<article class="case">` framing `ResumeWesume` and `Nothing on right now` (*"AI Engineer · Karachi"*) with `#0b0e17` surface cards, `#ff9ebb` accents, and `.loader.done { opacity:0;visibility:hidden }`.
5. **Colophon & Global Directory Footer (<footer.train-chart> — `https://www.raomuhammadhamza.tech/`)**:
   - Landmark `<footer class="train-chart">` anchoring `Rao Muhammad Hamza, AI Engineer` footer links (`Overview · Index · Archive · About · Contact`), copy *"Flat version WebGL isn't available in this browser."*, and `#1d202d` structural dividers.
