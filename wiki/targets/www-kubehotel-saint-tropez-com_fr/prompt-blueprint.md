---
title: "UI Prompt Blueprint: www-kubehotel-saint-tropez-com_fr"
date: 2026-11-15
target: "www-kubehotel-saint-tropez-com_fr"
status: analyzed
capture: specimen
capture_desktop: dom
capture_mobile: specimen
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fdf9f4` ink, `#7c7c7c` accent)"
---

# UI Design System & Master Generation Blueprint: www-kubehotel-saint-tropez-com_fr

> **Hôtel 5 étoiles à Saint-Tropez – Nouveau site bientôt en ligne** (https://www.kubehotel-saint-tropez.com/fr) — Notre nouveau site arrive très bientôt. Hôtel, restaurants, bien-être et piscines à Saint-Tropez : revenez nous voir prochainement.

![Desktop Viewport Capture](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Hôtel 5 étoiles à Saint-Tropez – Nouveau site bientôt en ligne** (`https://www.kubehotel-saint-tropez.com/fr`). Notre nouveau site arrive très bientôt. Hôtel, restaurants, bien-être et piscines à Saint-Tropez : revenez nous voir prochainement.
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fdf9f4` ink, `#7c7c7c` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--swatch--black)` in `:root`) paired with `#fdf9f4` primary typography and `#7c7c7c` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Saphion` for display copy (`Les plus belles vacances ont le goût`) with `Inter Variable` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `940px` container bounds (`gap: 16px`, padding `9px`) with `cubic-bezier(.175,.885,.32,1.275)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Design Specimen (Offline WebGL/JS Fallback — not live site capture)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `940px` extracted from `www-kubehotel-saint-tropez-com_fr` stylesheet.
- **Canvas Lateral Padding & Spacing**: `9px` lateral canvas padding with `16px` grid gap.
- **Border Radius Scale**: `3px`, `100%`, `50%`, `var(--radius--main)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 940px`, `gap: 16px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `9px` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen and (max-width:991px)`, `@media screen and (max-width:767px)`, `@media screen and (max-width:479px)`, `@media (min-width:768px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--swatch--black)` in `:root` |
| **Primary Typography Ink** | `#e1dcd9` | `var(--swatch--grey-200)` in `:root` |
| **Elevated Surface / Card Substrate** | `#c6c6c6` | `var(--swatch--grey-300)` in `:root` |
| **Interactive Accent / Highlight** | `#7c7c7c` | `var(--swatch--grey-700)` in `:root` |
| **Secondary / Muted Copy** | `#484847` | `var(--swatch--grey-800)` in `:root` |
| **Structural Hairline Border** | `#fdf9f4` | `var(--swatch--beige)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--w-backdrop-animation` | `initial` | Motion / Easing Token |
| `--_theme---background` | `var(--swatch--beige)` | Canvas / Surface Token |
| `--_text-style---font-family` | `var(--_typography---font--primary-family)` | Typography Ink Token |
| `--_theme---text` | `var(--swatch--black)` | Typography Ink Token |
| `--_text-style---font-size` | `var(--_typography---font-size--text-main)` | Typography Ink Token |
| `--_text-style---line-height` | `var(--_typography---line-height--large)` | Typography Ink Token |
| `--_text-style---font-weight` | `var(--_typography---font--primary-light)` | Typography Ink Token |
| `--_text-style---letter-spacing` | `var(--_typography---letter-spacing--tight)` | Typography Ink Token |
| `--radius--main` | `.5rem` | Elevation / Border Token |
| `--_theme---background-2` | `var(--swatch--beige-2)` | Canvas / Surface Token |
| `--site--column-count` | `12` | Layout / Spatial Grid Token |
| `--_responsive---large` | `1` | Design System Custom Token |
| `--_responsive---medium` | `0` | Design System Custom Token |
| `--_responsive---small` | `0` | Design System Custom Token |
| `--_responsive---xsmall` | `0` | Design System Custom Token |
| `--max-width--small` | `calc(var(--site--viewport-max)*1rem)` | Layout / Spatial Grid Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Saphion`.
- **Primary Body Stack**: `Inter Variable`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: rule `h1` (`font-size: var(--_text-style---font-size)`, `line-height: var(--_text-style---l...`, `letter-spacing: var(--_text-style---l...`, `font-weight: var(--_text-s...`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: var(--_text-style---font-size)`, `line-height: var(--_text-style---l...`, `letter-spacing: var(--_text-style---l...`, `font-weight: var(--_text-s...`).
- **Body Copy**: rule `p` (`line-height: var(--_typography---l...`).
- **Metadata & Navigation Labels**: CSS variables `--_text-style---letter-spacing: var(--_typography---letter-spacing--tight)`, `--_responsive---small: 0`, `--_responsive---xsmall: 0`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.175,.885,.32,1.275)`.

### Per-Element Transition & Choreography Rules
- **Selector `.w-webflow-badge>img`**: `transition: unset` extracted from `www-kubehotel-saint-tropez-com_fr` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s,color .1s` extracted from `www-kubehotel-saint-tropez-com_fr` stylesheet.
- **Selector `.w-lightbox-control`**: `transition: all .3s` extracted from `www-kubehotel-saint-tropez-com_fr` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.175,.885,.32,1.275)`)**: Governs interactive state transitions across `<header.hero_header_wrap>` and `<section.hero_wrap>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Hôtel 5 étoiles à Saint-Tropez – Nouveau s │
│ ====================================================================== │
│ [ <header.hero_header_wrap | fr · en · it · ru                      ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hero_wrap>                                  |   │
│ | H1: Les plus belles vacances ont le goût de l’insouci...         |   │
│ | Substrate: #000       | Ink: #fdf9f4    | Accent: #7c7c7c        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.hero_wrap>       ) max-w: 940px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Hôtel - Restaurant - Spa - P |  | Ouverture 1 er mai 2027      | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 16px  ) | │
│ | [<header.hero_heade] -> [<section.hero_wrap] -> [<section.hero_wrap] │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.w-embed>      ) | https://www.kubehotel-saint-tropez │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.hero_header_wrap> — `www-kubehotel-saint-tropez-com_fr`)**:
   - Landmark `<header class="hero_header_wrap">` hosting `Hôtel 5 étoiles à Saint-Tropez – Nou` navigation (`fr · en · it · ru`), DOM attributes (`data-wf-domain="www.layne-sainttropez..."`, `data-wf-page="69c122f05101301b0245c797"`, `data-wf-site="69c122f05101301b0245c7c6"`, `data-padding-bottom="none"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
2. **Hero Stage & Focal Lead (<section.hero_wrap> — `Les plus belles vacances ont le go`)**:
   - Landmark `<section class="hero_wrap u-section">` presenting display lead `Les plus belles vacances ont le goût de l’insouci...` and copy excerpt *"Hôtel - Restaurant - Spa - Piscines"* over `#000` canvas and `#fdf9f4` ink.
3. **Primary Showcase & Content Grid (<section.hero_wrap> — `Hôtel - Restaurant - Spa - Piscine`)**:
   - Landmark `<section class="hero_wrap u-section">` rendering section `Hôtel - Restaurant - Spa - Piscines` with copy *"Ouverture 1 er mai 2027"*, asset references (`cdn.prod.website-files.com`, `layne-sainttropez.webflow.shared....`, `player.vimeo.com`, `vod-adaptive-ak.vimeocdn.com`), and grid rule `summary { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.hero_wrap> — `Ouverture 1 er mai 2027`)**:
   - Landmark `<section class="hero_wrap u-section">` framing `Ouverture 1 er mai 2027` and `Informations et réservations : info@layne-saintt` (*"Informations et réservations : info@layne-sainttropez.com"*) with `#c6c6c6` surface cards, `#7c7c7c` accents, and `video { vertical-align:baseline;display:inline-block }`.
5. **Colophon & Global Directory Footer (<footer.w-embed> — `https://www.kubehotel-saint-tropez.com/fr`)**:
   - Landmark `<footer class="w-embed">` anchoring `Hôtel 5 étoiles à Saint-Tropez –` footer links (`fr · en · it · ru`), copy *"Informations et réservations :"*, and `#fdf9f4` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-kubehotel-saint-tropez-com_fr (Hôtel 5 étoiles à Saint-Tropez – Nouveau site bientôt en ligne)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-kubehotel-saint-tropez-com_fr` (**Hôtel 5 étoiles à Saint-Tropez – Nouveau site bientôt en ligne** — `https://www.kubehotel-saint-tropez.com/fr`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fdf9f4` ink, `#7c7c7c` accent).
- **Identity & Domain Context**: Notre nouveau site arrive très bientôt. Hôtel, restaurants, bien-être et piscines à Saint-Tropez : revenez nous voir prochainement.
- **Primary Substrate**: `#000` (`var(--swatch--black)` in `:root`), **Primary Ink**: `#fdf9f4`, **Accent / Highlight**: `#7c7c7c`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--swatch--black)` in `:root`) paired with `#fdf9f4` primary typography and `#7c7c7c` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Saphion` for display copy (`Les plus belles vacances ont le goût`) with `Inter Variable` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `940px` container bounds (`gap: 16px`, padding `9px`) with `cubic-bezier(.175,.885,.32,1.275)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-kubehotel-saint-tropez-com_fr` in your global stylesheet:

:root {
  /* Hôtel 5 étoiles à Saint-Tropez – Nouveau site bientôt en ligne (www-kubehotel-saint-tropez-com_fr) — Ground-Truth Extracted CSS Variables */
  --w-backdrop-animation: initial; /* Motion / Easing Token (www-kubehotel-saint-tropez-com_fr) */
  --_theme---background: var(--swatch--beige); /* Canvas / Surface Token (www-kubehotel-saint-tropez-com_fr) */
  --_text-style---font-family: var(--_typography---font--primary-family); /* Typography Ink Token (www-kubehotel-saint-tropez-com_fr) */
  --_theme---text: var(--swatch--black); /* Typography Ink Token (www-kubehotel-saint-tropez-com_fr) */
  --_text-style---font-size: var(--_typography---font-size--text-main); /* Typography Ink Token (www-kubehotel-saint-tropez-com_fr) */
  --_text-style---line-height: var(--_typography---line-height--large); /* Typography Ink Token (www-kubehotel-saint-tropez-com_fr) */
  --_text-style---font-weight: var(--_typography---font--primary-light); /* Typography Ink Token (www-kubehotel-saint-tropez-com_fr) */
  --_text-style---letter-spacing: var(--_typography---letter-spacing--tight); /* Typography Ink Token (www-kubehotel-saint-tropez-com_fr) */
  --radius--main: .5rem; /* Elevation / Border Token (www-kubehotel-saint-tropez-com_fr) */
  --_theme---background-2: var(--swatch--beige-2); /* Canvas / Surface Token (www-kubehotel-saint-tropez-com_fr) */
  --site--column-count: 12; /* Layout / Spatial Grid Token (www-kubehotel-saint-tropez-com_fr) */
  --_responsive---large: 1; /* Design System Custom Token (www-kubehotel-saint-tropez-com_fr) */
  --_responsive---medium: 0; /* Design System Custom Token (www-kubehotel-saint-tropez-com_fr) */
  --_responsive---small: 0; /* Design System Custom Token (www-kubehotel-saint-tropez-com_fr) */
  --_responsive---xsmall: 0; /* Design System Custom Token (www-kubehotel-saint-tropez-com_fr) */
  --max-width--small: calc(var(--site--viewport-max)*1rem); /* Layout / Spatial Grid Token (www-kubehotel-saint-tropez-com_fr) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#000` — grounded in `var(--swatch--black)` in `:root`
- **Primary Typography Ink**: `#e1dcd9` — grounded in `var(--swatch--grey-200)` in `:root`
- **Elevated Surface / Card Substrate**: `#c6c6c6` — grounded in `var(--swatch--grey-300)` in `:root`
- **Interactive Accent / Highlight**: `#7c7c7c` — grounded in `var(--swatch--grey-700)` in `:root`
- **Secondary / Muted Copy**: `#484847` — grounded in `var(--swatch--grey-800)` in `:root`
- **Structural Hairline Border**: `#fdf9f4` — grounded in `var(--swatch--beige)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `940px` extracted from `www-kubehotel-saint-tropez-com_fr` stylesheet
- **Padding & Gutters**: `9px` lateral canvas padding with `16px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 940px`, `gap: 16px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `9px` horizontal padding
- **Media Queries**: `@media screen and (max-width:991px)`, `@media screen and (max-width:767px)`, `@media screen and (max-width:479px)`, `@media (min-width:768px)`
- **Corner Radii**: `3px`, `100%`, `50%`, `var(--radius--main)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Saphion`
- **Body Font Stack**: `Inter Variable`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: rule `h1` (`font-size: var(--_text-style---font-size)`, `line-height: var(--_text-style---l...`, `letter-spacing: var(--_text-style---l...`, `font-weight: var(--_text-s...`)
- **H2 Section Rule**: rule `h2` (`font-size: var(--_text-style---font-size)`, `line-height: var(--_text-style---l...`, `letter-spacing: var(--_text-style---l...`, `font-weight: var(--_text-s...`)
- **Body Copy Rule**: rule `p` (`line-height: var(--_typography---l...`)
- **Metadata & Index Rule**: CSS variables `--_text-style---letter-spacing: var(--_typography---letter-spacing--tight)`, `--_responsive---small: 0`, `--_responsive---xsmall: 0`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-kubehotel-saint-tropez-com_fr` (`Hôtel 5 étoiles à Saint-Tropez – Nouveau site bientôt en ligne`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.hero_header_wrap> — `www-kubehotel-saint-tropez-com_fr`)**:
   - DOM & Selectors: Landmark `<header class="hero_header_wrap">` hosting `Hôtel 5 étoiles à Saint-Tropez – Nou` navigation (`fr · en · it · ru`), DOM attributes (`data-wf-domain="www.layne-sainttropez..."`, `data-wf-page="69c122f05101301b0245c797"`, `data-wf-site="69c122f05101301b0245c7c6"`, `data-padding-bottom="none"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.hero_header_wrap> — `www-kubehotel-saint-tropez-com_fr`)` (`www-kubehotel-saint-tropez-com_fr`) adapts across `@media screen and (max-width:991px)`, `@media screen and (max-width:767px)`, `@media screen and (max-width:479px)`, `@media (min-width:768px)` with `cubic-bezier(.175,.885,.32,1.275)` transitions and links `fr · en · it · ru`.
2. **Hero Stage & Focal Lead (<section.hero_wrap> — `Les plus belles vacances ont le go`)**:
   - DOM & Selectors: Landmark `<section class="hero_wrap u-section">` presenting display lead `Les plus belles vacances ont le goût de l’insouci...` and copy excerpt *"Hôtel - Restaurant - Spa - Piscines"* over `#000` canvas and `#fdf9f4` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#000` background with `#fdf9f4` headline `Les plus belles vacances ont le goût de l’insouci...`.
3. **Primary Showcase & Content Grid (<section.hero_wrap> — `Hôtel - Restaurant - Spa - Piscine`)**:
   - DOM & Selectors: Landmark `<section class="hero_wrap u-section">` rendering section `Hôtel - Restaurant - Spa - Piscines` with copy *"Ouverture 1 er mai 2027"*, asset references (`cdn.prod.website-files.com`, `layne-sainttropez.webflow.shared....`, `player.vimeo.com`, `vod-adaptive-ak.vimeocdn.com`), and grid rule `summary { display:block }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.hero_wrap> — `Hôtel - Restaurant - Spa - Piscine`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 940px`, `gap: 16px`) on desktop and Single-column vertical stack at `390px` viewport width with `9px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.hero_wrap> — `Ouverture 1 er mai 2027`)**:
   - DOM & Selectors: Landmark `<section class="hero_wrap u-section">` framing `Ouverture 1 er mai 2027` and `Informations et réservations : info@layne-saintt` (*"Informations et réservations : info@layne-sainttropez.com"*) with `#c6c6c6` surface cards, `#7c7c7c` accents, and `video { vertical-align:baseline;display:inline-block }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.hero_wrap> — `Ouverture 1 er mai 2027`)` uses `3px`, `100%`, `50%`, `var(--radius--main)` radii, `#7c7c7c` highlights, and assets (cdn.prod.website-files.com, layne-sainttropez.webflow.shared...., player.vimeo.com).
5. **Colophon & Global Directory Footer (<footer.w-embed> — `https://www.kubehotel-saint-tropez.com/fr`)**:
   - DOM & Selectors: Landmark `<footer class="w-embed">` anchoring `Hôtel 5 étoiles à Saint-Tropez –` footer links (`fr · en · it · ru`), copy *"Informations et réservations :"*, and `#fdf9f4` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.w-embed> — `https://www.kubehotel-saint-tropez.com/fr`)` aligns to `940px` extracted from `www-kubehotel-saint-tropez-com_fr` stylesheet with `9px` lateral canvas padding with `16px` grid gap and attributes (data-wf-domain="www.layne-sainttropez...", data-wf-page="69c122f05101301b0245c797", data-wf-site="69c122f05101301b0245c7c6").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Hôtel - Restaurant - Spa - Piscines"*
- Copy Excerpt 2: *"Ouverture 1 er mai 2027"*
- Copy Excerpt 3: *"Informations et réservations : info@layne-sainttropez.com"*
- Copy Excerpt 4: *"Informations et réservations :"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.175,.885,.32,1.275)`
- **Extracted Stylesheet Rules (`www-kubehotel-saint-tropez-com_fr`)**:
- `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`
- `summary { display:block }`
- `video { vertical-align:baseline;display:inline-block }`
- `template { display:none }`
- `strong { font-weight:700 }`
- **Per-Selector Transition Rules**:
- **Selector `.w-webflow-badge>img`**: `transition: unset` extracted from `www-kubehotel-saint-tropez-com_fr` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s,color .1s` extracted from `www-kubehotel-saint-tropez-com_fr` stylesheet.
- **Selector `.w-lightbox-control`**: `transition: all .3s` extracted from `www-kubehotel-saint-tropez-com_fr` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.175,.885,.32,1.275)`)**: Governs interactive state transitions across `<header.hero_header_wrap>` and `<section.hero_wrap>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-kubehotel-saint-tropez-com_fr`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
