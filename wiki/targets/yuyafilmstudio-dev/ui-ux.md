---
title: "UI & UX Architecture: yuyafilmstudio-dev"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: yuyafilmstudio-dev

## Overview & Design Identity
- **Target**: `yuyafilmstudio-dev` (**YUYA FILM STUDIO**)
- **Production URL**: [https://yuyafilmstudio.dev/](https://yuyafilmstudio.dev/)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#0b0b0a` / `#dddddd`)
- **Summary**: Walk through YUYA FILM STUDIO — a working film company built from Yuya's real Video OS, projects and footage.
- **Total Clean CSS Variables Extracted**: `9` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: `Courier Prime`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 44px`, `line-height: 46.64px`, `font-weight: 500`, `letter-spacing: 5.28px`); rule `h1` (`font-size: clamp(30px,3.5vw,44px)`, `line-height: 1.06`, `letter-spacing: .12em`, `font-weight: 500`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 9.5px`, `line-height: normal`, `font-weight: 500`, `letter-spacing: 3.04px`); rule `h2` (`font-size: 9.5px`, `letter-spacing: .32em`, `font-weight: 500`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: 21px`, `line-height: 1.38`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 11.5px`, `line-height: normal`, `font-weight: 600`, `letter-spacing: 3.91px`); CSS variables `--mono: "Courier Prime", "Courier New", monospace`; rule `small` (`font-size: 11px`, `letter-spacing: .01em`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#0b0b0a` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#f2ede4` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#0f0e0c` | `.bf-route li:before { background: #0f0e0c }` |
| **Interactive Accent / Highlight** | `#dddddd` | `.vf-shots button { color: #dddddd }` |
| **Secondary / Muted Copy** | `#a39e94` | `var(--muted)` in `:root` |
| **Structural Hairline Border** | `#5c5a56` | `kbd { border: #5c5a56 }` |
| **Variable Token (`--gold`)** | `#c9a96e` | `var(--gold)` in `:root` |
| **Variable Token (`--gold-dim`)** | `#8c7650` | `var(--gold-dim)` in `:root` |
| **Variable Token (`--rec`)** | `#e0402f` | `var(--rec)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ink` | `#0b0b0a` | Typography Ink Token |
| `--paper` | `#f2ede4` | Canvas / Surface Token |
| `--muted` | `#a39e94` | Color / Atmospheric Token |
| `--gold` | `#c9a96e` | Color / Atmospheric Token |
| `--gold-dim` | `#8c7650` | Color / Atmospheric Token |
| `--rec` | `#e0402f` | Color / Atmospheric Token |
| `--serif` | `"Cormorant Garamond", "Baskerville", Georgia, serif` | Typography / Scale Token |
| `--sans` | `"Inter", "Helvetica Neue", Arial, sans-serif` | Typography / Scale Token |
| `--mono` | `"Courier Prime", "Courier New", monospace` | Typography / Scale Token |
| `--yuyafilmstudio-d-bg` | `#0b0b0a` | Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) |
| `--yuyafilmstudio-d-ink` | `#f2ede4` | Primary Typography Ink (computed-derived) |
| `--yuyafilmstudio-d-surface` | `#0f0e0c` | Surface Substrate (computed-derived) |
| `--yuyafilmstudio-d-accent` | `#dddddd` | Interactive Accent (computed-derived) |
| `--yuyafilmstudio-d-muted` | `#a39e94` | Secondary Ink (computed-derived) |
| `--yuyafilmstudio-d-border` | `#5c5a56` | Structural Border (computed-derived) |
| `--yuyafilmstudio-d-container` | `1400px` | Container Bound (computed-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.bf-top> — `yuyafilmstudio-dev`)**:
   - Landmark `<header class="bf-top">` (`1120x47px`) hosting `YUYA FILM STUDIO` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-sdkn="@vercel/analytics"`, `data-sdkv="2.0.1"`, `data-engine="three.js r180"`, `data-k="KeyV"`), and stylesheet rule `gl { position:fixed;inset:0;width:100vw;height:100vh;display:block;outline:none }`.
2. **Hero Stage & Focal Lead (<section.bf-id> — `YUYA FILM STUDIO`)**:
   - Landmark `<section class="bf-id">` presenting display lead `YUYA FILM STUDIO` and copy excerpt *"Explore the studio, interact with the production process, and fol"* over `#0b0b0a` canvas and `#f2ede4` ink.
3. **Primary Showcase & Content Grid (<section.bf-controls> — `MOVE`)**:
   - Landmark `<section class="bf-controls">` rendering section `MOVE` with copy *"VISITOR ACCESS / STUDIO TOUR"*, asset references (`index-BGb4Src9.js`, `index-C-QYK-dA.css`, `script.js`), and grid rule `.hidden { display:none!important }`.
4. **Interactive Detail & Feature Matrix (<section.bf-map> — `EXPLORE`)**:
   - Landmark `<section class="bf-map">` framing `EXPLORE` and `OBJECTS` (*"ENTER YUYA FILM STUDIO"*) with `#0f0e0c` surface cards, `#dddddd` accents, and `button { font-family:var(--sans);cursor:pointer }`.
5. **Colophon & Global Directory Footer (<footer.bf-foot> — `https://yuyafilmstudio.dev/`)**:
   - Landmark `<footer class="bf-foot">` anchoring `YUYA FILM STUDIO` footer links (`Overview · Index · Archive · About · Contact`), copy *"Pulling stills from the ÉCLAT edit…"*, and `#5c5a56` structural dividers.
