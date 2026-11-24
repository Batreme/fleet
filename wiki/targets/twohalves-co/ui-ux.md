---
title: "UI & UX Architecture: twohalves-co"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: twohalves-co

## Overview & Design Identity
- **Target**: `twohalves-co` (**Two Halves — design & development studio, Cairo**)
- **Production URL**: [https://twohalves.co/](https://twohalves.co/)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1280×828px`, Mobile `390×2616px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#fff5ee`)
- **Summary**: We design and build websites people remember — motion, 3D and stories — for brands in Egypt and everywhere.
- **Total Clean CSS Variables Extracted**: `28` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `aileron`
- **Body Font Stack**: `aileron`
- **Monospace / Technical Font Stack**: `Cutive Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 15px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--font-display-src: "Cutive Mono", "Cutive Mono Fallback"`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 123.84px`, `line-height: 121.363px`, `font-weight: 700`, `letter-spacing: -3.7152px`)
- **Body Copy**: live computed `body` (`font-size: 15px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--font-body-src: "aileron", "aileron Fallback"`; rule `p` (`font-size: clamp(20px,1.9vw,30px)`, `line-height: 1.3`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 15px`, `line-height: 24px`, `font-weight: 400`); rule `small` (`font-size: .55em`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `html` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#fff5ee` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#1c1b1a` | `.wk-link { background: #1c1b1a }` |
| **Interactive Accent / Highlight** | `#fff5ee` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#161616` | `var(--ink-3)` in `:root` |
| **Structural Hairline Border** | `#292726` | `var(--line)` in `:root` (`fff5ee29`) |
| **Variable Token (`--paper-2`)** | `#f2e9e2` | `var(--paper-2)` in `:root` |
| **Variable Token (`--mute`)** | `#9a9a9a` | `var(--mute)` in `:root` |
| **Variable Token (`--mute-2`)** | `#6e6e6e` | `var(--mute-2)` in `:root` |
| **Variable Token (`--crease`)** | `#8c8c8c` | `var(--crease)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ink` | `#000` | Typography Ink Token |
| `--ink-2` | `#000` | Typography Ink Token |
| `--ink-3` | `#161616` | Typography Ink Token |
| `--paper` | `#fff5ee` | Canvas / Surface Token |
| `--paper-2` | `#f2e9e2` | Canvas / Surface Token |
| `--white` | `#fff5ee` | Canvas / Surface Token |
| `--mute` | `#9a9a9a` | Color / Atmospheric Token |
| `--mute-2` | `#6e6e6e` | Color / Atmospheric Token |
| `--crease` | `#8c8c8c` | Motion / Easing Token |
| `--fill` | `#fff5ee` | Color / Atmospheric Token |
| `--on-fill` | `#000` | Color / Atmospheric Token |
| `--seam` | `#8c8c8c` | Color / Atmospheric Token |
| `--line` | `#fff5ee29` | Color / Atmospheric Token |
| `--line-ink` | `#00000024` | Typography Ink Token |
| `--font-head` | `var(--font-display)` | Typography / Scale Token |
| `--pad` | `clamp(16px, 3vw, 44px)` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.nav> — `twohalves-co`)**:
   - Landmark `<header class="nav">` (`1440x68px`) hosting `Two Halves — design & development st` navigation (`Work · Services · Studio · Contact`), DOM attributes (`data-precedence="next"`, `data-tone="split"`, `data-hide="0"`, `data-side="a"`), and stylesheet rule `.oFPQLq_className { font-family:Cutive Mono,Cutive Mono Fallback;font-style:normal;font-weig... }`.
2. **Hero Stage & Focal Lead (<section.hero> — `You build it Physically, Two Halve`)**:
   - Landmark `<section class="hero">` presenting display lead `You build it Physically, Two Halves — websites de...` and copy excerpt *"Click a cube to open it, or hold it to turn it Scroll for the wor"* over `#000000` canvas and `#fff5ee` ink.
3. **Primary Showcase & Content Grid (<section.st> — `Work that moves.`)**:
   - Landmark `<section class="st">` rendering section `Work that moves.` with copy *"Click a cube to open it, or hold it to turn it"*, asset references (`512857af647c3544-s.p.25m0iq9x76hr...`, `aileron_latin_400_normal-s.p.1kb3...`, `aileron_latin_700_normal-s.p.1x-w...`, `nt_voice_500_normal-s.p.01xo7g1oe...`), and grid rule `.oFPQLq_variable { --font-display-src:"Cutive Mono", "Cutive Mono Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.wk> — `What we make.`)**:
   - Landmark `<section class="wk">` framing `What we make.` and `Websites that move` (*"Scroll for the work ↓"*) with `#1c1b1a` surface cards, `#fff5ee` accents, and `.n4YeuW_className { font-family:aileron,aileron Fallback }`.
5. **Colophon & Global Directory Footer (<footer.foot> — `https://twohalves.co/`)**:
   - Landmark `<footer class="foot">` anchoring `Two Halves — design & developmen` footer links (`Work · Services · Studio · Contact`), copy *"You build it Physically, Two Halves — websites designed & bu"*, and `#292726` structural dividers.
