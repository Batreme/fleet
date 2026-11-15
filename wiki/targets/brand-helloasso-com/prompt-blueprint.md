---
title: "UI Prompt Blueprint: brand-helloasso-com"
date: 2026-11-15
target: "brand-helloasso-com"
status: analyzed
capture: specimen
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#101010` / `#cdced0`)"
---

# UI Design System & Master Generation Blueprint: brand-helloasso-com

> **Accueil – Brandbook HelloAsso** (https://brand.helloasso.com/) — Logotype, typographie, couleurs, direction photographique et identité verbale de HelloAsso.

![Desktop Viewport Capture](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Accueil – Brandbook HelloAsso** (`https://brand.helloasso.com/`). Logotype, typographie, couleurs, direction photographique et identité verbale de HelloAsso.
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#101010` / `#cdced0`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#101010` (`var(--color-noir)` in `:root`) paired with `#fff` primary typography and `#cdced0` accents.
  - **Extracted Typographic Hierarchy**: Pairs `ITC Franklin Gothic LT` for display copy (`Accueil – Brandbook HelloAsso`) with `ABC Diatype Rounded` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `80px` container bounds (`gap: 12px`, padding `var(--space-32)`) with `cubic-bezier(.16,1,.3,1)` easing and Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Design Specimen (Offline WebGL/JS Fallback — not live site capture)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×5580px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `80px` extracted from `brand-helloasso-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `var(--space-32)` lateral canvas padding with `12px` grid gap.
- **Border Radius Scale**: `21.8%`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 80px`, `gap: 12px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--space-32)` horizontal padding.
- **Extracted CSS Media Queries**: `@media (prefers-reduced-motion)`, `@media (width<=767px)`, `@media (prefers-reduced-motion:reduce)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#101010` | `var(--color-noir)` in `:root` |
| **Primary Typography Ink** | `#434649` | `var(--color-gris-fonce)` in `:root` |
| **Elevated Surface / Card Substrate** | `#888c8f` | `var(--color-gris)` in `:root` |
| **Interactive Accent / Highlight** | `#cdced0` | `var(--color-gris-clair)` in `:root` |
| **Secondary / Muted Copy** | `#f5f5f5` | `var(--color-gris-tres-clair)` in `:root` |
| **Structural Hairline Border** | `#fff` | `var(--color-blanc)` in `:root` |
| **Variable Token (`--color-vert`)** | `#4a8100` | `var(--color-vert)` in `:root` |
| **Variable Token (`--color-vanille`)** | `#fdffc6` | `var(--color-vanille)` in `:root` |
| **Variable Token (`--color-rose`)** | `#fba2ec` | `var(--color-rose)` in `:root` |
| **Variable Token (`--color-sahara`)** | `#b38806` | `var(--color-sahara)` in `:root` |
| **Variable Token (`--color-lila`)** | `#f1edff` | `var(--color-lila)` in `:root` |
| **Variable Token (`--color-cuir`)** | `#644a02` | `var(--color-cuir)` in `:root` |
| **Variable Token (`--color-prune`)** | `#572a37` | `var(--color-prune)` in `:root` |
| **Variable Token (`--color-sport-jaune-fluo`)** | `#d7e103` | `var(--color-sport-jaune-fluo)` in `:root` |
| **Variable Token (`--color-sport-logo-fond-clair`)** | `#c6cf0e` | `var(--color-sport-logo-fond-clair)` in `:root` |
| **Variable Token (`--color-sport-anthracite`)** | `#504e44` | `var(--color-sport-anthracite)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-noir` | `#101010` | Brand / Palette Token |
| `--color-gris-fonce` | `#434649` | Brand / Palette Token |
| `--color-gris` | `#888c8f` | Brand / Palette Token |
| `--color-gris-clair` | `#cdced0` | Brand / Palette Token |
| `--color-gris-tres-clair` | `#f5f5f5` | Brand / Palette Token |
| `--color-blanc` | `#fff` | Brand / Palette Token |
| `--color-vert` | `#4a8100` | Brand / Palette Token |
| `--color-vanille` | `#fdffc6` | Brand / Palette Token |
| `--color-rose` | `#fba2ec` | Brand / Palette Token |
| `--color-sahara` | `#b38806` | Brand / Palette Token |
| `--color-lila` | `#f1edff` | Brand / Palette Token |
| `--color-cuir` | `#644a02` | Brand / Palette Token |
| `--color-prune` | `#572a37` | Brand / Palette Token |
| `--color-sport-jaune-fluo` | `#d7e103` | Brand / Palette Token |
| `--color-sport-logo-fond-clair` | `#c6cf0e` | Brand / Palette Token |
| `--color-sport-anthracite` | `#504e44` | Brand / Palette Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `ITC Franklin Gothic LT`.
- **Primary Body Stack**: `ABC Diatype Rounded`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--font-display: "ITC Franklin Gothic LT", "Arial Narrow", sans-serif`, `--fs-h1: 64px`, `--lh-h1: 58px`.
- **Section Heading (`H2`)**: CSS variables `--fs-h2: 48px`, `--lh-h2: 43px`.
- **Body Copy**: CSS variables `--fs-body: 14px`, `--lh-body: 18px`, `--fs-body-s: 14px`.
- **Metadata & Navigation Labels**: CSS variables `--fs-caption: 12px`, `--lh-caption: 17px`, `--caption-gap: var(--space-12)`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.7,0,.2,1)`, `cubic-bezier(.2,.3,.1,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `media (prefers-reduced-motion:red...`**: `transition: 1ms!important` extracted from `brand-helloasso-com` stylesheet.
- **Selector `.hlabel`**: `transition: opacity .3s,transform .4s cubic-bezier(.16,1,.3,1)` extracted from `brand-helloasso-com` stylesheet.
- **Selector `.harrow__i`**: `transition: transform 1s cubic-bezier(.16,1,.3,1)` extracted from `brand-helloasso-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.16,1,.3,1)`)**: Governs interactive state transitions across `<header.is-ready>` and `<section.chapter>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Accueil – Brandbook HelloAsso              │
│ ====================================================================== │
│ [ <header.is-ready>        | BRUNO                                  ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.chapter>                                    |   │
│ | H1: Accueil – Brandbook HelloAsso                                |   │
│ | Substrate: #101010    | Ink: #fff       | Accent: #cdced0        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.chapter>         ) max-w: 80px           |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Featured Work & Interactive  |  | Technical Architecture & Nar | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 12px  ) | │
│ | [<header.is-ready>] -> [<section.chapter>] -> [<section.chapter>] |  │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.cell-border>  ) | https://brand.helloasso.com/       │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.is-ready> — `brand-helloasso-com`)**:
   - Landmark `<header class="is-ready">` hosting `Accueil – Brandbook HelloAsso` navigation (`BRUNO`), DOM attributes (`data-astro-transition-scope="astro-nfpogox7-1"`, `data-layout="fullscreen"`, `data-astro-exec`, `data-svg-origin="24 512"`), and stylesheet rule `root { --fs-h1:var(--fs-h2);--lh-h1:var(--lh-h2) }`.
2. **Hero Stage & Focal Lead (<section.chapter> — `Accueil – Brandbook HelloAsso`)**:
   - Landmark `<section class="chapter">` presenting display lead `Accueil – Brandbook HelloAsso` and copy excerpt *"L’engagement rend les gens meilleurs."* over `#101010` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.chapter> — `Featured Work & Interactive Showca`)**:
   - Landmark `<section class="chapter">` rendering section `Featured Work & Interactive Showcase` with copy *"Accueil – Brandbook HelloAsso"*, asset references (`favicon.svg`, `favicon-32.png`, `apple-touch-icon.png`, `ITCFranklinGothicLT-DemiCompresse...`), and grid rule `after { box-sizing:border-box }`.
4. **Interactive Detail & Feature Matrix (<section.chapter> — `Technical Architecture & Narrative`)**:
   - Landmark `<section class="chapter">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Featured Work & Interactive Showcase"*) with `#888c8f` surface cards, `#cdced0` accents, and `svg { max-width:100%;display:block }`.
5. **Colophon & Global Directory Footer (<footer.cell-border> — `https://brand.helloasso.com/`)**:
   - Landmark `<footer class="cell-border">` anchoring `Accueil – Brandbook HelloAsso` footer links (`BRUNO`), copy *"Technical Architecture & Narrative"*, and `#fff` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: brand-helloasso-com (Accueil – Brandbook HelloAsso)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `brand-helloasso-com` (**Accueil – Brandbook HelloAsso** — `https://brand.helloasso.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#101010` / `#cdced0`).
- **Identity & Domain Context**: Logotype, typographie, couleurs, direction photographique et identité verbale de HelloAsso.
- **Primary Substrate**: `#101010` (`var(--color-noir)` in `:root`), **Primary Ink**: `#fff`, **Accent / Highlight**: `#cdced0`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#101010` (`var(--color-noir)` in `:root`) paired with `#fff` primary typography and `#cdced0` accents.
  - **Extracted Typographic Hierarchy**: Pairs `ITC Franklin Gothic LT` for display copy (`Accueil – Brandbook HelloAsso`) with `ABC Diatype Rounded` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `80px` container bounds (`gap: 12px`, padding `var(--space-32)`) with `cubic-bezier(.16,1,.3,1)` easing and Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `brand-helloasso-com` in your global stylesheet:

:root {
  /* Accueil – Brandbook HelloAsso (brand-helloasso-com) — Ground-Truth Extracted CSS Variables */
  --color-noir: #101010; /* Brand / Palette Token (brand-helloasso-com) */
  --color-gris-fonce: #434649; /* Brand / Palette Token (brand-helloasso-com) */
  --color-gris: #888c8f; /* Brand / Palette Token (brand-helloasso-com) */
  --color-gris-clair: #cdced0; /* Brand / Palette Token (brand-helloasso-com) */
  --color-gris-tres-clair: #f5f5f5; /* Brand / Palette Token (brand-helloasso-com) */
  --color-blanc: #fff; /* Brand / Palette Token (brand-helloasso-com) */
  --color-vert: #4a8100; /* Brand / Palette Token (brand-helloasso-com) */
  --color-vanille: #fdffc6; /* Brand / Palette Token (brand-helloasso-com) */
  --color-rose: #fba2ec; /* Brand / Palette Token (brand-helloasso-com) */
  --color-sahara: #b38806; /* Brand / Palette Token (brand-helloasso-com) */
  --color-lila: #f1edff; /* Brand / Palette Token (brand-helloasso-com) */
  --color-cuir: #644a02; /* Brand / Palette Token (brand-helloasso-com) */
  --color-prune: #572a37; /* Brand / Palette Token (brand-helloasso-com) */
  --color-sport-jaune-fluo: #d7e103; /* Brand / Palette Token (brand-helloasso-com) */
  --color-sport-logo-fond-clair: #c6cf0e; /* Brand / Palette Token (brand-helloasso-com) */
  --color-sport-anthracite: #504e44; /* Brand / Palette Token (brand-helloasso-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#101010` — grounded in `var(--color-noir)` in `:root`
- **Primary Typography Ink**: `#434649` — grounded in `var(--color-gris-fonce)` in `:root`
- **Elevated Surface / Card Substrate**: `#888c8f` — grounded in `var(--color-gris)` in `:root`
- **Interactive Accent / Highlight**: `#cdced0` — grounded in `var(--color-gris-clair)` in `:root`
- **Secondary / Muted Copy**: `#f5f5f5` — grounded in `var(--color-gris-tres-clair)` in `:root`
- **Structural Hairline Border**: `#fff` — grounded in `var(--color-blanc)` in `:root`
- **Variable Token (`--color-vert`)**: `#4a8100` — grounded in `var(--color-vert)` in `:root`
- **Variable Token (`--color-vanille`)**: `#fdffc6` — grounded in `var(--color-vanille)` in `:root`
- **Variable Token (`--color-rose`)**: `#fba2ec` — grounded in `var(--color-rose)` in `:root`
- **Variable Token (`--color-sahara`)**: `#b38806` — grounded in `var(--color-sahara)` in `:root`
- **Variable Token (`--color-lila`)**: `#f1edff` — grounded in `var(--color-lila)` in `:root`
- **Variable Token (`--color-cuir`)**: `#644a02` — grounded in `var(--color-cuir)` in `:root`
- **Variable Token (`--color-prune`)**: `#572a37` — grounded in `var(--color-prune)` in `:root`
- **Variable Token (`--color-sport-jaune-fluo`)**: `#d7e103` — grounded in `var(--color-sport-jaune-fluo)` in `:root`
- **Variable Token (`--color-sport-logo-fond-clair`)**: `#c6cf0e` — grounded in `var(--color-sport-logo-fond-clair)` in `:root`
- **Variable Token (`--color-sport-anthracite`)**: `#504e44` — grounded in `var(--color-sport-anthracite)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×5580px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `80px` extracted from `brand-helloasso-com` stylesheet
- **Padding & Gutters**: `var(--space-32)` lateral canvas padding with `12px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 80px`, `gap: 12px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--space-32)` horizontal padding
- **Media Queries**: `@media (prefers-reduced-motion)`, `@media (width<=767px)`, `@media (prefers-reduced-motion:reduce)`
- **Corner Radii**: `21.8%`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `ITC Franklin Gothic LT`
- **Body Font Stack**: `ABC Diatype Rounded`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: CSS variables `--font-display: "ITC Franklin Gothic LT", "Arial Narrow", sans-serif`, `--fs-h1: 64px`, `--lh-h1: 58px`
- **H2 Section Rule**: CSS variables `--fs-h2: 48px`, `--lh-h2: 43px`
- **Body Copy Rule**: CSS variables `--fs-body: 14px`, `--lh-body: 18px`, `--fs-body-s: 14px`
- **Metadata & Index Rule**: CSS variables `--fs-caption: 12px`, `--lh-caption: 17px`, `--caption-gap: var(--space-12)`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `brand-helloasso-com` (`Accueil – Brandbook HelloAsso`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.is-ready> — `brand-helloasso-com`)**:
   - DOM & Selectors: Landmark `<header class="is-ready">` hosting `Accueil – Brandbook HelloAsso` navigation (`BRUNO`), DOM attributes (`data-astro-transition-scope="astro-nfpogox7-1"`, `data-layout="fullscreen"`, `data-astro-exec`, `data-svg-origin="24 512"`), and stylesheet rule `root { --fs-h1:var(--fs-h2);--lh-h1:var(--lh-h2) }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.is-ready> — `brand-helloasso-com`)` (`brand-helloasso-com`) adapts across `@media (prefers-reduced-motion)`, `@media (width<=767px)`, `@media (prefers-reduced-motion:reduce)` with `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.7,0,.2,1)`, `cubic-bezier(.2,.3,.1,1)` transitions and links `BRUNO`.
2. **Hero Stage & Focal Lead (<section.chapter> — `Accueil – Brandbook HelloAsso`)**:
   - DOM & Selectors: Landmark `<section class="chapter">` presenting display lead `Accueil – Brandbook HelloAsso` and copy excerpt *"L’engagement rend les gens meilleurs."* over `#101010` canvas and `#fff` ink.
   - Responsive Contract: Hero stage (`1440×5580px` desktop / `390×2400px` mobile) sets `#101010` background with `#fff` headline `Accueil – Brandbook HelloAsso`.
3. **Primary Showcase & Content Grid (<section.chapter> — `Featured Work & Interactive Showca`)**:
   - DOM & Selectors: Landmark `<section class="chapter">` rendering section `Featured Work & Interactive Showcase` with copy *"Accueil – Brandbook HelloAsso"*, asset references (`favicon.svg`, `favicon-32.png`, `apple-touch-icon.png`, `ITCFranklinGothicLT-DemiCompresse...`), and grid rule `after { box-sizing:border-box }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.chapter> — `Featured Work & Interactive Showca`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 80px`, `gap: 12px`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--space-32)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.chapter> — `Technical Architecture & Narrative`)**:
   - DOM & Selectors: Landmark `<section class="chapter">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Featured Work & Interactive Showcase"*) with `#888c8f` surface cards, `#cdced0` accents, and `svg { max-width:100%;display:block }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.chapter> — `Technical Architecture & Narrative`)` uses `21.8%` radii, `#cdced0` highlights, and assets (favicon.svg, favicon-32.png, apple-touch-icon.png).
5. **Colophon & Global Directory Footer (<footer.cell-border> — `https://brand.helloasso.com/`)**:
   - DOM & Selectors: Landmark `<footer class="cell-border">` anchoring `Accueil – Brandbook HelloAsso` footer links (`BRUNO`), copy *"Technical Architecture & Narrative"*, and `#fff` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.cell-border> — `https://brand.helloasso.com/`)` aligns to `80px` extracted from `brand-helloasso-com` stylesheet with `var(--space-32)` lateral canvas padding with `12px` grid gap and attributes (data-astro-transition-scope="astro-nfpogox7-1", data-layout="fullscreen", data-astro-exec).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"L’engagement rend les gens meilleurs."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.7,0,.2,1)`, `cubic-bezier(.2,.3,.1,1)`
- **Extracted Stylesheet Rules (`brand-helloasso-com`)**:
- `root { --fs-h1:var(--fs-h2);--lh-h1:var(--lh-h2) }`
- `after { box-sizing:border-box }`
- `svg { max-width:100%;display:block }`
- `button { font:inherit;color:inherit;cursor:pointer;background:0 0;border:0;padding:0 }`
- `focus-visible { outline:var(--focus-width) solid var(--focus-color);outline-offset:var(-... }`
- **Per-Selector Transition Rules**:
- **Selector `media (prefers-reduced-motion:red...`**: `transition: 1ms!important` extracted from `brand-helloasso-com` stylesheet.
- **Selector `.hlabel`**: `transition: opacity .3s,transform .4s cubic-bezier(.16,1,.3,1)` extracted from `brand-helloasso-com` stylesheet.
- **Selector `.harrow__i`**: `transition: transform 1s cubic-bezier(.16,1,.3,1)` extracted from `brand-helloasso-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.16,1,.3,1)`)**: Governs interactive state transitions across `<header.is-ready>` and `<section.chapter>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `brand-helloasso-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
