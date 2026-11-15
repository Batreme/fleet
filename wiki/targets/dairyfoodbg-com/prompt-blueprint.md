---
title: "UI Prompt Blueprint: dairyfoodbg-com"
date: 2026-11-15
target: "[[overview|dairyfoodbg-com]]"
status: analyzed
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#2e7031` / `#ff4d4f`)"
---

# UI Design System & Master Generation Blueprint: dairyfoodbg-com

> **Dairy Food Bulgaria — Private-Label UHT Dairy Manufacturer** (https://dairyfoodbg.com/) — Private-label manufacturer of UHT milk, creams and protein drinks. Four aseptic filling lines, 28 export markets, co-development from rec...

![Desktop Viewport Capture (1440x22545)](file:///root/projects/fleet/wiki/targets/dairyfoodbg-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Dairy Food Bulgaria — Private-Label UHT Dairy Manufacturer** (`https://dairyfoodbg.com/`). Private-label manufacturer of UHT milk, creams and protein drinks. Four aseptic filling lines, 28 export markets, co-development from rec...
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#2e7031` / `#ff4d4f`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#2e7031` (`var(--_colors---brand--green-hover)` in `:root`) paired with `#fff` primary typography and `#ff4d4f` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Bricolagegrotesque` for display copy (`Elevate your brand`) with `Albertsans` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `90%` container bounds (`gap: var(--_space---md)`, padding `var(--_space---xl)`) with `cubic-bezier(.625,.05,0,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/dairyfoodbg-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×22545px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `90%` extracted from `dairyfoodbg-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `var(--_space---xl)` lateral canvas padding with `var(--_space---md)` grid gap.
- **Border Radius Scale**: `var(--_component---radius--xl)`, `var(--_component---radius--md)`, `var(--_component---radius--xs)`, `var(--_component---radius--full)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 90%`, `gap: var(--_space---md)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--_space---xl)` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen and (max-width:991px)`, `@media screen and (max-width:767px)`, `@media screen and (max-width:479px)`, `@media (min-width:768px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#2e7031` | `var(--_colors---brand--green-hover)` in `:root` |
| **Primary Typography Ink** | `#37863a` | `var(--_colors---brand--green)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fff` | `var(--_colors---neutral--white)` in `:root` |
| **Interactive Accent / Highlight** | `#ff4d4f` | `var(--_colors---status--error)` in `:root` |
| **Secondary / Muted Copy** | `#d7ecf6` | `var(--_colors---brand--sky)` in `:root` |
| **Structural Hairline Border** | `#151313` | `var(--_colors---neutral--900)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--_type---family--body` | `Albertsans,Verdana,sans-serif` | Typography / Scale Token |
| `--_colors---semantic--content-primary` | `var(--_colors---neutral--700)` | Brand / Palette Token |
| `--_type---scale--base` | `1em` | Typography / Scale Token |
| `--_type---weight--regular` | `400` | Typography / Scale Token |
| `--_padding---section--lg` | `7.5em` | Layout / Spatial Grid Token |
| `--_padding---container--page` | `1.25em` | Layout / Spatial Grid Token |
| `--_padding---section--md` | `5em` | Layout / Spatial Grid Token |
| `--_colors---semantic--bg` | `var(--_colors---brand--cloud)` | Canvas / Surface Token |
| `--_component---sizing--container-small` | `64em` | Layout / Spatial Grid Token |
| `--_space---2xl` | `3em` | Layout / Spatial Grid Token |
| `--_space---sm` | `.5em` | Layout / Spatial Grid Token |
| `--_colors---brand--green-hover` | `#2e7031` | Brand / Palette Token |
| `--_type---scale--xs` | `.75em` | Typography / Scale Token |
| `--_type---weight--semibold` | `600` | Typography / Scale Token |
| `--_type---tracking--eyebrow` | `.2em` | Typography / Scale Token |
| `--_type---family--display` | `Bricolagegrotesquesemicondensed,Verdana,sans-serif` | Typography / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Bricolagegrotesque`.
- **Primary Body Stack**: `Albertsans`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--_type---family--display: Bricolagegrotesquesemicondensed,Verdana,sans-serif`, `--_type---leading--display: 1`, `--_type---scale--display: 6em`.
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--_type---scale--base)`, `var(--_type---scale--5xl)`, `var(--_type---scale--xl)`, `var(--_type---scale--md)`, `var(--_type---scale--sm)`).
- **Body Copy**: CSS variables `--_type---family--body: Albertsans,Verdana,sans-serif`, `--_type---leading--body: 1.5`, `--_type---tracking--body: 0em`; rule `body` (`font-size: var(--size-font)`).
- **Metadata & Navigation Labels**: CSS variables `--_component---sizing--container-small: 64em`, `--_component---sizing--container-x-small: 48em`, `--cc-font-family-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.625,.05,0,1)`, `cubic-bezier(.34,1.3,.64,1)`, `cubic-bezier(.22,1,.36,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.w-webflow-badge>img`**: `transition: unset` extracted from `dairyfoodbg-com` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s,color .1s` extracted from `dairyfoodbg-com` stylesheet.
- **Selector `.w-lightbox-control`**: `transition: all .3s` extracted from `dairyfoodbg-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.625,.05,0,1)`)**: Governs interactive state transitions across `<header.navbar>` and `<section.about>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Dairy Food Bulgaria — Private-Label UHT Da │
│ ====================================================================== │
│ [ <header.navbar>          | Home · About · Products · Packaging ·  ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hero>                                       |   │
│ | H1: Elevate your brand                                           |   │
│ | Substrate: #2e7031    | Ink: #fff       | Accent: #ff4d4f        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.about>           ) max-w: 90%            |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Traditional craftsmanship wi |  | Customizable Products        | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: var(--) | │
│ | [<header.navbar>] -> [<section.hero>] -> [<section.about>] |         │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.site-footer>  ) | https://dairyfoodbg.com/           │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.navbar> — `dairyfoodbg-com`)**:
   - Landmark `<header class="navbar">` hosting `Dairy Food Bulgaria — Private-Label ` navigation (`Home · About · Products · Packaging · Catalog`), DOM attributes (`data-wf-domain="dairyfoodbg.com"`, `data-wf-page="6a450776d63ee937af4d29d7"`, `data-wf-site="6a450773d63ee937af4d28ea"`, `data-cc="analytics"`), and stylesheet rule `.hero { background-color:var(--_colors---brand--sky);height:400svh;position:rela... }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Elevate your brand`)**:
   - Landmark `<section class="hero">` presenting display lead `Elevate your brand` and copy excerpt *"Dairy Food Bulgaria"* over `#2e7031` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.about> — `Traditional craftsmanship with mod`)**:
   - Landmark `<section class="about">` rendering section `Traditional craftsmanship with modern UHT technol...` with copy *"Leading producer of private-label UHT dairy in Bulgaria. Leading "*, asset references (`cdn.prod.website-files.com`, `dairy-food.shared.ce91a50f0.min.css`, `dairy-food.6a450776d63ee937af4d29...`, `6abf58390100a7826e7f0b59_favicon-...`), and grid rule `.hero__sticky { height:100svh;position:sticky;top:0;overflow:hidden }`.
4. **Interactive Detail & Feature Matrix (<section.home-products> — `Customizable Products`)**:
   - Landmark `<section class="home-products">` framing `Customizable Products` and `Flexible Packaging` (*"Leading producer of private-label UHT dairy in Bulgaria."*) with `#fff` surface cards, `#ff4d4f` accents, and `.hero__video { z-index:0;pointer-events:none;object-fit:cover;width:100%;height:100%;po... }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://dairyfoodbg.com/`)**:
   - Landmark `<footer class="site-footer">` anchoring `Dairy Food Bulgaria — Private-La` footer links (`Home · About · Products · Packaging · Catalog`), copy *"From product development and packaging to large-scale manufa"*, and `#151313` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: dairyfoodbg-com (Dairy Food Bulgaria — Private-Label UHT Dairy Manufacturer)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `dairyfoodbg-com` (**Dairy Food Bulgaria — Private-Label UHT Dairy Manufacturer** — `https://dairyfoodbg.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#2e7031` / `#ff4d4f`).
- **Identity & Domain Context**: Private-label manufacturer of UHT milk, creams and protein drinks. Four aseptic filling lines, 28 export markets, co-development from rec...
- **Primary Substrate**: `#2e7031` (`var(--_colors---brand--green-hover)` in `:root`), **Primary Ink**: `#fff`, **Accent / Highlight**: `#ff4d4f`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#2e7031` (`var(--_colors---brand--green-hover)` in `:root`) paired with `#fff` primary typography and `#ff4d4f` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Bricolagegrotesque` for display copy (`Elevate your brand`) with `Albertsans` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `90%` container bounds (`gap: var(--_space---md)`, padding `var(--_space---xl)`) with `cubic-bezier(.625,.05,0,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `dairyfoodbg-com` in your global stylesheet:

:root {
  /* Dairy Food Bulgaria — Private-Label UHT Dairy Manufacturer (dairyfoodbg-com) — Ground-Truth Extracted CSS Variables */
  --_type---family--body: Albertsans,Verdana,sans-serif; /* Typography / Scale Token (dairyfoodbg-com) */
  --_colors---semantic--content-primary: var(--_colors---neutral--700); /* Brand / Palette Token (dairyfoodbg-com) */
  --_type---scale--base: 1em; /* Typography / Scale Token (dairyfoodbg-com) */
  --_type---weight--regular: 400; /* Typography / Scale Token (dairyfoodbg-com) */
  --_padding---section--lg: 7.5em; /* Layout / Spatial Grid Token (dairyfoodbg-com) */
  --_padding---container--page: 1.25em; /* Layout / Spatial Grid Token (dairyfoodbg-com) */
  --_padding---section--md: 5em; /* Layout / Spatial Grid Token (dairyfoodbg-com) */
  --_colors---semantic--bg: var(--_colors---brand--cloud); /* Canvas / Surface Token (dairyfoodbg-com) */
  --_component---sizing--container-small: 64em; /* Layout / Spatial Grid Token (dairyfoodbg-com) */
  --_space---2xl: 3em; /* Layout / Spatial Grid Token (dairyfoodbg-com) */
  --_space---sm: .5em; /* Layout / Spatial Grid Token (dairyfoodbg-com) */
  --_colors---brand--green-hover: #2e7031; /* Brand / Palette Token (dairyfoodbg-com) */
  --_type---scale--xs: .75em; /* Typography / Scale Token (dairyfoodbg-com) */
  --_type---weight--semibold: 600; /* Typography / Scale Token (dairyfoodbg-com) */
  --_type---tracking--eyebrow: .2em; /* Typography / Scale Token (dairyfoodbg-com) */
  --_type---family--display: Bricolagegrotesquesemicondensed,Verdana,sans-serif; /* Typography / Scale Token (dairyfoodbg-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#2e7031` — grounded in `var(--_colors---brand--green-hover)` in `:root`
- **Primary Typography Ink**: `#37863a` — grounded in `var(--_colors---brand--green)` in `:root`
- **Elevated Surface / Card Substrate**: `#fff` — grounded in `var(--_colors---neutral--white)` in `:root`
- **Interactive Accent / Highlight**: `#ff4d4f` — grounded in `var(--_colors---status--error)` in `:root`
- **Secondary / Muted Copy**: `#d7ecf6` — grounded in `var(--_colors---brand--sky)` in `:root`
- **Structural Hairline Border**: `#151313` — grounded in `var(--_colors---neutral--900)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×22545px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `90%` extracted from `dairyfoodbg-com` stylesheet
- **Padding & Gutters**: `var(--_space---xl)` lateral canvas padding with `var(--_space---md)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 90%`, `gap: var(--_space---md)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--_space---xl)` horizontal padding
- **Media Queries**: `@media screen and (max-width:991px)`, `@media screen and (max-width:767px)`, `@media screen and (max-width:479px)`, `@media (min-width:768px)`
- **Corner Radii**: `var(--_component---radius--xl)`, `var(--_component---radius--md)`, `var(--_component---radius--xs)`, `var(--_component---radius--full)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Bricolagegrotesque`
- **Body Font Stack**: `Albertsans`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: CSS variables `--_type---family--display: Bricolagegrotesquesemicondensed,Verdana,sans-serif`, `--_type---leading--display: 1`, `--_type---scale--display: 6em`
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--_type---scale--base)`, `var(--_type---scale--5xl)`, `var(--_type---scale--xl)`, `var(--_type---scale--md)`, `var(--_type---scale--sm)`)
- **Body Copy Rule**: CSS variables `--_type---family--body: Albertsans,Verdana,sans-serif`, `--_type---leading--body: 1.5`, `--_type---tracking--body: 0em`; rule `body` (`font-size: var(--size-font)`)
- **Metadata & Index Rule**: CSS variables `--_component---sizing--container-small: 64em`, `--_component---sizing--container-x-small: 48em`, `--cc-font-family-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `dairyfoodbg-com` (`Dairy Food Bulgaria — Private-Label UHT Dairy Manufacturer`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.navbar> — `dairyfoodbg-com`)**:
   - DOM & Selectors: Landmark `<header class="navbar">` hosting `Dairy Food Bulgaria — Private-Label ` navigation (`Home · About · Products · Packaging · Catalog`), DOM attributes (`data-wf-domain="dairyfoodbg.com"`, `data-wf-page="6a450776d63ee937af4d29d7"`, `data-wf-site="6a450773d63ee937af4d28ea"`, `data-cc="analytics"`), and stylesheet rule `.hero { background-color:var(--_colors---brand--sky);height:400svh;position:rela... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.navbar> — `dairyfoodbg-com`)` (`dairyfoodbg-com`) adapts across `@media screen and (max-width:991px)`, `@media screen and (max-width:767px)`, `@media screen and (max-width:479px)`, `@media (min-width:768px)` with `cubic-bezier(.625,.05,0,1)`, `cubic-bezier(.34,1.3,.64,1)`, `cubic-bezier(.22,1,.36,1)` transitions and links `Home · About · Products · Packaging · Catalog`.
2. **Hero Stage & Focal Lead (<section.hero> — `Elevate your brand`)**:
   - DOM & Selectors: Landmark `<section class="hero">` presenting display lead `Elevate your brand` and copy excerpt *"Dairy Food Bulgaria"* over `#2e7031` canvas and `#fff` ink.
   - Responsive Contract: Hero stage (`1440×22545px` desktop / `390×2400px` mobile) sets `#2e7031` background with `#fff` headline `Elevate your brand`.
3. **Primary Showcase & Content Grid (<section.about> — `Traditional craftsmanship with mod`)**:
   - DOM & Selectors: Landmark `<section class="about">` rendering section `Traditional craftsmanship with modern UHT technol...` with copy *"Leading producer of private-label UHT dairy in Bulgaria. Leading "*, asset references (`cdn.prod.website-files.com`, `dairy-food.shared.ce91a50f0.min.css`, `dairy-food.6a450776d63ee937af4d29...`, `6abf58390100a7826e7f0b59_favicon-...`), and grid rule `.hero__sticky { height:100svh;position:sticky;top:0;overflow:hidden }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.about> — `Traditional craftsmanship with mod`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 90%`, `gap: var(--_space---md)`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--_space---xl)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.home-products> — `Customizable Products`)**:
   - DOM & Selectors: Landmark `<section class="home-products">` framing `Customizable Products` and `Flexible Packaging` (*"Leading producer of private-label UHT dairy in Bulgaria."*) with `#fff` surface cards, `#ff4d4f` accents, and `.hero__video { z-index:0;pointer-events:none;object-fit:cover;width:100%;height:100%;po... }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.home-products> — `Customizable Products`)` uses `var(--_component---radius--xl)`, `var(--_component---radius--md)`, `var(--_component---radius--xs)`, `var(--_component---radius--full)` radii, `#ff4d4f` highlights, and assets (cdn.prod.website-files.com, dairy-food.shared.ce91a50f0.min.css, dairy-food.6a450776d63ee937af4d29...).
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://dairyfoodbg.com/`)**:
   - DOM & Selectors: Landmark `<footer class="site-footer">` anchoring `Dairy Food Bulgaria — Private-La` footer links (`Home · About · Products · Packaging · Catalog`), copy *"From product development and packaging to large-scale manufa"*, and `#151313` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.site-footer> — `https://dairyfoodbg.com/`)` aligns to `90%` extracted from `dairyfoodbg-com` stylesheet with `var(--_space---xl)` lateral canvas padding with `var(--_space---md)` grid gap and attributes (data-wf-domain="dairyfoodbg.com", data-wf-page="6a450776d63ee937af4d29d7", data-wf-site="6a450773d63ee937af4d28ea").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Dairy Food Bulgaria"*
- Copy Excerpt 2: *"Leading producer of private-label UHT dairy in Bulgaria. Leading producer of priva..."*
- Copy Excerpt 3: *"Leading producer of private-label UHT dairy in Bulgaria."*
- Copy Excerpt 4: *"From product development and packaging to large-scale manufacturing and export, we..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.625,.05,0,1)`, `cubic-bezier(.34,1.3,.64,1)`, `cubic-bezier(.22,1,.36,1)`
- **Extracted Stylesheet Rules (`dairyfoodbg-com`)**:
- `.hero { background-color:var(--_colors---brand--sky);height:400svh;position:rela... }`
- `.hero__sticky { height:100svh;position:sticky;top:0;overflow:hidden }`
- `.hero__video { z-index:0;pointer-events:none;object-fit:cover;width:100%;height:100%;po... }`
- `.hero__canvas { z-index:2;pointer-events:none;width:100%;height:100%;display:block;posit... }`
- `.hero__stats { z-index:8;pointer-events:none;position:absolute;inset:0 }`
- **Per-Selector Transition Rules**:
- **Selector `.w-webflow-badge>img`**: `transition: unset` extracted from `dairyfoodbg-com` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s,color .1s` extracted from `dairyfoodbg-com` stylesheet.
- **Selector `.w-lightbox-control`**: `transition: all .3s` extracted from `dairyfoodbg-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.625,.05,0,1)`)**: Governs interactive state transitions across `<header.navbar>` and `<section.about>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `dairyfoodbg-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
