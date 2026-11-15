---
title: "UI Prompt Blueprint: hopecancerresources-org"
date: 2026-11-15
target: "[[overview|hopecancerresources-org]]"
status: analyzed
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#0e1829` canvas, `#edf1f4` ink, `#476577` accent)"
---

# UI Design System & Master Generation Blueprint: hopecancerresources-org

> **Hope Cancer Resources - Support. Educate. Prevent.** (https://hopecancerresources.org/) — Providing free cancer support services through counseling, transportation, financial assistance, personal training, tobacco treatment, &...

![Desktop Viewport Capture (1440x5575)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Hope Cancer Resources - Support. Educate. Prevent.** (`https://hopecancerresources.org/`). Providing free cancer support services through counseling, transportation, financial assistance, personal training, tobacco treatment, &...
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#0e1829` canvas, `#edf1f4` ink, `#476577` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#0e1829` (`var(--color-brand-black)` in `:root`) paired with `#edf1f4` primary typography and `#476577` accents.
  - **Extracted Typographic Hierarchy**: Pairs `BrandonText` for display copy (`Support. Educate. Prevent.`) with `SourceSans` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1400px` container bounds (`gap: 20px`, padding `20px`) with `cubic-bezier(0.25,0.1,0.25,1)` easing and Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×5575px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `1400px` extracted from `hopecancerresources-org` stylesheet.
- **Canvas Lateral Padding & Spacing**: `20px` lateral canvas padding with `20px` grid gap.
- **Border Radius Scale**: `6px`, `100px`, `12px`, `10px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1400px`, `gap: 20px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `20px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width: 800px)`, `@media (min-width: 768px)`, `@media (min-width: 960px)`, `@media (min-width: 1400px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#0e1829` | `var(--color-brand-black)` in `:root` |
| **Primary Typography Ink** | `#1b7aaf` | `var(--color-brand-blue)` in `:root` |
| **Elevated Surface / Card Substrate** | `#1fa0e5` | `var(--color-brand-lightblue)` in `:root` |
| **Interactive Accent / Highlight** | `#476577` | `var(--color-brand-darkblue)` in `:root` |
| **Secondary / Muted Copy** | `#90a3bf` | `var(--color-brand-gray-500)` in `:root` |
| **Structural Hairline Border** | `#edf1f4` | `var(--color-lightest-gray)` in `:root` |
| **Variable Token (`--color-notice-warning`)** | `#dc4b4b` | `var(--color-notice-warning)` in `:root` |
| **Variable Token (`--color-notice-success`)** | `#2DB292` | `var(--color-notice-success)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-primary` | `"BrandonText", Arial, Helvetica, sans-serif` | Brand / Palette Token |
| `--font-heading` | `"BrandonText", Arial, Helvetica, sans-serif` | Typography Ink Token |
| `--font-base` | `"SourceSans", Arial, Helvetica, sans-serif` | Typography / Scale Token |
| `--font-serif` | `"EightiesComebackIt", "Times New Roman", "Garamond", serif` | Typography / Scale Token |
| `--color-brand-black` | `#0e1829` | Canvas / Surface Token |
| `--color-brand-blue` | `#1b7aaf` | Brand / Palette Token |
| `--color-brand-lightblue` | `#1fa0e5` | Canvas / Surface Token |
| `--color-brand-darkblue` | `#476577` | Canvas / Surface Token |
| `--color-brand-gray-500` | `#90a3bf` | Brand / Palette Token |
| `--color-light-gray` | `#476577` | Canvas / Surface Token |
| `--color-lightest-gray` | `#edf1f4` | Canvas / Surface Token |
| `--color-notice-warning` | `#dc4b4b` | Brand / Palette Token |
| `--color-notice-success` | `#2DB292` | Brand / Palette Token |
| `--color-primary` | `var(--color-brand-black)` | Brand / Palette Token |
| `--color-secondary` | `var(--color-brand-black)` | Brand / Palette Token |
| `--color-brand-text-base` | `var(--color-brand-black)` | Typography Ink Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `BrandonText`.
- **Primary Body Stack**: `SourceSans`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 2rem`, `line-height: 1`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(1.6rem,5vw,3rem)`, `font-weight: 900`).
- **Body Copy**: CSS variables `--color-brand-text-base: var(--color-brand-black)`; rule `p` (`font-size: 2rem`, `line-height: 1.5`, `font-weight: 400`).
- **Metadata & Navigation Labels**: rule `.label` (`font-size: 1rem`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.25,0.1,0.25,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `body *`**: `transition: all .2s ease-in` extracted from `hopecancerresources-org` stylesheet.
- **Selector `.reveal-overlay`**: `transition: mask-image .1s ease-out,-webkit-mask-image .1s ease-out` extracted from `hopecancerresources-org` stylesheet.
- **Selector `.skip-link`**: `transition: top .3s ease` extracted from `hopecancerresources-org` stylesheet.
- **Standard CSS Easing (`cubic-bezier(0.25,0.1,0.25,1)`)**: Default timing curve (no custom `cubic-bezier()` declared in static CSS).
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Hope Cancer Resources - Support. Educate.  │
│ ====================================================================== │
│ [ <header.site-header>     | Shop for Hope · About Hope · Our Story ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <article.post-type-page>                             |   │
│ | H1: Support. Educate. Prevent.                                   |   │
│ | Substrate: #0e1829    | Ink: #edf1f4    | Accent: #476577        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.page_heading>    ) max-w: 1400px         |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Driving real Change in North |  | At Hope Cancer Resources, we | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 20px  ) | │
│ | [<header.site-heade] -> [<article.post-type] -> [<section.page_head] │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.site-footer>  ) | https://hopecancerresources.org/   │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.site-header> — `hopecancerresources-org`)**:
   - Landmark `<header class="site-header template-home">` hosting `Hope Cancer Resources - Support. Edu` navigation (`Shop for Hope · About Hope · Our Story · Our Foundation · Staff`), DOM attributes (`data-template="base.twig"`), and stylesheet rule `content { background:fff;background-size:100% }`.
2. **Hero Stage & Focal Lead (<article.post-type-page> — `Support. Educate. Prevent.`)**:
   - Landmark `<article class="post-type-page">` presenting display lead `Support. Educate. Prevent.` and copy excerpt *"Skip to main content"* over `#0e1829` canvas and `#edf1f4` ink.
3. **Primary Showcase & Content Grid (<section.page_heading> — `Driving real Change in Northwest A`)**:
   - Landmark `<section class="page_heading section-block">` rendering section `Driving real Change in Northwest Arkansas (2025 R...` with copy *"About Back to About Hope Unscripted Podcast About Hope Our Story "*, asset references (`gtm.js`, `style.css`, `humans.txt`, `xmlrpc.php`), and grid rule `ge-template-wp-content .default-h... { padding-top:100px }`.
4. **Interactive Detail & Feature Matrix (<section.stats_block_one> — `At Hope Cancer Resources, we walk `)**:
   - Landmark `<section class="stats_block_one section-block">` framing `At Hope Cancer Resources, we walk beside those fa...` and `Ways We Help` (*"Hope Unscripted Podcast"*) with `#1fa0e5` surface cards, `#476577` accents, and `projects-template-default .post-h... { padding-top:80px }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://hopecancerresources.org/`)**:
   - Landmark `<footer class="site-footer">` anchoring `Hope Cancer Resources - Support.` footer links (`Shop for Hope · About Hope · Our Story · Our Foundation · Staff`), copy *"Board of Directors"*, and `#edf1f4` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: hopecancerresources-org (Hope Cancer Resources - Support. Educate. Prevent.)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `hopecancerresources-org` (**Hope Cancer Resources - Support. Educate. Prevent.** — `https://hopecancerresources.org/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#0e1829` canvas, `#edf1f4` ink, `#476577` accent).
- **Identity & Domain Context**: Providing free cancer support services through counseling, transportation, financial assistance, personal training, tobacco treatment, &...
- **Primary Substrate**: `#0e1829` (`var(--color-brand-black)` in `:root`), **Primary Ink**: `#edf1f4`, **Accent / Highlight**: `#476577`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#0e1829` (`var(--color-brand-black)` in `:root`) paired with `#edf1f4` primary typography and `#476577` accents.
  - **Extracted Typographic Hierarchy**: Pairs `BrandonText` for display copy (`Support. Educate. Prevent.`) with `SourceSans` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1400px` container bounds (`gap: 20px`, padding `20px`) with `cubic-bezier(0.25,0.1,0.25,1)` easing and Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `hopecancerresources-org` in your global stylesheet:

:root {
  /* Hope Cancer Resources - Support. Educate. Prevent. (hopecancerresources-org) — Ground-Truth Extracted CSS Variables */
  --font-primary: "BrandonText", Arial, Helvetica, sans-serif; /* Brand / Palette Token (hopecancerresources-org) */
  --font-heading: "BrandonText", Arial, Helvetica, sans-serif; /* Typography Ink Token (hopecancerresources-org) */
  --font-base: "SourceSans", Arial, Helvetica, sans-serif; /* Typography / Scale Token (hopecancerresources-org) */
  --font-serif: "EightiesComebackIt", "Times New Roman", "Garamond", serif; /* Typography / Scale Token (hopecancerresources-org) */
  --color-brand-black: #0e1829; /* Canvas / Surface Token (hopecancerresources-org) */
  --color-brand-blue: #1b7aaf; /* Brand / Palette Token (hopecancerresources-org) */
  --color-brand-lightblue: #1fa0e5; /* Canvas / Surface Token (hopecancerresources-org) */
  --color-brand-darkblue: #476577; /* Canvas / Surface Token (hopecancerresources-org) */
  --color-brand-gray-500: #90a3bf; /* Brand / Palette Token (hopecancerresources-org) */
  --color-light-gray: #476577; /* Canvas / Surface Token (hopecancerresources-org) */
  --color-lightest-gray: #edf1f4; /* Canvas / Surface Token (hopecancerresources-org) */
  --color-notice-warning: #dc4b4b; /* Brand / Palette Token (hopecancerresources-org) */
  --color-notice-success: #2DB292; /* Brand / Palette Token (hopecancerresources-org) */
  --color-primary: var(--color-brand-black); /* Brand / Palette Token (hopecancerresources-org) */
  --color-secondary: var(--color-brand-black); /* Brand / Palette Token (hopecancerresources-org) */
  --color-brand-text-base: var(--color-brand-black); /* Typography Ink Token (hopecancerresources-org) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#0e1829` — grounded in `var(--color-brand-black)` in `:root`
- **Primary Typography Ink**: `#1b7aaf` — grounded in `var(--color-brand-blue)` in `:root`
- **Elevated Surface / Card Substrate**: `#1fa0e5` — grounded in `var(--color-brand-lightblue)` in `:root`
- **Interactive Accent / Highlight**: `#476577` — grounded in `var(--color-brand-darkblue)` in `:root`
- **Secondary / Muted Copy**: `#90a3bf` — grounded in `var(--color-brand-gray-500)` in `:root`
- **Structural Hairline Border**: `#edf1f4` — grounded in `var(--color-lightest-gray)` in `:root`
- **Variable Token (`--color-notice-warning`)**: `#dc4b4b` — grounded in `var(--color-notice-warning)` in `:root`
- **Variable Token (`--color-notice-success`)**: `#2DB292` — grounded in `var(--color-notice-success)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×5575px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1400px` extracted from `hopecancerresources-org` stylesheet
- **Padding & Gutters**: `20px` lateral canvas padding with `20px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1400px`, `gap: 20px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `20px` horizontal padding
- **Media Queries**: `@media (min-width: 800px)`, `@media (min-width: 768px)`, `@media (min-width: 960px)`, `@media (min-width: 1400px)`
- **Corner Radii**: `6px`, `100px`, `12px`, `10px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `BrandonText`
- **Body Font Stack**: `SourceSans`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: rule `h1` (`font-size: 2rem`, `line-height: 1`)
- **H2 Section Rule**: rule `h2` (`font-size: clamp(1.6rem,5vw,3rem)`, `font-weight: 900`)
- **Body Copy Rule**: CSS variables `--color-brand-text-base: var(--color-brand-black)`; rule `p` (`font-size: 2rem`, `line-height: 1.5`, `font-weight: 400`)
- **Metadata & Index Rule**: rule `.label` (`font-size: 1rem`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `hopecancerresources-org` (`Hope Cancer Resources - Support. Educate. Prevent.`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.site-header> — `hopecancerresources-org`)**:
   - DOM & Selectors: Landmark `<header class="site-header template-home">` hosting `Hope Cancer Resources - Support. Edu` navigation (`Shop for Hope · About Hope · Our Story · Our Foundation · Staff`), DOM attributes (`data-template="base.twig"`), and stylesheet rule `content { background:fff;background-size:100% }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.site-header> — `hopecancerresources-org`)` (`hopecancerresources-org`) adapts across `@media (min-width: 800px)`, `@media (min-width: 768px)`, `@media (min-width: 960px)`, `@media (min-width: 1400px)` with `cubic-bezier(0.25,0.1,0.25,1)` transitions and links `Shop for Hope · About Hope · Our Story · Our Foundation · Staff`.
2. **Hero Stage & Focal Lead (<article.post-type-page> — `Support. Educate. Prevent.`)**:
   - DOM & Selectors: Landmark `<article class="post-type-page">` presenting display lead `Support. Educate. Prevent.` and copy excerpt *"Skip to main content"* over `#0e1829` canvas and `#edf1f4` ink.
   - Responsive Contract: Hero stage (`1440×5575px` desktop / `390×2400px` mobile) sets `#0e1829` background with `#edf1f4` headline `Support. Educate. Prevent.`.
3. **Primary Showcase & Content Grid (<section.page_heading> — `Driving real Change in Northwest A`)**:
   - DOM & Selectors: Landmark `<section class="page_heading section-block">` rendering section `Driving real Change in Northwest Arkansas (2025 R...` with copy *"About Back to About Hope Unscripted Podcast About Hope Our Story "*, asset references (`gtm.js`, `style.css`, `humans.txt`, `xmlrpc.php`), and grid rule `ge-template-wp-content .default-h... { padding-top:100px }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.page_heading> — `Driving real Change in Northwest A`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1400px`, `gap: 20px`) on desktop and Single-column vertical stack at `390px` viewport width with `20px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.stats_block_one> — `At Hope Cancer Resources, we walk `)**:
   - DOM & Selectors: Landmark `<section class="stats_block_one section-block">` framing `At Hope Cancer Resources, we walk beside those fa...` and `Ways We Help` (*"Hope Unscripted Podcast"*) with `#1fa0e5` surface cards, `#476577` accents, and `projects-template-default .post-h... { padding-top:80px }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.stats_block_one> — `At Hope Cancer Resources, we walk `)` uses `6px`, `100px`, `12px`, `10px` radii, `#476577` highlights, and assets (gtm.js, style.css, humans.txt).
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://hopecancerresources.org/`)**:
   - DOM & Selectors: Landmark `<footer class="site-footer">` anchoring `Hope Cancer Resources - Support.` footer links (`Shop for Hope · About Hope · Our Story · Our Foundation · Staff`), copy *"Board of Directors"*, and `#edf1f4` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.site-footer> — `https://hopecancerresources.org/`)` aligns to `1400px` extracted from `hopecancerresources-org` stylesheet with `20px` lateral canvas padding with `20px` grid gap and attributes (data-template="base.twig").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Skip to main content"*
- Copy Excerpt 2: *"About Back to About Hope Unscripted Podcast About Hope Our Story Our Foundation St..."*
- Copy Excerpt 3: *"Hope Unscripted Podcast"*
- Copy Excerpt 4: *"Board of Directors"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.25,0.1,0.25,1)`
- **Extracted Stylesheet Rules (`hopecancerresources-org`)**:
- `content { background:fff;background-size:100% }`
- `ge-template-wp-content .default-h... { padding-top:100px }`
- `projects-template-default .post-h... { padding-top:80px }`
- `.archive .standard-heading { padding-top:80px }`
- `.basic-page-padding { width:calc(100% - 40px);max-width:1400px;margin:0px auto;padding:20px 0... }`
- **Per-Selector Transition Rules**:
- **Selector `body *`**: `transition: all .2s ease-in` extracted from `hopecancerresources-org` stylesheet.
- **Selector `.reveal-overlay`**: `transition: mask-image .1s ease-out,-webkit-mask-image .1s ease-out` extracted from `hopecancerresources-org` stylesheet.
- **Selector `.skip-link`**: `transition: top .3s ease` extracted from `hopecancerresources-org` stylesheet.
- **Standard CSS Easing (`cubic-bezier(0.25,0.1,0.25,1)`)**: Default timing curve (no custom `cubic-bezier()` declared in static CSS).
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `hopecancerresources-org`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
