---
title: "UI Prompt Blueprint: faithibiza-com"
date: 2026-11-15
target: "[[overview|faithibiza-com]]"
status: analyzed
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#7a00df` canvas, `#ddd` ink, `#006ba1` accent)"
---

# UI Design System & Master Generation Blueprint: faithibiza-com

> **Faith Ibiza · VIP Ibiza Concierge Services** (https://faithibiza.com/) — Travelling to Ibiza and looking for a VIP experience? Our concierge services will ensure you experience all that the White Isle has to of...

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/faithibiza-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Faith Ibiza · VIP Ibiza Concierge Services** (`https://faithibiza.com/`). Travelling to Ibiza and looking for a VIP experience? Our concierge services will ensure you experience all that the White Isle has to of...
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#7a00df` canvas, `#ddd` ink, `#006ba1` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#7a00df` (`var(--wp-block-synced-color)` in `:root`) paired with `#ddd` primary typography and `#006ba1` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Afacad Flux` for display copy (`For the best Ibiza experience...`) with `Dream Orphans` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `600px` container bounds (`gap: 6.25rem`, padding `15px`) with `cubic-bezier(.25,.25,.75,.75)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/faithibiza-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `600px` extracted from `faithibiza-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `15px` lateral canvas padding with `6.25rem` grid gap.
- **Border Radius Scale**: `50%`, `500px`, `4px`, `8px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 600px`, `gap: 6.25rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `15px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-resolution:192dpi)`, `@media screen and (max-width:600px)`, `@media screen and (width <=620px)`, `@media screen and (orientation:landscape)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#7a00df` | `var(--wp-block-synced-color)` in `:root` |
| **Primary Typography Ink** | `#ddd` | `var(--wp-editor-canvas-background)` in `:root` |
| **Elevated Surface / Card Substrate** | `#007cba` | `var(--wp-admin-theme-color)` in `:root` |
| **Interactive Accent / Highlight** | `#006ba1` | `var(--wp-admin-theme-color-darker-10)` in `:root` |
| **Secondary / Muted Copy** | `#005a87` | `var(--wp-admin-theme-color-darker-20)` in `:root` |
| **Structural Hairline Border** | `#001d39` | `var(--cookieadmin-primary-color)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--i-star` | `url(https://faithibiza.com/wp-content/themes/general-block-wp/img/star.svg)` | Dimension / Scale Token |
| `--wp-block-synced-color` | `#7a00df` | Brand / Palette Token |
| `--wp-block-synced-color--rgb` | `122,0,223` | Brand / Palette Token |
| `--wp-bound-block-color` | `var(--wp-block-synced-color)` | Brand / Palette Token |
| `--wp-editor-canvas-background` | `#ddd` | Canvas / Surface Token |
| `--wp-admin-theme-color` | `#007cba` | Brand / Palette Token |
| `--wp-admin-theme-color--rgb` | `0,124,186` | Brand / Palette Token |
| `--wp-admin-theme-color-darker-10` | `#006ba1` | Canvas / Surface Token |
| `--wp-admin-theme-color-darker-10--rgb` | `0,107,160.5` | Canvas / Surface Token |
| `--wp-admin-theme-color-darker-20` | `#005a87` | Canvas / Surface Token |
| `--wp-admin-theme-color-darker-20--rgb` | `0,90,135` | Canvas / Surface Token |
| `--wp-admin-border-width-focus` | `2px` | Layout / Spatial Grid Token |
| `--wp-admin--admin-bar--position-offset` | `var(--wp-admin--admin-bar--height,0px)` | Dimension / Scale Token |
| `--pt` | `0px !important` | Dimension / Scale Token |
| `--pb` | `0px !important` | Dimension / Scale Token |
| `--bg-opacity` | `.75` | Canvas / Surface Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Afacad Flux`.
- **Primary Body Stack**: `Dream Orphans`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 2.5em`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: 2em`).
- **Body Copy**: rule `p` (`font-size: 10px`).
- **Metadata & Navigation Labels**: CSS variables `--modal-size-small: 500px`, `--gf-label-width: 30%`, `--gf-label-req-gap: 6px`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.25,.25,.75,.75)`, `cubic-bezier(.6,-.28,.735,.045)`, `cubic-bezier(.175,.885,.32,1.275)`.

### Per-Element Transition & Choreography Rules
- **Selector `.block-feature-cards .feature-car...`**: `transition: margin-right 300ms ease-out` extracted from `faithibiza-com` stylesheet.
- **Selector `.block-features .feature__title`**: `transition: transform 200ms ease-in-out` extracted from `faithibiza-com` stylesheet.
- **Selector `tures .feature-item .media-wrappe...`**: `transition: opacity 200ms ease-in-out` extracted from `faithibiza-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.25,.25,.75,.75)`)**: Governs interactive state transitions across `<header.site-header>` and `<main.site-main>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Faith Ibiza · VIP Ibiza Concierge Services │
│ ====================================================================== │
│ [ <header.site-header>     | About · About Us · Charity Work · Late ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <main.site-main>                                     |   │
│ | H1: For the best Ibiza experience...                             |   │
│ | Substrate: #7a00df    | Ink: #ddd       | Accent: #006ba1        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<main.site-main>          ) max-w: 600px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Book with Faith              |  | COME FOR THE BEACHES         | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 6.25re) | │
│ | [<header.site-heade] -> [<main.site-main>] -> [<main.site-main>] |   │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.site-footer>  ) | https://faithibiza.com/            │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.site-header> — `faithibiza-com`)**:
   - Landmark `<header class="site-header">` hosting `Faith Ibiza · VIP Ibiza Concierge Se` navigation (`About · About Us · Charity Work · Latest News · Where to stay`), DOM attributes (`data-optimized="1"`, `data-optimized="1"`, `data-optimized="2"`, `data-optimized="1"`), and stylesheet rule `ideo.background::-webkit-media-co... { display:none!important;opacity:0 }`.
2. **Hero Stage & Focal Lead (<main.site-main> — `For the best Ibiza experience...`)**:
   - Landmark `<main class="site-main">` presenting display lead `For the best Ibiza experience...` and copy excerpt *"About About Us Destination Management Corporate Experiences Chari"* over `#7a00df` canvas and `#ddd` ink.
3. **Primary Showcase & Content Grid (<main.site-main> — `Book with Faith`)**:
   - Landmark `<main class="site-main">` rendering section `Book with Faith` with copy *"Destination Management"*, asset references (`recaptcha__en.js`, `cdn.jsdelivr.net`, `unpkg.com`, `www.google.com`), and grid rule `it-media-controls-start-playback-... { display:none!important }`.
4. **Interactive Detail & Feature Matrix (<main.site-main> — `COME FOR THE BEACHES`)**:
   - Landmark `<main class="site-main">` framing `COME FOR THE BEACHES` and `Stay for the feeling` (*"Corporate Experiences"*) with `#007cba` surface cards, `#006ba1` accents, and `root { --wp-admin-border-width-focus:1.5px }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://faithibiza.com/`)**:
   - Landmark `<footer class="site-footer is-dark">` anchoring `Faith Ibiza · VIP Ibiza Concierg` footer links (`About · About Us · Charity Work · Latest News · Where to stay`), copy *"Where to stay Villas Hotels"*, and `#001d39` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: faithibiza-com (Faith Ibiza · VIP Ibiza Concierge Services)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `faithibiza-com` (**Faith Ibiza · VIP Ibiza Concierge Services** — `https://faithibiza.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#7a00df` canvas, `#ddd` ink, `#006ba1` accent).
- **Identity & Domain Context**: Travelling to Ibiza and looking for a VIP experience? Our concierge services will ensure you experience all that the White Isle has to of...
- **Primary Substrate**: `#7a00df` (`var(--wp-block-synced-color)` in `:root`), **Primary Ink**: `#ddd`, **Accent / Highlight**: `#006ba1`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#7a00df` (`var(--wp-block-synced-color)` in `:root`) paired with `#ddd` primary typography and `#006ba1` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Afacad Flux` for display copy (`For the best Ibiza experience...`) with `Dream Orphans` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `600px` container bounds (`gap: 6.25rem`, padding `15px`) with `cubic-bezier(.25,.25,.75,.75)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `faithibiza-com` in your global stylesheet:

:root {
  /* Faith Ibiza · VIP Ibiza Concierge Services (faithibiza-com) — Ground-Truth Extracted CSS Variables */
  --i-star: url(https://faithibiza.com/wp-content/themes/general-block-wp/img/star.svg); /* Dimension / Scale Token (faithibiza-com) */
  --wp-block-synced-color: #7a00df; /* Brand / Palette Token (faithibiza-com) */
  --wp-block-synced-color--rgb: 122,0,223; /* Brand / Palette Token (faithibiza-com) */
  --wp-bound-block-color: var(--wp-block-synced-color); /* Brand / Palette Token (faithibiza-com) */
  --wp-editor-canvas-background: #ddd; /* Canvas / Surface Token (faithibiza-com) */
  --wp-admin-theme-color: #007cba; /* Brand / Palette Token (faithibiza-com) */
  --wp-admin-theme-color--rgb: 0,124,186; /* Brand / Palette Token (faithibiza-com) */
  --wp-admin-theme-color-darker-10: #006ba1; /* Canvas / Surface Token (faithibiza-com) */
  --wp-admin-theme-color-darker-10--rgb: 0,107,160.5; /* Canvas / Surface Token (faithibiza-com) */
  --wp-admin-theme-color-darker-20: #005a87; /* Canvas / Surface Token (faithibiza-com) */
  --wp-admin-theme-color-darker-20--rgb: 0,90,135; /* Canvas / Surface Token (faithibiza-com) */
  --wp-admin-border-width-focus: 2px; /* Layout / Spatial Grid Token (faithibiza-com) */
  --wp-admin--admin-bar--position-offset: var(--wp-admin--admin-bar--height,0px); /* Dimension / Scale Token (faithibiza-com) */
  --pt: 0px !important; /* Dimension / Scale Token (faithibiza-com) */
  --pb: 0px !important; /* Dimension / Scale Token (faithibiza-com) */
  --bg-opacity: .75; /* Canvas / Surface Token (faithibiza-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#7a00df` — grounded in `var(--wp-block-synced-color)` in `:root`
- **Primary Typography Ink**: `#ddd` — grounded in `var(--wp-editor-canvas-background)` in `:root`
- **Elevated Surface / Card Substrate**: `#007cba` — grounded in `var(--wp-admin-theme-color)` in `:root`
- **Interactive Accent / Highlight**: `#006ba1` — grounded in `var(--wp-admin-theme-color-darker-10)` in `:root`
- **Secondary / Muted Copy**: `#005a87` — grounded in `var(--wp-admin-theme-color-darker-20)` in `:root`
- **Structural Hairline Border**: `#001d39` — grounded in `var(--cookieadmin-primary-color)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `600px` extracted from `faithibiza-com` stylesheet
- **Padding & Gutters**: `15px` lateral canvas padding with `6.25rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 600px`, `gap: 6.25rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `15px` horizontal padding
- **Media Queries**: `@media (min-resolution:192dpi)`, `@media screen and (max-width:600px)`, `@media screen and (width <=620px)`, `@media screen and (orientation:landscape)`
- **Corner Radii**: `50%`, `500px`, `4px`, `8px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Afacad Flux`
- **Body Font Stack**: `Dream Orphans`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: rule `h1` (`font-size: 2.5em`)
- **H2 Section Rule**: rule `h2` (`font-size: 2em`)
- **Body Copy Rule**: rule `p` (`font-size: 10px`)
- **Metadata & Index Rule**: CSS variables `--modal-size-small: 500px`, `--gf-label-width: 30%`, `--gf-label-req-gap: 6px`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `faithibiza-com` (`Faith Ibiza · VIP Ibiza Concierge Services`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.site-header> — `faithibiza-com`)**:
   - DOM & Selectors: Landmark `<header class="site-header">` hosting `Faith Ibiza · VIP Ibiza Concierge Se` navigation (`About · About Us · Charity Work · Latest News · Where to stay`), DOM attributes (`data-optimized="1"`, `data-optimized="1"`, `data-optimized="2"`, `data-optimized="1"`), and stylesheet rule `ideo.background::-webkit-media-co... { display:none!important;opacity:0 }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.site-header> — `faithibiza-com`)` (`faithibiza-com`) adapts across `@media (min-resolution:192dpi)`, `@media screen and (max-width:600px)`, `@media screen and (width <=620px)`, `@media screen and (orientation:landscape)` with `cubic-bezier(.25,.25,.75,.75)`, `cubic-bezier(.6,-.28,.735,.045)`, `cubic-bezier(.175,.885,.32,1.275)` transitions and links `About · About Us · Charity Work · Latest News · Where to stay`.
2. **Hero Stage & Focal Lead (<main.site-main> — `For the best Ibiza experience...`)**:
   - DOM & Selectors: Landmark `<main class="site-main">` presenting display lead `For the best Ibiza experience...` and copy excerpt *"About About Us Destination Management Corporate Experiences Chari"* over `#7a00df` canvas and `#ddd` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#7a00df` background with `#ddd` headline `For the best Ibiza experience...`.
3. **Primary Showcase & Content Grid (<main.site-main> — `Book with Faith`)**:
   - DOM & Selectors: Landmark `<main class="site-main">` rendering section `Book with Faith` with copy *"Destination Management"*, asset references (`recaptcha__en.js`, `cdn.jsdelivr.net`, `unpkg.com`, `www.google.com`), and grid rule `it-media-controls-start-playback-... { display:none!important }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<main.site-main> — `Book with Faith`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 600px`, `gap: 6.25rem`) on desktop and Single-column vertical stack at `390px` viewport width with `15px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<main.site-main> — `COME FOR THE BEACHES`)**:
   - DOM & Selectors: Landmark `<main class="site-main">` framing `COME FOR THE BEACHES` and `Stay for the feeling` (*"Corporate Experiences"*) with `#007cba` surface cards, `#006ba1` accents, and `root { --wp-admin-border-width-focus:1.5px }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<main.site-main> — `COME FOR THE BEACHES`)` uses `50%`, `500px`, `4px`, `8px` radii, `#006ba1` highlights, and assets (recaptcha__en.js, cdn.jsdelivr.net, unpkg.com).
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://faithibiza.com/`)**:
   - DOM & Selectors: Landmark `<footer class="site-footer is-dark">` anchoring `Faith Ibiza · VIP Ibiza Concierg` footer links (`About · About Us · Charity Work · Latest News · Where to stay`), copy *"Where to stay Villas Hotels"*, and `#001d39` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.site-footer> — `https://faithibiza.com/`)` aligns to `600px` extracted from `faithibiza-com` stylesheet with `15px` lateral canvas padding with `6.25rem` grid gap and attributes (data-optimized="1", data-optimized="1", data-optimized="2").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"About About Us Destination Management Corporate Experiences Charity Work Latest News"*
- Copy Excerpt 2: *"Destination Management"*
- Copy Excerpt 3: *"Corporate Experiences"*
- Copy Excerpt 4: *"Where to stay Villas Hotels"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.25,.25,.75,.75)`, `cubic-bezier(.6,-.28,.735,.045)`, `cubic-bezier(.175,.885,.32,1.275)`
- **Extracted Stylesheet Rules (`faithibiza-com`)**:
- `ideo.background::-webkit-media-co... { display:none!important;opacity:0 }`
- `it-media-controls-start-playback-... { display:none!important }`
- `root { --wp-admin-border-width-focus:1.5px }`
- `.wp-element-button { cursor:pointer }`
- `t .has-very-light-gray-background... { background-color:eee }`
- **Per-Selector Transition Rules**:
- **Selector `.block-feature-cards .feature-car...`**: `transition: margin-right 300ms ease-out` extracted from `faithibiza-com` stylesheet.
- **Selector `.block-features .feature__title`**: `transition: transform 200ms ease-in-out` extracted from `faithibiza-com` stylesheet.
- **Selector `tures .feature-item .media-wrappe...`**: `transition: opacity 200ms ease-in-out` extracted from `faithibiza-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.25,.25,.75,.75)`)**: Governs interactive state transitions across `<header.site-header>` and `<main.site-main>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `faithibiza-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
