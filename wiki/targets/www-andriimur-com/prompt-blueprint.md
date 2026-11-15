---
title: "UI Prompt Blueprint: www-andriimur-com"
date: 2026-11-15
target: "[[overview|www-andriimur-com]]"
status: analyzed
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#4f4f4f` accent)"
---

# UI Design System & Master Generation Blueprint: www-andriimur-com

> **Andrii Mur** (https://www.andriimur.com/) — Andrii Mur – Ukrainian street & documentary photographer in Tallinn, Estonia. From the information mess to how it feels to be Alive in an...

![Desktop Viewport Capture (1440x8019)](file:///root/projects/fleet/wiki/targets/www-andriimur-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Andrii Mur** (`https://www.andriimur.com/`). Andrii Mur – Ukrainian street & documentary photographer in Tallinn, Estonia. From the information mess to how it feels to be Alive in an...
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#4f4f4f` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--pswp-bg)` in `:root`) paired with `#fff` primary typography and `#4f4f4f` accents.
  - **Extracted Typographic Hierarchy**: Pairs `PT Serif` for display copy (`Monochrome`) with `PT Serif Fallback` and `IBM Plex Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `40rem` container bounds (`gap: var(--spacing)`, padding `16px`) with `cubic-bezier(.4,0,.22,1)` easing.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/www-andriimur-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×8019px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `40rem` extracted from `www-andriimur-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `16px` lateral canvas padding with `var(--spacing)` grid gap.
- **Border Radius Scale**: `.25rem`, `3px`, `var(--radius-lg)`, `var(--radius-md)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: var(--spacing)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `16px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--pswp-bg)` in `:root` |
| **Primary Typography Ink** | `#222` | `var(--pswp-placeholder-bg)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fff` | `var(--pswp-icon-color)` in `:root` |
| **Interactive Accent / Highlight** | `#4f4f4f` | `var(--pswp-icon-color-secondary)` in `:root` |
| **Secondary / Muted Copy** | `#fef9c2` | `var(--color-yellow-100)` in `:root` |
| **Structural Hairline Border** | `#a36100` | `var(--color-yellow-700)` in `:root` |
| **Variable Token (`--pswp-preloader-color`)** | `#4f4f4f66` | `var(--pswp-preloader-color)` in `:root` |
| **Variable Token (`--pswp-preloader-color-secondary`)** | `#ffffffe6` | `var(--pswp-preloader-color-secondary)` in `:root` |
| **Variable Token (`--color-blue-500`)** | `#3080ff` | `var(--color-blue-500)` in `:root` |
| **Variable Token (`--color-blue-800`)** | `#193cb8` | `var(--color-blue-800)` in `:root` |
| **Variable Token (`--color-slate-200`)** | `#e2e8f0` | `var(--color-slate-200)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--pswp-bg` | `#000` | Canvas / Surface Token |
| `--pswp-placeholder-bg` | `#222` | Canvas / Surface Token |
| `--pswp-root-z-index` | `100000` | Elevation / Border Token |
| `--pswp-preloader-color` | `#4f4f4f66` | Brand / Palette Token |
| `--pswp-preloader-color-secondary` | `#ffffffe6` | Brand / Palette Token |
| `--pswp-icon-color` | `#fff` | Brand / Palette Token |
| `--pswp-icon-color-secondary` | `#4f4f4f` | Brand / Palette Token |
| `--pswp-icon-stroke-color` | `#4f4f4f` | Brand / Palette Token |
| `--pswp-icon-stroke-width` | `2px` | Layout / Spatial Grid Token |
| `--pswp-error-text-color` | `var(--pswp-icon-color)` | Typography Ink Token |
| `--font-serif` | `ui-serif, Georgia, Cambria, "Times New Roman", Times, serif` | Typography / Scale Token |
| `--color-yellow-100` | `#fef9c2` | Brand / Palette Token |
| `--color-yellow-700` | `#a36100` | Brand / Palette Token |
| `--color-blue-500` | `#3080ff` | Brand / Palette Token |
| `--color-blue-800` | `#193cb8` | Brand / Palette Token |
| `--color-slate-200` | `#e2e8f0` | Brand / Palette Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `PT Serif`.
- **Primary Body Stack**: `PT Serif Fallback`.
- **Technical / Metadata Stack**: `IBM Plex Mono`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`.
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`.
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`.
- **Metadata & Navigation Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,.22,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.pswp .pswp__hide-on-close`**: `transition: opacity var(--pswp-transition-duration) cubic-bezier(.4, 0, .2...` extracted from `www-andriimur-com` stylesheet.
- **Selector `.pswp__button:focus`**: `transition: none` extracted from `www-andriimur-com` stylesheet.
- **Selector `.pswp__preloader .pswp__icn`**: `transition: opacity .2s linear` extracted from `www-andriimur-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.22,1)`)**: Governs interactive state transitions across `<header.sticky>` and `<section.snap-showcase>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<section.dark>` and `<section.snap-showcase>` interactive targets.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Andrii Mur                                 │
│ ====================================================================== │
│ [ <header.sticky>          | About · Monochrome · Drops of Melancho ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.dark>                                       |   │
│ | H1: Monochrome                                                   |   │
│ | Substrate: #000       | Ink: #fff       | Accent: #4f4f4f        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.snap-showcase>   ) max-w: 40rem          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Drops of Melancholy          |  | XA-23.4°                     | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: var(--) | │
│ | [<header.sticky>] -> [<section.dark>] -> [<section.snap-show] |      │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.relative>     ) | https://www.andriimur.com/         │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.sticky> — `www-andriimur-com`)**:
   - Landmark `<header class="sticky top-0">` hosting `Andrii Mur` navigation (`About · Monochrome · Drops of Melancholy · XA-23.4° · After Dusk`), DOM attributes (`data-theme="dark"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `.pswp img { max-width:none }`.
2. **Hero Stage & Focal Lead (<section.dark> — `Monochrome`)**:
   - Landmark `<section class="dark">` presenting display lead `Monochrome` and copy excerpt *"Drops of Melancholy"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.snap-showcase> — `Drops of Melancholy`)**:
   - Landmark `<section class="snap-showcase">` rendering section `Drops of Melancholy` with copy *"Fulfilling Emptiness"*, asset references (`m2ak1cq3.api.sanity.io`, `6ab71d031fe7ae3b-s.p.141jscyq52bj...`, `80bb744e92754df7-s.p.2eihtoujcocl...`, `83afe278b6a6bb3c-s.p.2bn3s6zvc0dy...`), and grid rule `.pswp--open { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.flex> — `XA-23.4°`)**:
   - Landmark `<section class="flex">` framing `XA-23.4°` and `After Dusk` (*"The Look From Silence"*) with `#fff` surface cards, `#4f4f4f` accents, and `.pswp__bg { will-change:opacity;transform:translateZ(0) }`.
5. **Colophon & Global Directory Footer (<footer.relative> — `https://www.andriimur.com/`)**:
   - Landmark `<footer class="relative bottom-0">` anchoring `Andrii Mur` footer links (`About · Monochrome · Drops of Melancholy · XA-23.4° · After Dusk`), copy *"Monochrome Black and White singles"*, and `#a36100` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-andriimur-com (Andrii Mur)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-andriimur-com` (**Andrii Mur** — `https://www.andriimur.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#4f4f4f` accent).
- **Identity & Domain Context**: Andrii Mur – Ukrainian street & documentary photographer in Tallinn, Estonia. From the information mess to how it feels to be Alive in an...
- **Primary Substrate**: `#000` (`var(--pswp-bg)` in `:root`), **Primary Ink**: `#fff`, **Accent / Highlight**: `#4f4f4f`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--pswp-bg)` in `:root`) paired with `#fff` primary typography and `#4f4f4f` accents.
  - **Extracted Typographic Hierarchy**: Pairs `PT Serif` for display copy (`Monochrome`) with `PT Serif Fallback` and `IBM Plex Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `40rem` container bounds (`gap: var(--spacing)`, padding `16px`) with `cubic-bezier(.4,0,.22,1)` easing.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-andriimur-com` in your global stylesheet:

:root {
  /* Andrii Mur (www-andriimur-com) — Ground-Truth Extracted CSS Variables */
  --pswp-bg: #000; /* Canvas / Surface Token (www-andriimur-com) */
  --pswp-placeholder-bg: #222; /* Canvas / Surface Token (www-andriimur-com) */
  --pswp-root-z-index: 100000; /* Elevation / Border Token (www-andriimur-com) */
  --pswp-preloader-color: #4f4f4f66; /* Brand / Palette Token (www-andriimur-com) */
  --pswp-preloader-color-secondary: #ffffffe6; /* Brand / Palette Token (www-andriimur-com) */
  --pswp-icon-color: #fff; /* Brand / Palette Token (www-andriimur-com) */
  --pswp-icon-color-secondary: #4f4f4f; /* Brand / Palette Token (www-andriimur-com) */
  --pswp-icon-stroke-color: #4f4f4f; /* Brand / Palette Token (www-andriimur-com) */
  --pswp-icon-stroke-width: 2px; /* Layout / Spatial Grid Token (www-andriimur-com) */
  --pswp-error-text-color: var(--pswp-icon-color); /* Typography Ink Token (www-andriimur-com) */
  --font-serif: ui-serif, Georgia, Cambria, "Times New Roman", Times, serif; /* Typography / Scale Token (www-andriimur-com) */
  --color-yellow-100: #fef9c2; /* Brand / Palette Token (www-andriimur-com) */
  --color-yellow-700: #a36100; /* Brand / Palette Token (www-andriimur-com) */
  --color-blue-500: #3080ff; /* Brand / Palette Token (www-andriimur-com) */
  --color-blue-800: #193cb8; /* Brand / Palette Token (www-andriimur-com) */
  --color-slate-200: #e2e8f0; /* Brand / Palette Token (www-andriimur-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#000` — grounded in `var(--pswp-bg)` in `:root`
- **Primary Typography Ink**: `#222` — grounded in `var(--pswp-placeholder-bg)` in `:root`
- **Elevated Surface / Card Substrate**: `#fff` — grounded in `var(--pswp-icon-color)` in `:root`
- **Interactive Accent / Highlight**: `#4f4f4f` — grounded in `var(--pswp-icon-color-secondary)` in `:root`
- **Secondary / Muted Copy**: `#fef9c2` — grounded in `var(--color-yellow-100)` in `:root`
- **Structural Hairline Border**: `#a36100` — grounded in `var(--color-yellow-700)` in `:root`
- **Variable Token (`--pswp-preloader-color`)**: `#4f4f4f66` — grounded in `var(--pswp-preloader-color)` in `:root`
- **Variable Token (`--pswp-preloader-color-secondary`)**: `#ffffffe6` — grounded in `var(--pswp-preloader-color-secondary)` in `:root`
- **Variable Token (`--color-blue-500`)**: `#3080ff` — grounded in `var(--color-blue-500)` in `:root`
- **Variable Token (`--color-blue-800`)**: `#193cb8` — grounded in `var(--color-blue-800)` in `:root`
- **Variable Token (`--color-slate-200`)**: `#e2e8f0` — grounded in `var(--color-slate-200)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×8019px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `40rem` extracted from `www-andriimur-com` stylesheet
- **Padding & Gutters**: `16px` lateral canvas padding with `var(--spacing)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: var(--spacing)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `16px` horizontal padding
- **Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)`
- **Corner Radii**: `.25rem`, `3px`, `var(--radius-lg)`, `var(--radius-md)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `PT Serif`
- **Body Font Stack**: `PT Serif Fallback`
- **Monospace / Technical Font Stack**: `IBM Plex Mono`
- **H1 Display Rule**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`
- **H2 Section Rule**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`
- **Body Copy Rule**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`
- **Metadata & Index Rule**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-andriimur-com` (`Andrii Mur`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.sticky> — `www-andriimur-com`)**:
   - DOM & Selectors: Landmark `<header class="sticky top-0">` hosting `Andrii Mur` navigation (`About · Monochrome · Drops of Melancholy · XA-23.4° · After Dusk`), DOM attributes (`data-theme="dark"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `.pswp img { max-width:none }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.sticky> — `www-andriimur-com`)` (`www-andriimur-com`) adapts across `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)` with `cubic-bezier(.4,0,.22,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)` transitions and links `About · Monochrome · Drops of Melancholy · XA-23.4° · After Dusk`.
2. **Hero Stage & Focal Lead (<section.dark> — `Monochrome`)**:
   - DOM & Selectors: Landmark `<section class="dark">` presenting display lead `Monochrome` and copy excerpt *"Drops of Melancholy"* over `#000` canvas and `#fff` ink.
   - Responsive Contract: Hero stage (`1440×8019px` desktop / `390×2400px` mobile) sets `#000` background with `#fff` headline `Monochrome`.
3. **Primary Showcase & Content Grid (<section.snap-showcase> — `Drops of Melancholy`)**:
   - DOM & Selectors: Landmark `<section class="snap-showcase">` rendering section `Drops of Melancholy` with copy *"Fulfilling Emptiness"*, asset references (`m2ak1cq3.api.sanity.io`, `6ab71d031fe7ae3b-s.p.141jscyq52bj...`, `80bb744e92754df7-s.p.2eihtoujcocl...`, `83afe278b6a6bb3c-s.p.2bn3s6zvc0dy...`), and grid rule `.pswp--open { display:block }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.snap-showcase> — `Drops of Melancholy`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: var(--spacing)`) on desktop and Single-column vertical stack at `390px` viewport width with `16px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.flex> — `XA-23.4°`)**:
   - DOM & Selectors: Landmark `<section class="flex">` framing `XA-23.4°` and `After Dusk` (*"The Look From Silence"*) with `#fff` surface cards, `#4f4f4f` accents, and `.pswp__bg { will-change:opacity;transform:translateZ(0) }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.flex> — `XA-23.4°`)` uses `.25rem`, `3px`, `var(--radius-lg)`, `var(--radius-md)` radii, `#4f4f4f` highlights, and assets (m2ak1cq3.api.sanity.io, 6ab71d031fe7ae3b-s.p.141jscyq52bj..., 80bb744e92754df7-s.p.2eihtoujcocl...).
5. **Colophon & Global Directory Footer (<footer.relative> — `https://www.andriimur.com/`)**:
   - DOM & Selectors: Landmark `<footer class="relative bottom-0">` anchoring `Andrii Mur` footer links (`About · Monochrome · Drops of Melancholy · XA-23.4° · After Dusk`), copy *"Monochrome Black and White singles"*, and `#a36100` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.relative> — `https://www.andriimur.com/`)` aligns to `40rem` extracted from `www-andriimur-com` stylesheet with `16px` lateral canvas padding with `var(--spacing)` grid gap and attributes (data-theme="dark", data-precedence="next", data-precedence="next").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Drops of Melancholy"*
- Copy Excerpt 2: *"Fulfilling Emptiness"*
- Copy Excerpt 3: *"The Look From Silence"*
- Copy Excerpt 4: *"Monochrome Black and White singles"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,.22,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`
- **Extracted Stylesheet Rules (`www-andriimur-com`)**:
- `.pswp img { max-width:none }`
- `.pswp--open { display:block }`
- `.pswp__bg { will-change:opacity;transform:translateZ(0) }`
- `.pswp__scroll-wrap { overflow:hidden }`
- `.pswp__zoom-wrap { width:100%;height:100%;position:absolute;top:0;left:0 }`
- **Per-Selector Transition Rules**:
- **Selector `.pswp .pswp__hide-on-close`**: `transition: opacity var(--pswp-transition-duration) cubic-bezier(.4, 0, .2...` extracted from `www-andriimur-com` stylesheet.
- **Selector `.pswp__button:focus`**: `transition: none` extracted from `www-andriimur-com` stylesheet.
- **Selector `.pswp__preloader .pswp__icn`**: `transition: opacity .2s linear` extracted from `www-andriimur-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.22,1)`)**: Governs interactive state transitions across `<header.sticky>` and `<section.snap-showcase>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<section.dark>` and `<section.snap-showcase>` interactive targets.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-andriimur-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
