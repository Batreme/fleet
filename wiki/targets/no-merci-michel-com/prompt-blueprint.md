---
title: "UI Prompt Blueprint: no-merci-michel-com"
date: 2026-11-15
target: "[[overview|no-merci-michel-com]]"
status: analyzed
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#555` / `#f89953`)"
---

# UI Design System & Master Generation Blueprint: no-merci-michel-com

> **No Mercy Michel** (https://no.merci-michel.com) — You thought we were nice people...Step into the arena and fight! Spoiler: you'll lose.

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/no-merci-michel-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **No Mercy Michel** (`https://no.merci-michel.com`). You thought we were nice people...Step into the arena and fight! Spoiler: you'll lose.
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#555` / `#f89953`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#555` (`html { color: #555 }`) paired with `#fff` primary typography and `#f89953` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Cetary` for display copy (`No Mercy Michel`) with `UnitedSansRegular` and `Roboto Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `768px` container bounds (`gap: 0px (flush layout)`, padding `6px`) with `cubic-bezier(.55,0,.1,1)` easing and Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/no-merci-michel-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `768px` extracted from `no-merci-michel-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `6px` lateral canvas padding with `0px (flush layout)` grid gap.
- **Border Radius Scale**: `45px`, `48px`, `50%`, `44px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 768px`, `gap: 0px (flush layout)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `6px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width: 375px) and (max-width: 768px)`, `@media (min-width: 768px) and (max-width: 1440px)`, `@media (min-width: 1440px) and (max-width: 1900px)`, `@media (min-width: 1901px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#555` | `html { color: #555 }` |
| **Primary Typography Ink** | `#3ea0f1` | `html { background: #3ea0f1 }` |
| **Elevated Surface / Card Substrate** | `#fff` | `::-moz-selection { color: #fff }` |
| **Interactive Accent / Highlight** | `#f89953` | `.old-browser .container h1 { color: #f89953 }` |
| **Secondary / Muted Copy** | `#ffffff` | `:after { border: white }` (`#ffffff`) |
| **Structural Hairline Border** | `#00f0f0` | `:before { color: #00f0f0 }` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
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

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Cetary`.
- **Primary Body Stack**: `UnitedSansRegular`.
- **Technical / Metadata Stack**: `Roboto Mono`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 7vw`, `line-height: 1`, `font-weight: 900`).
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `10px`, `100%`, `var(--base-text)`, `7vw`, `15vw`).
- **Body Copy**: rule `p` (`font-size: 1.2vw`, `font-weight: 400`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `10px`, `100%`, `var(--base-text)`, `7vw`, `15vw`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.55,0,.1,1)`, `cubic-bezier(.215,.61,.355,1)`, `cubic-bezier(.645,.045,.355,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.icon-star[data-v-402cbbe5]`**: `transition: transform .25s cubic-bezier(.55,0,.1,1)` extracted from `no-merci-michel-com` stylesheet.
- **Selector `erboard-close-button[data-v-b298e...`**: `transition: transform .2s cubic-bezier(.55,0,.1,1)` extracted from `no-merci-michel-com` stylesheet.
- **Selector `rboard-close-button[data-v-b298ed...`**: `transition: transform .2s cubic-bezier(.55,0,.1,1)` extracted from `no-merci-michel-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.55,0,.1,1)`)**: Governs interactive state transitions across `<header.desktop>` and `<main.ui>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — No Mercy Michel                            │
│ ====================================================================== │
│ [ <header.desktop>         | by                                     ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <main.ui>                                            |   │
│ | H1: No Mercy Michel                                              |   │
│ | Substrate: #555       | Ink: #fff       | Accent: #f89953        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<main.ui>                 ) max-w: 768px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Featured Work & Interactive  |  | Technical Architecture & Nar | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 0px (f) | │
│ | [<header.desktop>] -> [<main.ui>] -> [<main.ui>] |                   │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.icons-spritesh) | https://no.merci-michel.com        │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
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

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: no-merci-michel-com (No Mercy Michel)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `no-merci-michel-com` (**No Mercy Michel** — `https://no.merci-michel.com`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#555` / `#f89953`).
- **Identity & Domain Context**: You thought we were nice people...Step into the arena and fight! Spoiler: you'll lose.
- **Primary Substrate**: `#555` (`html { color: #555 }`), **Primary Ink**: `#fff`, **Accent / Highlight**: `#f89953`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#555` (`html { color: #555 }`) paired with `#fff` primary typography and `#f89953` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Cetary` for display copy (`No Mercy Michel`) with `UnitedSansRegular` and `Roboto Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `768px` container bounds (`gap: 0px (flush layout)`, padding `6px`) with `cubic-bezier(.55,0,.1,1)` easing and Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `no-merci-michel-com` in your global stylesheet:

:root {
  /* No Mercy Michel (no-merci-michel-com) — Ground-Truth Extracted CSS Variables */
  --base-text: calc((22px) * var(--h-demult, 1)); /* Typography Ink Token (no-merci-michel-com) */
  --padding: calc(var(--base-text)); /* Layout / Spatial Grid Token (no-merci-michel-com) */
  --btn-size: calc((195px) * var(--h-demult, 1)); /* Layout / Spatial Grid Token (no-merci-michel-com) */
  --btn-size-shared: calc((195px) * var(--h-demult, 1)); /* Layout / Spatial Grid Token (no-merci-michel-com) */
  --btn-circle: calc((70px) * var(--h-demult, 1)); /* Dimension / Scale Token (no-merci-michel-com) */
  --name-size: calc((48px) * var(--h-demult, 1)); /* Layout / Spatial Grid Token (no-merci-michel-com) */
  --size: calc(var(--name-size) * .35); /* Layout / Spatial Grid Token (no-merci-michel-com) */
  --top: 94px; /* Dimension / Scale Token (no-merci-michel-com) */
  --lb-padding: 2.5em; /* Layout / Spatial Grid Token (no-merci-michel-com) */
  --height: calc(100vh - 42px); /* Layout / Spatial Grid Token (no-merci-michel-com) */
  --leaderboardSize: calc((18px) * var(--h-demult, 1)); /* Layout / Spatial Grid Token (no-merci-michel-com) */
  --circle-size: 1.6em; /* Layout / Spatial Grid Token (no-merci-michel-com) */
  --half-circle-size: calc(var(--circle-size) / 2); /* Layout / Spatial Grid Token (no-merci-michel-com) */
  --input-size: clamp(280px, 40vw, 380px); /* Layout / Spatial Grid Token (no-merci-michel-com) */
  --input-shift-x: calc(var(--input-size) * -1 + var(--btn-circle)); /* Design System Custom Token (no-merci-michel-com) */
  --input-shift-y: calc(var(--btn-circle) * -.35); /* Design System Custom Token (no-merci-michel-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#555` — grounded in `html { color: #555 }`
- **Primary Typography Ink**: `#3ea0f1` — grounded in `html { background: #3ea0f1 }`
- **Elevated Surface / Card Substrate**: `#fff` — grounded in `::-moz-selection { color: #fff }`
- **Interactive Accent / Highlight**: `#f89953` — grounded in `.old-browser .container h1 { color: #f89953 }`
- **Secondary / Muted Copy**: `#ffffff` — grounded in `:after { border: white }` (`#ffffff`)
- **Structural Hairline Border**: `#00f0f0` — grounded in `:before { color: #00f0f0 }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `768px` extracted from `no-merci-michel-com` stylesheet
- **Padding & Gutters**: `6px` lateral canvas padding with `0px (flush layout)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 768px`, `gap: 0px (flush layout)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `6px` horizontal padding
- **Media Queries**: `@media (min-width: 375px) and (max-width: 768px)`, `@media (min-width: 768px) and (max-width: 1440px)`, `@media (min-width: 1440px) and (max-width: 1900px)`, `@media (min-width: 1901px)`
- **Corner Radii**: `45px`, `48px`, `50%`, `44px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Cetary`
- **Body Font Stack**: `UnitedSansRegular`
- **Monospace / Technical Font Stack**: `Roboto Mono`
- **H1 Display Rule**: rule `h1` (`font-size: 7vw`, `line-height: 1`, `font-weight: 900`)
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `10px`, `100%`, `var(--base-text)`, `7vw`, `15vw`)
- **Body Copy Rule**: rule `p` (`font-size: 1.2vw`, `font-weight: 400`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `10px`, `100%`, `var(--base-text)`, `7vw`, `15vw`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `no-merci-michel-com` (`No Mercy Michel`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.desktop> — `no-merci-michel-com`)**:
   - DOM & Selectors: Landmark `<header class="desktop">` hosting `No Mercy Michel` navigation (`by`), DOM attributes (`data-website-id="e07f52fc-c45c-4322-87..."`, `data-umami-event="Click - Preloader Button"`, `data-v-app`, `data-v-75f61e58`), and stylesheet rule `html { -webkit-tap-highlight-color:rgba(255,255,255,0);-webkit-touch-callout:no... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.desktop> — `no-merci-michel-com`)` (`no-merci-michel-com`) adapts across `@media (min-width: 375px) and (max-width: 768px)`, `@media (min-width: 768px) and (max-width: 1440px)`, `@media (min-width: 1440px) and (max-width: 1900px)`, `@media (min-width: 1901px)` with `cubic-bezier(.55,0,.1,1)`, `cubic-bezier(.215,.61,.355,1)`, `cubic-bezier(.645,.045,.355,1)` transitions and links `by`.
2. **Hero Stage & Focal Lead (<main.ui> — `No Mercy Michel`)**:
   - DOM & Selectors: Landmark `<main class="ui">` presenting display lead `No Mercy Michel` and copy excerpt *"Free stickers — Free stickers —"* over `#555` canvas and `#fff` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#555` background with `#fff` headline `No Mercy Michel`.
3. **Primary Showcase & Content Grid (<main.ui> — `Featured Work & Interactive Showca`)**:
   - DOM & Selectors: Landmark `<main class="ui">` rendering section `Featured Work & Interactive Showcase` with copy *"No Mercy Michel"*, asset references (`script.js`, `favicon.ico`, `favicon_dark.svg`, `favicon_light.svg`), and grid rule `body { display:block }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<main.ui> — `Featured Work & Interactive Showca`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 768px`, `gap: 0px (flush layout)`) on desktop and Single-column vertical stack at `390px` viewport width with `6px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<main.ui> — `Technical Architecture & Narrative`)**:
   - DOM & Selectors: Landmark `<main class="ui">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Featured Work & Interactive Showcase"*) with `#fff` surface cards, `#f89953` accents, and `after { box-sizing:border-box;touch-action:manipulation }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<main.ui> — `Technical Architecture & Narrative`)` uses `45px`, `48px`, `50%`, `44px` radii, `#f89953` highlights, and assets (script.js, favicon.ico, favicon_dark.svg).
5. **Colophon & Global Directory Footer (<footer.icons-spritesheet> — `https://no.merci-michel.com`)**:
   - DOM & Selectors: Landmark `<footer class="icons-spritesheet">` anchoring `No Mercy Michel` footer links (`by`), copy *"Technical Architecture & Narrative"*, and `#00f0f0` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.icons-spritesheet> — `https://no.merci-michel.com`)` aligns to `768px` extracted from `no-merci-michel-com` stylesheet with `6px` lateral canvas padding with `0px (flush layout)` grid gap and attributes (data-website-id="e07f52fc-c45c-4322-87...", data-umami-event="Click - Preloader Button", data-v-app).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Free stickers — Free stickers —"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.55,0,.1,1)`, `cubic-bezier(.215,.61,.355,1)`, `cubic-bezier(.645,.045,.355,1)`
- **Extracted Stylesheet Rules (`no-merci-michel-com`)**:
- `html { -webkit-tap-highlight-color:rgba(255,255,255,0);-webkit-touch-callout:no... }`
- `body { display:block }`
- `after { box-sizing:border-box;touch-action:manipulation }`
- `section { display:block }`
- `svg { max-width:100%;display:block }`
- **Per-Selector Transition Rules**:
- **Selector `.icon-star[data-v-402cbbe5]`**: `transition: transform .25s cubic-bezier(.55,0,.1,1)` extracted from `no-merci-michel-com` stylesheet.
- **Selector `erboard-close-button[data-v-b298e...`**: `transition: transform .2s cubic-bezier(.55,0,.1,1)` extracted from `no-merci-michel-com` stylesheet.
- **Selector `rboard-close-button[data-v-b298ed...`**: `transition: transform .2s cubic-bezier(.55,0,.1,1)` extracted from `no-merci-michel-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.55,0,.1,1)`)**: Governs interactive state transitions across `<header.desktop>` and `<main.ui>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `no-merci-michel-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
