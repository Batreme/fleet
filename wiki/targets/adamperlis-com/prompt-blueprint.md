---
title: "UI Prompt Blueprint: adamperlis-com"
date: 2026-11-15
target: "adamperlis-com"
status: analyzed
capture: dom
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#161615`)"
---

# UI Design System & Master Generation Blueprint: adamperlis-com

> **Adam Perlis — I design and build apps** (https://adamperlis.com) — Founder of Academy, formerly Head of Design at TIME and Head of UX at AKQA. I help founders and teams design, build and ship their apps.

![Desktop Viewport Capture](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Adam Perlis — I design and build apps** (`https://adamperlis.com`). Founder of Academy, formerly Head of Design at TIME and Head of UX at AKQA. I help founders and teams design, build and ship their apps.
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#161615`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--color-black)` in `:root`) paired with `#fff` primary typography and `#161615` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Geist Mono Variable` for display copy (`Hello, I'm Adam. I design and build `) with `Inter Variable` and `Geist Mono Variable`.
  - **Calibrated Spatial Grid & Motion**: Combines `88rem` container bounds (`gap: var(--spacing)`, padding `var(--spacing)`) with `cubic-bezier(.4,0,1,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `88rem` extracted from `adamperlis-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `var(--spacing)` lateral canvas padding with `var(--spacing)` grid gap.
- **Border Radius Scale**: `4px`, `.25rem`, `var(--radius-2xl)`, `var(--radius-3xl)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 88rem`, `gap: var(--spacing)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--spacing)` horizontal padding.
- **Extracted CSS Media Queries**: `@media (width>=40rem)`, `@media (width>=48rem)`, `@media (width>=64rem)`, `@media (width>=80rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#f5f5f2` | `var(--color-wash)` in `:root` |
| **Interactive Accent / Highlight** | `#161615` | `var(--color-ink)` in `:root` |
| **Secondary / Muted Copy** | `#8a8a85` | `var(--color-muted)` in `:root` |
| **Structural Hairline Border** | `#c6c6c0` | `var(--color-faint)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-mono` | `"Geist Mono Variable", ui-monospace, "SF Mono", Menlo, monospace` | Typography / Scale Token |
| `--color-red-500` | `oklch(63.7% .237 25.331)` | Brand / Palette Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--container-sm` | `24rem` | Layout / Spatial Grid Token |
| `--container-md` | `28rem` | Layout / Spatial Grid Token |
| `--container-lg` | `32rem` | Layout / Spatial Grid Token |
| `--container-xl` | `36rem` | Layout / Spatial Grid Token |
| `--container-2xl` | `42rem` | Layout / Spatial Grid Token |
| `--container-3xl` | `48rem` | Layout / Spatial Grid Token |
| `--container-4xl` | `56rem` | Layout / Spatial Grid Token |
| `--container-5xl` | `64rem` | Layout / Spatial Grid Token |
| `--container-6xl` | `72rem` | Layout / Spatial Grid Token |
| `--text-xs` | `.75rem` | Typography Ink Token |
| `--text-xs--line-height` | `calc(1 / .75)` | Typography Ink Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Geist Mono Variable`.
- **Primary Body Stack**: `Inter Variable`.
- **Technical / Metadata Stack**: `Geist Mono Variable`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`.
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`.
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`.
- **Metadata & Navigation Labels**: CSS variables `--font-mono: "Geist Mono Variable", ui-monospace, "SF Mono", Menlo, monospace`, `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: .15s` extracted from `adamperlis-com` stylesheet.
- **Selector `.metal-glass`**: `transition: background-color .45s var(--ease-out-quart), backdrop-filter ....` extracted from `adamperlis-com` stylesheet.
- **Selector `.metal-halo`**: `transition: opacity .45s var(--ease-out-quart)` extracted from `adamperlis-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,1,1)`)**: Governs interactive state transitions across `<header.pointer-events-none>` and `<section.moment>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Adam Perlis — I design and build apps      │
│ ====================================================================== │
│ [ <header.pointer-events-n | 01 Home · 02 Work · 03 Skills · 04 Pla ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.wrap>                                       |   │
│ | H1: Hello, I'm Adam. I design and build apps.                    |   │
│ | Substrate: #000       | Ink: #fff       | Accent: #161615        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.moment>          ) max-w: 88rem          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | 07 How I built this          |  | I design and build apps.     | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: var(--) | │
│ | [<header.pointer-ev] -> [<section.wrap>] -> [<section.moment>] |     │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.wrap>         ) | https://adamperlis.com             │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.pointer-events-none> — `adamperlis-com`)**:
   - Landmark `<header class="pointer-events-none fixed">` hosting `Adam Perlis — I design and build app` navigation (`01 Home · 02 Work · 03 Skills · 04 Playground · 05 Services`), DOM attributes (`data-paper-shader`, `data-intro`, `data-sound-toggle`, `data-sound-choice="on"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.wrap> — `Hello, I'm Adam. I design and buil`)**:
   - Landmark `<section class="wrap relative">` presenting display lead `Hello, I'm Adam. I design and build apps.` and copy excerpt *"07 How I built this"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.moment> — `07 How I built this`)**:
   - Landmark `<section class="moment py-12">` rendering section `07 How I built this` with copy *"I design and build apps."*, asset references (`favicon.ico`, `favicon-32.png`, `apple-touch-icon.png`, `site.webmanifest`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.grid> — `I design and build apps.`)**:
   - Landmark `<section class="grid place-items-center">` framing `I design and build apps.` and `He built me with Claude Code, Codex and a little` (*"He built me with Claude Code, Codex and a little bit of love. Mos"*) with `#f5f5f2` surface cards, `#161615` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.wrap> — `https://adamperlis.com`)**:
   - Landmark `<footer class="wrap flex">` anchoring `Adam Perlis — I design and build` footer links (`01 Home · 02 Work · 03 Skills · 04 Playground · 05 Services`), copy *"# best with sound on"*, and `#c6c6c0` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: adamperlis-com (Adam Perlis — I design and build apps)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `adamperlis-com` (**Adam Perlis — I design and build apps** — `https://adamperlis.com`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#161615`).
- **Identity & Domain Context**: Founder of Academy, formerly Head of Design at TIME and Head of UX at AKQA. I help founders and teams design, build and ship their apps.
- **Primary Substrate**: `#000` (`var(--color-black)` in `:root`), **Primary Ink**: `#fff`, **Accent / Highlight**: `#161615`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--color-black)` in `:root`) paired with `#fff` primary typography and `#161615` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Geist Mono Variable` for display copy (`Hello, I'm Adam. I design and build `) with `Inter Variable` and `Geist Mono Variable`.
  - **Calibrated Spatial Grid & Motion**: Combines `88rem` container bounds (`gap: var(--spacing)`, padding `var(--spacing)`) with `cubic-bezier(.4,0,1,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `adamperlis-com` in your global stylesheet:

:root {
  /* Adam Perlis — I design and build apps (adamperlis-com) — Ground-Truth Extracted CSS Variables */
  --font-mono: "Geist Mono Variable", ui-monospace, "SF Mono", Menlo, monospace; /* Typography / Scale Token (adamperlis-com) */
  --color-red-500: oklch(63.7% .237 25.331); /* Brand / Palette Token (adamperlis-com) */
  --color-black: #000; /* Canvas / Surface Token (adamperlis-com) */
  --color-white: #fff; /* Canvas / Surface Token (adamperlis-com) */
  --spacing: .25rem; /* Layout / Spatial Grid Token (adamperlis-com) */
  --container-sm: 24rem; /* Layout / Spatial Grid Token (adamperlis-com) */
  --container-md: 28rem; /* Layout / Spatial Grid Token (adamperlis-com) */
  --container-lg: 32rem; /* Layout / Spatial Grid Token (adamperlis-com) */
  --container-xl: 36rem; /* Layout / Spatial Grid Token (adamperlis-com) */
  --container-2xl: 42rem; /* Layout / Spatial Grid Token (adamperlis-com) */
  --container-3xl: 48rem; /* Layout / Spatial Grid Token (adamperlis-com) */
  --container-4xl: 56rem; /* Layout / Spatial Grid Token (adamperlis-com) */
  --container-5xl: 64rem; /* Layout / Spatial Grid Token (adamperlis-com) */
  --container-6xl: 72rem; /* Layout / Spatial Grid Token (adamperlis-com) */
  --text-xs: .75rem; /* Typography Ink Token (adamperlis-com) */
  --text-xs--line-height: calc(1 / .75); /* Typography Ink Token (adamperlis-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#000` — grounded in `var(--color-black)` in `:root`
- **Primary Typography Ink**: `#fff` — grounded in `var(--color-white)` in `:root`
- **Elevated Surface / Card Substrate**: `#f5f5f2` — grounded in `var(--color-wash)` in `:root`
- **Interactive Accent / Highlight**: `#161615` — grounded in `var(--color-ink)` in `:root`
- **Secondary / Muted Copy**: `#8a8a85` — grounded in `var(--color-muted)` in `:root`
- **Structural Hairline Border**: `#c6c6c0` — grounded in `var(--color-faint)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `88rem` extracted from `adamperlis-com` stylesheet
- **Padding & Gutters**: `var(--spacing)` lateral canvas padding with `var(--spacing)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 88rem`, `gap: var(--spacing)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--spacing)` horizontal padding
- **Media Queries**: `@media (width>=40rem)`, `@media (width>=48rem)`, `@media (width>=64rem)`, `@media (width>=80rem)`
- **Corner Radii**: `4px`, `.25rem`, `var(--radius-2xl)`, `var(--radius-3xl)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Geist Mono Variable`
- **Body Font Stack**: `Inter Variable`
- **Monospace / Technical Font Stack**: `Geist Mono Variable`
- **H1 Display Rule**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`
- **H2 Section Rule**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`
- **Body Copy Rule**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`
- **Metadata & Index Rule**: CSS variables `--font-mono: "Geist Mono Variable", ui-monospace, "SF Mono", Menlo, monospace`, `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `adamperlis-com` (`Adam Perlis — I design and build apps`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.pointer-events-none> — `adamperlis-com`)**:
   - DOM & Selectors: Landmark `<header class="pointer-events-none fixed">` hosting `Adam Perlis — I design and build app` navigation (`01 Home · 02 Work · 03 Skills · 04 Playground · 05 Services`), DOM attributes (`data-paper-shader`, `data-intro`, `data-sound-toggle`, `data-sound-choice="on"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.pointer-events-none> — `adamperlis-com`)` (`adamperlis-com`) adapts across `@media (width>=40rem)`, `@media (width>=48rem)`, `@media (width>=64rem)`, `@media (width>=80rem)` with `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)` transitions and links `01 Home · 02 Work · 03 Skills · 04 Playground · 05 Services`.
2. **Hero Stage & Focal Lead (<section.wrap> — `Hello, I'm Adam. I design and buil`)**:
   - DOM & Selectors: Landmark `<section class="wrap relative">` presenting display lead `Hello, I'm Adam. I design and build apps.` and copy excerpt *"07 How I built this"* over `#000` canvas and `#fff` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#000` background with `#fff` headline `Hello, I'm Adam. I design and build apps.`.
3. **Primary Showcase & Content Grid (<section.moment> — `07 How I built this`)**:
   - DOM & Selectors: Landmark `<section class="moment py-12">` rendering section `07 How I built this` with copy *"I design and build apps."*, asset references (`favicon.ico`, `favicon-32.png`, `apple-touch-icon.png`, `site.webmanifest`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.moment> — `07 How I built this`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 88rem`, `gap: var(--spacing)`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--spacing)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.grid> — `I design and build apps.`)**:
   - DOM & Selectors: Landmark `<section class="grid place-items-center">` framing `I design and build apps.` and `He built me with Claude Code, Codex and a little` (*"He built me with Claude Code, Codex and a little bit of love. Mos"*) with `#f5f5f2` surface cards, `#161615` accents, and `strong { font-weight:bolder }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.grid> — `I design and build apps.`)` uses `4px`, `.25rem`, `var(--radius-2xl)`, `var(--radius-3xl)` radii, `#161615` highlights, and assets (favicon.ico, favicon-32.png, apple-touch-icon.png).
5. **Colophon & Global Directory Footer (<footer.wrap> — `https://adamperlis.com`)**:
   - DOM & Selectors: Landmark `<footer class="wrap flex">` anchoring `Adam Perlis — I design and build` footer links (`01 Home · 02 Work · 03 Skills · 04 Playground · 05 Services`), copy *"# best with sound on"*, and `#c6c6c0` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.wrap> — `https://adamperlis.com`)` aligns to `88rem` extracted from `adamperlis-com` stylesheet with `var(--spacing)` lateral canvas padding with `var(--spacing)` grid gap and attributes (data-paper-shader, data-intro, data-sound-toggle).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"07 How I built this"*
- Copy Excerpt 2: *"I design and build apps."*
- Copy Excerpt 3: *"He built me with Claude Code, Codex and a little bit of love. Mostly the first two."*
- Copy Excerpt 4: *"# best with sound on"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`
- **Extracted Stylesheet Rules (`adamperlis-com`)**:
- `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `strong { font-weight:bolder }`
- `small { font-size:80% }`
- `sup { vertical-align:baseline;font-size:75%;line-height:0;position:relative }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: .15s` extracted from `adamperlis-com` stylesheet.
- **Selector `.metal-glass`**: `transition: background-color .45s var(--ease-out-quart), backdrop-filter ....` extracted from `adamperlis-com` stylesheet.
- **Selector `.metal-halo`**: `transition: opacity .45s var(--ease-out-quart)` extracted from `adamperlis-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,1,1)`)**: Governs interactive state transitions across `<header.pointer-events-none>` and `<section.moment>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `adamperlis-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
