---
title: "UI Prompt Blueprint: halloween-ferayna-com"
date: 2026-11-15
target: "[[overview|halloween-ferayna-com]]"
status: analyzed
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#0c0f0e` / `#5c6c63`)"
---

# UI Design System & Master Generation Blueprint: halloween-ferayna-com

> **Every brief has a face · Ferayna** (https://halloween.ferayna.com/) — Nine projects you have met before, carved into lanterns on a rock spire. A Halloween scene by Ferayna. Scroll to climb.

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/halloween-ferayna-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Every brief has a face · Ferayna** (`https://halloween.ferayna.com/`). Nine projects you have met before, carved into lanterns on a rock spire. A Halloween scene by Ferayna. Scroll to climb.
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#0c0f0e` / `#5c6c63`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#0c0f0e` (`var(--colors-night)` in `:root`) paired with `#ece7e1` primary typography and `#5c6c63` accents.
  - **Extracted Typographic Hierarchy**: Pairs `reckless` for display copy (`Every brief has a face`) with `reckless Fallback` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `40ch` container bounds (`gap: 0px (flush layout)`, padding `4px`) with `cubic-bezier(.4,0,.2,1)` easing and HTML5 `<canvas>` Interactive Viewport Surface.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/halloween-ferayna-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `40ch` extracted from `halloween-ferayna-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `4px` lateral canvas padding with `0px (flush layout)` grid gap.
- **Border Radius Scale**: `.25rem`, `var(--radius-3xl)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40ch`, `gap: 0px (flush layout)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `4px` horizontal padding.
- **Extracted CSS Media Queries**: `@media not all and (min-width:64rem)`, `@media not all and (min-width:48rem)`, `@media (max-width:767px)`, `@media (prefers-reduced-motion:reduce)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#0c0f0e` | `var(--colors-night)` in `:root` |
| **Primary Typography Ink** | `#151a18` | `var(--colors-plate)` in `:root` |
| **Elevated Surface / Card Substrate** | `#29322e` | `var(--colors-moss)` in `:root` |
| **Interactive Accent / Highlight** | `#5c6c63` | `var(--colors-sage)` in `:root` |
| **Secondary / Muted Copy** | `#9aa69f` | `var(--colors-dim)` in `:root` |
| **Structural Hairline Border** | `#ece7e1` | `var(--colors-ink)` in `:root` |
| **Variable Token (`--colors-green`)** | `#37d657` | `var(--colors-green)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-reckless` | `"reckless", "reckless Fallback"` | Typography / Scale Token |
| `--font-grotta` | `"grotta", "grotta Fallback"` | Typography / Scale Token |
| `--thread-at` | `0%` | Dimension / Scale Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--radius-3xl` | `1.5rem` | Elevation / Border Token |
| `--default-transition-duration` | `.15s` | Motion / Easing Token |
| `--default-transition-timing-function` | `cubic-bezier(.4, 0, .2, 1)` | Motion / Easing Token |
| `--default-font-family` | `var(--typography-font-sans)` | Typography / Scale Token |
| `--default-mono-font-family` | `var(--typography-font-mono)` | Typography / Scale Token |
| `--colors-night` | `#0c0f0e` | Brand / Palette Token |
| `--colors-plate` | `#151a18` | Brand / Palette Token |
| `--colors-moss` | `#29322e` | Brand / Palette Token |
| `--colors-sage` | `#5c6c63` | Brand / Palette Token |
| `--colors-dim` | `#9aa69f` | Brand / Palette Token |
| `--colors-ink` | `#ece7e1` | Typography Ink Token |
| `--colors-green` | `#37d657` | Brand / Palette Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `reckless`.
- **Primary Body Stack**: `reckless Fallback`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--typography-font-display: var(--font-reckless), Georgia, serif`.
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `13px`, `6px`).
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `13px`, `6px`).
- **Metadata & Navigation Labels**: CSS variables `--default-mono-font-family: var(--typography-font-mono)`, `--typography-font-mono: ui-monospace, SFMono-Regular, Menlo`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.65,0,.35,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: .15s` extracted from `halloween-ferayna-com` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `halloween-ferayna-com` stylesheet.
- **Selector `opacity\]`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `halloween-ferayna-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<nav.scene-thread>` and `<main.antialiased>`.
- **Runtime Interaction Engine**: Integrates HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Every brief has a face · Ferayna           │
│ ====================================================================== │
│ [ <nav.scene-thread>       | Overview · Index · Archive · About · C ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <main.text-foreground>                               |   │
│ | H1: Every brief has a face                                       |   │
│ | Substrate: #0c0f0e    | Ink: #ece7e1    | Accent: #5c6c63        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<main.antialiased>        ) max-w: 40ch           |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | The simple one               |  | The serious one              | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 0px (f) | │
│ | [<nav.scene-thread>] -> [<main.text-foregro] -> [<main.antialiased>] │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.scene-stage>  ) | https://halloween.ferayna.com/     │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.scene-thread> — `halloween-ferayna-com`)**:
   - Landmark `<nav class="scene-thread pointer-events-none">` hosting `Every brief has a face · Ferayna` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-scene-stage="true"`, `data-shot="0"`, `data-scene-fade="true"`), and stylesheet rule `less_ee4802df-module__FYuYzW__cla... { font-family:reckless,reckless Fallback;font-style:normal;font-weight:400 }`.
2. **Hero Stage & Focal Lead (<main.text-foreground> — `Every brief has a face`)**:
   - Landmark `<main class="text-foreground">` presenting display lead `Every brief has a face` and copy excerpt *"The lanterns can't light in this browser."* over `#0c0f0e` canvas and `#ece7e1` ink.
3. **Primary Showcase & Content Grid (<main.antialiased> — `The simple one`)**:
   - Landmark `<main class="antialiased">` rendering section `The simple one` with copy *"Every brief has a face"*, asset references (`Grotta_Regular-s.p.0hpxf2bw567b9....`, `RecklessCondensedS_Book-s.p.2no44...`, `2qvmtax7tpqlc.css`, `3dxvrezqwk0-f.js`), and grid rule `kless_ee4802df-module__FYuYzW__va... { --font-reckless:"reckless", "reckless Fallback" }`.
4. **Interactive Detail & Feature Matrix (<main.sr-only> — `The serious one`)**:
   - Landmark `<main class="sr-only">` framing `The serious one` and `The secret one` (*"Nine projects you have met before. Scroll to meet them again."*) with `#29322e` surface cards, `#5c6c63` accents, and `otta_9a104af5-module__lGjW5a__cla... { font-family:grotta,grotta Fallback;font-style:normal;font-weight:400 }`.
5. **Colophon & Global Directory Footer (<footer.scene-stage> — `https://halloween.ferayna.com/`)**:
   - Landmark `<footer class="scene-stage">` anchoring `Every brief has a face · Ferayna` footer links (`Overview · Index · Archive · About · Contact`), copy *"Turn the sound on Turn Turn the the sound sound on on"*, and `#ece7e1` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: halloween-ferayna-com (Every brief has a face · Ferayna)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `halloween-ferayna-com` (**Every brief has a face · Ferayna** — `https://halloween.ferayna.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#0c0f0e` / `#5c6c63`).
- **Identity & Domain Context**: Nine projects you have met before, carved into lanterns on a rock spire. A Halloween scene by Ferayna. Scroll to climb.
- **Primary Substrate**: `#0c0f0e` (`var(--colors-night)` in `:root`), **Primary Ink**: `#ece7e1`, **Accent / Highlight**: `#5c6c63`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#0c0f0e` (`var(--colors-night)` in `:root`) paired with `#ece7e1` primary typography and `#5c6c63` accents.
  - **Extracted Typographic Hierarchy**: Pairs `reckless` for display copy (`Every brief has a face`) with `reckless Fallback` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `40ch` container bounds (`gap: 0px (flush layout)`, padding `4px`) with `cubic-bezier(.4,0,.2,1)` easing and HTML5 `<canvas>` Interactive Viewport Surface.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `halloween-ferayna-com` in your global stylesheet:

:root {
  /* Every brief has a face · Ferayna (halloween-ferayna-com) — Ground-Truth Extracted CSS Variables */
  --font-reckless: "reckless", "reckless Fallback"; /* Typography / Scale Token (halloween-ferayna-com) */
  --font-grotta: "grotta", "grotta Fallback"; /* Typography / Scale Token (halloween-ferayna-com) */
  --thread-at: 0%; /* Dimension / Scale Token (halloween-ferayna-com) */
  --spacing: .25rem; /* Layout / Spatial Grid Token (halloween-ferayna-com) */
  --radius-3xl: 1.5rem; /* Elevation / Border Token (halloween-ferayna-com) */
  --default-transition-duration: .15s; /* Motion / Easing Token (halloween-ferayna-com) */
  --default-transition-timing-function: cubic-bezier(.4, 0, .2, 1); /* Motion / Easing Token (halloween-ferayna-com) */
  --default-font-family: var(--typography-font-sans); /* Typography / Scale Token (halloween-ferayna-com) */
  --default-mono-font-family: var(--typography-font-mono); /* Typography / Scale Token (halloween-ferayna-com) */
  --colors-night: #0c0f0e; /* Brand / Palette Token (halloween-ferayna-com) */
  --colors-plate: #151a18; /* Brand / Palette Token (halloween-ferayna-com) */
  --colors-moss: #29322e; /* Brand / Palette Token (halloween-ferayna-com) */
  --colors-sage: #5c6c63; /* Brand / Palette Token (halloween-ferayna-com) */
  --colors-dim: #9aa69f; /* Brand / Palette Token (halloween-ferayna-com) */
  --colors-ink: #ece7e1; /* Typography Ink Token (halloween-ferayna-com) */
  --colors-green: #37d657; /* Brand / Palette Token (halloween-ferayna-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#0c0f0e` — grounded in `var(--colors-night)` in `:root`
- **Primary Typography Ink**: `#151a18` — grounded in `var(--colors-plate)` in `:root`
- **Elevated Surface / Card Substrate**: `#29322e` — grounded in `var(--colors-moss)` in `:root`
- **Interactive Accent / Highlight**: `#5c6c63` — grounded in `var(--colors-sage)` in `:root`
- **Secondary / Muted Copy**: `#9aa69f` — grounded in `var(--colors-dim)` in `:root`
- **Structural Hairline Border**: `#ece7e1` — grounded in `var(--colors-ink)` in `:root`
- **Variable Token (`--colors-green`)**: `#37d657` — grounded in `var(--colors-green)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `40ch` extracted from `halloween-ferayna-com` stylesheet
- **Padding & Gutters**: `4px` lateral canvas padding with `0px (flush layout)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40ch`, `gap: 0px (flush layout)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `4px` horizontal padding
- **Media Queries**: `@media not all and (min-width:64rem)`, `@media not all and (min-width:48rem)`, `@media (max-width:767px)`, `@media (prefers-reduced-motion:reduce)`
- **Corner Radii**: `.25rem`, `var(--radius-3xl)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `reckless`
- **Body Font Stack**: `reckless Fallback`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: CSS variables `--typography-font-display: var(--font-reckless), Georgia, serif`
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `13px`, `6px`)
- **Body Copy Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `13px`, `6px`)
- **Metadata & Index Rule**: CSS variables `--default-mono-font-family: var(--typography-font-mono)`, `--typography-font-mono: ui-monospace, SFMono-Regular, Menlo`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `halloween-ferayna-com` (`Every brief has a face · Ferayna`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.scene-thread> — `halloween-ferayna-com`)**:
   - DOM & Selectors: Landmark `<nav class="scene-thread pointer-events-none">` hosting `Every brief has a face · Ferayna` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-scene-stage="true"`, `data-shot="0"`, `data-scene-fade="true"`), and stylesheet rule `less_ee4802df-module__FYuYzW__cla... { font-family:reckless,reckless Fallback;font-style:normal;font-weight:400 }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.scene-thread> — `halloween-ferayna-com`)` (`halloween-ferayna-com`) adapts across `@media not all and (min-width:64rem)`, `@media not all and (min-width:48rem)`, `@media (max-width:767px)`, `@media (prefers-reduced-motion:reduce)` with `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.65,0,.35,1)` transitions and links `Overview · Index · Archive · About · Contact`.
2. **Hero Stage & Focal Lead (<main.text-foreground> — `Every brief has a face`)**:
   - DOM & Selectors: Landmark `<main class="text-foreground">` presenting display lead `Every brief has a face` and copy excerpt *"The lanterns can't light in this browser."* over `#0c0f0e` canvas and `#ece7e1` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#0c0f0e` background with `#ece7e1` headline `Every brief has a face`.
3. **Primary Showcase & Content Grid (<main.antialiased> — `The simple one`)**:
   - DOM & Selectors: Landmark `<main class="antialiased">` rendering section `The simple one` with copy *"Every brief has a face"*, asset references (`Grotta_Regular-s.p.0hpxf2bw567b9....`, `RecklessCondensedS_Book-s.p.2no44...`, `2qvmtax7tpqlc.css`, `3dxvrezqwk0-f.js`), and grid rule `kless_ee4802df-module__FYuYzW__va... { --font-reckless:"reckless", "reckless Fallback" }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<main.antialiased> — `The simple one`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40ch`, `gap: 0px (flush layout)`) on desktop and Single-column vertical stack at `390px` viewport width with `4px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<main.sr-only> — `The serious one`)**:
   - DOM & Selectors: Landmark `<main class="sr-only">` framing `The serious one` and `The secret one` (*"Nine projects you have met before. Scroll to meet them again."*) with `#29322e` surface cards, `#5c6c63` accents, and `otta_9a104af5-module__lGjW5a__cla... { font-family:grotta,grotta Fallback;font-style:normal;font-weight:400 }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<main.sr-only> — `The serious one`)` uses `.25rem`, `var(--radius-3xl)` radii, `#5c6c63` highlights, and assets (Grotta_Regular-s.p.0hpxf2bw567b9...., RecklessCondensedS_Book-s.p.2no44..., 2qvmtax7tpqlc.css).
5. **Colophon & Global Directory Footer (<footer.scene-stage> — `https://halloween.ferayna.com/`)**:
   - DOM & Selectors: Landmark `<footer class="scene-stage">` anchoring `Every brief has a face · Ferayna` footer links (`Overview · Index · Archive · About · Contact`), copy *"Turn the sound on Turn Turn the the sound sound on on"*, and `#ece7e1` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.scene-stage> — `https://halloween.ferayna.com/`)` aligns to `40ch` extracted from `halloween-ferayna-com` stylesheet with `4px` lateral canvas padding with `0px (flush layout)` grid gap and attributes (data-precedence="next", data-scene-stage="true", data-shot="0").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"The lanterns can't light in this browser."*
- Copy Excerpt 2: *"Every brief has a face"*
- Copy Excerpt 3: *"Nine projects you have met before. Scroll to meet them again."*
- Copy Excerpt 4: *"Turn the sound on Turn Turn the the sound sound on on"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.65,0,.35,1)`
- **Extracted Stylesheet Rules (`halloween-ferayna-com`)**:
- `less_ee4802df-module__FYuYzW__cla... { font-family:reckless,reckless Fallback;font-style:normal;font-weight:400 }`
- `kless_ee4802df-module__FYuYzW__va... { --font-reckless:"reckless", "reckless Fallback" }`
- `otta_9a104af5-module__lGjW5a__cla... { font-family:grotta,grotta Fallback;font-style:normal;font-weight:400 }`
- `rotta_9a104af5-module__lGjW5a__va... { --font-grotta:"grotta", "grotta Fallback" }`
- `host { --thread-at:0% }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: .15s` extracted from `halloween-ferayna-com` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `halloween-ferayna-com` stylesheet.
- **Selector `opacity\]`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `halloween-ferayna-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<nav.scene-thread>` and `<main.antialiased>`.
- **Runtime Interaction Engine**: Integrates HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `halloween-ferayna-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
