---
title: "UI Prompt Blueprint: www-xantium-com"
date: 2026-11-15
target: "[[overview|www-xantium-com]]"
status: analyzed
archetype: "Light-Substrate Editorial & Modular Grid System (`#fff` canvas, `#221f25` ink, `#084432` accent)"
---

# UI Design System & Master Generation Blueprint: www-xantium-com

> **Xantium** (https://www.xantium.com) — Xantium

![Desktop Viewport Capture (1440x6423)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Xantium** (`https://www.xantium.com`). Xantium
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#fff` canvas, `#221f25` ink, `#084432` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fff` (`var(--color-white)` in `:root`) paired with `#221f25` primary typography and `#084432` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Inter` for display copy (`We build technology enhanced by huma`) with `Inter Fallback` and `Space Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `40rem` container bounds (`gap: 25px`, padding `6px`) with `cubic-bezier(0,0,.2,1)` easing and Lottie Vector Animation Player.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×6423px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `40rem` extracted from `www-xantium-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `6px` lateral canvas padding with `25px` grid gap.
- **Border Radius Scale**: `4px`, `10px`, `3px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: 25px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `6px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--color-white)` in `:root` |
| **Primary Typography Ink** | `#221f25` | `var(--color-cache-black)` in `:root` |
| **Elevated Surface / Card Substrate** | `#f5f5f2` | `var(--color-circuit-ivory)` in `:root` |
| **Interactive Accent / Highlight** | `#084432` | `var(--color-neural-moss)` in `:root` |
| **Secondary / Muted Copy** | `#00bf8b` | `var(--color-mint-engine)` in `:root` |
| **Structural Hairline Border** | `#c9ff8b` | `var(--color-data-beam)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-inter` | `"Inter","Inter Fallback"` | Typography / Scale Token |
| `--font-space-mono` | `"Space Mono","Space Mono Fallback"` | Typography / Scale Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--container-sm` | `24rem` | Layout / Spatial Grid Token |
| `--container-lg` | `32rem` | Layout / Spatial Grid Token |
| `--container-2xl` | `42rem` | Layout / Spatial Grid Token |
| `--container-3xl` | `48rem` | Layout / Spatial Grid Token |
| `--container-4xl` | `56rem` | Layout / Spatial Grid Token |
| `--text-xs` | `.75rem` | Typography Ink Token |
| `--text-xs--line-height` | `calc(1/.75)` | Typography Ink Token |
| `--text-sm` | `.875rem` | Typography Ink Token |
| `--text-sm--line-height` | `calc(1.25/.875)` | Typography Ink Token |
| `--text-base` | `1rem` | Typography Ink Token |
| `--text-base--line-height` | `calc(1.5/1)` | Typography Ink Token |
| `--text-xl` | `1.25rem` | Typography Ink Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Inter`.
- **Primary Body Stack**: `Inter Fallback`.
- **Technical / Metadata Stack**: `Space Mono`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5/2.25)`, `--text-5xl: 3rem`.
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2/1.5)`, `--text-3xl: 1.875rem`.
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5/1)`, `--font-body: system-ui,sans-serif`.
- **Metadata & Navigation Labels**: CSS variables `--font-space-mono: "Space Mono","Space Mono Fallback"`, `--text-xs: .75rem`, `--text-xs--line-height: calc(1/.75)`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: .15s` extracted from `www-xantium-com` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `www-xantium-com` stylesheet.
- **Selector `.transition-all`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `www-xantium-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<header.pointer-events-none>` and `<section.py-16>`.
- **Runtime Interaction Engine**: Integrates Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Xantium                                    │
│ ====================================================================== │
│ [ <header.pointer-events-n | Home · How We Work · Our Culture · Our ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.py-16>                                      |   │
│ | H1: We build technology enhanced by human insight to...          |   │
│ | Substrate: #fff       | Ink: #221f25    | Accent: #084432        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.py-16>           ) max-w: 40rem          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | What We Do                   |  | At a Glance                  | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 25px  ) | │
│ | [<header.pointer-ev] -> [<section.py-16>] -> [<section.py-16>] |     │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.relative>     ) | https://www.xantium.com            │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.pointer-events-none> — `www-xantium-com`)**:
   - Landmark `<header class="pointer-events-none absolute">` hosting `Xantium` navigation (`Home · How We Work · Our Culture · Our Team · Careers`), DOM attributes (`data-precedence="next"`, `data-nimg="fill"`, `data-nimg="fill"`, `data-nimg="fill"`), and stylesheet rule `nter_fe8b9d92-module__LINzvG__cla... { font-family:Inter,Inter Fallback;font-style:normal }`.
2. **Hero Stage & Focal Lead (<section.py-16> — `We build technology enhanced by hu`)**:
   - Landmark `<section class="py-16 relative">` presenting display lead `We build technology enhanced by human insight to...` and copy excerpt *"At Xantium, quantitative researchers, developers, fundamental ana"* over `#fff` canvas and `#221f25` ink.
3. **Primary Showcase & Content Grid (<section.py-16> — `What We Do`)**:
   - Landmark `<section class="py-16 relative">` rendering section `What We Do` with copy *"We are a global multi-strategy investment firm integrating quanti"*, asset references (`28e60ca39c9ae554-s.p.7a4e9fcc.woff2`, `83afe278b6a6bb3c-s.p.3a6ba036.woff2`, `8d05cfa5faa8406c-s.p.4adea45d.woff2`, `d7a0600e467cf0bd-s.p.20ecb425.woff2`), and grid rule `inter_fe8b9d92-module__LINzvG__va... { --font-inter:"Inter","Inter Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.py-16> — `At a Glance`)**:
   - Landmark `<section class="py-16 relative">` framing `At a Glance` and `Founded in 2019 as part of Tudor Group` (*"If you're drawn to complex problems and collaborative discovery, "*) with `#f5f5f2` surface cards, `#084432` accents, and `mono_e13c1f09-module__VyLqqa__cla... { font-family:Space Mono,Space Mono Fallback;font-style:normal }`.
5. **Colophon & Global Directory Footer (<footer.relative> — `https://www.xantium.com`)**:
   - Landmark `<footer class="relative z-10">` anchoring `Xantium` footer links (`Home · How We Work · Our Culture · Our Team · Careers`), copy *"Global presence, market breadth, scale"*, and `#c9ff8b` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-xantium-com (Xantium)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-xantium-com` (**Xantium** — `https://www.xantium.com`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#fff` canvas, `#221f25` ink, `#084432` accent).
- **Identity & Domain Context**: Xantium
- **Primary Substrate**: `#fff` (`var(--color-white)` in `:root`), **Primary Ink**: `#221f25`, **Accent / Highlight**: `#084432`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fff` (`var(--color-white)` in `:root`) paired with `#221f25` primary typography and `#084432` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Inter` for display copy (`We build technology enhanced by huma`) with `Inter Fallback` and `Space Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `40rem` container bounds (`gap: 25px`, padding `6px`) with `cubic-bezier(0,0,.2,1)` easing and Lottie Vector Animation Player.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-xantium-com` in your global stylesheet:

:root {
  /* Xantium (www-xantium-com) — Ground-Truth Extracted CSS Variables */
  --font-inter: "Inter","Inter Fallback"; /* Typography / Scale Token (www-xantium-com) */
  --font-space-mono: "Space Mono","Space Mono Fallback"; /* Typography / Scale Token (www-xantium-com) */
  --color-white: #fff; /* Canvas / Surface Token (www-xantium-com) */
  --spacing: .25rem; /* Layout / Spatial Grid Token (www-xantium-com) */
  --container-sm: 24rem; /* Layout / Spatial Grid Token (www-xantium-com) */
  --container-lg: 32rem; /* Layout / Spatial Grid Token (www-xantium-com) */
  --container-2xl: 42rem; /* Layout / Spatial Grid Token (www-xantium-com) */
  --container-3xl: 48rem; /* Layout / Spatial Grid Token (www-xantium-com) */
  --container-4xl: 56rem; /* Layout / Spatial Grid Token (www-xantium-com) */
  --text-xs: .75rem; /* Typography Ink Token (www-xantium-com) */
  --text-xs--line-height: calc(1/.75); /* Typography Ink Token (www-xantium-com) */
  --text-sm: .875rem; /* Typography Ink Token (www-xantium-com) */
  --text-sm--line-height: calc(1.25/.875); /* Typography Ink Token (www-xantium-com) */
  --text-base: 1rem; /* Typography Ink Token (www-xantium-com) */
  --text-base--line-height: calc(1.5/1); /* Typography Ink Token (www-xantium-com) */
  --text-xl: 1.25rem; /* Typography Ink Token (www-xantium-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#fff` — grounded in `var(--color-white)` in `:root`
- **Primary Typography Ink**: `#221f25` — grounded in `var(--color-cache-black)` in `:root`
- **Elevated Surface / Card Substrate**: `#f5f5f2` — grounded in `var(--color-circuit-ivory)` in `:root`
- **Interactive Accent / Highlight**: `#084432` — grounded in `var(--color-neural-moss)` in `:root`
- **Secondary / Muted Copy**: `#00bf8b` — grounded in `var(--color-mint-engine)` in `:root`
- **Structural Hairline Border**: `#c9ff8b` — grounded in `var(--color-data-beam)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×6423px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `40rem` extracted from `www-xantium-com` stylesheet
- **Padding & Gutters**: `6px` lateral canvas padding with `25px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: 25px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `6px` horizontal padding
- **Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)`
- **Corner Radii**: `4px`, `10px`, `3px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `Inter Fallback`
- **Monospace / Technical Font Stack**: `Space Mono`
- **H1 Display Rule**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5/2.25)`, `--text-5xl: 3rem`
- **H2 Section Rule**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2/1.5)`, `--text-3xl: 1.875rem`
- **Body Copy Rule**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5/1)`, `--font-body: system-ui,sans-serif`
- **Metadata & Index Rule**: CSS variables `--font-space-mono: "Space Mono","Space Mono Fallback"`, `--text-xs: .75rem`, `--text-xs--line-height: calc(1/.75)`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-xantium-com` (`Xantium`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.pointer-events-none> — `www-xantium-com`)**:
   - DOM & Selectors: Landmark `<header class="pointer-events-none absolute">` hosting `Xantium` navigation (`Home · How We Work · Our Culture · Our Team · Careers`), DOM attributes (`data-precedence="next"`, `data-nimg="fill"`, `data-nimg="fill"`, `data-nimg="fill"`), and stylesheet rule `nter_fe8b9d92-module__LINzvG__cla... { font-family:Inter,Inter Fallback;font-style:normal }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.pointer-events-none> — `www-xantium-com`)` (`www-xantium-com`) adapts across `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)` with `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)` transitions and links `Home · How We Work · Our Culture · Our Team · Careers`.
2. **Hero Stage & Focal Lead (<section.py-16> — `We build technology enhanced by hu`)**:
   - DOM & Selectors: Landmark `<section class="py-16 relative">` presenting display lead `We build technology enhanced by human insight to...` and copy excerpt *"At Xantium, quantitative researchers, developers, fundamental ana"* over `#fff` canvas and `#221f25` ink.
   - Responsive Contract: Hero stage (`1440×6423px` desktop / `390×2400px` mobile) sets `#fff` background with `#221f25` headline `We build technology enhanced by human insight to...`.
3. **Primary Showcase & Content Grid (<section.py-16> — `What We Do`)**:
   - DOM & Selectors: Landmark `<section class="py-16 relative">` rendering section `What We Do` with copy *"We are a global multi-strategy investment firm integrating quanti"*, asset references (`28e60ca39c9ae554-s.p.7a4e9fcc.woff2`, `83afe278b6a6bb3c-s.p.3a6ba036.woff2`, `8d05cfa5faa8406c-s.p.4adea45d.woff2`, `d7a0600e467cf0bd-s.p.20ecb425.woff2`), and grid rule `inter_fe8b9d92-module__LINzvG__va... { --font-inter:"Inter","Inter Fallback" }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.py-16> — `What We Do`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: 25px`) on desktop and Single-column vertical stack at `390px` viewport width with `6px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.py-16> — `At a Glance`)**:
   - DOM & Selectors: Landmark `<section class="py-16 relative">` framing `At a Glance` and `Founded in 2019 as part of Tudor Group` (*"If you're drawn to complex problems and collaborative discovery, "*) with `#f5f5f2` surface cards, `#084432` accents, and `mono_e13c1f09-module__VyLqqa__cla... { font-family:Space Mono,Space Mono Fallback;font-style:normal }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.py-16> — `At a Glance`)` uses `4px`, `10px`, `3px` radii, `#084432` highlights, and assets (28e60ca39c9ae554-s.p.7a4e9fcc.woff2, 83afe278b6a6bb3c-s.p.3a6ba036.woff2, 8d05cfa5faa8406c-s.p.4adea45d.woff2).
5. **Colophon & Global Directory Footer (<footer.relative> — `https://www.xantium.com`)**:
   - DOM & Selectors: Landmark `<footer class="relative z-10">` anchoring `Xantium` footer links (`Home · How We Work · Our Culture · Our Team · Careers`), copy *"Global presence, market breadth, scale"*, and `#c9ff8b` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.relative> — `https://www.xantium.com`)` aligns to `40rem` extracted from `www-xantium-com` stylesheet with `6px` lateral canvas padding with `25px` grid gap and attributes (data-precedence="next", data-nimg="fill", data-nimg="fill").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"At Xantium, quantitative researchers, developers, fundamental analysts and traders..."*
- Copy Excerpt 2: *"We are a global multi-strategy investment firm integrating quantitative research w..."*
- Copy Excerpt 3: *"If you're drawn to complex problems and collaborative discovery, you'll find your..."*
- Copy Excerpt 4: *"Global presence, market breadth, scale"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`
- **Extracted Stylesheet Rules (`www-xantium-com`)**:
- `nter_fe8b9d92-module__LINzvG__cla... { font-family:Inter,Inter Fallback;font-style:normal }`
- `inter_fe8b9d92-module__LINzvG__va... { --font-inter:"Inter","Inter Fallback" }`
- `mono_e13c1f09-module__VyLqqa__cla... { font-family:Space Mono,Space Mono Fallback;font-style:normal }`
- `mono_e13c1f09-module__VyLqqa__var... { --font-space-mono:"Space Mono","Space Mono Fallback" }`
- `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: .15s` extracted from `www-xantium-com` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `www-xantium-com` stylesheet.
- **Selector `.transition-all`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `www-xantium-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<header.pointer-events-none>` and `<section.py-16>`.
- **Runtime Interaction Engine**: Integrates Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-xantium-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
