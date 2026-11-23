---
title: "UI Prompt Blueprint: www-thelasttango-com"
date: 2026-11-23
captured_at: 2026-11-23
target: "www-thelasttango-com"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#030c1c` / `#0000ff`)"
---

# UI Design System & Master Generation Blueprint: www-thelasttango-com

> **The Last Tango / For the one who made us happy.** (https://www.thelasttango.com/) — An interactive tribute to Lionel Messi and the World Cup that brought millions of people together again. Every point, every goal, and eve...

![Desktop Viewport Capture (1440x900)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **The Last Tango / For the one who made us happy.** (`https://www.thelasttango.com/`). An interactive tribute to Lionel Messi and the World Cup that brought millions of people together again. Every point, every goal, and eve...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#030c1c` / `#0000ff`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#030c1c` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#f5f5f5` primary typography and `#0000ff` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Cormorant Garamond` for display copy (`The Last Tango / For the one who mad`) with `Cormorant Garamond` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `1920px` container bounds (`gap: var(--spacing-2)`, padding `var(--spacing-1)`) with `cubic-bezier(0,0,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x844)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×900px` (`assets/desktop.png`, single-viewport 100vh live capture (900px)), Mobile `390×844px` (`assets/mobile.png`, single-viewport 100vh live capture (844px)).
- **Master Container Bounds**: `1920px` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `var(--spacing-1)` lateral canvas padding with `var(--spacing-2)` grid gap.
- **Border Radius Scale**: `.25rem`, `var(--radius-2xl)`, `16px`, `var(--radius-lg)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1920px`, `gap: var(--spacing-2)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--spacing-1)` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:480px)`, `@media (min-width:640px)`, `@media (min-width:650px)`, `@media (min-width:768px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#030c1c` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#f5f5f5` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#000000` | `body { background-color: black }` (`#000000`) |
| **Interactive Accent / Highlight** | `#0000ff` | `.border-blue-600 { border-color: #0000ff }` |
| **Secondary / Muted Copy** | `#808080` | `.text-gray-600 { color: gray }` (`#808080`) |
| **Structural Hairline Border** | `#000000` | `.border-black { border-color: #000000 }` |
| **Variable Token (`--violet`)** | `#5021e9` | `var(--violet)` in `:root` |
| **Variable Token (`--dark`)** | `#17152f` | `var(--dark)` in `:root` |
| **Variable Token (`--white`)** | `#fefefe` | `var(--white)` in `:root` |
| **Variable Token (`--light`)** | `#eef2ff` | `var(--light)` in `:root` |
| **Variable Token (`--focus`)** | `#ddd4f9` | `var(--focus)` in `:root` |
| **Variable Token (`--disabled`)** | `#efefef` | `var(--disabled)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--violet` | `#5021e9` | Color / Atmospheric Token |
| `--dark` | `#17152f` | Canvas / Surface Token |
| `--white` | `#fefefe` | Canvas / Surface Token |
| `--light` | `#eef2ff` | Canvas / Surface Token |
| `--focus` | `#ddd4f9` | Color / Atmospheric Token |
| `--disabled` | `#efefef` | Color / Atmospheric Token |
| `--wrapper` | `100%` | Layout / Spatial Grid Token |
| `--max-w-wrapper` | `1680px` | Layout / Spatial Grid Token |
| `--grid-cols-space` | `28px` | Layout / Spatial Grid Token |
| `--safearea` | `48px` | Dimension / Scale Token |
| `--ctrl-desktop-max-w` | `1920px` | Layout / Spatial Grid Token |
| `--ctrl-tablet-max-w` | `100vw` | Layout / Spatial Grid Token |
| `--ctrl-mobile-max-w` | `100vw` | Layout / Spatial Grid Token |
| `--ctrl-desktop-max-h` | `100vh` | Dimension / Scale Token |
| `--ctrl-tablet-max-h` | `100vh` | Dimension / Scale Token |
| `--ctrl-mobile-max-h` | `90vh` | Dimension / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Cormorant Garamond`.
- **Primary Body Stack**: `Cormorant Garamond`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5/2.25)`, `--text-6xl: 3.75rem`.
- **Section Heading (`H2`)**: observed font-size ladder: `16px`, `80px`, `14px`, `1em`, `80%`.
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5/1)`.
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 14px`, `line-height: 21px`, `font-weight: 500`); CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1/.75)`, `--text-sm: .875rem`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.48,.04,.52,.96)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: .15s` extracted from `www-thelasttango-com` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `www-thelasttango-com` stylesheet.
- **Selector `box-shadow\]`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `www-thelasttango-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<header.z-100000>` and `<main.lenis-stopped>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — The Last Tango / For the one who made us h │
│ ====================================================================== │
│ [ <header.z-100000> (1440x64px)       | Esp                          ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <main.lenis> (w=1440px)                                | │
│ | H1: The Last Tango / For the one who made us happy.                | │
│ | Substrate: #030c1c | Ink: #f5f5f5 | Accent: #0000ff                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<main.lenis-stopped>) max-w: 1920px                 | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Featured Work & Interactive  |  | Technical Architecture & Nar | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<main.fonts-loaded>) — Global Directory & Co        | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.pointer-even) | https://www.thelasttango.com/        │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: var(--sp)   │
│ ====================================================================== │
│ [ HEADER BAR (<header.z-100000>       ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<main.lenis>) — 390px Vertical Lead                    | │
│ | H1: The Last Tango / For the one who made us happy.                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<main.lenis-stopped>) — 1-Col Stack                | │
│ | [ Item 1: Featured Work & Interactive Showcase                   ] | │
│ | [ Item 2: Technical Architecture & Narrative                     ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<main.fonts-loaded>) — 1-Col (Global Directory &)    | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.pointer-even) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.z-100000> — `www-thelasttango-com`)**:
   - Landmark `<header class="z-100000 fixed">` (`1440x64px`) hosting `The Last Tango / For the one who mad` navigation (`Esp`), DOM attributes (`data-loader-scroll-lock="true"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<main.lenis> — `The Last Tango / For the one who m`)**:
   - Landmark `<main class="lenis">` presenting display lead `The Last Tango / For the one who made us happy.` and copy excerpt *"0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9"* over `#030c1c` canvas and `#f5f5f5` ink.
3. **Primary Showcase & Content Grid (<main.lenis-stopped> — `Featured Work & Interactive Showca`)**:
   - Landmark `<main class="lenis-stopped">` rendering section `Featured Work & Interactive Showcase` with copy *"0 1 2 3 4 5 6 7 8 9"*, asset references (`187cmj4q350mm.css`, `0eqspdm2dt5_-.css`, `0kkv0xwvqoa86.css`, `14~g0x6k9zzx2.js`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<main.fonts-loaded> — `Technical Architecture & Narrative`)**:
   - Landmark `<main class="fonts-loaded">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Kansas City Stadium , June 17, 2026"*) with `#000000` surface cards, `#0000ff` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.pointer-events-auto> — `https://www.thelasttango.com/`)**:
   - Landmark `<footer class="pointer-events-auto">` anchoring `The Last Tango / For the one who` footer links (`Esp`), copy *"Every goal. Every record. Every moment that marked Messi 's "*, and `#000000` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-thelasttango-com (The Last Tango / For the one who made us happy.)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-thelasttango-com` (**The Last Tango / For the one who made us happy.** — `https://www.thelasttango.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#030c1c` / `#0000ff`).
- **Identity & Domain Context**: An interactive tribute to Lionel Messi and the World Cup that brought millions of people together again. Every point, every goal, and eve...
- **Primary Substrate**: `#030c1c` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#f5f5f5`, **Accent / Highlight**: `#0000ff`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#030c1c` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#f5f5f5` primary typography and `#0000ff` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Cormorant Garamond` for display copy (`The Last Tango / For the one who mad`) with `Cormorant Garamond` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `1920px` container bounds (`gap: var(--spacing-2)`, padding `var(--spacing-1)`) with `cubic-bezier(0,0,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-thelasttango-com` in your global stylesheet:

:root {
  /* The Last Tango / For the one who made us happy. (www-thelasttango-com) — Live-Grounded CSS Variables */
  --violet: #5021e9; /* Color / Atmospheric Token (www-thelasttango-com) */
  --dark: #17152f; /* Canvas / Surface Token (www-thelasttango-com) */
  --white: #fefefe; /* Canvas / Surface Token (www-thelasttango-com) */
  --light: #eef2ff; /* Canvas / Surface Token (www-thelasttango-com) */
  --focus: #ddd4f9; /* Color / Atmospheric Token (www-thelasttango-com) */
  --disabled: #efefef; /* Color / Atmospheric Token (www-thelasttango-com) */
  --wrapper: 100%; /* Layout / Spatial Grid Token (www-thelasttango-com) */
  --max-w-wrapper: 1680px; /* Layout / Spatial Grid Token (www-thelasttango-com) */
  --grid-cols-space: 28px; /* Layout / Spatial Grid Token (www-thelasttango-com) */
  --safearea: 48px; /* Dimension / Scale Token (www-thelasttango-com) */
  --ctrl-desktop-max-w: 1920px; /* Layout / Spatial Grid Token (www-thelasttango-com) */
  --ctrl-tablet-max-w: 100vw; /* Layout / Spatial Grid Token (www-thelasttango-com) */
  --ctrl-mobile-max-w: 100vw; /* Layout / Spatial Grid Token (www-thelasttango-com) */
  --ctrl-desktop-max-h: 100vh; /* Dimension / Scale Token (www-thelasttango-com) */
  --ctrl-tablet-max-h: 100vh; /* Dimension / Scale Token (www-thelasttango-com) */
  --ctrl-mobile-max-h: 90vh; /* Dimension / Scale Token (www-thelasttango-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#030c1c` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#f5f5f5` — grounded in live computed `main` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#000000` — grounded in `body { background-color: black }` (`#000000`)
- **Interactive Accent / Highlight**: `#0000ff` — grounded in `.border-blue-600 { border-color: #0000ff }`
- **Secondary / Muted Copy**: `#808080` — grounded in `.text-gray-600 { color: gray }` (`#808080`)
- **Structural Hairline Border**: `#000000` — grounded in `.border-black { border-color: #000000 }`
- **Variable Token (`--violet`)**: `#5021e9` — grounded in `var(--violet)` in `:root`
- **Variable Token (`--dark`)**: `#17152f` — grounded in `var(--dark)` in `:root`
- **Variable Token (`--white`)**: `#fefefe` — grounded in `var(--white)` in `:root`
- **Variable Token (`--light`)**: `#eef2ff` — grounded in `var(--light)` in `:root`
- **Variable Token (`--focus`)**: `#ddd4f9` — grounded in `var(--focus)` in `:root`
- **Variable Token (`--disabled`)**: `#efefef` — grounded in `var(--disabled)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×900px` (single-viewport 100vh live capture (900px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×844px` (single-viewport 100vh live capture (844px), `390px` standard mobile width).
- **Container Max-Width**: `1920px` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `var(--spacing-1)` lateral canvas padding with `var(--spacing-2)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1920px`, `gap: var(--spacing-2)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--spacing-1)` horizontal padding
- **Media Queries**: `@media (min-width:480px)`, `@media (min-width:640px)`, `@media (min-width:650px)`, `@media (min-width:768px)`
- **Corner Radii**: `.25rem`, `var(--radius-2xl)`, `16px`, `var(--radius-lg)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Cormorant Garamond`
- **Body Font Stack**: `Cormorant Garamond`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5/2.25)`, `--text-6xl: 3.75rem`
- **H2 Section Rule**: observed font-size ladder: `16px`, `80px`, `14px`, `1em`, `80%`
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5/1)`
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 14px`, `line-height: 21px`, `font-weight: 500`); CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1/.75)`, `--text-sm: .875rem`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-thelasttango-com` (`The Last Tango / For the one who made us happy.`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.z-100000> — `www-thelasttango-com`)**:
   - DOM & Selectors: Landmark `<header class="z-100000 fixed">` (`1440x64px`) hosting `The Last Tango / For the one who mad` navigation (`Esp`), DOM attributes (`data-loader-scroll-lock="true"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.z-100000> — `www-thelasttango-com`)` (`www-thelasttango-com`) adapts across `@media (min-width:480px)`, `@media (min-width:640px)`, `@media (min-width:650px)`, `@media (min-width:768px)` with `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.48,.04,.52,.96)` transitions and links `Esp`.
2. **Hero Stage & Focal Lead (<main.lenis> — `The Last Tango / For the one who m`)**:
   - DOM & Selectors: Landmark `<main class="lenis">` presenting display lead `The Last Tango / For the one who made us happy.` and copy excerpt *"0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9"* over `#030c1c` canvas and `#f5f5f5` ink.
   - Responsive Contract: Hero stage (`1440×900px` desktop / `390×844px` mobile) sets `#030c1c` background with `#f5f5f5` headline `The Last Tango / For the one who made us happy.`.
3. **Primary Showcase & Content Grid (<main.lenis-stopped> — `Featured Work & Interactive Showca`)**:
   - DOM & Selectors: Landmark `<main class="lenis-stopped">` rendering section `Featured Work & Interactive Showcase` with copy *"0 1 2 3 4 5 6 7 8 9"*, asset references (`187cmj4q350mm.css`, `0eqspdm2dt5_-.css`, `0kkv0xwvqoa86.css`, `14~g0x6k9zzx2.js`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<main.lenis-stopped> — `Featured Work & Interactive Showca`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1920px`, `gap: var(--spacing-2)`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--spacing-1)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<main.fonts-loaded> — `Technical Architecture & Narrative`)**:
   - DOM & Selectors: Landmark `<main class="fonts-loaded">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Kansas City Stadium , June 17, 2026"*) with `#000000` surface cards, `#0000ff` accents, and `strong { font-weight:bolder }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<main.fonts-loaded> — `Technical Architecture & Narrative`)` uses `.25rem`, `var(--radius-2xl)`, `16px`, `var(--radius-lg)` radii, `#0000ff` highlights, and assets (187cmj4q350mm.css, 0eqspdm2dt5_-.css, 0kkv0xwvqoa86.css).
5. **Colophon & Global Directory Footer (<footer.pointer-events-auto> — `https://www.thelasttango.com/`)**:
   - DOM & Selectors: Landmark `<footer class="pointer-events-auto">` anchoring `The Last Tango / For the one who` footer links (`Esp`), copy *"Every goal. Every record. Every moment that marked Messi 's "*, and `#000000` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.pointer-events-auto> — `https://www.thelasttango.com/`)` aligns to `1920px` (non-`@media` desktop container stylesheet rule) with `var(--spacing-1)` lateral canvas padding with `var(--spacing-2)` grid gap and attributes (data-loader-scroll-lock="true", data-precedence="next", data-precedence="next").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9"*
- Copy Excerpt 2: *"0 1 2 3 4 5 6 7 8 9"*
- Copy Excerpt 3: *"Kansas City Stadium , June 17, 2026"*
- Copy Excerpt 4: *"Every goal. Every record. Every moment that marked Messi 's last World Cup."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.48,.04,.52,.96)`
- **Extracted Stylesheet Rules (`www-thelasttango-com`)**:
- `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `strong { font-weight:bolder }`
- `small { font-size:80% }`
- `sup { vertical-align:baseline;font-size:75%;line-height:0;position:relative }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: .15s` extracted from `www-thelasttango-com` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `www-thelasttango-com` stylesheet.
- **Selector `box-shadow\]`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `www-thelasttango-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<header.z-100000>` and `<main.lenis-stopped>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-thelasttango-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
