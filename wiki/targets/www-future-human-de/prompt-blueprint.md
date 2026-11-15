---
title: "UI Prompt Blueprint: www-future-human-de"
date: 2026-11-15
target: "[[overview|www-future-human-de]]"
status: analyzed
archetype: "Light-Substrate Editorial & Modular Grid System (`#fff9ea` canvas, `#000` ink, `#fff` accent)"
---

# UI Design System & Master Generation Blueprint: www-future-human-de

> **FUTURE HUMAN · A Shared Year of Co-Creation & Presence** (https://www.future-human.de/) — A one-year training for multidimensional coaching & co-creation. 8 modules, 16 participants, at Das HILLA near Kassel. Starts Oct 30, 2026.

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/www-future-human-de/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **FUTURE HUMAN · A Shared Year of Co-Creation & Presence** (`https://www.future-human.de/`). A one-year training for multidimensional coaching & co-creation. 8 modules, 16 participants, at Das HILLA near Kassel. Starts Oct 30, 2026.
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#fff9ea` canvas, `#000` ink, `#fff` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fff9ea` (`var(--token-0ae2222e-ae06-4270-a415-3dc68910790b)` in `:root`) paired with `#000` primary typography and `#fff` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Spectral` for display copy (`T H E F U T U R E I S H U M A N .`) with `Inter` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1199.98px` container bounds (`gap: 4px`, padding `40px`) with `cubic-bezier(0.25,0.1,0.25,1)` easing and GSAP Timeline & ScrollTrigger, Framer Motion Layout Physics.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/www-future-human-de/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `1199.98px` extracted from `www-future-human-de` stylesheet.
- **Canvas Lateral Padding & Spacing**: `40px` lateral canvas padding with `4px` grid gap.
- **Border Radius Scale**: `8px`, `15px`, `100px`, `50px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1199.98px`, `gap: 4px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `40px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width: 1200px)`, `@media (min-width: 810px) and (max-width: 1199.98px)`, `@media (max-width: 809.98px)`, `@media (max-width:1199px) and (min-width:810px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff9ea` | `var(--token-0ae2222e-ae06-4270-a415-3dc68910790b)` in `:root` |
| **Primary Typography Ink** | `#121212` | `var(--token-5d91ee23-be21-4524-9b74-738a7ee13f13)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fffefc` | `var(--token-30996a26-1fe4-4007-9944-c80e3f142e44)` in `:root` |
| **Interactive Accent / Highlight** | `#fff` | `var(--token-5f5766cb-e316-4651-8423-ae295a71112c)` in `:root` |
| **Secondary / Muted Copy** | `#09f` | `.framer-S82Lr .framer-jkecn2 { color: #09f }` |
| **Structural Hairline Border** | `#000` | `:hover { color: #000 }` |
| **Variable Token (`--token-b6e76abb-dcfc-435b-9de5-4434133bc927`)** | `#fff9eacc` | `var(--token-b6e76abb-dcfc-435b-9de5-4434133bc927)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--token-0ae2222e-ae06-4270-a415-3dc68910790b` | `#fff9ea` | Color / Atmospheric Token |
| `--token-b6e76abb-dcfc-435b-9de5-4434133bc927` | `#fff9eacc` | Color / Atmospheric Token |
| `--token-5d91ee23-be21-4524-9b74-738a7ee13f13` | `#121212` | Color / Atmospheric Token |
| `--token-30996a26-1fe4-4007-9944-c80e3f142e44` | `#fffefc` | Color / Atmospheric Token |
| `--token-5f5766cb-e316-4651-8423-ae295a71112c` | `#fff` | Color / Atmospheric Token |
| `--text-decoration-skip-ink` | `var(--framer-text-decoration-skip-ink)` | Typography Ink Token |
| `--text-underline-offset` | `var(--framer-text-decoration-offset)` | Typography Ink Token |
| `--font-family` | `var(--framer-font-family)` | Typography / Scale Token |
| `--font-style` | `var(--framer-font-style)` | Typography / Scale Token |
| `--font-weight` | `var(--framer-font-weight)` | Typography / Scale Token |
| `--text-color` | `var(--framer-text-color)` | Typography Ink Token |
| `--letter-spacing` | `var(--framer-letter-spacing)` | Typography / Scale Token |
| `--font-size` | `var(--framer-font-size)` | Typography / Scale Token |
| `--text-transform` | `var(--framer-text-transform)` | Typography Ink Token |
| `--line-height` | `var(--framer-line-height)` | Typography / Scale Token |
| `--overflow-clip-fallback` | `hidden` | Design System Custom Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Spectral`.
- **Primary Body Stack**: `Inter`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 32px`, `line-height: 110%`, `letter-spacing: -.04em`, `font-weight: 300`).
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `var(--font-size)`, `var(--framer-font-size)`, `32px`, `28px`).
- **Body Copy**: rule `p` (`font-size: 18px`, `line-height: 140%`, `letter-spacing: -.02em`, `font-weight: 300`).
- **Metadata & Navigation Labels**: CSS variables `--letter-spacing: var(--framer-letter-spacing)`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.25,0.1,0.25,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `#__framer-editorbar-label`**: `transition: opacity 0.4s ease-out` extracted from `www-future-human-de` stylesheet.
- **Selector `style]`**: `transition: none` extracted from `www-future-human-de` stylesheet.
- **Selector `style]`**: `transition: none` extracted from `www-future-human-de` stylesheet.
- **Standard CSS Easing (`cubic-bezier(0.25,0.1,0.25,1)`)**: Default timing curve (no custom `cubic-bezier()` declared in static CSS).
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Framer Motion Layout Physics with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — FUTURE HUMAN · A Shared Year of Co-Creatio │
│ ====================================================================== │
│ [ <nav.framer-1m76co>      | Overview · Index · Archive · About · C ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.framer-16vyecu>                             |   │
│ | H1: T H E F U T U R E I S H U M A N .                            |   │
│ | Substrate: #fff9ea    | Ink: #000       | Accent: #fff           |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.framer-1omsice>  ) max-w: 1199.98px      |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | T h e M u l t i d i m e n s  |  | T h e C o l l e c t i v e F  | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 4px   ) | │
│ | [<nav.framer-1m76co] -> [<section.framer-16] -> [<section.framer-1o] │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.framer-1818ei9) | https://www.future-human.de/       │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.framer-1m76co> — `www-future-human-de`)**:
   - Landmark `<nav class="framer-1m76co">` hosting `FUTURE HUMAN · A Shared Year of Co-C` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-framer-font-css`, `data-framer-breakpoint-css`, `data-framer-css-ssr-minified`, `data-framer-components="framer-lib-cursors-ho..."`), and stylesheet rule `.hidden-72rtr7 { display:none!important }`.
2. **Hero Stage & Focal Lead (<section.framer-16vyecu> — `T H E F U T U R E I S H U M A N .`)**:
   - Landmark `<section class="framer-16vyecu sct-room">` presenting display lead `T H E F U T U R E I S H U M A N .` and copy excerpt *"D i e W e l t b r a u c h t d e i n e e i n z i g a r t i g e G a"* over `#fff9ea` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.framer-1omsice> — `T h e M u l t i d i m e n s i o n `)**:
   - Landmark `<section class="framer-1omsice sct-room">` rendering section `T h e M u l t i d i m e n s i o n a l H u m a n` with copy *"e i n z i g a r t i g e"*, asset references (`GAHKwEi2fQdp0x0qCbx0ph5tnCs.png`, `fonts.gstatic.com`, `hls.min.js`, `script`), and grid rule `.hidden-181529u { display:none!important }`.
4. **Interactive Detail & Feature Matrix (<section.framer-i64cag> — `T h e C o l l e c t i v e F i e l `)**:
   - Landmark `<section class="framer-i64cag sct-room">` framing `T h e C o l l e c t i v e F i e l d` and `T h e P a t h & T h e S a n c t u a r y` (*"M u l t i d i m e n s i o n a l"*) with `#fffefc` surface cards, `#fff` accents, and `.hidden-126ue0n { display:none!important }`.
5. **Colophon & Global Directory Footer (<footer.framer-1818ei9> — `https://www.future-human.de/`)**:
   - Landmark `<footer class="framer-1818ei9">` anchoring `FUTURE HUMAN · A Shared Year of ` footer links (`Overview · Index · Archive · About · Contact`), copy *"C o l l e c t i v e"*, and `#000` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-future-human-de (FUTURE HUMAN · A Shared Year of Co-Creation & Presence)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-future-human-de` (**FUTURE HUMAN · A Shared Year of Co-Creation & Presence** — `https://www.future-human.de/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#fff9ea` canvas, `#000` ink, `#fff` accent).
- **Identity & Domain Context**: A one-year training for multidimensional coaching & co-creation. 8 modules, 16 participants, at Das HILLA near Kassel. Starts Oct 30, 2026.
- **Primary Substrate**: `#fff9ea` (`var(--token-0ae2222e-ae06-4270-a415-3dc68910790b)` in `:root`), **Primary Ink**: `#000`, **Accent / Highlight**: `#fff`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fff9ea` (`var(--token-0ae2222e-ae06-4270-a415-3dc68910790b)` in `:root`) paired with `#000` primary typography and `#fff` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Spectral` for display copy (`T H E F U T U R E I S H U M A N .`) with `Inter` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1199.98px` container bounds (`gap: 4px`, padding `40px`) with `cubic-bezier(0.25,0.1,0.25,1)` easing and GSAP Timeline & ScrollTrigger, Framer Motion Layout Physics.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-future-human-de` in your global stylesheet:

:root {
  /* FUTURE HUMAN · A Shared Year of Co-Creation & Presence (www-future-human-de) — Ground-Truth Extracted CSS Variables */
  --token-0ae2222e-ae06-4270-a415-3dc68910790b: #fff9ea; /* Color / Atmospheric Token (www-future-human-de) */
  --token-b6e76abb-dcfc-435b-9de5-4434133bc927: #fff9eacc; /* Color / Atmospheric Token (www-future-human-de) */
  --token-5d91ee23-be21-4524-9b74-738a7ee13f13: #121212; /* Color / Atmospheric Token (www-future-human-de) */
  --token-30996a26-1fe4-4007-9944-c80e3f142e44: #fffefc; /* Color / Atmospheric Token (www-future-human-de) */
  --token-5f5766cb-e316-4651-8423-ae295a71112c: #fff; /* Color / Atmospheric Token (www-future-human-de) */
  --text-decoration-skip-ink: var(--framer-text-decoration-skip-ink); /* Typography Ink Token (www-future-human-de) */
  --text-underline-offset: var(--framer-text-decoration-offset); /* Typography Ink Token (www-future-human-de) */
  --font-family: var(--framer-font-family); /* Typography / Scale Token (www-future-human-de) */
  --font-style: var(--framer-font-style); /* Typography / Scale Token (www-future-human-de) */
  --font-weight: var(--framer-font-weight); /* Typography / Scale Token (www-future-human-de) */
  --text-color: var(--framer-text-color); /* Typography Ink Token (www-future-human-de) */
  --letter-spacing: var(--framer-letter-spacing); /* Typography / Scale Token (www-future-human-de) */
  --font-size: var(--framer-font-size); /* Typography / Scale Token (www-future-human-de) */
  --text-transform: var(--framer-text-transform); /* Typography Ink Token (www-future-human-de) */
  --line-height: var(--framer-line-height); /* Typography / Scale Token (www-future-human-de) */
  --overflow-clip-fallback: hidden; /* Design System Custom Token (www-future-human-de) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#fff9ea` — grounded in `var(--token-0ae2222e-ae06-4270-a415-3dc68910790b)` in `:root`
- **Primary Typography Ink**: `#121212` — grounded in `var(--token-5d91ee23-be21-4524-9b74-738a7ee13f13)` in `:root`
- **Elevated Surface / Card Substrate**: `#fffefc` — grounded in `var(--token-30996a26-1fe4-4007-9944-c80e3f142e44)` in `:root`
- **Interactive Accent / Highlight**: `#fff` — grounded in `var(--token-5f5766cb-e316-4651-8423-ae295a71112c)` in `:root`
- **Secondary / Muted Copy**: `#09f` — grounded in `.framer-S82Lr .framer-jkecn2 { color: #09f }`
- **Structural Hairline Border**: `#000` — grounded in `:hover { color: #000 }`
- **Variable Token (`--token-b6e76abb-dcfc-435b-9de5-4434133bc927`)**: `#fff9eacc` — grounded in `var(--token-b6e76abb-dcfc-435b-9de5-4434133bc927)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1199.98px` extracted from `www-future-human-de` stylesheet
- **Padding & Gutters**: `40px` lateral canvas padding with `4px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1199.98px`, `gap: 4px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `40px` horizontal padding
- **Media Queries**: `@media (min-width: 1200px)`, `@media (min-width: 810px) and (max-width: 1199.98px)`, `@media (max-width: 809.98px)`, `@media (max-width:1199px) and (min-width:810px)`
- **Corner Radii**: `8px`, `15px`, `100px`, `50px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Spectral`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: rule `h1` (`font-size: 32px`, `line-height: 110%`, `letter-spacing: -.04em`, `font-weight: 300`)
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `var(--font-size)`, `var(--framer-font-size)`, `32px`, `28px`)
- **Body Copy Rule**: rule `p` (`font-size: 18px`, `line-height: 140%`, `letter-spacing: -.02em`, `font-weight: 300`)
- **Metadata & Index Rule**: CSS variables `--letter-spacing: var(--framer-letter-spacing)`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-future-human-de` (`FUTURE HUMAN · A Shared Year of Co-Creation & Presence`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.framer-1m76co> — `www-future-human-de`)**:
   - DOM & Selectors: Landmark `<nav class="framer-1m76co">` hosting `FUTURE HUMAN · A Shared Year of Co-C` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-framer-font-css`, `data-framer-breakpoint-css`, `data-framer-css-ssr-minified`, `data-framer-components="framer-lib-cursors-ho..."`), and stylesheet rule `.hidden-72rtr7 { display:none!important }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.framer-1m76co> — `www-future-human-de`)` (`www-future-human-de`) adapts across `@media (min-width: 1200px)`, `@media (min-width: 810px) and (max-width: 1199.98px)`, `@media (max-width: 809.98px)`, `@media (max-width:1199px) and (min-width:810px)` with `cubic-bezier(0.25,0.1,0.25,1)` transitions and links `Overview · Index · Archive · About · Contact`.
2. **Hero Stage & Focal Lead (<section.framer-16vyecu> — `T H E F U T U R E I S H U M A N .`)**:
   - DOM & Selectors: Landmark `<section class="framer-16vyecu sct-room">` presenting display lead `T H E F U T U R E I S H U M A N .` and copy excerpt *"D i e W e l t b r a u c h t d e i n e e i n z i g a r t i g e G a"* over `#fff9ea` canvas and `#000` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#fff9ea` background with `#000` headline `T H E F U T U R E I S H U M A N .`.
3. **Primary Showcase & Content Grid (<section.framer-1omsice> — `T h e M u l t i d i m e n s i o n `)**:
   - DOM & Selectors: Landmark `<section class="framer-1omsice sct-room">` rendering section `T h e M u l t i d i m e n s i o n a l H u m a n` with copy *"e i n z i g a r t i g e"*, asset references (`GAHKwEi2fQdp0x0qCbx0ph5tnCs.png`, `fonts.gstatic.com`, `hls.min.js`, `script`), and grid rule `.hidden-181529u { display:none!important }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.framer-1omsice> — `T h e M u l t i d i m e n s i o n `)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1199.98px`, `gap: 4px`) on desktop and Single-column vertical stack at `390px` viewport width with `40px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.framer-i64cag> — `T h e C o l l e c t i v e F i e l `)**:
   - DOM & Selectors: Landmark `<section class="framer-i64cag sct-room">` framing `T h e C o l l e c t i v e F i e l d` and `T h e P a t h & T h e S a n c t u a r y` (*"M u l t i d i m e n s i o n a l"*) with `#fffefc` surface cards, `#fff` accents, and `.hidden-126ue0n { display:none!important }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.framer-i64cag> — `T h e C o l l e c t i v e F i e l `)` uses `8px`, `15px`, `100px`, `50px` radii, `#fff` highlights, and assets (GAHKwEi2fQdp0x0qCbx0ph5tnCs.png, fonts.gstatic.com, hls.min.js).
5. **Colophon & Global Directory Footer (<footer.framer-1818ei9> — `https://www.future-human.de/`)**:
   - DOM & Selectors: Landmark `<footer class="framer-1818ei9">` anchoring `FUTURE HUMAN · A Shared Year of ` footer links (`Overview · Index · Archive · About · Contact`), copy *"C o l l e c t i v e"*, and `#000` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.framer-1818ei9> — `https://www.future-human.de/`)` aligns to `1199.98px` extracted from `www-future-human-de` stylesheet with `40px` lateral canvas padding with `4px` grid gap and attributes (data-framer-font-css, data-framer-breakpoint-css, data-framer-css-ssr-minified).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"D i e W e l t b r a u c h t d e i n e e i n z i g a r t i g e G a b e ."*
- Copy Excerpt 2: *"e i n z i g a r t i g e"*
- Copy Excerpt 3: *"M u l t i d i m e n s i o n a l"*
- Copy Excerpt 4: *"C o l l e c t i v e"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.25,0.1,0.25,1)`
- **Extracted Stylesheet Rules (`www-future-human-de`)**:
- `.hidden-72rtr7 { display:none!important }`
- `.hidden-181529u { display:none!important }`
- `.hidden-126ue0n { display:none!important }`
- `main { box-sizing:border-box;margin:0;padding:0 }`
- `root { -webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale }`
- **Per-Selector Transition Rules**:
- **Selector `#__framer-editorbar-label`**: `transition: opacity 0.4s ease-out` extracted from `www-future-human-de` stylesheet.
- **Selector `style]`**: `transition: none` extracted from `www-future-human-de` stylesheet.
- **Selector `style]`**: `transition: none` extracted from `www-future-human-de` stylesheet.
- **Standard CSS Easing (`cubic-bezier(0.25,0.1,0.25,1)`)**: Default timing curve (no custom `cubic-bezier()` declared in static CSS).
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Framer Motion Layout Physics with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-future-human-de`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
