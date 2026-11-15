---
title: "UI Prompt Blueprint: iroom-devinthehood-com"
date: 2026-11-15
target: "[[overview|iroom-devinthehood-com]]"
status: analyzed
archetype: "Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#14181f` ink, `#e3e6eb` accent)"
---

# UI Design System & Master Generation Blueprint: iroom-devinthehood-com

> **iRoom framework 3 · Get started** (https://iroom.devinthehood.com/) — iRoom, the flex CSS framework: a twelve columns grid, 30+ components, light and dark themes driven by CSS custom properties, parallax, a...

![Desktop Viewport Capture (1440x3944)](file:///root/projects/fleet/wiki/targets/iroom-devinthehood-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **iRoom framework 3 · Get started** (`https://iroom.devinthehood.com/`). iRoom, the flex CSS framework: a twelve columns grid, 30+ components, light and dark themes driven by CSS custom properties, parallax, a...
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#14181f` ink, `#e3e6eb` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#ffffff` (`var(--ir-bg)` in `:root`) paired with `#14181f` primary typography and `#e3e6eb` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Poppins` for display copy (`The flex one, in a flex world.`) with `Libre Barcode 128 Text` and `Libre Barcode 128 Text`.
  - **Calibrated Spatial Grid & Motion**: Combines `var(--ir-container)` container bounds (`gap: 1rem`, padding `1.375rem`) with `cubic-bezier(0.2,0.7,0.3,1)` easing.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/iroom-devinthehood-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×3944px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `var(--ir-container)` extracted from `iroom-devinthehood-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `1.375rem` lateral canvas padding with `1rem` grid gap.
- **Border Radius Scale**: `var(--ir-radius-sm)`, `var(--ir-radius)`, `50%`, `var(--ir-radius-full)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: var(--ir-container)`, `gap: 1rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `1.375rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (prefers-reduced-motion: reduce)`, `@media (prefers-reduced-motion: no-preference)`, `@media (min-width: 601px)`, `@media (min-width: 993px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | `var(--ir-bg)` in `:root` |
| **Primary Typography Ink** | `#f6f7f9` | `var(--ir-surface-2)` in `:root` |
| **Elevated Surface / Card Substrate** | `#eceef2` | `var(--ir-surface-3)` in `:root` |
| **Interactive Accent / Highlight** | `#e3e6eb` | `var(--ir-border)` in `:root` |
| **Secondary / Muted Copy** | `#cdd2da` | `var(--ir-border-strong)` in `:root` |
| **Structural Hairline Border** | `#14181f` | `var(--ir-text)` in `:root` |
| **Variable Token (`--ir-text-muted`)** | `#5d6675` | `var(--ir-text-muted)` in `:root` |
| **Variable Token (`--ir-text-subtle`)** | `#8b93a1` | `var(--ir-text-subtle)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ir-bg` | `#ffffff` | Canvas / Surface Token |
| `--ir-surface` | `#ffffff` | Canvas / Surface Token |
| `--ir-surface-2` | `#f6f7f9` | Canvas / Surface Token |
| `--ir-surface-3` | `#eceef2` | Canvas / Surface Token |
| `--ir-border` | `#e3e6eb` | Elevation / Border Token |
| `--ir-border-strong` | `#cdd2da` | Elevation / Border Token |
| `--ir-text` | `#14181f` | Typography Ink Token |
| `--ir-text-muted` | `#5d6675` | Typography Ink Token |
| `--ir-text-subtle` | `#8b93a1` | Typography Ink Token |
| `--ir-inverse-bg` | `#14181f` | Canvas / Surface Token |
| `--ir-inverse-fg` | `#f6f7f9` | Typography Ink Token |
| `--ir-overlay` | `rgba(10, 12, 16, 0.55)` | Color / Atmospheric Token |
| `--ir-shadow-sm` | `0 1px 2px rgba(16, 24, 40, 0.06), 0 1px 3px rgba(16, 24, 40, 0.08)` | Elevation / Border Token |
| `--ir-shadow-xl` | `0 28px 56px -14px rgba(16, 24, 40, 0.28)` | Elevation / Border Token |
| `--ir-soft-mix` | `11%` | Dimension / Scale Token |
| `--ir-border-mix` | `32%` | Elevation / Border Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Poppins`.
- **Primary Body Stack**: `Libre Barcode 128 Text`.
- **Technical / Metadata Stack**: `Libre Barcode 128 Text`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: rule `,.h1` (`font-size: clamp(2rem,1.55rem + 1.9vw,2....`, `letter-spacing: -0.02em`).
- **Section Heading (`H2`)**: rule `,.h2` (`font-size: clamp(1.5rem,1.3rem + .9vw,2rem)`, `letter-spacing: -0.015em`).
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `80%`, `75%`, `1em`, `1rem`, `100%`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `80%`, `75%`, `1em`, `1rem`, `100%`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.2,0.7,0.3,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `media(prefers-reduced-motion: red...`**: `transition: .01ms !important` extracted from `iroom-devinthehood-com` stylesheet.
- **Selector `textarea)`**: `transition: border-color var(--ir-duration) var(--ir-ease),box-shadow var(...` extracted from `iroom-devinthehood-com` stylesheet.
- **Selector `input[type=radio]`**: `transition: background-color var(--ir-duration) var(--ir-ease),border-colo...` extracted from `iroom-devinthehood-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.2,0.7,0.3,1)`)**: Governs interactive state transitions across `<header.navbar>` and `<section.demo-section>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<section.demo-hero>` and `<section.demo-section>` interactive targets.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — iRoom framework 3 · Get started            │
│ ====================================================================== │
│ [ <header.navbar>          | Get started · Components · CSS · JavaS ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.demo-hero>                                  |   │
│ | H1: The flex one, in a flex world.                               |   │
│ | Substrate: #ffffff    | Ink: #14181f    | Accent: #e3e6eb        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.demo-section>    ) max-w: var(--ir-conta |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Everything a page needs, not |  | A real flex grid             | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 1rem  ) | │
│ | [<header.navbar>] -> [<section.demo-hero] -> [<section.demo-sect] |  │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.demo-footer>  ) | https://iroom.devinthehood.com/    │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.navbar> — `iroom-devinthehood-com`)**:
   - Landmark `<header class="navbar navbar-sticky">` hosting `iRoom framework 3 · Get started` navigation (`Get started · Components · CSS · JavaScript · Download`), DOM attributes (`data-theme="auto"`, `data-theme-toggle`, `data-tooltip="Dark theme"`, `data-tooltip-position="bottom"`), and stylesheet rule `after { box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<section.demo-hero> — `The flex one, in a flex world.`)**:
   - Landmark `<section class="demo-hero parallax">` presenting display lead `The flex one, in a flex world.` and copy excerpt *"A CSS framework built on flexbox, cascade layers and custom prope"* over `#ffffff` canvas and `#14181f` ink.
3. **Primary Showcase & Content Grid (<section.demo-section> — `Everything a page needs, nothing i`)**:
   - Landmark `<section class="demo-section">` rendering section `Everything a page needs, nothing it does not` with copy *"Classes that read like what they do, a grid that bends to every s"*, asset references (`iroom.ico`, `favicon.png`, `iroom.min.css`, `demo.css`), and grid rule `html { -webkit-text-size-adjust:100%;text-size-adjust:100%;-webkit-tap-highligh... }`.
4. **Interactive Detail & Feature Matrix (<section.demo-section> — `A real flex grid`)**:
   - Landmark `<section class="demo-section bg-subtle">` framing `A real flex grid` and `Cascade layers` (*"Twelve columns, four sizes, true gaps instead of negative margins"*) with `#eceef2` surface cards, `#e3e6eb` accents, and `body { margin:0;min-height:100vh;min-height:100dvh }`.
5. **Colophon & Global Directory Footer (<footer.demo-footer> — `https://iroom.devinthehood.com/`)**:
   - Landmark `<footer class="demo-footer">` anchoring `iRoom framework 3 · Get started` footer links (`Get started · Components · CSS · JavaScript · Download`), copy *"Reset, tokens, base, layout, components, utilities: an utili"*, and `#14181f` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: iroom-devinthehood-com (iRoom framework 3 · Get started)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `iroom-devinthehood-com` (**iRoom framework 3 · Get started** — `https://iroom.devinthehood.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#14181f` ink, `#e3e6eb` accent).
- **Identity & Domain Context**: iRoom, the flex CSS framework: a twelve columns grid, 30+ components, light and dark themes driven by CSS custom properties, parallax, a...
- **Primary Substrate**: `#ffffff` (`var(--ir-bg)` in `:root`), **Primary Ink**: `#14181f`, **Accent / Highlight**: `#e3e6eb`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#ffffff` (`var(--ir-bg)` in `:root`) paired with `#14181f` primary typography and `#e3e6eb` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Poppins` for display copy (`The flex one, in a flex world.`) with `Libre Barcode 128 Text` and `Libre Barcode 128 Text`.
  - **Calibrated Spatial Grid & Motion**: Combines `var(--ir-container)` container bounds (`gap: 1rem`, padding `1.375rem`) with `cubic-bezier(0.2,0.7,0.3,1)` easing.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `iroom-devinthehood-com` in your global stylesheet:

:root {
  /* iRoom framework 3 · Get started (iroom-devinthehood-com) — Ground-Truth Extracted CSS Variables */
  --ir-bg: #ffffff; /* Canvas / Surface Token (iroom-devinthehood-com) */
  --ir-surface: #ffffff; /* Canvas / Surface Token (iroom-devinthehood-com) */
  --ir-surface-2: #f6f7f9; /* Canvas / Surface Token (iroom-devinthehood-com) */
  --ir-surface-3: #eceef2; /* Canvas / Surface Token (iroom-devinthehood-com) */
  --ir-border: #e3e6eb; /* Elevation / Border Token (iroom-devinthehood-com) */
  --ir-border-strong: #cdd2da; /* Elevation / Border Token (iroom-devinthehood-com) */
  --ir-text: #14181f; /* Typography Ink Token (iroom-devinthehood-com) */
  --ir-text-muted: #5d6675; /* Typography Ink Token (iroom-devinthehood-com) */
  --ir-text-subtle: #8b93a1; /* Typography Ink Token (iroom-devinthehood-com) */
  --ir-inverse-bg: #14181f; /* Canvas / Surface Token (iroom-devinthehood-com) */
  --ir-inverse-fg: #f6f7f9; /* Typography Ink Token (iroom-devinthehood-com) */
  --ir-overlay: rgba(10, 12, 16, 0.55); /* Color / Atmospheric Token (iroom-devinthehood-com) */
  --ir-shadow-sm: 0 1px 2px rgba(16, 24, 40, 0.06), 0 1px 3px rgba(16, 24, 40, 0.08); /* Elevation / Border Token (iroom-devinthehood-com) */
  --ir-shadow-xl: 0 28px 56px -14px rgba(16, 24, 40, 0.28); /* Elevation / Border Token (iroom-devinthehood-com) */
  --ir-soft-mix: 11%; /* Dimension / Scale Token (iroom-devinthehood-com) */
  --ir-border-mix: 32%; /* Elevation / Border Token (iroom-devinthehood-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ffffff` — grounded in `var(--ir-bg)` in `:root`
- **Primary Typography Ink**: `#f6f7f9` — grounded in `var(--ir-surface-2)` in `:root`
- **Elevated Surface / Card Substrate**: `#eceef2` — grounded in `var(--ir-surface-3)` in `:root`
- **Interactive Accent / Highlight**: `#e3e6eb` — grounded in `var(--ir-border)` in `:root`
- **Secondary / Muted Copy**: `#cdd2da` — grounded in `var(--ir-border-strong)` in `:root`
- **Structural Hairline Border**: `#14181f` — grounded in `var(--ir-text)` in `:root`
- **Variable Token (`--ir-text-muted`)**: `#5d6675` — grounded in `var(--ir-text-muted)` in `:root`
- **Variable Token (`--ir-text-subtle`)**: `#8b93a1` — grounded in `var(--ir-text-subtle)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×3944px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `var(--ir-container)` extracted from `iroom-devinthehood-com` stylesheet
- **Padding & Gutters**: `1.375rem` lateral canvas padding with `1rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: var(--ir-container)`, `gap: 1rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `1.375rem` horizontal padding
- **Media Queries**: `@media (prefers-reduced-motion: reduce)`, `@media (prefers-reduced-motion: no-preference)`, `@media (min-width: 601px)`, `@media (min-width: 993px)`
- **Corner Radii**: `var(--ir-radius-sm)`, `var(--ir-radius)`, `50%`, `var(--ir-radius-full)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Poppins`
- **Body Font Stack**: `Libre Barcode 128 Text`
- **Monospace / Technical Font Stack**: `Libre Barcode 128 Text`
- **H1 Display Rule**: rule `,.h1` (`font-size: clamp(2rem,1.55rem + 1.9vw,2....`, `letter-spacing: -0.02em`)
- **H2 Section Rule**: rule `,.h2` (`font-size: clamp(1.5rem,1.3rem + .9vw,2rem)`, `letter-spacing: -0.015em`)
- **Body Copy Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `80%`, `75%`, `1em`, `1rem`, `100%`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `80%`, `75%`, `1em`, `1rem`, `100%`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `iroom-devinthehood-com` (`iRoom framework 3 · Get started`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.navbar> — `iroom-devinthehood-com`)**:
   - DOM & Selectors: Landmark `<header class="navbar navbar-sticky">` hosting `iRoom framework 3 · Get started` navigation (`Get started · Components · CSS · JavaScript · Download`), DOM attributes (`data-theme="auto"`, `data-theme-toggle`, `data-tooltip="Dark theme"`, `data-tooltip-position="bottom"`), and stylesheet rule `after { box-sizing:border-box }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.navbar> — `iroom-devinthehood-com`)` (`iroom-devinthehood-com`) adapts across `@media (prefers-reduced-motion: reduce)`, `@media (prefers-reduced-motion: no-preference)`, `@media (min-width: 601px)`, `@media (min-width: 993px)` with `cubic-bezier(0.2,0.7,0.3,1)` transitions and links `Get started · Components · CSS · JavaScript · Download`.
2. **Hero Stage & Focal Lead (<section.demo-hero> — `The flex one, in a flex world.`)**:
   - DOM & Selectors: Landmark `<section class="demo-hero parallax">` presenting display lead `The flex one, in a flex world.` and copy excerpt *"A CSS framework built on flexbox, cascade layers and custom prope"* over `#ffffff` canvas and `#14181f` ink.
   - Responsive Contract: Hero stage (`1440×3944px` desktop / `390×2400px` mobile) sets `#ffffff` background with `#14181f` headline `The flex one, in a flex world.`.
3. **Primary Showcase & Content Grid (<section.demo-section> — `Everything a page needs, nothing i`)**:
   - DOM & Selectors: Landmark `<section class="demo-section">` rendering section `Everything a page needs, nothing it does not` with copy *"Classes that read like what they do, a grid that bends to every s"*, asset references (`iroom.ico`, `favicon.png`, `iroom.min.css`, `demo.css`), and grid rule `html { -webkit-text-size-adjust:100%;text-size-adjust:100%;-webkit-tap-highligh... }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.demo-section> — `Everything a page needs, nothing i`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: var(--ir-container)`, `gap: 1rem`) on desktop and Single-column vertical stack at `390px` viewport width with `1.375rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.demo-section> — `A real flex grid`)**:
   - DOM & Selectors: Landmark `<section class="demo-section bg-subtle">` framing `A real flex grid` and `Cascade layers` (*"Twelve columns, four sizes, true gaps instead of negative margins"*) with `#eceef2` surface cards, `#e3e6eb` accents, and `body { margin:0;min-height:100vh;min-height:100dvh }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.demo-section> — `A real flex grid`)` uses `var(--ir-radius-sm)`, `var(--ir-radius)`, `50%`, `var(--ir-radius-full)` radii, `#e3e6eb` highlights, and assets (iroom.ico, favicon.png, iroom.min.css).
5. **Colophon & Global Directory Footer (<footer.demo-footer> — `https://iroom.devinthehood.com/`)**:
   - DOM & Selectors: Landmark `<footer class="demo-footer">` anchoring `iRoom framework 3 · Get started` footer links (`Get started · Components · CSS · JavaScript · Download`), copy *"Reset, tokens, base, layout, components, utilities: an utili"*, and `#14181f` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.demo-footer> — `https://iroom.devinthehood.com/`)` aligns to `var(--ir-container)` extracted from `iroom-devinthehood-com` stylesheet with `1.375rem` lateral canvas padding with `1rem` grid gap and attributes (data-theme="auto", data-theme-toggle, data-tooltip="Dark theme").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"A CSS framework built on flexbox, cascade layers and custom properties: a twelve c..."*
- Copy Excerpt 2: *"Classes that read like what they do, a grid that bends to every screen and compone..."*
- Copy Excerpt 3: *"Twelve columns, four sizes, true gaps instead of negative margins, offsets, order..."*
- Copy Excerpt 4: *"Reset, tokens, base, layout, components, utilities: an utility always wins, and yo..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.2,0.7,0.3,1)`
- **Extracted Stylesheet Rules (`iroom-devinthehood-com`)**:
- `after { box-sizing:border-box }`
- `html { -webkit-text-size-adjust:100%;text-size-adjust:100%;-webkit-tap-highligh... }`
- `body { margin:0;min-height:100vh;min-height:100dvh }`
- `blockquote { overflow-wrap:break-word }`
- `strong { font-weight:bolder }`
- **Per-Selector Transition Rules**:
- **Selector `media(prefers-reduced-motion: red...`**: `transition: .01ms !important` extracted from `iroom-devinthehood-com` stylesheet.
- **Selector `textarea)`**: `transition: border-color var(--ir-duration) var(--ir-ease),box-shadow var(...` extracted from `iroom-devinthehood-com` stylesheet.
- **Selector `input[type=radio]`**: `transition: background-color var(--ir-duration) var(--ir-ease),border-colo...` extracted from `iroom-devinthehood-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.2,0.7,0.3,1)`)**: Governs interactive state transitions across `<header.navbar>` and `<section.demo-section>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<section.demo-hero>` and `<section.demo-section>` interactive targets.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `iroom-devinthehood-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
