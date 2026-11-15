# UI & UX Architecture: no-merci-michel-com

## Overview & Design Identity
- **Target**: `no-merci-michel-com` (**No Mercy Michel**)
- **Production URL**: [https://no.merci-michel.com](https://no.merci-michel.com)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#555` / `#f89953`)
- **Summary**: You thought we were nice people...Step into the arena and fight! Spoiler: you'll lose.
- **Total Clean CSS Variables Extracted**: `49` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Cetary`
- **Body Font Stack**: `UnitedSansRegular`
- **Monospace / Technical Font Stack**: `Roboto Mono`
- **Hero Display (`H1`)**: rule `h1` (`font-size: 7vw`, `line-height: 1`, `font-weight: 900`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `10px`, `100%`, `var(--base-text)`, `7vw`, `15vw`)
- **Body Copy**: rule `p` (`font-size: 1.2vw`, `font-weight: 400`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `10px`, `100%`, `var(--base-text)`, `7vw`, `15vw`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#555` | `html { color: #555 }` |
| **Primary Typography Ink** | `#3ea0f1` | `html { background: #3ea0f1 }` |
| **Elevated Surface / Card Substrate** | `#fff` | `::-moz-selection { color: #fff }` |
| **Interactive Accent / Highlight** | `#f89953` | `.old-browser .container h1 { color: #f89953 }` |
| **Secondary / Muted Copy** | `#ffffff` | `:after { border: white }` (`#ffffff`) |
| **Structural Hairline Border** | `#00f0f0` | `:before { color: #00f0f0 }` |

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
   - Landmark `<header class="desktop">` hosting `No Mercy Michel` navigation (`by`), DOM attributes (`data-website-id="e07f52fc-c45c-4322-87..."`, `data-umami-event="Click - Preloader Button"`, `data-v-app`, `data-v-75f61e58`), and stylesheet rule `html { -webkit-tap-highlight-color:rgba(255,255,255,0);-webkit-touch-callout:no... }`.
2. **Hero Stage & Focal Lead (<main.ui> — `No Mercy Michel`)**:
   - Landmark `<main class="ui">` presenting display lead `No Mercy Michel` and copy excerpt *"Free stickers — Free stickers —"* over `#555` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<main.ui> — `Featured Work & Interactive Showca`)**:
   - Landmark `<main class="ui">` rendering section `Featured Work & Interactive Showcase` with copy *"No Mercy Michel"*, asset references (`script.js`, `favicon.ico`, `favicon_dark.svg`, `favicon_light.svg`), and grid rule `body { display:block }`.
4. **Interactive Detail & Feature Matrix (<main.ui> — `Technical Architecture & Narrative`)**:
   - Landmark `<main class="ui">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Featured Work & Interactive Showcase"*) with `#fff` surface cards, `#f89953` accents, and `after { box-sizing:border-box;touch-action:manipulation }`.
5. **Colophon & Global Directory Footer (<footer.icons-spritesheet> — `https://no.merci-michel.com`)**:
   - Landmark `<footer class="icons-spritesheet">` anchoring `No Mercy Michel` footer links (`by`), copy *"Technical Architecture & Narrative"*, and `#00f0f0` structural dividers.
