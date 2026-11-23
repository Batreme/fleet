---
title: "UI & UX Architecture: labellavista-es"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: labellavista-es

## Overview & Design Identity
- **Target**: `labellavista-es` (**LABELLAVISTA — Creative production co.**)
- **Production URL**: [https://labellavista.es/](https://labellavista.es/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#2f4a8a` canvas, `#ffffff` ink, `#e2d6c0` accent)
- **Summary**: LABELLAVISTA is a creative production co. based in Galicia and Madrid: music videos, commercials and films, shot wherever the story is.
- **Total Clean CSS Variables Extracted**: `36` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Archivo`
- **Body Font Stack**: `Archivo`
- **Monospace / Technical Font Stack**: `DM Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 31.68px`, `line-height: 44.352px`, `font-weight: 700`); CSS variables `--display: clamp(64px, 9vw, 160px)`
- **Section Heading (`H2`)**: observed font-size ladder: `31.68px`, `15.84px`, `12px`, `var(--body)`, `var(--ui)`
- **Body Copy**: live computed `body` (`font-size: 15.84px`, `line-height: 22.176px`, `font-weight: 400`); CSS variables `--body: clamp(15px, 1.1vw, 17px)`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 15.84px`, `line-height: 22.176px`, `font-weight: 400`); CSS variables `--font-mono: var(--font-dm-mono), ui-monospace, "Courier New", monospace`, `--font-dm-mono: "DM Mono", "DM Mono Fallback"`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#2f4a8a` | live computed `html` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `nav` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#0000ff` | `html { background: blue }` (`#0000ff`) |
| **Interactive Accent / Highlight** | `#e2d6c0` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#e2d6c0` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#65749a` | `var(--line)` in `:root` (`e2d6c04d`) |
| **Variable Token (`--black`)** | `#0a0a0a` | `var(--black)` in `:root` |
| **Variable Token (`--paper`)** | `#eee9de` | `var(--paper)` in `:root` |
| **Variable Token (`--ink`)** | `#111111` | `var(--ink)` in `:root` |
| **Variable Token (`--blue-lift`)** | `#6e8fd6` | `var(--blue-lift)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--black` | `#0a0a0a` | Canvas / Surface Token |
| `--paper` | `#eee9de` | Canvas / Surface Token |
| `--ink` | `#111` | Typography Ink Token |
| `--white` | `#fff` | Canvas / Surface Token |
| `--blue` | `#2f4a8a` | Color / Atmospheric Token |
| `--blue-lift` | `#6e8fd6` | Color / Atmospheric Token |
| `--cream` | `#e2d6c0` | Color / Atmospheric Token |
| `--font-sans` | `var(--font-archivo), system-ui, -apple-system, "Segoe UI", sans-serif` | Typography / Scale Token |
| `--font-mono` | `var(--font-dm-mono), ui-monospace, "Courier New", monospace` | Typography / Scale Token |
| `--display` | `clamp(64px, 9vw, 160px)` | Dimension / Scale Token |
| `--section` | `clamp(32px, 2.8vw, 40px)` | Dimension / Scale Token |
| `--body` | `clamp(15px, 1.1vw, 17px)` | Dimension / Scale Token |
| `--ui` | `11px` | Dimension / Scale Token |
| `--margin` | `24px` | Layout / Spatial Grid Token |
| `--gutter` | `24px` | Layout / Spatial Grid Token |
| `--bar` | `48px` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.bar> — `labellavista-es`)**:
   - Landmark `<header class="bar">` (`1440x48px`) hosting `LABELLAVISTA — Creative production c` navigation (`MUSIC VIDEOS · COMMERCIALS · FILMS · STUDIO · CONTACT`), DOM attributes (`data-cover`, `data-precedence="next"`, `data-room="dark"`, `data-hidden="false"`), and stylesheet rule `hivo_8c2be2a3-module__iX1fDW__cla... { font-family:Archivo,Archivo Fallback;font-style:normal }`.
2. **Hero Stage & Focal Lead (<section.reel> — `LABELLAVISTA`)**:
   - Landmark `<section class="reel">` presenting display lead `LABELLAVISTA` and copy excerpt *"PLEASE LOWER YOUR WINDOW SHADE"* over `#2f4a8a` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.reel:nth(2)> — `PLEASE LOWER YOUR WINDOW SHADE`)**:
   - Landmark `<section class="reel">` rendering section `PLEASE LOWER YOUR WINDOW SHADE` with copy *"BV 009 SÉ FELIZ X MI · Christian Nodal"*, asset references (`21ca8f3f56c22ca2-s.p.1cp9-4nby68j...`, `36363bfb06833f56-s.p.38hmww4cj4vm...`, `cabin-window.webp`, `cabin-shade.webp`), and grid rule `chivo_8c2be2a3-module__iX1fDW__va... { --font-archivo:"Archivo", "Archivo Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.reel:nth(3)> — `BV 009 SÉ FELIZ X MI · Christian N`)**:
   - Landmark `<section class="reel">` framing `BV 009 SÉ FELIZ X MI · Christian Nodal` and `BV 013 Non Sei Como · The Rapants ft. Joe Crepús` (*"BV 013 Non Sei Como · The Rapants ft. Joe Crepúsculo"*) with `#0000ff` surface cards, `#e2d6c0` accents, and `mono_685a951c-module__v6oBuq__cla... { font-family:DM Mono,DM Mono Fallback;font-style:normal;font-weight:400 }`.
5. **Colophon & Global Directory Footer (<footer.foot> — `https://labellavista.es/`)**:
   - Landmark `<footer class="foot ui">` anchoring `LABELLAVISTA — Creative producti` footer links (`MUSIC VIDEOS · COMMERCIALS · FILMS · STUDIO · CONTACT`), copy *"· The Rapants ft. Joe Crepúsculo"*, and `#65749a` structural dividers.
