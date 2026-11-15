---
title: "UI Prompt Blueprint: dsquaredmedia-net"
date: 2026-11-15
target: "dsquaredmedia-net"
status: analyzed
capture: dom
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#16161a`)"
---

# UI Design System & Master Generation Blueprint: dsquaredmedia-net

> **South Florida Marketing Agency · Branding, Web & AI · Dsquared Media** (https://dsquaredmedia.net) — Dsquared Media is a boutique West Palm Beach marketing agency serving South Florida. Branding, web design, growth, and AI, built as one s...

![Desktop Viewport Capture](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **South Florida Marketing Agency · Branding, Web & AI · Dsquared Media** (`https://dsquaredmedia.net`). Dsquared Media is a boutique West Palm Beach marketing agency serving South Florida. Branding, web design, growth, and AI, built as one s...
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#16161a`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fff` (`var(--color-white)` in `:root`) paired with `#07090d` primary typography and `#16161a` accents.
  - **Extracted Typographic Hierarchy**: Pairs `jakarta` for display copy (`A South Florida marketing agency bui`) with `jakarta Fallback` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `40rem` container bounds (`gap: 1px`, padding `30px`) with `cubic-bezier(0,0,.2,1)` easing and Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×11984px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `40rem` extracted from `dsquaredmedia-net` stylesheet.
- **Canvas Lateral Padding & Spacing**: `30px` lateral canvas padding with `1px` grid gap.
- **Border Radius Scale**: `.25rem`, `4px`, `22px`, `7px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: 1px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `30px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--color-white)` in `:root` |
| **Primary Typography Ink** | `#07090d` | `var(--color-bg)` in `:root` |
| **Elevated Surface / Card Substrate** | `#111113` | `var(--color-surface)` in `:root` |
| **Interactive Accent / Highlight** | `#16161a` | `var(--color-surface-2)` in `:root` |
| **Secondary / Muted Copy** | `#0e0e13` | `var(--color-surface-raised)` in `:root` |
| **Structural Hairline Border** | `#0c0d12` | `var(--color-surface-card)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-sans` | `var(--font-jakarta),system-ui,sans-serif` | Typography / Scale Token |
| `--font-mono` | `var(--font-victor),ui-monospace,monospace` | Typography / Scale Token |
| `--color-amber-50` | `oklch(98.7% .022 95.277)` | Brand / Palette Token |
| `--color-gray-100` | `oklch(96.7% .003 264.542)` | Brand / Palette Token |
| `--color-gray-600` | `oklch(44.6% .03 256.802)` | Brand / Palette Token |
| `--color-gray-900` | `oklch(21% .034 264.665)` | Brand / Palette Token |
| `--color-zinc-200` | `oklch(92% .004 286.32)` | Brand / Palette Token |
| `--color-zinc-900` | `oklch(21% .006 285.885)` | Brand / Palette Token |
| `--color-zinc-950` | `oklch(14.1% .005 285.823)` | Brand / Palette Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--container-7xl` | `80rem` | Layout / Spatial Grid Token |
| `--text-base` | `1rem` | Typography Ink Token |
| `--text-base--line-height` | `calc(1.5 / 1)` | Typography Ink Token |
| `--text-4xl` | `2.25rem` | Typography Ink Token |
| `--text-4xl--line-height` | `calc(2.5 / 2.25)` | Typography Ink Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `jakarta`.
- **Primary Body Stack**: `jakarta Fallback`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`; rule `,h1` (`font-size: 62px`, `line-height: 1.05`, `letter-spacing: -.03em`, `font-weight: 600`).
- **Section Heading (`H2`)**: rule `,h2` (`font-size: clamp(32px,4vw,56px)`, `line-height: 1.04`, `letter-spacing: -.025em`, `font-weight: 500`).
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`; rule `p` (`font-size: 16px`, `line-height: 1.7`).
- **Metadata & Navigation Labels**: CSS variables `--font-mono: var(--font-victor),ui-monospace,monospace`, `--default-mono-font-family: var(--font-mono)`; rule `small` (`font-size: 14px`, `letter-spacing: 0`, `font-weight: 500`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.22,.8,.35,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: .15s` extracted from `dsquaredmedia-net` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `dsquaredmedia-net` stylesheet.
- **Selector `.ease-in-out`**: `transition: var(--ease-in-out)` extracted from `dsquaredmedia-net` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<header.cap-fw-head>` and `<section.statement>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — South Florida Marketing Agency · Branding, │
│ ====================================================================== │
│ [ <header.cap-fw-head>     | About · Services · Flex · The Hub · Wo ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hero>                                       |   │
│ | H1: A South Florida marketing agency built to shape y...         |   │
│ | Substrate: #fff       | Ink: #07090d    | Accent: #16161a        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.statement>       ) max-w: 40rem          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Branding, web, growth and AI |  | Graphic Design               | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 1px   ) | │
│ | [<header.cap-fw-hea] -> [<section.hero>] -> [<section.statement] |   │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.caf-footer>   ) | https://dsquaredmedia.net          │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.cap-fw-head> — `dsquaredmedia-net`)**:
   - Landmark `<header class="cap-fw-head">` hosting `South Florida Marketing Agency · Bra` navigation (`About · Services · Flex · The Hub · Work`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `before { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.hero> — `A South Florida marketing agency b`)**:
   - Landmark `<section class="hero hero-in">` presenting display lead `A South Florida marketing agency built to shape y...` and copy excerpt *"Consent Preferences"* over `#fff` canvas and `#07090d` ink.
3. **Primary Showcase & Content Grid (<section.statement> — `Branding, web, growth and AI, buil`)**:
   - Landmark `<section class="statement">` rendering section `Branding, web, growth and AI, built as one system.` with copy *"We live in a world shaped by perception."*, asset references (`636a5ac981f94f8b-s.p.woff2`, `8d2bb7cdfa09b0c5-s.p.woff2`, `ee62220d3ef0f600.css`, `182c5d4bd48e5167.css`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.cap-fw> — `Graphic Design`)**:
   - Landmark `<section class="cap-fw anim">` framing `Graphic Design` and `Web Design & Development` (*"A full-service marketing agency in West Palm Beach, working with "*) with `#111113` surface cards, `#16161a` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.caf-footer> — `https://dsquaredmedia.net`)**:
   - Landmark `<footer class="caf-footer">` anchoring `South Florida Marketing Agency ·` footer links (`About · Services · Flex · The Hub · Work`), copy *"5.0 across 100+ client reviews"*, and `#0c0d12` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: dsquaredmedia-net (South Florida Marketing Agency · Branding, Web & AI · Dsquared Media)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `dsquaredmedia-net` (**South Florida Marketing Agency · Branding, Web & AI · Dsquared Media** — `https://dsquaredmedia.net`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#16161a`).
- **Identity & Domain Context**: Dsquared Media is a boutique West Palm Beach marketing agency serving South Florida. Branding, web design, growth, and AI, built as one s...
- **Primary Substrate**: `#fff` (`var(--color-white)` in `:root`), **Primary Ink**: `#07090d`, **Accent / Highlight**: `#16161a`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fff` (`var(--color-white)` in `:root`) paired with `#07090d` primary typography and `#16161a` accents.
  - **Extracted Typographic Hierarchy**: Pairs `jakarta` for display copy (`A South Florida marketing agency bui`) with `jakarta Fallback` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `40rem` container bounds (`gap: 1px`, padding `30px`) with `cubic-bezier(0,0,.2,1)` easing and Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `dsquaredmedia-net` in your global stylesheet:

:root {
  /* South Florida Marketing Agency · Branding, Web & AI · Dsquared Media (dsquaredmedia-net) — Ground-Truth Extracted CSS Variables */
  --font-sans: var(--font-jakarta),system-ui,sans-serif; /* Typography / Scale Token (dsquaredmedia-net) */
  --font-mono: var(--font-victor),ui-monospace,monospace; /* Typography / Scale Token (dsquaredmedia-net) */
  --color-amber-50: oklch(98.7% .022 95.277); /* Brand / Palette Token (dsquaredmedia-net) */
  --color-gray-100: oklch(96.7% .003 264.542); /* Brand / Palette Token (dsquaredmedia-net) */
  --color-gray-600: oklch(44.6% .03 256.802); /* Brand / Palette Token (dsquaredmedia-net) */
  --color-gray-900: oklch(21% .034 264.665); /* Brand / Palette Token (dsquaredmedia-net) */
  --color-zinc-200: oklch(92% .004 286.32); /* Brand / Palette Token (dsquaredmedia-net) */
  --color-zinc-900: oklch(21% .006 285.885); /* Brand / Palette Token (dsquaredmedia-net) */
  --color-zinc-950: oklch(14.1% .005 285.823); /* Brand / Palette Token (dsquaredmedia-net) */
  --color-white: #fff; /* Canvas / Surface Token (dsquaredmedia-net) */
  --spacing: .25rem; /* Layout / Spatial Grid Token (dsquaredmedia-net) */
  --container-7xl: 80rem; /* Layout / Spatial Grid Token (dsquaredmedia-net) */
  --text-base: 1rem; /* Typography Ink Token (dsquaredmedia-net) */
  --text-base--line-height: calc(1.5 / 1); /* Typography Ink Token (dsquaredmedia-net) */
  --text-4xl: 2.25rem; /* Typography Ink Token (dsquaredmedia-net) */
  --text-4xl--line-height: calc(2.5 / 2.25); /* Typography Ink Token (dsquaredmedia-net) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#fff` — grounded in `var(--color-white)` in `:root`
- **Primary Typography Ink**: `#07090d` — grounded in `var(--color-bg)` in `:root`
- **Elevated Surface / Card Substrate**: `#111113` — grounded in `var(--color-surface)` in `:root`
- **Interactive Accent / Highlight**: `#16161a` — grounded in `var(--color-surface-2)` in `:root`
- **Secondary / Muted Copy**: `#0e0e13` — grounded in `var(--color-surface-raised)` in `:root`
- **Structural Hairline Border**: `#0c0d12` — grounded in `var(--color-surface-card)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×11984px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `40rem` extracted from `dsquaredmedia-net` stylesheet
- **Padding & Gutters**: `30px` lateral canvas padding with `1px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: 1px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `30px` horizontal padding
- **Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)`
- **Corner Radii**: `.25rem`, `4px`, `22px`, `7px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `jakarta`
- **Body Font Stack**: `jakarta Fallback`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`; rule `,h1` (`font-size: 62px`, `line-height: 1.05`, `letter-spacing: -.03em`, `font-weight: 600`)
- **H2 Section Rule**: rule `,h2` (`font-size: clamp(32px,4vw,56px)`, `line-height: 1.04`, `letter-spacing: -.025em`, `font-weight: 500`)
- **Body Copy Rule**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`; rule `p` (`font-size: 16px`, `line-height: 1.7`)
- **Metadata & Index Rule**: CSS variables `--font-mono: var(--font-victor),ui-monospace,monospace`, `--default-mono-font-family: var(--font-mono)`; rule `small` (`font-size: 14px`, `letter-spacing: 0`, `font-weight: 500`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `dsquaredmedia-net` (`South Florida Marketing Agency · Branding, Web & AI · Dsquared Media`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.cap-fw-head> — `dsquaredmedia-net`)**:
   - DOM & Selectors: Landmark `<header class="cap-fw-head">` hosting `South Florida Marketing Agency · Bra` navigation (`About · Services · Flex · The Hub · Work`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `before { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.cap-fw-head> — `dsquaredmedia-net`)` (`dsquaredmedia-net`) adapts across `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)` with `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.22,.8,.35,1)` transitions and links `About · Services · Flex · The Hub · Work`.
2. **Hero Stage & Focal Lead (<section.hero> — `A South Florida marketing agency b`)**:
   - DOM & Selectors: Landmark `<section class="hero hero-in">` presenting display lead `A South Florida marketing agency built to shape y...` and copy excerpt *"Consent Preferences"* over `#fff` canvas and `#07090d` ink.
   - Responsive Contract: Hero stage (`1440×11984px` desktop / `390×2400px` mobile) sets `#fff` background with `#07090d` headline `A South Florida marketing agency built to shape y...`.
3. **Primary Showcase & Content Grid (<section.statement> — `Branding, web, growth and AI, buil`)**:
   - DOM & Selectors: Landmark `<section class="statement">` rendering section `Branding, web, growth and AI, built as one system.` with copy *"We live in a world shaped by perception."*, asset references (`636a5ac981f94f8b-s.p.woff2`, `8d2bb7cdfa09b0c5-s.p.woff2`, `ee62220d3ef0f600.css`, `182c5d4bd48e5167.css`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.statement> — `Branding, web, growth and AI, buil`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: 1px`) on desktop and Single-column vertical stack at `390px` viewport width with `30px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.cap-fw> — `Graphic Design`)**:
   - DOM & Selectors: Landmark `<section class="cap-fw anim">` framing `Graphic Design` and `Web Design & Development` (*"A full-service marketing agency in West Palm Beach, working with "*) with `#111113` surface cards, `#16161a` accents, and `strong { font-weight:bolder }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.cap-fw> — `Graphic Design`)` uses `.25rem`, `4px`, `22px`, `7px` radii, `#16161a` highlights, and assets (636a5ac981f94f8b-s.p.woff2, 8d2bb7cdfa09b0c5-s.p.woff2, ee62220d3ef0f600.css).
5. **Colophon & Global Directory Footer (<footer.caf-footer> — `https://dsquaredmedia.net`)**:
   - DOM & Selectors: Landmark `<footer class="caf-footer">` anchoring `South Florida Marketing Agency ·` footer links (`About · Services · Flex · The Hub · Work`), copy *"5.0 across 100+ client reviews"*, and `#0c0d12` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.caf-footer> — `https://dsquaredmedia.net`)` aligns to `40rem` extracted from `dsquaredmedia-net` stylesheet with `30px` lateral canvas padding with `1px` grid gap and attributes (data-precedence="next", data-precedence="next", data-precedence="next").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Consent Preferences"*
- Copy Excerpt 2: *"We live in a world shaped by perception."*
- Copy Excerpt 3: *"A full-service marketing agency in West Palm Beach, working with South Florida bra..."*
- Copy Excerpt 4: *"5.0 across 100+ client reviews"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.22,.8,.35,1)`
- **Extracted Stylesheet Rules (`dsquaredmedia-net`)**:
- `before { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `strong { font-weight:bolder }`
- `small { font-size:80% }`
- `sup { vertical-align:baseline;font-size:75%;line-height:0;position:relative }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: .15s` extracted from `dsquaredmedia-net` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `dsquaredmedia-net` stylesheet.
- **Selector `.ease-in-out`**: `transition: var(--ease-in-out)` extracted from `dsquaredmedia-net` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<header.cap-fw-head>` and `<section.statement>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `dsquaredmedia-net`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
