---
title: "UI Prompt Blueprint: www-lesgmstudios-com"
date: 2026-11-23
captured_at: 2026-11-23
target: "www-lesgmstudios-com"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#070707` canvas, `#ffffff` ink, `#f7a100` accent)"
---

# UI Design System & Master Generation Blueprint: www-lesgmstudios-com

> **GM Studios — Du contenu qui dépasse les chiffres** (https://www.lesgmstudios.com/) — Agence de contenu & studio d'enregistrement à Montréal. 1 milliard de vues générées pour nos clients.

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **GM Studios — Du contenu qui dépasse les chiffres** (`https://www.lesgmstudios.com/`). Agence de contenu & studio d'enregistrement à Montréal. 1 milliard de vues générées pour nos clients.
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#070707` canvas, `#ffffff` ink, `#f7a100` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#070707` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#ffffff` primary typography and `#f7a100` accents.
  - **Grounded Typographic Hierarchy**: Pairs `clashDisplay` for display copy (`DU CONTENU QUI DÉPASSE LES CHIFFRES`) with `clashDisplay` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1344px` container bounds (`gap: 24px`, padding `6rem`) with `cubic-bezier(.4,0,1,1)` easing and Swiper Touch Carousel Engine.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, clamped at 2400px live multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `1344px` (measured widest bounded `<section>` landmark width on `1440px` desktop).
- **Canvas Lateral Padding & Spacing**: `6rem` lateral canvas padding with `24px` grid gap.
- **Border Radius Scale**: `8px`, `50%`, `.25rem`, `var(--radius-2xl)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1344px`, `gap: 24px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `6rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#070707` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#0c0c0c` | `var(--color-bg-page)` in `:root` |
| **Interactive Accent / Highlight** | `#f7a100` | `var(--color-accent-orange)` in `:root` |
| **Secondary / Muted Copy** | `#728898` | `QVrC .styles_progressBar__total... { color: #728898 }` |
| **Structural Hairline Border** | `#ffffff` | `var(--color-border)` in `:root` |
| **Variable Token (`--color-black`)** | `#000000` | `var(--color-black)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--container-max` | `1440px` | Layout / Spatial Grid Token |
| `--font-sans` | `var(--font-geist), system-ui, sans-serif` | Typography / Scale Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--container-4xl` | `56rem` | Layout / Spatial Grid Token |
| `--text-sm` | `.875rem` | Typography Ink Token |
| `--text-sm--line-height` | `calc(1.25 / .875)` | Typography Ink Token |
| `--font-weight-normal` | `400` | Typography / Scale Token |
| `--font-weight-medium` | `500` | Typography / Scale Token |
| `--font-weight-semibold` | `600` | Typography / Scale Token |
| `--font-weight-bold` | `700` | Typography / Scale Token |
| `--leading-tight` | `1.25` | Typography / Scale Token |
| `--leading-snug` | `1.375` | Typography / Scale Token |
| `--radius-xs` | `4px` | Elevation / Border Token |
| `--radius-sm` | `8px` | Elevation / Border Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `clashDisplay`.
- **Primary Body Stack**: `clashDisplay`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 16px`, `line-height: 15.2px`, `font-weight: 400`, `letter-spacing: -0.16px`); CSS variables `--font-display: var(--font-clash), system-ui, sans-serif`.
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 71px`, `line-height: 85.2px`, `font-weight: 600`); rule `h2` (`font-size: var(--h2-size,clamp(38px, 5.1...`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-sm: .875rem`, `--text-sm--line-height: calc(1.25 / .875)`, `--default-mono-font-family: var(--font-mono)`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.swiper-wrapper`**: `transition: var(--swiper-wrapper-transition-timing-function,initial)` extracted from `www-lesgmstudios-com` stylesheet.
- **Selector `.swiper-free-mode>.swiper-wrapper`**: `transition: ease-out` extracted from `www-lesgmstudios-com` stylesheet.
- **Selector `layer theme`**: `transition: .15s` extracted from `www-lesgmstudios-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,1,1)`)**: Governs interactive state transitions across `<header.inset-x-0>` and `<section.overflow-x-clip>`.
- **Runtime Interaction Engine**: Integrates Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — GM Studios — Du contenu qui dépasse les ch │
│ ====================================================================== │
│ [ <header.inset-x-0> (1440x97px)      | Accueil · Agence · Évènement ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.inset-x-0> (w=1440px)                         | │
│ | H1: DU CONTENU QUI DÉPASSE LES CHIFFRES                            | │
│ | Substrate: #070707 | Ink: #ffffff | Accent: #f7a100                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.overflow-x-clip>) max-w: 1344px            | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Du contenu qui dé p asse les |  | Clients & Partenaires        | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.noise-layer>) — Nos services               | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.overflow-x-c) | https://www.lesgmstudios.com/        │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 24px)       │
│ ====================================================================== │
│ [ HEADER BAR (<header.inset-x-0>      ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.inset-x-0>) — 390px Vertical Lead             | │
│ | H1: DU CONTENU QUI DÉPASSE LES CHIFFRES                            | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.overflow-x-cl) — 1-Col Stack              | │
│ | [ Item 1: Du contenu qui dé p asse les chiffres                  ] | │
│ | [ Item 2: Clients & Partenaires                                  ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.noise-layer>) — 1-Col (Nos services)        | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.overflow-x-c) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.inset-x-0> — `www-lesgmstudios-com`)**:
   - Landmark `<header class="inset-x-0 top-0">` (`1440x97px`) hosting `GM Studios — Du contenu qui dépasse ` navigation (`Accueil · Agence · Évènements · Cas clients · Équipe`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-voomly-styles`), and stylesheet rule `root { --swiper-theme-color:007aff }`.
2. **Hero Stage & Focal Lead (<section.inset-x-0> — `DU CONTENU QUI DÉPASSE LES CHIFFRE`)**:
   - Landmark `<section class="inset-x-0 top-0">` presenting display lead `DU CONTENU QUI DÉPASSE LES CHIFFRES` and copy excerpt *"Nous transformons vos idées en contenus percutants qui captivent "* over `#070707` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.overflow-x-clip> — `Du contenu qui dé p asse les chiff`)**:
   - Landmark `<section class="overflow-x-clip py-10">` rendering section `Du contenu qui dé p asse les chiffres` with copy *"Selon plus de 450 clients satisfaits"*, asset references (`ClashDisplay_Bold-s.p.2nvxwaktzfx...`, `ClashDisplay_Medium-s.p.0olkjtjdv...`, `ClashDisplay_Regular-s.p.2qbs-i2c...`, `ClashDisplay_Semibold-s.p.082yiqt...`), and grid rule `host { z-index:1;margin-left:auto;margin-right:auto;display:block;position:rela... }`.
4. **Interactive Detail & Feature Matrix (<section.noise-layer> — `Clients & Partenaires`)**:
   - Landmark `<section class="noise-layer py-32">` framing `Clients & Partenaires` and `Nos services` (*"Studio de production à Montréal"*) with `#0c0c0c` surface cards, `#f7a100` accents, and `.swiper { z-index:1;margin-left:auto;margin-right:auto;padding:0;list-style:none;d... }`.
5. **Colophon & Global Directory Footer (<footer.overflow-x-clip> — `https://www.lesgmstudios.com/`)**:
   - Landmark `<footer class="overflow-x-clip bg-transparent">` anchoring `GM Studios — Du contenu qui dépa` footer links (`Accueil · Agence · Évènements · Cas clients · Équipe`), copy *"Du contenu qui dé p asse"*, and `#ffffff` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-lesgmstudios-com (GM Studios — Du contenu qui dépasse les chiffres)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-lesgmstudios-com` (**GM Studios — Du contenu qui dépasse les chiffres** — `https://www.lesgmstudios.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#070707` canvas, `#ffffff` ink, `#f7a100` accent).
- **Identity & Domain Context**: Agence de contenu & studio d'enregistrement à Montréal. 1 milliard de vues générées pour nos clients.
- **Primary Substrate**: `#070707` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#ffffff`, **Accent / Highlight**: `#f7a100`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#070707` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#ffffff` primary typography and `#f7a100` accents.
  - **Grounded Typographic Hierarchy**: Pairs `clashDisplay` for display copy (`DU CONTENU QUI DÉPASSE LES CHIFFRES`) with `clashDisplay` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1344px` container bounds (`gap: 24px`, padding `6rem`) with `cubic-bezier(.4,0,1,1)` easing and Swiper Touch Carousel Engine.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-lesgmstudios-com` in your global stylesheet:

:root {
  /* GM Studios — Du contenu qui dépasse les chiffres (www-lesgmstudios-com) — Live-Grounded CSS Variables */
  --container-max: 1440px; /* Layout / Spatial Grid Token (www-lesgmstudios-com) */
  --font-sans: var(--font-geist), system-ui, sans-serif; /* Typography / Scale Token (www-lesgmstudios-com) */
  --color-black: #000; /* Canvas / Surface Token (www-lesgmstudios-com) */
  --color-white: #fff; /* Canvas / Surface Token (www-lesgmstudios-com) */
  --spacing: .25rem; /* Layout / Spatial Grid Token (www-lesgmstudios-com) */
  --container-4xl: 56rem; /* Layout / Spatial Grid Token (www-lesgmstudios-com) */
  --text-sm: .875rem; /* Typography Ink Token (www-lesgmstudios-com) */
  --text-sm--line-height: calc(1.25 / .875); /* Typography Ink Token (www-lesgmstudios-com) */
  --font-weight-normal: 400; /* Typography / Scale Token (www-lesgmstudios-com) */
  --font-weight-medium: 500; /* Typography / Scale Token (www-lesgmstudios-com) */
  --font-weight-semibold: 600; /* Typography / Scale Token (www-lesgmstudios-com) */
  --font-weight-bold: 700; /* Typography / Scale Token (www-lesgmstudios-com) */
  --leading-tight: 1.25; /* Typography / Scale Token (www-lesgmstudios-com) */
  --leading-snug: 1.375; /* Typography / Scale Token (www-lesgmstudios-com) */
  --radius-xs: 4px; /* Elevation / Border Token (www-lesgmstudios-com) */
  --radius-sm: 8px; /* Elevation / Border Token (www-lesgmstudios-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#070707` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#ffffff` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#0c0c0c` — grounded in `var(--color-bg-page)` in `:root`
- **Interactive Accent / Highlight**: `#f7a100` — grounded in `var(--color-accent-orange)` in `:root`
- **Secondary / Muted Copy**: `#728898` — grounded in `QVrC .styles_progressBar__total... { color: #728898 }`
- **Structural Hairline Border**: `#ffffff` — grounded in `var(--color-border)` in `:root`
- **Variable Token (`--color-black`)**: `#000000` — grounded in `var(--color-black)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (clamped at 2400px live multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1344px` (measured widest bounded `<section>` landmark width on `1440px` desktop)
- **Padding & Gutters**: `6rem` lateral canvas padding with `24px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1344px`, `gap: 24px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `6rem` horizontal padding
- **Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)`
- **Corner Radii**: `8px`, `50%`, `.25rem`, `var(--radius-2xl)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `clashDisplay`
- **Body Font Stack**: `clashDisplay`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: live computed `h1` (`font-size: 16px`, `line-height: 15.2px`, `font-weight: 400`, `letter-spacing: -0.16px`); CSS variables `--font-display: var(--font-clash), system-ui, sans-serif`
- **H2 Section Rule**: live computed `h2` (`font-size: 71px`, `line-height: 85.2px`, `font-weight: 600`); rule `h2` (`font-size: var(--h2-size,clamp(38px, 5.1...`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-sm: .875rem`, `--text-sm--line-height: calc(1.25 / .875)`, `--default-mono-font-family: var(--font-mono)`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-lesgmstudios-com` (`GM Studios — Du contenu qui dépasse les chiffres`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.inset-x-0> — `www-lesgmstudios-com`)**:
   - DOM & Selectors: Landmark `<header class="inset-x-0 top-0">` (`1440x97px`) hosting `GM Studios — Du contenu qui dépasse ` navigation (`Accueil · Agence · Évènements · Cas clients · Équipe`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-voomly-styles`), and stylesheet rule `root { --swiper-theme-color:007aff }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.inset-x-0> — `www-lesgmstudios-com`)` (`www-lesgmstudios-com`) adapts across `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)` with `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)` transitions and links `Accueil · Agence · Évènements · Cas clients · Équipe`.
2. **Hero Stage & Focal Lead (<section.inset-x-0> — `DU CONTENU QUI DÉPASSE LES CHIFFRE`)**:
   - DOM & Selectors: Landmark `<section class="inset-x-0 top-0">` presenting display lead `DU CONTENU QUI DÉPASSE LES CHIFFRES` and copy excerpt *"Nous transformons vos idées en contenus percutants qui captivent "* over `#070707` canvas and `#ffffff` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#070707` background with `#ffffff` headline `DU CONTENU QUI DÉPASSE LES CHIFFRES`.
3. **Primary Showcase & Content Grid (<section.overflow-x-clip> — `Du contenu qui dé p asse les chiff`)**:
   - DOM & Selectors: Landmark `<section class="overflow-x-clip py-10">` rendering section `Du contenu qui dé p asse les chiffres` with copy *"Selon plus de 450 clients satisfaits"*, asset references (`ClashDisplay_Bold-s.p.2nvxwaktzfx...`, `ClashDisplay_Medium-s.p.0olkjtjdv...`, `ClashDisplay_Regular-s.p.2qbs-i2c...`, `ClashDisplay_Semibold-s.p.082yiqt...`), and grid rule `host { z-index:1;margin-left:auto;margin-right:auto;display:block;position:rela... }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.overflow-x-clip> — `Du contenu qui dé p asse les chiff`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1344px`, `gap: 24px`) on desktop and Single-column vertical stack at `390px` viewport width with `6rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.noise-layer> — `Clients & Partenaires`)**:
   - DOM & Selectors: Landmark `<section class="noise-layer py-32">` framing `Clients & Partenaires` and `Nos services` (*"Studio de production à Montréal"*) with `#0c0c0c` surface cards, `#f7a100` accents, and `.swiper { z-index:1;margin-left:auto;margin-right:auto;padding:0;list-style:none;d... }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.noise-layer> — `Clients & Partenaires`)` uses `8px`, `50%`, `.25rem`, `var(--radius-2xl)` radii, `#f7a100` highlights, and assets (ClashDisplay_Bold-s.p.2nvxwaktzfx..., ClashDisplay_Medium-s.p.0olkjtjdv..., ClashDisplay_Regular-s.p.2qbs-i2c...).
5. **Colophon & Global Directory Footer (<footer.overflow-x-clip> — `https://www.lesgmstudios.com/`)**:
   - DOM & Selectors: Landmark `<footer class="overflow-x-clip bg-transparent">` anchoring `GM Studios — Du contenu qui dépa` footer links (`Accueil · Agence · Évènements · Cas clients · Équipe`), copy *"Du contenu qui dé p asse"*, and `#ffffff` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.overflow-x-clip> — `https://www.lesgmstudios.com/`)` aligns to `1344px` (measured widest bounded `<section>` landmark width on `1440px` desktop) with `6rem` lateral canvas padding with `24px` grid gap and attributes (data-precedence="next", data-precedence="next", data-precedence="next").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Nous transformons vos idées en contenus percutants qui captivent votre audience et..."*
- Copy Excerpt 2: *"Selon plus de 450 clients satisfaits"*
- Copy Excerpt 3: *"Studio de production à Montréal"*
- Copy Excerpt 4: *"Du contenu qui dé p asse"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`
- **Extracted Stylesheet Rules (`www-lesgmstudios-com`)**:
- `root { --swiper-theme-color:007aff }`
- `host { z-index:1;margin-left:auto;margin-right:auto;display:block;position:rela... }`
- `.swiper { z-index:1;margin-left:auto;margin-right:auto;padding:0;list-style:none;d... }`
- `.swiper-vertical>.swiper-wrapper { flex-direction:column }`
- `.swiper-wrapper { transform:translate(0,0) }`
- **Per-Selector Transition Rules**:
- **Selector `.swiper-wrapper`**: `transition: var(--swiper-wrapper-transition-timing-function,initial)` extracted from `www-lesgmstudios-com` stylesheet.
- **Selector `.swiper-free-mode>.swiper-wrapper`**: `transition: ease-out` extracted from `www-lesgmstudios-com` stylesheet.
- **Selector `layer theme`**: `transition: .15s` extracted from `www-lesgmstudios-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,1,1)`)**: Governs interactive state transitions across `<header.inset-x-0>` and `<section.overflow-x-clip>`.
- **Runtime Interaction Engine**: Integrates Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-lesgmstudios-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
