---
title: "UI Prompt Blueprint: www-alpineguides-co-nz"
date: 2026-11-15
target: "[[overview|www-alpineguides-co-nz]]"
status: analyzed
archetype: "Light-Substrate Editorial & Modular Grid System (`#fcb124` canvas, `#1e1e1e` ink, `#dad9d9` accent)"
---

# UI Design System & Master Generation Blueprint: www-alpineguides-co-nz

> **Alpine Guides Aoraki · NZ Mountain Guiding Since 1966** (https://www.alpineguides.co.nz/) — Explore guided ascents, mountaineering courses, ski touring, Tasman Glacier heli-hike and alpine adventures in Aoraki/Mount Cook with pro...

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/www-alpineguides-co-nz/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Alpine Guides Aoraki · NZ Mountain Guiding Since 1966** (`https://www.alpineguides.co.nz/`). Explore guided ascents, mountaineering courses, ski touring, Tasman Glacier heli-hike and alpine adventures in Aoraki/Mount Cook with pro...
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#fcb124` canvas, `#1e1e1e` ink, `#dad9d9` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fcb124` (`var(--_theme---agl-gold)` in `:root`) paired with `#1e1e1e` primary typography and `#dad9d9` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Mozillaheadline Variablefont Wdth Wght` for display copy (`Expert Mountain Adventures Since 196`) with `Robotocondensed` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `940px` container bounds (`gap: 16px`, padding `9px`) with `cubic-bezier(.49,.78,.46,1.34)` easing and GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/www-alpineguides-co-nz/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `940px` extracted from `www-alpineguides-co-nz` stylesheet.
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
| **Primary Canvas Substrate** | `#fcb124` | `var(--_theme---agl-gold)` in `:root` |
| **Primary Typography Ink** | `#f2f2f3` | `var(--_theme---white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#1e1e1e` | `var(--_theme---carbon)` in `:root` |
| **Interactive Accent / Highlight** | `#dad9d9` | `var(--_theme---cloud)` in `:root` |
| **Secondary / Muted Copy** | `#888` | `var(--_theme---ash)` in `:root` |
| **Structural Hairline Border** | `#343435` | `var(--_theme---graphite)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--w-backdrop-animation` | `initial` | Motion / Easing Token |
| `--_text-syle---font-family` | `Robotocondensed, Arial, sans-serif` | Typography Ink Token |
| `--_theme---color--heading` | `var(--_theme---white)` | Typography Ink Token |
| `--_responsive---h1` | `7rem` | Typography / Scale Token |
| `--_text-syle---line-height` | `1.25` | Typography Ink Token |
| `--_text-syle---font-weight` | `200` | Typography Ink Token |
| `--_text-syle---letter-spacing` | `0rem` | Typography Ink Token |
| `--_responsive---h2` | `3rem` | Typography / Scale Token |
| `--_theme---color--eyebrow` | `var(--_theme---agl-gold)` | Brand / Palette Token |
| `--_text-syle---text-size` | `var(--_responsive---paragraph)` | Typography Ink Token |
| `--_theme---color--text` | `var(--_theme---white)` | Typography Ink Token |
| `--_responsive---paragraph` | `1.4rem` | Typography / Scale Token |
| `--_theme---agl-gold` | `#fcb124` | Brand / Palette Token |
| `--_theme---color--border` | `var(--_theme---ash)` | Brand / Palette Token |
| `--_theme---color--background` | `var(--_theme---black)` | Canvas / Surface Token |
| `--_theme---white` | `#f2f2f3` | Canvas / Surface Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Mozillaheadline Variablefont Wdth Wght`.
- **Primary Body Stack**: `Robotocondensed`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--_responsive---h1: 7rem`, `--_responsive---h1-line-height: .5rem`; rule `h1` (`font-size: 2em`).
- **Section Heading (`H2`)**: CSS variables `--_responsive---h2: 3rem`; rule `h2` (`font-size: 32px`, `line-height: 36px`).
- **Body Copy**: CSS variables `--_responsive---paragraph: 1.4rem`, `--_responsive---paragraph_small: 1rem`; rule `body` (`font-size: 14px`, `line-height: 20px`).
- **Metadata & Navigation Labels**: CSS variables `--_text-syle---letter-spacing: 0rem`, `--_responsive---spacer-small: .7rem`, `--_responsive---paragraph_small: 1rem`; rule `small` (`font-size: 80%`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.49,.78,.46,1.34)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,1,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.w-webflow-badge > img`**: `transition: unset` extracted from `www-alpineguides-co-nz` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s, color .1s` extracted from `www-alpineguides-co-nz` stylesheet.
- **Selector `.w-lightbox-control`**: `transition: all .3s` extracted from `www-alpineguides-co-nz` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.49,.78,.46,1.34)`)**: Governs interactive state transitions across `<header.w-mod-js>` and `<section.prepare-mega>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Alpine Guides Aoraki · NZ Mountain Guiding │
│ ====================================================================== │
│ [ <header.w-mod-js>        | prepare · contact us · alpine hiking · ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.explore-mega>                               |   │
│ | H1: Expert Mountain Adventures Since 1966                        |   │
│ | Substrate: #fcb124    | Ink: #1e1e1e    | Accent: #dad9d9        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.prepare-mega>    ) max-w: 940px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | From glaciers to legendary a |  | Trips Worth Checking Out     | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 16px  ) | │
│ | [<header.w-mod-js>] -> [<section.explore-m] -> [<section.prepare-m]  │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer>       ) | https://www.alpineguides.co.nz/    │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.w-mod-js> — `www-alpineguides-co-nz`)**:
   - Landmark `<header class="w-mod-js">` hosting `Alpine Guides Aoraki · NZ Mountain G` navigation (`prepare · contact us · alpine hiking · learn the ropes · guided ascents`), DOM attributes (`data-wf-domain="www.alpineguides.co.nz"`, `data-wf-page="6948a91537f8a4167b84e785"`, `data-wf-site="6948a91537f8a4167b84e770"`, `data-page="home"`), and stylesheet rule `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`.
2. **Hero Stage & Focal Lead (<section.explore-mega> — `Expert Mountain Adventures Since 1`)**:
   - Landmark `<section class="explore-mega">` presenting display lead `Expert Mountain Adventures Since 1966` and copy excerpt *"Explore With The Experts"* over `#fcb124` canvas and `#1e1e1e` ink.
3. **Primary Showcase & Content Grid (<section.prepare-mega> — `From glaciers to legendary ascents`)**:
   - Landmark `<section class="prepare-mega">` rendering section `From glaciers to legendary ascents, our NZMGA/IFM...` with copy *"tasman glacier adventures"*, asset references (`cdn.prod.website-files.com`, `alpine-guides.webflow.shared.ac09...`, `www-widgetapi.js`, `recaptcha__en.js`), and grid rule `body { margin: 0; }`.
4. **Interactive Detail & Feature Matrix (<section.c-hero> — `Trips Worth Checking Out`)**:
   - Landmark `<section class="c-hero">` framing `Trips Worth Checking Out` and `Where We Guide` (*"private guiding · bespoke trips"*) with `#1e1e1e` surface cards, `#dad9d9` accents, and `summary { display: block; }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://www.alpineguides.co.nz/`)**:
   - Landmark `<footer class="footer">` anchoring `Alpine Guides Aoraki · NZ Mounta` footer links (`prepare · contact us · alpine hiking · learn the ropes · guided ascents`), copy *"ski the southern alps"*, and `#343435` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-alpineguides-co-nz (Alpine Guides Aoraki · NZ Mountain Guiding Since 1966)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-alpineguides-co-nz` (**Alpine Guides Aoraki · NZ Mountain Guiding Since 1966** — `https://www.alpineguides.co.nz/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#fcb124` canvas, `#1e1e1e` ink, `#dad9d9` accent).
- **Identity & Domain Context**: Explore guided ascents, mountaineering courses, ski touring, Tasman Glacier heli-hike and alpine adventures in Aoraki/Mount Cook with pro...
- **Primary Substrate**: `#fcb124` (`var(--_theme---agl-gold)` in `:root`), **Primary Ink**: `#1e1e1e`, **Accent / Highlight**: `#dad9d9`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fcb124` (`var(--_theme---agl-gold)` in `:root`) paired with `#1e1e1e` primary typography and `#dad9d9` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Mozillaheadline Variablefont Wdth Wght` for display copy (`Expert Mountain Adventures Since 196`) with `Robotocondensed` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `940px` container bounds (`gap: 16px`, padding `9px`) with `cubic-bezier(.49,.78,.46,1.34)` easing and GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-alpineguides-co-nz` in your global stylesheet:

:root {
  /* Alpine Guides Aoraki · NZ Mountain Guiding Since 1966 (www-alpineguides-co-nz) — Ground-Truth Extracted CSS Variables */
  --w-backdrop-animation: initial; /* Motion / Easing Token (www-alpineguides-co-nz) */
  --_text-syle---font-family: Robotocondensed, Arial, sans-serif; /* Typography Ink Token (www-alpineguides-co-nz) */
  --_theme---color--heading: var(--_theme---white); /* Typography Ink Token (www-alpineguides-co-nz) */
  --_responsive---h1: 7rem; /* Typography / Scale Token (www-alpineguides-co-nz) */
  --_text-syle---line-height: 1.25; /* Typography Ink Token (www-alpineguides-co-nz) */
  --_text-syle---font-weight: 200; /* Typography Ink Token (www-alpineguides-co-nz) */
  --_text-syle---letter-spacing: 0rem; /* Typography Ink Token (www-alpineguides-co-nz) */
  --_responsive---h2: 3rem; /* Typography / Scale Token (www-alpineguides-co-nz) */
  --_theme---color--eyebrow: var(--_theme---agl-gold); /* Brand / Palette Token (www-alpineguides-co-nz) */
  --_text-syle---text-size: var(--_responsive---paragraph); /* Typography Ink Token (www-alpineguides-co-nz) */
  --_theme---color--text: var(--_theme---white); /* Typography Ink Token (www-alpineguides-co-nz) */
  --_responsive---paragraph: 1.4rem; /* Typography / Scale Token (www-alpineguides-co-nz) */
  --_theme---agl-gold: #fcb124; /* Brand / Palette Token (www-alpineguides-co-nz) */
  --_theme---color--border: var(--_theme---ash); /* Brand / Palette Token (www-alpineguides-co-nz) */
  --_theme---color--background: var(--_theme---black); /* Canvas / Surface Token (www-alpineguides-co-nz) */
  --_theme---white: #f2f2f3; /* Canvas / Surface Token (www-alpineguides-co-nz) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#fcb124` — grounded in `var(--_theme---agl-gold)` in `:root`
- **Primary Typography Ink**: `#f2f2f3` — grounded in `var(--_theme---white)` in `:root`
- **Elevated Surface / Card Substrate**: `#1e1e1e` — grounded in `var(--_theme---carbon)` in `:root`
- **Interactive Accent / Highlight**: `#dad9d9` — grounded in `var(--_theme---cloud)` in `:root`
- **Secondary / Muted Copy**: `#888` — grounded in `var(--_theme---ash)` in `:root`
- **Structural Hairline Border**: `#343435` — grounded in `var(--_theme---graphite)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `940px` extracted from `www-alpineguides-co-nz` stylesheet
- **Padding & Gutters**: `9px` lateral canvas padding with `16px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 940px`, `gap: 16px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `9px` horizontal padding
- **Media Queries**: `@media screen and (max-width: 991px)`, `@media screen and (max-width: 767px)`, `@media screen and (max-width: 479px)`, `@media (min-width: 768px)`
- **Corner Radii**: `3px`, `100%`, `50%`, `2px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Mozillaheadline Variablefont Wdth Wght`
- **Body Font Stack**: `Robotocondensed`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: CSS variables `--_responsive---h1: 7rem`, `--_responsive---h1-line-height: .5rem`; rule `h1` (`font-size: 2em`)
- **H2 Section Rule**: CSS variables `--_responsive---h2: 3rem`; rule `h2` (`font-size: 32px`, `line-height: 36px`)
- **Body Copy Rule**: CSS variables `--_responsive---paragraph: 1.4rem`, `--_responsive---paragraph_small: 1rem`; rule `body` (`font-size: 14px`, `line-height: 20px`)
- **Metadata & Index Rule**: CSS variables `--_text-syle---letter-spacing: 0rem`, `--_responsive---spacer-small: .7rem`, `--_responsive---paragraph_small: 1rem`; rule `small` (`font-size: 80%`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-alpineguides-co-nz` (`Alpine Guides Aoraki · NZ Mountain Guiding Since 1966`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.w-mod-js> — `www-alpineguides-co-nz`)**:
   - DOM & Selectors: Landmark `<header class="w-mod-js">` hosting `Alpine Guides Aoraki · NZ Mountain G` navigation (`prepare · contact us · alpine hiking · learn the ropes · guided ascents`), DOM attributes (`data-wf-domain="www.alpineguides.co.nz"`, `data-wf-page="6948a91537f8a4167b84e785"`, `data-wf-site="6948a91537f8a4167b84e770"`, `data-page="home"`), and stylesheet rule `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.w-mod-js> — `www-alpineguides-co-nz`)` (`www-alpineguides-co-nz`) adapts across `@media screen and (max-width: 991px)`, `@media screen and (max-width: 767px)`, `@media screen and (max-width: 479px)`, `@media (min-width: 768px)` with `cubic-bezier(.49,.78,.46,1.34)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,1,1)` transitions and links `prepare · contact us · alpine hiking · learn the ropes · guided ascents`.
2. **Hero Stage & Focal Lead (<section.explore-mega> — `Expert Mountain Adventures Since 1`)**:
   - DOM & Selectors: Landmark `<section class="explore-mega">` presenting display lead `Expert Mountain Adventures Since 1966` and copy excerpt *"Explore With The Experts"* over `#fcb124` canvas and `#1e1e1e` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#fcb124` background with `#1e1e1e` headline `Expert Mountain Adventures Since 1966`.
3. **Primary Showcase & Content Grid (<section.prepare-mega> — `From glaciers to legendary ascents`)**:
   - DOM & Selectors: Landmark `<section class="prepare-mega">` rendering section `From glaciers to legendary ascents, our NZMGA/IFM...` with copy *"tasman glacier adventures"*, asset references (`cdn.prod.website-files.com`, `alpine-guides.webflow.shared.ac09...`, `www-widgetapi.js`, `recaptcha__en.js`), and grid rule `body { margin: 0; }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.prepare-mega> — `From glaciers to legendary ascents`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 940px`, `gap: 16px`) on desktop and Single-column vertical stack at `390px` viewport width with `9px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.c-hero> — `Trips Worth Checking Out`)**:
   - DOM & Selectors: Landmark `<section class="c-hero">` framing `Trips Worth Checking Out` and `Where We Guide` (*"private guiding · bespoke trips"*) with `#1e1e1e` surface cards, `#dad9d9` accents, and `summary { display: block; }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.c-hero> — `Trips Worth Checking Out`)` uses `3px`, `100%`, `50%`, `2px` radii, `#dad9d9` highlights, and assets (cdn.prod.website-files.com, alpine-guides.webflow.shared.ac09..., www-widgetapi.js).
5. **Colophon & Global Directory Footer (<footer.footer> — `https://www.alpineguides.co.nz/`)**:
   - DOM & Selectors: Landmark `<footer class="footer">` anchoring `Alpine Guides Aoraki · NZ Mounta` footer links (`prepare · contact us · alpine hiking · learn the ropes · guided ascents`), copy *"ski the southern alps"*, and `#343435` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.footer> — `https://www.alpineguides.co.nz/`)` aligns to `940px` extracted from `www-alpineguides-co-nz` stylesheet with `9px` lateral canvas padding with `16px` grid gap and attributes (data-wf-domain="www.alpineguides.co.nz", data-wf-page="6948a91537f8a4167b84e785", data-wf-site="6948a91537f8a4167b84e770").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Explore With The Experts"*
- Copy Excerpt 2: *"tasman glacier adventures"*
- Copy Excerpt 3: *"private guiding · bespoke trips"*
- Copy Excerpt 4: *"ski the southern alps"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.49,.78,.46,1.34)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,1,1)`
- **Extracted Stylesheet Rules (`www-alpineguides-co-nz`)**:
- `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`
- `body { margin: 0; }`
- `summary { display: block; }`
- `video { vertical-align: baseline; display: inline-block; }`
- `template { display: none; }`
- **Per-Selector Transition Rules**:
- **Selector `.w-webflow-badge > img`**: `transition: unset` extracted from `www-alpineguides-co-nz` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s, color .1s` extracted from `www-alpineguides-co-nz` stylesheet.
- **Selector `.w-lightbox-control`**: `transition: all .3s` extracted from `www-alpineguides-co-nz` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.49,.78,.46,1.34)`)**: Governs interactive state transitions across `<header.w-mod-js>` and `<section.prepare-mega>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-alpineguides-co-nz`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
