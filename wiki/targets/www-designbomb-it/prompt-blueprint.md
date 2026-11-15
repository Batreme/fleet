---
title: "UI Prompt Blueprint: www-designbomb-it"
date: 2026-11-15
target: "www-designbomb-it"
status: analyzed
capture: specimen
capture_desktop: dom
capture_mobile: specimen
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#4a60ff` / `#31a362`)"
---

# UI Design System & Master Generation Blueprint: www-designbomb-it

> **Design Bomb Festival** (https://www.designbomb.it/) — The Wave presenta la nuova edizione di Design Bomb, che cresce e diventa festival. 22-23-24 Maggio, Catania.

![Desktop Viewport Capture](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Design Bomb Festival** (`https://www.designbomb.it/`). The Wave presenta la nuova edizione di Design Bomb, che cresce e diventa festival. 22-23-24 Maggio, Catania.
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#4a60ff` / `#31a362`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#4a60ff` (`var(--token-0689d26c-723f-45fc-b97a-089acbcfc796)` in `:root`) paired with `#f7f6eb` primary typography and `#31a362` accents.
  - **Extracted Typographic Hierarchy**: Pairs `PP Frama Extrabold Italic` for display copy (`Design Bomb Festival`) with `PP Frama Black Italic` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1439.98px` container bounds (`gap: 24px`, padding `64px`) with `cubic-bezier(0.25,0.1,0.25,1)` easing and Lenis Smooth Scroll (`data-lenis`), Lottie Vector Animation Player.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Design Specimen (Offline WebGL/JS Fallback — not live site capture)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×10601px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `1439.98px` extracted from `www-designbomb-it` stylesheet.
- **Canvas Lateral Padding & Spacing**: `64px` lateral canvas padding with `24px` grid gap.
- **Border Radius Scale**: `16px`, `9999px`, `30px`, `4px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1439.98px`, `gap: 24px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `64px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width: 1440px)`, `@media (min-width: 1200px) and (max-width: 1439.98px)`, `@media (min-width: 810px) and (max-width: 1199.98px)`, `@media (max-width: 809.98px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#4a60ff` | `var(--token-0689d26c-723f-45fc-b97a-089acbcfc796)` in `:root` |
| **Primary Typography Ink** | `#ceff00` | `var(--token-7cb9fefc-a8e8-4059-91ee-bd65906318ee)` in `:root` |
| **Elevated Surface / Card Substrate** | `#ff3eba` | `var(--token-4809db6f-b397-4188-a942-074244c77dac)` in `:root` |
| **Interactive Accent / Highlight** | `#31a362` | `var(--token-797c06e2-082b-4d59-9429-4a87c1a6bdd2)` in `:root` |
| **Secondary / Muted Copy** | `#f7f6eb` | `var(--token-f1aabd16-a90b-4a64-bd76-31330e5c4d0f)` in `:root` |
| **Structural Hairline Border** | `#141414` | `var(--token-cd7ed41b-0134-43b6-beec-bf340d65ac87)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--token-0689d26c-723f-45fc-b97a-089acbcfc796` | `#4a60ff` | Color / Atmospheric Token |
| `--token-7cb9fefc-a8e8-4059-91ee-bd65906318ee` | `#ceff00` | Color / Atmospheric Token |
| `--token-4809db6f-b397-4188-a942-074244c77dac` | `#ff3eba` | Color / Atmospheric Token |
| `--token-797c06e2-082b-4d59-9429-4a87c1a6bdd2` | `#31a362` | Color / Atmospheric Token |
| `--token-f1aabd16-a90b-4a64-bd76-31330e5c4d0f` | `#f7f6eb` | Color / Atmospheric Token |
| `--token-cd7ed41b-0134-43b6-beec-bf340d65ac87` | `#141414` | Color / Atmospheric Token |
| `--token-8e1f8495-735c-4bc6-8090-6a9a9f74db16` | `#141414` | Color / Atmospheric Token |
| `--text-decoration-skip-ink` | `var(--framer-text-decoration-skip-ink)` | Typography Ink Token |
| `--text-underline-offset` | `var(--framer-text-decoration-offset)` | Typography Ink Token |
| `--font-family` | `var(--framer-font-family)` | Typography / Scale Token |
| `--font-style` | `var(--framer-font-style)` | Typography / Scale Token |
| `--font-weight` | `var(--framer-font-weight)` | Typography / Scale Token |
| `--text-color` | `var(--framer-text-color)` | Typography Ink Token |
| `--letter-spacing` | `var(--framer-letter-spacing)` | Typography / Scale Token |
| `--font-size` | `var(--framer-font-size)` | Typography / Scale Token |
| `--text-transform` | `var(--framer-text-transform)` | Typography Ink Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `PP Frama Extrabold Italic`.
- **Primary Body Stack**: `PP Frama Black Italic`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `var(--font-size)`, `var(--framer-font-size)`, `16px`, `1px`).
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `var(--font-size)`, `var(--framer-font-size)`, `16px`, `1px`).
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `var(--font-size)`, `var(--framer-font-size)`, `16px`, `1px`).
- **Metadata & Navigation Labels**: CSS variables `--letter-spacing: var(--framer-letter-spacing)`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.25,0.1,0.25,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `#__framer-editorbar-label`**: `transition: opacity 0.4s ease-out` extracted from `www-designbomb-it` stylesheet.
- **Selector `style]`**: `transition: none` extracted from `www-designbomb-it` stylesheet.
- **Selector `style]`**: `transition: none` extracted from `www-designbomb-it` stylesheet.
- **Standard CSS Easing (`cubic-bezier(0.25,0.1,0.25,1)`)**: Default timing curve (no custom `cubic-bezier()` declared in static CSS).
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Lottie Vector Animation Player, Framer Motion Layout Physics, HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Design Bomb Festival                       │
│ ====================================================================== │
│ [ <header.lenis>           | Programma · Workshop · cameretta · Sho ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.framer-hw4kQ>                               |   │
│ | H1: Design Bomb Festival                                         |   │
│ | Substrate: #4a60ff    | Ink: #f7f6eb    | Accent: #31a362        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.framer-6q1hH>    ) max-w: 1439.98px      |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Featured Work & Interactive  |  | Technical Architecture & Nar | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 24px  ) | │
│ | [<header.lenis>] -> [<section.framer-hw] -> [<section.framer-6q] |   │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.framer-1qs623s) | https://www.designbomb.it/         │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.lenis> — `www-designbomb-it`)**:
   - Landmark `<header class="lenis">` hosting `Design Bomb Festival` navigation (`Programma · Workshop · cameretta · Shop · TICKET`), DOM attributes (`data-framer-font-css`, `data-framer-breakpoint-css`, `data-framer-css-ssr-minified`, `data-framer-components="framer-lib-cursors-ho..."`), and stylesheet rule `.hidden-16glhda { display:none!important }`.
2. **Hero Stage & Focal Lead (<section.framer-hw4kQ> — `Design Bomb Festival`)**:
   - Landmark `<section class="framer-hw4kQ">` presenting display lead `Design Bomb Festival` and copy excerpt *"Un festival per tutta la community"* over `#4a60ff` canvas and `#f7f6eb` ink.
3. **Primary Showcase & Content Grid (<section.framer-6q1hH> — `Featured Work & Interactive Showca`)**:
   - Landmark `<section class="framer-6q1hH">` rendering section `Featured Work & Interactive Showcase` with copy *"Un festival per tutta"*, asset references (`CHxdCbEfx7lZs5B6CqTOXcfZQo.jpg`, `script`, `sNmVGd3Q3ckANl0dcx338qCTY4.png`, `yuFzZzaiq6SXFBvCqfED1Hgy4.png`), and grid rule `.hidden-1qs623s { display:none!important }`.
4. **Interactive Detail & Feature Matrix (<section.framer-LuCAZ> — `Technical Architecture & Narrative`)**:
   - Landmark `<section class="framer-LuCAZ">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Tre giorni, tantissimi ospiti, centinaia di persone che respirano"*) with `#ff3eba` surface cards, `#31a362` accents, and `.hidden-1tdjaai { display:none!important }`.
5. **Colophon & Global Directory Footer (<footer.framer-1qs623s> — `https://www.designbomb.it/`)**:
   - Landmark `<footer class="framer-1qs623s">` anchoring `Design Bomb Festival` footer links (`Programma · Workshop · cameretta · Shop · TICKET`), copy *"Awwwards Studio of the Year / Enea Rossi, CEO, Co-Founder e "*, and `#141414` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-designbomb-it (Design Bomb Festival)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-designbomb-it` (**Design Bomb Festival** — `https://www.designbomb.it/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#4a60ff` / `#31a362`).
- **Identity & Domain Context**: The Wave presenta la nuova edizione di Design Bomb, che cresce e diventa festival. 22-23-24 Maggio, Catania.
- **Primary Substrate**: `#4a60ff` (`var(--token-0689d26c-723f-45fc-b97a-089acbcfc796)` in `:root`), **Primary Ink**: `#f7f6eb`, **Accent / Highlight**: `#31a362`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#4a60ff` (`var(--token-0689d26c-723f-45fc-b97a-089acbcfc796)` in `:root`) paired with `#f7f6eb` primary typography and `#31a362` accents.
  - **Extracted Typographic Hierarchy**: Pairs `PP Frama Extrabold Italic` for display copy (`Design Bomb Festival`) with `PP Frama Black Italic` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1439.98px` container bounds (`gap: 24px`, padding `64px`) with `cubic-bezier(0.25,0.1,0.25,1)` easing and Lenis Smooth Scroll (`data-lenis`), Lottie Vector Animation Player.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-designbomb-it` in your global stylesheet:

:root {
  /* Design Bomb Festival (www-designbomb-it) — Ground-Truth Extracted CSS Variables */
  --token-0689d26c-723f-45fc-b97a-089acbcfc796: #4a60ff; /* Color / Atmospheric Token (www-designbomb-it) */
  --token-7cb9fefc-a8e8-4059-91ee-bd65906318ee: #ceff00; /* Color / Atmospheric Token (www-designbomb-it) */
  --token-4809db6f-b397-4188-a942-074244c77dac: #ff3eba; /* Color / Atmospheric Token (www-designbomb-it) */
  --token-797c06e2-082b-4d59-9429-4a87c1a6bdd2: #31a362; /* Color / Atmospheric Token (www-designbomb-it) */
  --token-f1aabd16-a90b-4a64-bd76-31330e5c4d0f: #f7f6eb; /* Color / Atmospheric Token (www-designbomb-it) */
  --token-cd7ed41b-0134-43b6-beec-bf340d65ac87: #141414; /* Color / Atmospheric Token (www-designbomb-it) */
  --token-8e1f8495-735c-4bc6-8090-6a9a9f74db16: #141414; /* Color / Atmospheric Token (www-designbomb-it) */
  --text-decoration-skip-ink: var(--framer-text-decoration-skip-ink); /* Typography Ink Token (www-designbomb-it) */
  --text-underline-offset: var(--framer-text-decoration-offset); /* Typography Ink Token (www-designbomb-it) */
  --font-family: var(--framer-font-family); /* Typography / Scale Token (www-designbomb-it) */
  --font-style: var(--framer-font-style); /* Typography / Scale Token (www-designbomb-it) */
  --font-weight: var(--framer-font-weight); /* Typography / Scale Token (www-designbomb-it) */
  --text-color: var(--framer-text-color); /* Typography Ink Token (www-designbomb-it) */
  --letter-spacing: var(--framer-letter-spacing); /* Typography / Scale Token (www-designbomb-it) */
  --font-size: var(--framer-font-size); /* Typography / Scale Token (www-designbomb-it) */
  --text-transform: var(--framer-text-transform); /* Typography Ink Token (www-designbomb-it) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#4a60ff` — grounded in `var(--token-0689d26c-723f-45fc-b97a-089acbcfc796)` in `:root`
- **Primary Typography Ink**: `#ceff00` — grounded in `var(--token-7cb9fefc-a8e8-4059-91ee-bd65906318ee)` in `:root`
- **Elevated Surface / Card Substrate**: `#ff3eba` — grounded in `var(--token-4809db6f-b397-4188-a942-074244c77dac)` in `:root`
- **Interactive Accent / Highlight**: `#31a362` — grounded in `var(--token-797c06e2-082b-4d59-9429-4a87c1a6bdd2)` in `:root`
- **Secondary / Muted Copy**: `#f7f6eb` — grounded in `var(--token-f1aabd16-a90b-4a64-bd76-31330e5c4d0f)` in `:root`
- **Structural Hairline Border**: `#141414` — grounded in `var(--token-cd7ed41b-0134-43b6-beec-bf340d65ac87)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×10601px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1439.98px` extracted from `www-designbomb-it` stylesheet
- **Padding & Gutters**: `64px` lateral canvas padding with `24px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1439.98px`, `gap: 24px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `64px` horizontal padding
- **Media Queries**: `@media (min-width: 1440px)`, `@media (min-width: 1200px) and (max-width: 1439.98px)`, `@media (min-width: 810px) and (max-width: 1199.98px)`, `@media (max-width: 809.98px)`
- **Corner Radii**: `16px`, `9999px`, `30px`, `4px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `PP Frama Extrabold Italic`
- **Body Font Stack**: `PP Frama Black Italic`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `var(--font-size)`, `var(--framer-font-size)`, `16px`, `1px`)
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `var(--font-size)`, `var(--framer-font-size)`, `16px`, `1px`)
- **Body Copy Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `var(--font-size)`, `var(--framer-font-size)`, `16px`, `1px`)
- **Metadata & Index Rule**: CSS variables `--letter-spacing: var(--framer-letter-spacing)`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-designbomb-it` (`Design Bomb Festival`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.lenis> — `www-designbomb-it`)**:
   - DOM & Selectors: Landmark `<header class="lenis">` hosting `Design Bomb Festival` navigation (`Programma · Workshop · cameretta · Shop · TICKET`), DOM attributes (`data-framer-font-css`, `data-framer-breakpoint-css`, `data-framer-css-ssr-minified`, `data-framer-components="framer-lib-cursors-ho..."`), and stylesheet rule `.hidden-16glhda { display:none!important }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.lenis> — `www-designbomb-it`)` (`www-designbomb-it`) adapts across `@media (min-width: 1440px)`, `@media (min-width: 1200px) and (max-width: 1439.98px)`, `@media (min-width: 810px) and (max-width: 1199.98px)`, `@media (max-width: 809.98px)` with `cubic-bezier(0.25,0.1,0.25,1)` transitions and links `Programma · Workshop · cameretta · Shop · TICKET`.
2. **Hero Stage & Focal Lead (<section.framer-hw4kQ> — `Design Bomb Festival`)**:
   - DOM & Selectors: Landmark `<section class="framer-hw4kQ">` presenting display lead `Design Bomb Festival` and copy excerpt *"Un festival per tutta la community"* over `#4a60ff` canvas and `#f7f6eb` ink.
   - Responsive Contract: Hero stage (`1440×10601px` desktop / `390×2400px` mobile) sets `#4a60ff` background with `#f7f6eb` headline `Design Bomb Festival`.
3. **Primary Showcase & Content Grid (<section.framer-6q1hH> — `Featured Work & Interactive Showca`)**:
   - DOM & Selectors: Landmark `<section class="framer-6q1hH">` rendering section `Featured Work & Interactive Showcase` with copy *"Un festival per tutta"*, asset references (`CHxdCbEfx7lZs5B6CqTOXcfZQo.jpg`, `script`, `sNmVGd3Q3ckANl0dcx338qCTY4.png`, `yuFzZzaiq6SXFBvCqfED1Hgy4.png`), and grid rule `.hidden-1qs623s { display:none!important }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.framer-6q1hH> — `Featured Work & Interactive Showca`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1439.98px`, `gap: 24px`) on desktop and Single-column vertical stack at `390px` viewport width with `64px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.framer-LuCAZ> — `Technical Architecture & Narrative`)**:
   - DOM & Selectors: Landmark `<section class="framer-LuCAZ">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Tre giorni, tantissimi ospiti, centinaia di persone che respirano"*) with `#ff3eba` surface cards, `#31a362` accents, and `.hidden-1tdjaai { display:none!important }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.framer-LuCAZ> — `Technical Architecture & Narrative`)` uses `16px`, `9999px`, `30px`, `4px` radii, `#31a362` highlights, and assets (CHxdCbEfx7lZs5B6CqTOXcfZQo.jpg, script, sNmVGd3Q3ckANl0dcx338qCTY4.png).
5. **Colophon & Global Directory Footer (<footer.framer-1qs623s> — `https://www.designbomb.it/`)**:
   - DOM & Selectors: Landmark `<footer class="framer-1qs623s">` anchoring `Design Bomb Festival` footer links (`Programma · Workshop · cameretta · Shop · TICKET`), copy *"Awwwards Studio of the Year / Enea Rossi, CEO, Co-Founder e "*, and `#141414` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.framer-1qs623s> — `https://www.designbomb.it/`)` aligns to `1439.98px` extracted from `www-designbomb-it` stylesheet with `64px` lateral canvas padding with `24px` grid gap and attributes (data-framer-font-css, data-framer-breakpoint-css, data-framer-css-ssr-minified).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Un festival per tutta la community"*
- Copy Excerpt 2: *"Un festival per tutta"*
- Copy Excerpt 3: *"Tre giorni, tantissimi ospiti, centinaia di persone che respirano la stessa aria...."*
- Copy Excerpt 4: *"Awwwards Studio of the Year / Enea Rossi, CEO, Co-Founder e Creative Partner"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.25,0.1,0.25,1)`
- **Extracted Stylesheet Rules (`www-designbomb-it`)**:
- `.hidden-16glhda { display:none!important }`
- `.hidden-1qs623s { display:none!important }`
- `.hidden-1tdjaai { display:none!important }`
- `.hidden-tzhh5x { display:none!important }`
- `main { box-sizing:border-box;margin:0;padding:0 }`
- **Per-Selector Transition Rules**:
- **Selector `#__framer-editorbar-label`**: `transition: opacity 0.4s ease-out` extracted from `www-designbomb-it` stylesheet.
- **Selector `style]`**: `transition: none` extracted from `www-designbomb-it` stylesheet.
- **Selector `style]`**: `transition: none` extracted from `www-designbomb-it` stylesheet.
- **Standard CSS Easing (`cubic-bezier(0.25,0.1,0.25,1)`)**: Default timing curve (no custom `cubic-bezier()` declared in static CSS).
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Lottie Vector Animation Player, Framer Motion Layout Physics, HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-designbomb-it`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
