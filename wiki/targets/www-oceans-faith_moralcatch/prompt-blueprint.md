---
title: "UI Prompt Blueprint: www-oceans-faith_moralcatch"
date: 2026-11-15
target: "[[overview|www-oceans-faith_moralcatch]]"
status: analyzed
archetype: "Light-Substrate Editorial & Modular Grid System (`#ff0` canvas, `#000` ink, `#fff` accent)"
---

# UI Design System & Master Generation Blueprint: www-oceans-faith_moralcatch

> **The Moral Catch: Fisheries & Ocean Justice — Faiths for Oceans** (https://www.oceans.faith/moralcatch) — Explore fisheries, ocean life and workers’ rights. Read The Moral Catch report, take the two-minute meal test, and use the faith institut...

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/www-oceans-faith_moralcatch/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **The Moral Catch: Fisheries & Ocean Justice — Faiths for Oceans** (`https://www.oceans.faith/moralcatch`). Explore fisheries, ocean life and workers’ rights. Read The Moral Catch report, take the two-minute meal test, and use the faith institut...
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#ff0` canvas, `#000` ink, `#fff` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#ff0` (`mark { background: #ff0 }`) paired with `#000` primary typography and `#fff` accents.
  - **Extracted Typographic Hierarchy**: Pairs `squarespace-ui-font` for display copy (`Stay Connected`) with `Poppins` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `640px` container bounds (`gap: 10px`, padding `1.3rem`) with `cubic-bezier(.25,.46,.45,.94)` easing and GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/www-oceans-faith_moralcatch/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `640px` extracted from `www-oceans-faith_moralcatch` stylesheet.
- **Canvas Lateral Padding & Spacing**: `1.3rem` lateral canvas padding with `10px` grid gap.
- **Border Radius Scale**: `3px`, `14px`, `150px`, `0px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 640px`, `gap: 10px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `1.3rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width:640px)`, `@media (min-width:640px)`, `@media screen and (max-width: 432px)`, `@media screen and (min-width: 433px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#ff0` | `mark { background: #ff0 }` |
| **Primary Typography Ink** | `#000` | `mark { color: #000 }` |
| **Elevated Surface / Card Substrate** | `#c0c0c0` | `fieldset { border: silver }` (`#c0c0c0`) |
| **Interactive Accent / Highlight** | `#fff` | `.sqs-cookie-banner-v2.DARK a { color: #fff }` |
| **Secondary / Muted Copy** | `#777` | `ner-v2.DARK.TEXT .sqs-cookie-ba... { border-bottom: #777 }` |
| **Structural Hairline Border** | `#eee` | `.sqs-cookie-banner-v2.LIGHT { background-color: #eee }` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--white-hsl` | `0,100%,99.02%` | Canvas / Surface Token |
| `--sqsp-palette-lightest-color` | `hsla(0,100%,99.02%,1)` | Canvas / Surface Token |
| `--lightAccent-hsl` | `0,0%,96.08%` | Canvas / Surface Token |
| `--sqsp-palette-light-color` | `hsla(0,0%,96.08%,1)` | Canvas / Surface Token |
| `--accent-hsl` | `0,0%,85.1%` | Brand / Palette Token |
| `--sqsp-palette-accent-color` | `hsla(0,0%,85.1%,1)` | Brand / Palette Token |
| `--darkAccent-hsl` | `0,0%,47.45%` | Canvas / Surface Token |
| `--sqsp-palette-dark-color` | `hsla(0,0%,47.45%,1)` | Canvas / Surface Token |
| `--black-hsl` | `0,0%,0%` | Canvas / Surface Token |
| `--sqsp-palette-darkest-color` | `hsla(0,0%,0%,1)` | Canvas / Surface Token |
| `--safeLightAccent-hsl` | `0,0%,85.1%` | Canvas / Surface Token |
| `--safeDarkAccent-hsl` | `0,0%,0%` | Canvas / Surface Token |
| `--safeInverseAccent-hsl` | `0,0%,0%` | Brand / Palette Token |
| `--safeInverseLightAccent-hsl` | `0,0%,0%` | Canvas / Surface Token |
| `--safeInverseDarkAccent-hsl` | `0,0%,100%` | Canvas / Surface Token |
| `--course-item-nav-text-color` | `hsla(var(--black-hsl),1)` | Typography Ink Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `squarespace-ui-font`.
- **Primary Body Stack**: `Poppins`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--sqsp-heading-1-color: hsla(var(--black-hsl),1)`, `--heading-1-size: 4rem`, `--heading-1-size-value: 4`; rule `.title` (`letter-spacing: .5px`, `font-weight: 500`).
- **Section Heading (`H2`)**: CSS variables `--image-block-collage-image-subtitle-color: hsla(var(--black-hsl),1)`, `--image-block-card-image-subtitle-color: hsla(var(--black-hsl),1)`, `--image-block-poster-image-subtitle-color: hsla(var(--white-hsl),1)`.
- **Body Copy**: CSS variables `--paragraphSmallColor: hsla(var(--black-hsl),1)`, `--sqsp-paragraph-3-color: hsla(var(--black-hsl),1)`, `--paragraphLargeColor: hsla(var(--black-hsl),1)`; rule `p` (`font-size: 14px`, `line-height: 1.5em`).
- **Metadata & Navigation Labels**: CSS variables `--paragraphSmallColor: hsla(var(--black-hsl),1)`, `--tweak-paragraph-small-color-on-background: hsla(var(--black-hsl),1)`, `--tweak-form-block-caption-color-on-background: hsla(var(--black-hsl),1)`; rule `.caption` (`font-size: 12px`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.25,.46,.45,.94)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.19,1,.22,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.sqs-image-zoom-duplicate`**: `transition: opacity .4s ease` extracted from `www-oceans-faith_moralcatch` stylesheet.
- **Selector `.sqs-system-error input`**: `transition: background-color .1s ease-in-out, opacity .1s ease-in-out` extracted from `www-oceans-faith_moralcatch` stylesheet.
- **Selector `.sqsp-tooltip .buttons a:not(.rej...`**: `transition: background-color .1s ease-in-out, opacity .1s ease-in-out` extracted from `www-oceans-faith_moralcatch` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.25,.46,.45,.94)`)**: Governs interactive state transitions across `<header.bright-inverse>` and `<section.region>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — The Moral Catch: Fisheries & Ocean Justice │
│ ====================================================================== │
│ [ <header.bright-inverse>  | SIGN THE DECLARATION · SIGNATORIES · P ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <article.page-regions>                               |   │
│ | H1: Stay Connected                                               |   │
│ | Substrate: #ff0       | Ink: #000       | Accent: #fff           |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.region>          ) max-w: 640px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | HIGH AMBITION COALITION      |  | MULTI-FAITH DECLARATION      | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 10px  ) | │
│ | [<header.bright-inv] -> [<article.page-regi] -> [<section.region>] | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.sections>     ) | https://www.oceans.faith/moralcatc │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.bright-inverse> — `www-oceans-faith_moralcatch`)**:
   - Landmark `<header class="bright-inverse header">` hosting `The Moral Catch: Fisheries & Ocean J` navigation (`SIGN THE DECLARATION · SIGNATORIES · POLICY PRIMERS · GLOSSARY · REPORT`), DOM attributes (`data-sqsp-font-ids="6a3139e4691a2d058d1a1..."`, `data-name="static-context"`, `data-animation-state="booted"`, `data-test="header"`), and stylesheet rule `summary { display:block }`.
2. **Hero Stage & Focal Lead (<article.page-regions> — `Stay Connected`)**:
   - Landmark `<article class="page-regions">` presenting display lead `Stay Connected` and copy excerpt *"HIGH AMBITION COALITION"* over `#ff0` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.region> — `HIGH AMBITION COALITION`)**:
   - Landmark `<section class="region">` rendering section `HIGH AMBITION COALITION` with copy *"MULTI-FAITH DECLARATION"*, asset references (`popup-overlay-f39ec8cdc95ccd84-mi...`, `popup-overlay-7afaba259a8e252a-mi...`, `favicon.ico`, `moralcatch`), and grid rule `video { display:inline-block }`.
4. **Interactive Detail & Feature Matrix (<section.page-section> — `MULTI-FAITH DECLARATION`)**:
   - Landmark `<section class="page-section full-bleed-section">` framing `MULTI-FAITH DECLARATION` and `SIGN THE DECLARATION` (*"SIGN THE DECLARATION"*) with `#c0c0c0` surface cards, `#fff` accents, and `template { display:none }`.
5. **Colophon & Global Directory Footer (<footer.sections> — `https://www.oceans.faith/moralcatch`)**:
   - Landmark `<footer class="sections">` anchoring `The Moral Catch: Fisheries & Oce` footer links (`SIGN THE DECLARATION · SIGNATORIES · POLICY PRIMERS · GLOSSARY · REPORT`), copy *"OCEAN INTERFAITH FORUM"*, and `#eee` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-oceans-faith_moralcatch (The Moral Catch: Fisheries & Ocean Justice — Faiths for Oceans)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-oceans-faith_moralcatch` (**The Moral Catch: Fisheries & Ocean Justice — Faiths for Oceans** — `https://www.oceans.faith/moralcatch`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#ff0` canvas, `#000` ink, `#fff` accent).
- **Identity & Domain Context**: Explore fisheries, ocean life and workers’ rights. Read The Moral Catch report, take the two-minute meal test, and use the faith institut...
- **Primary Substrate**: `#ff0` (`mark { background: #ff0 }`), **Primary Ink**: `#000`, **Accent / Highlight**: `#fff`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#ff0` (`mark { background: #ff0 }`) paired with `#000` primary typography and `#fff` accents.
  - **Extracted Typographic Hierarchy**: Pairs `squarespace-ui-font` for display copy (`Stay Connected`) with `Poppins` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `640px` container bounds (`gap: 10px`, padding `1.3rem`) with `cubic-bezier(.25,.46,.45,.94)` easing and GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-oceans-faith_moralcatch` in your global stylesheet:

:root {
  /* The Moral Catch: Fisheries & Ocean Justice — Faiths for Oceans (www-oceans-faith_moralcatch) — Ground-Truth Extracted CSS Variables */
  --white-hsl: 0,100%,99.02%; /* Canvas / Surface Token (www-oceans-faith_moralcatch) */
  --sqsp-palette-lightest-color: hsla(0,100%,99.02%,1); /* Canvas / Surface Token (www-oceans-faith_moralcatch) */
  --lightAccent-hsl: 0,0%,96.08%; /* Canvas / Surface Token (www-oceans-faith_moralcatch) */
  --sqsp-palette-light-color: hsla(0,0%,96.08%,1); /* Canvas / Surface Token (www-oceans-faith_moralcatch) */
  --accent-hsl: 0,0%,85.1%; /* Brand / Palette Token (www-oceans-faith_moralcatch) */
  --sqsp-palette-accent-color: hsla(0,0%,85.1%,1); /* Brand / Palette Token (www-oceans-faith_moralcatch) */
  --darkAccent-hsl: 0,0%,47.45%; /* Canvas / Surface Token (www-oceans-faith_moralcatch) */
  --sqsp-palette-dark-color: hsla(0,0%,47.45%,1); /* Canvas / Surface Token (www-oceans-faith_moralcatch) */
  --black-hsl: 0,0%,0%; /* Canvas / Surface Token (www-oceans-faith_moralcatch) */
  --sqsp-palette-darkest-color: hsla(0,0%,0%,1); /* Canvas / Surface Token (www-oceans-faith_moralcatch) */
  --safeLightAccent-hsl: 0,0%,85.1%; /* Canvas / Surface Token (www-oceans-faith_moralcatch) */
  --safeDarkAccent-hsl: 0,0%,0%; /* Canvas / Surface Token (www-oceans-faith_moralcatch) */
  --safeInverseAccent-hsl: 0,0%,0%; /* Brand / Palette Token (www-oceans-faith_moralcatch) */
  --safeInverseLightAccent-hsl: 0,0%,0%; /* Canvas / Surface Token (www-oceans-faith_moralcatch) */
  --safeInverseDarkAccent-hsl: 0,0%,100%; /* Canvas / Surface Token (www-oceans-faith_moralcatch) */
  --course-item-nav-text-color: hsla(var(--black-hsl),1); /* Typography Ink Token (www-oceans-faith_moralcatch) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ff0` — grounded in `mark { background: #ff0 }`
- **Primary Typography Ink**: `#000` — grounded in `mark { color: #000 }`
- **Elevated Surface / Card Substrate**: `#c0c0c0` — grounded in `fieldset { border: silver }` (`#c0c0c0`)
- **Interactive Accent / Highlight**: `#fff` — grounded in `.sqs-cookie-banner-v2.DARK a { color: #fff }`
- **Secondary / Muted Copy**: `#777` — grounded in `ner-v2.DARK.TEXT .sqs-cookie-ba... { border-bottom: #777 }`
- **Structural Hairline Border**: `#eee` — grounded in `.sqs-cookie-banner-v2.LIGHT { background-color: #eee }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `640px` extracted from `www-oceans-faith_moralcatch` stylesheet
- **Padding & Gutters**: `1.3rem` lateral canvas padding with `10px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 640px`, `gap: 10px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `1.3rem` horizontal padding
- **Media Queries**: `@media (max-width:640px)`, `@media (min-width:640px)`, `@media screen and (max-width: 432px)`, `@media screen and (min-width: 433px)`
- **Corner Radii**: `3px`, `14px`, `150px`, `0px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `squarespace-ui-font`
- **Body Font Stack**: `Poppins`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: CSS variables `--sqsp-heading-1-color: hsla(var(--black-hsl),1)`, `--heading-1-size: 4rem`, `--heading-1-size-value: 4`; rule `.title` (`letter-spacing: .5px`, `font-weight: 500`)
- **H2 Section Rule**: CSS variables `--image-block-collage-image-subtitle-color: hsla(var(--black-hsl),1)`, `--image-block-card-image-subtitle-color: hsla(var(--black-hsl),1)`, `--image-block-poster-image-subtitle-color: hsla(var(--white-hsl),1)`
- **Body Copy Rule**: CSS variables `--paragraphSmallColor: hsla(var(--black-hsl),1)`, `--sqsp-paragraph-3-color: hsla(var(--black-hsl),1)`, `--paragraphLargeColor: hsla(var(--black-hsl),1)`; rule `p` (`font-size: 14px`, `line-height: 1.5em`)
- **Metadata & Index Rule**: CSS variables `--paragraphSmallColor: hsla(var(--black-hsl),1)`, `--tweak-paragraph-small-color-on-background: hsla(var(--black-hsl),1)`, `--tweak-form-block-caption-color-on-background: hsla(var(--black-hsl),1)`; rule `.caption` (`font-size: 12px`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-oceans-faith_moralcatch` (`The Moral Catch: Fisheries & Ocean Justice — Faiths for Oceans`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.bright-inverse> — `www-oceans-faith_moralcatch`)**:
   - DOM & Selectors: Landmark `<header class="bright-inverse header">` hosting `The Moral Catch: Fisheries & Ocean J` navigation (`SIGN THE DECLARATION · SIGNATORIES · POLICY PRIMERS · GLOSSARY · REPORT`), DOM attributes (`data-sqsp-font-ids="6a3139e4691a2d058d1a1..."`, `data-name="static-context"`, `data-animation-state="booted"`, `data-test="header"`), and stylesheet rule `summary { display:block }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.bright-inverse> — `www-oceans-faith_moralcatch`)` (`www-oceans-faith_moralcatch`) adapts across `@media (max-width:640px)`, `@media (min-width:640px)`, `@media screen and (max-width: 432px)`, `@media screen and (min-width: 433px)` with `cubic-bezier(.25,.46,.45,.94)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.19,1,.22,1)` transitions and links `SIGN THE DECLARATION · SIGNATORIES · POLICY PRIMERS · GLOSSARY · REPORT`.
2. **Hero Stage & Focal Lead (<article.page-regions> — `Stay Connected`)**:
   - DOM & Selectors: Landmark `<article class="page-regions">` presenting display lead `Stay Connected` and copy excerpt *"HIGH AMBITION COALITION"* over `#ff0` canvas and `#000` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#ff0` background with `#000` headline `Stay Connected`.
3. **Primary Showcase & Content Grid (<section.region> — `HIGH AMBITION COALITION`)**:
   - DOM & Selectors: Landmark `<section class="region">` rendering section `HIGH AMBITION COALITION` with copy *"MULTI-FAITH DECLARATION"*, asset references (`popup-overlay-f39ec8cdc95ccd84-mi...`, `popup-overlay-7afaba259a8e252a-mi...`, `favicon.ico`, `moralcatch`), and grid rule `video { display:inline-block }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.region> — `HIGH AMBITION COALITION`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 640px`, `gap: 10px`) on desktop and Single-column vertical stack at `390px` viewport width with `1.3rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.page-section> — `MULTI-FAITH DECLARATION`)**:
   - DOM & Selectors: Landmark `<section class="page-section full-bleed-section">` framing `MULTI-FAITH DECLARATION` and `SIGN THE DECLARATION` (*"SIGN THE DECLARATION"*) with `#c0c0c0` surface cards, `#fff` accents, and `template { display:none }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.page-section> — `MULTI-FAITH DECLARATION`)` uses `3px`, `14px`, `150px`, `0px` radii, `#fff` highlights, and assets (popup-overlay-f39ec8cdc95ccd84-mi..., popup-overlay-7afaba259a8e252a-mi..., favicon.ico).
5. **Colophon & Global Directory Footer (<footer.sections> — `https://www.oceans.faith/moralcatch`)**:
   - DOM & Selectors: Landmark `<footer class="sections">` anchoring `The Moral Catch: Fisheries & Oce` footer links (`SIGN THE DECLARATION · SIGNATORIES · POLICY PRIMERS · GLOSSARY · REPORT`), copy *"OCEAN INTERFAITH FORUM"*, and `#eee` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.sections> — `https://www.oceans.faith/moralcatch`)` aligns to `640px` extracted from `www-oceans-faith_moralcatch` stylesheet with `1.3rem` lateral canvas padding with `10px` grid gap and attributes (data-sqsp-font-ids="6a3139e4691a2d058d1a1...", data-name="static-context", data-animation-state="booted").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"HIGH AMBITION COALITION"*
- Copy Excerpt 2: *"MULTI-FAITH DECLARATION"*
- Copy Excerpt 3: *"SIGN THE DECLARATION"*
- Copy Excerpt 4: *"OCEAN INTERFAITH FORUM"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.25,.46,.45,.94)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.19,1,.22,1)`
- **Extracted Stylesheet Rules (`www-oceans-faith_moralcatch`)**:
- `summary { display:block }`
- `video { display:inline-block }`
- `template { display:none }`
- `html { font-family:sans-serif;-ms-text-size-adjust:100%;-webkit-text-size-adjus... }`
- `a:focus { outline:thin dotted }`
- **Per-Selector Transition Rules**:
- **Selector `.sqs-image-zoom-duplicate`**: `transition: opacity .4s ease` extracted from `www-oceans-faith_moralcatch` stylesheet.
- **Selector `.sqs-system-error input`**: `transition: background-color .1s ease-in-out, opacity .1s ease-in-out` extracted from `www-oceans-faith_moralcatch` stylesheet.
- **Selector `.sqsp-tooltip .buttons a:not(.rej...`**: `transition: background-color .1s ease-in-out, opacity .1s ease-in-out` extracted from `www-oceans-faith_moralcatch` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.25,.46,.45,.94)`)**: Governs interactive state transitions across `<header.bright-inverse>` and `<section.region>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Barba.js Page Transition Router with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-oceans-faith_moralcatch`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
