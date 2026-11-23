---
title: "UI & UX Architecture: no-merci-michel-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: no-merci-michel-com

## Overview & Design Identity
- **Target**: `no-merci-michel-com` (**No Mercy Michel**)
- **Production URL**: [https://no.merci-michel.com](https://no.merci-michel.com)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#3ea0f1` / `#ffffff`)
- **Summary**: You thought we were nice people...Step into the arena and fight! Spoiler: you'll lose.
- **Total Clean CSS Variables Extracted**: `49` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `UnitedSansCondensed`
- **Body Font Stack**: `UnitedSansRegular`
- **Monospace / Technical Font Stack**: `Roboto Mono`
- **Hero Display (`H1`)**: rule `h1` (`font-size: 7vw`, `line-height: 1`, `font-weight: 900`)
- **Section Heading (`H2`)**: observed font-size ladder: `68px`, `22.4211px`, `10px`, `100%`, `var(--base-text)`
- **Body Copy**: live computed `body` (`font-size: 68px`, `line-height: normal`, `font-weight: 100`); rule `p` (`font-size: 1.2vw`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 22.4211px`, `line-height: normal`, `font-weight: 100`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#3ea0f1` | live computed `html` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `a` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#dfdfdf` | `#preloader .preloader-button .c... { background: #dfdfdf }` |
| **Interactive Accent / Highlight** | `#ffffff` | live computed `button` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#555555` | live computed `main` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#65b3f4` | `.marquee { stroke: #65b3f4 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--base-text` | `calc((22px) * var(--h-demult, 1))` | Typography Ink Token |
| `--padding` | `calc(var(--base-text))` | Layout / Spatial Grid Token |
| `--btn-size` | `calc((195px) * var(--h-demult, 1))` | Layout / Spatial Grid Token |
| `--btn-size-shared` | `calc((195px) * var(--h-demult, 1))` | Layout / Spatial Grid Token |
| `--btn-circle` | `calc((70px) * var(--h-demult, 1))` | Dimension / Scale Token |
| `--name-size` | `calc((48px) * var(--h-demult, 1))` | Layout / Spatial Grid Token |
| `--size` | `calc(var(--name-size) * .35)` | Layout / Spatial Grid Token |
| `--top` | `94px` | Dimension / Scale Token |
| `--lb-padding` | `2.5em` | Layout / Spatial Grid Token |
| `--height` | `calc(100vh - 42px)` | Layout / Spatial Grid Token |
| `--leaderboardSize` | `calc((18px) * var(--h-demult, 1))` | Layout / Spatial Grid Token |
| `--circle-size` | `1.6em` | Layout / Spatial Grid Token |
| `--half-circle-size` | `calc(var(--circle-size) / 2)` | Layout / Spatial Grid Token |
| `--input-size` | `clamp(280px, 40vw, 380px)` | Layout / Spatial Grid Token |
| `--input-shift-x` | `calc(var(--input-size) * -1 + var(--btn-circle))` | Design System Custom Token |
| `--input-shift-y` | `calc(var(--btn-circle) * -.35)` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.desktop> — `no-merci-michel-com`)**:
   - Landmark `<header class="desktop">` (`1440px`) hosting `No Mercy Michel` navigation (`by`), DOM attributes (`data-website-id="e07f52fc-c45c-4322-87..."`, `data-umami-event="Click - Preloader Button"`, `data-v-app`, `data-v-75f61e58`), and stylesheet rule `html { -webkit-tap-highlight-color:rgba(255,255,255,0);-webkit-touch-callout:no... }`.
2. **Hero Stage & Focal Lead (<main.ui> — `No Mercy Michel`)**:
   - Landmark `<main class="ui">` presenting display lead `No Mercy Michel` and copy excerpt *"FREE STICKERS — FREE STICKERS —"* over `#3ea0f1` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<main.ui:nth(2)> — `Featured Work & Interactive Showca`)**:
   - Landmark `<main class="ui">` rendering section `Featured Work & Interactive Showcase` with copy *"Free stickers — Free stickers —"*, asset references (`script.js`, `favicon.ico`, `favicon_dark.svg`, `favicon_light.svg`), and grid rule `body { display:block }`.
4. **Interactive Detail & Feature Matrix (<main.ui:nth(3)> — `Technical Architecture & Narrative`)**:
   - Landmark `<main class="ui">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Featured Work & Interactive Showcase"*) with `#dfdfdf` surface cards, `#ffffff` accents, and `after { box-sizing:border-box;touch-action:manipulation }`.
5. **Colophon & Global Directory Footer (<footer.icons-spritesheet> — `https://no.merci-michel.com`)**:
   - Landmark `<footer class="icons-spritesheet">` anchoring `No Mercy Michel` footer links (`by`), copy *"Technical Architecture & Narrative"*, and `#65b3f4` structural dividers.
