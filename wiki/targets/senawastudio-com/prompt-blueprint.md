---
title: "UI Prompt Blueprint: senawastudio-com"
date: 2026-11-15
target: "senawastudio-com"
status: analyzed
capture: dom
capture_desktop: dom
capture_mobile: dom
archetype: "Light-Substrate Editorial & Modular Grid System (`#f6f2eb` canvas, `#302620` ink, `#a8967e` accent)"
---

# UI Design System & Master Generation Blueprint: senawastudio-com

> **Senawa · Architecture & Interior Design Studio in Jakarta** (https://senawastudio.com) — Architecture made for how people actually live. An architecture, interior, and furniture design studio in the Greater Jakarta area.

![Desktop Viewport Capture](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Senawa · Architecture & Interior Design Studio in Jakarta** (`https://senawastudio.com`). Architecture made for how people actually live. An architecture, interior, and furniture design studio in the Greater Jakarta area.
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#f6f2eb` canvas, `#302620` ink, `#a8967e` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#f6f2eb` (`var(--wool)` in `:root`) paired with `#302620` primary typography and `#a8967e` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Inter` for display copy (`Senawa, Architecture & Interior Desi`) with `Inter Fallback` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `560px` container bounds (`gap: 16px`, padding `48px`) with `cubic-bezier(.4,0,.2,1)` easing.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `560px` extracted from `senawastudio-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `48px` lateral canvas padding with `16px` grid gap.
- **Border Radius Scale**: `3px`, `var(--radius-sm)`, `var(--radius-md)`, `4px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 560px`, `gap: 16px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `48px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (min-width:1024px) and (max-height:860px)`, `@media (max-width:1023px)`, `@media (max-width:767px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#f6f2eb` | `var(--wool)` in `:root` |
| **Primary Typography Ink** | `#ede6d8` | `var(--linen)` in `:root` |
| **Elevated Surface / Card Substrate** | `#d4c9b4` | `var(--sand)` in `:root` |
| **Interactive Accent / Highlight** | `#a8967e` | `var(--oak)` in `:root` |
| **Secondary / Muted Copy** | `#6b5a48` | `var(--walnut)` in `:root` |
| **Structural Hairline Border** | `#302620` | `var(--slate)` in `:root` |
| **Variable Token (`--s-dim`)** | `#302620b8` | `var(--s-dim)` in `:root` |
| **Variable Token (`--s-line`)** | `#30262024` | `var(--s-line)` in `:root` |
| **Variable Token (`--b-ink-soft`)** | `#302620b3` | `var(--b-ink-soft)` in `:root` |
| **Variable Token (`--b-ink-faint`)** | `#30262057` | `var(--b-ink-faint)` in `:root` |
| **Variable Token (`--b-line-wake`)** | `#30262038` | `var(--b-line-wake)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-sans` | `"Inter", "Inter Fallback"` | Typography / Scale Token |
| `--font-sora` | `"Sora", "Sora Fallback"` | Typography / Scale Token |
| `--s-dim` | `#302620b8` | Color / Atmospheric Token |
| `--s-dim2` | `#302620b8` | Color / Atmospheric Token |
| `--s-line` | `#30262024` | Color / Atmospheric Token |
| `--studio-ink` | `82, 80, 80` | Typography Ink Token |
| `--b-ease` | `var(--ease-out,cubic-bezier(.16, 1, .3, 1))` | Motion / Easing Token |
| `--b-ink` | `var(--slate)` | Typography Ink Token |
| `--b-ink-soft` | `#302620b3` | Typography Ink Token |
| `--b-ink-faint` | `#30262057` | Typography Ink Token |
| `--b-line-wake` | `#30262038` | Color / Atmospheric Token |
| `--b-dot` | `var(--slate)` | Design System Custom Token |
| `--b-t-slow` | `.84s` | Motion / Timing Token |
| `--b-t-mid` | `var(--duration-mid)` | Design System Custom Token |
| `--crop-ease` | `var(--ease-out)` | Motion / Easing Token |
| `--wool` | `#f6f2eb` | Color / Atmospheric Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Inter`.
- **Primary Body Stack**: `Inter Fallback`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--font-display: var(--font-sora), "Sora", var(--font-sans), "Helvetica Neue", sans-serif`.
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `10px`, `clamp(1.25rem,1.7vw,1.625rem)`, `12px`, `13px`, `clamp(.9375rem,1vw,1.0625rem)`).
- **Body Copy**: CSS variables `--font-body: var(--font-sans), "Inter", "Helvetica Neue", sans-serif`, `--leading-body: 1.75`; rule `p` (`font-size: clamp(.9375rem,1vw,1.0625rem)`, `line-height: var(--leading-body)`, `font-weight: 300`).
- **Metadata & Navigation Labels**: CSS variables `--color-text-caption: var(--slate)`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.33,1,.68,1)`, `cubic-bezier(.5,1,.89,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.PageTransition-module__kKDxmW__c...`**: `transition: opacity .45s cubic-bezier(.4,0,.2,1)` extracted from `senawastudio-com` stylesheet.
- **Selector `.PageTransition-module__kKDxmW__r...`**: `transition: opacity .55s cubic-bezier(.4,0,.2,1)` extracted from `senawastudio-com` stylesheet.
- **Selector `.PageTransition-module__kKDxmW__mark`**: `transition: opacity .45s cubic-bezier(.4,0,.2,1),transform .45s cubic-bezi...` extracted from `senawastudio-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<nav.Nav-module__bLoQaq__nav>` and `<section.skip-link>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<section.antialiased>` and `<section.skip-link>` interactive targets.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Senawa · Architecture & Interior Design St │
│ ====================================================================== │
│ [ <nav.Nav-module__bLoQaq_ | Overview · Index · Archive · About · C ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.antialiased>                                |   │
│ | H1: Senawa, Architecture & Interior Design Studio in...          |   │
│ | Substrate: #f6f2eb    | Ink: #302620    | Accent: #a8967e        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.skip-link>       ) max-w: 560px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | contact.senawastudio@gmail.c |  | BSD, Tangerang Selatan       | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 16px  ) | │
│ | [<nav.Nav-module__b] -> [<section.antialias] -> [<section.skip-link] │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.Nav-module__bL) | https://senawastudio.com           │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.Nav-module__bLoQaq__nav> — `senawastudio-com`)**:
   - Landmark `<nav class="Nav-module__bLoQaq__nav Nav-module__bLoQaq__navHome">` hosting `Senawa · Architecture & Interior Des` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-href="/_next/static/chunks/..."`, `data-active`, `data-hero`), and stylesheet rule `nter_c21b1aaa-module__0pqmKW__cla... { font-family:Inter,Inter Fallback;font-style:normal }`.
2. **Hero Stage & Focal Lead (<section.antialiased> — `Senawa, Architecture & Interior De`)**:
   - Landmark `<section class="antialiased">` presenting display lead `Senawa, Architecture & Interior Design Studio in...` and copy excerpt *"contact.senawastudio@gmail.com"* over `#f6f2eb` canvas and `#302620` ink.
3. **Primary Showcase & Content Grid (<section.skip-link> — `contact.senawastudio@gmail.com`)**:
   - Landmark `<section class="skip-link">` rendering section `contact.senawastudio@gmail.com` with copy *"BSD, Tangerang Selatan"*, asset references (`clarity.js`, `xmr8ny30a5`, `0ha4m18glnjqn.js`, `3r7r9eemmq-97.js`), and grid rule `inter_c21b1aaa-module__0pqmKW__va... { --font-sans:"Inter", "Inter Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.Nav-module__bLoQaq__nav> — `BSD, Tangerang Selatan`)**:
   - Landmark `<section class="Nav-module__bLoQaq__nav">` framing `BSD, Tangerang Selatan` and `→ AA House Bintaro Residential · 2025` (*"→ AA House Bintaro Residential · 2025"*) with `#d4c9b4` surface cards, `#a8967e` accents, and `sora_2a023f4c-module__BGqKYq__cla... { font-family:Sora,Sora Fallback;font-style:normal }`.
5. **Colophon & Global Directory Footer (<footer.Nav-module__bLoQaq__navHome> — `https://senawastudio.com`)**:
   - Landmark `<footer class="Nav-module__bLoQaq__navHome">` anchoring `Senawa · Architecture & Interior` footer links (`Overview · Index · Archive · About · Contact`), copy *"Residential · 2025"*, and `#302620` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: senawastudio-com (Senawa · Architecture & Interior Design Studio in Jakarta)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `senawastudio-com` (**Senawa · Architecture & Interior Design Studio in Jakarta** — `https://senawastudio.com`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#f6f2eb` canvas, `#302620` ink, `#a8967e` accent).
- **Identity & Domain Context**: Architecture made for how people actually live. An architecture, interior, and furniture design studio in the Greater Jakarta area.
- **Primary Substrate**: `#f6f2eb` (`var(--wool)` in `:root`), **Primary Ink**: `#302620`, **Accent / Highlight**: `#a8967e`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#f6f2eb` (`var(--wool)` in `:root`) paired with `#302620` primary typography and `#a8967e` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Inter` for display copy (`Senawa, Architecture & Interior Desi`) with `Inter Fallback` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `560px` container bounds (`gap: 16px`, padding `48px`) with `cubic-bezier(.4,0,.2,1)` easing.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `senawastudio-com` in your global stylesheet:

:root {
  /* Senawa · Architecture & Interior Design Studio in Jakarta (senawastudio-com) — Ground-Truth Extracted CSS Variables */
  --font-sans: "Inter", "Inter Fallback"; /* Typography / Scale Token (senawastudio-com) */
  --font-sora: "Sora", "Sora Fallback"; /* Typography / Scale Token (senawastudio-com) */
  --s-dim: #302620b8; /* Color / Atmospheric Token (senawastudio-com) */
  --s-dim2: #302620b8; /* Color / Atmospheric Token (senawastudio-com) */
  --s-line: #30262024; /* Color / Atmospheric Token (senawastudio-com) */
  --studio-ink: 82, 80, 80; /* Typography Ink Token (senawastudio-com) */
  --b-ease: var(--ease-out,cubic-bezier(.16, 1, .3, 1)); /* Motion / Easing Token (senawastudio-com) */
  --b-ink: var(--slate); /* Typography Ink Token (senawastudio-com) */
  --b-ink-soft: #302620b3; /* Typography Ink Token (senawastudio-com) */
  --b-ink-faint: #30262057; /* Typography Ink Token (senawastudio-com) */
  --b-line-wake: #30262038; /* Color / Atmospheric Token (senawastudio-com) */
  --b-dot: var(--slate); /* Design System Custom Token (senawastudio-com) */
  --b-t-slow: .84s; /* Motion / Timing Token (senawastudio-com) */
  --b-t-mid: var(--duration-mid); /* Design System Custom Token (senawastudio-com) */
  --crop-ease: var(--ease-out); /* Motion / Easing Token (senawastudio-com) */
  --wool: #f6f2eb; /* Color / Atmospheric Token (senawastudio-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#f6f2eb` — grounded in `var(--wool)` in `:root`
- **Primary Typography Ink**: `#ede6d8` — grounded in `var(--linen)` in `:root`
- **Elevated Surface / Card Substrate**: `#d4c9b4` — grounded in `var(--sand)` in `:root`
- **Interactive Accent / Highlight**: `#a8967e` — grounded in `var(--oak)` in `:root`
- **Secondary / Muted Copy**: `#6b5a48` — grounded in `var(--walnut)` in `:root`
- **Structural Hairline Border**: `#302620` — grounded in `var(--slate)` in `:root`
- **Variable Token (`--s-dim`)**: `#302620b8` — grounded in `var(--s-dim)` in `:root`
- **Variable Token (`--s-line`)**: `#30262024` — grounded in `var(--s-line)` in `:root`
- **Variable Token (`--b-ink-soft`)**: `#302620b3` — grounded in `var(--b-ink-soft)` in `:root`
- **Variable Token (`--b-ink-faint`)**: `#30262057` — grounded in `var(--b-ink-faint)` in `:root`
- **Variable Token (`--b-line-wake`)**: `#30262038` — grounded in `var(--b-line-wake)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `560px` extracted from `senawastudio-com` stylesheet
- **Padding & Gutters**: `48px` lateral canvas padding with `16px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 560px`, `gap: 16px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `48px` horizontal padding
- **Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (min-width:1024px) and (max-height:860px)`, `@media (max-width:1023px)`, `@media (max-width:767px)`
- **Corner Radii**: `3px`, `var(--radius-sm)`, `var(--radius-md)`, `4px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `Inter Fallback`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: CSS variables `--font-display: var(--font-sora), "Sora", var(--font-sans), "Helvetica Neue", sans-serif`
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `10px`, `clamp(1.25rem,1.7vw,1.625rem)`, `12px`, `13px`, `clamp(.9375rem,1vw,1.0625rem)`)
- **Body Copy Rule**: CSS variables `--font-body: var(--font-sans), "Inter", "Helvetica Neue", sans-serif`, `--leading-body: 1.75`; rule `p` (`font-size: clamp(.9375rem,1vw,1.0625rem)`, `line-height: var(--leading-body)`, `font-weight: 300`)
- **Metadata & Index Rule**: CSS variables `--color-text-caption: var(--slate)`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `senawastudio-com` (`Senawa · Architecture & Interior Design Studio in Jakarta`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.Nav-module__bLoQaq__nav> — `senawastudio-com`)**:
   - DOM & Selectors: Landmark `<nav class="Nav-module__bLoQaq__nav Nav-module__bLoQaq__navHome">` hosting `Senawa · Architecture & Interior Des` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-href="/_next/static/chunks/..."`, `data-active`, `data-hero`), and stylesheet rule `nter_c21b1aaa-module__0pqmKW__cla... { font-family:Inter,Inter Fallback;font-style:normal }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.Nav-module__bLoQaq__nav> — `senawastudio-com`)` (`senawastudio-com`) adapts across `@media (prefers-reduced-motion:reduce)`, `@media (min-width:1024px) and (max-height:860px)`, `@media (max-width:1023px)`, `@media (max-width:767px)` with `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.33,1,.68,1)`, `cubic-bezier(.5,1,.89,1)` transitions and links `Overview · Index · Archive · About · Contact`.
2. **Hero Stage & Focal Lead (<section.antialiased> — `Senawa, Architecture & Interior De`)**:
   - DOM & Selectors: Landmark `<section class="antialiased">` presenting display lead `Senawa, Architecture & Interior Design Studio in...` and copy excerpt *"contact.senawastudio@gmail.com"* over `#f6f2eb` canvas and `#302620` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#f6f2eb` background with `#302620` headline `Senawa, Architecture & Interior Design Studio in...`.
3. **Primary Showcase & Content Grid (<section.skip-link> — `contact.senawastudio@gmail.com`)**:
   - DOM & Selectors: Landmark `<section class="skip-link">` rendering section `contact.senawastudio@gmail.com` with copy *"BSD, Tangerang Selatan"*, asset references (`clarity.js`, `xmr8ny30a5`, `0ha4m18glnjqn.js`, `3r7r9eemmq-97.js`), and grid rule `inter_c21b1aaa-module__0pqmKW__va... { --font-sans:"Inter", "Inter Fallback" }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.skip-link> — `contact.senawastudio@gmail.com`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 560px`, `gap: 16px`) on desktop and Single-column vertical stack at `390px` viewport width with `48px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.Nav-module__bLoQaq__nav> — `BSD, Tangerang Selatan`)**:
   - DOM & Selectors: Landmark `<section class="Nav-module__bLoQaq__nav">` framing `BSD, Tangerang Selatan` and `→ AA House Bintaro Residential · 2025` (*"→ AA House Bintaro Residential · 2025"*) with `#d4c9b4` surface cards, `#a8967e` accents, and `sora_2a023f4c-module__BGqKYq__cla... { font-family:Sora,Sora Fallback;font-style:normal }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.Nav-module__bLoQaq__nav> — `BSD, Tangerang Selatan`)` uses `3px`, `var(--radius-sm)`, `var(--radius-md)`, `4px` radii, `#a8967e` highlights, and assets (clarity.js, xmr8ny30a5, 0ha4m18glnjqn.js).
5. **Colophon & Global Directory Footer (<footer.Nav-module__bLoQaq__navHome> — `https://senawastudio.com`)**:
   - DOM & Selectors: Landmark `<footer class="Nav-module__bLoQaq__navHome">` anchoring `Senawa · Architecture & Interior` footer links (`Overview · Index · Archive · About · Contact`), copy *"Residential · 2025"*, and `#302620` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.Nav-module__bLoQaq__navHome> — `https://senawastudio.com`)` aligns to `560px` extracted from `senawastudio-com` stylesheet with `48px` lateral canvas padding with `16px` grid gap and attributes (data-precedence="next", data-href="/_next/static/chunks/...", data-active).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"contact.senawastudio@gmail.com"*
- Copy Excerpt 2: *"BSD, Tangerang Selatan"*
- Copy Excerpt 3: *"→ AA House Bintaro Residential · 2025"*
- Copy Excerpt 4: *"Residential · 2025"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.33,1,.68,1)`, `cubic-bezier(.5,1,.89,1)`
- **Extracted Stylesheet Rules (`senawastudio-com`)**:
- `nter_c21b1aaa-module__0pqmKW__cla... { font-family:Inter,Inter Fallback;font-style:normal }`
- `inter_c21b1aaa-module__0pqmKW__va... { --font-sans:"Inter", "Inter Fallback" }`
- `sora_2a023f4c-module__BGqKYq__cla... { font-family:Sora,Sora Fallback;font-style:normal }`
- `.sora_2a023f4c-module__BGqKYq__va... { --font-sora:"Sora", "Sora Fallback" }`
- `PageTransition-module__kKDxmW__co... { opacity:1;visibility:visible;pointer-events:auto;transition:opacity .45s... }`
- **Per-Selector Transition Rules**:
- **Selector `.PageTransition-module__kKDxmW__c...`**: `transition: opacity .45s cubic-bezier(.4,0,.2,1)` extracted from `senawastudio-com` stylesheet.
- **Selector `.PageTransition-module__kKDxmW__r...`**: `transition: opacity .55s cubic-bezier(.4,0,.2,1)` extracted from `senawastudio-com` stylesheet.
- **Selector `.PageTransition-module__kKDxmW__mark`**: `transition: opacity .45s cubic-bezier(.4,0,.2,1),transform .45s cubic-bezi...` extracted from `senawastudio-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<nav.Nav-module__bLoQaq__nav>` and `<section.skip-link>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<section.antialiased>` and `<section.skip-link>` interactive targets.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `senawastudio-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
