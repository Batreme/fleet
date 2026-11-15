---
title: "UI Prompt Blueprint: inks-studio"
date: 2026-11-15
target: "[[overview|inks-studio]]"
status: analyzed
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#f2f9fe` ink, `#959ba6` accent)"
---

# UI Design System & Master Generation Blueprint: inks-studio

> **Ink Studio - UI UX Design, CRO & Webflow Development Agency** (http://inks.studio/) — Ink Studio is a UI/UX design and CRO agency. We build high-converting Webflow sites, mobile & web apps, and design systems for SaaS and s...

![Desktop Viewport Capture (1440x9230)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Ink Studio - UI UX Design, CRO & Webflow Development Agency** (`http://inks.studio/`). Ink Studio is a UI/UX design and CRO agency. We build high-converting Webflow sites, mobile & web apps, and design systems for SaaS and s...
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#f2f9fe` ink, `#959ba6` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--black)` in `:root`) paired with `#f2f9fe` primary typography and `#959ba6` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Ibmplexserif` for display copy (`Building Impact`) with `Instrument Serif` and `Ibmplexserif`.
  - **Calibrated Spatial Grid & Motion**: Combines `940px` container bounds (`gap: .4rem`, padding `40px`) with `cubic-bezier(.4,0,1,1)` easing and GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×9230px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `940px` extracted from `inks-studio` stylesheet.
- **Canvas Lateral Padding & Spacing**: `40px` lateral canvas padding with `.4rem` grid gap.
- **Border Radius Scale**: `2px`, `6px`, `8px`, `100px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 940px`, `gap: .4rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `40px` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen and (max-width:991px)`, `@media screen and (max-width:767px)`, `@media screen and (min-width:1440px)`, `@media screen and (min-width:1920px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--black)` in `:root` |
| **Primary Typography Ink** | `#4141f2` | `var(--blue)` in `:root` |
| **Elevated Surface / Card Substrate** | `#ffd401` | `var(--primary)` in `:root` |
| **Interactive Accent / Highlight** | `#959ba6` | `var(--gray)` in `:root` |
| **Secondary / Muted Copy** | `#afafaf` | `var(--white-light)` in `:root` |
| **Structural Hairline Border** | `#f2f9fe` | `var(--white-tiny)` in `:root` |
| **Variable Token (`--dark-light`)** | `#3f3f3f` | `var(--dark-light)` in `:root` |
| **Variable Token (`--gray-bg`)** | `#e9e9e9` | `var(--gray-bg)` in `:root` |
| **Variable Token (`--bg-color`)** | `#0f1115` | `var(--bg-color)` in `:root` |
| **Variable Token (`--divider`)** | `#e8e8e8` | `var(--divider)` in `:root` |
| **Variable Token (`--bg-blue`)** | `#d5ecf8` | `var(--bg-blue)` in `:root` |
| **Variable Token (`--purple`)** | `#27104e` | `var(--purple)` in `:root` |
| **Variable Token (`--green`)** | `#104e3b` | `var(--green)` in `:root` |
| **Variable Token (`--color`)** | `#ffefed` | `var(--color)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--black` | `#000` | Canvas / Surface Token |
| `--background` | `whitesmoke` | Canvas / Surface Token |
| `--blue` | `#4141f2` | Color / Atmospheric Token |
| `--primary` | `#ffd401` | Brand / Palette Token |
| `--gray` | `#959ba6` | Color / Atmospheric Token |
| `--white-light` | `#afafaf` | Canvas / Surface Token |
| `--white-tiny` | `#f2f9fe` | Canvas / Surface Token |
| `--dark-light` | `#3f3f3f` | Canvas / Surface Token |
| `--gray-bg` | `#e9e9e9` | Canvas / Surface Token |
| `--white` | `white` | Canvas / Surface Token |
| `--bg-color` | `#0f1115` | Canvas / Surface Token |
| `--divider` | `#e8e8e8` | Color / Atmospheric Token |
| `--bg-blue` | `#d5ecf8` | Canvas / Surface Token |
| `--purple` | `#27104e` | Color / Atmospheric Token |
| `--green` | `#104e3b` | Color / Atmospheric Token |
| `--color` | `#ffefed` | Brand / Palette Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Ibmplexserif`.
- **Primary Body Stack**: `Instrument Serif`.
- **Technical / Metadata Stack**: `Ibmplexserif`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5/2.25)`, `--text-5xl: 3rem`; rule `h1` (`font-size: var(--text-base)!important`, `line-height: var(--tw-leading,var(...`).
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2/1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`font-size: var(--text-sm)!important`, `line-height: var(--tw-leading,var(...`).
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5/1)`; rule `p` (`font-size: var(--text-sm)`, `line-height: var(--tw-leading,var(...`).
- **Metadata & Navigation Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1/.75)`, `--text-sm: .875rem`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.nav-link`**: `transition: border-color .4s` extracted from `inks-studio` stylesheet.
- **Selector `.section-featured-img-wrapper`**: `transition: all .2s` extracted from `inks-studio` stylesheet.
- **Selector `.pricing-card-button`**: `transition: background-color .4s,color .4s` extracted from `inks-studio` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,1,1)`)**: Governs interactive state transitions across `<header.section-hero>` and `<section.section-service>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Framer Motion Layout Physics with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Ink Studio - UI UX Design, CRO & Webflow D │
│ ====================================================================== │
│ [ <header.section-hero>    | Home · Work · Webflow · Framer · Astro ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.section-featured-item>                      |   │
│ | H1: Building Impact                                              |   │
│ | Substrate: #000       | Ink: #f2f9fe    | Accent: #959ba6        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.section-service> ) max-w: 940px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Level up your SaaS.Turn sign |  | Trusted by founders. Built f | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: .4rem ) | │
│ | [<header.section-he] -> [<section.section-f] -> [<section.section-s] │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.footer>       ) | http://inks.studio/                │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.section-hero> — `inks-studio`)**:
   - Landmark `<header class="section-hero">` hosting `Ink Studio - UI UX Design, CRO & Web` navigation (`Home · Work · Webflow · Framer · Astro`), DOM attributes (`data-wf-domain="www.inks.studio"`, `data-wf-page="67375bd348251862372613c7"`, `data-wf-site="67375bd348251862372613c8"`, `data-gtag-id="AW-18125669814"`), and stylesheet rule `body { color:333;font-family:Manrope,sans-serif;font-size:1rem;line-height:20px }`.
2. **Hero Stage & Focal Lead (<section.section-featured-item> — `Building Impact`)**:
   - Landmark `<section class="section-featured-item">` presenting display lead `Building Impact` and copy excerpt *"at checkout for 30% off any template"* over `#000` canvas and `#f2f9fe` ink.
3. **Primary Showcase & Content Grid (<section.section-service> — `Level up your SaaS.Turn sign-ups i`)**:
   - Landmark `<section class="section-service">` rendering section `Level up your SaaS.Turn sign-ups into paying users.` with copy *"UI & UX Design Services"*, asset references (`cdn.prod.website-files.com`, `inks-studio.webflow.shared.1e5091...`, `inks-studio.webflow.67375bd348251...`, `fonts.googleapis.com`), and grid rule `label { color:var(--black);margin-bottom:5px;font-family:Sourcesanspro;font-weig... }`.
4. **Interactive Detail & Feature Matrix (<section.section-trust> — `Trusted by founders. Built for mea`)**:
   - Landmark `<section class="section-trust">` framing `Trusted by founders. Built for measurable growth.` and `Before & After: How We Transformed These Products` (*"Conversion Strategist"*) with `#ffd401` surface cards, `#959ba6` accents, and `figure { margin-bottom:10px }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `http://inks.studio/`)**:
   - Landmark `<footer class="footer">` anchoring `Ink Studio - UI UX Design, CRO &` footer links (`Home · Work · Webflow · Framer · Astro`), copy *"Let's Discuss project Let's Discuss project"*, and `#f2f9fe` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: inks-studio (Ink Studio - UI UX Design, CRO & Webflow Development Agency)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `inks-studio` (**Ink Studio - UI UX Design, CRO & Webflow Development Agency** — `http://inks.studio/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#f2f9fe` ink, `#959ba6` accent).
- **Identity & Domain Context**: Ink Studio is a UI/UX design and CRO agency. We build high-converting Webflow sites, mobile & web apps, and design systems for SaaS and s...
- **Primary Substrate**: `#000` (`var(--black)` in `:root`), **Primary Ink**: `#f2f9fe`, **Accent / Highlight**: `#959ba6`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--black)` in `:root`) paired with `#f2f9fe` primary typography and `#959ba6` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Ibmplexserif` for display copy (`Building Impact`) with `Instrument Serif` and `Ibmplexserif`.
  - **Calibrated Spatial Grid & Motion**: Combines `940px` container bounds (`gap: .4rem`, padding `40px`) with `cubic-bezier(.4,0,1,1)` easing and GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `inks-studio` in your global stylesheet:

:root {
  /* Ink Studio - UI UX Design, CRO & Webflow Development Agency (inks-studio) — Ground-Truth Extracted CSS Variables */
  --black: #000; /* Canvas / Surface Token (inks-studio) */
  --background: whitesmoke; /* Canvas / Surface Token (inks-studio) */
  --blue: #4141f2; /* Color / Atmospheric Token (inks-studio) */
  --primary: #ffd401; /* Brand / Palette Token (inks-studio) */
  --gray: #959ba6; /* Color / Atmospheric Token (inks-studio) */
  --white-light: #afafaf; /* Canvas / Surface Token (inks-studio) */
  --white-tiny: #f2f9fe; /* Canvas / Surface Token (inks-studio) */
  --dark-light: #3f3f3f; /* Canvas / Surface Token (inks-studio) */
  --gray-bg: #e9e9e9; /* Canvas / Surface Token (inks-studio) */
  --white: white; /* Canvas / Surface Token (inks-studio) */
  --bg-color: #0f1115; /* Canvas / Surface Token (inks-studio) */
  --divider: #e8e8e8; /* Color / Atmospheric Token (inks-studio) */
  --bg-blue: #d5ecf8; /* Canvas / Surface Token (inks-studio) */
  --purple: #27104e; /* Color / Atmospheric Token (inks-studio) */
  --green: #104e3b; /* Color / Atmospheric Token (inks-studio) */
  --color: #ffefed; /* Brand / Palette Token (inks-studio) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#000` — grounded in `var(--black)` in `:root`
- **Primary Typography Ink**: `#4141f2` — grounded in `var(--blue)` in `:root`
- **Elevated Surface / Card Substrate**: `#ffd401` — grounded in `var(--primary)` in `:root`
- **Interactive Accent / Highlight**: `#959ba6` — grounded in `var(--gray)` in `:root`
- **Secondary / Muted Copy**: `#afafaf` — grounded in `var(--white-light)` in `:root`
- **Structural Hairline Border**: `#f2f9fe` — grounded in `var(--white-tiny)` in `:root`
- **Variable Token (`--dark-light`)**: `#3f3f3f` — grounded in `var(--dark-light)` in `:root`
- **Variable Token (`--gray-bg`)**: `#e9e9e9` — grounded in `var(--gray-bg)` in `:root`
- **Variable Token (`--bg-color`)**: `#0f1115` — grounded in `var(--bg-color)` in `:root`
- **Variable Token (`--divider`)**: `#e8e8e8` — grounded in `var(--divider)` in `:root`
- **Variable Token (`--bg-blue`)**: `#d5ecf8` — grounded in `var(--bg-blue)` in `:root`
- **Variable Token (`--purple`)**: `#27104e` — grounded in `var(--purple)` in `:root`
- **Variable Token (`--green`)**: `#104e3b` — grounded in `var(--green)` in `:root`
- **Variable Token (`--color`)**: `#ffefed` — grounded in `var(--color)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×9230px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `940px` extracted from `inks-studio` stylesheet
- **Padding & Gutters**: `40px` lateral canvas padding with `.4rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 940px`, `gap: .4rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `40px` horizontal padding
- **Media Queries**: `@media screen and (max-width:991px)`, `@media screen and (max-width:767px)`, `@media screen and (min-width:1440px)`, `@media screen and (min-width:1920px)`
- **Corner Radii**: `2px`, `6px`, `8px`, `100px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Ibmplexserif`
- **Body Font Stack**: `Instrument Serif`
- **Monospace / Technical Font Stack**: `Ibmplexserif`
- **H1 Display Rule**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5/2.25)`, `--text-5xl: 3rem`; rule `h1` (`font-size: var(--text-base)!important`, `line-height: var(--tw-leading,var(...`)
- **H2 Section Rule**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2/1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`font-size: var(--text-sm)!important`, `line-height: var(--tw-leading,var(...`)
- **Body Copy Rule**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5/1)`; rule `p` (`font-size: var(--text-sm)`, `line-height: var(--tw-leading,var(...`)
- **Metadata & Index Rule**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1/.75)`, `--text-sm: .875rem`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `inks-studio` (`Ink Studio - UI UX Design, CRO & Webflow Development Agency`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.section-hero> — `inks-studio`)**:
   - DOM & Selectors: Landmark `<header class="section-hero">` hosting `Ink Studio - UI UX Design, CRO & Web` navigation (`Home · Work · Webflow · Framer · Astro`), DOM attributes (`data-wf-domain="www.inks.studio"`, `data-wf-page="67375bd348251862372613c7"`, `data-wf-site="67375bd348251862372613c8"`, `data-gtag-id="AW-18125669814"`), and stylesheet rule `body { color:333;font-family:Manrope,sans-serif;font-size:1rem;line-height:20px }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.section-hero> — `inks-studio`)` (`inks-studio`) adapts across `@media screen and (max-width:991px)`, `@media screen and (max-width:767px)`, `@media screen and (min-width:1440px)`, `@media screen and (min-width:1920px)` with `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)` transitions and links `Home · Work · Webflow · Framer · Astro`.
2. **Hero Stage & Focal Lead (<section.section-featured-item> — `Building Impact`)**:
   - DOM & Selectors: Landmark `<section class="section-featured-item">` presenting display lead `Building Impact` and copy excerpt *"at checkout for 30% off any template"* over `#000` canvas and `#f2f9fe` ink.
   - Responsive Contract: Hero stage (`1440×9230px` desktop / `390×2400px` mobile) sets `#000` background with `#f2f9fe` headline `Building Impact`.
3. **Primary Showcase & Content Grid (<section.section-service> — `Level up your SaaS.Turn sign-ups i`)**:
   - DOM & Selectors: Landmark `<section class="section-service">` rendering section `Level up your SaaS.Turn sign-ups into paying users.` with copy *"UI & UX Design Services"*, asset references (`cdn.prod.website-files.com`, `inks-studio.webflow.shared.1e5091...`, `inks-studio.webflow.67375bd348251...`, `fonts.googleapis.com`), and grid rule `label { color:var(--black);margin-bottom:5px;font-family:Sourcesanspro;font-weig... }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.section-service> — `Level up your SaaS.Turn sign-ups i`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 940px`, `gap: .4rem`) on desktop and Single-column vertical stack at `390px` viewport width with `40px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.section-trust> — `Trusted by founders. Built for mea`)**:
   - DOM & Selectors: Landmark `<section class="section-trust">` framing `Trusted by founders. Built for measurable growth.` and `Before & After: How We Transformed These Products` (*"Conversion Strategist"*) with `#ffd401` surface cards, `#959ba6` accents, and `figure { margin-bottom:10px }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.section-trust> — `Trusted by founders. Built for mea`)` uses `2px`, `6px`, `8px`, `100px` radii, `#959ba6` highlights, and assets (cdn.prod.website-files.com, inks-studio.webflow.shared.1e5091..., inks-studio.webflow.67375bd348251...).
5. **Colophon & Global Directory Footer (<footer.footer> — `http://inks.studio/`)**:
   - DOM & Selectors: Landmark `<footer class="footer">` anchoring `Ink Studio - UI UX Design, CRO &` footer links (`Home · Work · Webflow · Framer · Astro`), copy *"Let's Discuss project Let's Discuss project"*, and `#f2f9fe` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.footer> — `http://inks.studio/`)` aligns to `940px` extracted from `inks-studio` stylesheet with `40px` lateral canvas padding with `.4rem` grid gap and attributes (data-wf-domain="www.inks.studio", data-wf-page="67375bd348251862372613c7", data-wf-site="67375bd348251862372613c8").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"at checkout for 30% off any template"*
- Copy Excerpt 2: *"UI & UX Design Services"*
- Copy Excerpt 3: *"Conversion Strategist"*
- Copy Excerpt 4: *"Let's Discuss project Let's Discuss project"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`
- **Extracted Stylesheet Rules (`inks-studio`)**:
- `body { color:333;font-family:Manrope,sans-serif;font-size:1rem;line-height:20px }`
- `label { color:var(--black);margin-bottom:5px;font-family:Sourcesanspro;font-weig... }`
- `figure { margin-bottom:10px }`
- `.w-layout-blockcontainer { max-width:940px;margin-left:auto;margin-right:auto;display:block }`
- `.w-checkbox { margin-bottom:5px;padding-left:20px;display:block }`
- **Per-Selector Transition Rules**:
- **Selector `.nav-link`**: `transition: border-color .4s` extracted from `inks-studio` stylesheet.
- **Selector `.section-featured-img-wrapper`**: `transition: all .2s` extracted from `inks-studio` stylesheet.
- **Selector `.pricing-card-button`**: `transition: background-color .4s,color .4s` extracted from `inks-studio` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,1,1)`)**: Governs interactive state transitions across `<header.section-hero>` and `<section.section-service>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Framer Motion Layout Physics with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `inks-studio`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
