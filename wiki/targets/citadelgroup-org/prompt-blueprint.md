---
title: "UI Prompt Blueprint: citadelgroup-org"
date: 2026-11-15
target: "citadelgroup-org"
status: analyzed
capture: dom
capture_desktop: dom
capture_mobile: dom
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#f7953e` / `#e3e3e4`)"
---

# UI Design System & Master Generation Blueprint: citadelgroup-org

> **Citadel National Construction Group · Nationwide Construction** (https://citadelgroup.org/) — Citadel connects leading regional construction firms into one nationwide network, combining local expertise with national resources to de...

![Desktop Viewport Capture](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Citadel National Construction Group · Nationwide Construction** (`https://citadelgroup.org/`). Citadel connects leading regional construction firms into one nationwide network, combining local expertise with national resources to de...
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#f7953e` / `#e3e3e4`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#f7953e` (`var(--citadel-orange)` in `:root`) paired with `#000000` primary typography and `#e3e3e4` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Montserrat` for display copy (`National Reach. Local Expertise.`) with `Bebas Neue` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `5%` container bounds (`gap: .25rem`, padding `1rem`) with `cubic-bezier(.22,1,.36,1)` easing and Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×10151px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `5%` extracted from `citadelgroup-org` stylesheet.
- **Canvas Lateral Padding & Spacing**: `1rem` lateral canvas padding with `.25rem` grid gap.
- **Border Radius Scale**: `.25rem`, `.5rem`, `1rem`, `1.5rem`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 5%`, `gap: .25rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `1rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:1140px)`, `@media (min-width:768px)`, `@media (min-width:1280px)`, `@media (min-width:767px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#f7953e` | `var(--citadel-orange)` in `:root` |
| **Primary Typography Ink** | `#f87000` | `var(--citadel-dark-orange)` in `:root` |
| **Elevated Surface / Card Substrate** | `#818486` | `var(--citadel-medium-grey)` in `:root` |
| **Interactive Accent / Highlight** | `#e3e3e4` | `var(--citadel-light-grey)` in `:root` |
| **Secondary / Muted Copy** | `#000000` | `var(--citadel-black)` in `:root` |
| **Structural Hairline Border** | `#e17e00` | `var(--color-brand-orange-hover)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--citadel-orange` | `#f7953e` | Color / Atmospheric Token |
| `--citadel-dark-orange` | `#f87000` | Canvas / Surface Token |
| `--citadel-medium-grey` | `#818486` | Color / Atmospheric Token |
| `--citadel-light-grey` | `#e3e3e4` | Canvas / Surface Token |
| `--citadel-black` | `#000000` | Canvas / Surface Token |
| `--color-brand-orange` | `var(--citadel-orange)` | Brand / Palette Token |
| `--color-brand-dark-orange` | `var(--citadel-dark-orange)` | Canvas / Surface Token |
| `--color-brand-orange-hover` | `#e17e00` | Brand / Palette Token |
| `--color-brand-black` | `var(--citadel-black)` | Canvas / Surface Token |
| `--color-brand-medium-grey` | `var(--citadel-medium-grey)` | Brand / Palette Token |
| `--color-brand-light-grey` | `var(--citadel-light-grey)` | Canvas / Surface Token |
| `--color-bg-dark` | `var(--citadel-black)` | Canvas / Surface Token |
| `--color-bg-light` | `var(--citadel-light-grey)` | Canvas / Surface Token |
| `--color-text-primary` | `var(--citadel-black)` | Typography Ink Token |
| `--color-accent` | `var(--citadel-orange)` | Brand / Palette Token |
| `--font-citadel-heading` | `"Montserrat", system-ui, sans-serif` | Typography Ink Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Montserrat`.
- **Primary Body Stack**: `Bebas Neue`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `.6rem`, `.7rem`, `.8rem`, `1.2rem`, `1.5rem`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(2.9rem,2.9vw,3.9rem)!im...`, `line-height: 1.02!important`).
- **Body Copy**: CSS variables `--font-citadel-body: "Montserrat", system-ui, sans-serif`; rule `p` (`font-size: .88rem`, `line-height: 1.35`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `.6rem`, `.7rem`, `.8rem`, `1.2rem`, `1.5rem`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.22,1,.36,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.citadel-site-header`**: `transition: color .22s ease` extracted from `citadelgroup-org` stylesheet.
- **Selector `.logo-cover`**: `transition: background-color .36s ease,opacity .36s ease` extracted from `citadelgroup-org` stylesheet.
- **Selector `.citadel-site-nav-link`**: `transition: color .18s ease` extracted from `citadelgroup-org` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.22,1,.36,1)`)**: Governs interactive state transitions across `<header.citadel-site-header>` and `<section.citadel-about>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Citadel National Construction Group · Nati │
│ ====================================================================== │
│ [ <header.citadel-site-hea | About · Case Studies · Map · Principal ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.citadel-hero>                               |   │
│ | H1: National Reach. Local Expertise.                             |   │
│ | Substrate: #f7953e    | Ink: #000000    | Accent: #e3e3e4        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.citadel-about>   ) max-w: 5%             |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Serving Clients With Nationa |  | Seven firms. One connected c | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: .25rem) | │
│ | [<header.citadel-si] -> [<section.citadel-h] -> [<section.citadel-a] │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.site-footer-me) | https://citadelgroup.org/          │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.citadel-site-header> — `citadelgroup-org`)**:
   - Landmark `<header class="citadel-site-header is-over-hero">` hosting `Citadel National Construction Group ` navigation (`About · Case Studies · Map · Principals`), DOM attributes (`data-wp-strategy="async"`, `data-loaded="true"`, `data-module="scrollspy-nav"`, `data-logo-cover-surface="hidden"`), and stylesheet rule `font-primary { font-family:var(--font-primary) }`.
2. **Hero Stage & Focal Lead (<section.citadel-hero> — `National Reach. Local Expertise.`)**:
   - Landmark `<section class="citadel-hero">` presenting display lead `National Reach. Local Expertise.` and copy excerpt *"Citadel Construction Group"* over `#f7953e` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.citadel-about> — `Serving Clients With National Need`)**:
   - Landmark `<section class="citadel-about">` rendering section `Serving Clients With National Needs` with copy *"Citadel National Construction Group leverages seven best-in-class"*, asset references (`www.googletagmanager.com`, `embed`, `theme-core.min.css`, `framework-md.min.css`), and grid rule `font-secondary { font-family:var(--font-secondary) }`.
4. **Interactive Detail & Feature Matrix (<section.citadel-partners> — `Seven firms. One connected constru`)**:
   - Landmark `<section class="citadel-partners flex">` framing `Seven firms. One connected construction network.` and `Case Studies` (*"L o c a l s t r e n g t h . N a t i o n a l s c a l e ."*) with `#818486` surface cards, `#e3e3e4` accents, and `font-open-sans { font-family:var(--font-base) }`.
5. **Colophon & Global Directory Footer (<footer.site-footer-meta> — `https://citadelgroup.org/`)**:
   - Landmark `<footer class="site-footer-meta">` anchoring `Citadel National Construction Gr` footer links (`About · Case Studies · Map · Principals`), copy *"L o c a l s t r e n g t h ."*, and `#e17e00` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: citadelgroup-org (Citadel National Construction Group · Nationwide Construction)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `citadelgroup-org` (**Citadel National Construction Group · Nationwide Construction** — `https://citadelgroup.org/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f7953e` / `#e3e3e4`).
- **Identity & Domain Context**: Citadel connects leading regional construction firms into one nationwide network, combining local expertise with national resources to de...
- **Primary Substrate**: `#f7953e` (`var(--citadel-orange)` in `:root`), **Primary Ink**: `#000000`, **Accent / Highlight**: `#e3e3e4`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#f7953e` (`var(--citadel-orange)` in `:root`) paired with `#000000` primary typography and `#e3e3e4` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Montserrat` for display copy (`National Reach. Local Expertise.`) with `Bebas Neue` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `5%` container bounds (`gap: .25rem`, padding `1rem`) with `cubic-bezier(.22,1,.36,1)` easing and Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `citadelgroup-org` in your global stylesheet:

:root {
  /* Citadel National Construction Group · Nationwide Construction (citadelgroup-org) — Ground-Truth Extracted CSS Variables */
  --citadel-orange: #f7953e; /* Color / Atmospheric Token (citadelgroup-org) */
  --citadel-dark-orange: #f87000; /* Canvas / Surface Token (citadelgroup-org) */
  --citadel-medium-grey: #818486; /* Color / Atmospheric Token (citadelgroup-org) */
  --citadel-light-grey: #e3e3e4; /* Canvas / Surface Token (citadelgroup-org) */
  --citadel-black: #000000; /* Canvas / Surface Token (citadelgroup-org) */
  --color-brand-orange: var(--citadel-orange); /* Brand / Palette Token (citadelgroup-org) */
  --color-brand-dark-orange: var(--citadel-dark-orange); /* Canvas / Surface Token (citadelgroup-org) */
  --color-brand-orange-hover: #e17e00; /* Brand / Palette Token (citadelgroup-org) */
  --color-brand-black: var(--citadel-black); /* Canvas / Surface Token (citadelgroup-org) */
  --color-brand-medium-grey: var(--citadel-medium-grey); /* Brand / Palette Token (citadelgroup-org) */
  --color-brand-light-grey: var(--citadel-light-grey); /* Canvas / Surface Token (citadelgroup-org) */
  --color-bg-dark: var(--citadel-black); /* Canvas / Surface Token (citadelgroup-org) */
  --color-bg-light: var(--citadel-light-grey); /* Canvas / Surface Token (citadelgroup-org) */
  --color-text-primary: var(--citadel-black); /* Typography Ink Token (citadelgroup-org) */
  --color-accent: var(--citadel-orange); /* Brand / Palette Token (citadelgroup-org) */
  --font-citadel-heading: "Montserrat", system-ui, sans-serif; /* Typography Ink Token (citadelgroup-org) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#f7953e` — grounded in `var(--citadel-orange)` in `:root`
- **Primary Typography Ink**: `#f87000` — grounded in `var(--citadel-dark-orange)` in `:root`
- **Elevated Surface / Card Substrate**: `#818486` — grounded in `var(--citadel-medium-grey)` in `:root`
- **Interactive Accent / Highlight**: `#e3e3e4` — grounded in `var(--citadel-light-grey)` in `:root`
- **Secondary / Muted Copy**: `#000000` — grounded in `var(--citadel-black)` in `:root`
- **Structural Hairline Border**: `#e17e00` — grounded in `var(--color-brand-orange-hover)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×10151px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `5%` extracted from `citadelgroup-org` stylesheet
- **Padding & Gutters**: `1rem` lateral canvas padding with `.25rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 5%`, `gap: .25rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `1rem` horizontal padding
- **Media Queries**: `@media (min-width:1140px)`, `@media (min-width:768px)`, `@media (min-width:1280px)`, `@media (min-width:767px)`
- **Corner Radii**: `.25rem`, `.5rem`, `1rem`, `1.5rem`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Montserrat`
- **Body Font Stack**: `Bebas Neue`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `.6rem`, `.7rem`, `.8rem`, `1.2rem`, `1.5rem`)
- **H2 Section Rule**: rule `h2` (`font-size: clamp(2.9rem,2.9vw,3.9rem)!im...`, `line-height: 1.02!important`)
- **Body Copy Rule**: CSS variables `--font-citadel-body: "Montserrat", system-ui, sans-serif`; rule `p` (`font-size: .88rem`, `line-height: 1.35`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `.6rem`, `.7rem`, `.8rem`, `1.2rem`, `1.5rem`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `citadelgroup-org` (`Citadel National Construction Group · Nationwide Construction`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.citadel-site-header> — `citadelgroup-org`)**:
   - DOM & Selectors: Landmark `<header class="citadel-site-header is-over-hero">` hosting `Citadel National Construction Group ` navigation (`About · Case Studies · Map · Principals`), DOM attributes (`data-wp-strategy="async"`, `data-loaded="true"`, `data-module="scrollspy-nav"`, `data-logo-cover-surface="hidden"`), and stylesheet rule `font-primary { font-family:var(--font-primary) }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.citadel-site-header> — `citadelgroup-org`)` (`citadelgroup-org`) adapts across `@media (min-width:1140px)`, `@media (min-width:768px)`, `@media (min-width:1280px)`, `@media (min-width:767px)` with `cubic-bezier(.22,1,.36,1)` transitions and links `About · Case Studies · Map · Principals`.
2. **Hero Stage & Focal Lead (<section.citadel-hero> — `National Reach. Local Expertise.`)**:
   - DOM & Selectors: Landmark `<section class="citadel-hero">` presenting display lead `National Reach. Local Expertise.` and copy excerpt *"Citadel Construction Group"* over `#f7953e` canvas and `#000000` ink.
   - Responsive Contract: Hero stage (`1440×10151px` desktop / `390×2400px` mobile) sets `#f7953e` background with `#000000` headline `National Reach. Local Expertise.`.
3. **Primary Showcase & Content Grid (<section.citadel-about> — `Serving Clients With National Need`)**:
   - DOM & Selectors: Landmark `<section class="citadel-about">` rendering section `Serving Clients With National Needs` with copy *"Citadel National Construction Group leverages seven best-in-class"*, asset references (`www.googletagmanager.com`, `embed`, `theme-core.min.css`, `framework-md.min.css`), and grid rule `font-secondary { font-family:var(--font-secondary) }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.citadel-about> — `Serving Clients With National Need`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 5%`, `gap: .25rem`) on desktop and Single-column vertical stack at `390px` viewport width with `1rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.citadel-partners> — `Seven firms. One connected constru`)**:
   - DOM & Selectors: Landmark `<section class="citadel-partners flex">` framing `Seven firms. One connected construction network.` and `Case Studies` (*"L o c a l s t r e n g t h . N a t i o n a l s c a l e ."*) with `#818486` surface cards, `#e3e3e4` accents, and `font-open-sans { font-family:var(--font-base) }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.citadel-partners> — `Seven firms. One connected constru`)` uses `.25rem`, `.5rem`, `1rem`, `1.5rem` radii, `#e3e3e4` highlights, and assets (www.googletagmanager.com, embed, theme-core.min.css).
5. **Colophon & Global Directory Footer (<footer.site-footer-meta> — `https://citadelgroup.org/`)**:
   - DOM & Selectors: Landmark `<footer class="site-footer-meta">` anchoring `Citadel National Construction Gr` footer links (`About · Case Studies · Map · Principals`), copy *"L o c a l s t r e n g t h ."*, and `#e17e00` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.site-footer-meta> — `https://citadelgroup.org/`)` aligns to `5%` extracted from `citadelgroup-org` stylesheet with `1rem` lateral canvas padding with `.25rem` grid gap and attributes (data-wp-strategy="async", data-loaded="true", data-module="scrollspy-nav").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Citadel Construction Group"*
- Copy Excerpt 2: *"Citadel National Construction Group leverages seven best-in-class contractors to d..."*
- Copy Excerpt 3: *"L o c a l s t r e n g t h . N a t i o n a l s c a l e ."*
- Copy Excerpt 4: *"L o c a l s t r e n g t h ."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.22,1,.36,1)`
- **Extracted Stylesheet Rules (`citadelgroup-org`)**:
- `font-primary { font-family:var(--font-primary) }`
- `font-secondary { font-family:var(--font-secondary) }`
- `font-open-sans { font-family:var(--font-base) }`
- `font-trump { font-family:var(--font-trump) }`
- `text-dark { color:var(--color-dark) }`
- **Per-Selector Transition Rules**:
- **Selector `.citadel-site-header`**: `transition: color .22s ease` extracted from `citadelgroup-org` stylesheet.
- **Selector `.logo-cover`**: `transition: background-color .36s ease,opacity .36s ease` extracted from `citadelgroup-org` stylesheet.
- **Selector `.citadel-site-nav-link`**: `transition: color .18s ease` extracted from `citadelgroup-org` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.22,1,.36,1)`)**: Governs interactive state transitions across `<header.citadel-site-header>` and `<section.citadel-about>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `citadelgroup-org`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
