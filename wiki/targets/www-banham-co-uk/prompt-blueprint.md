---
title: "UI Prompt Blueprint: www-banham-co-uk"
date: 2026-11-15
target: "[[overview|www-banham-co-uk]]"
status: analyzed
archetype: "Light-Substrate Editorial & Modular Grid System (`#0000` canvas, `#000` ink, `#2b3239` accent)"
---

# UI Design System & Master Generation Blueprint: www-banham-co-uk

> **Banham · Experts in Security Services Since 1926** (https://www.banham.co.uk/) — Welcome to Banham, market-leaders in the security industry since 1926, and the perfect people to help secure your property

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/www-banham-co-uk/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Banham · Experts in Security Services Since 1926** (`https://www.banham.co.uk/`). Welcome to Banham, market-leaders in the security industry since 1926, and the perfect people to help secure your property
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#0000` canvas, `#000` ink, `#2b3239` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#0000` (`var(--btn-stroke)` in `:root`) paired with `#000` primary typography and `#2b3239` accents.
  - **Extracted Typographic Hierarchy**: Pairs `IvarText` for display copy (`Which Banham products are you intere`) with `IvarItalic` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `640px` container bounds (`gap: .375rem`, padding `2px`) with `cubic-bezier(.4,0,.2,1)` easing and Three.js / WebGL Canvas Pipeline, Barba.js Page Transition Router.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/www-banham-co-uk/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `640px` extracted from `www-banham-co-uk` stylesheet.
- **Canvas Lateral Padding & Spacing**: `2px` lateral canvas padding with `.375rem` grid gap.
- **Border Radius Scale**: `5px`, `3px`, `100%`, `.3125rem`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 640px`, `gap: .375rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `2px` horizontal padding.
- **Extracted CSS Media Queries**: `@media only screen and (-webkit-min-device-pixel-ratio:1.5),only...`, `@media (min-width:640px)`, `@media (min-width:768px)`, `@media (min-width:1024px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#0000` | `var(--btn-stroke)` in `:root` |
| **Primary Typography Ink** | `#333e48` | `var(--btn-bg)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fff` | `var(--btn-color)` in `:root` |
| **Interactive Accent / Highlight** | `#2b3239` | `var(--btn-hover-bg)` in `:root` |
| **Secondary / Muted Copy** | `#000` | `var(--line-after)` in `:root` |
| **Structural Hairline Border** | `#8392a7` | `var(--color-cornflower-100)` in `:root` |
| **Variable Token (`--color-amsb_graystarts`)** | `#cbd5e0` | `var(--color-amsb_graystarts)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--btn-stroke` | `#0000` | Elevation / Border Token |
| `--btn-bg` | `#333e48` | Canvas / Surface Token |
| `--btn-color` | `#fff` | Brand / Palette Token |
| `--btn-hover-bg` | `#2b3239` | Canvas / Surface Token |
| `--btn-active-bg` | `#2b3239` | Canvas / Surface Token |
| `--line-after` | `#000` | Color / Atmospheric Token |
| `--line-before` | `#0000` | Color / Atmospheric Token |
| `--width-am-latter` | `32px` | Layout / Spatial Grid Token |
| `--width-am-brand` | `120px` | Brand / Palette Token |
| `--width-am-popup-content` | `600px` | Layout / Spatial Grid Token |
| `--height-am-latter` | `32px` | Layout / Spatial Grid Token |
| `--height-am-popup-content` | `415px` | Layout / Spatial Grid Token |
| `--background-size-size20` | `20px` | Canvas / Surface Token |
| `--color-cornflower-100` | `#8392a7` | Brand / Palette Token |
| `--padding-full` | `100%` | Layout / Spatial Grid Token |
| `--color-amsb_graystarts` | `#cbd5e0` | Brand / Palette Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `IvarText`.
- **Primary Body Stack**: `IvarItalic`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--dfd-btn-display: inline-flex`, `--dfd-btn-group-display: flex`; rule `,h1` (`font-size: 2.25rem`, `line-height: 2.5rem`, `letter-spacing: .36px`).
- **Section Heading (`H2`)**: rule `,h2` (`font-size: 28px`, `line-height: 1.25`, `letter-spacing: .28px`).
- **Body Copy**: rule `p` (`font-size: .875rem`, `line-height: 1.25rem`).
- **Metadata & Navigation Labels**: rule `.label` (`font-size: 1rem`, `line-height: 1.5rem`, `font-weight: 600`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.8,0,1,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.catalog-product-view .product-ta...`**: `transition: cubic-bezier(.4,0,.2,1)` extracted from `www-banham-co-uk` stylesheet.
- **Selector `.catalog-product-view .what-new a`**: `transition: .3s` extracted from `www-banham-co-uk` stylesheet.
- **Selector `builder-banner-wrapper .pagebuild...`**: `transition: .5s` extracted from `www-banham-co-uk` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<header.page-header>` and `<section.storyblok-home>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Barba.js Page Transition Router, Framer Motion Layout Physics with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Banham · Experts in Security Services Sinc │
│ ====================================================================== │
│ [ <header.page-header>     | Book a Survey · Locks · All Locks · Do ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.message>                                    |   │
│ | H1: Which Banham products are you interested in?                 |   │
│ | Substrate: #0000      | Ink: #000       | Accent: #2b3239        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.storyblok-home>  ) max-w: 640px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | About Your Enquiry           |  | We’ll need a little informat | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: .375re) | │
│ | [<header.page-heade] -> [<section.message>] -> [<section.storyblok]  │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer-contain) | https://www.banham.co.uk/          │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.page-header> — `www-banham-co-uk`)**:
   - Landmark `<header class="page-header">` hosting `Banham · Experts in Security Service` navigation (`Book a Survey · Locks · All Locks · Door Locks · Emergency Locksmiths`), DOM attributes (`data-mm-order="40"`, `data-mm-order="50"`, `data-ueto="ueto_4f22d9b1ed"`, `data-uid="zfDhhC1778"`), and stylesheet rule `container.chosen-with-drop .chose... { clip:auto;-webkit-clip-path:none;clip-path:none }`.
2. **Hero Stage & Focal Lead (<section.message> — `Which Banham products are you inte`)**:
   - Landmark `<section class="message global">` presenting display lead `Which Banham products are you interested in?` and copy excerpt *"Prefer to call? Reach us on 020 7819 3730"* over `#0000` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.storyblok-home> — `About Your Enquiry`)**:
   - Landmark `<section class="storyblok-home">` rendering section `About Your Enquiry` with copy *"Which Banham products are you interested in?"*, asset references (`styles.min.css`, `chosen.min.css`, `trustpilot.min.css`, `Banham_Logo_FA-04.png`), and grid rule `.chosen-container a { cursor:pointer }`.
4. **Interactive Detail & Feature Matrix (<section.fixed> — `We’ll need a little information ab`)**:
   - Landmark `<section class="fixed w-full">` framing `We’ll need a little information about you` and `Search for the property you’d like surveyed` (*"About Your Enquiry"*) with `#fff` surface cards, `#2b3239` accents, and `en-container .search-choice .grou... { margin-right:4px;overflow:hidden;white-space:nowrap;text-overflow:ellips... }`.
5. **Colophon & Global Directory Footer (<footer.footer-container> — `https://www.banham.co.uk/`)**:
   - Landmark `<footer class="footer-container">` anchoring `Banham · Experts in Security Ser` footer links (`Book a Survey · Locks · All Locks · Door Locks · Emergency Locksmiths`), copy *"We’ll need a little information about you"*, and `#8392a7` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-banham-co-uk (Banham · Experts in Security Services Since 1926)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-banham-co-uk` (**Banham · Experts in Security Services Since 1926** — `https://www.banham.co.uk/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#0000` canvas, `#000` ink, `#2b3239` accent).
- **Identity & Domain Context**: Welcome to Banham, market-leaders in the security industry since 1926, and the perfect people to help secure your property
- **Primary Substrate**: `#0000` (`var(--btn-stroke)` in `:root`), **Primary Ink**: `#000`, **Accent / Highlight**: `#2b3239`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#0000` (`var(--btn-stroke)` in `:root`) paired with `#000` primary typography and `#2b3239` accents.
  - **Extracted Typographic Hierarchy**: Pairs `IvarText` for display copy (`Which Banham products are you intere`) with `IvarItalic` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `640px` container bounds (`gap: .375rem`, padding `2px`) with `cubic-bezier(.4,0,.2,1)` easing and Three.js / WebGL Canvas Pipeline, Barba.js Page Transition Router.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-banham-co-uk` in your global stylesheet:

:root {
  /* Banham · Experts in Security Services Since 1926 (www-banham-co-uk) — Ground-Truth Extracted CSS Variables */
  --btn-stroke: #0000; /* Elevation / Border Token (www-banham-co-uk) */
  --btn-bg: #333e48; /* Canvas / Surface Token (www-banham-co-uk) */
  --btn-color: #fff; /* Brand / Palette Token (www-banham-co-uk) */
  --btn-hover-bg: #2b3239; /* Canvas / Surface Token (www-banham-co-uk) */
  --btn-active-bg: #2b3239; /* Canvas / Surface Token (www-banham-co-uk) */
  --line-after: #000; /* Color / Atmospheric Token (www-banham-co-uk) */
  --line-before: #0000; /* Color / Atmospheric Token (www-banham-co-uk) */
  --width-am-latter: 32px; /* Layout / Spatial Grid Token (www-banham-co-uk) */
  --width-am-brand: 120px; /* Brand / Palette Token (www-banham-co-uk) */
  --width-am-popup-content: 600px; /* Layout / Spatial Grid Token (www-banham-co-uk) */
  --height-am-latter: 32px; /* Layout / Spatial Grid Token (www-banham-co-uk) */
  --height-am-popup-content: 415px; /* Layout / Spatial Grid Token (www-banham-co-uk) */
  --background-size-size20: 20px; /* Canvas / Surface Token (www-banham-co-uk) */
  --color-cornflower-100: #8392a7; /* Brand / Palette Token (www-banham-co-uk) */
  --padding-full: 100%; /* Layout / Spatial Grid Token (www-banham-co-uk) */
  --color-amsb_graystarts: #cbd5e0; /* Brand / Palette Token (www-banham-co-uk) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#0000` — grounded in `var(--btn-stroke)` in `:root`
- **Primary Typography Ink**: `#333e48` — grounded in `var(--btn-bg)` in `:root`
- **Elevated Surface / Card Substrate**: `#fff` — grounded in `var(--btn-color)` in `:root`
- **Interactive Accent / Highlight**: `#2b3239` — grounded in `var(--btn-hover-bg)` in `:root`
- **Secondary / Muted Copy**: `#000` — grounded in `var(--line-after)` in `:root`
- **Structural Hairline Border**: `#8392a7` — grounded in `var(--color-cornflower-100)` in `:root`
- **Variable Token (`--color-amsb_graystarts`)**: `#cbd5e0` — grounded in `var(--color-amsb_graystarts)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `640px` extracted from `www-banham-co-uk` stylesheet
- **Padding & Gutters**: `2px` lateral canvas padding with `.375rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 640px`, `gap: .375rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `2px` horizontal padding
- **Media Queries**: `@media only screen and (-webkit-min-device-pixel-ratio:1.5),only...`, `@media (min-width:640px)`, `@media (min-width:768px)`, `@media (min-width:1024px)`
- **Corner Radii**: `5px`, `3px`, `100%`, `.3125rem`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `IvarText`
- **Body Font Stack**: `IvarItalic`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: CSS variables `--dfd-btn-display: inline-flex`, `--dfd-btn-group-display: flex`; rule `,h1` (`font-size: 2.25rem`, `line-height: 2.5rem`, `letter-spacing: .36px`)
- **H2 Section Rule**: rule `,h2` (`font-size: 28px`, `line-height: 1.25`, `letter-spacing: .28px`)
- **Body Copy Rule**: rule `p` (`font-size: .875rem`, `line-height: 1.25rem`)
- **Metadata & Index Rule**: rule `.label` (`font-size: 1rem`, `line-height: 1.5rem`, `font-weight: 600`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-banham-co-uk` (`Banham · Experts in Security Services Since 1926`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.page-header> — `www-banham-co-uk`)**:
   - DOM & Selectors: Landmark `<header class="page-header">` hosting `Banham · Experts in Security Service` navigation (`Book a Survey · Locks · All Locks · Door Locks · Emergency Locksmiths`), DOM attributes (`data-mm-order="40"`, `data-mm-order="50"`, `data-ueto="ueto_4f22d9b1ed"`, `data-uid="zfDhhC1778"`), and stylesheet rule `container.chosen-with-drop .chose... { clip:auto;-webkit-clip-path:none;clip-path:none }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.page-header> — `www-banham-co-uk`)` (`www-banham-co-uk`) adapts across `@media only screen and (-webkit-min-device-pixel-ratio:1.5),only...`, `@media (min-width:640px)`, `@media (min-width:768px)`, `@media (min-width:1024px)` with `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.8,0,1,1)` transitions and links `Book a Survey · Locks · All Locks · Door Locks · Emergency Locksmiths`.
2. **Hero Stage & Focal Lead (<section.message> — `Which Banham products are you inte`)**:
   - DOM & Selectors: Landmark `<section class="message global">` presenting display lead `Which Banham products are you interested in?` and copy excerpt *"Prefer to call? Reach us on 020 7819 3730"* over `#0000` canvas and `#000` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#0000` background with `#000` headline `Which Banham products are you interested in?`.
3. **Primary Showcase & Content Grid (<section.storyblok-home> — `About Your Enquiry`)**:
   - DOM & Selectors: Landmark `<section class="storyblok-home">` rendering section `About Your Enquiry` with copy *"Which Banham products are you interested in?"*, asset references (`styles.min.css`, `chosen.min.css`, `trustpilot.min.css`, `Banham_Logo_FA-04.png`), and grid rule `.chosen-container a { cursor:pointer }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.storyblok-home> — `About Your Enquiry`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 640px`, `gap: .375rem`) on desktop and Single-column vertical stack at `390px` viewport width with `2px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.fixed> — `We’ll need a little information ab`)**:
   - DOM & Selectors: Landmark `<section class="fixed w-full">` framing `We’ll need a little information about you` and `Search for the property you’d like surveyed` (*"About Your Enquiry"*) with `#fff` surface cards, `#2b3239` accents, and `en-container .search-choice .grou... { margin-right:4px;overflow:hidden;white-space:nowrap;text-overflow:ellips... }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.fixed> — `We’ll need a little information ab`)` uses `5px`, `3px`, `100%`, `.3125rem` radii, `#2b3239` highlights, and assets (styles.min.css, chosen.min.css, trustpilot.min.css).
5. **Colophon & Global Directory Footer (<footer.footer-container> — `https://www.banham.co.uk/`)**:
   - DOM & Selectors: Landmark `<footer class="footer-container">` anchoring `Banham · Experts in Security Ser` footer links (`Book a Survey · Locks · All Locks · Door Locks · Emergency Locksmiths`), copy *"We’ll need a little information about you"*, and `#8392a7` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.footer-container> — `https://www.banham.co.uk/`)` aligns to `640px` extracted from `www-banham-co-uk` stylesheet with `2px` lateral canvas padding with `.375rem` grid gap and attributes (data-mm-order="40", data-mm-order="50", data-ueto="ueto_4f22d9b1ed").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Prefer to call? Reach us on 020 7819 3730"*
- Copy Excerpt 2: *"Which Banham products are you interested in?"*
- Copy Excerpt 3: *"About Your Enquiry"*
- Copy Excerpt 4: *"We’ll need a little information about you"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.8,0,1,1)`
- **Extracted Stylesheet Rules (`www-banham-co-uk`)**:
- `container.chosen-with-drop .chose... { clip:auto;-webkit-clip-path:none;clip-path:none }`
- `.chosen-container a { cursor:pointer }`
- `en-container .search-choice .grou... { margin-right:4px;overflow:hidden;white-space:nowrap;text-overflow:ellips... }`
- `tainer .search-choice .group-name... { content:":";padding-left:2px;vertical-align:top }`
- `chosen-container-single .chosen-d... { color:999 }`
- **Per-Selector Transition Rules**:
- **Selector `.catalog-product-view .product-ta...`**: `transition: cubic-bezier(.4,0,.2,1)` extracted from `www-banham-co-uk` stylesheet.
- **Selector `.catalog-product-view .what-new a`**: `transition: .3s` extracted from `www-banham-co-uk` stylesheet.
- **Selector `builder-banner-wrapper .pagebuild...`**: `transition: .5s` extracted from `www-banham-co-uk` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<header.page-header>` and `<section.storyblok-home>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Barba.js Page Transition Router, Framer Motion Layout Physics with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-banham-co-uk`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
