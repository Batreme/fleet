---
title: "UI Prompt Blueprint: thebranx-com"
date: 2026-11-15
target: "[[overview|thebranx-com]]"
status: analyzed
archetype: "Light-Substrate Editorial & Modular Grid System (`#fff085` canvas, `#4a5565` ink, `#f9fafb` accent)"
---

# UI Design System & Master Generation Blueprint: thebranx-com

> **The branding agency for startups, AI & SaaS - The Branx** (https://thebranx.com) — The Branx builds category-defining brands and websites for AI, SaaS and B2B tech startups: strategy, identity, web design and motion, fro...

![Desktop Viewport Capture (1440x9398)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **The branding agency for startups, AI & SaaS - The Branx** (`https://thebranx.com`). The Branx builds category-defining brands and websites for AI, SaaS and B2B tech startups: strategy, identity, web design and motion, fro...
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#fff085` canvas, `#4a5565` ink, `#f9fafb` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fff085` (`var(--color-yellow-200)` in `:root`) paired with `#4a5565` primary typography and `#f9fafb` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Marcellus` for display copy (`The tech branding agency for AI & Sa`) with `Marcellus Fallback` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `40rem` container bounds (`gap: var(--bx-space-3)`, padding `var(--bx-section)`) with `cubic-bezier(.4,0,.2,1)` easing and Three.js / WebGL Canvas Pipeline, Lottie Vector Animation Player.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×9398px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `40rem` extracted from `thebranx-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `var(--bx-section)` lateral canvas padding with `var(--bx-space-3)` grid gap.
- **Border Radius Scale**: `.25rem`, `50%`, `44px`, `16px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: var(--bx-space-3)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--bx-section)` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff085` | `var(--color-yellow-200)` in `:root` |
| **Primary Typography Ink** | `#3080ff` | `var(--color-blue-500)` in `:root` |
| **Elevated Surface / Card Substrate** | `#155dfc` | `var(--color-blue-600)` in `:root` |
| **Interactive Accent / Highlight** | `#f9fafb` | `var(--color-gray-50)` in `:root` |
| **Secondary / Muted Copy** | `#4a5565` | `var(--color-gray-600)` in `:root` |
| **Structural Hairline Border** | `#fff` | `var(--color-white)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-marcellus` | `"Marcellus", "Marcellus Fallback"` | Typography / Scale Token |
| `--font-sans` | `var(--bx-sans)` | Typography / Scale Token |
| `--font-mono` | `var(--bx-mono)` | Typography / Scale Token |
| `--color-yellow-200` | `#fff085` | Brand / Palette Token |
| `--color-blue-500` | `#3080ff` | Brand / Palette Token |
| `--color-blue-600` | `#155dfc` | Brand / Palette Token |
| `--color-gray-50` | `#f9fafb` | Brand / Palette Token |
| `--color-gray-600` | `#4a5565` | Brand / Palette Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--text-xs` | `14px` | Typography Ink Token |
| `--text-sm` | `var(--bx-fs-small)` | Typography Ink Token |
| `--text-sm--line-height` | `calc(1.25 / .875)` | Typography Ink Token |
| `--text-lg` | `var(--bx-fs-lead)` | Typography Ink Token |
| `--text-xl` | `var(--bx-fs-card)` | Typography Ink Token |
| `--text-3xl` | `var(--bx-fs-h2)` | Typography Ink Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Marcellus`.
- **Primary Body Stack**: `Marcellus Fallback`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--text-4xl: var(--bx-fs-display)`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-6xl: 3.75rem`; rule `h1` (`font-size: var(--bx-fs-statement)`, `line-height: var(--bx-lh-statement)`).
- **Section Heading (`H2`)**: CSS variables `--text-3xl: var(--bx-fs-h2)`, `--text-3xl--line-height: calc(2.25 / 1.875)`, `--bx-fs-h2: clamp(32px, 3.6vw, 72px)`; rule `h2` (`font-size: var(--text-xl)`).
- **Body Copy**: CSS variables `--leading-body: var(--bx-lh-body)`, `--bx-fs-body: 16px`, `--bx-lh-body: 1.6`; rule `p` (`font-size: var(--bx-fs-lead)`, `line-height: var(--bx-lh-body)`).
- **Metadata & Navigation Labels**: CSS variables `--font-mono: var(--bx-mono)`, `--text-xs: 14px`, `--text-sm: var(--bx-fs-small)`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(0.17,0,0.2,1)`, `cubic-bezier(0.5,0,0.83,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: .15s` extracted from `thebranx-com` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `thebranx-com` stylesheet.
- **Selector `body`**: `transition: background-color var(--bx-dur-slow) var(--bx-ease)` extracted from `thebranx-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<header.bx-navbar>` and `<section.bx-section>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — The branding agency for startups, AI & Saa │
│ ====================================================================== │
│ [ <header.bx-navbar>       | Brand identity · Web design & dev. · S ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.bx-hero>                                    |   │
│ | H1: The tech branding agency for AI & SaaS startups              |   │
│ | Substrate: #fff085    | Ink: #4a5565    | Accent: #f9fafb        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.bx-section>      ) max-w: 40rem          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | The Branx turns complex tech |  | AI made it easy to launch a  | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: var(--) | │
│ | [<header.bx-navbar>] -> [<section.bx-hero>] -> [<section.bx-sectio]  │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.bx-footer>    ) | https://thebranx.com               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.bx-navbar> — `thebranx-com`)**:
   - Landmark `<header class="bx-navbar">` hosting `The branding agency for startups, AI` navigation (`Brand identity · Web design & dev. · Strategy & messaging · Motion design · Product naming`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-ch2css="true"`, `data-bx-nav`), and stylesheet rule `llus_b0edf5b9-module__eeLBqG__cla... { font-family:Marcellus,Marcellus Fallback;font-style:normal;font-weight:400 }`.
2. **Hero Stage & Focal Lead (<section.bx-hero> — `The tech branding agency for AI & `)**:
   - Landmark `<section class="bx-hero">` presenting display lead `The tech branding agency for AI & SaaS startups` and copy excerpt *"Strategy & messaging"* over `#fff085` canvas and `#4a5565` ink.
3. **Primary Showcase & Content Grid (<section.bx-section> — `The Branx turns complex tech into `)**:
   - Landmark `<section class="bx-section">` rendering section `The Branx turns complex tech into category-defini...` with copy *"The tech branding agency"*, asset references (`ec2f4458eb06f74e-s.p.217u6tza6bra...`, `0u5m-o-ck0mfs.css`, `3rz2zp8k1t-b-.css`, `194ug3jq7qzm9.js`), and grid rule `ellus_b0edf5b9-module__eeLBqG__va... { --font-marcellus:"Marcellus", "Marcellus Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.bx-philosophy> — `AI made it easy to launch a brand.`)**:
   - Landmark `<section class="bx-philosophy">` framing `AI made it easy to launch a brand. It made it har...` and `Start with the identity. Add the rest when you're...` (*"for AI & SaaS startups"*) with `#155dfc` surface cards, `#f9fafb` accents, and `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
5. **Colophon & Global Directory Footer (<footer.bx-footer> — `https://thebranx.com`)**:
   - Landmark `<footer class="bx-footer">` anchoring `The branding agency for startups` footer links (`Brand identity · Web design & dev. · Strategy & messaging · Motion design · Product naming`), copy *"Video intelligence for the real world"*, and `#fff` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: thebranx-com (The branding agency for startups, AI & SaaS - The Branx)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `thebranx-com` (**The branding agency for startups, AI & SaaS - The Branx** — `https://thebranx.com`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#fff085` canvas, `#4a5565` ink, `#f9fafb` accent).
- **Identity & Domain Context**: The Branx builds category-defining brands and websites for AI, SaaS and B2B tech startups: strategy, identity, web design and motion, fro...
- **Primary Substrate**: `#fff085` (`var(--color-yellow-200)` in `:root`), **Primary Ink**: `#4a5565`, **Accent / Highlight**: `#f9fafb`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fff085` (`var(--color-yellow-200)` in `:root`) paired with `#4a5565` primary typography and `#f9fafb` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Marcellus` for display copy (`The tech branding agency for AI & Sa`) with `Marcellus Fallback` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `40rem` container bounds (`gap: var(--bx-space-3)`, padding `var(--bx-section)`) with `cubic-bezier(.4,0,.2,1)` easing and Three.js / WebGL Canvas Pipeline, Lottie Vector Animation Player.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `thebranx-com` in your global stylesheet:

:root {
  /* The branding agency for startups, AI & SaaS - The Branx (thebranx-com) — Ground-Truth Extracted CSS Variables */
  --font-marcellus: "Marcellus", "Marcellus Fallback"; /* Typography / Scale Token (thebranx-com) */
  --font-sans: var(--bx-sans); /* Typography / Scale Token (thebranx-com) */
  --font-mono: var(--bx-mono); /* Typography / Scale Token (thebranx-com) */
  --color-yellow-200: #fff085; /* Brand / Palette Token (thebranx-com) */
  --color-blue-500: #3080ff; /* Brand / Palette Token (thebranx-com) */
  --color-blue-600: #155dfc; /* Brand / Palette Token (thebranx-com) */
  --color-gray-50: #f9fafb; /* Brand / Palette Token (thebranx-com) */
  --color-gray-600: #4a5565; /* Brand / Palette Token (thebranx-com) */
  --color-white: #fff; /* Canvas / Surface Token (thebranx-com) */
  --spacing: .25rem; /* Layout / Spatial Grid Token (thebranx-com) */
  --text-xs: 14px; /* Typography Ink Token (thebranx-com) */
  --text-sm: var(--bx-fs-small); /* Typography Ink Token (thebranx-com) */
  --text-sm--line-height: calc(1.25 / .875); /* Typography Ink Token (thebranx-com) */
  --text-lg: var(--bx-fs-lead); /* Typography Ink Token (thebranx-com) */
  --text-xl: var(--bx-fs-card); /* Typography Ink Token (thebranx-com) */
  --text-3xl: var(--bx-fs-h2); /* Typography Ink Token (thebranx-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#fff085` — grounded in `var(--color-yellow-200)` in `:root`
- **Primary Typography Ink**: `#3080ff` — grounded in `var(--color-blue-500)` in `:root`
- **Elevated Surface / Card Substrate**: `#155dfc` — grounded in `var(--color-blue-600)` in `:root`
- **Interactive Accent / Highlight**: `#f9fafb` — grounded in `var(--color-gray-50)` in `:root`
- **Secondary / Muted Copy**: `#4a5565` — grounded in `var(--color-gray-600)` in `:root`
- **Structural Hairline Border**: `#fff` — grounded in `var(--color-white)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×9398px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `40rem` extracted from `thebranx-com` stylesheet
- **Padding & Gutters**: `var(--bx-section)` lateral canvas padding with `var(--bx-space-3)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: var(--bx-space-3)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--bx-section)` horizontal padding
- **Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)`
- **Corner Radii**: `.25rem`, `50%`, `44px`, `16px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Marcellus`
- **Body Font Stack**: `Marcellus Fallback`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: CSS variables `--text-4xl: var(--bx-fs-display)`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-6xl: 3.75rem`; rule `h1` (`font-size: var(--bx-fs-statement)`, `line-height: var(--bx-lh-statement)`)
- **H2 Section Rule**: CSS variables `--text-3xl: var(--bx-fs-h2)`, `--text-3xl--line-height: calc(2.25 / 1.875)`, `--bx-fs-h2: clamp(32px, 3.6vw, 72px)`; rule `h2` (`font-size: var(--text-xl)`)
- **Body Copy Rule**: CSS variables `--leading-body: var(--bx-lh-body)`, `--bx-fs-body: 16px`, `--bx-lh-body: 1.6`; rule `p` (`font-size: var(--bx-fs-lead)`, `line-height: var(--bx-lh-body)`)
- **Metadata & Index Rule**: CSS variables `--font-mono: var(--bx-mono)`, `--text-xs: 14px`, `--text-sm: var(--bx-fs-small)`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `thebranx-com` (`The branding agency for startups, AI & SaaS - The Branx`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.bx-navbar> — `thebranx-com`)**:
   - DOM & Selectors: Landmark `<header class="bx-navbar">` hosting `The branding agency for startups, AI` navigation (`Brand identity · Web design & dev. · Strategy & messaging · Motion design · Product naming`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-ch2css="true"`, `data-bx-nav`), and stylesheet rule `llus_b0edf5b9-module__eeLBqG__cla... { font-family:Marcellus,Marcellus Fallback;font-style:normal;font-weight:400 }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.bx-navbar> — `thebranx-com`)` (`thebranx-com`) adapts across `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)` with `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(0.17,0,0.2,1)`, `cubic-bezier(0.5,0,0.83,1)` transitions and links `Brand identity · Web design & dev. · Strategy & messaging · Motion design · Product naming`.
2. **Hero Stage & Focal Lead (<section.bx-hero> — `The tech branding agency for AI & `)**:
   - DOM & Selectors: Landmark `<section class="bx-hero">` presenting display lead `The tech branding agency for AI & SaaS startups` and copy excerpt *"Strategy & messaging"* over `#fff085` canvas and `#4a5565` ink.
   - Responsive Contract: Hero stage (`1440×9398px` desktop / `390×2400px` mobile) sets `#fff085` background with `#4a5565` headline `The tech branding agency for AI & SaaS startups`.
3. **Primary Showcase & Content Grid (<section.bx-section> — `The Branx turns complex tech into `)**:
   - DOM & Selectors: Landmark `<section class="bx-section">` rendering section `The Branx turns complex tech into category-defini...` with copy *"The tech branding agency"*, asset references (`ec2f4458eb06f74e-s.p.217u6tza6bra...`, `0u5m-o-ck0mfs.css`, `3rz2zp8k1t-b-.css`, `194ug3jq7qzm9.js`), and grid rule `ellus_b0edf5b9-module__eeLBqG__va... { --font-marcellus:"Marcellus", "Marcellus Fallback" }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.bx-section> — `The Branx turns complex tech into `)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: var(--bx-space-3)`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--bx-section)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.bx-philosophy> — `AI made it easy to launch a brand.`)**:
   - DOM & Selectors: Landmark `<section class="bx-philosophy">` framing `AI made it easy to launch a brand. It made it har...` and `Start with the identity. Add the rest when you're...` (*"for AI & SaaS startups"*) with `#155dfc` surface cards, `#f9fafb` accents, and `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.bx-philosophy> — `AI made it easy to launch a brand.`)` uses `.25rem`, `50%`, `44px`, `16px` radii, `#f9fafb` highlights, and assets (ec2f4458eb06f74e-s.p.217u6tza6bra..., 0u5m-o-ck0mfs.css, 3rz2zp8k1t-b-.css).
5. **Colophon & Global Directory Footer (<footer.bx-footer> — `https://thebranx.com`)**:
   - DOM & Selectors: Landmark `<footer class="bx-footer">` anchoring `The branding agency for startups` footer links (`Brand identity · Web design & dev. · Strategy & messaging · Motion design · Product naming`), copy *"Video intelligence for the real world"*, and `#fff` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.bx-footer> — `https://thebranx.com`)` aligns to `40rem` extracted from `thebranx-com` stylesheet with `var(--bx-section)` lateral canvas padding with `var(--bx-space-3)` grid gap and attributes (data-precedence="next", data-precedence="next", data-ch2css="true").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Strategy & messaging"*
- Copy Excerpt 2: *"The tech branding agency"*
- Copy Excerpt 3: *"for AI & SaaS startups"*
- Copy Excerpt 4: *"Video intelligence for the real world"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(0.17,0,0.2,1)`, `cubic-bezier(0.5,0,0.83,1)`
- **Extracted Stylesheet Rules (`thebranx-com`)**:
- `llus_b0edf5b9-module__eeLBqG__cla... { font-family:Marcellus,Marcellus Fallback;font-style:normal;font-weight:400 }`
- `ellus_b0edf5b9-module__eeLBqG__va... { --font-marcellus:"Marcellus", "Marcellus Fallback" }`
- `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `strong { font-weight:bolder }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: .15s` extracted from `thebranx-com` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `thebranx-com` stylesheet.
- **Selector `body`**: `transition: background-color var(--bx-dur-slow) var(--bx-ease)` extracted from `thebranx-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<header.bx-navbar>` and `<section.bx-section>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `thebranx-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
