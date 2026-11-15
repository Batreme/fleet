---
title: "UI Prompt Blueprint: karma-tracks-com"
date: 2026-11-15
target: "[[overview|karma-tracks-com]]"
status: analyzed
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#ffcaca` / `#fb2c36`)"
---

# UI Design System & Master Generation Blueprint: karma-tracks-com

> **karma tracks** (https://karma-tracks.com/) — the tracks of one music producer from the last ten years, every one of them drawn as a card.

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/karma-tracks-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **karma tracks** (`https://karma-tracks.com/`). the tracks of one music producer from the last ten years, every one of them drawn as a card.
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#ffcaca` / `#fb2c36`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#ffcaca` (`var(--color-red-200)` in `:root`) paired with `#fb2c36` primary typography and `#fb2c36` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Gloock` for display copy (`karma tracks`) with `Gloock Fallback` and `Space Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `40rem` container bounds (`gap: 4rem`, padding `4px`) with `cubic-bezier(0,0,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/karma-tracks-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `40rem` extracted from `karma-tracks-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `4px` lateral canvas padding with `4rem` grid gap.
- **Border Radius Scale**: `.25rem`, `var(--radius-2xl)`, `var(--radius-lg)`, `var(--radius-md)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: 4rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `4px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#ffcaca` | `var(--color-red-200)` in `:root` |
| **Primary Typography Ink** | `#ffa3a3` | `var(--color-red-300)` in `:root` |
| **Elevated Surface / Card Substrate** | `#ff6568` | `var(--color-red-400)` in `:root` |
| **Interactive Accent / Highlight** | `#fb2c36` | `var(--color-red-500)` in `:root` |
| **Secondary / Muted Copy** | `#fee685` | `var(--color-amber-200)` in `:root` |
| **Structural Hairline Border** | `#ffd236` | `var(--color-amber-300)` in `:root` |
| **Variable Token (`--color-amber-400`)** | `#fcbb00` | `var(--color-amber-400)` in `:root` |
| **Variable Token (`--color-amber-500`)** | `#f99c00` | `var(--color-amber-500)` in `:root` |
| **Variable Token (`--color-green-200`)** | `#b9f8cf` | `var(--color-green-200)` in `:root` |
| **Variable Token (`--color-green-500`)** | `#00c758` | `var(--color-green-500)` in `:root` |
| **Variable Token (`--color-emerald-200`)** | `#a4f4cf` | `var(--color-emerald-200)` in `:root` |
| **Variable Token (`--color-emerald-400`)** | `#00d294` | `var(--color-emerald-400)` in `:root` |
| **Variable Token (`--color-emerald-500`)** | `#00bb7f` | `var(--color-emerald-500)` in `:root` |
| **Variable Token (`--color-sky-200`)** | `#b8e6fe` | `var(--color-sky-200)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-gloock` | `"Gloock", "Gloock Fallback"` | Typography / Scale Token |
| `--font-space-mono` | `"Space Mono", "Space Mono Fallback"` | Typography / Scale Token |
| `--color-red-200` | `#ffcaca` | Brand / Palette Token |
| `--color-red-300` | `#ffa3a3` | Brand / Palette Token |
| `--color-red-400` | `#ff6568` | Brand / Palette Token |
| `--color-red-500` | `#fb2c36` | Brand / Palette Token |
| `--color-amber-200` | `#fee685` | Brand / Palette Token |
| `--color-amber-300` | `#ffd236` | Brand / Palette Token |
| `--color-amber-400` | `#fcbb00` | Brand / Palette Token |
| `--color-amber-500` | `#f99c00` | Brand / Palette Token |
| `--color-green-200` | `#b9f8cf` | Brand / Palette Token |
| `--color-green-500` | `#00c758` | Brand / Palette Token |
| `--color-emerald-200` | `#a4f4cf` | Brand / Palette Token |
| `--color-emerald-400` | `#00d294` | Brand / Palette Token |
| `--color-emerald-500` | `#00bb7f` | Brand / Palette Token |
| `--color-sky-200` | `#b8e6fe` | Brand / Palette Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Gloock`.
- **Primary Body Stack**: `Gloock Fallback`.
- **Technical / Metadata Stack**: `Space Mono`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--font-display: var(--font-gloock), Georgia, serif`.
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`.
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`.
- **Metadata & Navigation Labels**: CSS variables `--font-space-mono: "Space Mono", "Space Mono Fallback"`, `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.2,.8,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: .15s` extracted from `karma-tracks-com` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `karma-tracks-com` stylesheet.
- **Selector `.transition-all`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `karma-tracks-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<header.h-full>` and `<section.lenis>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — karma tracks                               │
│ ====================================================================== │
│ [ <header.h-full>          | Overview · Index · Archive · About · C ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.antialiased>                                |   │
│ | H1: karma tracks                                                 |   │
│ | Substrate: #ffcaca    | Ink: #fb2c36    | Accent: #fb2c36        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.lenis>           ) max-w: 40rem          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Featured Work & Interactive  |  | Technical Architecture & Nar | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 4rem  ) | │
│ | [<header.h-full>] -> [<section.antialias] -> [<section.lenis>] |     │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.has-custom-cur) | https://karma-tracks.com/          │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.h-full> — `karma-tracks-com`)**:
   - Landmark `<header class="h-full">` hosting `karma tracks` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-engine="three.js r184"`, `data-lenis-prevent="true"`, `data-inspect-panel="true"`), and stylesheet rule `oock_a2ed214b-module__p916ta__cla... { font-family:Gloock,Gloock Fallback;font-style:normal;font-weight:400 }`.
2. **Hero Stage & Focal Lead (<section.antialiased> — `karma tracks`)**:
   - Landmark `<section class="antialiased">` presenting display lead `karma tracks` and copy excerpt *"these are my tracks from the last ten years. every one of them is"* over `#ffcaca` canvas and `#fb2c36` ink.
3. **Primary Showcase & Content Grid (<section.lenis> — `Featured Work & Interactive Showca`)**:
   - Landmark `<section class="lenis">` rendering section `Featured Work & Interactive Showcase` with copy *"by conversation telegram instagram"*, asset references (`8d05cfa5faa8406c-s.p.0kbulo~7o8gi...`, `c5bca4b73401f535-s.p.0ld0~zebno3h...`, `dc0d9adbac686440-s.p.0~z396rbj0t4...`, `16_jj7v3ye6b5.css`), and grid rule `loock_a2ed214b-module__p916ta__va... { --font-gloock:"Gloock", "Gloock Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.has-rail> — `Technical Architecture & Narrative`)**:
   - Landmark `<section class="has-rail">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"telegram instagram"*) with `#ff6568` surface cards, `#fb2c36` accents, and `mono_754f223c-module__vnF5cq__cla... { font-family:Space Mono,Space Mono Fallback;font-style:normal }`.
5. **Colophon & Global Directory Footer (<footer.has-custom-cursor> — `https://karma-tracks.com/`)**:
   - Landmark `<footer class="has-custom-cursor">` anchoring `karma tracks` footer links (`Overview · Index · Archive · About · Contact`), copy *"browse all 166 tracks"*, and `#ffd236` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: karma-tracks-com (karma tracks)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `karma-tracks-com` (**karma tracks** — `https://karma-tracks.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffcaca` / `#fb2c36`).
- **Identity & Domain Context**: the tracks of one music producer from the last ten years, every one of them drawn as a card.
- **Primary Substrate**: `#ffcaca` (`var(--color-red-200)` in `:root`), **Primary Ink**: `#fb2c36`, **Accent / Highlight**: `#fb2c36`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#ffcaca` (`var(--color-red-200)` in `:root`) paired with `#fb2c36` primary typography and `#fb2c36` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Gloock` for display copy (`karma tracks`) with `Gloock Fallback` and `Space Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `40rem` container bounds (`gap: 4rem`, padding `4px`) with `cubic-bezier(0,0,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `karma-tracks-com` in your global stylesheet:

:root {
  /* karma tracks (karma-tracks-com) — Ground-Truth Extracted CSS Variables */
  --font-gloock: "Gloock", "Gloock Fallback"; /* Typography / Scale Token (karma-tracks-com) */
  --font-space-mono: "Space Mono", "Space Mono Fallback"; /* Typography / Scale Token (karma-tracks-com) */
  --color-red-200: #ffcaca; /* Brand / Palette Token (karma-tracks-com) */
  --color-red-300: #ffa3a3; /* Brand / Palette Token (karma-tracks-com) */
  --color-red-400: #ff6568; /* Brand / Palette Token (karma-tracks-com) */
  --color-red-500: #fb2c36; /* Brand / Palette Token (karma-tracks-com) */
  --color-amber-200: #fee685; /* Brand / Palette Token (karma-tracks-com) */
  --color-amber-300: #ffd236; /* Brand / Palette Token (karma-tracks-com) */
  --color-amber-400: #fcbb00; /* Brand / Palette Token (karma-tracks-com) */
  --color-amber-500: #f99c00; /* Brand / Palette Token (karma-tracks-com) */
  --color-green-200: #b9f8cf; /* Brand / Palette Token (karma-tracks-com) */
  --color-green-500: #00c758; /* Brand / Palette Token (karma-tracks-com) */
  --color-emerald-200: #a4f4cf; /* Brand / Palette Token (karma-tracks-com) */
  --color-emerald-400: #00d294; /* Brand / Palette Token (karma-tracks-com) */
  --color-emerald-500: #00bb7f; /* Brand / Palette Token (karma-tracks-com) */
  --color-sky-200: #b8e6fe; /* Brand / Palette Token (karma-tracks-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ffcaca` — grounded in `var(--color-red-200)` in `:root`
- **Primary Typography Ink**: `#ffa3a3` — grounded in `var(--color-red-300)` in `:root`
- **Elevated Surface / Card Substrate**: `#ff6568` — grounded in `var(--color-red-400)` in `:root`
- **Interactive Accent / Highlight**: `#fb2c36` — grounded in `var(--color-red-500)` in `:root`
- **Secondary / Muted Copy**: `#fee685` — grounded in `var(--color-amber-200)` in `:root`
- **Structural Hairline Border**: `#ffd236` — grounded in `var(--color-amber-300)` in `:root`
- **Variable Token (`--color-amber-400`)**: `#fcbb00` — grounded in `var(--color-amber-400)` in `:root`
- **Variable Token (`--color-amber-500`)**: `#f99c00` — grounded in `var(--color-amber-500)` in `:root`
- **Variable Token (`--color-green-200`)**: `#b9f8cf` — grounded in `var(--color-green-200)` in `:root`
- **Variable Token (`--color-green-500`)**: `#00c758` — grounded in `var(--color-green-500)` in `:root`
- **Variable Token (`--color-emerald-200`)**: `#a4f4cf` — grounded in `var(--color-emerald-200)` in `:root`
- **Variable Token (`--color-emerald-400`)**: `#00d294` — grounded in `var(--color-emerald-400)` in `:root`
- **Variable Token (`--color-emerald-500`)**: `#00bb7f` — grounded in `var(--color-emerald-500)` in `:root`
- **Variable Token (`--color-sky-200`)**: `#b8e6fe` — grounded in `var(--color-sky-200)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `40rem` extracted from `karma-tracks-com` stylesheet
- **Padding & Gutters**: `4px` lateral canvas padding with `4rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: 4rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `4px` horizontal padding
- **Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)`
- **Corner Radii**: `.25rem`, `var(--radius-2xl)`, `var(--radius-lg)`, `var(--radius-md)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Gloock`
- **Body Font Stack**: `Gloock Fallback`
- **Monospace / Technical Font Stack**: `Space Mono`
- **H1 Display Rule**: CSS variables `--font-display: var(--font-gloock), Georgia, serif`
- **H2 Section Rule**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`
- **Body Copy Rule**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`
- **Metadata & Index Rule**: CSS variables `--font-space-mono: "Space Mono", "Space Mono Fallback"`, `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `karma-tracks-com` (`karma tracks`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.h-full> — `karma-tracks-com`)**:
   - DOM & Selectors: Landmark `<header class="h-full">` hosting `karma tracks` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-engine="three.js r184"`, `data-lenis-prevent="true"`, `data-inspect-panel="true"`), and stylesheet rule `oock_a2ed214b-module__p916ta__cla... { font-family:Gloock,Gloock Fallback;font-style:normal;font-weight:400 }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.h-full> — `karma-tracks-com`)` (`karma-tracks-com`) adapts across `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)` with `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.2,.8,.2,1)` transitions and links `Overview · Index · Archive · About · Contact`.
2. **Hero Stage & Focal Lead (<section.antialiased> — `karma tracks`)**:
   - DOM & Selectors: Landmark `<section class="antialiased">` presenting display lead `karma tracks` and copy excerpt *"these are my tracks from the last ten years. every one of them is"* over `#ffcaca` canvas and `#fb2c36` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#ffcaca` background with `#fb2c36` headline `karma tracks`.
3. **Primary Showcase & Content Grid (<section.lenis> — `Featured Work & Interactive Showca`)**:
   - DOM & Selectors: Landmark `<section class="lenis">` rendering section `Featured Work & Interactive Showcase` with copy *"by conversation telegram instagram"*, asset references (`8d05cfa5faa8406c-s.p.0kbulo~7o8gi...`, `c5bca4b73401f535-s.p.0ld0~zebno3h...`, `dc0d9adbac686440-s.p.0~z396rbj0t4...`, `16_jj7v3ye6b5.css`), and grid rule `loock_a2ed214b-module__p916ta__va... { --font-gloock:"Gloock", "Gloock Fallback" }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.lenis> — `Featured Work & Interactive Showca`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: 4rem`) on desktop and Single-column vertical stack at `390px` viewport width with `4px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.has-rail> — `Technical Architecture & Narrative`)**:
   - DOM & Selectors: Landmark `<section class="has-rail">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"telegram instagram"*) with `#ff6568` surface cards, `#fb2c36` accents, and `mono_754f223c-module__vnF5cq__cla... { font-family:Space Mono,Space Mono Fallback;font-style:normal }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.has-rail> — `Technical Architecture & Narrative`)` uses `.25rem`, `var(--radius-2xl)`, `var(--radius-lg)`, `var(--radius-md)` radii, `#fb2c36` highlights, and assets (8d05cfa5faa8406c-s.p.0kbulo~7o8gi..., c5bca4b73401f535-s.p.0ld0~zebno3h..., dc0d9adbac686440-s.p.0~z396rbj0t4...).
5. **Colophon & Global Directory Footer (<footer.has-custom-cursor> — `https://karma-tracks.com/`)**:
   - DOM & Selectors: Landmark `<footer class="has-custom-cursor">` anchoring `karma tracks` footer links (`Overview · Index · Archive · About · Contact`), copy *"browse all 166 tracks"*, and `#ffd236` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.has-custom-cursor> — `https://karma-tracks.com/`)` aligns to `40rem` extracted from `karma-tracks-com` stylesheet with `4px` lateral canvas padding with `4rem` grid gap and attributes (data-precedence="next", data-engine="three.js r184", data-lenis-prevent="true").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"these are my tracks from the last ten years. every one of them is a card, drawn fr..."*
- Copy Excerpt 2: *"by conversation telegram instagram"*
- Copy Excerpt 3: *"telegram instagram"*
- Copy Excerpt 4: *"browse all 166 tracks"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.2,.8,.2,1)`
- **Extracted Stylesheet Rules (`karma-tracks-com`)**:
- `oock_a2ed214b-module__p916ta__cla... { font-family:Gloock,Gloock Fallback;font-style:normal;font-weight:400 }`
- `loock_a2ed214b-module__p916ta__va... { --font-gloock:"Gloock", "Gloock Fallback" }`
- `mono_754f223c-module__vnF5cq__cla... { font-family:Space Mono,Space Mono Fallback;font-style:normal }`
- `mono_754f223c-module__vnF5cq__var... { --font-space-mono:"Space Mono", "Space Mono Fallback" }`
- `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: .15s` extracted from `karma-tracks-com` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `karma-tracks-com` stylesheet.
- **Selector `.transition-all`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `karma-tracks-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<header.h-full>` and `<section.lenis>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `karma-tracks-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
