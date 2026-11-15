---
title: "UI Prompt Blueprint: www-fiabamia-com"
date: 2026-11-15
target: "[[overview|www-fiabamia-com]]"
status: analyzed
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#ffa3a3` / `#fffbeb`)"
---

# UI Design System & Master Generation Blueprint: www-fiabamia-com

> **FiabaMia — Personalized bedtime stories for children** (https://www.fiabamia.com/) — Every night a brand-new bedtime story where your child is the hero: written in 30 seconds to fit their age, with music, interactive sound...

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **FiabaMia — Personalized bedtime stories for children** (`https://www.fiabamia.com/`). Every night a brand-new bedtime story where your child is the hero: written in 30 seconds to fit their age, with music, interactive sound...
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#ffa3a3` / `#fffbeb`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#ffa3a3` (`var(--color-red-300)` in `:root`) paired with `#fb2c36` primary typography and `#fffbeb` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Lora` for display copy (`Personalized bedtime stories for chi`) with `Lora Fallback` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `40rem` container bounds (`gap: 3px`, padding `.62rem`) with `cubic-bezier(.4,0,1,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `40rem` extracted from `www-fiabamia-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `.62rem` lateral canvas padding with `3px` grid gap.
- **Border Radius Scale**: `var(--radius-xl)`, `var(--radius-2xl)`, `.25rem`, `var(--radius-3xl)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: 3px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `.62rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#ffa3a3` | `var(--color-red-300)` in `:root` |
| **Primary Typography Ink** | `#ff6568` | `var(--color-red-400)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fb2c36` | `var(--color-red-500)` in `:root` |
| **Interactive Accent / Highlight** | `#fffbeb` | `var(--color-amber-50)` in `:root` |
| **Secondary / Muted Copy** | `#ffd236` | `var(--color-amber-300)` in `:root` |
| **Structural Hairline Border** | `#fcbb00` | `var(--color-amber-400)` in `:root` |
| **Variable Token (`--color-amber-500`)** | `#f99c00` | `var(--color-amber-500)` in `:root` |
| **Variable Token (`--color-amber-600`)** | `#dd7400` | `var(--color-amber-600)` in `:root` |
| **Variable Token (`--color-amber-700`)** | `#b75000` | `var(--color-amber-700)` in `:root` |
| **Variable Token (`--color-yellow-400`)** | `#fac800` | `var(--color-yellow-400)` in `:root` |
| **Variable Token (`--color-yellow-500`)** | `#edb200` | `var(--color-yellow-500)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-lora` | `"Lora", "Lora Fallback"` | Typography / Scale Token |
| `--font-cormorant-sc` | `"Cormorant SC", "Cormorant SC Fallback"` | Typography / Scale Token |
| `--font-nunito` | `"Nunito", "Nunito Fallback"` | Typography / Scale Token |
| `--font-sans` | `var(--font-nunito)` | Typography / Scale Token |
| `--font-serif` | `var(--font-lora)` | Typography / Scale Token |
| `--color-red-300` | `#ffa3a3` | Brand / Palette Token |
| `--color-red-400` | `#ff6568` | Brand / Palette Token |
| `--color-red-500` | `#fb2c36` | Brand / Palette Token |
| `--color-amber-50` | `#fffbeb` | Brand / Palette Token |
| `--color-amber-300` | `#ffd236` | Brand / Palette Token |
| `--color-amber-400` | `#fcbb00` | Brand / Palette Token |
| `--color-amber-500` | `#f99c00` | Brand / Palette Token |
| `--color-amber-600` | `#dd7400` | Brand / Palette Token |
| `--color-amber-700` | `#b75000` | Brand / Palette Token |
| `--color-yellow-400` | `#fac800` | Brand / Palette Token |
| `--color-yellow-500` | `#edb200` | Brand / Palette Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Lora`.
- **Primary Body Stack**: `Lora Fallback`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`.
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`font-size: clamp(1.45rem,2.6vw,1.85rem)`, `line-height: 1.2`, `letter-spacing: -.02em`, `font-weight: 300`).
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`; rule `p` (`font-size: clamp(1.05rem,1.5vw,1.38rem)`, `line-height: 1.4`, `font-weight: 300`).
- **Metadata & Navigation Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`; rule `small` (`font-size: .42em`, `letter-spacing: 0`, `font-weight: 300`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: .15s` extracted from `www-fiabamia-com` stylesheet.
- **Selector `layer components`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `www-fiabamia-com` stylesheet.
- **Selector `.btn-secondary`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `www-fiabamia-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,1,1)`)**: Governs interactive state transitions across `<header.vg-testata>` and `<section.vg-lettura>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — FiabaMia — Personalized bedtime stories fo │
│ ====================================================================== │
│ [ <header.vg-testata>      | Create a story                         ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.vg-hero>                                    |   │
│ | H1: Personalized bedtime stories for children A fairy...         |   │
│ | Substrate: #ffa3a3    | Ink: #fb2c36    | Accent: #fffbeb        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.vg-lettura>      ) max-w: 40rem          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | A story made to measure: nam |  | Every story has its own musi | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 3px   ) | │
│ | [<header.vg-testata] -> [<section.vg-hero>] -> [<section.vg-lettur]  │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.vg-fondo>     ) | https://www.fiabamia.com/          │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.vg-testata> — `www-fiabamia-com`)**:
   - Landmark `<header class="vg-testata">` hosting `FiabaMia — Personalized bedtime stor` navigation (`Create a story`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `lora_59c43264-module__4gbARq__cla... { font-family:Lora,Lora Fallback;font-style:normal }`.
2. **Hero Stage & Focal Lead (<section.vg-hero> — `Personalized bedtime stories for c`)**:
   - Landmark `<section class="vg-hero">` presenting display lead `Personalized bedtime stories for children A fairy...` and copy excerpt *"FiabaMia · a bedtime fairy tale"* over `#ffa3a3` canvas and `#fb2c36` ink.
3. **Primary Showcase & Content Grid (<section.vg-lettura> — `A story made to measure: name, age`)**:
   - Landmark `<section class="vg-lettura">` rendering section `A story made to measure: name, age, value, place...` with copy *"No one has ever told it…"*, asset references (`07454f8ad8aaac57-s.p.0tqkxa-w3pk~...`, `25e51d4a4d803f16-s.p.01lzzy~hm0v2...`, `4917c4fe274b6773-s.p.03o7i-1ioayt...`, `54fc36028e2bb174-s.p.0nkps02--w45...`), and grid rule `.lora_59c43264-module__4gbARq__va... { --font-lora:"Lora", "Lora Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.vg-tunnel> — `Every story has its own music`)**:
   - Landmark `<section class="vg-tunnel">` framing `Every story has its own music` and `Words that come to life` (*"Listen with sound Sound on"*) with `#fb2c36` surface cards, `#fffbeb` accents, and `t_sc_8e09fe47-module__uQmyda__cla... { font-family:Cormorant SC,Cormorant SC Fallback;font-style:normal }`.
5. **Colophon & Global Directory Footer (<footer.vg-fondo> — `https://www.fiabamia.com/`)**:
   - Landmark `<footer class="vg-fondo site-footer">` anchoring `FiabaMia — Personalized bedtime ` footer links (`Create a story`), copy *"Personalized bedtime stories for children"*, and `#fcbb00` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-fiabamia-com (FiabaMia — Personalized bedtime stories for children)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-fiabamia-com` (**FiabaMia — Personalized bedtime stories for children** — `https://www.fiabamia.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffa3a3` / `#fffbeb`).
- **Identity & Domain Context**: Every night a brand-new bedtime story where your child is the hero: written in 30 seconds to fit their age, with music, interactive sound...
- **Primary Substrate**: `#ffa3a3` (`var(--color-red-300)` in `:root`), **Primary Ink**: `#fb2c36`, **Accent / Highlight**: `#fffbeb`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#ffa3a3` (`var(--color-red-300)` in `:root`) paired with `#fb2c36` primary typography and `#fffbeb` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Lora` for display copy (`Personalized bedtime stories for chi`) with `Lora Fallback` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `40rem` container bounds (`gap: 3px`, padding `.62rem`) with `cubic-bezier(.4,0,1,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-fiabamia-com` in your global stylesheet:

:root {
  /* FiabaMia — Personalized bedtime stories for children (www-fiabamia-com) — Ground-Truth Extracted CSS Variables */
  --font-lora: "Lora", "Lora Fallback"; /* Typography / Scale Token (www-fiabamia-com) */
  --font-cormorant-sc: "Cormorant SC", "Cormorant SC Fallback"; /* Typography / Scale Token (www-fiabamia-com) */
  --font-nunito: "Nunito", "Nunito Fallback"; /* Typography / Scale Token (www-fiabamia-com) */
  --font-sans: var(--font-nunito); /* Typography / Scale Token (www-fiabamia-com) */
  --font-serif: var(--font-lora); /* Typography / Scale Token (www-fiabamia-com) */
  --color-red-300: #ffa3a3; /* Brand / Palette Token (www-fiabamia-com) */
  --color-red-400: #ff6568; /* Brand / Palette Token (www-fiabamia-com) */
  --color-red-500: #fb2c36; /* Brand / Palette Token (www-fiabamia-com) */
  --color-amber-50: #fffbeb; /* Brand / Palette Token (www-fiabamia-com) */
  --color-amber-300: #ffd236; /* Brand / Palette Token (www-fiabamia-com) */
  --color-amber-400: #fcbb00; /* Brand / Palette Token (www-fiabamia-com) */
  --color-amber-500: #f99c00; /* Brand / Palette Token (www-fiabamia-com) */
  --color-amber-600: #dd7400; /* Brand / Palette Token (www-fiabamia-com) */
  --color-amber-700: #b75000; /* Brand / Palette Token (www-fiabamia-com) */
  --color-yellow-400: #fac800; /* Brand / Palette Token (www-fiabamia-com) */
  --color-yellow-500: #edb200; /* Brand / Palette Token (www-fiabamia-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ffa3a3` — grounded in `var(--color-red-300)` in `:root`
- **Primary Typography Ink**: `#ff6568` — grounded in `var(--color-red-400)` in `:root`
- **Elevated Surface / Card Substrate**: `#fb2c36` — grounded in `var(--color-red-500)` in `:root`
- **Interactive Accent / Highlight**: `#fffbeb` — grounded in `var(--color-amber-50)` in `:root`
- **Secondary / Muted Copy**: `#ffd236` — grounded in `var(--color-amber-300)` in `:root`
- **Structural Hairline Border**: `#fcbb00` — grounded in `var(--color-amber-400)` in `:root`
- **Variable Token (`--color-amber-500`)**: `#f99c00` — grounded in `var(--color-amber-500)` in `:root`
- **Variable Token (`--color-amber-600`)**: `#dd7400` — grounded in `var(--color-amber-600)` in `:root`
- **Variable Token (`--color-amber-700`)**: `#b75000` — grounded in `var(--color-amber-700)` in `:root`
- **Variable Token (`--color-yellow-400`)**: `#fac800` — grounded in `var(--color-yellow-400)` in `:root`
- **Variable Token (`--color-yellow-500`)**: `#edb200` — grounded in `var(--color-yellow-500)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `40rem` extracted from `www-fiabamia-com` stylesheet
- **Padding & Gutters**: `.62rem` lateral canvas padding with `3px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: 3px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `.62rem` horizontal padding
- **Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)`
- **Corner Radii**: `var(--radius-xl)`, `var(--radius-2xl)`, `.25rem`, `var(--radius-3xl)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Lora`
- **Body Font Stack**: `Lora Fallback`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`
- **H2 Section Rule**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`font-size: clamp(1.45rem,2.6vw,1.85rem)`, `line-height: 1.2`, `letter-spacing: -.02em`, `font-weight: 300`)
- **Body Copy Rule**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`; rule `p` (`font-size: clamp(1.05rem,1.5vw,1.38rem)`, `line-height: 1.4`, `font-weight: 300`)
- **Metadata & Index Rule**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`; rule `small` (`font-size: .42em`, `letter-spacing: 0`, `font-weight: 300`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-fiabamia-com` (`FiabaMia — Personalized bedtime stories for children`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.vg-testata> — `www-fiabamia-com`)**:
   - DOM & Selectors: Landmark `<header class="vg-testata">` hosting `FiabaMia — Personalized bedtime stor` navigation (`Create a story`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `lora_59c43264-module__4gbARq__cla... { font-family:Lora,Lora Fallback;font-style:normal }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.vg-testata> — `www-fiabamia-com`)` (`www-fiabamia-com`) adapts across `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)` with `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)` transitions and links `Create a story`.
2. **Hero Stage & Focal Lead (<section.vg-hero> — `Personalized bedtime stories for c`)**:
   - DOM & Selectors: Landmark `<section class="vg-hero">` presenting display lead `Personalized bedtime stories for children A fairy...` and copy excerpt *"FiabaMia · a bedtime fairy tale"* over `#ffa3a3` canvas and `#fb2c36` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#ffa3a3` background with `#fb2c36` headline `Personalized bedtime stories for children A fairy...`.
3. **Primary Showcase & Content Grid (<section.vg-lettura> — `A story made to measure: name, age`)**:
   - DOM & Selectors: Landmark `<section class="vg-lettura">` rendering section `A story made to measure: name, age, value, place...` with copy *"No one has ever told it…"*, asset references (`07454f8ad8aaac57-s.p.0tqkxa-w3pk~...`, `25e51d4a4d803f16-s.p.01lzzy~hm0v2...`, `4917c4fe274b6773-s.p.03o7i-1ioayt...`, `54fc36028e2bb174-s.p.0nkps02--w45...`), and grid rule `.lora_59c43264-module__4gbARq__va... { --font-lora:"Lora", "Lora Fallback" }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.vg-lettura> — `A story made to measure: name, age`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: 3px`) on desktop and Single-column vertical stack at `390px` viewport width with `.62rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.vg-tunnel> — `Every story has its own music`)**:
   - DOM & Selectors: Landmark `<section class="vg-tunnel">` framing `Every story has its own music` and `Words that come to life` (*"Listen with sound Sound on"*) with `#fb2c36` surface cards, `#fffbeb` accents, and `t_sc_8e09fe47-module__uQmyda__cla... { font-family:Cormorant SC,Cormorant SC Fallback;font-style:normal }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.vg-tunnel> — `Every story has its own music`)` uses `var(--radius-xl)`, `var(--radius-2xl)`, `.25rem`, `var(--radius-3xl)` radii, `#fffbeb` highlights, and assets (07454f8ad8aaac57-s.p.0tqkxa-w3pk~..., 25e51d4a4d803f16-s.p.01lzzy~hm0v2..., 4917c4fe274b6773-s.p.03o7i-1ioayt...).
5. **Colophon & Global Directory Footer (<footer.vg-fondo> — `https://www.fiabamia.com/`)**:
   - DOM & Selectors: Landmark `<footer class="vg-fondo site-footer">` anchoring `FiabaMia — Personalized bedtime ` footer links (`Create a story`), copy *"Personalized bedtime stories for children"*, and `#fcbb00` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.vg-fondo> — `https://www.fiabamia.com/`)` aligns to `40rem` extracted from `www-fiabamia-com` stylesheet with `.62rem` lateral canvas padding with `3px` grid gap and attributes (data-precedence="next", data-precedence="next", data-precedence="next").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"FiabaMia · a bedtime fairy tale"*
- Copy Excerpt 2: *"No one has ever told it…"*
- Copy Excerpt 3: *"Listen with sound Sound on"*
- Copy Excerpt 4: *"Personalized bedtime stories for children"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`
- **Extracted Stylesheet Rules (`www-fiabamia-com`)**:
- `lora_59c43264-module__4gbARq__cla... { font-family:Lora,Lora Fallback;font-style:normal }`
- `.lora_59c43264-module__4gbARq__va... { --font-lora:"Lora", "Lora Fallback" }`
- `t_sc_8e09fe47-module__uQmyda__cla... { font-family:Cormorant SC,Cormorant SC Fallback;font-style:normal }`
- `nt_sc_8e09fe47-module__uQmyda__va... { --font-cormorant-sc:"Cormorant SC", "Cormorant SC Fallback" }`
- `nito_c83fe90b-module__6Ix-nq__cla... { font-family:Nunito,Nunito Fallback;font-style:normal }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: .15s` extracted from `www-fiabamia-com` stylesheet.
- **Selector `layer components`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `www-fiabamia-com` stylesheet.
- **Selector `.btn-secondary`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `www-fiabamia-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,1,1)`)**: Governs interactive state transitions across `<header.vg-testata>` and `<section.vg-lettura>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-fiabamia-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
