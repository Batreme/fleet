---
title: "UI Prompt Blueprint: altamedfoundation-org"
date: 2026-11-15
target: "[[overview|altamedfoundation-org]]"
status: analyzed
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#fb2c36` canvas, `#f9fafb` ink, `#155dfc` accent)"
---

# UI Design System & Master Generation Blueprint: altamedfoundation-org

> **AltaMed Foundation · AltaMed Foundation** (https://altamedfoundation.org/) — AltaMed ensures everyone in our community has access to quality health care, enabling them to live healthy, happy lives.

![Desktop Viewport Capture (1440x4182)](file:///root/projects/fleet/wiki/targets/altamedfoundation-org/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **AltaMed Foundation · AltaMed Foundation** (`https://altamedfoundation.org/`). AltaMed ensures everyone in our community has access to quality health care, enabling them to live healthy, happy lives.
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#fb2c36` canvas, `#f9fafb` ink, `#155dfc` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fb2c36` (`var(--color-red-500)` in `:root`) paired with `#f9fafb` primary typography and `#155dfc` accents.
  - **Extracted Typographic Hierarchy**: Pairs `proxima-nova` for display copy (`H.E.L.P. Campaign`) with `gotham-xnarrow` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `40rem` container bounds (`gap: var(--spacing)`, padding `var(--spacing)`) with `cubic-bezier(0,0,.2,1)` easing.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/altamedfoundation-org/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×4182px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `40rem` extracted from `altamedfoundation-org` stylesheet.
- **Canvas Lateral Padding & Spacing**: `var(--spacing)` lateral canvas padding with `var(--spacing)` grid gap.
- **Border Radius Scale**: `.3125rem`, `.375rem`, `.25rem`, `4px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: var(--spacing)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--spacing)` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fb2c36` | `var(--color-red-500)` in `:root` |
| **Primary Typography Ink** | `#bf000f` | `var(--color-red-700)` in `:root` |
| **Elevated Surface / Card Substrate** | `#3080ff` | `var(--color-blue-500)` in `:root` |
| **Interactive Accent / Highlight** | `#155dfc` | `var(--color-blue-600)` in `:root` |
| **Secondary / Muted Copy** | `#f9fafb` | `var(--color-gray-50)` in `:root` |
| **Structural Hairline Border** | `#f3f4f6` | `var(--color-gray-100)` in `:root` |
| **Variable Token (`--color-gray-200`)** | `#e5e7eb` | `var(--color-gray-200)` in `:root` |
| **Variable Token (`--color-gray-300`)** | `#d1d5db` | `var(--color-gray-300)` in `:root` |
| **Variable Token (`--color-gray-400`)** | `#9ca3af` | `var(--color-gray-400)` in `:root` |
| **Variable Token (`--color-gray-500`)** | `#6b7280` | `var(--color-gray-500)` in `:root` |
| **Variable Token (`--color-gray-600`)** | `#5e5668` | `var(--color-gray-600)` in `:root` |
| **Variable Token (`--color-gray-700`)** | `#374151` | `var(--color-gray-700)` in `:root` |
| **Variable Token (`--color-gray-800`)** | `#1f2937` | `var(--color-gray-800)` in `:root` |
| **Variable Token (`--color-gray-900`)** | `#242029` | `var(--color-gray-900)` in `:root` |
| **Variable Token (`--color-black`)** | `#000` | `var(--color-black)` in `:root` |
| **Variable Token (`--color-white`)** | `#fff` | `var(--color-white)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-red-500` | `#fb2c36` | Brand / Palette Token |
| `--color-red-700` | `#bf000f` | Brand / Palette Token |
| `--color-blue-500` | `#3080ff` | Brand / Palette Token |
| `--color-blue-600` | `#155dfc` | Brand / Palette Token |
| `--color-gray-50` | `#f9fafb` | Brand / Palette Token |
| `--color-gray-100` | `#f3f4f6` | Brand / Palette Token |
| `--color-gray-200` | `#e5e7eb` | Brand / Palette Token |
| `--color-gray-300` | `#d1d5db` | Brand / Palette Token |
| `--color-gray-400` | `#9ca3af` | Brand / Palette Token |
| `--color-gray-500` | `#6b7280` | Brand / Palette Token |
| `--color-gray-600` | `#5e5668` | Brand / Palette Token |
| `--color-gray-700` | `#374151` | Brand / Palette Token |
| `--color-gray-800` | `#1f2937` | Brand / Palette Token |
| `--color-gray-900` | `#242029` | Brand / Palette Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `proxima-nova`.
- **Primary Body Stack**: `gotham-xnarrow`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`.
- **Section Heading (`H2`)**: CSS variables `--text-3xl: 1.875rem`, `--text-3xl--line-height: calc(2.25 / 1.875)`, `--text-title-lg: 34px`.
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`, `--font-size-body: 18px`.
- **Metadata & Navigation Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(.4,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: .15s` extracted from `altamedfoundation-org` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `altamedfoundation-org` stylesheet.
- **Selector `color\]`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `altamedfoundation-org` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<header.relative>` and `<section.scroll-mt-24>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<section.bg-white>` and `<section.scroll-mt-24>` interactive targets.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — AltaMed Foundation · AltaMed Foundation    │
│ ====================================================================== │
│ [ <header.relative>        | Overview · Index · Archive · About · C ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.bg-white>                                   |   │
│ | H1: H.E.L.P. Campaign                                            |   │
│ | Substrate: #fb2c36    | Ink: #f9fafb    | Accent: #155dfc        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.scroll-mt-24>    ) max-w: 40rem          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Impact Stories               |  | Homeward Bound: Preemie Twin | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: var(--) | │
│ | [<header.relative>] -> [<section.bg-white>] -> [<section.scroll-mt]  │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.bg-white>     ) | https://altamedfoundation.org/     │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.relative> — `altamedfoundation-org`)**:
   - Landmark `<header class="relative z-50">` hosting `AltaMed Foundation · AltaMed Foundat` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-scroll-behavior="smooth"`, `data-precedence="next"`, `data-href="/_next/static/immutab..."`, `data-nimg="1"`), and stylesheet rule `.tk-proxima-nova { font-family: "proxima-nova",sans-serif; }`.
2. **Hero Stage & Focal Lead (<section.bg-white> — `H.E.L.P. Campaign`)**:
   - Landmark `<section class="bg-white py-12">` presenting display lead `H.E.L.P. Campaign` and copy excerpt *"AltaMed ensures everyone in our community has access to quality h"* over `#fb2c36` canvas and `#f9fafb` ink.
3. **Primary Showcase & Content Grid (<section.scroll-mt-24> — `Impact Stories`)**:
   - Landmark `<section class="scroll-mt-24 bg-purple">` rendering section `Impact Stories` with copy *"Health. Equity. Life. Programs."*, asset references (`vdqo9h3n.api.sanity.io`, `altamed-foundation-logo.svg`, `3kc4s5-t1h7ps.js`, `1h6ujiewnnn1_.js`), and grid rule `.tk-gotham-xnarrow { font-family: "gotham-xnarrow",sans-serif; }`.
4. **Interactive Detail & Feature Matrix (<section.scroll-mt-24> — `Homeward Bound: Preemie Twins’ Inc`)**:
   - Landmark `<section class="scroll-mt-24 bg-white">` framing `Homeward Bound: Preemie Twins’ Incredible Journey...` and `Make a Difference` (*"Learn More about the H.E.L.P. Campaign"*) with `#3080ff` surface cards, `#155dfc` accents, and `.tk-gotham-narrow { font-family: "gotham-narrow",sans-serif; }`.
5. **Colophon & Global Directory Footer (<footer.bg-white> — `https://altamedfoundation.org/`)**:
   - Landmark `<footer class="bg-white pt-8">` anchoring `AltaMed Foundation · AltaMed Fou` footer links (`Overview · Index · Archive · About · Contact`), copy *"about the H.E.L.P. Campaign"*, and `#f3f4f6` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: altamedfoundation-org (AltaMed Foundation · AltaMed Foundation)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `altamedfoundation-org` (**AltaMed Foundation · AltaMed Foundation** — `https://altamedfoundation.org/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#fb2c36` canvas, `#f9fafb` ink, `#155dfc` accent).
- **Identity & Domain Context**: AltaMed ensures everyone in our community has access to quality health care, enabling them to live healthy, happy lives.
- **Primary Substrate**: `#fb2c36` (`var(--color-red-500)` in `:root`), **Primary Ink**: `#f9fafb`, **Accent / Highlight**: `#155dfc`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fb2c36` (`var(--color-red-500)` in `:root`) paired with `#f9fafb` primary typography and `#155dfc` accents.
  - **Extracted Typographic Hierarchy**: Pairs `proxima-nova` for display copy (`H.E.L.P. Campaign`) with `gotham-xnarrow` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `40rem` container bounds (`gap: var(--spacing)`, padding `var(--spacing)`) with `cubic-bezier(0,0,.2,1)` easing.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `altamedfoundation-org` in your global stylesheet:

:root {
  /* AltaMed Foundation · AltaMed Foundation (altamedfoundation-org) — Ground-Truth Extracted CSS Variables */
  --color-red-500: #fb2c36; /* Brand / Palette Token (altamedfoundation-org) */
  --color-red-700: #bf000f; /* Brand / Palette Token (altamedfoundation-org) */
  --color-blue-500: #3080ff; /* Brand / Palette Token (altamedfoundation-org) */
  --color-blue-600: #155dfc; /* Brand / Palette Token (altamedfoundation-org) */
  --color-gray-50: #f9fafb; /* Brand / Palette Token (altamedfoundation-org) */
  --color-gray-100: #f3f4f6; /* Brand / Palette Token (altamedfoundation-org) */
  --color-gray-200: #e5e7eb; /* Brand / Palette Token (altamedfoundation-org) */
  --color-gray-300: #d1d5db; /* Brand / Palette Token (altamedfoundation-org) */
  --color-gray-400: #9ca3af; /* Brand / Palette Token (altamedfoundation-org) */
  --color-gray-500: #6b7280; /* Brand / Palette Token (altamedfoundation-org) */
  --color-gray-600: #5e5668; /* Brand / Palette Token (altamedfoundation-org) */
  --color-gray-700: #374151; /* Brand / Palette Token (altamedfoundation-org) */
  --color-gray-800: #1f2937; /* Brand / Palette Token (altamedfoundation-org) */
  --color-gray-900: #242029; /* Brand / Palette Token (altamedfoundation-org) */
  --color-black: #000; /* Canvas / Surface Token (altamedfoundation-org) */
  --color-white: #fff; /* Canvas / Surface Token (altamedfoundation-org) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#fb2c36` — grounded in `var(--color-red-500)` in `:root`
- **Primary Typography Ink**: `#bf000f` — grounded in `var(--color-red-700)` in `:root`
- **Elevated Surface / Card Substrate**: `#3080ff` — grounded in `var(--color-blue-500)` in `:root`
- **Interactive Accent / Highlight**: `#155dfc` — grounded in `var(--color-blue-600)` in `:root`
- **Secondary / Muted Copy**: `#f9fafb` — grounded in `var(--color-gray-50)` in `:root`
- **Structural Hairline Border**: `#f3f4f6` — grounded in `var(--color-gray-100)` in `:root`
- **Variable Token (`--color-gray-200`)**: `#e5e7eb` — grounded in `var(--color-gray-200)` in `:root`
- **Variable Token (`--color-gray-300`)**: `#d1d5db` — grounded in `var(--color-gray-300)` in `:root`
- **Variable Token (`--color-gray-400`)**: `#9ca3af` — grounded in `var(--color-gray-400)` in `:root`
- **Variable Token (`--color-gray-500`)**: `#6b7280` — grounded in `var(--color-gray-500)` in `:root`
- **Variable Token (`--color-gray-600`)**: `#5e5668` — grounded in `var(--color-gray-600)` in `:root`
- **Variable Token (`--color-gray-700`)**: `#374151` — grounded in `var(--color-gray-700)` in `:root`
- **Variable Token (`--color-gray-800`)**: `#1f2937` — grounded in `var(--color-gray-800)` in `:root`
- **Variable Token (`--color-gray-900`)**: `#242029` — grounded in `var(--color-gray-900)` in `:root`
- **Variable Token (`--color-black`)**: `#000` — grounded in `var(--color-black)` in `:root`
- **Variable Token (`--color-white`)**: `#fff` — grounded in `var(--color-white)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×4182px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `40rem` extracted from `altamedfoundation-org` stylesheet
- **Padding & Gutters**: `var(--spacing)` lateral canvas padding with `var(--spacing)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: var(--spacing)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--spacing)` horizontal padding
- **Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)`
- **Corner Radii**: `.3125rem`, `.375rem`, `.25rem`, `4px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `proxima-nova`
- **Body Font Stack**: `gotham-xnarrow`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`
- **H2 Section Rule**: CSS variables `--text-3xl: 1.875rem`, `--text-3xl--line-height: calc(2.25 / 1.875)`, `--text-title-lg: 34px`
- **Body Copy Rule**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`, `--font-size-body: 18px`
- **Metadata & Index Rule**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `altamedfoundation-org` (`AltaMed Foundation · AltaMed Foundation`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.relative> — `altamedfoundation-org`)**:
   - DOM & Selectors: Landmark `<header class="relative z-50">` hosting `AltaMed Foundation · AltaMed Foundat` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-scroll-behavior="smooth"`, `data-precedence="next"`, `data-href="/_next/static/immutab..."`, `data-nimg="1"`), and stylesheet rule `.tk-proxima-nova { font-family: "proxima-nova",sans-serif; }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.relative> — `altamedfoundation-org`)` (`altamedfoundation-org`) adapts across `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)` with `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(.4,0,.2,1)` transitions and links `Overview · Index · Archive · About · Contact`.
2. **Hero Stage & Focal Lead (<section.bg-white> — `H.E.L.P. Campaign`)**:
   - DOM & Selectors: Landmark `<section class="bg-white py-12">` presenting display lead `H.E.L.P. Campaign` and copy excerpt *"AltaMed ensures everyone in our community has access to quality h"* over `#fb2c36` canvas and `#f9fafb` ink.
   - Responsive Contract: Hero stage (`1440×4182px` desktop / `390×2400px` mobile) sets `#fb2c36` background with `#f9fafb` headline `H.E.L.P. Campaign`.
3. **Primary Showcase & Content Grid (<section.scroll-mt-24> — `Impact Stories`)**:
   - DOM & Selectors: Landmark `<section class="scroll-mt-24 bg-purple">` rendering section `Impact Stories` with copy *"Health. Equity. Life. Programs."*, asset references (`vdqo9h3n.api.sanity.io`, `altamed-foundation-logo.svg`, `3kc4s5-t1h7ps.js`, `1h6ujiewnnn1_.js`), and grid rule `.tk-gotham-xnarrow { font-family: "gotham-xnarrow",sans-serif; }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.scroll-mt-24> — `Impact Stories`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: var(--spacing)`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--spacing)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.scroll-mt-24> — `Homeward Bound: Preemie Twins’ Inc`)**:
   - DOM & Selectors: Landmark `<section class="scroll-mt-24 bg-white">` framing `Homeward Bound: Preemie Twins’ Incredible Journey...` and `Make a Difference` (*"Learn More about the H.E.L.P. Campaign"*) with `#3080ff` surface cards, `#155dfc` accents, and `.tk-gotham-narrow { font-family: "gotham-narrow",sans-serif; }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.scroll-mt-24> — `Homeward Bound: Preemie Twins’ Inc`)` uses `.3125rem`, `.375rem`, `.25rem`, `4px` radii, `#155dfc` highlights, and assets (vdqo9h3n.api.sanity.io, altamed-foundation-logo.svg, 3kc4s5-t1h7ps.js).
5. **Colophon & Global Directory Footer (<footer.bg-white> — `https://altamedfoundation.org/`)**:
   - DOM & Selectors: Landmark `<footer class="bg-white pt-8">` anchoring `AltaMed Foundation · AltaMed Fou` footer links (`Overview · Index · Archive · About · Contact`), copy *"about the H.E.L.P. Campaign"*, and `#f3f4f6` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.bg-white> — `https://altamedfoundation.org/`)` aligns to `40rem` extracted from `altamedfoundation-org` stylesheet with `var(--spacing)` lateral canvas padding with `var(--spacing)` grid gap and attributes (data-scroll-behavior="smooth", data-precedence="next", data-href="/_next/static/immutab...").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"AltaMed ensures everyone in our community has access to quality health care, enabl..."*
- Copy Excerpt 2: *"Health. Equity. Life. Programs."*
- Copy Excerpt 3: *"Learn More about the H.E.L.P. Campaign"*
- Copy Excerpt 4: *"about the H.E.L.P. Campaign"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(.4,0,.2,1)`
- **Extracted Stylesheet Rules (`altamedfoundation-org`)**:
- `.tk-proxima-nova { font-family: "proxima-nova",sans-serif; }`
- `.tk-gotham-xnarrow { font-family: "gotham-xnarrow",sans-serif; }`
- `.tk-gotham-narrow { font-family: "gotham-narrow",sans-serif; }`
- `.tk-gotham-condensed { font-family: "gotham-condensed",sans-serif; }`
- `.tk-gotham { font-family: "gotham",sans-serif; }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: .15s` extracted from `altamedfoundation-org` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `altamedfoundation-org` stylesheet.
- **Selector `color\]`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `altamedfoundation-org` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<header.relative>` and `<section.scroll-mt-24>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<section.bg-white>` and `<section.scroll-mt-24>` interactive targets.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `altamedfoundation-org`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
