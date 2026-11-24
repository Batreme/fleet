---
title: "UI & UX Architecture: www-designbomb-it"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: www-designbomb-it

## Overview & Design Identity
- **Target**: `www-designbomb-it` (**Design Bomb Festival**)
- **Production URL**: [https://www.designbomb.it/](https://www.designbomb.it/)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×1744px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#141414` / `#0000ee`)
- **Summary**: The Wave presenta la nuova edizione di Design Bomb, che cresce e diventa festival. 22-23-24 Maggio, Catania.
- **Total Clean CSS Variables Extracted**: `36` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `PP Frama Extrabold Italic`
- **Body Font Stack**: `PP Frama Regular`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: observed font-size ladder: `12px`, `16px`, `var(--font-size)`, `var(--framer-font-size)`, `1px`
- **Section Heading (`H2`)**: observed font-size ladder: `12px`, `16px`, `var(--font-size)`, `var(--framer-font-size)`, `1px`
- **Body Copy**: live computed `body` (`font-size: 12px`, `line-height: normal`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 12px`, `line-height: normal`, `font-weight: 400`); CSS variables `--letter-spacing: var(--framer-letter-spacing)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#141414` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#f7f6eb` | live computed `p` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ceff00` | `.framer-hw4kQ.framer-1zonqd { background-color: #ceff00 }` |
| **Interactive Accent / Highlight** | `#0000ee` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#000000` | live computed `body` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#f7f6eb` | `var(--border-color)` in `:root` |
| **Variable Token (`--token-0689d26c-723f-45fc-b97a-089acbcfc796`)** | `#4a60ff` | `var(--token-0689d26c-723f-45fc-b97a-089acbcfc796)` in `:root` |
| **Variable Token (`--token-4809db6f-b397-4188-a942-074244c77dac`)** | `#ff3eba` | `var(--token-4809db6f-b397-4188-a942-074244c77dac)` in `:root` |
| **Variable Token (`--token-797c06e2-082b-4d59-9429-4a87c1a6bdd2`)** | `#31a362` | `var(--token-797c06e2-082b-4d59-9429-4a87c1a6bdd2)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--token-0689d26c-723f-45fc-b97a-089acbcfc796` | `#4a60ff` | Color / Atmospheric Token |
| `--token-7cb9fefc-a8e8-4059-91ee-bd65906318ee` | `#ceff00` | Color / Atmospheric Token |
| `--token-4809db6f-b397-4188-a942-074244c77dac` | `#ff3eba` | Color / Atmospheric Token |
| `--token-797c06e2-082b-4d59-9429-4a87c1a6bdd2` | `#31a362` | Color / Atmospheric Token |
| `--token-f1aabd16-a90b-4a64-bd76-31330e5c4d0f` | `#f7f6eb` | Color / Atmospheric Token |
| `--token-cd7ed41b-0134-43b6-beec-bf340d65ac87` | `#141414` | Color / Atmospheric Token |
| `--token-8e1f8495-735c-4bc6-8090-6a9a9f74db16` | `#141414` | Color / Atmospheric Token |
| `--text-decoration-skip-ink` | `var(--framer-text-decoration-skip-ink)` | Typography Ink Token |
| `--text-underline-offset` | `var(--framer-text-decoration-offset)` | Typography Ink Token |
| `--font-family` | `var(--framer-font-family)` | Typography / Scale Token |
| `--font-style` | `var(--framer-font-style)` | Typography / Scale Token |
| `--font-weight` | `var(--framer-font-weight)` | Typography / Scale Token |
| `--text-color` | `var(--framer-text-color)` | Typography Ink Token |
| `--letter-spacing` | `var(--framer-letter-spacing)` | Typography / Scale Token |
| `--font-size` | `var(--framer-font-size)` | Typography / Scale Token |
| `--text-transform` | `var(--framer-text-transform)` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.lenis> — `www-designbomb-it`)**:
   - Landmark `<header class="lenis">` (`1440px`) hosting `Design Bomb Festival` navigation (`Programma · Workshop · cameretta · Shop · TICKET`), DOM attributes (`data-framer-font-css`, `data-framer-breakpoint-css`, `data-framer-css-ssr-minified`, `data-framer-components="framer-lib-cursors-ho..."`), and stylesheet rule `.hidden-16glhda { display:none!important }`.
2. **Hero Stage & Focal Lead (<section.framer-hw4kQ> — `Design Bomb Festival`)**:
   - Landmark `<section class="framer-hw4kQ">` presenting display lead `Design Bomb Festival` and copy excerpt *"Un festival per tutta la community"* over `#141414` canvas and `#f7f6eb` ink.
3. **Primary Showcase & Content Grid (<section.framer-6q1hH> — `Featured Work & Interactive Showca`)**:
   - Landmark `<section class="framer-6q1hH">` rendering section `Featured Work & Interactive Showcase` with copy *"Un festival per tutta"*, asset references (`CHxdCbEfx7lZs5B6CqTOXcfZQo.jpg`, `script`, `sNmVGd3Q3ckANl0dcx338qCTY4.png`, `yuFzZzaiq6SXFBvCqfED1Hgy4.png`), and grid rule `.hidden-1qs623s { display:none!important }`.
4. **Interactive Detail & Feature Matrix (<section.framer-LuCAZ> — `Technical Architecture & Narrative`)**:
   - Landmark `<section class="framer-LuCAZ">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Tre giorni, tantissimi ospiti, centinaia di persone che respirano"*) with `#ceff00` surface cards, `#0000ee` accents, and `.hidden-1tdjaai { display:none!important }`.
5. **Colophon & Global Directory Footer (<footer.framer-1qs623s> — `https://www.designbomb.it/`)**:
   - Landmark `<footer class="framer-1qs623s">` anchoring `Design Bomb Festival` footer links (`Programma · Workshop · cameretta · Shop · TICKET`), copy *"Awwwards Studio of the Year / Enea Rossi, CEO, Co-Founder e "*, and `#f7f6eb` structural dividers.
