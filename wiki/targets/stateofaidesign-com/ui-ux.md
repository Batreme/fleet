---
title: "UI & UX Architecture: stateofaidesign-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: stateofaidesign-com

## Overview & Design Identity
- **Target**: `stateofaidesign-com` (**AI in Design Report 2026**)
- **Production URL**: [https://stateofaidesign.com/](https://stateofaidesign.com/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#0000ee` accent)
- **Summary**: The second annual report by Designer Fund and Foundation Capital on how design teams are adapting to AI across tooling, craft, and org.
- **Total Clean CSS Variables Extracted**: `42` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Beausite Classic Medium`
- **Body Font Stack**: `Beausite Classic Medium Placeholder`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 120px`, `line-height: 114px`, `font-weight: 500`, `letter-spacing: -7.2px`); rule `h1` (`font-size: 50px`, `line-height: 1em`, `letter-spacing: -.04em`, `font-weight: 500`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 80px`, `line-height: 76px`, `font-weight: 500`, `letter-spacing: -4.8px`)
- **Body Copy**: live computed `body` (`font-size: 12px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: 50px`, `line-height: 120%`, `letter-spacing: -.03em`, `font-weight: 500`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 12px`, `line-height: normal`, `font-weight: 400`); CSS variables `--letter-spacing: var(--framer-letter-spacing)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#cdabfe` | live computed `a` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#0000ee` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#0000ee` | live computed `a` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#000000` | `var(--border-color)` in `:root` |
| **Variable Token (`--token-3412d4dd-2f5f-48c8-b607-f8105a8b7211`)** | `#fe7141` | `var(--token-3412d4dd-2f5f-48c8-b607-f8105a8b7211)` in `:root` |
| **Variable Token (`--token-6af35a76-1812-4e65-b20e-93b47dd846c7`)** | `#597e87` | `var(--token-6af35a76-1812-4e65-b20e-93b47dd846c7)` in `:root` |
| **Variable Token (`--token-dc58878c-6871-4081-9b9a-81f0df31eb6a`)** | `#d1ddd3` | `var(--token-dc58878c-6871-4081-9b9a-81f0df31eb6a)` in `:root` |
| **Variable Token (`--token-9c987371-9131-4ecc-9a69-10e703280af3`)** | `#f5f9fc` | `var(--token-9c987371-9131-4ecc-9a69-10e703280af3)` in `:root` |
| **Variable Token (`--token-ce625ef5-5dd0-428c-a706-db60cbd06c7f`)** | `#153250` | `var(--token-ce625ef5-5dd0-428c-a706-db60cbd06c7f)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--token-3412d4dd-2f5f-48c8-b607-f8105a8b7211` | `#fe7141` | Color / Atmospheric Token |
| `--token-a228bc56-904d-4a09-b7f8-6b60e0221982` | `#000` | Color / Atmospheric Token |
| `--token-0d9c52bb-4346-4afb-b8ae-283673444b3f` | `#fff` | Color / Atmospheric Token |
| `--token-54653423-a788-4b87-99d2-f130e2af5148` | `#cdabfe` | Color / Atmospheric Token |
| `--token-6af35a76-1812-4e65-b20e-93b47dd846c7` | `#597e87` | Color / Atmospheric Token |
| `--token-dc58878c-6871-4081-9b9a-81f0df31eb6a` | `#d1ddd3` | Color / Atmospheric Token |
| `--token-9c987371-9131-4ecc-9a69-10e703280af3` | `#f5f9fc` | Color / Atmospheric Token |
| `--token-ce625ef5-5dd0-428c-a706-db60cbd06c7f` | `#153250` | Color / Atmospheric Token |
| `--token-d66b7197-4553-4ba6-b16f-d06cd8b6ab87` | `#d1ddd3` | Color / Atmospheric Token |
| `--text-decoration-skip-ink` | `var(--framer-text-decoration-skip-ink)` | Typography Ink Token |
| `--text-underline-offset` | `var(--framer-text-decoration-offset)` | Typography Ink Token |
| `--font-family` | `var(--framer-font-family)` | Typography / Scale Token |
| `--font-style` | `var(--framer-font-style)` | Typography / Scale Token |
| `--font-weight` | `var(--framer-font-weight)` | Typography / Scale Token |
| `--text-color` | `var(--framer-text-color)` | Typography Ink Token |
| `--letter-spacing` | `var(--framer-letter-spacing)` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.framer-g5d54> — `stateofaidesign-com`)**:
   - Landmark `<nav class="framer-g5d54 framer-60e8rl">` (`1425x56px`) hosting `AI in Design Report 2026` navigation (`About About · Tools 01 · Craft 02 · Teams 03 · Sierra 01`), DOM attributes (`data-framer-font-css`, `data-framer-breakpoint-css`, `data-framer-css-ssr-minified`, `data-framer-components="framer-lib-cursors-ho..."`), and stylesheet rule `.hidden-miin9m { display:none!important }`.
2. **Hero Stage & Focal Lead (<article.framer-1ti4ff8> — `AI in Design Report 2026`)**:
   - Landmark `<article class="framer-1ti4ff8">` presenting display lead `AI in Design Report 2026` and copy excerpt *"©2026 Designer Fund, Foundation Capital. All rights reserved"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<article.framer-HiGHW> — `In 2025, designers were experiment`)**:
   - Landmark `<article class="framer-HiGHW">` rendering section `In 2025, designers were experimenting with AI. In...` with copy *"How designers are evolving their tools, craft, and teams with AI"*, asset references (`YeBg4KhukpeFDQRc7qUySaNCzM4.png`, `LYZGuKjYSwOjtebGnDa0R1K1zg.png`, `fonts.gstatic.com`, `adora-start.js`), and grid rule `.hidden-72rtr7 { display:none!important }`.
4. **Interactive Detail & Feature Matrix (<article.framer-72rtr7> — `The great toolstack shakeup`)**:
   - Landmark `<article class="framer-72rtr7">` framing `The great toolstack shakeup` and `Craft in the age of infinite output` (*"By Designer Fund in partnership with Foundation Capital"*) with `#cdabfe` surface cards, `#0000ee` accents, and `.hidden-t69d6d { display:none!important }`.
5. **Colophon & Global Directory Footer (<footer.framer-3azmvu> — `https://stateofaidesign.com/`)**:
   - Landmark `<footer class="framer-3azmvu">` anchoring `AI in Design Report 2026` footer links (`About About · Tools 01 · Craft 02 · Teams 03 · Sierra 01`), copy *"An Inflection Point"*, and `#000000` structural dividers.
