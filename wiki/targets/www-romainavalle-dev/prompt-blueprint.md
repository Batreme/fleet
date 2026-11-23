---
title: "UI Prompt Blueprint: www-romainavalle-dev"
date: 2026-11-23
captured_at: 2026-11-23
target: "www-romainavalle-dev"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier2_webgl
http_status: 200
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#f3f2f1`)"
---

# UI Design System & Master Generation Blueprint: www-romainavalle-dev

> **Romain Avalle - Interactive developper** (https://www.romainavalle.dev/) — Romain Avalle, interactive developer since 2006. Team Lead & Tech Lead at REF Digital in Montréal. Awwwards jury member, 40+ Awwwards and...

![Desktop Viewport Capture (1440x900)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Romain Avalle - Interactive developper** (`https://www.romainavalle.dev/`). Romain Avalle, interactive developer since 2006. Team Lead & Tech Lead at REF Digital in Montréal. Awwwards jury member, 40+ Awwwards and...
- **Final Redirected URL**: [https://romainavalle.dev/](https://romainavalle.dev/)
- **Capture Provenance**: Live browser capture (`tier2_webgl`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#f3f2f1`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `browser-default` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#f3f2f1` accents.
  - **Grounded Typographic Hierarchy**: Pairs `RemusVariableVF` for display copy (`Romain Avalle`) with `RemusVariableVF` and `andale-mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 8.22857px`, padding `8.22857px`) with `cubic-bezier(.23,1,.32,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×900px` (`assets/desktop.png`, single-viewport 100vh live capture (900px)), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport).
- **Canvas Lateral Padding & Spacing**: `8.22857px` lateral canvas padding with `8.22857px` grid gap.
- **Border Radius Scale**: `3.08571px`, `.3rem`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 8.22857px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `8.22857px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (width>=650px)`, `@media (width>=1024px)`, `@media (width>=800px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `browser-default` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#000000` | live computed `header` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#f3f2f1` | `<meta name="theme-color" content="#f3f2f1">` in `dom.html` |
| **Secondary / Muted Copy** | `#000000` | secondary opacity step of live computed `h1` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#000000` | hairline divider derived from secondary opacity step of live computed `h1` `color` (`computed_styles.json`) |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--size` | `375` | Layout / Spatial Grid Token |
| `--lvh` | `1lvh` | Layout / Spatial Grid Token |
| `--dvh` | `1dvh` | Layout / Spatial Grid Token |
| `--svh` | `1svh` | Layout / Spatial Grid Token |
| `--spacing` | `.1rem` | Layout / Spatial Grid Token |
| `--default-transition-duration` | `.15s` | Motion / Easing Token |
| `--default-transition-timing-function` | `cubic-bezier(.23, 1, .32, 1)` | Motion / Easing Token |
| `--default-font-family` | `var(--font-sans)` | Typography / Scale Token |
| `--default-mono-font-family` | `var(--font-mono)` | Typography / Scale Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--tw-translate-x` | `0` | Design System Custom Token |
| `--tw-translate-y` | `0` | Design System Custom Token |
| `--tw-translate-z` | `0` | Design System Custom Token |
| `--www-romainavalle-bg` | `#ffffff` | Canvas Substrate (from live computed `browser-default` `background-color` (`computed_styles.json`)) |
| `--www-romainavalle-ink` | `#000000` | Primary Typography Ink (computed-derived) |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `RemusVariableVF`.
- **Primary Body Stack**: `RemusVariableVF`.
- **Technical / Metadata Stack**: `andale-mono`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 16.4571px`, `line-height: 19.7486px`, `font-weight: 600`, `letter-spacing: -0.308571px`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 16.4571px`, `line-height: 19.7486px`, `font-weight: 600`, `letter-spacing: -0.308571px`).
- **Body Copy**: live computed `body` (`font-size: 16.4571px`, `line-height: 19.7486px`, `font-weight: 600`, `letter-spacing: -0.308571px`); rule `,body` (`font-size: 1.6rem`, `line-height: 1.2`, `letter-spacing: -.03rem`, `font-weight: 600`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 12.3429px`, `line-height: 14.8114px`, `font-weight: 600`, `letter-spacing: -0.308571px`); CSS variables `--default-mono-font-family: var(--font-mono)`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.23,1,.32,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.home-work[data-v-187357cc]:before`**: `transition: transform .7s ease-out .11s` extracted from `www-romainavalle-dev` stylesheet.
- **Selector `.lenis.lenis-autoToggle`**: `transition: 1ms` extracted from `www-romainavalle-dev` stylesheet.
- **Selector `.back .arrow[data-v-9e8fb527]`**: `transition: transform .3s` extracted from `www-romainavalle-dev` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.23,1,.32,1)`)**: Governs interactive state transitions across `<header.gap-8>` and `<section.bg-black>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Romain Avalle - Interactive developper     │
│ ====================================================================== │
│ [ <header.gap-8> (337x31px)           | Let's talk                   ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.white> (w=1440px)                             | │
│ | H1: Romain Avalle                                                  | │
│ | Substrate: #ffffff | Ink: #000000 | Accent: #f3f2f1                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.bg-black>) max-w: 1440px                   | │
│ | +------------------------------+  +------------------------------+ | │
│ | | R o m a i n A v a l l e      |  | I n t e r a c t i v e D e v  | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.text-white>) — █ █ █ █ █ █ █ █ █ █ █       | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.z-1>        ) | https://www.romainavalle.dev/        │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 8.22857p)   │
│ ====================================================================== │
│ [ HEADER BAR (<header.gap-8>          ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.white>) — 390px Vertical Lead                 | │
│ | H1: Romain Avalle                                                  | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.bg-black>) — 1-Col Stack                  | │
│ | [ Item 1: R o m a i n A v a l l e                                ] | │
│ | [ Item 2: I n t e r a c t i v e D e v e l o p e r                ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.text-white>) — 1-Col (█ █ █ █ █ █ █ █ █ )   | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.z-1>        ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.gap-8> — `www-romainavalle-dev`)**:
   - Landmark `<header class="gap-8 bottom-30">` (`337x31px`) hosting `Romain Avalle - Interactive developp` navigation (`Let's talk`), DOM attributes (`data-v-54411a74`, `data-char="R"`, `data-char="o"`, `data-char="m"`), and stylesheet rule `.common-scene { height:100lvh }`.
2. **Hero Stage & Focal Lead (<section.white> — `Romain Avalle`)**:
   - Landmark `<section class="white">` presenting display lead `Romain Avalle` and copy excerpt *"I'm Romain Avalle, an interactive developer with 20 years of dedi"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.bg-black> — `R o m a i n A v a l l e`)**:
   - Landmark `<section class="bg-black">` rendering section `R o m a i n A v a l l e` with copy *"Interactive Developer"*, asset references (`gtm.js`, `_payload.json`, `BC66KIH3.js`, `B3W-aES6.js`), and grid rule `before { transform:scaleX(1) }`.
4. **Interactive Detail & Feature Matrix (<section.text-white> — `I n t e r a c t i v e D e v e l o `)**:
   - Landmark `<section class="text-white">` framing `I n t e r a c t i v e D e v e l o p e r` and `█ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ ░ ░ ░ ░ ░ ░ ░ ░ ` (*"█ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░"*) with `#000000` surface cards, `#f3f2f1` accents, and `html.lenis body { height:auto }`.
5. **Colophon & Global Directory Footer (<footer.z-1> — `https://www.romainavalle.dev/`)**:
   - Landmark `<footer class="z-1 h-screen">` anchoring `Romain Avalle - Interactive deve` footer links (`Let's talk`), copy *"R o m a i n A v a l l e"*, and `#000000` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-romainavalle-dev (Romain Avalle - Interactive developper)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-romainavalle-dev` (**Romain Avalle - Interactive developper** — `https://www.romainavalle.dev/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#f3f2f1`).
- **Identity & Domain Context**: Romain Avalle, interactive developer since 2006. Team Lead & Tech Lead at REF Digital in Montréal. Awwwards jury member, 40+ Awwwards and...
- **Primary Substrate**: `#ffffff` (live computed `browser-default` `background-color` (`computed_styles.json`)), **Primary Ink**: `#000000`, **Accent / Highlight**: `#f3f2f1`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `browser-default` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#f3f2f1` accents.
  - **Grounded Typographic Hierarchy**: Pairs `RemusVariableVF` for display copy (`Romain Avalle`) with `RemusVariableVF` and `andale-mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 8.22857px`, padding `8.22857px`) with `cubic-bezier(.23,1,.32,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-romainavalle-dev` in your global stylesheet:

:root {
  /* Romain Avalle - Interactive developper (www-romainavalle-dev) — Live-Grounded CSS Variables */
  --size: 375; /* Layout / Spatial Grid Token (www-romainavalle-dev) */
  --lvh: 1lvh; /* Layout / Spatial Grid Token (www-romainavalle-dev) */
  --dvh: 1dvh; /* Layout / Spatial Grid Token (www-romainavalle-dev) */
  --svh: 1svh; /* Layout / Spatial Grid Token (www-romainavalle-dev) */
  --spacing: .1rem; /* Layout / Spatial Grid Token (www-romainavalle-dev) */
  --default-transition-duration: .15s; /* Motion / Easing Token (www-romainavalle-dev) */
  --default-transition-timing-function: cubic-bezier(.23, 1, .32, 1); /* Motion / Easing Token (www-romainavalle-dev) */
  --default-font-family: var(--font-sans); /* Typography / Scale Token (www-romainavalle-dev) */
  --default-mono-font-family: var(--font-mono); /* Typography / Scale Token (www-romainavalle-dev) */
  --color-white: #fff; /* Canvas / Surface Token (www-romainavalle-dev) */
  --color-black: #000; /* Canvas / Surface Token (www-romainavalle-dev) */
  --tw-translate-x: 0; /* Design System Custom Token (www-romainavalle-dev) */
  --tw-translate-y: 0; /* Design System Custom Token (www-romainavalle-dev) */
  --tw-translate-z: 0; /* Design System Custom Token (www-romainavalle-dev) */
  --www-romainavalle-bg: #ffffff; /* Canvas Substrate (from live computed `browser-default` `background-color` (`computed_styles.json`)) (www-romainavalle-dev) */
  --www-romainavalle-ink: #000000; /* Primary Typography Ink (computed-derived) (www-romainavalle-dev) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ffffff` — grounded in live computed `browser-default` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#000000` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#000000` — grounded in live computed `header` `background-color` (`computed_styles.json`)
- **Interactive Accent / Highlight**: `#f3f2f1` — grounded in `<meta name="theme-color" content="#f3f2f1">` in `dom.html`
- **Secondary / Muted Copy**: `#000000` — grounded in secondary opacity step of live computed `h1` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#000000` — grounded in hairline divider derived from secondary opacity step of live computed `h1` `color` (`computed_styles.json`)

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×900px` (single-viewport 100vh live capture (900px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport)
- **Padding & Gutters**: `8.22857px` lateral canvas padding with `8.22857px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 8.22857px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `8.22857px` horizontal padding
- **Media Queries**: `@media (width>=650px)`, `@media (width>=1024px)`, `@media (width>=800px)`
- **Corner Radii**: `3.08571px`, `.3rem`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `RemusVariableVF`
- **Body Font Stack**: `RemusVariableVF`
- **Monospace / Technical Font Stack**: `andale-mono`
- **H1 Display Rule**: live computed `h1` (`font-size: 16.4571px`, `line-height: 19.7486px`, `font-weight: 600`, `letter-spacing: -0.308571px`)
- **H2 Section Rule**: live computed `h2` (`font-size: 16.4571px`, `line-height: 19.7486px`, `font-weight: 600`, `letter-spacing: -0.308571px`)
- **Body Copy Rule**: live computed `body` (`font-size: 16.4571px`, `line-height: 19.7486px`, `font-weight: 600`, `letter-spacing: -0.308571px`); rule `,body` (`font-size: 1.6rem`, `line-height: 1.2`, `letter-spacing: -.03rem`, `font-weight: 600`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 12.3429px`, `line-height: 14.8114px`, `font-weight: 600`, `letter-spacing: -0.308571px`); CSS variables `--default-mono-font-family: var(--font-mono)`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-romainavalle-dev` (`Romain Avalle - Interactive developper`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.gap-8> — `www-romainavalle-dev`)**:
   - DOM & Selectors: Landmark `<header class="gap-8 bottom-30">` (`337x31px`) hosting `Romain Avalle - Interactive developp` navigation (`Let's talk`), DOM attributes (`data-v-54411a74`, `data-char="R"`, `data-char="o"`, `data-char="m"`), and stylesheet rule `.common-scene { height:100lvh }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.gap-8> — `www-romainavalle-dev`)` (`www-romainavalle-dev`) adapts across `@media (width>=650px)`, `@media (width>=1024px)`, `@media (width>=800px)` with `cubic-bezier(.23,1,.32,1)` transitions and links `Let's talk`.
2. **Hero Stage & Focal Lead (<section.white> — `Romain Avalle`)**:
   - DOM & Selectors: Landmark `<section class="white">` presenting display lead `Romain Avalle` and copy excerpt *"I'm Romain Avalle, an interactive developer with 20 years of dedi"* over `#ffffff` canvas and `#000000` ink.
   - Responsive Contract: Hero stage (`1440×900px` desktop / `390×2400px` mobile) sets `#ffffff` background with `#000000` headline `Romain Avalle`.
3. **Primary Showcase & Content Grid (<section.bg-black> — `R o m a i n A v a l l e`)**:
   - DOM & Selectors: Landmark `<section class="bg-black">` rendering section `R o m a i n A v a l l e` with copy *"Interactive Developer"*, asset references (`gtm.js`, `_payload.json`, `BC66KIH3.js`, `B3W-aES6.js`), and grid rule `before { transform:scaleX(1) }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.bg-black> — `R o m a i n A v a l l e`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 8.22857px`) on desktop and Single-column vertical stack at `390px` viewport width with `8.22857px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.text-white> — `I n t e r a c t i v e D e v e l o `)**:
   - DOM & Selectors: Landmark `<section class="text-white">` framing `I n t e r a c t i v e D e v e l o p e r` and `█ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ ░ ░ ░ ░ ░ ░ ░ ░ ` (*"█ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░"*) with `#000000` surface cards, `#f3f2f1` accents, and `html.lenis body { height:auto }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.text-white> — `I n t e r a c t i v e D e v e l o `)` uses `3.08571px`, `.3rem` radii, `#f3f2f1` highlights, and assets (gtm.js, _payload.json, BC66KIH3.js).
5. **Colophon & Global Directory Footer (<footer.z-1> — `https://www.romainavalle.dev/`)**:
   - DOM & Selectors: Landmark `<footer class="z-1 h-screen">` anchoring `Romain Avalle - Interactive deve` footer links (`Let's talk`), copy *"R o m a i n A v a l l e"*, and `#000000` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.z-1> — `https://www.romainavalle.dev/`)` aligns to `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport) with `8.22857px` lateral canvas padding with `8.22857px` grid gap and attributes (data-v-54411a74, data-char="R", data-char="o").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"I'm Romain Avalle, an interactive developer with 20 years of dedicated experience..."*
- Copy Excerpt 2: *"Interactive Developer"*
- Copy Excerpt 3: *"█ █ █ █ █ █ █ █ █ █ █ █ █ █ █ █ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░"*
- Copy Excerpt 4: *"R o m a i n A v a l l e"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.23,1,.32,1)`
- **Extracted Stylesheet Rules (`www-romainavalle-dev`)**:
- `.common-scene { height:100lvh }`
- `before { transform:scaleX(1) }`
- `html.lenis body { height:auto }`
- `.lenis-stopped { overflow:clip }`
- `.lenis.lenis-smooth iframe { pointer-events:none }`
- **Per-Selector Transition Rules**:
- **Selector `.home-work[data-v-187357cc]:before`**: `transition: transform .7s ease-out .11s` extracted from `www-romainavalle-dev` stylesheet.
- **Selector `.lenis.lenis-autoToggle`**: `transition: 1ms` extracted from `www-romainavalle-dev` stylesheet.
- **Selector `.back .arrow[data-v-9e8fb527]`**: `transition: transform .3s` extracted from `www-romainavalle-dev` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.23,1,.32,1)`)**: Governs interactive state transitions across `<header.gap-8>` and `<section.bg-black>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-romainavalle-dev`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
