---
title: "UI Prompt Blueprint: www-hollywoodexhibit2026-com"
date: 2026-11-15
target: "[[overview|www-hollywoodexhibit2026-com]]"
status: analyzed
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#000000`)"
---

# UI Design System & Master Generation Blueprint: www-hollywoodexhibit2026-com

> **ELLE & Esquire, The New Hollywood Photography Exhibition** (https://www.hollywoodexhibit2026.com) — Hearst Galleries presented a joint photography exhibition for ELLE and Esquire, ELLE: The New Hollywood and Esquire Goes to Hollywood, fe...

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/www-hollywoodexhibit2026-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **ELLE & Esquire, The New Hollywood Photography Exhibition** (`https://www.hollywoodexhibit2026.com`). Hearst Galleries presented a joint photography exhibition for ELLE and Esquire, ELLE: The New Hollywood and Esquire Goes to Hollywood, fe...
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#000000`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--color-black)` in `:root`) paired with `#fff` primary typography and `#000000` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Instrument Sans` for display copy (`THE ELLE ESQUIRE HOLLYWOOD`) with `Instrument Sans Fallback` and `safiraMarch`.
  - **Calibrated Spatial Grid & Motion**: Combines `40rem` container bounds (`gap: 0px (flush layout)`, padding `0px`) with `cubic-bezier(.4,0,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/www-hollywoodexhibit2026-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `40rem` extracted from `www-hollywoodexhibit2026-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `0px` lateral canvas padding with `0px (flush layout)` grid gap.
- **Border Radius Scale**: `var(--radius-8)`, `var(--radius-full)`, `50%`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: 0px (flush layout)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `0px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#0000` | `textarea { background-color: #0000 }` |
| **Interactive Accent / Highlight** | `#000000` | `.border-black { border-color: black }` (`#000000`) |
| **Secondary / Muted Copy** | `#ffffff` | `50 { border-color: white }` (`#ffffff`) |
| **Structural Hairline Border** | `#fff3` | `20 { background-color: #fff3 }` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--spacing` | `.0625rem` | Layout / Spatial Grid Token |
| `--font-weight-light` | `300` | Canvas / Surface Token |
| `--animate-spin` | `spin 1s linear infinite` | Motion / Easing Token |
| `--default-transition-duration` | `.15s` | Motion / Easing Token |
| `--default-transition-timing-function` | `cubic-bezier(.4,0,.2,1)` | Motion / Easing Token |
| `--fluid-min-w` | `var(--layout-min-w,375)` | Design System Custom Token |
| `--fluid-max-w` | `var(--layout-max-w,1920)` | Layout / Spatial Grid Token |
| `--text-label--font-weight` | `400` | Typography Ink Token |
| `--text-label--line-height` | `1` | Typography Ink Token |
| `--text-label--letter-spacing` | `.03em` | Typography Ink Token |
| `--text-body-10--font-weight` | `400` | Typography Ink Token |
| `--text-body-10--line-height` | `1.25` | Typography Ink Token |
| `--text-body-10--letter-spacing` | `-2%` | Typography Ink Token |
| `--text-headline-10--font-weight` | `400` | Typography Ink Token |
| `--text-headline-10--line-height` | `1` | Typography Ink Token |
| `--text-headline-10--letter-spacing` | `normal` | Typography Ink Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Instrument Sans`.
- **Primary Body Stack**: `Instrument Sans Fallback`.
- **Technical / Metadata Stack**: `safiraMarch`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `var(--text-headline-10)`, `var(--text-headline-18)`).
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `var(--text-headline-10)`, `var(--text-headline-18)`).
- **Body Copy**: CSS variables `--text-body-10--font-weight: 400`, `--text-body-10--line-height: 1.25`, `--text-body-10--letter-spacing: -2%`.
- **Metadata & Navigation Labels**: CSS variables `--text-label--font-weight: 400`, `--text-label--line-height: 1`, `--text-label--letter-spacing: .03em`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.39,.57,.56,1)`, `cubic-bezier(.77,0,.18,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: .15s` extracted from `www-hollywoodexhibit2026-com` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `www-hollywoodexhibit2026-com` stylesheet.
- **Selector `.transition-colors`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `www-hollywoodexhibit2026-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<header.wf-ivyprestodisplay-n3-active>` and `<main.wf-helveticaltpro-i7-active>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — ELLE & Esquire, The New Hollywood Photogra │
│ ====================================================================== │
│ [ <header.wf-ivyprestodisp | Overview · Index · Archive · About · C ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <main.wf-ivyprestodisplay-i3-active>                 |   │
│ | H1: THE ELLE ESQUIRE HOLLYWOOD                                   |   │
│ | Substrate: #000       | Ink: #fff       | Accent: #000000        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<main.wf-helveticaltpro-i7) max-w: 40rem          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | THE ELLE ESQUIRE HOLLYWOOD   |  | As seen in the Hearst Tower, | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 0px (f) | │
│ | [<header.wf-ivypres] -> [<main.wf-ivypresto] -> [<main.wf-helvetica] │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.wf-helveticalt) | https://www.hollywoodexhibit2026.c │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.wf-ivyprestodisplay-n3-active> — `www-hollywoodexhibit2026-com`)**:
   - Landmark `<header class="wf-ivyprestodisplay-n3-active">` hosting `ELLE & Esquire, The New Hollywood Ph` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-engine="three.js r182"`, `data-nscript="afterInteractive"`, `data-nscript="afterInteractive"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<main.wf-ivyprestodisplay-i3-active> — `THE ELLE ESQUIRE HOLLYWOOD`)**:
   - Landmark `<main class="wf-ivyprestodisplay-i3-active">` presenting display lead `THE ELLE ESQUIRE HOLLYWOOD` and copy excerpt *"THE ELLE ESQUIRE HOLLYWOOD"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<main.wf-helveticaltpro-i7-active> — `THE ELLE ESQUIRE HOLLYWOOD`)**:
   - Landmark `<main class="wf-helveticaltpro-i7-active">` rendering section `THE ELLE ESQUIRE HOLLYWOOD` with copy *"As seen in the Hearst Tower, located in"*, asset references (`ABCArizonaVariable-s.p.6844b0f6.w...`, `Haigrast-s.p.42f2de84.woff2`, `IvyPrestoHeadline_Thin-s.p.830ff3...`, `IvyPrestoText_Thin-s.p.3ba47ad4.w...`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<main.wf-helveticaltpro-i4-active> — `As seen in the Hearst Tower, locat`)**:
   - Landmark `<main class="wf-helveticaltpro-i4-active">` framing `As seen in the Hearst Tower, located in` and `www-hollywoodexhibit2026-com Archive & Directory` (*"THE ELLE ESQUIRE HOLLYWOOD"*) with `#0000` surface cards, `#000000` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.wf-helveticaltpro-n7-active> — `https://www.hollywoodexhibit2026.com`)**:
   - Landmark `<footer class="wf-helveticaltpro-n7-active">` anchoring `ELLE & Esquire, The New Hollywoo` footer links (`Overview · Index · Archive · About · Contact`), copy *"As seen in the Hearst Tower, located in"*, and `#fff3` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-hollywoodexhibit2026-com (ELLE & Esquire, The New Hollywood Photography Exhibition)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-hollywoodexhibit2026-com` (**ELLE & Esquire, The New Hollywood Photography Exhibition** — `https://www.hollywoodexhibit2026.com`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#000000`).
- **Identity & Domain Context**: Hearst Galleries presented a joint photography exhibition for ELLE and Esquire, ELLE: The New Hollywood and Esquire Goes to Hollywood, fe...
- **Primary Substrate**: `#000` (`var(--color-black)` in `:root`), **Primary Ink**: `#fff`, **Accent / Highlight**: `#000000`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--color-black)` in `:root`) paired with `#fff` primary typography and `#000000` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Instrument Sans` for display copy (`THE ELLE ESQUIRE HOLLYWOOD`) with `Instrument Sans Fallback` and `safiraMarch`.
  - **Calibrated Spatial Grid & Motion**: Combines `40rem` container bounds (`gap: 0px (flush layout)`, padding `0px`) with `cubic-bezier(.4,0,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-hollywoodexhibit2026-com` in your global stylesheet:

:root {
  /* ELLE & Esquire, The New Hollywood Photography Exhibition (www-hollywoodexhibit2026-com) — Ground-Truth Extracted CSS Variables */
  --spacing: .0625rem; /* Layout / Spatial Grid Token (www-hollywoodexhibit2026-com) */
  --font-weight-light: 300; /* Canvas / Surface Token (www-hollywoodexhibit2026-com) */
  --animate-spin: spin 1s linear infinite; /* Motion / Easing Token (www-hollywoodexhibit2026-com) */
  --default-transition-duration: .15s; /* Motion / Easing Token (www-hollywoodexhibit2026-com) */
  --default-transition-timing-function: cubic-bezier(.4,0,.2,1); /* Motion / Easing Token (www-hollywoodexhibit2026-com) */
  --fluid-min-w: var(--layout-min-w,375); /* Design System Custom Token (www-hollywoodexhibit2026-com) */
  --fluid-max-w: var(--layout-max-w,1920); /* Layout / Spatial Grid Token (www-hollywoodexhibit2026-com) */
  --text-label--font-weight: 400; /* Typography Ink Token (www-hollywoodexhibit2026-com) */
  --text-label--line-height: 1; /* Typography Ink Token (www-hollywoodexhibit2026-com) */
  --text-label--letter-spacing: .03em; /* Typography Ink Token (www-hollywoodexhibit2026-com) */
  --text-body-10--font-weight: 400; /* Typography Ink Token (www-hollywoodexhibit2026-com) */
  --text-body-10--line-height: 1.25; /* Typography Ink Token (www-hollywoodexhibit2026-com) */
  --text-body-10--letter-spacing: -2%; /* Typography Ink Token (www-hollywoodexhibit2026-com) */
  --text-headline-10--font-weight: 400; /* Typography Ink Token (www-hollywoodexhibit2026-com) */
  --text-headline-10--line-height: 1; /* Typography Ink Token (www-hollywoodexhibit2026-com) */
  --text-headline-10--letter-spacing: normal; /* Typography Ink Token (www-hollywoodexhibit2026-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#000` — grounded in `var(--color-black)` in `:root`
- **Primary Typography Ink**: `#fff` — grounded in `var(--color-white)` in `:root`
- **Elevated Surface / Card Substrate**: `#0000` — grounded in `textarea { background-color: #0000 }`
- **Interactive Accent / Highlight**: `#000000` — grounded in `.border-black { border-color: black }` (`#000000`)
- **Secondary / Muted Copy**: `#ffffff` — grounded in `50 { border-color: white }` (`#ffffff`)
- **Structural Hairline Border**: `#fff3` — grounded in `20 { background-color: #fff3 }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `40rem` extracted from `www-hollywoodexhibit2026-com` stylesheet
- **Padding & Gutters**: `0px` lateral canvas padding with `0px (flush layout)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: 0px (flush layout)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `0px` horizontal padding
- **Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)`
- **Corner Radii**: `var(--radius-8)`, `var(--radius-full)`, `50%`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Instrument Sans`
- **Body Font Stack**: `Instrument Sans Fallback`
- **Monospace / Technical Font Stack**: `safiraMarch`
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `var(--text-headline-10)`, `var(--text-headline-18)`)
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `var(--text-headline-10)`, `var(--text-headline-18)`)
- **Body Copy Rule**: CSS variables `--text-body-10--font-weight: 400`, `--text-body-10--line-height: 1.25`, `--text-body-10--letter-spacing: -2%`
- **Metadata & Index Rule**: CSS variables `--text-label--font-weight: 400`, `--text-label--line-height: 1`, `--text-label--letter-spacing: .03em`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-hollywoodexhibit2026-com` (`ELLE & Esquire, The New Hollywood Photography Exhibition`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.wf-ivyprestodisplay-n3-active> — `www-hollywoodexhibit2026-com`)**:
   - DOM & Selectors: Landmark `<header class="wf-ivyprestodisplay-n3-active">` hosting `ELLE & Esquire, The New Hollywood Ph` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-engine="three.js r182"`, `data-nscript="afterInteractive"`, `data-nscript="afterInteractive"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.wf-ivyprestodisplay-n3-active> — `www-hollywoodexhibit2026-com`)` (`www-hollywoodexhibit2026-com`) adapts across `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)` with `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.39,.57,.56,1)`, `cubic-bezier(.77,0,.18,1)` transitions and links `Overview · Index · Archive · About · Contact`.
2. **Hero Stage & Focal Lead (<main.wf-ivyprestodisplay-i3-active> — `THE ELLE ESQUIRE HOLLYWOOD`)**:
   - DOM & Selectors: Landmark `<main class="wf-ivyprestodisplay-i3-active">` presenting display lead `THE ELLE ESQUIRE HOLLYWOOD` and copy excerpt *"THE ELLE ESQUIRE HOLLYWOOD"* over `#000` canvas and `#fff` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#000` background with `#fff` headline `THE ELLE ESQUIRE HOLLYWOOD`.
3. **Primary Showcase & Content Grid (<main.wf-helveticaltpro-i7-active> — `THE ELLE ESQUIRE HOLLYWOOD`)**:
   - DOM & Selectors: Landmark `<main class="wf-helveticaltpro-i7-active">` rendering section `THE ELLE ESQUIRE HOLLYWOOD` with copy *"As seen in the Hearst Tower, located in"*, asset references (`ABCArizonaVariable-s.p.6844b0f6.w...`, `Haigrast-s.p.42f2de84.woff2`, `IvyPrestoHeadline_Thin-s.p.830ff3...`, `IvyPrestoText_Thin-s.p.3ba47ad4.w...`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<main.wf-helveticaltpro-i7-active> — `THE ELLE ESQUIRE HOLLYWOOD`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: 0px (flush layout)`) on desktop and Single-column vertical stack at `390px` viewport width with `0px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<main.wf-helveticaltpro-i4-active> — `As seen in the Hearst Tower, locat`)**:
   - DOM & Selectors: Landmark `<main class="wf-helveticaltpro-i4-active">` framing `As seen in the Hearst Tower, located in` and `www-hollywoodexhibit2026-com Archive & Directory` (*"THE ELLE ESQUIRE HOLLYWOOD"*) with `#0000` surface cards, `#000000` accents, and `strong { font-weight:bolder }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<main.wf-helveticaltpro-i4-active> — `As seen in the Hearst Tower, locat`)` uses `var(--radius-8)`, `var(--radius-full)`, `50%` radii, `#000000` highlights, and assets (ABCArizonaVariable-s.p.6844b0f6.w..., Haigrast-s.p.42f2de84.woff2, IvyPrestoHeadline_Thin-s.p.830ff3...).
5. **Colophon & Global Directory Footer (<footer.wf-helveticaltpro-n7-active> — `https://www.hollywoodexhibit2026.com`)**:
   - DOM & Selectors: Landmark `<footer class="wf-helveticaltpro-n7-active">` anchoring `ELLE & Esquire, The New Hollywoo` footer links (`Overview · Index · Archive · About · Contact`), copy *"As seen in the Hearst Tower, located in"*, and `#fff3` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.wf-helveticaltpro-n7-active> — `https://www.hollywoodexhibit2026.com`)` aligns to `40rem` extracted from `www-hollywoodexhibit2026-com` stylesheet with `0px` lateral canvas padding with `0px (flush layout)` grid gap and attributes (data-precedence="next", data-engine="three.js r182", data-nscript="afterInteractive").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"THE ELLE ESQUIRE HOLLYWOOD"*
- Copy Excerpt 2: *"As seen in the Hearst Tower, located in"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.39,.57,.56,1)`, `cubic-bezier(.77,0,.18,1)`
- **Extracted Stylesheet Rules (`www-hollywoodexhibit2026-com`)**:
- `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `strong { font-weight:bolder }`
- `small { font-size:80% }`
- `sup { vertical-align:baseline;font-size:75%;line-height:0;position:relative }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: .15s` extracted from `www-hollywoodexhibit2026-com` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `www-hollywoodexhibit2026-com` stylesheet.
- **Selector `.transition-colors`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `www-hollywoodexhibit2026-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<header.wf-ivyprestodisplay-n3-active>` and `<main.wf-helveticaltpro-i7-active>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-hollywoodexhibit2026-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
