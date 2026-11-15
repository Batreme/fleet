---
title: "UI Prompt Blueprint: 11moissanstoit-com"
date: 2026-11-15
target: "[[overview|11moissanstoit-com]]"
status: analyzed
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#fee422` / `#92939d`)"
---

# UI Design System & Master Generation Blueprint: 11moissanstoit-com

> **11 mois sans toi(t), le tour du monde de Josué & Philippe** (https://11moissanstoit.com/) — Tour du monde autobiographique 2010-2011 de Josué & Philippe. 11 mois, des dizaines d'étapes, des milliers de tweets, de photos et de sou...

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **11 mois sans toi(t), le tour du monde de Josué & Philippe** (`https://11moissanstoit.com/`). Tour du monde autobiographique 2010-2011 de Josué & Philippe. 11 mois, des dizaines d'étapes, des milliers de tweets, de photos et de sou...
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#fee422` / `#92939d`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fee422` (`var(--primary-yellow)` in `:root`) paired with `#151723` primary typography and `#92939d` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Founders Grotesk X-Condensed` for display copy (`11 mois sans toi(t), le tour du mond`) with `Founders Grotesk` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `640px` container bounds (`gap: .25rem`, padding `.5rem`) with `cubic-bezier(.4,0,.6,1)` easing and Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `640px` extracted from `11moissanstoit-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `.5rem` lateral canvas padding with `.25rem` grid gap.
- **Border Radius Scale**: `.25rem`, `10px`, `12px`, `15px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 640px`, `gap: .25rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `.5rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:640px)`, `@media (min-width:768px)`, `@media (min-width:1024px)`, `@media (min-width:1280px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fee422` | `var(--primary-yellow)` in `:root` |
| **Primary Typography Ink** | `#151723` | `var(--dark-blue)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fff` | `var(--white-clear)` in `:root` |
| **Interactive Accent / Highlight** | `#92939d` | `var(--medium-blue-grey)` in `:root` |
| **Secondary / Muted Copy** | `#e8edf3` | `var(--hyper-light-blue-grey)` in `:root` |
| **Structural Hairline Border** | `#d1c658` | `var(--brown-yellow-bright)` in `:root` |
| **Variable Token (`--blue-notif`)** | `#3acfe1` | `var(--blue-notif)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--primary-yellow` | `#fee422` | Brand / Palette Token |
| `--dark-blue` | `#151723` | Canvas / Surface Token |
| `--white-clear` | `#fff` | Canvas / Surface Token |
| `--medium-blue-grey` | `#92939d` | Color / Atmospheric Token |
| `--hyper-light-blue-grey` | `#e8edf3` | Canvas / Surface Token |
| `--brown-yellow-bright` | `#d1c658` | Color / Atmospheric Token |
| `--blue-notif` | `#3acfe1` | Color / Atmospheric Token |
| `--background` | `#fee422` | Canvas / Surface Token |
| `--foreground` | `#151723` | Typography Ink Token |
| `--tw-border-spacing-x` | `0` | Layout / Spatial Grid Token |
| `--tw-border-spacing-y` | `0` | Layout / Spatial Grid Token |
| `--tw-translate-x` | `0` | Design System Custom Token |
| `--tw-translate-y` | `0` | Design System Custom Token |
| `--tw-rotate` | `0` | Design System Custom Token |
| `--11moissanstoit-c-bg` | `#fee422` | Canvas Substrate (from `var(--primary-yellow)` in `:root`) |
| `--11moissanstoit-c-ink` | `#151723` | Primary Typography Ink (stylesheet-derived) |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Founders Grotesk X-Condensed`.
- **Primary Body Stack**: `Founders Grotesk`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `14px`).
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `14px`).
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `14px`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `14px`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.4,0,1,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.transition`**: `transition: .15s` extracted from `11moissanstoit-com` stylesheet.
- **Selector `opacity\]`**: `transition: .15s` extracted from `11moissanstoit-com` stylesheet.
- **Selector `transform\]`**: `transition: .15s` extracted from `11moissanstoit-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.6,1)`)**: Governs interactive state transitions across `<header.h-full>` and `<section.font-condensed>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — 11 mois sans toi(t), le tour du monde de J │
│ ====================================================================== │
│ [ <header.h-full>          | MapLibre · EOxCloudless 2024 · CC BY-N ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.relative>                                   |   │
│ | H1: 11 mois sans toi(t), le tour du monde de Josué &             |   │
│ | Substrate: #fee422    | Ink: #151723    | Accent: #92939d        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.font-condensed>  ) max-w: 640px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Featured Work & Interactive  |  | Technical Architecture & Nar | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: .25rem) | │
│ | [<header.h-full>] -> [<section.relative>] -> [<section.font-cond] |  │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.inset-0>      ) | https://11moissanstoit.com/        │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.h-full> — `11moissanstoit-com`)**:
   - Landmark `<header class="h-full">` hosting `11 mois sans toi(t), le tour du mond` navigation (`MapLibre · EOxCloudless 2024 · CC BY-NC-SA · OpenFreeMap · © OpenMapTiles`), DOM attributes (`data-precedence="next"`, `data-sdkn="@vercel/analytics/next"`, `data-sdkv="2.0.1"`, `data-disable-auto-track="1"`), and stylesheet rule `after { box-sizing:border-box;border:0 solid e5e7eb }`.
2. **Hero Stage & Focal Lead (<section.relative> — `11 mois sans toi(t), le tour du mo`)**:
   - Landmark `<section class="relative font-condensed">` presenting display lead `11 mois sans toi(t), le tour du monde de Josué &` and copy excerpt *"October 2010. Philippe and Josué , two childhood friends, make th"* over `#fee422` canvas and `#151723` ink.
3. **Primary Showcase & Content Grid (<section.font-condensed> — `Featured Work & Interactive Showca`)**:
   - Landmark `<section class="font-condensed font-medium">` rendering section `Featured Work & Interactive Showcase` with copy *"a journey told in real time through their digital footprints, on "*, asset references (`logo-vecto.svg`, `photoLogo_11moissanstoi.png`, `2_er3-xpipny2.css`, `3cwyw8ne2vg7_.js`), and grid rule `body { line-height:inherit;margin:0 }`.
4. **Interactive Detail & Feature Matrix (<section.relative> — `Technical Architecture & Narrative`)**:
   - Landmark `<section class="relative font-condensed">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"15 years later, for the anniversary of our return (August 24, 201"*) with `#fff` surface cards, `#92939d` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.inset-0> — `https://11moissanstoit.com/`)**:
   - Landmark `<footer class="inset-0">` anchoring `11 mois sans toi(t), le tour du ` footer links (`MapLibre · EOxCloudless 2024 · CC BY-NC-SA · OpenFreeMap · © OpenMapTiles`), copy *"Everything that follows was written live, in 2010 and 2011, "*, and `#d1c658` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: 11moissanstoit-com (11 mois sans toi(t), le tour du monde de Josué & Philippe)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `11moissanstoit-com` (**11 mois sans toi(t), le tour du monde de Josué & Philippe** — `https://11moissanstoit.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fee422` / `#92939d`).
- **Identity & Domain Context**: Tour du monde autobiographique 2010-2011 de Josué & Philippe. 11 mois, des dizaines d'étapes, des milliers de tweets, de photos et de sou...
- **Primary Substrate**: `#fee422` (`var(--primary-yellow)` in `:root`), **Primary Ink**: `#151723`, **Accent / Highlight**: `#92939d`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fee422` (`var(--primary-yellow)` in `:root`) paired with `#151723` primary typography and `#92939d` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Founders Grotesk X-Condensed` for display copy (`11 mois sans toi(t), le tour du mond`) with `Founders Grotesk` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `640px` container bounds (`gap: .25rem`, padding `.5rem`) with `cubic-bezier(.4,0,.6,1)` easing and Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `11moissanstoit-com` in your global stylesheet:

:root {
  /* 11 mois sans toi(t), le tour du monde de Josué & Philippe (11moissanstoit-com) — Ground-Truth Extracted CSS Variables */
  --primary-yellow: #fee422; /* Brand / Palette Token (11moissanstoit-com) */
  --dark-blue: #151723; /* Canvas / Surface Token (11moissanstoit-com) */
  --white-clear: #fff; /* Canvas / Surface Token (11moissanstoit-com) */
  --medium-blue-grey: #92939d; /* Color / Atmospheric Token (11moissanstoit-com) */
  --hyper-light-blue-grey: #e8edf3; /* Canvas / Surface Token (11moissanstoit-com) */
  --brown-yellow-bright: #d1c658; /* Color / Atmospheric Token (11moissanstoit-com) */
  --blue-notif: #3acfe1; /* Color / Atmospheric Token (11moissanstoit-com) */
  --background: #fee422; /* Canvas / Surface Token (11moissanstoit-com) */
  --foreground: #151723; /* Typography Ink Token (11moissanstoit-com) */
  --tw-border-spacing-x: 0; /* Layout / Spatial Grid Token (11moissanstoit-com) */
  --tw-border-spacing-y: 0; /* Layout / Spatial Grid Token (11moissanstoit-com) */
  --tw-translate-x: 0; /* Design System Custom Token (11moissanstoit-com) */
  --tw-translate-y: 0; /* Design System Custom Token (11moissanstoit-com) */
  --tw-rotate: 0; /* Design System Custom Token (11moissanstoit-com) */
  --11moissanstoit-c-bg: #fee422; /* Canvas Substrate (from `var(--primary-yellow)` in `:root`) (11moissanstoit-com) */
  --11moissanstoit-c-ink: #151723; /* Primary Typography Ink (stylesheet-derived) (11moissanstoit-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#fee422` — grounded in `var(--primary-yellow)` in `:root`
- **Primary Typography Ink**: `#151723` — grounded in `var(--dark-blue)` in `:root`
- **Elevated Surface / Card Substrate**: `#fff` — grounded in `var(--white-clear)` in `:root`
- **Interactive Accent / Highlight**: `#92939d` — grounded in `var(--medium-blue-grey)` in `:root`
- **Secondary / Muted Copy**: `#e8edf3` — grounded in `var(--hyper-light-blue-grey)` in `:root`
- **Structural Hairline Border**: `#d1c658` — grounded in `var(--brown-yellow-bright)` in `:root`
- **Variable Token (`--blue-notif`)**: `#3acfe1` — grounded in `var(--blue-notif)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `640px` extracted from `11moissanstoit-com` stylesheet
- **Padding & Gutters**: `.5rem` lateral canvas padding with `.25rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 640px`, `gap: .25rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `.5rem` horizontal padding
- **Media Queries**: `@media (min-width:640px)`, `@media (min-width:768px)`, `@media (min-width:1024px)`, `@media (min-width:1280px)`
- **Corner Radii**: `.25rem`, `10px`, `12px`, `15px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Founders Grotesk X-Condensed`
- **Body Font Stack**: `Founders Grotesk`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `14px`)
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `14px`)
- **Body Copy Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `14px`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `14px`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `11moissanstoit-com` (`11 mois sans toi(t), le tour du monde de Josué & Philippe`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.h-full> — `11moissanstoit-com`)**:
   - DOM & Selectors: Landmark `<header class="h-full">` hosting `11 mois sans toi(t), le tour du mond` navigation (`MapLibre · EOxCloudless 2024 · CC BY-NC-SA · OpenFreeMap · © OpenMapTiles`), DOM attributes (`data-precedence="next"`, `data-sdkn="@vercel/analytics/next"`, `data-sdkv="2.0.1"`, `data-disable-auto-track="1"`), and stylesheet rule `after { box-sizing:border-box;border:0 solid e5e7eb }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.h-full> — `11moissanstoit-com`)` (`11moissanstoit-com`) adapts across `@media (min-width:640px)`, `@media (min-width:768px)`, `@media (min-width:1024px)`, `@media (min-width:1280px)` with `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.4,0,1,1)` transitions and links `MapLibre · EOxCloudless 2024 · CC BY-NC-SA · OpenFreeMap · © OpenMapTiles`.
2. **Hero Stage & Focal Lead (<section.relative> — `11 mois sans toi(t), le tour du mo`)**:
   - DOM & Selectors: Landmark `<section class="relative font-condensed">` presenting display lead `11 mois sans toi(t), le tour du monde de Josué &` and copy excerpt *"October 2010. Philippe and Josué , two childhood friends, make th"* over `#fee422` canvas and `#151723` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#fee422` background with `#151723` headline `11 mois sans toi(t), le tour du monde de Josué &`.
3. **Primary Showcase & Content Grid (<section.font-condensed> — `Featured Work & Interactive Showca`)**:
   - DOM & Selectors: Landmark `<section class="font-condensed font-medium">` rendering section `Featured Work & Interactive Showcase` with copy *"a journey told in real time through their digital footprints, on "*, asset references (`logo-vecto.svg`, `photoLogo_11moissanstoi.png`, `2_er3-xpipny2.css`, `3cwyw8ne2vg7_.js`), and grid rule `body { line-height:inherit;margin:0 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.font-condensed> — `Featured Work & Interactive Showca`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 640px`, `gap: .25rem`) on desktop and Single-column vertical stack at `390px` viewport width with `.5rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.relative> — `Technical Architecture & Narrative`)**:
   - DOM & Selectors: Landmark `<section class="relative font-condensed">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"15 years later, for the anniversary of our return (August 24, 201"*) with `#fff` surface cards, `#92939d` accents, and `strong { font-weight:bolder }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.relative> — `Technical Architecture & Narrative`)` uses `.25rem`, `10px`, `12px`, `15px` radii, `#92939d` highlights, and assets (logo-vecto.svg, photoLogo_11moissanstoi.png, 2_er3-xpipny2.css).
5. **Colophon & Global Directory Footer (<footer.inset-0> — `https://11moissanstoit.com/`)**:
   - DOM & Selectors: Landmark `<footer class="inset-0">` anchoring `11 mois sans toi(t), le tour du ` footer links (`MapLibre · EOxCloudless 2024 · CC BY-NC-SA · OpenFreeMap · © OpenMapTiles`), copy *"Everything that follows was written live, in 2010 and 2011, "*, and `#d1c658` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.inset-0> — `https://11moissanstoit.com/`)` aligns to `640px` extracted from `11moissanstoit-com` stylesheet with `.5rem` lateral canvas padding with `.25rem` grid gap and attributes (data-precedence="next", data-sdkn="@vercel/analytics/next", data-sdkv="2.0.1").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"October 2010. Philippe and Josué , two childhood friends, make their childhood dre..."*
- Copy Excerpt 2: *"a journey told in real time through their digital footprints, on a flash website:..."*
- Copy Excerpt 3: *"15 years later, for the anniversary of our return (August 24, 2011), this site is..."*
- Copy Excerpt 4: *"Everything that follows was written live, in 2010 and 2011, with the eyes, the wor..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.4,0,1,1)`
- **Extracted Stylesheet Rules (`11moissanstoit-com`)**:
- `after { box-sizing:border-box;border:0 solid e5e7eb }`
- `body { line-height:inherit;margin:0 }`
- `strong { font-weight:bolder }`
- `small { font-size:80% }`
- `sup { vertical-align:baseline;font-size:75%;line-height:0;position:relative }`
- **Per-Selector Transition Rules**:
- **Selector `.transition`**: `transition: .15s` extracted from `11moissanstoit-com` stylesheet.
- **Selector `opacity\]`**: `transition: .15s` extracted from `11moissanstoit-com` stylesheet.
- **Selector `transform\]`**: `transition: .15s` extracted from `11moissanstoit-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.6,1)`)**: Governs interactive state transitions across `<header.h-full>` and `<section.font-condensed>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `11moissanstoit-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
