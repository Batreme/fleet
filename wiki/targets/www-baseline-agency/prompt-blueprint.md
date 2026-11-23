---
title: "UI Prompt Blueprint: www-baseline-agency"
date: 2026-11-23
captured_at: 2026-11-23
target: "www-baseline-agency"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#000000`)"
---

# UI Design System & Master Generation Blueprint: www-baseline-agency

> **Baseline · Brand identity systems, designed and built** (https://www.baseline.agency/) — Brand identity studio in Cluj-Napoca led by Victor Deaconu. Positioning, identity, rules and guidelines in 3 to 4 weeks, for brands that...

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Baseline · Brand identity systems, designed and built** (`https://www.baseline.agency/`). Brand identity studio in Cluj-Napoca led by Victor Deaconu. Positioning, identity, rules and guidelines in 3 to 4 weeks, for brands that...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#000000`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#000000` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Inter` for display copy (`You got here with your brand working`) with `Inter` and `IBM Plex Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `96rem` container bounds (`gap: .5rem`, padding `.375rem`) with `cubic-bezier(.22,1,.36,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, clamped at 2400px live multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `96rem` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `.375rem` lateral canvas padding with `.5rem` grid gap.
- **Border Radius Scale**: `.25rem`, `.35625rem`, `.375rem`, `.9375rem`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 96rem`, `gap: .5rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `.375rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `body` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#e0e0e0` | `.UwedmG_neutral .UwedmG_layerBase { background: #e0e0e0 }` |
| **Interactive Accent / Highlight** | `#000000` | `.S6Hkya_link:hover { color: #000000 }` |
| **Secondary / Muted Copy** | `#0d0d0d` | `:focus-visible { color: #0d0d0d }` |
| **Structural Hairline Border** | `#cecece` | `25 { border-color: #cecece }` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--background` | `#fff` | Canvas / Surface Token |
| `--foreground` | `#000` | Typography Ink Token |
| `--t-display` | `clamp(calc(34*1px),calc(30.1*1px) + 1.04vw,calc(48.07*1px))` | Dimension / Scale Token |
| `--t-heading` | `clamp(calc(24*1px),calc(22.9*1px) + .296vw,calc(28*1px))` | Typography Ink Token |
| `--t-body` | `clamp(calc(16*1px),calc(15.45*1px) + .148vw,calc(18*1px))` | Dimension / Scale Token |
| `--t-label` | `calc(14*1px)` | Dimension / Scale Token |
| `--edge` | `clamp(calc(17*1px),calc(14.5*1px) + .665vw,calc(26*1px))` | Dimension / Scale Token |
| `--gap` | `clamp(calc(16*1px),calc(13.2*1px) + .739vw,calc(26*1px))` | Layout / Spatial Grid Token |
| `--space-row` | `clamp(calc(48*1px),calc(34.7*1px) + 3.548vw,calc(96*1px))` | Layout / Spatial Grid Token |
| `--space-section` | `clamp(calc(96*1px),calc(72.7*1px) + 6.208vw,calc(180*1px))` | Layout / Spatial Grid Token |
| `--ink-light` | `0` | Canvas / Surface Token |
| `--duration-exit` | `.15s` | Motion / Easing Token |
| `--duration-enter` | `.21s` | Motion / Easing Token |
| `--duration-move` | `.4s` | Motion / Easing Token |
| `--font-inter` | `"Inter", "Inter Fallback"` | Typography / Scale Token |
| `--font-inter-tight` | `"Inter Tight", "Inter Tight Fallback"` | Typography / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Inter`.
- **Primary Body Stack**: `Inter`.
- **Technical / Metadata Stack**: `IBM Plex Mono`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 46.5333px`, `line-height: 44.2067px`, `font-weight: 700`, `letter-spacing: -1.396px`); CSS variables `--t-display: clamp(calc(34*1px),calc(30.1*1px) + 1.04vw,calc(48.07*1px))`.
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 45.8333px`, `line-height: 50.4167px`, `font-weight: 700`, `letter-spacing: -1.375px`).
- **Body Copy**: live computed `body` (`font-size: 15.28px`, `line-height: 22.92px`, `font-weight: 400`); CSS variables `--t-body: clamp(calc(16*1px),calc(15.45*1px) + .148vw,calc(18*1px))`.
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 15.28px`, `line-height: 18.145px`, `font-weight: 700`, `letter-spacing: -0.6112px`); CSS variables `--t-label: calc(14*1px)`, `--default-mono-font-family: var(--font-mono)`, `--about-small: clamp(calc(11 * 1px), .88vw, calc(24 * 1px))`.

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

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Baseline · Brand identity systems, designe │
│ ====================================================================== │
│ [ <header.lenis> (1440px)             | About > A b o u t            ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hero-drift> (w=1440px)                        | │
│ | H1: You got here with your brand working against you....           | │
│ | Substrate: #ffffff | Ink: #000000 | Accent: #000000                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.relative>) max-w: 96rem                    | │
│ | +------------------------------+  +------------------------------+ | │
│ | | You've grown this far despit |  | Baseline B a s e l i n e Stu | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<article.flex>) — Baseline B a s e l i              | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.relative>   ) | https://www.baseline.agency/         │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: .5rem)      │
│ ====================================================================== │
│ [ HEADER BAR (<header.lenis>          ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.hero-drift>) — 390px Vertical Lead            | │
│ | H1: You got here with your brand working against you....           | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.relative>) — 1-Col Stack                  | │
│ | [ Item 1: You've grown this far despite the brand and webs       ] | │
│ | [ Item 2: Baseline B a s e l i n e Studio S t u d i o            ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<article.flex>) — 1-Col (Baseline B a s e l)         | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.relative>   ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.lenis> — `www-baseline-agency`)**:
   - Landmark `<header class="lenis">` (`1440px`) hosting `Baseline · Brand identity systems, d` navigation (`About > A b o u t`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-sdkn="@vercel/analytics/next"`), and stylesheet rule `.LW-vgW_cta { opacity:0;visibility:hidden;transition:opacity .3s,visibility 0s linear .3s }`.
2. **Hero Stage & Focal Lead (<section.hero-drift> — `You got here with your brand worki`)**:
   - Landmark `<section class="hero-drift relative">` presenting display lead `You got here with your brand working against you....` and copy excerpt *"You've grown this far despite the brand and website built when yo"* over `#ffffff` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.relative> — `You've grown this far despite the `)**:
   - Landmark `<section class="relative text-white">` rendering section `You've grown this far despite the brand and webs` with copy *"Baseline B a s e l i n e Studio S t u d i o"*, asset references (`41q-9hyqnol8s.css`, `11vyltt-w7ouz.css`, `027ldshog-_ys.css`, `3ya-20k_dn7en.js`), and grid rule `.LW-vgW_dim { opacity:0;transition:opacity 0s linear .3s }`.
4. **Interactive Detail & Feature Matrix (<article.flex> — `Baseline B a s e l i n e Studio S `)**:
   - Landmark `<article class="flex flex-col">` framing `Baseline B a s e l i n e Studio S t u d i o` and `Baseline B a s e l i n e` (*"Baseline B a s e l i n e"*) with `#e0e0e0` surface cards, `#000000` accents, and `.LW-vgW_line { margin:0 -.1em -.14em;padding:0 .1em .14em;display:block;overflow:hidden }`.
5. **Colophon & Global Directory Footer (<footer.relative> — `https://www.baseline.agency/`)**:
   - Landmark `<footer class="relative w-full">` anchoring `Baseline · Brand identity system` footer links (`About > A b o u t`), copy *"Studio S t u d i o"*, and `#cecece` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-baseline-agency (Baseline · Brand identity systems, designed and built)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-baseline-agency` (**Baseline · Brand identity systems, designed and built** — `https://www.baseline.agency/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#000000`).
- **Identity & Domain Context**: Brand identity studio in Cluj-Napoca led by Victor Deaconu. Positioning, identity, rules and guidelines in 3 to 4 weeks, for brands that...
- **Primary Substrate**: `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#000000`, **Accent / Highlight**: `#000000`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#000000` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Inter` for display copy (`You got here with your brand working`) with `Inter` and `IBM Plex Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `96rem` container bounds (`gap: .5rem`, padding `.375rem`) with `cubic-bezier(.22,1,.36,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-baseline-agency` in your global stylesheet:

:root {
  /* Baseline · Brand identity systems, designed and built (www-baseline-agency) — Live-Grounded CSS Variables */
  --background: #fff; /* Canvas / Surface Token (www-baseline-agency) */
  --foreground: #000; /* Typography Ink Token (www-baseline-agency) */
  --t-display: clamp(calc(34*1px),calc(30.1*1px) + 1.04vw,calc(48.07*1px)); /* Dimension / Scale Token (www-baseline-agency) */
  --t-heading: clamp(calc(24*1px),calc(22.9*1px) + .296vw,calc(28*1px)); /* Typography Ink Token (www-baseline-agency) */
  --t-body: clamp(calc(16*1px),calc(15.45*1px) + .148vw,calc(18*1px)); /* Dimension / Scale Token (www-baseline-agency) */
  --t-label: calc(14*1px); /* Dimension / Scale Token (www-baseline-agency) */
  --edge: clamp(calc(17*1px),calc(14.5*1px) + .665vw,calc(26*1px)); /* Dimension / Scale Token (www-baseline-agency) */
  --gap: clamp(calc(16*1px),calc(13.2*1px) + .739vw,calc(26*1px)); /* Layout / Spatial Grid Token (www-baseline-agency) */
  --space-row: clamp(calc(48*1px),calc(34.7*1px) + 3.548vw,calc(96*1px)); /* Layout / Spatial Grid Token (www-baseline-agency) */
  --space-section: clamp(calc(96*1px),calc(72.7*1px) + 6.208vw,calc(180*1px)); /* Layout / Spatial Grid Token (www-baseline-agency) */
  --ink-light: 0; /* Canvas / Surface Token (www-baseline-agency) */
  --duration-exit: .15s; /* Motion / Easing Token (www-baseline-agency) */
  --duration-enter: .21s; /* Motion / Easing Token (www-baseline-agency) */
  --duration-move: .4s; /* Motion / Easing Token (www-baseline-agency) */
  --font-inter: "Inter", "Inter Fallback"; /* Typography / Scale Token (www-baseline-agency) */
  --font-inter-tight: "Inter Tight", "Inter Tight Fallback"; /* Typography / Scale Token (www-baseline-agency) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ffffff` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#000000` — grounded in live computed `body` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#e0e0e0` — grounded in `.UwedmG_neutral .UwedmG_layerBase { background: #e0e0e0 }`
- **Interactive Accent / Highlight**: `#000000` — grounded in `.S6Hkya_link:hover { color: #000000 }`
- **Secondary / Muted Copy**: `#0d0d0d` — grounded in `:focus-visible { color: #0d0d0d }`
- **Structural Hairline Border**: `#cecece` — grounded in `25 { border-color: #cecece }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (clamped at 2400px live multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `96rem` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `.375rem` lateral canvas padding with `.5rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 96rem`, `gap: .5rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `.375rem` horizontal padding
- **Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`
- **Corner Radii**: `.25rem`, `.35625rem`, `.375rem`, `.9375rem`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: `IBM Plex Mono`
- **H1 Display Rule**: live computed `h1` (`font-size: 46.5333px`, `line-height: 44.2067px`, `font-weight: 700`, `letter-spacing: -1.396px`); CSS variables `--t-display: clamp(calc(34*1px),calc(30.1*1px) + 1.04vw,calc(48.07*1px))`
- **H2 Section Rule**: live computed `h2` (`font-size: 45.8333px`, `line-height: 50.4167px`, `font-weight: 700`, `letter-spacing: -1.375px`)
- **Body Copy Rule**: live computed `body` (`font-size: 15.28px`, `line-height: 22.92px`, `font-weight: 400`); CSS variables `--t-body: clamp(calc(16*1px),calc(15.45*1px) + .148vw,calc(18*1px))`
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 15.28px`, `line-height: 18.145px`, `font-weight: 700`, `letter-spacing: -0.6112px`); CSS variables `--t-label: calc(14*1px)`, `--default-mono-font-family: var(--font-mono)`, `--about-small: clamp(calc(11 * 1px), .88vw, calc(24 * 1px))`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-baseline-agency` (`Baseline · Brand identity systems, designed and built`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.lenis> — `www-baseline-agency`)**:
   - DOM & Selectors: Landmark `<header class="lenis">` (`1440px`) hosting `Baseline · Brand identity systems, d` navigation (`About > A b o u t`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-sdkn="@vercel/analytics/next"`), and stylesheet rule `.LW-vgW_cta { opacity:0;visibility:hidden;transition:opacity .3s,visibility 0s linear .3s }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.lenis> — `www-baseline-agency`)` (`www-baseline-agency`) adapts across `@media (prefers-reduced-motion:reduce)`, `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)` with `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(.19,1,.22,1)`, `cubic-bezier(.6,0,.3,1)` transitions and links `About > A b o u t`.
2. **Hero Stage & Focal Lead (<section.hero-drift> — `You got here with your brand worki`)**:
   - DOM & Selectors: Landmark `<section class="hero-drift relative">` presenting display lead `You got here with your brand working against you....` and copy excerpt *"You've grown this far despite the brand and website built when yo"* over `#ffffff` canvas and `#000000` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#ffffff` background with `#000000` headline `You got here with your brand working against you....`.
3. **Primary Showcase & Content Grid (<section.relative> — `You've grown this far despite the `)**:
   - DOM & Selectors: Landmark `<section class="relative text-white">` rendering section `You've grown this far despite the brand and webs` with copy *"Baseline B a s e l i n e Studio S t u d i o"*, asset references (`41q-9hyqnol8s.css`, `11vyltt-w7ouz.css`, `027ldshog-_ys.css`, `3ya-20k_dn7en.js`), and grid rule `.LW-vgW_dim { opacity:0;transition:opacity 0s linear .3s }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.relative> — `You've grown this far despite the `)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 96rem`, `gap: .5rem`) on desktop and Single-column vertical stack at `390px` viewport width with `.375rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<article.flex> — `Baseline B a s e l i n e Studio S `)**:
   - DOM & Selectors: Landmark `<article class="flex flex-col">` framing `Baseline B a s e l i n e Studio S t u d i o` and `Baseline B a s e l i n e` (*"Baseline B a s e l i n e"*) with `#e0e0e0` surface cards, `#000000` accents, and `.LW-vgW_line { margin:0 -.1em -.14em;padding:0 .1em .14em;display:block;overflow:hidden }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<article.flex> — `Baseline B a s e l i n e Studio S `)` uses `.25rem`, `.35625rem`, `.375rem`, `.9375rem` radii, `#000000` highlights, and assets (41q-9hyqnol8s.css, 11vyltt-w7ouz.css, 027ldshog-_ys.css).
5. **Colophon & Global Directory Footer (<footer.relative> — `https://www.baseline.agency/`)**:
   - DOM & Selectors: Landmark `<footer class="relative w-full">` anchoring `Baseline · Brand identity system` footer links (`About > A b o u t`), copy *"Studio S t u d i o"*, and `#cecece` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.relative> — `https://www.baseline.agency/`)` aligns to `96rem` (non-`@media` desktop container stylesheet rule) with `.375rem` lateral canvas padding with `.5rem` grid gap and attributes (data-precedence="next", data-precedence="next", data-precedence="next").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"You've grown this far despite the brand and website built when you were half this..."*
- Copy Excerpt 2: *"Baseline B a s e l i n e Studio S t u d i o"*
- Copy Excerpt 3: *"Baseline B a s e l i n e"*
- Copy Excerpt 4: *"Studio S t u d i o"*

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
