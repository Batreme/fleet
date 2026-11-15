---
title: "UI Prompt Blueprint: lorenzolottici-it_en"
date: 2026-11-15
target: "[[overview|lorenzolottici-it_en]]"
status: analyzed
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#3080ff` / `#070707`)"
---

# UI Design System & Master Generation Blueprint: lorenzolottici-it_en

> **Lorenzo Lottici · Order in chaos** (https://lorenzolottici.it/en) — I bring order to the chaos in your business. Outside, a site people recognize at first glance. Inside, automations and AI agents that wor...

![Desktop Viewport Capture (1440x24039)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Lorenzo Lottici · Order in chaos** (`https://lorenzolottici.it/en`). I bring order to the chaos in your business. Outside, a site people recognize at first glance. Inside, automations and AI agents that wor...
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#3080ff` / `#070707`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#3080ff` (`var(--color-blue-500)` in `:root`) paired with `#fff` primary typography and `#070707` accents.
  - **Extracted Typographic Hierarchy**: Pairs `archivo` for display copy (`Websites and AI automation in Parma`) with `archivo Fallback` and `jetbrainsMono`.
  - **Calibrated Spatial Grid & Motion**: Combines `80rem` container bounds (`gap: 8px`, padding `16px`) with `cubic-bezier(.4,0,1,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×24039px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `80rem` extracted from `lorenzolottici-it_en` stylesheet.
- **Canvas Lateral Padding & Spacing**: `16px` lateral canvas padding with `8px` grid gap.
- **Border Radius Scale**: `50%`, `4px`, `.25rem`, `var(--radius-2xl)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 80rem`, `gap: 8px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `16px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width:640px)`, `@media (max-width:760px)`, `@media (max-width:300px)`, `@media (prefers-reduced-motion:reduce)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#3080ff` | `var(--color-blue-500)` in `:root` |
| **Primary Typography Ink** | `#000` | `var(--color-black)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fff` | `var(--color-white)` in `:root` |
| **Interactive Accent / Highlight** | `#070707` | `var(--fondo)` in `:root` |
| **Secondary / Muted Copy** | `#0b0c0f` | `var(--pietra)` in `:root` |
| **Structural Hairline Border** | `#14140f` | `var(--inchiostro)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--tenue` | `var(--avorio)` | Design System Custom Token |
| `--avorio-32` | `var(--avorio-10)` | Design System Custom Token |
| `--mono` | `var(--font-jetbrains-mono), ui-monospace, monospace` | Typography / Scale Token |
| `--bordo` | `clamp(8px, 1.2cqmin, 16px)` | Dimension / Scale Token |
| `--su-tocco` | `max(48px, 3rem)` | Dimension / Scale Token |
| `--su-icona` | `max(16px, 1.125rem)` | Dimension / Scale Token |
| `--th` | `clamp(72px, 9vh, 96px)` | Dimension / Scale Token |
| `--riga-h` | `56px` | Dimension / Scale Token |
| `--finestra` | `44svh` | Dimension / Scale Token |
| `--font-grotesk` | `"archivo", "archivo Fallback", system-ui, sans-serif` | Typography / Scale Token |
| `--font-jetbrains-mono` | `"jetbrainsMono", Courier New, ui-monospace, monospace` | Typography / Scale Token |
| `--font-serif` | `ui-serif,Georgia,Cambria,"Times New Roman",Times,serif` | Typography / Scale Token |
| `--color-blue-500` | `#3080ff` | Brand / Palette Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `archivo`.
- **Primary Body Stack**: `archivo Fallback`.
- **Technical / Metadata Stack**: `jetbrainsMono`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--font-display: var(--font-grande)`, `--tipo-display: clamp(2.75rem,calc(1.2708rem + 6.5741vw),7.1875rem)`, `--lh-display: .98`; rule `h1` (`font-size: var(--tipo-titolo)`, `line-height: var(--lh-titolo)`, `letter-spacing: var(--ls-titolo)`, `font-weight: var(--peso-di...`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: var(--tipo-label)`, `line-height: var(--lh-label)`, `letter-spacing: var(--ls-label)`, `font-weight: var(--peso-la...`).
- **Body Copy**: rule `p` (`line-height: var(--lh-corpo)`).
- **Metadata & Navigation Labels**: CSS variables `--mono: var(--font-jetbrains-mono), ui-monospace, monospace`, `--font-jetbrains-mono: "jetbrainsMono", Courier New, ui-monospace, monospace`, `--text-xs: .75rem`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `._2ZgDjW_eroe[data-via=scivola]`**: `transition: transform var(--dur-scopri) var(--curva-uscita)` extracted from `lorenzolottici-it_en` stylesheet.
- **Selector `._2ZgDjW_piede`**: `transition: transform var(--dur-scopri) var(--curva)` extracted from `lorenzolottici-it_en` stylesheet.
- **Selector `html[data-lavori-esce] ._2ZgDjW_p...`**: `transition: transform var(--dur-stato) var(--curva)` extracted from `lorenzolottici-it_en` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,1,1)`)**: Governs interactive state transitions across `<header.indice-home>` and `<section.js>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Framer Motion Layout Physics with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Lorenzo Lottici · Order in chaos           │
│ ====================================================================== │
│ [ <header.indice-home>     | What I do · Path · Work · Thinking · L ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.dark>                                       |   │
│ | H1: Websites and AI automation in Parma                          |   │
│ | Substrate: #3080ff    | Ink: #fff       | Accent: #070707        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.js>              ) max-w: 80rem          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | What I do                    |  | Websites & e-commerce        | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 8px   ) | │
│ | [<header.indice-hom] -> [<section.dark>] -> [<section.js>] |         │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.su-piede>     ) | https://lorenzolottici.it/en       │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.indice-home> — `lorenzolottici-it_en`)**:
   - Landmark `<header class="indice-home indice-testata">` hosting `Lorenzo Lottici · Order in chaos` navigation (`What I do · Path · Work · Thinking · Let’s talk`), DOM attributes (`data-testata="1"`, `data-caricamento="1"`, `data-tre="1"`, `data-precedence="next"`), and stylesheet rule `.iLAgaa_colonna { max-width:80rem;margin:0 auto;position:relative }`.
2. **Hero Stage & Focal Lead (<section.dark> — `Websites and AI automation in Parm`)**:
   - Landmark `<section class="dark">` presenting display lead `Websites and AI automation in Parma` and copy excerpt *"I’m Lorenzo Lottici. I bring order to the chaos in your business:"* over `#3080ff` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.js> — `What I do`)**:
   - Landmark `<section class="js">` rendering section `What I do` with copy *"I give shape to your ideas. From solid corporate architecture to "*, asset references (`archivo_latin_var-s.p.3b1_7etm2gp...`, `jetbrains_mono_latin_var.p.0gbvn7...`, `polvere-carta.webp`, `420u9fgvjqgpl.js`), and grid rule `.iLAgaa_stelle { border-radius:50%;width:1px;height:1px;position:absolute;top:0;left:0 }`.
4. **Interactive Detail & Feature Matrix (<section.scroll-fermo> — `Websites & e-commerce`)**:
   - Landmark `<section class="scroll-fermo">` framing `Websites & e-commerce` and `AI & automation` (*"I take the weight off your hands. More time for people, zero oper"*) with `#fff` surface cards, `#070707` accents, and `.iLAgaa_pianeta { width:120vw;top:-74vw;right:-62vw }`.
5. **Colophon & Global Directory Footer (<footer.su-piede> — `https://lorenzolottici.it/en`)**:
   - Landmark `<footer class="su-piede indice-home">` anchoring `Lorenzo Lottici · Order in chaos` footer links (`What I do · Path · Work · Thinking · Let’s talk`), copy *"Roxam : the site of a company that’s been building trade sho"*, and `#14140f` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: lorenzolottici-it_en (Lorenzo Lottici · Order in chaos)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `lorenzolottici-it_en` (**Lorenzo Lottici · Order in chaos** — `https://lorenzolottici.it/en`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#3080ff` / `#070707`).
- **Identity & Domain Context**: I bring order to the chaos in your business. Outside, a site people recognize at first glance. Inside, automations and AI agents that wor...
- **Primary Substrate**: `#3080ff` (`var(--color-blue-500)` in `:root`), **Primary Ink**: `#fff`, **Accent / Highlight**: `#070707`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#3080ff` (`var(--color-blue-500)` in `:root`) paired with `#fff` primary typography and `#070707` accents.
  - **Extracted Typographic Hierarchy**: Pairs `archivo` for display copy (`Websites and AI automation in Parma`) with `archivo Fallback` and `jetbrainsMono`.
  - **Calibrated Spatial Grid & Motion**: Combines `80rem` container bounds (`gap: 8px`, padding `16px`) with `cubic-bezier(.4,0,1,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `lorenzolottici-it_en` in your global stylesheet:

:root {
  /* Lorenzo Lottici · Order in chaos (lorenzolottici-it_en) — Ground-Truth Extracted CSS Variables */
  --tenue: var(--avorio); /* Design System Custom Token (lorenzolottici-it_en) */
  --avorio-32: var(--avorio-10); /* Design System Custom Token (lorenzolottici-it_en) */
  --mono: var(--font-jetbrains-mono), ui-monospace, monospace; /* Typography / Scale Token (lorenzolottici-it_en) */
  --bordo: clamp(8px, 1.2cqmin, 16px); /* Dimension / Scale Token (lorenzolottici-it_en) */
  --su-tocco: max(48px, 3rem); /* Dimension / Scale Token (lorenzolottici-it_en) */
  --su-icona: max(16px, 1.125rem); /* Dimension / Scale Token (lorenzolottici-it_en) */
  --th: clamp(72px, 9vh, 96px); /* Dimension / Scale Token (lorenzolottici-it_en) */
  --riga-h: 56px; /* Dimension / Scale Token (lorenzolottici-it_en) */
  --finestra: 44svh; /* Dimension / Scale Token (lorenzolottici-it_en) */
  --font-grotesk: "archivo", "archivo Fallback", system-ui, sans-serif; /* Typography / Scale Token (lorenzolottici-it_en) */
  --font-jetbrains-mono: "jetbrainsMono", Courier New, ui-monospace, monospace; /* Typography / Scale Token (lorenzolottici-it_en) */
  --font-serif: ui-serif,Georgia,Cambria,"Times New Roman",Times,serif; /* Typography / Scale Token (lorenzolottici-it_en) */
  --color-blue-500: #3080ff; /* Brand / Palette Token (lorenzolottici-it_en) */
  --color-black: #000; /* Canvas / Surface Token (lorenzolottici-it_en) */
  --color-white: #fff; /* Canvas / Surface Token (lorenzolottici-it_en) */
  --spacing: .25rem; /* Layout / Spatial Grid Token (lorenzolottici-it_en) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#3080ff` — grounded in `var(--color-blue-500)` in `:root`
- **Primary Typography Ink**: `#000` — grounded in `var(--color-black)` in `:root`
- **Elevated Surface / Card Substrate**: `#fff` — grounded in `var(--color-white)` in `:root`
- **Interactive Accent / Highlight**: `#070707` — grounded in `var(--fondo)` in `:root`
- **Secondary / Muted Copy**: `#0b0c0f` — grounded in `var(--pietra)` in `:root`
- **Structural Hairline Border**: `#14140f` — grounded in `var(--inchiostro)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×24039px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `80rem` extracted from `lorenzolottici-it_en` stylesheet
- **Padding & Gutters**: `16px` lateral canvas padding with `8px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 80rem`, `gap: 8px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `16px` horizontal padding
- **Media Queries**: `@media (max-width:640px)`, `@media (max-width:760px)`, `@media (max-width:300px)`, `@media (prefers-reduced-motion:reduce)`
- **Corner Radii**: `50%`, `4px`, `.25rem`, `var(--radius-2xl)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `archivo`
- **Body Font Stack**: `archivo Fallback`
- **Monospace / Technical Font Stack**: `jetbrainsMono`
- **H1 Display Rule**: CSS variables `--font-display: var(--font-grande)`, `--tipo-display: clamp(2.75rem,calc(1.2708rem + 6.5741vw),7.1875rem)`, `--lh-display: .98`; rule `h1` (`font-size: var(--tipo-titolo)`, `line-height: var(--lh-titolo)`, `letter-spacing: var(--ls-titolo)`, `font-weight: var(--peso-di...`)
- **H2 Section Rule**: rule `h2` (`font-size: var(--tipo-label)`, `line-height: var(--lh-label)`, `letter-spacing: var(--ls-label)`, `font-weight: var(--peso-la...`)
- **Body Copy Rule**: rule `p` (`line-height: var(--lh-corpo)`)
- **Metadata & Index Rule**: CSS variables `--mono: var(--font-jetbrains-mono), ui-monospace, monospace`, `--font-jetbrains-mono: "jetbrainsMono", Courier New, ui-monospace, monospace`, `--text-xs: .75rem`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `lorenzolottici-it_en` (`Lorenzo Lottici · Order in chaos`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.indice-home> — `lorenzolottici-it_en`)**:
   - DOM & Selectors: Landmark `<header class="indice-home indice-testata">` hosting `Lorenzo Lottici · Order in chaos` navigation (`What I do · Path · Work · Thinking · Let’s talk`), DOM attributes (`data-testata="1"`, `data-caricamento="1"`, `data-tre="1"`, `data-precedence="next"`), and stylesheet rule `.iLAgaa_colonna { max-width:80rem;margin:0 auto;position:relative }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.indice-home> — `lorenzolottici-it_en`)` (`lorenzolottici-it_en`) adapts across `@media (max-width:640px)`, `@media (max-width:760px)`, `@media (max-width:300px)`, `@media (prefers-reduced-motion:reduce)` with `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)` transitions and links `What I do · Path · Work · Thinking · Let’s talk`.
2. **Hero Stage & Focal Lead (<section.dark> — `Websites and AI automation in Parm`)**:
   - DOM & Selectors: Landmark `<section class="dark">` presenting display lead `Websites and AI automation in Parma` and copy excerpt *"I’m Lorenzo Lottici. I bring order to the chaos in your business:"* over `#3080ff` canvas and `#fff` ink.
   - Responsive Contract: Hero stage (`1440×24039px` desktop / `390×2400px` mobile) sets `#3080ff` background with `#fff` headline `Websites and AI automation in Parma`.
3. **Primary Showcase & Content Grid (<section.js> — `What I do`)**:
   - DOM & Selectors: Landmark `<section class="js">` rendering section `What I do` with copy *"I give shape to your ideas. From solid corporate architecture to "*, asset references (`archivo_latin_var-s.p.3b1_7etm2gp...`, `jetbrains_mono_latin_var.p.0gbvn7...`, `polvere-carta.webp`, `420u9fgvjqgpl.js`), and grid rule `.iLAgaa_stelle { border-radius:50%;width:1px;height:1px;position:absolute;top:0;left:0 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.js> — `What I do`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 80rem`, `gap: 8px`) on desktop and Single-column vertical stack at `390px` viewport width with `16px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.scroll-fermo> — `Websites & e-commerce`)**:
   - DOM & Selectors: Landmark `<section class="scroll-fermo">` framing `Websites & e-commerce` and `AI & automation` (*"I take the weight off your hands. More time for people, zero oper"*) with `#fff` surface cards, `#070707` accents, and `.iLAgaa_pianeta { width:120vw;top:-74vw;right:-62vw }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.scroll-fermo> — `Websites & e-commerce`)` uses `50%`, `4px`, `.25rem`, `var(--radius-2xl)` radii, `#070707` highlights, and assets (archivo_latin_var-s.p.3b1_7etm2gp..., jetbrains_mono_latin_var.p.0gbvn7..., polvere-carta.webp).
5. **Colophon & Global Directory Footer (<footer.su-piede> — `https://lorenzolottici.it/en`)**:
   - DOM & Selectors: Landmark `<footer class="su-piede indice-home">` anchoring `Lorenzo Lottici · Order in chaos` footer links (`What I do · Path · Work · Thinking · Let’s talk`), copy *"Roxam : the site of a company that’s been building trade sho"*, and `#14140f` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.su-piede> — `https://lorenzolottici.it/en`)` aligns to `80rem` extracted from `lorenzolottici-it_en` stylesheet with `16px` lateral canvas padding with `8px` grid gap and attributes (data-testata="1", data-caricamento="1", data-tre="1").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"I’m Lorenzo Lottici. I bring order to the chaos in your business: the website and..."*
- Copy Excerpt 2: *"I give shape to your ideas. From solid corporate architecture to the most visionar..."*
- Copy Excerpt 3: *"I take the weight off your hands. More time for people, zero operational errors."*
- Copy Excerpt 4: *"Roxam : the site of a company that’s been building trade show stands since 1976."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`
- **Extracted Stylesheet Rules (`lorenzolottici-it_en`)**:
- `.iLAgaa_colonna { max-width:80rem;margin:0 auto;position:relative }`
- `.iLAgaa_stelle { border-radius:50%;width:1px;height:1px;position:absolute;top:0;left:0 }`
- `.iLAgaa_pianeta { width:120vw;top:-74vw;right:-62vw }`
- `.iLAgaa_vai { color:var(--tenue) }`
- `.iLAgaa_meta a { color:inherit;align-items:center;min-height:44px;margin:-12px 0;text-dec... }`
- **Per-Selector Transition Rules**:
- **Selector `._2ZgDjW_eroe[data-via=scivola]`**: `transition: transform var(--dur-scopri) var(--curva-uscita)` extracted from `lorenzolottici-it_en` stylesheet.
- **Selector `._2ZgDjW_piede`**: `transition: transform var(--dur-scopri) var(--curva)` extracted from `lorenzolottici-it_en` stylesheet.
- **Selector `html[data-lavori-esce] ._2ZgDjW_p...`**: `transition: transform var(--dur-stato) var(--curva)` extracted from `lorenzolottici-it_en` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,1,1)`)**: Governs interactive state transitions across `<header.indice-home>` and `<section.js>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Framer Motion Layout Physics with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `lorenzolottici-it_en`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
