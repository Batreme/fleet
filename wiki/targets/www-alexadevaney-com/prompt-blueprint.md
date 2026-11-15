---
title: "UI Prompt Blueprint: www-alexadevaney-com"
date: 2026-11-15
target: "[[overview|www-alexadevaney-com]]"
status: analyzed
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#004F71` canvas, `#FFFFFF` ink, `#FFFFFF` accent)"
---

# UI Design System & Master Generation Blueprint: www-alexadevaney-com

> **North County San Diego Luxury Homes – Alexa Devaney** (https://www.alexadevaney.com/) — Alexa Devaney, Senior Realtor Associate with The Oppenheim Group, helps families buy and sell luxury homes from Encinitas and Carlsbad to...

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/www-alexadevaney-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **North County San Diego Luxury Homes – Alexa Devaney** (`https://www.alexadevaney.com/`). Alexa Devaney, Senior Realtor Associate with The Oppenheim Group, helps families buy and sell luxury homes from Encinitas and Carlsbad to...
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#004F71` canvas, `#FFFFFF` ink, `#FFFFFF` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#004F71` (`var(--navy)` in `:root`) paired with `#FFFFFF` primary typography and `#FFFFFF` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Montserrat` for display copy (`A Family-First Realtor for North Cou`) with `Montserrat` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1370px` container bounds (`gap: 18px`, padding `18px`) with `cubic-bezier(.4,0,.2,1)` easing.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/www-alexadevaney-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `1370px` extracted from `www-alexadevaney-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `18px` lateral canvas padding with `18px` grid gap.
- **Border Radius Scale**: `50%`, `999px`, `2px`, `4px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1370px`, `gap: 18px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `18px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width:600px)`, `@media (prefers-reduced-motion:reduce)`, `@media (max-width:1240px)`, `@media (max-width:992px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#004F71` | `var(--navy)` in `:root` |
| **Primary Typography Ink** | `#88786A` | `var(--taupe)` in `:root` |
| **Elevated Surface / Card Substrate** | `#FBF9F7` | `var(--cream)` in `:root` |
| **Interactive Accent / Highlight** | `#FFFFFF` | `var(--white)` in `:root` |
| **Secondary / Muted Copy** | `#7fb0c4` | `var(--cat)` in `:root` |
| **Structural Hairline Border** | `#2a0409` | `.intro { background: #2a0409 }` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--navy` | `#004F71` | Layout / Spatial Grid Token |
| `--navy-90` | `rgba(0,79,113,0.9)` | Layout / Spatial Grid Token |
| `--taupe` | `#88786A` | Color / Atmospheric Token |
| `--taupe-overlay` | `rgba(136,120,106,0.4)` | Color / Atmospheric Token |
| `--cream` | `#FBF9F7` | Color / Atmospheric Token |
| `--white` | `#FFFFFF` | Canvas / Surface Token |
| `--heading-font` | `"Montserrat",sans-serif` | Typography Ink Token |
| `--display-font` | `"Montserrat",sans-serif` | Typography / Scale Token |
| `--body-font` | `"Montserrat",sans-serif` | Typography / Scale Token |
| `--rail-gutter` | `max(25px,calc((100% - 1370px) / 2 + 25px))` | Layout / Spatial Grid Token |
| `--cat` | `#7fb0c4` | Color / Atmospheric Token |
| `--ag-top` | `96px` | Dimension / Scale Token |
| `--ag-h` | `min(calc(100vh - var(--ag-top) - 24px),780px)` | Dimension / Scale Token |
| `--decal` | `url(/brand/og-ring-decal.webp)` | Design System Custom Token |
| `--mix` | `0` | Design System Custom Token |
| `--hs-menu-max` | `340px` | Dimension / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Montserrat`.
- **Primary Body Stack**: `Montserrat`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--display-font: "Montserrat",sans-serif`; rule `h1` (`font-size: clamp(38px,5.4vw,72px)`, `line-height: 1.02`, `letter-spacing: -1.4px`, `font-weight: 300`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: 30px`, `letter-spacing: 1px`, `font-weight: 400`).
- **Body Copy**: CSS variables `--body-font: "Montserrat",sans-serif`; rule `p` (`font-size: 16px`, `line-height: 1.7`, `letter-spacing: 1px`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(22px,4.2vw,40px)`, `clamp(38px,4.5vw,62px)`, `clamp(30px,3vw,42px)`, `12px`, `14px`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.77,0,.175,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `html[data-intro=play] .intro`**: `transition: opacity .6s cubic-bezier(.4,0,.2,1)` extracted from `www-alexadevaney-com` stylesheet.
- **Selector `html[data-intro=leaving] .intro__orb`**: `transition: scale .6s ease-in` extracted from `www-alexadevaney-com` stylesheet.
- **Selector `html[data-intro=leaving] .intro__...`**: `transition: translate .6s ease-in` extracted from `www-alexadevaney-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<nav.navbar>` and `<section.hn-statement>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<section.video-section>` and `<section.hn-statement>` interactive targets.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — North County San Diego Luxury Homes – Alex │
│ ====================================================================== │
│ [ <nav.navbar>             | Buy · Sell · Old Encinitas · Leucadia  ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.video-section>                              |   │
│ | H1: A Family-First Realtor for North County                      |   │
│ | Substrate: #004F71    | Ink: #FFFFFF    | Accent: #FFFFFF        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.hn-statement>    ) max-w: 1370px         |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | For more than ten years I ha |  | Featured Properties          | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 18px  ) | │
│ | [<nav.navbar>] -> [<section.video-sec] -> [<section.hn-statem] |     │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.intro__emblem>) | https://www.alexadevaney.com/      │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.navbar> — `www-alexadevaney-com`)**:
   - Landmark `<nav class="navbar">` hosting `North County San Diego Luxury Homes ` navigation (`Buy · Sell · Old Encinitas · Leucadia · Cardiff-by-the-Sea`), DOM attributes (`data-intro="done"`, `data-precedence="next"`, `data-precedence="next"`, `data-nimg="fill"`), and stylesheet rule `.intro { display:none }`.
2. **Hero Stage & Focal Lead (<section.video-section> — `A Family-First Realtor for North C`)**:
   - Landmark `<section class="video-section hn-hero">` presenting display lead `A Family-First Realtor for North County` and copy excerpt *"Communities North County San Diego View all communities → Encinit"* over `#004F71` canvas and `#FFFFFF` ink.
3. **Primary Showcase & Content Grid (<section.hn-statement> — `For more than ten years I have sol`)**:
   - Landmark `<section class="hn-statement">` rendering section `For more than ten years I have sold homes across...` with copy *"North County San Diego"*, asset references (`og-emblem.webp`, `og-wordmark-light.webp`, `og-wordmark-dark.webp`, `og-ring-decal.webp`), and grid rule `.intro__orb { scale:1.12;transition:scale .6s ease-in }`.
4. **Interactive Detail & Feature Matrix (<section.hn-stats> — `Featured Properties`)**:
   - Landmark `<section class="hn-stats">` framing `Featured Properties` and `Encinitas` (*"View all communities →"*) with `#FBF9F7` surface cards, `#FFFFFF` accents, and `.intro__content { position:relative;display:flex;flex-direction:column;align-items:center;... }`.
5. **Colophon & Global Directory Footer (<footer.intro__emblem> — `https://www.alexadevaney.com/`)**:
   - Landmark `<footer class="intro__emblem">` anchoring `North County San Diego Luxury Ho` footer links (`Buy · Sell · Old Encinitas · Leucadia · Cardiff-by-the-Sea`), copy *"Encinitas → Surf breaks, bluff-top streets, and a laid-back "*, and `#2a0409` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-alexadevaney-com (North County San Diego Luxury Homes – Alexa Devaney)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-alexadevaney-com` (**North County San Diego Luxury Homes – Alexa Devaney** — `https://www.alexadevaney.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#004F71` canvas, `#FFFFFF` ink, `#FFFFFF` accent).
- **Identity & Domain Context**: Alexa Devaney, Senior Realtor Associate with The Oppenheim Group, helps families buy and sell luxury homes from Encinitas and Carlsbad to...
- **Primary Substrate**: `#004F71` (`var(--navy)` in `:root`), **Primary Ink**: `#FFFFFF`, **Accent / Highlight**: `#FFFFFF`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#004F71` (`var(--navy)` in `:root`) paired with `#FFFFFF` primary typography and `#FFFFFF` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Montserrat` for display copy (`A Family-First Realtor for North Cou`) with `Montserrat` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1370px` container bounds (`gap: 18px`, padding `18px`) with `cubic-bezier(.4,0,.2,1)` easing.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-alexadevaney-com` in your global stylesheet:

:root {
  /* North County San Diego Luxury Homes – Alexa Devaney (www-alexadevaney-com) — Ground-Truth Extracted CSS Variables */
  --navy: #004F71; /* Layout / Spatial Grid Token (www-alexadevaney-com) */
  --navy-90: rgba(0,79,113,0.9); /* Layout / Spatial Grid Token (www-alexadevaney-com) */
  --taupe: #88786A; /* Color / Atmospheric Token (www-alexadevaney-com) */
  --taupe-overlay: rgba(136,120,106,0.4); /* Color / Atmospheric Token (www-alexadevaney-com) */
  --cream: #FBF9F7; /* Color / Atmospheric Token (www-alexadevaney-com) */
  --white: #FFFFFF; /* Canvas / Surface Token (www-alexadevaney-com) */
  --heading-font: "Montserrat",sans-serif; /* Typography Ink Token (www-alexadevaney-com) */
  --display-font: "Montserrat",sans-serif; /* Typography / Scale Token (www-alexadevaney-com) */
  --body-font: "Montserrat",sans-serif; /* Typography / Scale Token (www-alexadevaney-com) */
  --rail-gutter: max(25px,calc((100% - 1370px) / 2 + 25px)); /* Layout / Spatial Grid Token (www-alexadevaney-com) */
  --cat: #7fb0c4; /* Color / Atmospheric Token (www-alexadevaney-com) */
  --ag-top: 96px; /* Dimension / Scale Token (www-alexadevaney-com) */
  --ag-h: min(calc(100vh - var(--ag-top) - 24px),780px); /* Dimension / Scale Token (www-alexadevaney-com) */
  --decal: url(/brand/og-ring-decal.webp); /* Design System Custom Token (www-alexadevaney-com) */
  --mix: 0; /* Design System Custom Token (www-alexadevaney-com) */
  --hs-menu-max: 340px; /* Dimension / Scale Token (www-alexadevaney-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#004F71` — grounded in `var(--navy)` in `:root`
- **Primary Typography Ink**: `#88786A` — grounded in `var(--taupe)` in `:root`
- **Elevated Surface / Card Substrate**: `#FBF9F7` — grounded in `var(--cream)` in `:root`
- **Interactive Accent / Highlight**: `#FFFFFF` — grounded in `var(--white)` in `:root`
- **Secondary / Muted Copy**: `#7fb0c4` — grounded in `var(--cat)` in `:root`
- **Structural Hairline Border**: `#2a0409` — grounded in `.intro { background: #2a0409 }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1370px` extracted from `www-alexadevaney-com` stylesheet
- **Padding & Gutters**: `18px` lateral canvas padding with `18px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1370px`, `gap: 18px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `18px` horizontal padding
- **Media Queries**: `@media (max-width:600px)`, `@media (prefers-reduced-motion:reduce)`, `@media (max-width:1240px)`, `@media (max-width:992px)`
- **Corner Radii**: `50%`, `999px`, `2px`, `4px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Montserrat`
- **Body Font Stack**: `Montserrat`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: CSS variables `--display-font: "Montserrat",sans-serif`; rule `h1` (`font-size: clamp(38px,5.4vw,72px)`, `line-height: 1.02`, `letter-spacing: -1.4px`, `font-weight: 300`)
- **H2 Section Rule**: rule `h2` (`font-size: 30px`, `letter-spacing: 1px`, `font-weight: 400`)
- **Body Copy Rule**: CSS variables `--body-font: "Montserrat",sans-serif`; rule `p` (`font-size: 16px`, `line-height: 1.7`, `letter-spacing: 1px`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(22px,4.2vw,40px)`, `clamp(38px,4.5vw,62px)`, `clamp(30px,3vw,42px)`, `12px`, `14px`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-alexadevaney-com` (`North County San Diego Luxury Homes – Alexa Devaney`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.navbar> — `www-alexadevaney-com`)**:
   - DOM & Selectors: Landmark `<nav class="navbar">` hosting `North County San Diego Luxury Homes ` navigation (`Buy · Sell · Old Encinitas · Leucadia · Cardiff-by-the-Sea`), DOM attributes (`data-intro="done"`, `data-precedence="next"`, `data-precedence="next"`, `data-nimg="fill"`), and stylesheet rule `.intro { display:none }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.navbar> — `www-alexadevaney-com`)` (`www-alexadevaney-com`) adapts across `@media (max-width:600px)`, `@media (prefers-reduced-motion:reduce)`, `@media (max-width:1240px)`, `@media (max-width:992px)` with `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.77,0,.175,1)` transitions and links `Buy · Sell · Old Encinitas · Leucadia · Cardiff-by-the-Sea`.
2. **Hero Stage & Focal Lead (<section.video-section> — `A Family-First Realtor for North C`)**:
   - DOM & Selectors: Landmark `<section class="video-section hn-hero">` presenting display lead `A Family-First Realtor for North County` and copy excerpt *"Communities North County San Diego View all communities → Encinit"* over `#004F71` canvas and `#FFFFFF` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#004F71` background with `#FFFFFF` headline `A Family-First Realtor for North County`.
3. **Primary Showcase & Content Grid (<section.hn-statement> — `For more than ten years I have sol`)**:
   - DOM & Selectors: Landmark `<section class="hn-statement">` rendering section `For more than ten years I have sold homes across...` with copy *"North County San Diego"*, asset references (`og-emblem.webp`, `og-wordmark-light.webp`, `og-wordmark-dark.webp`, `og-ring-decal.webp`), and grid rule `.intro__orb { scale:1.12;transition:scale .6s ease-in }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.hn-statement> — `For more than ten years I have sol`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1370px`, `gap: 18px`) on desktop and Single-column vertical stack at `390px` viewport width with `18px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.hn-stats> — `Featured Properties`)**:
   - DOM & Selectors: Landmark `<section class="hn-stats">` framing `Featured Properties` and `Encinitas` (*"View all communities →"*) with `#FBF9F7` surface cards, `#FFFFFF` accents, and `.intro__content { position:relative;display:flex;flex-direction:column;align-items:center;... }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.hn-stats> — `Featured Properties`)` uses `50%`, `999px`, `2px`, `4px` radii, `#FFFFFF` highlights, and assets (og-emblem.webp, og-wordmark-light.webp, og-wordmark-dark.webp).
5. **Colophon & Global Directory Footer (<footer.intro__emblem> — `https://www.alexadevaney.com/`)**:
   - DOM & Selectors: Landmark `<footer class="intro__emblem">` anchoring `North County San Diego Luxury Ho` footer links (`Buy · Sell · Old Encinitas · Leucadia · Cardiff-by-the-Sea`), copy *"Encinitas → Surf breaks, bluff-top streets, and a laid-back "*, and `#2a0409` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.intro__emblem> — `https://www.alexadevaney.com/`)` aligns to `1370px` extracted from `www-alexadevaney-com` stylesheet with `18px` lateral canvas padding with `18px` grid gap and attributes (data-intro="done", data-precedence="next", data-precedence="next").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Communities North County San Diego View all communities → Encinitas → Surf breaks,..."*
- Copy Excerpt 2: *"North County San Diego"*
- Copy Excerpt 3: *"View all communities →"*
- Copy Excerpt 4: *"Encinitas → Surf breaks, bluff-top streets, and a laid-back coastal village from L..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.16,1,.3,1)`, `cubic-bezier(.77,0,.175,1)`
- **Extracted Stylesheet Rules (`www-alexadevaney-com`)**:
- `.intro { display:none }`
- `.intro__orb { scale:1.12;transition:scale .6s ease-in }`
- `.intro__content { position:relative;display:flex;flex-direction:column;align-items:center;... }`
- `.intro__wordmark { filter:brightness(0) invert(1) drop-shadow(0 1px 12px rgba(42,4,9,.35)) }`
- `.intro__emblem { width:72px;height:auto;animation:introRise 1s cubic-bezier(.4,0,.2,1) .... }`
- **Per-Selector Transition Rules**:
- **Selector `html[data-intro=play] .intro`**: `transition: opacity .6s cubic-bezier(.4,0,.2,1)` extracted from `www-alexadevaney-com` stylesheet.
- **Selector `html[data-intro=leaving] .intro__orb`**: `transition: scale .6s ease-in` extracted from `www-alexadevaney-com` stylesheet.
- **Selector `html[data-intro=leaving] .intro__...`**: `transition: translate .6s ease-in` extracted from `www-alexadevaney-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<nav.navbar>` and `<section.hn-statement>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<section.video-section>` and `<section.hn-statement>` interactive targets.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-alexadevaney-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
