---
title: "UI Prompt Blueprint: stateofaidesign-com"
date: 2026-11-23
captured_at: 2026-11-23
target: "stateofaidesign-com"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#0000ee` accent)"
---

# UI Design System & Master Generation Blueprint: stateofaidesign-com

> **AI in Design Report 2026** (https://stateofaidesign.com/) — The second annual report by Designer Fund and Foundation Capital on how design teams are adapting to AI across tooling, craft, and org.

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **AI in Design Report 2026** (`https://stateofaidesign.com/`). The second annual report by Designer Fund and Foundation Capital on how design teams are adapting to AI across tooling, craft, and org.
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#0000ee` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#0000ee` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Beausite Classic Medium` for display copy (`AI in Design Report 2026`) with `Beausite Classic Medium Placeholder` and `Geist Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 0px 16px`, padding `145px`) with `cubic-bezier(.44,0,.56,1)` easing and Framer Motion Layout Physics.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, clamped at 2400px live multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `1440px` (full-bleed `100%` viewport stage).
- **Canvas Lateral Padding & Spacing**: `145px` lateral canvas padding with `0px 16px` grid gap.
- **Border Radius Scale**: `8px`, `15px`, `0px`, `100%`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 0px 16px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `145px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:768px) and (max-width:1199.98px)`, `@media (max-width:767.98px)`, `@media (min-width:2560px)`, `@media (max-width:2559px) and (min-width:1440px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
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

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
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

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Beausite Classic Medium`.
- **Primary Body Stack**: `Beausite Classic Medium Placeholder`.
- **Technical / Metadata Stack**: `Geist Mono`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 120px`, `line-height: 114px`, `font-weight: 500`, `letter-spacing: -7.2px`); rule `h1` (`font-size: 50px`, `line-height: 1em`, `letter-spacing: -.04em`, `font-weight: 500`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 80px`, `line-height: 76px`, `font-weight: 500`, `letter-spacing: -4.8px`).
- **Body Copy**: live computed `body` (`font-size: 12px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: 50px`, `line-height: 120%`, `letter-spacing: -.03em`, `font-weight: 500`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 12px`, `line-height: normal`, `font-weight: 400`); CSS variables `--letter-spacing: var(--framer-letter-spacing)`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.44,0,.56,1)`, `cubic-bezier(0.4,0,1,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `r-styles-preset-1irpjtw.rich-text...`**: `transition: color .2s cubic-bezier(.44,0,.56,1),text-decoration-color .2s...` extracted from `stateofaidesign-com` stylesheet.
- **Selector `er-styles-preset-minbjw.rich-text...`**: `transition: color .2s cubic-bezier(.44,0,.56,1),text-decoration-color .2s...` extracted from `stateofaidesign-com` stylesheet.
- **Selector `.framer-form-input-wrapper:after`**: `transition: var(--framer-input-focused-transition)` extracted from `stateofaidesign-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.44,0,.56,1)`)**: Governs interactive state transitions across `<nav.framer-g5d54>` and `<article.framer-HiGHW>`.
- **Runtime Interaction Engine**: Integrates Framer Motion Layout Physics with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — AI in Design Report 2026                   │
│ ====================================================================== │
│ [ <nav.framer-g5d54> (1425x56px)      | About About · Tools 01 · Cra ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <article.framer-1ti4ff8> (w=1440px)                    | │
│ | H1: AI in Design Report 2026                                       | │
│ | Substrate: #ffffff | Ink: #000000 | Accent: #0000ee                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<article.framer-HiGHW>) max-w: 1440px               | │
│ | +------------------------------+  +------------------------------+ | │
│ | | In 2025, designers were expe |  | The great toolstack shakeup  | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<article.framer-72rtr7>) — Craft in the age of i    | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.framer-3azmv) | https://stateofaidesign.com/         │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 0px 16px)   │
│ ====================================================================== │
│ [ HEADER BAR (<nav.framer-g5d54>      ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<article.framer-1ti4ff8>) — 390px Vertical Lead        | │
│ | H1: AI in Design Report 2026                                       | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<article.framer-HiGHW>) — 1-Col Stack              | │
│ | [ Item 1: In 2025, designers were experimenting with AI. In...   ] | │
│ | [ Item 2: The great toolstack shakeup                            ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<article.framer-72rtr7>) — 1-Col (Craft in the age o)  │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.framer-3azmv) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.framer-g5d54> — `stateofaidesign-com`)**:
   - Landmark `<nav class="framer-g5d54 framer-60e8rl">` (`1425x56px`) hosting `AI in Design Report 2026` navigation (`About About · Tools 01 · Craft 02 · Teams 03 · Sierra 01`), DOM attributes (`data-framer-font-css`, `data-framer-css-ssr-minified`, `data-framer-components="framer-lib-cursors-ho..."`, `data-fid="7cd17bb067b245589aa6a..."`), and stylesheet rule `main { box-sizing:border-box;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<article.framer-1ti4ff8> — `AI in Design Report 2026`)**:
   - Landmark `<article class="framer-1ti4ff8">` presenting display lead `AI in Design Report 2026` and copy excerpt *"©2026 Designer Fund, Foundation Capital. All rights reserved"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<article.framer-HiGHW> — `In 2025, designers were experiment`)**:
   - Landmark `<article class="framer-HiGHW">` rendering section `In 2025, designers were experimenting with AI. In...` with copy *"How designers are evolving their tools, craft, and teams with AI"*, asset references (`YeBg4KhukpeFDQRc7qUySaNCzM4.png`, `LYZGuKjYSwOjtebGnDa0R1K1zg.png`, `fonts.gstatic.com`, `adora-start.js`), and grid rule `root { -webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale }`.
4. **Interactive Detail & Feature Matrix (<article.framer-72rtr7> — `The great toolstack shakeup`)**:
   - Landmark `<article class="framer-72rtr7">` framing `The great toolstack shakeup` and `Craft in the age of infinite output` (*"By Designer Fund in partnership with Foundation Capital"*) with `#cdabfe` surface cards, `#0000ee` accents, and `button { font-family:sans-serif;font-size:12px }`.
5. **Colophon & Global Directory Footer (<footer.framer-3azmvu> — `https://stateofaidesign.com/`)**:
   - Landmark `<footer class="framer-3azmvu">` anchoring `AI in Design Report 2026` footer links (`About About · Tools 01 · Craft 02 · Teams 03 · Sierra 01`), copy *"An Inflection Point"*, and `#000000` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: stateofaidesign-com (AI in Design Report 2026)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `stateofaidesign-com` (**AI in Design Report 2026** — `https://stateofaidesign.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#000000` ink, `#0000ee` accent).
- **Identity & Domain Context**: The second annual report by Designer Fund and Foundation Capital on how design teams are adapting to AI across tooling, craft, and org.
- **Primary Substrate**: `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#000000`, **Accent / Highlight**: `#0000ee`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#0000ee` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Beausite Classic Medium` for display copy (`AI in Design Report 2026`) with `Beausite Classic Medium Placeholder` and `Geist Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 0px 16px`, padding `145px`) with `cubic-bezier(.44,0,.56,1)` easing and Framer Motion Layout Physics.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `stateofaidesign-com` in your global stylesheet:

:root {
  /* AI in Design Report 2026 (stateofaidesign-com) — Live-Grounded CSS Variables */
  --token-3412d4dd-2f5f-48c8-b607-f8105a8b7211: #fe7141; /* Color / Atmospheric Token (stateofaidesign-com) */
  --token-a228bc56-904d-4a09-b7f8-6b60e0221982: #000; /* Color / Atmospheric Token (stateofaidesign-com) */
  --token-0d9c52bb-4346-4afb-b8ae-283673444b3f: #fff; /* Color / Atmospheric Token (stateofaidesign-com) */
  --token-54653423-a788-4b87-99d2-f130e2af5148: #cdabfe; /* Color / Atmospheric Token (stateofaidesign-com) */
  --token-6af35a76-1812-4e65-b20e-93b47dd846c7: #597e87; /* Color / Atmospheric Token (stateofaidesign-com) */
  --token-dc58878c-6871-4081-9b9a-81f0df31eb6a: #d1ddd3; /* Color / Atmospheric Token (stateofaidesign-com) */
  --token-9c987371-9131-4ecc-9a69-10e703280af3: #f5f9fc; /* Color / Atmospheric Token (stateofaidesign-com) */
  --token-ce625ef5-5dd0-428c-a706-db60cbd06c7f: #153250; /* Color / Atmospheric Token (stateofaidesign-com) */
  --token-d66b7197-4553-4ba6-b16f-d06cd8b6ab87: #d1ddd3; /* Color / Atmospheric Token (stateofaidesign-com) */
  --text-decoration-skip-ink: var(--framer-text-decoration-skip-ink); /* Typography Ink Token (stateofaidesign-com) */
  --text-underline-offset: var(--framer-text-decoration-offset); /* Typography Ink Token (stateofaidesign-com) */
  --font-family: var(--framer-font-family); /* Typography / Scale Token (stateofaidesign-com) */
  --font-style: var(--framer-font-style); /* Typography / Scale Token (stateofaidesign-com) */
  --font-weight: var(--framer-font-weight); /* Typography / Scale Token (stateofaidesign-com) */
  --text-color: var(--framer-text-color); /* Typography Ink Token (stateofaidesign-com) */
  --letter-spacing: var(--framer-letter-spacing); /* Typography / Scale Token (stateofaidesign-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ffffff` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#000000` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#cdabfe` — grounded in live computed `a` `background-color` (`computed_styles.json`)
- **Interactive Accent / Highlight**: `#0000ee` — grounded in live computed `a` `color` (`computed_styles.json`)
- **Secondary / Muted Copy**: `#0000ee` — grounded in live computed `a` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#000000` — grounded in `var(--border-color)` in `:root`
- **Variable Token (`--token-3412d4dd-2f5f-48c8-b607-f8105a8b7211`)**: `#fe7141` — grounded in `var(--token-3412d4dd-2f5f-48c8-b607-f8105a8b7211)` in `:root`
- **Variable Token (`--token-6af35a76-1812-4e65-b20e-93b47dd846c7`)**: `#597e87` — grounded in `var(--token-6af35a76-1812-4e65-b20e-93b47dd846c7)` in `:root`
- **Variable Token (`--token-dc58878c-6871-4081-9b9a-81f0df31eb6a`)**: `#d1ddd3` — grounded in `var(--token-dc58878c-6871-4081-9b9a-81f0df31eb6a)` in `:root`
- **Variable Token (`--token-9c987371-9131-4ecc-9a69-10e703280af3`)**: `#f5f9fc` — grounded in `var(--token-9c987371-9131-4ecc-9a69-10e703280af3)` in `:root`
- **Variable Token (`--token-ce625ef5-5dd0-428c-a706-db60cbd06c7f`)**: `#153250` — grounded in `var(--token-ce625ef5-5dd0-428c-a706-db60cbd06c7f)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (clamped at 2400px live multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1440px` (full-bleed `100%` viewport stage)
- **Padding & Gutters**: `145px` lateral canvas padding with `0px 16px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 0px 16px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `145px` horizontal padding
- **Media Queries**: `@media (min-width:768px) and (max-width:1199.98px)`, `@media (max-width:767.98px)`, `@media (min-width:2560px)`, `@media (max-width:2559px) and (min-width:1440px)`
- **Corner Radii**: `8px`, `15px`, `0px`, `100%`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Beausite Classic Medium`
- **Body Font Stack**: `Beausite Classic Medium Placeholder`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **H1 Display Rule**: live computed `h1` (`font-size: 120px`, `line-height: 114px`, `font-weight: 500`, `letter-spacing: -7.2px`); rule `h1` (`font-size: 50px`, `line-height: 1em`, `letter-spacing: -.04em`, `font-weight: 500`)
- **H2 Section Rule**: live computed `h2` (`font-size: 80px`, `line-height: 76px`, `font-weight: 500`, `letter-spacing: -4.8px`)
- **Body Copy Rule**: live computed `body` (`font-size: 12px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: 50px`, `line-height: 120%`, `letter-spacing: -.03em`, `font-weight: 500`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 12px`, `line-height: normal`, `font-weight: 400`); CSS variables `--letter-spacing: var(--framer-letter-spacing)`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `stateofaidesign-com` (`AI in Design Report 2026`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.framer-g5d54> — `stateofaidesign-com`)**:
   - DOM & Selectors: Landmark `<nav class="framer-g5d54 framer-60e8rl">` (`1425x56px`) hosting `AI in Design Report 2026` navigation (`About About · Tools 01 · Craft 02 · Teams 03 · Sierra 01`), DOM attributes (`data-framer-font-css`, `data-framer-css-ssr-minified`, `data-framer-components="framer-lib-cursors-ho..."`, `data-fid="7cd17bb067b245589aa6a..."`), and stylesheet rule `main { box-sizing:border-box;margin:0;padding:0 }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.framer-g5d54> — `stateofaidesign-com`)` (`stateofaidesign-com`) adapts across `@media (min-width:768px) and (max-width:1199.98px)`, `@media (max-width:767.98px)`, `@media (min-width:2560px)`, `@media (max-width:2559px) and (min-width:1440px)` with `cubic-bezier(.44,0,.56,1)`, `cubic-bezier(0.4,0,1,1)` transitions and links `About About · Tools 01 · Craft 02 · Teams 03 · Sierra 01`.
2. **Hero Stage & Focal Lead (<article.framer-1ti4ff8> — `AI in Design Report 2026`)**:
   - DOM & Selectors: Landmark `<article class="framer-1ti4ff8">` presenting display lead `AI in Design Report 2026` and copy excerpt *"©2026 Designer Fund, Foundation Capital. All rights reserved"* over `#ffffff` canvas and `#000000` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#ffffff` background with `#000000` headline `AI in Design Report 2026`.
3. **Primary Showcase & Content Grid (<article.framer-HiGHW> — `In 2025, designers were experiment`)**:
   - DOM & Selectors: Landmark `<article class="framer-HiGHW">` rendering section `In 2025, designers were experimenting with AI. In...` with copy *"How designers are evolving their tools, craft, and teams with AI"*, asset references (`YeBg4KhukpeFDQRc7qUySaNCzM4.png`, `LYZGuKjYSwOjtebGnDa0R1K1zg.png`, `fonts.gstatic.com`, `adora-start.js`), and grid rule `root { -webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<article.framer-HiGHW> — `In 2025, designers were experiment`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 0px 16px`) on desktop and Single-column vertical stack at `390px` viewport width with `145px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<article.framer-72rtr7> — `The great toolstack shakeup`)**:
   - DOM & Selectors: Landmark `<article class="framer-72rtr7">` framing `The great toolstack shakeup` and `Craft in the age of infinite output` (*"By Designer Fund in partnership with Foundation Capital"*) with `#cdabfe` surface cards, `#0000ee` accents, and `button { font-family:sans-serif;font-size:12px }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<article.framer-72rtr7> — `The great toolstack shakeup`)` uses `8px`, `15px`, `0px`, `100%` radii, `#0000ee` highlights, and assets (YeBg4KhukpeFDQRc7qUySaNCzM4.png, LYZGuKjYSwOjtebGnDa0R1K1zg.png, fonts.gstatic.com).
5. **Colophon & Global Directory Footer (<footer.framer-3azmvu> — `https://stateofaidesign.com/`)**:
   - DOM & Selectors: Landmark `<footer class="framer-3azmvu">` anchoring `AI in Design Report 2026` footer links (`About About · Tools 01 · Craft 02 · Teams 03 · Sierra 01`), copy *"An Inflection Point"*, and `#000000` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.framer-3azmvu> — `https://stateofaidesign.com/`)` aligns to `1440px` (full-bleed `100%` viewport stage) with `145px` lateral canvas padding with `0px 16px` grid gap and attributes (data-framer-font-css, data-framer-css-ssr-minified, data-framer-components="framer-lib-cursors-ho...").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"©2026 Designer Fund, Foundation Capital. All rights reserved"*
- Copy Excerpt 2: *"How designers are evolving their tools, craft, and teams with AI"*
- Copy Excerpt 3: *"By Designer Fund in partnership with Foundation Capital"*
- Copy Excerpt 4: *"An Inflection Point"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.44,0,.56,1)`, `cubic-bezier(0.4,0,1,1)`
- **Extracted Stylesheet Rules (`stateofaidesign-com`)**:
- `main { box-sizing:border-box;margin:0;padding:0 }`
- `root { -webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale }`
- `button { font-family:sans-serif;font-size:12px }`
- `body { --framer-will-change-override:transform }`
- `.framer-text.framer-image { display:var(--text-truncation-display-inline-for-safari-16,revert) }`
- **Per-Selector Transition Rules**:
- **Selector `r-styles-preset-1irpjtw.rich-text...`**: `transition: color .2s cubic-bezier(.44,0,.56,1),text-decoration-color .2s...` extracted from `stateofaidesign-com` stylesheet.
- **Selector `er-styles-preset-minbjw.rich-text...`**: `transition: color .2s cubic-bezier(.44,0,.56,1),text-decoration-color .2s...` extracted from `stateofaidesign-com` stylesheet.
- **Selector `.framer-form-input-wrapper:after`**: `transition: var(--framer-input-focused-transition)` extracted from `stateofaidesign-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.44,0,.56,1)`)**: Governs interactive state transitions across `<nav.framer-g5d54>` and `<article.framer-HiGHW>`.
- **Runtime Interaction Engine**: Integrates Framer Motion Layout Physics with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `stateofaidesign-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
