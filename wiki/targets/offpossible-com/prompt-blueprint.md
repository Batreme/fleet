---
title: "UI Prompt Blueprint: offpossible-com"
date: 2026-11-15
target: "[[overview|offpossible-com]]"
status: analyzed
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#0006`)"
---

# UI Design System & Master Generation Blueprint: offpossible-com

> **OffPossible · Interfaces Between People and Their Own Minds** (https://offpossible.com/) — OffPossible builds and backs interfaces between people and their own minds. In-house products live at Noumen, including Actually and None...

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/offpossible-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **OffPossible · Interfaces Between People and Their Own Minds** (`https://offpossible.com/`). OffPossible builds and backs interfaces between people and their own minds. In-house products live at Noumen, including Actually and None...
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#0006`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--scramble-color)` in `:root`) paired with `#fff` primary typography and `#0006` accents.
  - **Extracted Typographic Hierarchy**: Pairs `ABC Diatype Semi Mono` for display copy (`We build and back interfaces between`) with `Inter` and `ABC Diatype Semi Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `36px` container bounds (`gap: 48px`, padding `var(--edge-inset)`) with `cubic-bezier(.16,1,.3,1)` easing and HTML5 `<canvas>` Interactive Viewport Surface.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/offpossible-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `36px` extracted from `offpossible-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `var(--edge-inset)` lateral canvas padding with `48px` grid gap.
- **Border Radius Scale**: `50%`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 36px`, `gap: 48px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--edge-inset)` horizontal padding.
- **Extracted CSS Media Queries**: `@media (width>=1000px) and (orientation:landscape),(width>=560px...`, `@media (prefers-reduced-motion:reduce)`, `@media (width<=768px)`, `@media (width>=769px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--scramble-color)` in `:root` |
| **Primary Typography Ink** | `#fff` | `.chrome-hit { color: #fff }` |
| **Elevated Surface / Card Substrate** | `#fff6` | `.footer-action-muted { color: #fff6 }` |
| **Interactive Accent / Highlight** | `#0006` | `.footer-action-muted { color: #0006 }` |
| **Secondary / Muted Copy** | `#0b351c` | `.stack-line-accent { color: #0b351c }` |
| **Structural Hairline Border** | `#f4cae3` | `.stack-line-accent { color: #f4cae3 }` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--edge-inset` | `max(20px, 2vmin)` | Dimension / Scale Token |
| `--header-logo-width` | `24.53vw` | Layout / Spatial Grid Token |
| `--header-logo-height` | `calc(var(--header-logo-width) * 75 / 533)` | Layout / Spatial Grid Token |
| `--header-logo-ink-top` | `calc(var(--header-logo-height) * 2.98828 / 75)` | Typography Ink Token |
| `--site-symbol-size` | `calc(var(--header-logo-height) * 70.39 / 75)` | Layout / Spatial Grid Token |
| `--font-mono` | `"ABC Diatype Semi Mono", ui-monospace, "SF Mono", Menlo, monospace` | Typography / Scale Token |
| `--font-display` | `var(--font-mono)` | Typography / Scale Token |
| `--font-ui` | `"Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif` | Typography / Scale Token |
| `--instrument-panel-gap` | `clamp(16px, 1.5vw, 24px)` | Layout / Spatial Grid Token |
| `--scramble-color` | `#000!important` | Brand / Palette Token |
| `--mobile-screen-inset` | `24px` | Dimension / Scale Token |
| `--mobile-screen-padding-x` | `8px` | Layout / Spatial Grid Token |
| `--mobile-shader-overscan-y` | `240px` | Dimension / Scale Token |
| `--instrument-intensity` | `1.000` | Design System Custom Token |
| `--instrument-certainty` | `0.000` | Design System Custom Token |
| `--instrument-agency` | `1.000` | Design System Custom Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `ABC Diatype Semi Mono`.
- **Primary Body Stack**: `Inter`.
- **Technical / Metadata Stack**: `ABC Diatype Semi Mono`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--font-display: var(--font-mono)`; rule `h1` (`font-size: clamp(46px,8vw,88px)`, `line-height: .95`, `letter-spacing: -.045em`, `font-weight: 400`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: 18px`, `line-height: 1.2`, `letter-spacing: -.02em`, `font-weight: 400`).
- **Body Copy**: rule `p` (`font-size: 20px`, `line-height: 1.25`, `letter-spacing: -.2px`).
- **Metadata & Navigation Labels**: CSS variables `--font-mono: "ABC Diatype Semi Mono", ui-monospace, "SF Mono", Menlo, monospace`; rule `.label` (`font-size: 16px`, `line-height: 1.25`, `letter-spacing: -.16px`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.16,1,.3,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `t-flooding .backdrop-grid.backdro...`**: `transition: none` extracted from `offpossible-com` stylesheet.
- **Selector `html.prompt-closing .easter-prompt`**: `transition: .2s` extracted from `offpossible-com` stylesheet.
- **Selector `.site-symbol-orbit-shape`**: `transition: transform .42s cubic-bezier(.16,1,.3,1),opacity .24s,rx .42s c...` extracted from `offpossible-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.16,1,.3,1)`)**: Governs interactive state transitions across `<header.backdrop-grid>` and `<section.scroll-section>`.
- **Runtime Interaction Engine**: Integrates HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — OffPossible · Interfaces Between People an │
│ ====================================================================== │
│ [ <header.backdrop-grid>   | Noumen · Privacy · seenoumen.com       ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.easter-prompt>                              |   │
│ | H1: We build and back interfaces between people and t...         |   │
│ | Substrate: #000       | Ink: #fff       | Accent: #0006          |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.scroll-section>  ) max-w: 36px           |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | No one has direct sight of t |  | We support builders who make | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 48px  ) | │
│ | [<header.backdrop-g] -> [<section.easter-pr] -> [<section.scroll-se] │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.site-footer>  ) | https://offpossible.com/           │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.backdrop-grid> — `offpossible-com`)**:
   - Landmark `<header class="backdrop-grid">` hosting `OffPossible · Interfaces Between Peo` navigation (`Noumen · Privacy · seenoumen.com`), DOM attributes (`data-shader-layer="fixed"`, `data-field-sound="muted"`, `data-agency-mode="steer"`, `data-content-mode="base"`), and stylesheet rule `body { background-color:000;width:100%;min-height:100vh;overflow-x:hidden }`.
2. **Hero Stage & Focal Lead (<section.easter-prompt> — `We build and back interfaces betwe`)**:
   - Landmark `<section class="easter-prompt">` presenting display lead `We build and back interfaces between people and t...` and copy excerpt *"M h a t w o u l d y o u b u i l d ?"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.scroll-section> — `No one has direct sight of their o`)**:
   - Landmark `<section class="scroll-section">` rendering section `No one has direct sight of their own mind.` with copy *"Privacy Policy Privacy"*, asset references (`clarity.js`, `z1sq4va9rn`, `sitemap.xml`, `llms.txt`), and grid rule `webkit-scrollbar { display:none }`.
4. **Interactive Detail & Feature Matrix (<section.scroll-section> — `We support builders who make peopl`)**:
   - Landmark `<section class="scroll-section">` framing `We support builders who make people more legible...` and `We work early enough to change the question, not...` (*"Prompts and generated results may be privately retained and revie"*) with `#fff6` surface cards, `#0006` accents, and `html.no-js .sound-toggle { display:none }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://offpossible.com/`)**:
   - Landmark `<footer class="site-footer">` anchoring `OffPossible · Interfaces Between` footer links (`Noumen · Privacy · seenoumen.com`), copy *"Lenses gave people sight of cells and distant planets."*, and `#f4cae3` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: offpossible-com (OffPossible · Interfaces Between People and Their Own Minds)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `offpossible-com` (**OffPossible · Interfaces Between People and Their Own Minds** — `https://offpossible.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#0006`).
- **Identity & Domain Context**: OffPossible builds and backs interfaces between people and their own minds. In-house products live at Noumen, including Actually and None...
- **Primary Substrate**: `#000` (`var(--scramble-color)` in `:root`), **Primary Ink**: `#fff`, **Accent / Highlight**: `#0006`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--scramble-color)` in `:root`) paired with `#fff` primary typography and `#0006` accents.
  - **Extracted Typographic Hierarchy**: Pairs `ABC Diatype Semi Mono` for display copy (`We build and back interfaces between`) with `Inter` and `ABC Diatype Semi Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `36px` container bounds (`gap: 48px`, padding `var(--edge-inset)`) with `cubic-bezier(.16,1,.3,1)` easing and HTML5 `<canvas>` Interactive Viewport Surface.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `offpossible-com` in your global stylesheet:

:root {
  /* OffPossible · Interfaces Between People and Their Own Minds (offpossible-com) — Ground-Truth Extracted CSS Variables */
  --edge-inset: max(20px, 2vmin); /* Dimension / Scale Token (offpossible-com) */
  --header-logo-width: 24.53vw; /* Layout / Spatial Grid Token (offpossible-com) */
  --header-logo-height: calc(var(--header-logo-width) * 75 / 533); /* Layout / Spatial Grid Token (offpossible-com) */
  --header-logo-ink-top: calc(var(--header-logo-height) * 2.98828 / 75); /* Typography Ink Token (offpossible-com) */
  --site-symbol-size: calc(var(--header-logo-height) * 70.39 / 75); /* Layout / Spatial Grid Token (offpossible-com) */
  --font-mono: "ABC Diatype Semi Mono", ui-monospace, "SF Mono", Menlo, monospace; /* Typography / Scale Token (offpossible-com) */
  --font-display: var(--font-mono); /* Typography / Scale Token (offpossible-com) */
  --font-ui: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; /* Typography / Scale Token (offpossible-com) */
  --instrument-panel-gap: clamp(16px, 1.5vw, 24px); /* Layout / Spatial Grid Token (offpossible-com) */
  --scramble-color: #000!important; /* Brand / Palette Token (offpossible-com) */
  --mobile-screen-inset: 24px; /* Dimension / Scale Token (offpossible-com) */
  --mobile-screen-padding-x: 8px; /* Layout / Spatial Grid Token (offpossible-com) */
  --mobile-shader-overscan-y: 240px; /* Dimension / Scale Token (offpossible-com) */
  --instrument-intensity: 1.000; /* Design System Custom Token (offpossible-com) */
  --instrument-certainty: 0.000; /* Design System Custom Token (offpossible-com) */
  --instrument-agency: 1.000; /* Design System Custom Token (offpossible-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#000` — grounded in `var(--scramble-color)` in `:root`
- **Primary Typography Ink**: `#fff` — grounded in `.chrome-hit { color: #fff }`
- **Elevated Surface / Card Substrate**: `#fff6` — grounded in `.footer-action-muted { color: #fff6 }`
- **Interactive Accent / Highlight**: `#0006` — grounded in `.footer-action-muted { color: #0006 }`
- **Secondary / Muted Copy**: `#0b351c` — grounded in `.stack-line-accent { color: #0b351c }`
- **Structural Hairline Border**: `#f4cae3` — grounded in `.stack-line-accent { color: #f4cae3 }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `36px` extracted from `offpossible-com` stylesheet
- **Padding & Gutters**: `var(--edge-inset)` lateral canvas padding with `48px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 36px`, `gap: 48px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--edge-inset)` horizontal padding
- **Media Queries**: `@media (width>=1000px) and (orientation:landscape),(width>=560px...`, `@media (prefers-reduced-motion:reduce)`, `@media (width<=768px)`, `@media (width>=769px)`
- **Corner Radii**: `50%`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `ABC Diatype Semi Mono`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: `ABC Diatype Semi Mono`
- **H1 Display Rule**: CSS variables `--font-display: var(--font-mono)`; rule `h1` (`font-size: clamp(46px,8vw,88px)`, `line-height: .95`, `letter-spacing: -.045em`, `font-weight: 400`)
- **H2 Section Rule**: rule `h2` (`font-size: 18px`, `line-height: 1.2`, `letter-spacing: -.02em`, `font-weight: 400`)
- **Body Copy Rule**: rule `p` (`font-size: 20px`, `line-height: 1.25`, `letter-spacing: -.2px`)
- **Metadata & Index Rule**: CSS variables `--font-mono: "ABC Diatype Semi Mono", ui-monospace, "SF Mono", Menlo, monospace`; rule `.label` (`font-size: 16px`, `line-height: 1.25`, `letter-spacing: -.16px`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `offpossible-com` (`OffPossible · Interfaces Between People and Their Own Minds`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.backdrop-grid> — `offpossible-com`)**:
   - DOM & Selectors: Landmark `<header class="backdrop-grid">` hosting `OffPossible · Interfaces Between Peo` navigation (`Noumen · Privacy · seenoumen.com`), DOM attributes (`data-shader-layer="fixed"`, `data-field-sound="muted"`, `data-agency-mode="steer"`, `data-content-mode="base"`), and stylesheet rule `body { background-color:000;width:100%;min-height:100vh;overflow-x:hidden }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.backdrop-grid> — `offpossible-com`)` (`offpossible-com`) adapts across `@media (width>=1000px) and (orientation:landscape),(width>=560px...`, `@media (prefers-reduced-motion:reduce)`, `@media (width<=768px)`, `@media (width>=769px)` with `cubic-bezier(.16,1,.3,1)` transitions and links `Noumen · Privacy · seenoumen.com`.
2. **Hero Stage & Focal Lead (<section.easter-prompt> — `We build and back interfaces betwe`)**:
   - DOM & Selectors: Landmark `<section class="easter-prompt">` presenting display lead `We build and back interfaces between people and t...` and copy excerpt *"M h a t w o u l d y o u b u i l d ?"* over `#000` canvas and `#fff` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#000` background with `#fff` headline `We build and back interfaces between people and t...`.
3. **Primary Showcase & Content Grid (<section.scroll-section> — `No one has direct sight of their o`)**:
   - DOM & Selectors: Landmark `<section class="scroll-section">` rendering section `No one has direct sight of their own mind.` with copy *"Privacy Policy Privacy"*, asset references (`clarity.js`, `z1sq4va9rn`, `sitemap.xml`, `llms.txt`), and grid rule `webkit-scrollbar { display:none }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.scroll-section> — `No one has direct sight of their o`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 36px`, `gap: 48px`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--edge-inset)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.scroll-section> — `We support builders who make peopl`)**:
   - DOM & Selectors: Landmark `<section class="scroll-section">` framing `We support builders who make people more legible...` and `We work early enough to change the question, not...` (*"Prompts and generated results may be privately retained and revie"*) with `#fff6` surface cards, `#0006` accents, and `html.no-js .sound-toggle { display:none }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.scroll-section> — `We support builders who make peopl`)` uses `50%` radii, `#0006` highlights, and assets (clarity.js, z1sq4va9rn, sitemap.xml).
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://offpossible.com/`)**:
   - DOM & Selectors: Landmark `<footer class="site-footer">` anchoring `OffPossible · Interfaces Between` footer links (`Noumen · Privacy · seenoumen.com`), copy *"Lenses gave people sight of cells and distant planets."*, and `#f4cae3` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.site-footer> — `https://offpossible.com/`)` aligns to `36px` extracted from `offpossible-com` stylesheet with `var(--edge-inset)` lateral canvas padding with `48px` grid gap and attributes (data-shader-layer="fixed", data-field-sound="muted", data-agency-mode="steer").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"M h a t w o u l d y o u b u i l d ?"*
- Copy Excerpt 2: *"Privacy Policy Privacy"*
- Copy Excerpt 3: *"Prompts and generated results may be privately retained and reviewed to operate, s..."*
- Copy Excerpt 4: *"Lenses gave people sight of cells and distant planets."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.16,1,.3,1)`
- **Extracted Stylesheet Rules (`offpossible-com`)**:
- `body { background-color:000;width:100%;min-height:100vh;overflow-x:hidden }`
- `webkit-scrollbar { display:none }`
- `html.no-js .sound-toggle { display:none }`
- `html.no-js .scroll-wrapper { width:100%;height:100vh }`
- `html.no-js .scroll-section { display:none }`
- **Per-Selector Transition Rules**:
- **Selector `t-flooding .backdrop-grid.backdro...`**: `transition: none` extracted from `offpossible-com` stylesheet.
- **Selector `html.prompt-closing .easter-prompt`**: `transition: .2s` extracted from `offpossible-com` stylesheet.
- **Selector `.site-symbol-orbit-shape`**: `transition: transform .42s cubic-bezier(.16,1,.3,1),opacity .24s,rx .42s c...` extracted from `offpossible-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.16,1,.3,1)`)**: Governs interactive state transitions across `<header.backdrop-grid>` and `<section.scroll-section>`.
- **Runtime Interaction Engine**: Integrates HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `offpossible-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
