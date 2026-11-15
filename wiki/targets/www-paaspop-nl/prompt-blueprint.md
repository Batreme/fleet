---
title: "UI Prompt Blueprint: www-paaspop-nl"
date: 2026-11-15
target: "www-paaspop-nl"
status: analyzed
capture: dom
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#100026` / `#000c`)"
---

# UI Design System & Master Generation Blueprint: www-paaspop-nl

> **Paaspop 2027 · 26, 27 & 28 maart** (https://www.paaspop.nl/) — Op 26, 27 en 28 maart vieren we 50 jaar Paaspop. Verschillende generaties, verschillende smaken, dezelfde mentaliteit. Dat vieren we groo...

![Desktop Viewport Capture](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Paaspop 2027 · 26, 27 & 28 maart** (`https://www.paaspop.nl/`). Op 26, 27 en 28 maart vieren we 50 jaar Paaspop. Verschillende generaties, verschillende smaken, dezelfde mentaliteit. Dat vieren we groo...
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#100026` / `#000c`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#100026` (`var(--_colors---midnight--100)` in `:root`) paired with `#ffb82e` primary typography and `#000c` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Onest` for display copy (`Deze website maakt gebruik van cooki`) with `Recoleta` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `940px` container bounds (`gap: 16px`, padding `9px`) with `cubic-bezier(.625,.05,0,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `940px` extracted from `www-paaspop-nl` stylesheet.
- **Canvas Lateral Padding & Spacing**: `9px` lateral canvas padding with `16px` grid gap.
- **Border Radius Scale**: `3px`, `100%`, `50%`, `2px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 940px`, `gap: 16px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `9px` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen and (max-width:991px)`, `@media screen and (max-width:767px)`, `@media screen and (max-width:479px)`, `@media (min-width:768px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#100026` | `var(--_colors---midnight--100)` in `:root` |
| **Primary Typography Ink** | `#ffb82e` | `var(--_colors---amber--100)` in `:root` |
| **Elevated Surface / Card Substrate** | `#0003` | `var(--_colors---black--20)` in `:root` |
| **Interactive Accent / Highlight** | `#000c` | `var(--_colors---black--80)` in `:root` |
| **Secondary / Muted Copy** | `#fff3` | `var(--_colors---white--20)` in `:root` |
| **Structural Hairline Border** | `#7e10ff` | `var(--_colors---purple--100)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--w-backdrop-animation` | `initial` | Motion / Easing Token |
| `--_colors---midnight--100` | `#100026` | Brand / Palette Token |
| `--_typography---fonts--primary-font` | `Onest,sans-serif` | Brand / Palette Token |
| `--_colors---black--100` | `black` | Canvas / Surface Token |
| `--_typography---body-size--regular` | `1rem` | Layout / Spatial Grid Token |
| `--_typography---line-height--body` | `1.3` | Typography / Scale Token |
| `--_typography---fonts--heading-font` | `Recoleta,Arial,sans-serif` | Typography Ink Token |
| `--_typography---heading-size--xlarge` | `5rem` | Typography Ink Token |
| `--_typography---line-height--heading` | `1` | Typography Ink Token |
| `--_typography---heading-size--large` | `4.5rem` | Typography Ink Token |
| `--_typography---heading-size--medium` | `2.5rem` | Typography Ink Token |
| `--_typography---heading-size--small` | `1.5rem` | Typography Ink Token |
| `--_typography---heading-size--xsmall` | `1.25rem` | Typography Ink Token |
| `--_typography---button-size--regular` | `.875rem` | Layout / Spatial Grid Token |
| `--_typography---line-height--button` | `1.2` | Typography / Scale Token |
| `--_typography---body-size--large` | `1.5rem` | Layout / Spatial Grid Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Onest`.
- **Primary Body Stack**: `Recoleta`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--_typography---rich-text--h1: 6rem`; rule `h1` (`font-size: var(--_typography---rich-text...`, `line-height: var(--_typography---l...`).
- **Section Heading (`H2`)**: CSS variables `--_typography---rich-text--h2: 4rem`; rule `h2` (`font-size: var(--_typography---rich-text...`, `line-height: var(--_typography---l...`).
- **Body Copy**: CSS variables `--_typography---body-size--regular: 1rem`, `--_typography---line-height--body: 1.3`, `--_typography---body-size--large: 1.5rem`; rule `p` (`font-size: var(--_typography---body-size...`).
- **Metadata & Navigation Labels**: CSS variables `--_typography---heading-size--small: 1.5rem`, `--_typography---heading-size--xsmall: 1.25rem`, `--gap-spacing--small: 1rem`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.625,.05,0,1)`, `cubic-bezier(.5,0,.5,1)`, `cubic-bezier(0.16,1,0.3,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.w-webflow-badge>img`**: `transition: unset` extracted from `www-paaspop-nl` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s,color .1s` extracted from `www-paaspop-nl` stylesheet.
- **Selector `.w-lightbox-control`**: `transition: all .3s` extracted from `www-paaspop-nl` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.625,.05,0,1)`)**: Governs interactive state transitions across `<header.navbar_component>` and `<section.section_fifty-years>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Paaspop 2027 · 26, 27 & 28 maart           │
│ ====================================================================== │
│ [ <header.navbar_component | Home · Line-up · Tickets · Veelgesteld ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.section_hero>                               |   │
│ | H1: Deze website maakt gebruik van cookies                       |   │
│ | Substrate: #100026    | Ink: #ffb82e    | Accent: #000c          |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.section_fifty-yea) max-w: 940px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | The unexpected, the unbeliev |  | 50 years of the greatest sho | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 16px  ) | │
│ | [<header.navbar_com] -> [<section.section_h] -> [<section.section_f] │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer_compone) | https://www.paaspop.nl/            │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.navbar_component> — `www-paaspop-nl`)**:
   - Landmark `<header class="navbar_component">` hosting `Paaspop 2027 · 26, 27 & 28 maart` navigation (`Home · Line-up · Tickets · Veelgestelde vragen · Paradise City`), DOM attributes (`data-wf-domain="www.paaspop.nl"`, `data-wf-page="6ac63e14514945d47eafbb94"`, `data-wf-site="6ac63e14514945d47eafbb98"`, `data-page-load-state="done"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
2. **Hero Stage & Focal Lead (<section.section_hero> — `Deze website maakt gebruik van coo`)**:
   - Landmark `<section class="section_hero">` presenting display lead `Deze website maakt gebruik van cookies` and copy excerpt *"Noodzakelijk Noodzakelijke cookies helpen een website bruikbaarde"* over `#100026` canvas and `#ffb82e` ink.
3. **Primary Showcase & Content Grid (<section.section_fifty-years> — `The unexpected, the unbelievable, `)**:
   - Landmark `<section class="section_fifty-years">` rendering section `The unexpected, the unbelievable, & unforgettable` with copy *"Noodzakelijke cookies helpen een website bruikbaarder te maken, d"*, asset references (`cdn.prod.website-files.com`, `paaspop.webflow.shared.7aa3d0213....`, `fonts.googleapis.com`, `fonts.gstatic.com`), and grid rule `summary { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.section_line-up> — `50 years of the greatest show on e`)**:
   - Landmark `<section class="section_line-up">` framing `50 years of the greatest show on earth` and `the first 50 names` (*"Voorkeuren Voorkeurscookies zorgen ervoor dat een website informa"*) with `#0003` surface cards, `#000c` accents, and `video { vertical-align:baseline;display:inline-block }`.
5. **Colophon & Global Directory Footer (<footer.footer_component> — `https://www.paaspop.nl/`)**:
   - Landmark `<footer class="footer_component">` anchoring `Paaspop 2027 · 26, 27 & 28 maart` footer links (`Home · Line-up · Tickets · Veelgestelde vragen · Paradise City`), copy *"Voorkeurscookies zorgen ervoor dat een website informatie ka"*, and `#7e10ff` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-paaspop-nl (Paaspop 2027 · 26, 27 & 28 maart)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-paaspop-nl` (**Paaspop 2027 · 26, 27 & 28 maart** — `https://www.paaspop.nl/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#100026` / `#000c`).
- **Identity & Domain Context**: Op 26, 27 en 28 maart vieren we 50 jaar Paaspop. Verschillende generaties, verschillende smaken, dezelfde mentaliteit. Dat vieren we groo...
- **Primary Substrate**: `#100026` (`var(--_colors---midnight--100)` in `:root`), **Primary Ink**: `#ffb82e`, **Accent / Highlight**: `#000c`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#100026` (`var(--_colors---midnight--100)` in `:root`) paired with `#ffb82e` primary typography and `#000c` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Onest` for display copy (`Deze website maakt gebruik van cooki`) with `Recoleta` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `940px` container bounds (`gap: 16px`, padding `9px`) with `cubic-bezier(.625,.05,0,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-paaspop-nl` in your global stylesheet:

:root {
  /* Paaspop 2027 · 26, 27 & 28 maart (www-paaspop-nl) — Ground-Truth Extracted CSS Variables */
  --w-backdrop-animation: initial; /* Motion / Easing Token (www-paaspop-nl) */
  --_colors---midnight--100: #100026; /* Brand / Palette Token (www-paaspop-nl) */
  --_typography---fonts--primary-font: Onest,sans-serif; /* Brand / Palette Token (www-paaspop-nl) */
  --_colors---black--100: black; /* Canvas / Surface Token (www-paaspop-nl) */
  --_typography---body-size--regular: 1rem; /* Layout / Spatial Grid Token (www-paaspop-nl) */
  --_typography---line-height--body: 1.3; /* Typography / Scale Token (www-paaspop-nl) */
  --_typography---fonts--heading-font: Recoleta,Arial,sans-serif; /* Typography Ink Token (www-paaspop-nl) */
  --_typography---heading-size--xlarge: 5rem; /* Typography Ink Token (www-paaspop-nl) */
  --_typography---line-height--heading: 1; /* Typography Ink Token (www-paaspop-nl) */
  --_typography---heading-size--large: 4.5rem; /* Typography Ink Token (www-paaspop-nl) */
  --_typography---heading-size--medium: 2.5rem; /* Typography Ink Token (www-paaspop-nl) */
  --_typography---heading-size--small: 1.5rem; /* Typography Ink Token (www-paaspop-nl) */
  --_typography---heading-size--xsmall: 1.25rem; /* Typography Ink Token (www-paaspop-nl) */
  --_typography---button-size--regular: .875rem; /* Layout / Spatial Grid Token (www-paaspop-nl) */
  --_typography---line-height--button: 1.2; /* Typography / Scale Token (www-paaspop-nl) */
  --_typography---body-size--large: 1.5rem; /* Layout / Spatial Grid Token (www-paaspop-nl) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#100026` — grounded in `var(--_colors---midnight--100)` in `:root`
- **Primary Typography Ink**: `#ffb82e` — grounded in `var(--_colors---amber--100)` in `:root`
- **Elevated Surface / Card Substrate**: `#0003` — grounded in `var(--_colors---black--20)` in `:root`
- **Interactive Accent / Highlight**: `#000c` — grounded in `var(--_colors---black--80)` in `:root`
- **Secondary / Muted Copy**: `#fff3` — grounded in `var(--_colors---white--20)` in `:root`
- **Structural Hairline Border**: `#7e10ff` — grounded in `var(--_colors---purple--100)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `940px` extracted from `www-paaspop-nl` stylesheet
- **Padding & Gutters**: `9px` lateral canvas padding with `16px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 940px`, `gap: 16px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `9px` horizontal padding
- **Media Queries**: `@media screen and (max-width:991px)`, `@media screen and (max-width:767px)`, `@media screen and (max-width:479px)`, `@media (min-width:768px)`
- **Corner Radii**: `3px`, `100%`, `50%`, `2px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Onest`
- **Body Font Stack**: `Recoleta`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: CSS variables `--_typography---rich-text--h1: 6rem`; rule `h1` (`font-size: var(--_typography---rich-text...`, `line-height: var(--_typography---l...`)
- **H2 Section Rule**: CSS variables `--_typography---rich-text--h2: 4rem`; rule `h2` (`font-size: var(--_typography---rich-text...`, `line-height: var(--_typography---l...`)
- **Body Copy Rule**: CSS variables `--_typography---body-size--regular: 1rem`, `--_typography---line-height--body: 1.3`, `--_typography---body-size--large: 1.5rem`; rule `p` (`font-size: var(--_typography---body-size...`)
- **Metadata & Index Rule**: CSS variables `--_typography---heading-size--small: 1.5rem`, `--_typography---heading-size--xsmall: 1.25rem`, `--gap-spacing--small: 1rem`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-paaspop-nl` (`Paaspop 2027 · 26, 27 & 28 maart`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.navbar_component> — `www-paaspop-nl`)**:
   - DOM & Selectors: Landmark `<header class="navbar_component">` hosting `Paaspop 2027 · 26, 27 & 28 maart` navigation (`Home · Line-up · Tickets · Veelgestelde vragen · Paradise City`), DOM attributes (`data-wf-domain="www.paaspop.nl"`, `data-wf-page="6ac63e14514945d47eafbb94"`, `data-wf-site="6ac63e14514945d47eafbb98"`, `data-page-load-state="done"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.navbar_component> — `www-paaspop-nl`)` (`www-paaspop-nl`) adapts across `@media screen and (max-width:991px)`, `@media screen and (max-width:767px)`, `@media screen and (max-width:479px)`, `@media (min-width:768px)` with `cubic-bezier(.625,.05,0,1)`, `cubic-bezier(.5,0,.5,1)`, `cubic-bezier(0.16,1,0.3,1)` transitions and links `Home · Line-up · Tickets · Veelgestelde vragen · Paradise City`.
2. **Hero Stage & Focal Lead (<section.section_hero> — `Deze website maakt gebruik van coo`)**:
   - DOM & Selectors: Landmark `<section class="section_hero">` presenting display lead `Deze website maakt gebruik van cookies` and copy excerpt *"Noodzakelijk Noodzakelijke cookies helpen een website bruikbaarde"* over `#100026` canvas and `#ffb82e` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#100026` background with `#ffb82e` headline `Deze website maakt gebruik van cookies`.
3. **Primary Showcase & Content Grid (<section.section_fifty-years> — `The unexpected, the unbelievable, `)**:
   - DOM & Selectors: Landmark `<section class="section_fifty-years">` rendering section `The unexpected, the unbelievable, & unforgettable` with copy *"Noodzakelijke cookies helpen een website bruikbaarder te maken, d"*, asset references (`cdn.prod.website-files.com`, `paaspop.webflow.shared.7aa3d0213....`, `fonts.googleapis.com`, `fonts.gstatic.com`), and grid rule `summary { display:block }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.section_fifty-years> — `The unexpected, the unbelievable, `)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 940px`, `gap: 16px`) on desktop and Single-column vertical stack at `390px` viewport width with `9px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.section_line-up> — `50 years of the greatest show on e`)**:
   - DOM & Selectors: Landmark `<section class="section_line-up">` framing `50 years of the greatest show on earth` and `the first 50 names` (*"Voorkeuren Voorkeurscookies zorgen ervoor dat een website informa"*) with `#0003` surface cards, `#000c` accents, and `video { vertical-align:baseline;display:inline-block }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.section_line-up> — `50 years of the greatest show on e`)` uses `3px`, `100%`, `50%`, `2px` radii, `#000c` highlights, and assets (cdn.prod.website-files.com, paaspop.webflow.shared.7aa3d0213...., fonts.googleapis.com).
5. **Colophon & Global Directory Footer (<footer.footer_component> — `https://www.paaspop.nl/`)**:
   - DOM & Selectors: Landmark `<footer class="footer_component">` anchoring `Paaspop 2027 · 26, 27 & 28 maart` footer links (`Home · Line-up · Tickets · Veelgestelde vragen · Paradise City`), copy *"Voorkeurscookies zorgen ervoor dat een website informatie ka"*, and `#7e10ff` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.footer_component> — `https://www.paaspop.nl/`)` aligns to `940px` extracted from `www-paaspop-nl` stylesheet with `9px` lateral canvas padding with `16px` grid gap and attributes (data-wf-domain="www.paaspop.nl", data-wf-page="6ac63e14514945d47eafbb94", data-wf-site="6ac63e14514945d47eafbb98").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Noodzakelijk Noodzakelijke cookies helpen een website bruikbaarder te maken, door..."*
- Copy Excerpt 2: *"Noodzakelijke cookies helpen een website bruikbaarder te maken, door basisfuncties..."*
- Copy Excerpt 3: *"Voorkeuren Voorkeurscookies zorgen ervoor dat een website informatie kan onthouden..."*
- Copy Excerpt 4: *"Voorkeurscookies zorgen ervoor dat een website informatie kan onthouden die van in..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.625,.05,0,1)`, `cubic-bezier(.5,0,.5,1)`, `cubic-bezier(0.16,1,0.3,1)`
- **Extracted Stylesheet Rules (`www-paaspop-nl`)**:
- `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`
- `summary { display:block }`
- `video { vertical-align:baseline;display:inline-block }`
- `template { display:none }`
- `strong { font-weight:700 }`
- **Per-Selector Transition Rules**:
- **Selector `.w-webflow-badge>img`**: `transition: unset` extracted from `www-paaspop-nl` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s,color .1s` extracted from `www-paaspop-nl` stylesheet.
- **Selector `.w-lightbox-control`**: `transition: all .3s` extracted from `www-paaspop-nl` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.625,.05,0,1)`)**: Governs interactive state transitions across `<header.navbar_component>` and `<section.section_fifty-years>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-paaspop-nl`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
