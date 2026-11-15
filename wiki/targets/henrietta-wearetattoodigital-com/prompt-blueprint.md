---
title: "UI Prompt Blueprint: henrietta-wearetattoodigital-com"
date: 2026-11-15
target: "[[overview|henrietta-wearetattoodigital-com]]"
status: analyzed
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#e3a898` / `#8b231a`)"
---

# UI Design System & Master Generation Blueprint: henrietta-wearetattoodigital-com

> **Henrietta Said : Scandalously Spicy** (https://henrietta.wearetattoodigital.com/) — It’s hard to contain this kind of spiciness. That’s why we’re bringing our scandalously spicy selves to the mainstream with bold wing-fla...

![Desktop Viewport Capture (1440x19740)](file:///root/projects/fleet/wiki/targets/henrietta-wearetattoodigital-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Henrietta Said : Scandalously Spicy** (`https://henrietta.wearetattoodigital.com/`). It’s hard to contain this kind of spiciness. That’s why we’re bringing our scandalously spicy selves to the mainstream with bold wing-fla...
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#e3a898` / `#8b231a`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#e3a898` (`var(--body)` in `:root`) paired with `#8b231a` primary typography and `#8b231a` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Changa One` for display copy (`home`) with `Thedodgerinky` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `940px` container bounds (`gap: 16px`, padding `9px`) with `cubic-bezier(.68,-.55,.265,1.55)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/henrietta-wearetattoodigital-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×19740px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `940px` extracted from `henrietta-wearetattoodigital-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `9px` lateral canvas padding with `16px` grid gap.
- **Border Radius Scale**: `3px`, `100%`, `50%`, `2px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 940px`, `gap: 16px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `9px` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen and (max-width: 991px)`, `@media screen and (max-width: 767px)`, `@media screen and (max-width: 479px)`, `@media (min-width: 768px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#e3a898` | `var(--body)` in `:root` |
| **Primary Typography Ink** | `#d32929` | `var(--kimchi-red)` in `:root` |
| **Elevated Surface / Card Substrate** | `#eae6e3` | `var(--light-grey)` in `:root` |
| **Interactive Accent / Highlight** | `#8b231a` | `var(--brown-chicken)` in `:root` |
| **Secondary / Muted Copy** | `#f45016` | `var(--orange)` in `:root` |
| **Structural Hairline Border** | `#efc415` | `var(--lemon)` in `:root` |
| **Variable Token (`--dark`)** | `#2d2a26` | `var(--dark)` in `:root` |
| **Variable Token (`--white`)** | `#fff` | `var(--white)` in `:root` |
| **Variable Token (`--black`)** | `#0E0E0E` | `var(--black)` in `:root` |
| **Variable Token (`--salmon`)** | `#f7894e` | `var(--salmon)` in `:root` |
| **Variable Token (`--dark-red`)** | `#761615` | `var(--dark-red)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--w-backdrop-animation` | `initial` | Motion / Easing Token |
| `--body` | `#e3a898` | Color / Atmospheric Token |
| `--kimchi-red` | `#d32929` | Color / Atmospheric Token |
| `--light-grey` | `#eae6e3` | Canvas / Surface Token |
| `--brown-chicken` | `#8b231a` | Color / Atmospheric Token |
| `--orange` | `#f45016` | Color / Atmospheric Token |
| `--lemon` | `#efc415` | Color / Atmospheric Token |
| `--dark` | `#2d2a26` | Canvas / Surface Token |
| `--white` | `#fff` | Canvas / Surface Token |
| `--black` | `#0E0E0E` | Canvas / Surface Token |
| `--salmon` | `#f7894e` | Color / Atmospheric Token |
| `--dark-red` | `#761615` | Canvas / Surface Token |
| `--blush` | `#e3a898` | Color / Atmospheric Token |
| `--hst-duration-exit` | `0.8s` | Motion / Easing Token |
| `--hst-duration-enter` | `0.95s` | Motion / Easing Token |
| `--hst-easing` | `cubic-bezier(0.76, 0, 0.24, 1)` | Motion / Easing Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Changa One`.
- **Primary Body Stack**: `Thedodgerinky`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 2em`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: 32px`, `line-height: 36px`).
- **Body Copy**: CSS variables `--body: #e3a898`; rule `body` (`font-size: 14px`, `line-height: 20px`).
- **Metadata & Navigation Labels**: rule `small` (`font-size: 80%`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.68,-.55,.265,1.55)`, `cubic-bezier(0.76,0,0.24,1)`, `cubic-bezier(0.215,0.61,0.355,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.w-webflow-badge > img`**: `transition: unset` extracted from `henrietta-wearetattoodigital-com` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s, color .1s` extracted from `henrietta-wearetattoodigital-com` stylesheet.
- **Selector `.w-lightbox-control`**: `transition: all .3s` extracted from `henrietta-wearetattoodigital-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.68,-.55,.265,1.55)`)**: Governs interactive state transitions across `<nav.our-products-list>` and `<div.preloader>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Lottie Vector Animation Player, HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Henrietta Said : Scandalously Spicy        │
│ ====================================================================== │
│ [ <nav.our-products-list>  | ancho kimchi · original buffalo · lemo ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <div.preloader>                                      |   │
│ | H1: home                                                         |   │
│ | Substrate: #e3a898    | Ink: #8b231a    | Accent: #8b231a        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<div.preloader>           ) max-w: 940px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | scandal pages                |  | our story                    | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 16px  ) | │
│ | [<nav.our-products-] -> [<div.preloader>] -> [<div.preloader>] |     │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.lenis>        ) | https://henrietta.wearetattoodigit │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.our-products-list> — `henrietta-wearetattoodigital-com`)**:
   - Landmark `<nav class="our-products-list w-dropdown-list">` hosting `Henrietta Said : Scandalously Spicy` navigation (`ancho kimchi · original buffalo · lemon pepper`), DOM attributes (`data-wf-domain="henrietta.wearetattoo..."`, `data-wf-page="69fc9bd508ea045856fc2e42"`, `data-wf-site="69fc9bd208ea045856fc2c0a"`, `data-preloader-counter`), and stylesheet rule `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`.
2. **Hero Stage & Focal Lead (<div.preloader> — `home`)**:
   - Landmark `<div class="preloader">` presenting display lead `home` and copy excerpt *"s c a n d a l p a g e s"* over `#e3a898` canvas and `#8b231a` ink.
3. **Primary Showcase & Content Grid (<div.preloader> — `scandal pages`)**:
   - Landmark `<div class="preloader">` rendering section `scandal pages` with copy *"NASHVILLE HOT CHICKEN"*, asset references (`cdn.prod.website-files.com`, `henrietta-said.webflow.shared.afe...`, `fonts.googleapis.com`, `fonts.gstatic.com`), and grid rule `body { margin: 0; }`.
4. **Interactive Detail & Feature Matrix (<div.preloader> — `our story`)**:
   - Landmark `<div class="preloader">` framing `our story` and `press` (*"nashville hot chicken"*) with `#eae6e3` surface cards, `#8b231a` accents, and `summary { display: block; }`.
5. **Colophon & Global Directory Footer (<footer.lenis> — `https://henrietta.wearetattoodigital.com/`)**:
   - Landmark `<footer class="lenis">` anchoring `Henrietta Said : Scandalously Sp` footer links (`ancho kimchi · original buffalo · lemon pepper`), copy *"Jumbo roasted peanuts with a fusion of flavorfully fun ancho"*, and `#efc415` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: henrietta-wearetattoodigital-com (Henrietta Said : Scandalously Spicy)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `henrietta-wearetattoodigital-com` (**Henrietta Said : Scandalously Spicy** — `https://henrietta.wearetattoodigital.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#e3a898` / `#8b231a`).
- **Identity & Domain Context**: It’s hard to contain this kind of spiciness. That’s why we’re bringing our scandalously spicy selves to the mainstream with bold wing-fla...
- **Primary Substrate**: `#e3a898` (`var(--body)` in `:root`), **Primary Ink**: `#8b231a`, **Accent / Highlight**: `#8b231a`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#e3a898` (`var(--body)` in `:root`) paired with `#8b231a` primary typography and `#8b231a` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Changa One` for display copy (`home`) with `Thedodgerinky` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `940px` container bounds (`gap: 16px`, padding `9px`) with `cubic-bezier(.68,-.55,.265,1.55)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `henrietta-wearetattoodigital-com` in your global stylesheet:

:root {
  /* Henrietta Said : Scandalously Spicy (henrietta-wearetattoodigital-com) — Ground-Truth Extracted CSS Variables */
  --w-backdrop-animation: initial; /* Motion / Easing Token (henrietta-wearetattoodigital-com) */
  --body: #e3a898; /* Color / Atmospheric Token (henrietta-wearetattoodigital-com) */
  --kimchi-red: #d32929; /* Color / Atmospheric Token (henrietta-wearetattoodigital-com) */
  --light-grey: #eae6e3; /* Canvas / Surface Token (henrietta-wearetattoodigital-com) */
  --brown-chicken: #8b231a; /* Color / Atmospheric Token (henrietta-wearetattoodigital-com) */
  --orange: #f45016; /* Color / Atmospheric Token (henrietta-wearetattoodigital-com) */
  --lemon: #efc415; /* Color / Atmospheric Token (henrietta-wearetattoodigital-com) */
  --dark: #2d2a26; /* Canvas / Surface Token (henrietta-wearetattoodigital-com) */
  --white: #fff; /* Canvas / Surface Token (henrietta-wearetattoodigital-com) */
  --black: #0E0E0E; /* Canvas / Surface Token (henrietta-wearetattoodigital-com) */
  --salmon: #f7894e; /* Color / Atmospheric Token (henrietta-wearetattoodigital-com) */
  --dark-red: #761615; /* Canvas / Surface Token (henrietta-wearetattoodigital-com) */
  --blush: #e3a898; /* Color / Atmospheric Token (henrietta-wearetattoodigital-com) */
  --hst-duration-exit: 0.8s; /* Motion / Easing Token (henrietta-wearetattoodigital-com) */
  --hst-duration-enter: 0.95s; /* Motion / Easing Token (henrietta-wearetattoodigital-com) */
  --hst-easing: cubic-bezier(0.76, 0, 0.24, 1); /* Motion / Easing Token (henrietta-wearetattoodigital-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#e3a898` — grounded in `var(--body)` in `:root`
- **Primary Typography Ink**: `#d32929` — grounded in `var(--kimchi-red)` in `:root`
- **Elevated Surface / Card Substrate**: `#eae6e3` — grounded in `var(--light-grey)` in `:root`
- **Interactive Accent / Highlight**: `#8b231a` — grounded in `var(--brown-chicken)` in `:root`
- **Secondary / Muted Copy**: `#f45016` — grounded in `var(--orange)` in `:root`
- **Structural Hairline Border**: `#efc415` — grounded in `var(--lemon)` in `:root`
- **Variable Token (`--dark`)**: `#2d2a26` — grounded in `var(--dark)` in `:root`
- **Variable Token (`--white`)**: `#fff` — grounded in `var(--white)` in `:root`
- **Variable Token (`--black`)**: `#0E0E0E` — grounded in `var(--black)` in `:root`
- **Variable Token (`--salmon`)**: `#f7894e` — grounded in `var(--salmon)` in `:root`
- **Variable Token (`--dark-red`)**: `#761615` — grounded in `var(--dark-red)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×19740px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `940px` extracted from `henrietta-wearetattoodigital-com` stylesheet
- **Padding & Gutters**: `9px` lateral canvas padding with `16px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 940px`, `gap: 16px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `9px` horizontal padding
- **Media Queries**: `@media screen and (max-width: 991px)`, `@media screen and (max-width: 767px)`, `@media screen and (max-width: 479px)`, `@media (min-width: 768px)`
- **Corner Radii**: `3px`, `100%`, `50%`, `2px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Changa One`
- **Body Font Stack**: `Thedodgerinky`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: rule `h1` (`font-size: 2em`)
- **H2 Section Rule**: rule `h2` (`font-size: 32px`, `line-height: 36px`)
- **Body Copy Rule**: CSS variables `--body: #e3a898`; rule `body` (`font-size: 14px`, `line-height: 20px`)
- **Metadata & Index Rule**: rule `small` (`font-size: 80%`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `henrietta-wearetattoodigital-com` (`Henrietta Said : Scandalously Spicy`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.our-products-list> — `henrietta-wearetattoodigital-com`)**:
   - DOM & Selectors: Landmark `<nav class="our-products-list w-dropdown-list">` hosting `Henrietta Said : Scandalously Spicy` navigation (`ancho kimchi · original buffalo · lemon pepper`), DOM attributes (`data-wf-domain="henrietta.wearetattoo..."`, `data-wf-page="69fc9bd508ea045856fc2e42"`, `data-wf-site="69fc9bd208ea045856fc2c0a"`, `data-preloader-counter`), and stylesheet rule `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.our-products-list> — `henrietta-wearetattoodigital-com`)` (`henrietta-wearetattoodigital-com`) adapts across `@media screen and (max-width: 991px)`, `@media screen and (max-width: 767px)`, `@media screen and (max-width: 479px)`, `@media (min-width: 768px)` with `cubic-bezier(.68,-.55,.265,1.55)`, `cubic-bezier(0.76,0,0.24,1)`, `cubic-bezier(0.215,0.61,0.355,1)` transitions and links `ancho kimchi · original buffalo · lemon pepper`.
2. **Hero Stage & Focal Lead (<div.preloader> — `home`)**:
   - DOM & Selectors: Landmark `<div class="preloader">` presenting display lead `home` and copy excerpt *"s c a n d a l p a g e s"* over `#e3a898` canvas and `#8b231a` ink.
   - Responsive Contract: Hero stage (`1440×19740px` desktop / `390×2400px` mobile) sets `#e3a898` background with `#8b231a` headline `home`.
3. **Primary Showcase & Content Grid (<div.preloader> — `scandal pages`)**:
   - DOM & Selectors: Landmark `<div class="preloader">` rendering section `scandal pages` with copy *"NASHVILLE HOT CHICKEN"*, asset references (`cdn.prod.website-files.com`, `henrietta-said.webflow.shared.afe...`, `fonts.googleapis.com`, `fonts.gstatic.com`), and grid rule `body { margin: 0; }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<div.preloader> — `scandal pages`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 940px`, `gap: 16px`) on desktop and Single-column vertical stack at `390px` viewport width with `9px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<div.preloader> — `our story`)**:
   - DOM & Selectors: Landmark `<div class="preloader">` framing `our story` and `press` (*"nashville hot chicken"*) with `#eae6e3` surface cards, `#8b231a` accents, and `summary { display: block; }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<div.preloader> — `our story`)` uses `3px`, `100%`, `50%`, `2px` radii, `#8b231a` highlights, and assets (cdn.prod.website-files.com, henrietta-said.webflow.shared.afe..., fonts.googleapis.com).
5. **Colophon & Global Directory Footer (<footer.lenis> — `https://henrietta.wearetattoodigital.com/`)**:
   - DOM & Selectors: Landmark `<footer class="lenis">` anchoring `Henrietta Said : Scandalously Sp` footer links (`ancho kimchi · original buffalo · lemon pepper`), copy *"Jumbo roasted peanuts with a fusion of flavorfully fun ancho"*, and `#efc415` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.lenis> — `https://henrietta.wearetattoodigital.com/`)` aligns to `940px` extracted from `henrietta-wearetattoodigital-com` stylesheet with `9px` lateral canvas padding with `16px` grid gap and attributes (data-wf-domain="henrietta.wearetattoo...", data-wf-page="69fc9bd508ea045856fc2e42", data-wf-site="69fc9bd208ea045856fc2c0a").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"s c a n d a l p a g e s"*
- Copy Excerpt 2: *"NASHVILLE HOT CHICKEN"*
- Copy Excerpt 3: *"nashville hot chicken"*
- Copy Excerpt 4: *"Jumbo roasted peanuts with a fusion of flavorfully fun ancho kimchi seasonings. Sp..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.68,-.55,.265,1.55)`, `cubic-bezier(0.76,0,0.24,1)`, `cubic-bezier(0.215,0.61,0.355,1)`
- **Extracted Stylesheet Rules (`henrietta-wearetattoodigital-com`)**:
- `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`
- `body { margin: 0; }`
- `summary { display: block; }`
- `video { vertical-align: baseline; display: inline-block; }`
- `template { display: none; }`
- **Per-Selector Transition Rules**:
- **Selector `.w-webflow-badge > img`**: `transition: unset` extracted from `henrietta-wearetattoodigital-com` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s, color .1s` extracted from `henrietta-wearetattoodigital-com` stylesheet.
- **Selector `.w-lightbox-control`**: `transition: all .3s` extracted from `henrietta-wearetattoodigital-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.68,-.55,.265,1.55)`)**: Governs interactive state transitions across `<nav.our-products-list>` and `<div.preloader>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Lottie Vector Animation Player, HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `henrietta-wearetattoodigital-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
