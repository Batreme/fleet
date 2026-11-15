---
title: "UI Prompt Blueprint: www-lucaslima-design"
date: 2026-11-15
target: "[[overview|www-lucaslima-design]]"
status: analyzed
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#fafafb` / `#dce0e5`)"
---

# UI Design System & Master Generation Blueprint: www-lucaslima-design

> **Lucas Lima · Product designer and design engineer** (https://www.lucaslima.design/) — Brazilian product designer working across SaaS, finance and AI. I work directly in code, exploring live interfaces and bridging design an...

![Desktop Viewport Capture (1440x5927)](file:///root/projects/fleet/wiki/targets/www-lucaslima-design/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Lucas Lima · Product designer and design engineer** (`https://www.lucaslima.design/`). Brazilian product designer working across SaaS, finance and AI. I work directly in code, exploring live interfaces and bridging design an...
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#fafafb` / `#dce0e5`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fafafb` (`var(--color-gray-50)` in `:root`) paired with `#737b88` primary typography and `#dce0e5` accents.
  - **Extracted Typographic Hierarchy**: Pairs `DM Sans Variable` for display copy (`Senior Product Designer`) with `Inter Variable` and `Geist Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `1200px` container bounds (`gap: 16px`, padding `12px`) with `cubic-bezier(.23,1,.32,1)` easing and Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/www-lucaslima-design/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×5927px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `1200px` extracted from `www-lucaslima-design` stylesheet.
- **Canvas Lateral Padding & Spacing**: `12px` lateral canvas padding with `16px` grid gap.
- **Border Radius Scale**: `8px`, `50%`, `6px`, `12px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1200px`, `gap: 16px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `12px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (width<=1000px)`, `@media (prefers-reduced-motion:reduce)`, `@media (width<=540px)`, `@media (width<=700px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fafafb` | `var(--color-gray-50)` in `:root` |
| **Primary Typography Ink** | `#f2f3f5` | `var(--color-gray-100)` in `:root` |
| **Elevated Surface / Card Substrate** | `#e9ebee` | `var(--color-gray-200)` in `:root` |
| **Interactive Accent / Highlight** | `#dce0e5` | `var(--color-gray-300)` in `:root` |
| **Secondary / Muted Copy** | `#c1c6ce` | `var(--color-gray-400)` in `:root` |
| **Structural Hairline Border** | `#737b88` | `var(--color-gray-500)` in `:root` |
| **Variable Token (`--color-gray-600`)** | `#626a76` | `var(--color-gray-600)` in `:root` |
| **Variable Token (`--color-gray-700`)** | `#454c57` | `var(--color-gray-700)` in `:root` |
| **Variable Token (`--color-gray-800`)** | `#2c313a` | `var(--color-gray-800)` in `:root` |
| **Variable Token (`--color-gray-900`)** | `#1c2027` | `var(--color-gray-900)` in `:root` |
| **Variable Token (`--color-gray-950`)** | `#101318` | `var(--color-gray-950)` in `:root` |
| **Variable Token (`--cover-surface`)** | `#e9ebef` | `var(--cover-surface)` in `:root` |
| **Variable Token (`--cover-hover`)** | `#e3e6eb` | `var(--cover-hover)` in `:root` |
| **Variable Token (`--hairline`)** | `#1c202710` | `var(--hairline)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-gray-50` | `#fafafb` | Brand / Palette Token |
| `--color-gray-100` | `#f2f3f5` | Brand / Palette Token |
| `--color-gray-200` | `#e9ebee` | Brand / Palette Token |
| `--color-gray-300` | `#dce0e5` | Brand / Palette Token |
| `--color-gray-400` | `#c1c6ce` | Brand / Palette Token |
| `--color-gray-500` | `#737b88` | Brand / Palette Token |
| `--color-gray-600` | `#626a76` | Brand / Palette Token |
| `--color-gray-700` | `#454c57` | Brand / Palette Token |
| `--color-gray-800` | `#2c313a` | Brand / Palette Token |
| `--color-gray-900` | `#1c2027` | Brand / Palette Token |
| `--color-gray-950` | `#101318` | Brand / Palette Token |
| `--color-card-surface` | `#f2f3f5` | Canvas / Surface Token |
| `--color-card-fade` | `#f2f3f5` | Brand / Palette Token |
| `--cover-surface` | `#e9ebef` | Canvas / Surface Token |
| `--cover-hover` | `#e3e6eb` | Color / Atmospheric Token |
| `--hairline` | `#1c202710` | Color / Atmospheric Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `DM Sans Variable`.
- **Primary Body Stack**: `Inter Variable`.
- **Technical / Metadata Stack**: `Geist Mono`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--brand-display: 4rem`.
- **Section Heading (`H2`)**: rule `h2` (`letter-spacing: inherit`).
- **Body Copy**: CSS variables `--brand-body: 1rem`.
- **Metadata & Navigation Labels**: CSS variables `--font-mono: "Inter Variable", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif`, `--brand-caption: .8125rem`, `--default-mono-font-family: var(--font-mono)`; rule `small` (`font-size: 12px`, `font-weight: 400`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.23,1,.32,1)`, `cubic-bezier(.2,0,0,1)`, `cubic-bezier(.34,1.45,.64,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `media (prefers-reduced-motion:red...`**: `transition: .01ms!important` extracted from `www-lucaslima-design` stylesheet.
- **Selector `.simple-row`**: `transition: color .2s` extracted from `www-lucaslima-design` stylesheet.
- **Selector `.simple-industry`**: `transition: color .2s` extracted from `www-lucaslima-design` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.23,1,.32,1)`)**: Governs interactive state transitions across `<header.st-header>` and `<section.st-pad>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Lucas Lima · Product designer and design e │
│ ====================================================================== │
│ [ <header.st-header>       | Lucas Lima · Projects · Writing · Abou ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.st-pad>                                     |   │
│ | H1: Senior Product Designer                                      |   │
│ | Substrate: #fafafb    | Ink: #737b88    | Accent: #dce0e5        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.st-pad>          ) max-w: 1200px         |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Selected work                |  | Things I make on the side    | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 16px  ) | │
│ | [<header.st-header>] -> [<section.st-pad>] -> [<section.st-pad>] |   │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.st-footer>    ) | https://www.lucaslima.design/      │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.st-header> — `www-lucaslima-design`)**:
   - Landmark `<header class="st-header">` hosting `Lucas Lima · Product designer and de` navigation (`Lucas Lima · Projects · Writing · About · Photography`), DOM attributes (`data-theme="light"`, `data-prerendered="true"`, `data-js="live"`, `data-intro="play"`), and stylesheet rule `html { scroll-behavior:auto;scrollbar-gutter:stable }`.
2. **Hero Stage & Focal Lead (<section.st-pad> — `Senior Product Designer`)**:
   - Landmark `<section class="st-pad">` presenting display lead `Senior Product Designer` and copy excerpt *"hello@lucaslima.design Copied"* over `#fafafb` canvas and `#737b88` ink.
3. **Primary Showcase & Content Grid (<section.st-pad> — `Selected work`)**:
   - Landmark `<section class="st-pad">` rendering section `Selected work` with copy *"hello@lucaslima.design"*, asset references (`general-sans-500.woff2`, `general-sans-400.woff2`, `favicon.ico`, `favicon.svg`), and grid rule `body { font-family:var(--font-sans) }`.
4. **Interactive Detail & Feature Matrix (<section.st-pad> — `Things I make on the side`)**:
   - Landmark `<section class="st-pad">` framing `Things I make on the side` and `Writing` (*"And design engineer, designing in code"*) with `#e9ebee` surface cards, `#dce0e5` accents, and `.portfolio { min-height:100svh }`.
5. **Colophon & Global Directory Footer (<footer.st-footer> — `https://www.lucaslima.design/`)**:
   - Landmark `<footer class="st-footer">` anchoring `Lucas Lima · Product designer an` footer links (`Lucas Lima · Projects · Writing · About · Photography`), copy *"Lucas Lima is a Brazilian designer and psychologist with a s"*, and `#737b88` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-lucaslima-design (Lucas Lima · Product designer and design engineer)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-lucaslima-design` (**Lucas Lima · Product designer and design engineer** — `https://www.lucaslima.design/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fafafb` / `#dce0e5`).
- **Identity & Domain Context**: Brazilian product designer working across SaaS, finance and AI. I work directly in code, exploring live interfaces and bridging design an...
- **Primary Substrate**: `#fafafb` (`var(--color-gray-50)` in `:root`), **Primary Ink**: `#737b88`, **Accent / Highlight**: `#dce0e5`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fafafb` (`var(--color-gray-50)` in `:root`) paired with `#737b88` primary typography and `#dce0e5` accents.
  - **Extracted Typographic Hierarchy**: Pairs `DM Sans Variable` for display copy (`Senior Product Designer`) with `Inter Variable` and `Geist Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `1200px` container bounds (`gap: 16px`, padding `12px`) with `cubic-bezier(.23,1,.32,1)` easing and Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-lucaslima-design` in your global stylesheet:

:root {
  /* Lucas Lima · Product designer and design engineer (www-lucaslima-design) — Ground-Truth Extracted CSS Variables */
  --color-gray-50: #fafafb; /* Brand / Palette Token (www-lucaslima-design) */
  --color-gray-100: #f2f3f5; /* Brand / Palette Token (www-lucaslima-design) */
  --color-gray-200: #e9ebee; /* Brand / Palette Token (www-lucaslima-design) */
  --color-gray-300: #dce0e5; /* Brand / Palette Token (www-lucaslima-design) */
  --color-gray-400: #c1c6ce; /* Brand / Palette Token (www-lucaslima-design) */
  --color-gray-500: #737b88; /* Brand / Palette Token (www-lucaslima-design) */
  --color-gray-600: #626a76; /* Brand / Palette Token (www-lucaslima-design) */
  --color-gray-700: #454c57; /* Brand / Palette Token (www-lucaslima-design) */
  --color-gray-800: #2c313a; /* Brand / Palette Token (www-lucaslima-design) */
  --color-gray-900: #1c2027; /* Brand / Palette Token (www-lucaslima-design) */
  --color-gray-950: #101318; /* Brand / Palette Token (www-lucaslima-design) */
  --color-card-surface: #f2f3f5; /* Canvas / Surface Token (www-lucaslima-design) */
  --color-card-fade: #f2f3f5; /* Brand / Palette Token (www-lucaslima-design) */
  --cover-surface: #e9ebef; /* Canvas / Surface Token (www-lucaslima-design) */
  --cover-hover: #e3e6eb; /* Color / Atmospheric Token (www-lucaslima-design) */
  --hairline: #1c202710; /* Color / Atmospheric Token (www-lucaslima-design) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#fafafb` — grounded in `var(--color-gray-50)` in `:root`
- **Primary Typography Ink**: `#f2f3f5` — grounded in `var(--color-gray-100)` in `:root`
- **Elevated Surface / Card Substrate**: `#e9ebee` — grounded in `var(--color-gray-200)` in `:root`
- **Interactive Accent / Highlight**: `#dce0e5` — grounded in `var(--color-gray-300)` in `:root`
- **Secondary / Muted Copy**: `#c1c6ce` — grounded in `var(--color-gray-400)` in `:root`
- **Structural Hairline Border**: `#737b88` — grounded in `var(--color-gray-500)` in `:root`
- **Variable Token (`--color-gray-600`)**: `#626a76` — grounded in `var(--color-gray-600)` in `:root`
- **Variable Token (`--color-gray-700`)**: `#454c57` — grounded in `var(--color-gray-700)` in `:root`
- **Variable Token (`--color-gray-800`)**: `#2c313a` — grounded in `var(--color-gray-800)` in `:root`
- **Variable Token (`--color-gray-900`)**: `#1c2027` — grounded in `var(--color-gray-900)` in `:root`
- **Variable Token (`--color-gray-950`)**: `#101318` — grounded in `var(--color-gray-950)` in `:root`
- **Variable Token (`--cover-surface`)**: `#e9ebef` — grounded in `var(--cover-surface)` in `:root`
- **Variable Token (`--cover-hover`)**: `#e3e6eb` — grounded in `var(--cover-hover)` in `:root`
- **Variable Token (`--hairline`)**: `#1c202710` — grounded in `var(--hairline)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×5927px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1200px` extracted from `www-lucaslima-design` stylesheet
- **Padding & Gutters**: `12px` lateral canvas padding with `16px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1200px`, `gap: 16px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `12px` horizontal padding
- **Media Queries**: `@media (width<=1000px)`, `@media (prefers-reduced-motion:reduce)`, `@media (width<=540px)`, `@media (width<=700px)`
- **Corner Radii**: `8px`, `50%`, `6px`, `12px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `DM Sans Variable`
- **Body Font Stack**: `Inter Variable`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **H1 Display Rule**: CSS variables `--brand-display: 4rem`
- **H2 Section Rule**: rule `h2` (`letter-spacing: inherit`)
- **Body Copy Rule**: CSS variables `--brand-body: 1rem`
- **Metadata & Index Rule**: CSS variables `--font-mono: "Inter Variable", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif`, `--brand-caption: .8125rem`, `--default-mono-font-family: var(--font-mono)`; rule `small` (`font-size: 12px`, `font-weight: 400`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-lucaslima-design` (`Lucas Lima · Product designer and design engineer`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.st-header> — `www-lucaslima-design`)**:
   - DOM & Selectors: Landmark `<header class="st-header">` hosting `Lucas Lima · Product designer and de` navigation (`Lucas Lima · Projects · Writing · About · Photography`), DOM attributes (`data-theme="light"`, `data-prerendered="true"`, `data-js="live"`, `data-intro="play"`), and stylesheet rule `html { scroll-behavior:auto;scrollbar-gutter:stable }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.st-header> — `www-lucaslima-design`)` (`www-lucaslima-design`) adapts across `@media (width<=1000px)`, `@media (prefers-reduced-motion:reduce)`, `@media (width<=540px)`, `@media (width<=700px)` with `cubic-bezier(.23,1,.32,1)`, `cubic-bezier(.2,0,0,1)`, `cubic-bezier(.34,1.45,.64,1)` transitions and links `Lucas Lima · Projects · Writing · About · Photography`.
2. **Hero Stage & Focal Lead (<section.st-pad> — `Senior Product Designer`)**:
   - DOM & Selectors: Landmark `<section class="st-pad">` presenting display lead `Senior Product Designer` and copy excerpt *"hello@lucaslima.design Copied"* over `#fafafb` canvas and `#737b88` ink.
   - Responsive Contract: Hero stage (`1440×5927px` desktop / `390×2400px` mobile) sets `#fafafb` background with `#737b88` headline `Senior Product Designer`.
3. **Primary Showcase & Content Grid (<section.st-pad> — `Selected work`)**:
   - DOM & Selectors: Landmark `<section class="st-pad">` rendering section `Selected work` with copy *"hello@lucaslima.design"*, asset references (`general-sans-500.woff2`, `general-sans-400.woff2`, `favicon.ico`, `favicon.svg`), and grid rule `body { font-family:var(--font-sans) }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.st-pad> — `Selected work`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1200px`, `gap: 16px`) on desktop and Single-column vertical stack at `390px` viewport width with `12px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.st-pad> — `Things I make on the side`)**:
   - DOM & Selectors: Landmark `<section class="st-pad">` framing `Things I make on the side` and `Writing` (*"And design engineer, designing in code"*) with `#e9ebee` surface cards, `#dce0e5` accents, and `.portfolio { min-height:100svh }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.st-pad> — `Things I make on the side`)` uses `8px`, `50%`, `6px`, `12px` radii, `#dce0e5` highlights, and assets (general-sans-500.woff2, general-sans-400.woff2, favicon.ico).
5. **Colophon & Global Directory Footer (<footer.st-footer> — `https://www.lucaslima.design/`)**:
   - DOM & Selectors: Landmark `<footer class="st-footer">` anchoring `Lucas Lima · Product designer an` footer links (`Lucas Lima · Projects · Writing · About · Photography`), copy *"Lucas Lima is a Brazilian designer and psychologist with a s"*, and `#737b88` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.st-footer> — `https://www.lucaslima.design/`)` aligns to `1200px` extracted from `www-lucaslima-design` stylesheet with `12px` lateral canvas padding with `16px` grid gap and attributes (data-theme="light", data-prerendered="true", data-js="live").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"hello@lucaslima.design Copied"*
- Copy Excerpt 2: *"hello@lucaslima.design"*
- Copy Excerpt 3: *"And design engineer, designing in code"*
- Copy Excerpt 4: *"Lucas Lima is a Brazilian designer and psychologist with a soft spot for complex p..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.23,1,.32,1)`, `cubic-bezier(.2,0,0,1)`, `cubic-bezier(.34,1.45,.64,1)`
- **Extracted Stylesheet Rules (`www-lucaslima-design`)**:
- `html { scroll-behavior:auto;scrollbar-gutter:stable }`
- `body { font-family:var(--font-sans) }`
- `.portfolio { min-height:100svh }`
- `.portfolio button { -webkit-tap-highlight-color:transparent }`
- `.portfolio button:focus-visible { outline:2px solid var(--color-azure-500);outline-offset:5px }`
- **Per-Selector Transition Rules**:
- **Selector `media (prefers-reduced-motion:red...`**: `transition: .01ms!important` extracted from `www-lucaslima-design` stylesheet.
- **Selector `.simple-row`**: `transition: color .2s` extracted from `www-lucaslima-design` stylesheet.
- **Selector `.simple-industry`**: `transition: color .2s` extracted from `www-lucaslima-design` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.23,1,.32,1)`)**: Governs interactive state transitions across `<header.st-header>` and `<section.st-pad>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-lucaslima-design`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
