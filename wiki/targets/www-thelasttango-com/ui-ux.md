---
title: "UI & UX Architecture: www-thelasttango-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-thelasttango-com

## Overview & Design Identity
- **Target**: `www-thelasttango-com` (**The Last Tango / For the one who made us happy.**)
- **Production URL**: [https://www.thelasttango.com/](https://www.thelasttango.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#030c1c` / `#0000ff`)
- **Summary**: An interactive tribute to Lionel Messi and the World Cup that brought millions of people together again. Every point, every goal, and eve...
- **Total Clean CSS Variables Extracted**: `119` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Cormorant Garamond`
- **Body Font Stack**: `Cormorant Garamond`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5/2.25)`, `--text-6xl: 3.75rem`
- **Section Heading (`H2`)**: observed font-size ladder: `16px`, `80px`, `14px`, `1em`, `80%`
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5/1)`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 14px`, `line-height: 21px`, `font-weight: 500`); CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1/.75)`, `--text-sm: .875rem`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#030c1c` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#f5f5f5` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#000000` | `body { background-color: black }` (`#000000`) |
| **Interactive Accent / Highlight** | `#0000ff` | `.border-blue-600 { border-color: #0000ff }` |
| **Secondary / Muted Copy** | `#808080` | `.text-gray-600 { color: gray }` (`#808080`) |
| **Structural Hairline Border** | `#000000` | `.border-black { border-color: #000000 }` |
| **Variable Token (`--violet`)** | `#5021e9` | `var(--violet)` in `:root` |
| **Variable Token (`--dark`)** | `#17152f` | `var(--dark)` in `:root` |
| **Variable Token (`--white`)** | `#fefefe` | `var(--white)` in `:root` |
| **Variable Token (`--light`)** | `#eef2ff` | `var(--light)` in `:root` |
| **Variable Token (`--focus`)** | `#ddd4f9` | `var(--focus)` in `:root` |
| **Variable Token (`--disabled`)** | `#efefef` | `var(--disabled)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--violet` | `#5021e9` | Color / Atmospheric Token |
| `--dark` | `#17152f` | Canvas / Surface Token |
| `--white` | `#fefefe` | Canvas / Surface Token |
| `--light` | `#eef2ff` | Canvas / Surface Token |
| `--focus` | `#ddd4f9` | Color / Atmospheric Token |
| `--disabled` | `#efefef` | Color / Atmospheric Token |
| `--wrapper` | `100%` | Layout / Spatial Grid Token |
| `--max-w-wrapper` | `1680px` | Layout / Spatial Grid Token |
| `--grid-cols-space` | `28px` | Layout / Spatial Grid Token |
| `--safearea` | `48px` | Dimension / Scale Token |
| `--ctrl-desktop-max-w` | `1920px` | Layout / Spatial Grid Token |
| `--ctrl-tablet-max-w` | `100vw` | Layout / Spatial Grid Token |
| `--ctrl-mobile-max-w` | `100vw` | Layout / Spatial Grid Token |
| `--ctrl-desktop-max-h` | `100vh` | Dimension / Scale Token |
| `--ctrl-tablet-max-h` | `100vh` | Dimension / Scale Token |
| `--ctrl-mobile-max-h` | `90vh` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.z-100000> — `www-thelasttango-com`)**:
   - Landmark `<header class="z-100000 fixed">` (`1440x64px`) hosting `The Last Tango / For the one who mad` navigation (`Esp`), DOM attributes (`data-loader-scroll-lock="true"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<main.lenis> — `The Last Tango / For the one who m`)**:
   - Landmark `<main class="lenis">` presenting display lead `The Last Tango / For the one who made us happy.` and copy excerpt *"0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9"* over `#030c1c` canvas and `#f5f5f5` ink.
3. **Primary Showcase & Content Grid (<main.lenis-stopped> — `Featured Work & Interactive Showca`)**:
   - Landmark `<main class="lenis-stopped">` rendering section `Featured Work & Interactive Showcase` with copy *"0 1 2 3 4 5 6 7 8 9"*, asset references (`187cmj4q350mm.css`, `0eqspdm2dt5_-.css`, `0kkv0xwvqoa86.css`, `14~g0x6k9zzx2.js`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<main.fonts-loaded> — `Technical Architecture & Narrative`)**:
   - Landmark `<main class="fonts-loaded">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Kansas City Stadium , June 17, 2026"*) with `#000000` surface cards, `#0000ff` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.pointer-events-auto> — `https://www.thelasttango.com/`)**:
   - Landmark `<footer class="pointer-events-auto">` anchoring `The Last Tango / For the one who` footer links (`Esp`), copy *"Every goal. Every record. Every moment that marked Messi 's "*, and `#000000` structural dividers.
