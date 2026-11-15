---
title: "UI Prompt Blueprint: www-baseline-agency"
date: 2026-11-15
target: "[[overview|www-baseline-agency]]"
status: analyzed
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#fff3`)"
---

# UI Design System & Master Generation Blueprint: www-baseline-agency

> **Baseline · Brand identity systems, designed and built** (https://www.baseline.agency/) — Brand identity studio in Cluj-Napoca led by Victor Deaconu. Positioning, identity, rules and guidelines in 3 to 4 weeks, for brands that...

![Desktop Viewport Capture (1440x17185)](file:///root/projects/fleet/wiki/targets/www-baseline-agency/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Baseline · Brand identity systems, designed and built** (`https://www.baseline.agency/`). Brand identity studio in Cluj-Napoca led by Victor Deaconu. Positioning, identity, rules and guidelines in 3 to 4 weeks, for brands that...
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#fff3`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--color-black)` in `:root`) paired with `#fff` primary typography and `#fff3` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Inter` for display copy (`You got here with your brand working`) with `Inter Fallback` and `IBM Plex Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `40rem` container bounds (`gap: .5rem`, padding `.375rem`) with `cubic-bezier(.22,1,.36,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/www-baseline-agency/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×17185px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `40rem` extracted from `www-baseline-agency` stylesheet.
- **Canvas Lateral Padding & Spacing**: `.375rem` lateral canvas padding with `.5rem` grid gap.
- **Border Radius Scale**: `.25rem`, `.35625rem`, `.375rem`, `.9375rem`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: .5rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `.375rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#e0e0e0` | `.UwedmG_neutral .UwedmG_layerBase { background: #e0e0e0 }` |
| **Interactive Accent / Highlight** | `#fff3` | `.UwedmG_ghost .UwedmG_layerBase { background: #fff3 }` |
| **Secondary / Muted Copy** | `#0000` | `textarea { background-color: #0000 }` |
| **Structural Hairline Border** | `#000000` | `.border-black { border-color: black }` (`#000000`) |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ink-light` | `0` | Canvas / Surface Token |
| `--font-inter` | `"Inter", "Inter Fallback"` | Typography / Scale Token |
| `--font-inter-tight` | `"Inter Tight", "Inter Tight Fallback"` | Typography / Scale Token |
| `--font-hedvig` | `"Hedvig Letters Serif", "Hedvig Letters Serif Fallback"` | Typography / Scale Token |
| `--font-averia` | `"Averia Serif Libre", "Averia Serif Libre Fallback"` | Typography / Scale Token |
| `--font-geist` | `"Geist", "Geist Fallback"` | Typography / Scale Token |
| `--col-r` | `44.5` | Layout / Spatial Grid Token |
| `--row-t` | `61` | Design System Custom Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--font-weight-light` | `300` | Canvas / Surface Token |
| `--font-weight-normal` | `400` | Typography / Scale Token |
| `--font-weight-medium` | `500` | Typography / Scale Token |
| `--font-weight-semibold` | `600` | Typography / Scale Token |
| `--font-weight-bold` | `700` | Typography / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Inter`.
- **Primary Body Stack**: `Inter Fallback`.
- **Technical / Metadata Stack**: `IBM Plex Mono`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--t-display: clamp(calc(34*1px),calc(30.1*1px) + 1.04vw,calc(48.07*1px))`.
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `.875rem`, `.75063rem`, `1.11113rem`, `1em`, `80%`).
- **Body Copy**: CSS variables `--t-body: clamp(calc(16*1px),calc(15.45*1px) + .148vw,calc(18*1px))`.
- **Metadata & Navigation Labels**: CSS variables `--default-mono-font-family: var(--font-mono)`, `--t-label: calc(14*1px)`, `--about-small: clamp(calc(11 * 1px), .88vw, calc(24 * 1px))`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(.19,1,.22,1)`, `cubic-bezier(.6,0,.3,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.LW-vgW_cta`**: `transition: opacity .3s,visibility 0s linear .3s` extracted from `www-baseline-agency` stylesheet.
- **Selector `.LW-vgW_stage[data-shown=true] .L...`**: `transition: none` extracted from `www-baseline-agency` stylesheet.
- **Selector `.LW-vgW_dim`**: `transition: opacity 0s linear .3s` extracted from `www-baseline-agency` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.22,1,.36,1)`)**: Governs interactive state transitions across `<header.lenis>` and `<section.relative>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Baseline · Brand identity systems, designe │
│ ====================================================================== │
│ [ <header.lenis>           | About > A b o u t                      ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hero-drift>                                 |   │
│ | H1: You got here with your brand working against you....         |   │
│ | Substrate: #000       | Ink: #fff       | Accent: #fff3          |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.relative>        ) max-w: 40rem          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Clients who’ve raised $100M+ |  | We rebuild the baseline.     | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: .5rem ) | │
│ | [<header.lenis>] -> [<section.hero-drif] -> [<section.relative>] |   │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.relative>     ) | https://www.baseline.agency/       │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.lenis> — `www-baseline-agency`)**:
   - Landmark `<header class="lenis">` hosting `Baseline · Brand identity systems, d` navigation (`About > A b o u t`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-sdkn="@vercel/analytics/next"`), and stylesheet rule `.LW-vgW_cta { opacity:0;visibility:hidden;transition:opacity .3s,visibility 0s linear .3s }`.
2. **Hero Stage & Focal Lead (<section.hero-drift> — `You got here with your brand worki`)**:
   - Landmark `<section class="hero-drift relative">` presenting display lead `You got here with your brand working against you....` and copy excerpt *"Baseline B a s e l i n e Studio S t u d i o"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.relative> — `Clients who’ve raised $100M+ betwe`)**:
   - Landmark `<section class="relative text-white">` rendering section `Clients who’ve raised $100M+ between them` with copy *"Baseline B a s e l i n e"*, asset references (`387c923d20582ec7-s.p.2m62wczl7f17...`, `83afe278b6a6bb3c-s.p.45535valc9rz...`, `9873593f5e895d3f-s.p.1q5z3qm5aeja...`, `a69a711ce91a20c2-s.p.288yeszdmy1l...`), and grid rule `.LW-vgW_dim { opacity:0;transition:opacity 0s linear .3s }`.
4. **Interactive Detail & Feature Matrix (<article.flex> — `We rebuild the baseline.`)**:
   - Landmark `<article class="flex flex-col">` framing `We rebuild the baseline.` and `v21 Studio` (*"Studio S t u d i o"*) with `#e0e0e0` surface cards, `#fff3` accents, and `.LW-vgW_line { margin:0 -.1em -.14em;padding:0 .1em .14em;display:block;overflow:hidden }`.
5. **Colophon & Global Directory Footer (<footer.relative> — `https://www.baseline.agency/`)**:
   - Landmark `<footer class="relative w-full">` anchoring `Baseline · Brand identity system` footer links (`About > A b o u t`), copy *"Services > S e r v i c e s"*, and `#000000` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-baseline-agency (Baseline · Brand identity systems, designed and built)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-baseline-agency` (**Baseline · Brand identity systems, designed and built** — `https://www.baseline.agency/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#fff3`).
- **Identity & Domain Context**: Brand identity studio in Cluj-Napoca led by Victor Deaconu. Positioning, identity, rules and guidelines in 3 to 4 weeks, for brands that...
- **Primary Substrate**: `#000` (`var(--color-black)` in `:root`), **Primary Ink**: `#fff`, **Accent / Highlight**: `#fff3`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--color-black)` in `:root`) paired with `#fff` primary typography and `#fff3` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Inter` for display copy (`You got here with your brand working`) with `Inter Fallback` and `IBM Plex Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `40rem` container bounds (`gap: .5rem`, padding `.375rem`) with `cubic-bezier(.22,1,.36,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-baseline-agency` in your global stylesheet:

:root {
  /* Baseline · Brand identity systems, designed and built (www-baseline-agency) — Ground-Truth Extracted CSS Variables */
  --ink-light: 0; /* Canvas / Surface Token (www-baseline-agency) */
  --font-inter: "Inter", "Inter Fallback"; /* Typography / Scale Token (www-baseline-agency) */
  --font-inter-tight: "Inter Tight", "Inter Tight Fallback"; /* Typography / Scale Token (www-baseline-agency) */
  --font-hedvig: "Hedvig Letters Serif", "Hedvig Letters Serif Fallback"; /* Typography / Scale Token (www-baseline-agency) */
  --font-averia: "Averia Serif Libre", "Averia Serif Libre Fallback"; /* Typography / Scale Token (www-baseline-agency) */
  --font-geist: "Geist", "Geist Fallback"; /* Typography / Scale Token (www-baseline-agency) */
  --col-r: 44.5; /* Layout / Spatial Grid Token (www-baseline-agency) */
  --row-t: 61; /* Design System Custom Token (www-baseline-agency) */
  --color-black: #000; /* Canvas / Surface Token (www-baseline-agency) */
  --color-white: #fff; /* Canvas / Surface Token (www-baseline-agency) */
  --spacing: .25rem; /* Layout / Spatial Grid Token (www-baseline-agency) */
  --font-weight-light: 300; /* Canvas / Surface Token (www-baseline-agency) */
  --font-weight-normal: 400; /* Typography / Scale Token (www-baseline-agency) */
  --font-weight-medium: 500; /* Typography / Scale Token (www-baseline-agency) */
  --font-weight-semibold: 600; /* Typography / Scale Token (www-baseline-agency) */
  --font-weight-bold: 700; /* Typography / Scale Token (www-baseline-agency) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#000` — grounded in `var(--color-black)` in `:root`
- **Primary Typography Ink**: `#fff` — grounded in `var(--color-white)` in `:root`
- **Elevated Surface / Card Substrate**: `#e0e0e0` — grounded in `.UwedmG_neutral .UwedmG_layerBase { background: #e0e0e0 }`
- **Interactive Accent / Highlight**: `#fff3` — grounded in `.UwedmG_ghost .UwedmG_layerBase { background: #fff3 }`
- **Secondary / Muted Copy**: `#0000` — grounded in `textarea { background-color: #0000 }`
- **Structural Hairline Border**: `#000000` — grounded in `.border-black { border-color: black }` (`#000000`)

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×17185px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `40rem` extracted from `www-baseline-agency` stylesheet
- **Padding & Gutters**: `.375rem` lateral canvas padding with `.5rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: .5rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `.375rem` horizontal padding
- **Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`
- **Corner Radii**: `.25rem`, `.35625rem`, `.375rem`, `.9375rem`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `Inter Fallback`
- **Monospace / Technical Font Stack**: `IBM Plex Mono`
- **H1 Display Rule**: CSS variables `--t-display: clamp(calc(34*1px),calc(30.1*1px) + 1.04vw,calc(48.07*1px))`
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `.875rem`, `.75063rem`, `1.11113rem`, `1em`, `80%`)
- **Body Copy Rule**: CSS variables `--t-body: clamp(calc(16*1px),calc(15.45*1px) + .148vw,calc(18*1px))`
- **Metadata & Index Rule**: CSS variables `--default-mono-font-family: var(--font-mono)`, `--t-label: calc(14*1px)`, `--about-small: clamp(calc(11 * 1px), .88vw, calc(24 * 1px))`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-baseline-agency` (`Baseline · Brand identity systems, designed and built`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.lenis> — `www-baseline-agency`)**:
   - DOM & Selectors: Landmark `<header class="lenis">` hosting `Baseline · Brand identity systems, d` navigation (`About > A b o u t`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-sdkn="@vercel/analytics/next"`), and stylesheet rule `.LW-vgW_cta { opacity:0;visibility:hidden;transition:opacity .3s,visibility 0s linear .3s }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.lenis> — `www-baseline-agency`)` (`www-baseline-agency`) adapts across `@media (prefers-reduced-motion:reduce)`, `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)` with `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(.19,1,.22,1)`, `cubic-bezier(.6,0,.3,1)` transitions and links `About > A b o u t`.
2. **Hero Stage & Focal Lead (<section.hero-drift> — `You got here with your brand worki`)**:
   - DOM & Selectors: Landmark `<section class="hero-drift relative">` presenting display lead `You got here with your brand working against you....` and copy excerpt *"Baseline B a s e l i n e Studio S t u d i o"* over `#000` canvas and `#fff` ink.
   - Responsive Contract: Hero stage (`1440×17185px` desktop / `390×2400px` mobile) sets `#000` background with `#fff` headline `You got here with your brand working against you....`.
3. **Primary Showcase & Content Grid (<section.relative> — `Clients who’ve raised $100M+ betwe`)**:
   - DOM & Selectors: Landmark `<section class="relative text-white">` rendering section `Clients who’ve raised $100M+ between them` with copy *"Baseline B a s e l i n e"*, asset references (`387c923d20582ec7-s.p.2m62wczl7f17...`, `83afe278b6a6bb3c-s.p.45535valc9rz...`, `9873593f5e895d3f-s.p.1q5z3qm5aeja...`, `a69a711ce91a20c2-s.p.288yeszdmy1l...`), and grid rule `.LW-vgW_dim { opacity:0;transition:opacity 0s linear .3s }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.relative> — `Clients who’ve raised $100M+ betwe`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: .5rem`) on desktop and Single-column vertical stack at `390px` viewport width with `.375rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<article.flex> — `We rebuild the baseline.`)**:
   - DOM & Selectors: Landmark `<article class="flex flex-col">` framing `We rebuild the baseline.` and `v21 Studio` (*"Studio S t u d i o"*) with `#e0e0e0` surface cards, `#fff3` accents, and `.LW-vgW_line { margin:0 -.1em -.14em;padding:0 .1em .14em;display:block;overflow:hidden }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<article.flex> — `We rebuild the baseline.`)` uses `.25rem`, `.35625rem`, `.375rem`, `.9375rem` radii, `#fff3` highlights, and assets (387c923d20582ec7-s.p.2m62wczl7f17..., 83afe278b6a6bb3c-s.p.45535valc9rz..., 9873593f5e895d3f-s.p.1q5z3qm5aeja...).
5. **Colophon & Global Directory Footer (<footer.relative> — `https://www.baseline.agency/`)**:
   - DOM & Selectors: Landmark `<footer class="relative w-full">` anchoring `Baseline · Brand identity system` footer links (`About > A b o u t`), copy *"Services > S e r v i c e s"*, and `#000000` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.relative> — `https://www.baseline.agency/`)` aligns to `40rem` extracted from `www-baseline-agency` stylesheet with `.375rem` lateral canvas padding with `.5rem` grid gap and attributes (data-precedence="next", data-precedence="next", data-precedence="next").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Baseline B a s e l i n e Studio S t u d i o"*
- Copy Excerpt 2: *"Baseline B a s e l i n e"*
- Copy Excerpt 3: *"Studio S t u d i o"*
- Copy Excerpt 4: *"Services > S e r v i c e s"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(.19,1,.22,1)`, `cubic-bezier(.6,0,.3,1)`
- **Extracted Stylesheet Rules (`www-baseline-agency`)**:
- `.LW-vgW_cta { opacity:0;visibility:hidden;transition:opacity .3s,visibility 0s linear .3s }`
- `.LW-vgW_dim { opacity:0;transition:opacity 0s linear .3s }`
- `.LW-vgW_line { margin:0 -.1em -.14em;padding:0 .1em .14em;display:block;overflow:hidden }`
- `.LW-vgW_line>span { transition:transform 0s linear .3s;display:block;transform:translateY(115%) }`
- `.LW-vgW_rise { opacity:0;transition:opacity 0s linear .3s,transform 0s linear .3s;trans... }`
- **Per-Selector Transition Rules**:
- **Selector `.LW-vgW_cta`**: `transition: opacity .3s,visibility 0s linear .3s` extracted from `www-baseline-agency` stylesheet.
- **Selector `.LW-vgW_stage[data-shown=true] .L...`**: `transition: none` extracted from `www-baseline-agency` stylesheet.
- **Selector `.LW-vgW_dim`**: `transition: opacity 0s linear .3s` extracted from `www-baseline-agency` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.22,1,.36,1)`)**: Governs interactive state transitions across `<header.lenis>` and `<section.relative>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-baseline-agency`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
