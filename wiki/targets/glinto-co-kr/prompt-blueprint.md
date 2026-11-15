---
title: "UI Prompt Blueprint: glinto-co-kr"
date: 2026-11-15
target: "[[overview|glinto-co-kr]]"
status: analyzed
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#ffc7b0`)"
---

# UI Design System & Master Generation Blueprint: glinto-co-kr

> **Glinto — Creative studio** (https://glinto.co.kr) — Glinto is a creative studio where one team takes brand strategy and identity, film and photography, design, and web and app development f...

![Desktop Viewport Capture (1440x9417)](file:///root/projects/fleet/wiki/targets/glinto-co-kr/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Glinto — Creative studio** (`https://glinto.co.kr`). Glinto is a creative studio where one team takes brand strategy and identity, film and photography, design, and web and app development f...
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#ffc7b0`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fff` (`var(--color-white)` in `:root`) paired with `#ff7f54` primary typography and `#ffc7b0` accents.
  - **Extracted Typographic Hierarchy**: Pairs `DM Sans` for display copy (`Everything your brand needs, from on`) with `DM Sans Fallback` and `JetBrains Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `40rem` container bounds (`gap: var(--spacing-1)`, padding `var(--spacing-1)`) with `cubic-bezier(.4,0,1,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/glinto-co-kr/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×9417px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `40rem` extracted from `glinto-co-kr` stylesheet.
- **Canvas Lateral Padding & Spacing**: `var(--spacing-1)` lateral canvas padding with `var(--spacing-1)` grid gap.
- **Border Radius Scale**: `.25rem`, `var(--pixel-radius)`, `.5rem`, `.75rem`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: var(--spacing-1)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--spacing-1)` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--color-white)` in `:root` |
| **Primary Typography Ink** | `#fff3ee` | `var(--accent-50)` in `:root` |
| **Elevated Surface / Card Substrate** | `#ffe4d9` | `var(--accent-100)` in `:root` |
| **Interactive Accent / Highlight** | `#ffc7b0` | `var(--accent-200)` in `:root` |
| **Secondary / Muted Copy** | `#ffa47d` | `var(--accent-300)` in `:root` |
| **Structural Hairline Border** | `#ff7f54` | `var(--accent-400)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-dm-sans` | `"DM Sans", "DM Sans Fallback"` | Typography / Scale Token |
| `--header-fill` | `0` | Layout / Spatial Grid Token |
| `--px-x` | `80%` | Dimension / Scale Token |
| `--px-y` | `0%` | Dimension / Scale Token |
| `--wm-x` | `20%` | Dimension / Scale Token |
| `--wm-y` | `30%` | Dimension / Scale Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--text-sm` | `var(--fs-sm)` | Typography Ink Token |
| `--text-sm--line-height` | `var(--lh-sm)` | Typography Ink Token |
| `--font-weight-light` | `300` | Canvas / Surface Token |
| `--font-weight-normal` | `400` | Typography / Scale Token |
| `--font-weight-medium` | `500` | Typography / Scale Token |
| `--font-weight-semibold` | `600` | Typography / Scale Token |
| `--font-weight-bold` | `700` | Typography / Scale Token |
| `--ease-in` | `cubic-bezier(.4, 0, 1, 1)` | Motion / Easing Token |
| `--ease-out` | `cubic-bezier(0, 0, .2, 1)` | Motion / Easing Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `DM Sans`.
- **Primary Body Stack**: `DM Sans Fallback`.
- **Technical / Metadata Stack**: `JetBrains Mono`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--text-h1: var(--fs-h1)`, `--text-h1--line-height: var(--lh-figma)`, `--text-display-sans: var(--fs-display-sans)`.
- **Section Heading (`H2`)**: CSS variables `--text-h2: var(--fs-h2)`, `--text-h2--line-height: var(--lh-figma)`, `--subtitle-color: var(--gray-200)`.
- **Body Copy**: CSS variables `--text-body-s: var(--fs-body-s)`, `--text-body-s--line-height: var(--lh-figma)`, `--text-body-m: var(--fs-body-m)`.
- **Metadata & Navigation Labels**: CSS variables `--text-sm: var(--fs-sm)`, `--text-sm--line-height: var(--lh-sm)`, `--default-mono-font-family: var(--font-mono)`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: .15s` extracted from `glinto-co-kr` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `glinto-co-kr` stylesheet.
- **Selector `.transition-\[clip-path\]`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `glinto-co-kr` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,1,1)`)**: Governs interactive state transitions across `<header.site-header-wrap>` and `<section.pt-24>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Glinto — Creative studio                   │
│ ====================================================================== │
│ [ <header.site-header-wrap | About · Services · Glinto.dev · Works  ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.antialiased>                                |   │
│ | H1: Everything your brand needs, from one team                   |   │
│ | Substrate: #fff       | Ink: #ff7f54    | Accent: #ffc7b0        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.pt-24>           ) max-w: 40rem          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Media                        |  | Design                       | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: var(--) | │
│ | [<header.site-heade] -> [<section.antialias] -> [<section.pt-24>] |  │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.mt-24>        ) | https://glinto.co.kr               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.site-header-wrap> — `glinto-co-kr`)**:
   - Landmark `<header class="site-header-wrap sticky">` hosting `Glinto — Creative studio` navigation (`About · Services · Glinto.dev · Works · Contact`), DOM attributes (`data-theme="light"`, `data-reveal-ready`, `data-progress-ready`, `data-precedence="next"`), and stylesheet rule `sans_efc253b3-module__w1i8Da__cla... { font-family:DM Sans,DM Sans Fallback;font-style:normal }`.
2. **Hero Stage & Focal Lead (<section.antialiased> — `Everything your brand needs, from `)**:
   - Landmark `<section class="antialiased">` presenting display lead `Everything your brand needs, from one team` and copy excerpt *"Services Glinto.dev"* over `#fff` canvas and `#ff7f54` ink.
3. **Primary Showcase & Content Grid (<section.pt-24> — `Media`)**:
   - Landmark `<section class="pt-24">` rendering section `Media` with copy *"Creative studio for identity, visuals, and code."*, asset references (`2f7d2945a32bc936-s.p.0q9pvfn3wr_3...`, `5c285b27cdda1fe8-s.p.0lsanbtneewq...`, `0k1f2nt08p6_n.css`, `0twwmijs60d6j.css`), and grid rule `sans_efc253b3-module__w1i8Da__var... { --font-dm-sans:"DM Sans", "DM Sans Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.pt-24> — `Design`)**:
   - Landmark `<section class="pt-24">` framing `Design` and `Engineering` (*"BX Plan it BX Plan it"*) with `#ffe4d9` surface cards, `#ffc7b0` accents, and `host { --header-fill:0;--px-x:80%;--px-y:0% }`.
5. **Colophon & Global Directory Footer (<footer.mt-24> — `https://glinto.co.kr`)**:
   - Landmark `<footer class="mt-24">` anchoring `Glinto — Creative studio` footer links (`About · Services · Glinto.dev · Works · Contact`), copy *"Media Capture it Media Capture it"*, and `#ff7f54` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: glinto-co-kr (Glinto — Creative studio)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `glinto-co-kr` (**Glinto — Creative studio** — `https://glinto.co.kr`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#ffc7b0`).
- **Identity & Domain Context**: Glinto is a creative studio where one team takes brand strategy and identity, film and photography, design, and web and app development f...
- **Primary Substrate**: `#fff` (`var(--color-white)` in `:root`), **Primary Ink**: `#ff7f54`, **Accent / Highlight**: `#ffc7b0`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fff` (`var(--color-white)` in `:root`) paired with `#ff7f54` primary typography and `#ffc7b0` accents.
  - **Extracted Typographic Hierarchy**: Pairs `DM Sans` for display copy (`Everything your brand needs, from on`) with `DM Sans Fallback` and `JetBrains Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `40rem` container bounds (`gap: var(--spacing-1)`, padding `var(--spacing-1)`) with `cubic-bezier(.4,0,1,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `glinto-co-kr` in your global stylesheet:

:root {
  /* Glinto — Creative studio (glinto-co-kr) — Ground-Truth Extracted CSS Variables */
  --font-dm-sans: "DM Sans", "DM Sans Fallback"; /* Typography / Scale Token (glinto-co-kr) */
  --header-fill: 0; /* Layout / Spatial Grid Token (glinto-co-kr) */
  --px-x: 80%; /* Dimension / Scale Token (glinto-co-kr) */
  --px-y: 0%; /* Dimension / Scale Token (glinto-co-kr) */
  --wm-x: 20%; /* Dimension / Scale Token (glinto-co-kr) */
  --wm-y: 30%; /* Dimension / Scale Token (glinto-co-kr) */
  --spacing: .25rem; /* Layout / Spatial Grid Token (glinto-co-kr) */
  --text-sm: var(--fs-sm); /* Typography Ink Token (glinto-co-kr) */
  --text-sm--line-height: var(--lh-sm); /* Typography Ink Token (glinto-co-kr) */
  --font-weight-light: 300; /* Canvas / Surface Token (glinto-co-kr) */
  --font-weight-normal: 400; /* Typography / Scale Token (glinto-co-kr) */
  --font-weight-medium: 500; /* Typography / Scale Token (glinto-co-kr) */
  --font-weight-semibold: 600; /* Typography / Scale Token (glinto-co-kr) */
  --font-weight-bold: 700; /* Typography / Scale Token (glinto-co-kr) */
  --ease-in: cubic-bezier(.4, 0, 1, 1); /* Motion / Easing Token (glinto-co-kr) */
  --ease-out: cubic-bezier(0, 0, .2, 1); /* Motion / Easing Token (glinto-co-kr) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#fff` — grounded in `var(--color-white)` in `:root`
- **Primary Typography Ink**: `#fff3ee` — grounded in `var(--accent-50)` in `:root`
- **Elevated Surface / Card Substrate**: `#ffe4d9` — grounded in `var(--accent-100)` in `:root`
- **Interactive Accent / Highlight**: `#ffc7b0` — grounded in `var(--accent-200)` in `:root`
- **Secondary / Muted Copy**: `#ffa47d` — grounded in `var(--accent-300)` in `:root`
- **Structural Hairline Border**: `#ff7f54` — grounded in `var(--accent-400)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×9417px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `40rem` extracted from `glinto-co-kr` stylesheet
- **Padding & Gutters**: `var(--spacing-1)` lateral canvas padding with `var(--spacing-1)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: var(--spacing-1)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--spacing-1)` horizontal padding
- **Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)`
- **Corner Radii**: `.25rem`, `var(--pixel-radius)`, `.5rem`, `.75rem`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `DM Sans`
- **Body Font Stack**: `DM Sans Fallback`
- **Monospace / Technical Font Stack**: `JetBrains Mono`
- **H1 Display Rule**: CSS variables `--text-h1: var(--fs-h1)`, `--text-h1--line-height: var(--lh-figma)`, `--text-display-sans: var(--fs-display-sans)`
- **H2 Section Rule**: CSS variables `--text-h2: var(--fs-h2)`, `--text-h2--line-height: var(--lh-figma)`, `--subtitle-color: var(--gray-200)`
- **Body Copy Rule**: CSS variables `--text-body-s: var(--fs-body-s)`, `--text-body-s--line-height: var(--lh-figma)`, `--text-body-m: var(--fs-body-m)`
- **Metadata & Index Rule**: CSS variables `--text-sm: var(--fs-sm)`, `--text-sm--line-height: var(--lh-sm)`, `--default-mono-font-family: var(--font-mono)`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `glinto-co-kr` (`Glinto — Creative studio`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.site-header-wrap> — `glinto-co-kr`)**:
   - DOM & Selectors: Landmark `<header class="site-header-wrap sticky">` hosting `Glinto — Creative studio` navigation (`About · Services · Glinto.dev · Works · Contact`), DOM attributes (`data-theme="light"`, `data-reveal-ready`, `data-progress-ready`, `data-precedence="next"`), and stylesheet rule `sans_efc253b3-module__w1i8Da__cla... { font-family:DM Sans,DM Sans Fallback;font-style:normal }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.site-header-wrap> — `glinto-co-kr`)` (`glinto-co-kr`) adapts across `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)` with `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)` transitions and links `About · Services · Glinto.dev · Works · Contact`.
2. **Hero Stage & Focal Lead (<section.antialiased> — `Everything your brand needs, from `)**:
   - DOM & Selectors: Landmark `<section class="antialiased">` presenting display lead `Everything your brand needs, from one team` and copy excerpt *"Services Glinto.dev"* over `#fff` canvas and `#ff7f54` ink.
   - Responsive Contract: Hero stage (`1440×9417px` desktop / `390×2400px` mobile) sets `#fff` background with `#ff7f54` headline `Everything your brand needs, from one team`.
3. **Primary Showcase & Content Grid (<section.pt-24> — `Media`)**:
   - DOM & Selectors: Landmark `<section class="pt-24">` rendering section `Media` with copy *"Creative studio for identity, visuals, and code."*, asset references (`2f7d2945a32bc936-s.p.0q9pvfn3wr_3...`, `5c285b27cdda1fe8-s.p.0lsanbtneewq...`, `0k1f2nt08p6_n.css`, `0twwmijs60d6j.css`), and grid rule `sans_efc253b3-module__w1i8Da__var... { --font-dm-sans:"DM Sans", "DM Sans Fallback" }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.pt-24> — `Media`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: var(--spacing-1)`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--spacing-1)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.pt-24> — `Design`)**:
   - DOM & Selectors: Landmark `<section class="pt-24">` framing `Design` and `Engineering` (*"BX Plan it BX Plan it"*) with `#ffe4d9` surface cards, `#ffc7b0` accents, and `host { --header-fill:0;--px-x:80%;--px-y:0% }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.pt-24> — `Design`)` uses `.25rem`, `var(--pixel-radius)`, `.5rem`, `.75rem` radii, `#ffc7b0` highlights, and assets (2f7d2945a32bc936-s.p.0q9pvfn3wr_3..., 5c285b27cdda1fe8-s.p.0lsanbtneewq..., 0k1f2nt08p6_n.css).
5. **Colophon & Global Directory Footer (<footer.mt-24> — `https://glinto.co.kr`)**:
   - DOM & Selectors: Landmark `<footer class="mt-24">` anchoring `Glinto — Creative studio` footer links (`About · Services · Glinto.dev · Works · Contact`), copy *"Media Capture it Media Capture it"*, and `#ff7f54` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.mt-24> — `https://glinto.co.kr`)` aligns to `40rem` extracted from `glinto-co-kr` stylesheet with `var(--spacing-1)` lateral canvas padding with `var(--spacing-1)` grid gap and attributes (data-theme="light", data-reveal-ready, data-progress-ready).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Services Glinto.dev"*
- Copy Excerpt 2: *"Creative studio for identity, visuals, and code."*
- Copy Excerpt 3: *"BX Plan it BX Plan it"*
- Copy Excerpt 4: *"Media Capture it Media Capture it"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`
- **Extracted Stylesheet Rules (`glinto-co-kr`)**:
- `sans_efc253b3-module__w1i8Da__cla... { font-family:DM Sans,DM Sans Fallback;font-style:normal }`
- `sans_efc253b3-module__w1i8Da__var... { --font-dm-sans:"DM Sans", "DM Sans Fallback" }`
- `host { --header-fill:0;--px-x:80%;--px-y:0% }`
- `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: .15s` extracted from `glinto-co-kr` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `glinto-co-kr` stylesheet.
- **Selector `.transition-\[clip-path\]`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `glinto-co-kr` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,1,1)`)**: Governs interactive state transitions across `<header.site-header-wrap>` and `<section.pt-24>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `glinto-co-kr`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
