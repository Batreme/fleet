---
title: "UI Prompt Blueprint: trek-cards"
date: 2026-11-15
target: "trek-cards"
status: analyzed
capture: dom
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#18001A` / `#2E1650`)"
---

# UI Design System & Master Generation Blueprint: trek-cards

> **Trek Cards - The AI-Powered TCG Where Every Card Has a Story** (https://trek.cards/) — Trek Cards is the AI-powered trading card game (TCG). Craft UNIQUE character cards, battle players worldwide and track your cards around...

![Desktop Viewport Capture](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Trek Cards - The AI-Powered TCG Where Every Card Has a Story** (`https://trek.cards/`). Trek Cards is the AI-powered trading card game (TCG). Craft UNIQUE character cards, battle players worldwide and track your cards around...
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#18001A` / `#2E1650`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#18001A` (`var(--ground)` in `:root`) paired with `#FF00EE` primary typography and `#2E1650` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Rubik One` for display copy (`Every card has a story.`) with `Rubik` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `860px` container bounds (`gap: 10px`, padding `1px`) with `cubic-bezier(.2,.8,.2,1)` easing and Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `860px` extracted from `trek-cards` stylesheet.
- **Canvas Lateral Padding & Spacing**: `1px` lateral canvas padding with `10px` grid gap.
- **Border Radius Scale**: `6px`, `50%`, `24px`, `100px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 860px`, `gap: 10px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `1px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width: 860px)`, `@media (max-width: 900px)`, `@media (max-width: 1000px)`, `@media (min-width: 821px) and (max-width: 1100px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#18001A` | `var(--ground)` in `:root` |
| **Primary Typography Ink** | `#1A0A2E` | `var(--bg)` in `:root` |
| **Elevated Surface / Card Substrate** | `#221041` | `var(--surface)` in `:root` |
| **Interactive Accent / Highlight** | `#2E1650` | `var(--surface-2)` in `:root` |
| **Secondary / Muted Copy** | `#6A00FF` | `var(--purple)` in `:root` |
| **Structural Hairline Border** | `#FF00EE` | `var(--pink)` in `:root` |
| **Variable Token (`--lilac`)** | `#B176FF` | `var(--lilac)` in `:root` |
| **Variable Token (`--ink`)** | `#FFFFFF` | `var(--ink)` in `:root` |
| **Variable Token (`--muted`)** | `#B6A6D6` | `var(--muted)` in `:root` |
| **Variable Token (`--green`)** | `#68FF8E` | `var(--green)` in `:root` |
| **Variable Token (`--brand`)** | `#7B22FF` | `var(--brand)` in `:root` |
| **Variable Token (`--brand`)** | `#C215F6` | `var(--brand)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ground` | `#18001A` | Color / Atmospheric Token |
| `--bg` | `#1A0A2E` | Canvas / Surface Token |
| `--surface` | `#221041` | Canvas / Surface Token |
| `--surface-2` | `#2E1650` | Canvas / Surface Token |
| `--purple` | `#6A00FF` | Color / Atmospheric Token |
| `--pink` | `#FF00EE` | Typography Ink Token |
| `--lilac` | `#B176FF` | Color / Atmospheric Token |
| `--ink` | `#FFFFFF` | Typography Ink Token |
| `--muted` | `#B6A6D6` | Color / Atmospheric Token |
| `--soft` | `rgba(255, 255, 255, 0.72)` | Color / Atmospheric Token |
| `--stroke` | `rgba(255, 255, 255, 0.08)` | Elevation / Border Token |
| `--green` | `#68FF8E` | Color / Atmospheric Token |
| `--title` | `'Rubik One', 'Rubik', sans-serif` | Design System Custom Token |
| `--body` | `'Rubik', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif` | Dimension / Scale Token |
| `--brand` | `linear-gradient(55deg, #7B22FF 0%, #C215F6 38%, #FF00EE 82%)` | Brand / Palette Token |
| `--ease` | `cubic-bezier(.2, .8, .2, 1)` | Motion / Easing Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Rubik One`.
- **Primary Body Stack**: `Rubik`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: rule `.title` (`line-height: .98`, `letter-spacing: -0.03em`, `font-weight: 400`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(38px, 6vw, 92px)`).
- **Body Copy**: CSS variables `--body: 'Rubik', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif`; rule `body` (`font-size: 17px`, `line-height: 1.6`).
- **Metadata & Navigation Labels**: rule `small` (`font-size: 11px`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.2,.8,.2,1)`, `cubic-bezier(.2,.6,.35,1)`, `cubic-bezier(.37,0,.63,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.cursor-glow`**: `transition: opacity .6s` extracted from `trek-cards` stylesheet.
- **Selector `.btn`**: `transition: transform .25s var(--ease), box-shadow .3s` extracted from `trek-cards` stylesheet.
- **Selector `.btn--glass::after`**: `transition: opacity .4s` extracted from `trek-cards` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.2,.8,.2,1)`)**: Governs interactive state transitions across `<header.nav>` and `<section.prologue>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Trek Cards - The AI-Powered TCG Where Ever │
│ ====================================================================== │
│ [ <header.nav>             | Craft · Battle · Journey · Legacy · Co ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hero>                                       |   │
│ | H1: Every card has a story.                                      |   │
│ | Substrate: #18001A    | Ink: #FF00EE    | Accent: #2E1650        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.prologue>        ) max-w: 860px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Craft your Unique            |  | 1 Describe your character    | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 10px  ) | │
│ | [<header.nav>] -> [<section.hero>] -> [<section.prologue>] |         │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.foot>         ) | https://trek.cards/                │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.nav> — `trek-cards`)**:
   - Landmark `<header class="nav">` hosting `Trek Cards - The AI-Powered TCG Wher` navigation (`Craft · Battle · Journey · Legacy · Collect`), DOM attributes (`data-notify`, `data-when="prelaunch"`, `data-when="launch"`, `data-key="kravix"`), and stylesheet rule `font-face { font-family: 'Rubik One'; src: url('../fonts/rubik-one.woff') format('wo... }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Every card has a story.`)**:
   - Landmark `<section class="hero">` presenting display lead `Every card has a story.` and copy excerpt *"Download on the App Store"* over `#18001A` canvas and `#FF00EE` ink.
3. **Primary Showcase & Content Grid (<section.prologue> — `Craft your Unique`)**:
   - Landmark `<section class="prologue">` rendering section `Craft your Unique` with copy *"For iPhone iOS 17 or later"*, asset references (`favicon-32x32.png`, `apple-touch-icon.png`, `site.css`, `trek-logo.webp (Trek Cards)`), and grid rule `after { box-sizing: border-box; margin: 0; padding: 0; }`.
4. **Interactive Detail & Feature Matrix (<section.chapter> — `1 Describe your character`)**:
   - Landmark `<section class="chapter ch-craft">` framing `1 Describe your character` and `2 Choose a frame` (*"Get it on Google Play"*) with `#221041` surface cards, `#2E1650` accents, and `html { -webkit-text-size-adjust: 100%; overflow-x: hidden; overflow-x: clip; }`.
5. **Colophon & Global Directory Footer (<footer.foot> — `https://trek.cards/`)**:
   - Landmark `<footer class="foot">` anchoring `Trek Cards - The AI-Powered TCG ` footer links (`Craft · Battle · Journey · Legacy · Collect`), copy *"For Android On Google Play"*, and `#FF00EE` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: trek-cards (Trek Cards - The AI-Powered TCG Where Every Card Has a Story)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `trek-cards` (**Trek Cards - The AI-Powered TCG Where Every Card Has a Story** — `https://trek.cards/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#18001A` / `#2E1650`).
- **Identity & Domain Context**: Trek Cards is the AI-powered trading card game (TCG). Craft UNIQUE character cards, battle players worldwide and track your cards around...
- **Primary Substrate**: `#18001A` (`var(--ground)` in `:root`), **Primary Ink**: `#FF00EE`, **Accent / Highlight**: `#2E1650`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#18001A` (`var(--ground)` in `:root`) paired with `#FF00EE` primary typography and `#2E1650` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Rubik One` for display copy (`Every card has a story.`) with `Rubik` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `860px` container bounds (`gap: 10px`, padding `1px`) with `cubic-bezier(.2,.8,.2,1)` easing and Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `trek-cards` in your global stylesheet:

:root {
  /* Trek Cards - The AI-Powered TCG Where Every Card Has a Story (trek-cards) — Ground-Truth Extracted CSS Variables */
  --ground: #18001A; /* Color / Atmospheric Token (trek-cards) */
  --bg: #1A0A2E; /* Canvas / Surface Token (trek-cards) */
  --surface: #221041; /* Canvas / Surface Token (trek-cards) */
  --surface-2: #2E1650; /* Canvas / Surface Token (trek-cards) */
  --purple: #6A00FF; /* Color / Atmospheric Token (trek-cards) */
  --pink: #FF00EE; /* Typography Ink Token (trek-cards) */
  --lilac: #B176FF; /* Color / Atmospheric Token (trek-cards) */
  --ink: #FFFFFF; /* Typography Ink Token (trek-cards) */
  --muted: #B6A6D6; /* Color / Atmospheric Token (trek-cards) */
  --soft: rgba(255, 255, 255, 0.72); /* Color / Atmospheric Token (trek-cards) */
  --stroke: rgba(255, 255, 255, 0.08); /* Elevation / Border Token (trek-cards) */
  --green: #68FF8E; /* Color / Atmospheric Token (trek-cards) */
  --title: 'Rubik One', 'Rubik', sans-serif; /* Design System Custom Token (trek-cards) */
  --body: 'Rubik', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; /* Dimension / Scale Token (trek-cards) */
  --brand: linear-gradient(55deg, #7B22FF 0%, #C215F6 38%, #FF00EE 82%); /* Brand / Palette Token (trek-cards) */
  --ease: cubic-bezier(.2, .8, .2, 1); /* Motion / Easing Token (trek-cards) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#18001A` — grounded in `var(--ground)` in `:root`
- **Primary Typography Ink**: `#1A0A2E` — grounded in `var(--bg)` in `:root`
- **Elevated Surface / Card Substrate**: `#221041` — grounded in `var(--surface)` in `:root`
- **Interactive Accent / Highlight**: `#2E1650` — grounded in `var(--surface-2)` in `:root`
- **Secondary / Muted Copy**: `#6A00FF` — grounded in `var(--purple)` in `:root`
- **Structural Hairline Border**: `#FF00EE` — grounded in `var(--pink)` in `:root`
- **Variable Token (`--lilac`)**: `#B176FF` — grounded in `var(--lilac)` in `:root`
- **Variable Token (`--ink`)**: `#FFFFFF` — grounded in `var(--ink)` in `:root`
- **Variable Token (`--muted`)**: `#B6A6D6` — grounded in `var(--muted)` in `:root`
- **Variable Token (`--green`)**: `#68FF8E` — grounded in `var(--green)` in `:root`
- **Variable Token (`--brand`)**: `#7B22FF` — grounded in `var(--brand)` in `:root`
- **Variable Token (`--brand`)**: `#C215F6` — grounded in `var(--brand)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `860px` extracted from `trek-cards` stylesheet
- **Padding & Gutters**: `1px` lateral canvas padding with `10px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 860px`, `gap: 10px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `1px` horizontal padding
- **Media Queries**: `@media (max-width: 860px)`, `@media (max-width: 900px)`, `@media (max-width: 1000px)`, `@media (min-width: 821px) and (max-width: 1100px)`
- **Corner Radii**: `6px`, `50%`, `24px`, `100px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Rubik One`
- **Body Font Stack**: `Rubik`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: rule `.title` (`line-height: .98`, `letter-spacing: -0.03em`, `font-weight: 400`)
- **H2 Section Rule**: rule `h2` (`font-size: clamp(38px, 6vw, 92px)`)
- **Body Copy Rule**: CSS variables `--body: 'Rubik', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif`; rule `body` (`font-size: 17px`, `line-height: 1.6`)
- **Metadata & Index Rule**: rule `small` (`font-size: 11px`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `trek-cards` (`Trek Cards - The AI-Powered TCG Where Every Card Has a Story`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.nav> — `trek-cards`)**:
   - DOM & Selectors: Landmark `<header class="nav">` hosting `Trek Cards - The AI-Powered TCG Wher` navigation (`Craft · Battle · Journey · Legacy · Collect`), DOM attributes (`data-notify`, `data-when="prelaunch"`, `data-when="launch"`, `data-key="kravix"`), and stylesheet rule `font-face { font-family: 'Rubik One'; src: url('../fonts/rubik-one.woff') format('wo... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.nav> — `trek-cards`)` (`trek-cards`) adapts across `@media (max-width: 860px)`, `@media (max-width: 900px)`, `@media (max-width: 1000px)`, `@media (min-width: 821px) and (max-width: 1100px)` with `cubic-bezier(.2,.8,.2,1)`, `cubic-bezier(.2,.6,.35,1)`, `cubic-bezier(.37,0,.63,1)` transitions and links `Craft · Battle · Journey · Legacy · Collect`.
2. **Hero Stage & Focal Lead (<section.hero> — `Every card has a story.`)**:
   - DOM & Selectors: Landmark `<section class="hero">` presenting display lead `Every card has a story.` and copy excerpt *"Download on the App Store"* over `#18001A` canvas and `#FF00EE` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#18001A` background with `#FF00EE` headline `Every card has a story.`.
3. **Primary Showcase & Content Grid (<section.prologue> — `Craft your Unique`)**:
   - DOM & Selectors: Landmark `<section class="prologue">` rendering section `Craft your Unique` with copy *"For iPhone iOS 17 or later"*, asset references (`favicon-32x32.png`, `apple-touch-icon.png`, `site.css`, `trek-logo.webp (Trek Cards)`), and grid rule `after { box-sizing: border-box; margin: 0; padding: 0; }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.prologue> — `Craft your Unique`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 860px`, `gap: 10px`) on desktop and Single-column vertical stack at `390px` viewport width with `1px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.chapter> — `1 Describe your character`)**:
   - DOM & Selectors: Landmark `<section class="chapter ch-craft">` framing `1 Describe your character` and `2 Choose a frame` (*"Get it on Google Play"*) with `#221041` surface cards, `#2E1650` accents, and `html { -webkit-text-size-adjust: 100%; overflow-x: hidden; overflow-x: clip; }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.chapter> — `1 Describe your character`)` uses `6px`, `50%`, `24px`, `100px` radii, `#2E1650` highlights, and assets (favicon-32x32.png, apple-touch-icon.png, site.css).
5. **Colophon & Global Directory Footer (<footer.foot> — `https://trek.cards/`)**:
   - DOM & Selectors: Landmark `<footer class="foot">` anchoring `Trek Cards - The AI-Powered TCG ` footer links (`Craft · Battle · Journey · Legacy · Collect`), copy *"For Android On Google Play"*, and `#FF00EE` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.foot> — `https://trek.cards/`)` aligns to `860px` extracted from `trek-cards` stylesheet with `1px` lateral canvas padding with `10px` grid gap and attributes (data-notify, data-when="prelaunch", data-when="launch").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Download on the App Store"*
- Copy Excerpt 2: *"For iPhone iOS 17 or later"*
- Copy Excerpt 3: *"Get it on Google Play"*
- Copy Excerpt 4: *"For Android On Google Play"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.2,.8,.2,1)`, `cubic-bezier(.2,.6,.35,1)`, `cubic-bezier(.37,0,.63,1)`
- **Extracted Stylesheet Rules (`trek-cards`)**:
- `font-face { font-family: 'Rubik One'; src: url('../fonts/rubik-one.woff') format('wo... }`
- `after { box-sizing: border-box; margin: 0; padding: 0; }`
- `html { -webkit-text-size-adjust: 100%; overflow-x: hidden; overflow-x: clip; }`
- `img { max-width: 100%; height: auto; display: block; }`
- `button { font: inherit; color: inherit; background: none; border: 0; cursor: poin... }`
- **Per-Selector Transition Rules**:
- **Selector `.cursor-glow`**: `transition: opacity .6s` extracted from `trek-cards` stylesheet.
- **Selector `.btn`**: `transition: transform .25s var(--ease), box-shadow .3s` extracted from `trek-cards` stylesheet.
- **Selector `.btn--glass::after`**: `transition: opacity .4s` extracted from `trek-cards` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.2,.8,.2,1)`)**: Governs interactive state transitions across `<header.nav>` and `<section.prologue>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `trek-cards`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
