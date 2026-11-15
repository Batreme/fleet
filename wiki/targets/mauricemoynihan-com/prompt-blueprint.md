---
title: "UI Prompt Blueprint: mauricemoynihan-com"
date: 2026-11-15
target: "[[overview|mauricemoynihan-com]]"
status: analyzed
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#EFEDE6` / `#4c4a43`)"
---

# UI Design System & Master Generation Blueprint: mauricemoynihan-com

> **Maurice Moynihan** (https://mauricemoynihan.com) — Advertising creative director, Melbourne. A portfolio. Some of it won things. It also has an album, which hasn’t.

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/mauricemoynihan-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Maurice Moynihan** (`https://mauricemoynihan.com`). Advertising creative director, Melbourne. A portfolio. Some of it won things. It also has an album, which hasn’t.
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#EFEDE6` / `#4c4a43`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#EFEDE6` (`var(--bone)` in `:root`) paired with `#161511` primary typography and `#4c4a43` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Archivo` for display copy (`Maurice Moynihan`) with `Space Mono` and `Space Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `768px` container bounds (`gap: 1rem`, padding `.7rem`) with `cubic-bezier(.35,.05,.4,1)` easing and Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/mauricemoynihan-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `768px` extracted from `mauricemoynihan-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `.7rem` lateral canvas padding with `1rem` grid gap.
- **Border Radius Scale**: `1px`, `2px`, `50%`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 768px`, `gap: 1rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `.7rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (max-height:800px) and (min-width:769px)`, `@media (min-width:769px)`, `@media (max-width:768px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#EFEDE6` | `var(--bone)` in `:root` |
| **Primary Typography Ink** | `#E6E3D9` | `var(--bone-deep)` in `:root` |
| **Elevated Surface / Card Substrate** | `#161511` | `var(--ink)` in `:root` |
| **Interactive Accent / Highlight** | `#4c4a43` | `var(--ink-soft)` in `:root` |
| **Secondary / Muted Copy** | `#FFFFFF` | `var(--paper)` in `:root` |
| **Structural Hairline Border** | `#ff0000` | `::selection { background: red }` (`#ff0000`) |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bone` | `#EFEDE6` | Color / Atmospheric Token |
| `--bone-deep` | `#E6E3D9` | Color / Atmospheric Token |
| `--ink` | `#161511` | Typography Ink Token |
| `--ink-soft` | `#4c4a43` | Typography Ink Token |
| `--red` | `#161511` | Color / Atmospheric Token |
| `--red-deep` | `#161511` | Color / Atmospheric Token |
| `--red-lift` | `#EFEDE6` | Color / Atmospheric Token |
| `--paper` | `#FFFFFF` | Canvas / Surface Token |
| `--sans` | `"Archivo","Helvetica Neue",Helvetica,Arial,sans-serif` | Typography / Scale Token |
| `--mono` | `"Space Mono","Courier New",monospace` | Typography / Scale Token |
| `--serif` | `"Archivo","Helvetica Neue",Helvetica,Arial,sans-serif` | Typography / Scale Token |
| `--pad` | `clamp(1rem, 3.4vw, 3rem)` | Layout / Spatial Grid Token |
| `--hair` | `1.5px solid var(--ink)` | Dimension / Scale Token |
| `--card` | `clamp(7rem,13.2vw,11.5rem)` | Dimension / Scale Token |
| `--shelf-pad` | `clamp(1rem,3vh,2.4rem)` | Layout / Spatial Grid Token |
| `--shelf` | `calc(var(--card) * 1.22 + var(--shelf-pad) + var(--nav-h) + 1.6rem + 1.8vw)` | Dimension / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Archivo`.
- **Primary Body Stack**: `Space Mono`.
- **Technical / Metadata Stack**: `Space Mono`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: rule `h1` (`font-size: clamp(1.9rem,5.2vw,4.4rem)`, `line-height: 1.02`, `letter-spacing: -.02em`, `font-weight: 900`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(2rem,7vw,5.2rem)`, `line-height: .92`, `letter-spacing: -.02em`, `font-weight: 900`).
- **Body Copy**: rule `body` (`font-size: 1.0625rem`, `line-height: 1.55`).
- **Metadata & Navigation Labels**: CSS variables `--mono: "Space Mono","Courier New",monospace`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.35,.05,.4,1)`, `cubic-bezier(.45,0,.25,1)`, `cubic-bezier(.2,.8,.3,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.skip`**: `transition: top .15s` extracted from `mauricemoynihan-com` stylesheet.
- **Selector `.nav--home`**: `transition: background .18s ease` extracted from `mauricemoynihan-com` stylesheet.
- **Selector `media (prefers-reduced-motion:red...`**: `transition: none` extracted from `mauricemoynihan-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.35,.05,.4,1)`)**: Governs interactive state transitions across `<header.nav>` and `<section.hero>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Maurice Moynihan                           │
│ ====================================================================== │
│ [ <header.nav>             | Advertising · adnauseum.ai · Music · A ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hero>                                       |   │
│ | H1: Maurice Moynihan                                             |   │
│ | Substrate: #EFEDE6    | Ink: #161511    | Accent: #4c4a43        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.hero>            ) max-w: 768px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Skip to the content          |  | is a Creative Director, Song | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 1rem  ) | │
│ | [<header.nav>] -> [<section.hero>] -> [<section.hero>] |             │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer>       ) | https://mauricemoynihan.com        │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.nav> — `mauricemoynihan-com`)**:
   - Landmark `<header class="nav nav--home">` hosting `Maurice Moynihan` navigation (`Advertising · adnauseum.ai · Music · About`), DOM attributes (`data-src="assets/koi/koi_a.webp"`, `data-src2="assets/koi/koi_b.webp"`, `data-panel`, `data-ink-top="0.7539"`), and stylesheet rule `html { scroll-behavior:smooth; }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Maurice Moynihan`)**:
   - Landmark `<section class="hero">` presenting display lead `Maurice Moynihan` and copy excerpt *"Skip to the content"* over `#EFEDE6` canvas and `#161511` ink.
3. **Primary Showcase & Content Grid (<section.hero> — `Skip to the content`)**:
   - Landmark `<section class="hero">` rendering section `Skip to the content` with copy *"is a Creative Director, Songwriter and Governor of the Central Ba"*, asset references (`apple-touch-icon.png`, `fonts.googleapis.com`, `fonts.gstatic.com`, `css2`), and grid rule `video { max-width:100%;display:block; }`.
4. **Interactive Detail & Feature Matrix (<section.hero> — `is a Creative Director, Songwriter`)**:
   - Landmark `<section class="hero">` framing `is a Creative Director, Songwriter and Governor ` and `Governor of the Central Bank of Ireland` (*"Governor of the Central Bank of Ireland"*) with `#161511` surface cards, `#4c4a43` accents, and `selection { background:var(--red);color:var(--bone); }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://mauricemoynihan.com`)**:
   - Landmark `<footer class="footer">` anchoring `Maurice Moynihan` footer links (`Advertising · adnauseum.ai · Music · About`), copy *"01 Advertising Things that made people buy other things."*, and `#ff0000` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: mauricemoynihan-com (Maurice Moynihan)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `mauricemoynihan-com` (**Maurice Moynihan** — `https://mauricemoynihan.com`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#EFEDE6` / `#4c4a43`).
- **Identity & Domain Context**: Advertising creative director, Melbourne. A portfolio. Some of it won things. It also has an album, which hasn’t.
- **Primary Substrate**: `#EFEDE6` (`var(--bone)` in `:root`), **Primary Ink**: `#161511`, **Accent / Highlight**: `#4c4a43`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#EFEDE6` (`var(--bone)` in `:root`) paired with `#161511` primary typography and `#4c4a43` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Archivo` for display copy (`Maurice Moynihan`) with `Space Mono` and `Space Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `768px` container bounds (`gap: 1rem`, padding `.7rem`) with `cubic-bezier(.35,.05,.4,1)` easing and Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `mauricemoynihan-com` in your global stylesheet:

:root {
  /* Maurice Moynihan (mauricemoynihan-com) — Ground-Truth Extracted CSS Variables */
  --bone: #EFEDE6; /* Color / Atmospheric Token (mauricemoynihan-com) */
  --bone-deep: #E6E3D9; /* Color / Atmospheric Token (mauricemoynihan-com) */
  --ink: #161511; /* Typography Ink Token (mauricemoynihan-com) */
  --ink-soft: #4c4a43; /* Typography Ink Token (mauricemoynihan-com) */
  --red: #161511; /* Color / Atmospheric Token (mauricemoynihan-com) */
  --red-deep: #161511; /* Color / Atmospheric Token (mauricemoynihan-com) */
  --red-lift: #EFEDE6; /* Color / Atmospheric Token (mauricemoynihan-com) */
  --paper: #FFFFFF; /* Canvas / Surface Token (mauricemoynihan-com) */
  --sans: "Archivo","Helvetica Neue",Helvetica,Arial,sans-serif; /* Typography / Scale Token (mauricemoynihan-com) */
  --mono: "Space Mono","Courier New",monospace; /* Typography / Scale Token (mauricemoynihan-com) */
  --serif: "Archivo","Helvetica Neue",Helvetica,Arial,sans-serif; /* Typography / Scale Token (mauricemoynihan-com) */
  --pad: clamp(1rem, 3.4vw, 3rem); /* Layout / Spatial Grid Token (mauricemoynihan-com) */
  --hair: 1.5px solid var(--ink); /* Dimension / Scale Token (mauricemoynihan-com) */
  --card: clamp(7rem,13.2vw,11.5rem); /* Dimension / Scale Token (mauricemoynihan-com) */
  --shelf-pad: clamp(1rem,3vh,2.4rem); /* Layout / Spatial Grid Token (mauricemoynihan-com) */
  --shelf: calc(var(--card) * 1.22 + var(--shelf-pad) + var(--nav-h) + 1.6rem + 1.8vw); /* Dimension / Scale Token (mauricemoynihan-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#EFEDE6` — grounded in `var(--bone)` in `:root`
- **Primary Typography Ink**: `#E6E3D9` — grounded in `var(--bone-deep)` in `:root`
- **Elevated Surface / Card Substrate**: `#161511` — grounded in `var(--ink)` in `:root`
- **Interactive Accent / Highlight**: `#4c4a43` — grounded in `var(--ink-soft)` in `:root`
- **Secondary / Muted Copy**: `#FFFFFF` — grounded in `var(--paper)` in `:root`
- **Structural Hairline Border**: `#ff0000` — grounded in `::selection { background: red }` (`#ff0000`)

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `768px` extracted from `mauricemoynihan-com` stylesheet
- **Padding & Gutters**: `.7rem` lateral canvas padding with `1rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 768px`, `gap: 1rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `.7rem` horizontal padding
- **Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (max-height:800px) and (min-width:769px)`, `@media (min-width:769px)`, `@media (max-width:768px)`
- **Corner Radii**: `1px`, `2px`, `50%`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Archivo`
- **Body Font Stack**: `Space Mono`
- **Monospace / Technical Font Stack**: `Space Mono`
- **H1 Display Rule**: rule `h1` (`font-size: clamp(1.9rem,5.2vw,4.4rem)`, `line-height: 1.02`, `letter-spacing: -.02em`, `font-weight: 900`)
- **H2 Section Rule**: rule `h2` (`font-size: clamp(2rem,7vw,5.2rem)`, `line-height: .92`, `letter-spacing: -.02em`, `font-weight: 900`)
- **Body Copy Rule**: rule `body` (`font-size: 1.0625rem`, `line-height: 1.55`)
- **Metadata & Index Rule**: CSS variables `--mono: "Space Mono","Courier New",monospace`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `mauricemoynihan-com` (`Maurice Moynihan`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.nav> — `mauricemoynihan-com`)**:
   - DOM & Selectors: Landmark `<header class="nav nav--home">` hosting `Maurice Moynihan` navigation (`Advertising · adnauseum.ai · Music · About`), DOM attributes (`data-src="assets/koi/koi_a.webp"`, `data-src2="assets/koi/koi_b.webp"`, `data-panel`, `data-ink-top="0.7539"`), and stylesheet rule `html { scroll-behavior:smooth; }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.nav> — `mauricemoynihan-com`)` (`mauricemoynihan-com`) adapts across `@media (prefers-reduced-motion:reduce)`, `@media (max-height:800px) and (min-width:769px)`, `@media (min-width:769px)`, `@media (max-width:768px)` with `cubic-bezier(.35,.05,.4,1)`, `cubic-bezier(.45,0,.25,1)`, `cubic-bezier(.2,.8,.3,1)` transitions and links `Advertising · adnauseum.ai · Music · About`.
2. **Hero Stage & Focal Lead (<section.hero> — `Maurice Moynihan`)**:
   - DOM & Selectors: Landmark `<section class="hero">` presenting display lead `Maurice Moynihan` and copy excerpt *"Skip to the content"* over `#EFEDE6` canvas and `#161511` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#EFEDE6` background with `#161511` headline `Maurice Moynihan`.
3. **Primary Showcase & Content Grid (<section.hero> — `Skip to the content`)**:
   - DOM & Selectors: Landmark `<section class="hero">` rendering section `Skip to the content` with copy *"is a Creative Director, Songwriter and Governor of the Central Ba"*, asset references (`apple-touch-icon.png`, `fonts.googleapis.com`, `fonts.gstatic.com`, `css2`), and grid rule `video { max-width:100%;display:block; }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.hero> — `Skip to the content`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 768px`, `gap: 1rem`) on desktop and Single-column vertical stack at `390px` viewport width with `.7rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.hero> — `is a Creative Director, Songwriter`)**:
   - DOM & Selectors: Landmark `<section class="hero">` framing `is a Creative Director, Songwriter and Governor ` and `Governor of the Central Bank of Ireland` (*"Governor of the Central Bank of Ireland"*) with `#161511` surface cards, `#4c4a43` accents, and `selection { background:var(--red);color:var(--bone); }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.hero> — `is a Creative Director, Songwriter`)` uses `1px`, `2px`, `50%` radii, `#4c4a43` highlights, and assets (apple-touch-icon.png, fonts.googleapis.com, fonts.gstatic.com).
5. **Colophon & Global Directory Footer (<footer.footer> — `https://mauricemoynihan.com`)**:
   - DOM & Selectors: Landmark `<footer class="footer">` anchoring `Maurice Moynihan` footer links (`Advertising · adnauseum.ai · Music · About`), copy *"01 Advertising Things that made people buy other things."*, and `#ff0000` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.footer> — `https://mauricemoynihan.com`)` aligns to `768px` extracted from `mauricemoynihan-com` stylesheet with `.7rem` lateral canvas padding with `1rem` grid gap and attributes (data-src="assets/koi/koi_a.webp", data-src2="assets/koi/koi_b.webp", data-panel).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Skip to the content"*
- Copy Excerpt 2: *"is a Creative Director, Songwriter and Governor of the Central Bank of Ireland ."*
- Copy Excerpt 3: *"Governor of the Central Bank of Ireland"*
- Copy Excerpt 4: *"01 Advertising Things that made people buy other things."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.35,.05,.4,1)`, `cubic-bezier(.45,0,.25,1)`, `cubic-bezier(.2,.8,.3,1)`
- **Extracted Stylesheet Rules (`mauricemoynihan-com`)**:
- `html { scroll-behavior:smooth; }`
- `video { max-width:100%;display:block; }`
- `selection { background:var(--red);color:var(--bone); }`
- `focus-visible { outline:3px solid var(--red);outline-offset:3px;border-radius:1px; }`
- `.skip:focus { top:.8rem; }`
- **Per-Selector Transition Rules**:
- **Selector `.skip`**: `transition: top .15s` extracted from `mauricemoynihan-com` stylesheet.
- **Selector `.nav--home`**: `transition: background .18s ease` extracted from `mauricemoynihan-com` stylesheet.
- **Selector `media (prefers-reduced-motion:red...`**: `transition: none` extracted from `mauricemoynihan-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.35,.05,.4,1)`)**: Governs interactive state transitions across `<header.nav>` and `<section.hero>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `mauricemoynihan-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
