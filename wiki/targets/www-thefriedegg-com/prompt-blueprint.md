---
title: "UI Prompt Blueprint: www-thefriedegg-com"
date: 2026-11-15
target: "[[overview|www-thefriedegg-com]]"
status: analyzed
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#666` canvas, `#f3f1e7` ink, `#fff0` accent)"
---

# UI Design System & Master Generation Blueprint: www-thefriedegg-com

> **Fried Egg Golf** (https://www.thefriedegg.com/) — Visit Fried Egg Golf for in-depth golf course profiles, entertaining podcasts, premium event access, and all of the merch you never knew...

![Desktop Viewport Capture (1440x13591)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Fried Egg Golf** (`https://www.thefriedegg.com/`). Visit Fried Egg Golf for in-depth golf course profiles, entertaining podcasts, premium event access, and all of the merch you never knew...
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#666` canvas, `#f3f1e7` ink, `#fff0` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#666` (`var(--_colours---base--grey-100)` in `:root`) paired with `#f3f1e7` primary typography and `#fff0` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Stanley` for display copy (`A deeper level of golf`) with `Grey` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `940px` container bounds (`gap: 16px`, padding `9px`) with `cubic-bezier(.645,.045,.355,1)` easing and GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×13591px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `940px` extracted from `www-thefriedegg-com` stylesheet.
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
| **Primary Canvas Substrate** | `#666` | `var(--_colours---base--grey-100)` in `:root` |
| **Primary Typography Ink** | `#f3f1e7` | `var(--_colours---base--cream)` in `:root` |
| **Elevated Surface / Card Substrate** | `#1b1a1a` | `var(--_colours---base--black)` in `:root` |
| **Interactive Accent / Highlight** | `#fff0` | `var(--_colours---base--transparent)` in `:root` |
| **Secondary / Muted Copy** | `#ffee54` | `var(--_colours---base--brand)` in `:root` |
| **Structural Hairline Border** | `#fe4d12` | `var(--_colours---base--orange)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--w-backdrop-animation` | `initial` | Motion / Easing Token |
| `--_theme---background` | `var(--_colours---base--white)` | Canvas / Surface Token |
| `--_text-style---font-family` | `var(--_typography---font--primary-family)` | Typography Ink Token |
| `--_theme---text` | `var(--_colours---base--black)` | Typography Ink Token |
| `--_text-style---font-size` | `var(--_typography---font-size--text-main)` | Typography Ink Token |
| `--_text-style---line-height` | `var(--_typography---line-height--1-4)` | Typography Ink Token |
| `--_text-style---font-weight` | `var(--_typography---font--primary-regular)` | Typography Ink Token |
| `--_text-style---letter-spacing` | `var(--_typography---letter-spacing--0em)` | Typography Ink Token |
| `--_spacing---space--5` | `1.25rem` | Layout / Spatial Grid Token |
| `--_typography---font--primary-medium` | `500` | Brand / Palette Token |
| `--size--0-5rem` | `.5rem` | Layout / Spatial Grid Token |
| `--size--2rem` | `2rem` | Layout / Spatial Grid Token |
| `--size--1-5rem` | `1.5rem` | Layout / Spatial Grid Token |
| `--size--1rem` | `1rem` | Layout / Spatial Grid Token |
| `--_typography---font--secondary-family` | `Stanley,Arial,sans-serif` | Brand / Palette Token |
| `--_typography---font-size--text-medium` | `1.125rem` | Typography Ink Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Stanley`.
- **Primary Body Stack**: `Grey`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--_typography---font-size--h1: 5rem`, `--_typography---font-size--display: 6rem`; rule `h1` (`font-size: var(--_text-style---font-size)`, `line-height: var(--_text-style---l...`, `letter-spacing: var(--_text-style---l...`, `font-weight: var(--_text-s...`).
- **Section Heading (`H2`)**: CSS variables `--_typography---font-size--h2: 4rem`; rule `h2` (`font-size: var(--_text-style---font-size)`, `line-height: var(--_text-style---l...`, `letter-spacing: var(--_text-style---l...`, `font-weight: var(--_text-s...`).
- **Body Copy**: rule `p` (`font-size: var(--_typography---font-size...`, `line-height: var(--_typography---l...`, `letter-spacing: var(--_typography---l...`).
- **Metadata & Navigation Labels**: CSS variables `--_text-style---letter-spacing: var(--_typography---letter-spacing--0em)`, `--_typography---letter-spacing--0-03em: -.03em`, `--radius--small: .5rem`; rule `small` (`font-size: 0.75rem`, `letter-spacing: 0.06em`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.645,.045,.355,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.w-webflow-badge>img`**: `transition: unset` extracted from `www-thefriedegg-com` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s,color .1s` extracted from `www-thefriedegg-com` stylesheet.
- **Selector `.w-lightbox-control`**: `transition: all .3s` extracted from `www-thefriedegg-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.645,.045,.355,1)`)**: Governs interactive state transitions across `<header.header_main_wrap>` and `<section.explore_content_wrap>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine, Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Fried Egg Golf                             │
│ ====================================================================== │
│ [ <header.header_main_wrap | Log in · Newsletter · Pro Shop · Archi ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.cms_filters_wrap>                           |   │
│ | H1: A deeper level of golf                                       |   │
│ | Substrate: #666       | Ink: #f3f1e7    | Accent: #fff0          |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.explore_content_w) max-w: 940px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | 2026 U.S. Mid-Amateur Champi |  | The Commons                  | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 16px  ) | │
│ | [<header.header_mai] -> [<section.cms_filte] -> [<section.explore_c] │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer_wrap>  ) | https://www.thefriedegg.com/       │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.header_main_wrap> — `www-thefriedegg-com`)**:
   - Landmark `<header class="header_main_wrap">` hosting `Fried Egg Golf` navigation (`Log in · Newsletter · Pro Shop · Architecture · Course Profiles`), DOM attributes (`data-wf-domain="www.thefriedegg.com"`, `data-wf-page="67ab6ef769ff843db623d6fa"`, `data-wf-site="67ab6ef769ff843db623d6f5"`, `data-hubspot-styled-components`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
2. **Hero Stage & Focal Lead (<section.cms_filters_wrap> — `A deeper level of golf`)**:
   - Landmark `<section class="cms_filters_wrap cms_home_filters">` presenting display lead `A deeper level of golf` and copy excerpt *"Skip to main content"* over `#666` canvas and `#f3f1e7` ink.
3. **Primary Showcase & Content Grid (<section.explore_content_wrap> — `2026 U.S. Mid-Amateur Champion And`)**:
   - Landmark `<section class="explore_content_wrap">` rendering section `2026 U.S. Mid-Amateur Champion Andrew Bailey` with copy *"Architect Profiles"*, asset references (`cdn.prod.website-files.com`, `friedegg-staging.shared.1a7f178f4...`, `iframe_api.b14cb21cf7e4cfe54860.js`, `www-widgetapi.js`), and grid rule `summary { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.latest_wrap> — `The Commons`)**:
   - Landmark `<section class="latest_wrap">` framing `The Commons` and `Paulie's Picks: 2026 Austin Championship presente...` (*"Eggstracurriculars"*) with `#1b1a1a` surface cards, `#fff0` accents, and `video { vertical-align:baseline;display:inline-block }`.
5. **Colophon & Global Directory Footer (<footer.footer_wrap> — `https://www.thefriedegg.com/`)**:
   - Landmark `<footer class="footer_wrap">` anchoring `Fried Egg Golf` footer links (`Log in · Newsletter · Pro Shop · Architecture · Course Profiles`), copy *"Fried Egg Golf Guides"*, and `#fe4d12` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-thefriedegg-com (Fried Egg Golf)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-thefriedegg-com` (**Fried Egg Golf** — `https://www.thefriedegg.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#666` canvas, `#f3f1e7` ink, `#fff0` accent).
- **Identity & Domain Context**: Visit Fried Egg Golf for in-depth golf course profiles, entertaining podcasts, premium event access, and all of the merch you never knew...
- **Primary Substrate**: `#666` (`var(--_colours---base--grey-100)` in `:root`), **Primary Ink**: `#f3f1e7`, **Accent / Highlight**: `#fff0`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#666` (`var(--_colours---base--grey-100)` in `:root`) paired with `#f3f1e7` primary typography and `#fff0` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Stanley` for display copy (`A deeper level of golf`) with `Grey` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `940px` container bounds (`gap: 16px`, padding `9px`) with `cubic-bezier(.645,.045,.355,1)` easing and GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-thefriedegg-com` in your global stylesheet:

:root {
  /* Fried Egg Golf (www-thefriedegg-com) — Ground-Truth Extracted CSS Variables */
  --w-backdrop-animation: initial; /* Motion / Easing Token (www-thefriedegg-com) */
  --_theme---background: var(--_colours---base--white); /* Canvas / Surface Token (www-thefriedegg-com) */
  --_text-style---font-family: var(--_typography---font--primary-family); /* Typography Ink Token (www-thefriedegg-com) */
  --_theme---text: var(--_colours---base--black); /* Typography Ink Token (www-thefriedegg-com) */
  --_text-style---font-size: var(--_typography---font-size--text-main); /* Typography Ink Token (www-thefriedegg-com) */
  --_text-style---line-height: var(--_typography---line-height--1-4); /* Typography Ink Token (www-thefriedegg-com) */
  --_text-style---font-weight: var(--_typography---font--primary-regular); /* Typography Ink Token (www-thefriedegg-com) */
  --_text-style---letter-spacing: var(--_typography---letter-spacing--0em); /* Typography Ink Token (www-thefriedegg-com) */
  --_spacing---space--5: 1.25rem; /* Layout / Spatial Grid Token (www-thefriedegg-com) */
  --_typography---font--primary-medium: 500; /* Brand / Palette Token (www-thefriedegg-com) */
  --size--0-5rem: .5rem; /* Layout / Spatial Grid Token (www-thefriedegg-com) */
  --size--2rem: 2rem; /* Layout / Spatial Grid Token (www-thefriedegg-com) */
  --size--1-5rem: 1.5rem; /* Layout / Spatial Grid Token (www-thefriedegg-com) */
  --size--1rem: 1rem; /* Layout / Spatial Grid Token (www-thefriedegg-com) */
  --_typography---font--secondary-family: Stanley,Arial,sans-serif; /* Brand / Palette Token (www-thefriedegg-com) */
  --_typography---font-size--text-medium: 1.125rem; /* Typography Ink Token (www-thefriedegg-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#666` — grounded in `var(--_colours---base--grey-100)` in `:root`
- **Primary Typography Ink**: `#f3f1e7` — grounded in `var(--_colours---base--cream)` in `:root`
- **Elevated Surface / Card Substrate**: `#1b1a1a` — grounded in `var(--_colours---base--black)` in `:root`
- **Interactive Accent / Highlight**: `#fff0` — grounded in `var(--_colours---base--transparent)` in `:root`
- **Secondary / Muted Copy**: `#ffee54` — grounded in `var(--_colours---base--brand)` in `:root`
- **Structural Hairline Border**: `#fe4d12` — grounded in `var(--_colours---base--orange)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×13591px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `940px` extracted from `www-thefriedegg-com` stylesheet
- **Padding & Gutters**: `9px` lateral canvas padding with `16px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 940px`, `gap: 16px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `9px` horizontal padding
- **Media Queries**: `@media screen and (max-width:991px)`, `@media screen and (max-width:767px)`, `@media screen and (max-width:479px)`, `@media (min-width:768px)`
- **Corner Radii**: `3px`, `100%`, `50%`, `2px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Stanley`
- **Body Font Stack**: `Grey`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: CSS variables `--_typography---font-size--h1: 5rem`, `--_typography---font-size--display: 6rem`; rule `h1` (`font-size: var(--_text-style---font-size)`, `line-height: var(--_text-style---l...`, `letter-spacing: var(--_text-style---l...`, `font-weight: var(--_text-s...`)
- **H2 Section Rule**: CSS variables `--_typography---font-size--h2: 4rem`; rule `h2` (`font-size: var(--_text-style---font-size)`, `line-height: var(--_text-style---l...`, `letter-spacing: var(--_text-style---l...`, `font-weight: var(--_text-s...`)
- **Body Copy Rule**: rule `p` (`font-size: var(--_typography---font-size...`, `line-height: var(--_typography---l...`, `letter-spacing: var(--_typography---l...`)
- **Metadata & Index Rule**: CSS variables `--_text-style---letter-spacing: var(--_typography---letter-spacing--0em)`, `--_typography---letter-spacing--0-03em: -.03em`, `--radius--small: .5rem`; rule `small` (`font-size: 0.75rem`, `letter-spacing: 0.06em`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-thefriedegg-com` (`Fried Egg Golf`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.header_main_wrap> — `www-thefriedegg-com`)**:
   - DOM & Selectors: Landmark `<header class="header_main_wrap">` hosting `Fried Egg Golf` navigation (`Log in · Newsletter · Pro Shop · Architecture · Course Profiles`), DOM attributes (`data-wf-domain="www.thefriedegg.com"`, `data-wf-page="67ab6ef769ff843db623d6fa"`, `data-wf-site="67ab6ef769ff843db623d6f5"`, `data-hubspot-styled-components`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.header_main_wrap> — `www-thefriedegg-com`)` (`www-thefriedegg-com`) adapts across `@media screen and (max-width:991px)`, `@media screen and (max-width:767px)`, `@media screen and (max-width:479px)`, `@media (min-width:768px)` with `cubic-bezier(.645,.045,.355,1)` transitions and links `Log in · Newsletter · Pro Shop · Architecture · Course Profiles`.
2. **Hero Stage & Focal Lead (<section.cms_filters_wrap> — `A deeper level of golf`)**:
   - DOM & Selectors: Landmark `<section class="cms_filters_wrap cms_home_filters">` presenting display lead `A deeper level of golf` and copy excerpt *"Skip to main content"* over `#666` canvas and `#f3f1e7` ink.
   - Responsive Contract: Hero stage (`1440×13591px` desktop / `390×2400px` mobile) sets `#666` background with `#f3f1e7` headline `A deeper level of golf`.
3. **Primary Showcase & Content Grid (<section.explore_content_wrap> — `2026 U.S. Mid-Amateur Champion And`)**:
   - DOM & Selectors: Landmark `<section class="explore_content_wrap">` rendering section `2026 U.S. Mid-Amateur Champion Andrew Bailey` with copy *"Architect Profiles"*, asset references (`cdn.prod.website-files.com`, `friedegg-staging.shared.1a7f178f4...`, `iframe_api.b14cb21cf7e4cfe54860.js`, `www-widgetapi.js`), and grid rule `summary { display:block }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.explore_content_wrap> — `2026 U.S. Mid-Amateur Champion And`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 940px`, `gap: 16px`) on desktop and Single-column vertical stack at `390px` viewport width with `9px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.latest_wrap> — `The Commons`)**:
   - DOM & Selectors: Landmark `<section class="latest_wrap">` framing `The Commons` and `Paulie's Picks: 2026 Austin Championship presente...` (*"Eggstracurriculars"*) with `#1b1a1a` surface cards, `#fff0` accents, and `video { vertical-align:baseline;display:inline-block }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.latest_wrap> — `The Commons`)` uses `3px`, `100%`, `50%`, `2px` radii, `#fff0` highlights, and assets (cdn.prod.website-files.com, friedegg-staging.shared.1a7f178f4..., iframe_api.b14cb21cf7e4cfe54860.js).
5. **Colophon & Global Directory Footer (<footer.footer_wrap> — `https://www.thefriedegg.com/`)**:
   - DOM & Selectors: Landmark `<footer class="footer_wrap">` anchoring `Fried Egg Golf` footer links (`Log in · Newsletter · Pro Shop · Architecture · Course Profiles`), copy *"Fried Egg Golf Guides"*, and `#fe4d12` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.footer_wrap> — `https://www.thefriedegg.com/`)` aligns to `940px` extracted from `www-thefriedegg-com` stylesheet with `9px` lateral canvas padding with `16px` grid gap and attributes (data-wf-domain="www.thefriedegg.com", data-wf-page="67ab6ef769ff843db623d6fa", data-wf-site="67ab6ef769ff843db623d6f5").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Skip to main content"*
- Copy Excerpt 2: *"Architect Profiles"*
- Copy Excerpt 3: *"Eggstracurriculars"*
- Copy Excerpt 4: *"Fried Egg Golf Guides"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.645,.045,.355,1)`
- **Extracted Stylesheet Rules (`www-thefriedegg-com`)**:
- `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`
- `summary { display:block }`
- `video { vertical-align:baseline;display:inline-block }`
- `template { display:none }`
- `strong { font-weight:700 }`
- **Per-Selector Transition Rules**:
- **Selector `.w-webflow-badge>img`**: `transition: unset` extracted from `www-thefriedegg-com` stylesheet.
- **Selector `.w-slider-dot`**: `transition: background-color .1s,color .1s` extracted from `www-thefriedegg-com` stylesheet.
- **Selector `.w-lightbox-control`**: `transition: all .3s` extracted from `www-thefriedegg-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.645,.045,.355,1)`)**: Governs interactive state transitions across `<header.header_main_wrap>` and `<section.explore_content_wrap>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine, Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-thefriedegg-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
