---
title: "UI Prompt Blueprint: www-tedxportland-com"
date: 2026-11-15
target: "[[overview|www-tedxportland-com]]"
status: analyzed
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#be000c` accent)"
---

# UI Design System & Master Generation Blueprint: www-tedxportland-com

> **TEDxPortland** (https://www.tedxportland.com/) — TEDxPortland is a nonprofit organization in Portland, OR that seeks to build community and provide a platform for every discipline and cu...

![Desktop Viewport Capture (1440x7830)](file:///root/projects/fleet/wiki/targets/www-tedxportland-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **TEDxPortland** (`https://www.tedxportland.com/`). TEDxPortland is a nonprofit organization in Portland, OR that seeks to build community and provide a platform for every discipline and cu...
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#be000c` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--color-black)` in `:root`) paired with `#fff` primary typography and `#be000c` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Inter` for display copy (`Tickets On Sale Now:`) with `Helvetica Neue` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `1023.98px` container bounds (`gap: .75rem`, padding `var(--spacing)`) with `cubic-bezier(.4,0,1,1)` easing.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/www-tedxportland-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×7830px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `1023.98px` extracted from `www-tedxportland-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `var(--spacing)` lateral canvas padding with `.75rem` grid gap.
- **Border Radius Scale**: `.25rem`, `var(--radius-2xl)`, `1.75rem`, `2rem`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1023.98px`, `gap: .75rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--spacing)` horizontal padding.
- **Extracted CSS Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (min-width:640px) and (max-width:1023.98px)`, `@media (min-width:1024px)`, `@media (prefers-reduced-motion:no-preference) and (hover:hover)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#ed000f` | `var(--color-ted-red)` in `:root` |
| **Interactive Accent / Highlight** | `#be000c` | `var(--color-ted-red-dark)` in `:root` |
| **Secondary / Muted Copy** | `#ff4f5b` | `var(--color-ted-red-light)` in `:root` |
| **Structural Hairline Border** | `#151515` | `var(--color-ted-black)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-sans` | `"Helvetica Neue", Helvetica, Inter, Arial, sans-serif` | Typography / Scale Token |
| `--color-green-600` | `oklch(62.7% .194 149.214)` | Brand / Palette Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--container-md` | `28rem` | Layout / Spatial Grid Token |
| `--container-2xl` | `42rem` | Layout / Spatial Grid Token |
| `--container-3xl` | `48rem` | Layout / Spatial Grid Token |
| `--container-4xl` | `56rem` | Layout / Spatial Grid Token |
| `--container-5xl` | `64rem` | Layout / Spatial Grid Token |
| `--container-6xl` | `72rem` | Layout / Spatial Grid Token |
| `--container-7xl` | `80rem` | Layout / Spatial Grid Token |
| `--text-xs` | `.75rem` | Typography Ink Token |
| `--text-xs--line-height` | `calc(1 / .75)` | Typography Ink Token |
| `--text-sm` | `.875rem` | Typography Ink Token |
| `--text-sm--line-height` | `calc(1.25 / .875)` | Typography Ink Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Inter`.
- **Primary Body Stack**: `Helvetica Neue`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`.
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`font-size: 1.5rem`).
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`; rule `p` (`letter-spacing: .015em`, `font-weight: 300`).
- **Metadata & Navigation Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: .15s` extracted from `www-tedxportland-com` stylesheet.
- **Selector `.prose-copy a`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `www-tedxportland-com` stylesheet.
- **Selector `data-reveal]`**: `transition: opacity .7s var(--ease-swift), transform .7s var(--ease-swift)` extracted from `www-tedxportland-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,1,1)`)**: Governs interactive state transitions across `<header.site-header>` and `<section.scroll-mt-20>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<section.relative>` and `<section.scroll-mt-20>` interactive targets.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — TEDxPortland                               │
│ ====================================================================== │
│ [ <header.site-header>     | About · Gallery · Films · Salons · Pat ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.relative>                                   |   │
│ | H1: Tickets On Sale Now:                                         |   │
│ | Substrate: #000       | Ink: #fff       | Accent: #be000c        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.scroll-mt-20>    ) max-w: 1023.98px      |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Our Legacy                   |  | TEDxPortland Salons & Specia | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: .75rem) | │
│ | [<header.site-heade] -> [<section.relative>] -> [<section.scroll-mt] │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.mt-16>        ) | https://www.tedxportland.com/      │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.site-header> — `www-tedxportland-com`)**:
   - Landmark `<header class="site-header sticky">` hosting `TEDxPortland` navigation (`About · Gallery · Films · Salons · Patron Society`), DOM attributes (`data-nav="wide"`, `data-mc-endpoint="https://mc.us14.list-..."`, `data-mc-honey="b_5b58926d605dff78fd8..."`, `data-mc-success="Thank you for subscri..."`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.relative> — `Tickets On Sale Now:`)**:
   - Landmark `<section class="relative z-30">` presenting display lead `Tickets On Sale Now:` and copy excerpt *"Subscribe For Updates"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.scroll-mt-20> — `Our Legacy`)**:
   - Landmark `<section class="scroll-mt-20 px-3">` rendering section `Our Legacy` with copy *"Year 15 Save the Date May 29, 2027"*, asset references (`0f458eb0-7b6e-4fd8-8afb-49134387e...`, `favicon-16x16.png`, `favicon-32x32.png`, `favicon-96x96.png`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.scroll-mt-20> — `TEDxPortland Salons & Special Even`)**:
   - Landmark `<section class="scroll-mt-20 bg-white">` framing `TEDxPortland Salons & Special Events` and `Gallery` (*"Save the Date May 29, 2027"*) with `#ed000f` surface cards, `#be000c` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.mt-16> — `https://www.tedxportland.com/`)**:
   - Landmark `<footer class="mt-16 bg-ted-black">` anchoring `TEDxPortland` footer links (`About · Gallery · Films · Salons · Patron Society`), copy *"Year 14 April 11, 2026"*, and `#151515` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-tedxportland-com (TEDxPortland)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-tedxportland-com` (**TEDxPortland** — `https://www.tedxportland.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#be000c` accent).
- **Identity & Domain Context**: TEDxPortland is a nonprofit organization in Portland, OR that seeks to build community and provide a platform for every discipline and cu...
- **Primary Substrate**: `#000` (`var(--color-black)` in `:root`), **Primary Ink**: `#fff`, **Accent / Highlight**: `#be000c`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--color-black)` in `:root`) paired with `#fff` primary typography and `#be000c` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Inter` for display copy (`Tickets On Sale Now:`) with `Helvetica Neue` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `1023.98px` container bounds (`gap: .75rem`, padding `var(--spacing)`) with `cubic-bezier(.4,0,1,1)` easing.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-tedxportland-com` in your global stylesheet:

:root {
  /* TEDxPortland (www-tedxportland-com) — Ground-Truth Extracted CSS Variables */
  --font-sans: "Helvetica Neue", Helvetica, Inter, Arial, sans-serif; /* Typography / Scale Token (www-tedxportland-com) */
  --color-green-600: oklch(62.7% .194 149.214); /* Brand / Palette Token (www-tedxportland-com) */
  --color-black: #000; /* Canvas / Surface Token (www-tedxportland-com) */
  --color-white: #fff; /* Canvas / Surface Token (www-tedxportland-com) */
  --spacing: .25rem; /* Layout / Spatial Grid Token (www-tedxportland-com) */
  --container-md: 28rem; /* Layout / Spatial Grid Token (www-tedxportland-com) */
  --container-2xl: 42rem; /* Layout / Spatial Grid Token (www-tedxportland-com) */
  --container-3xl: 48rem; /* Layout / Spatial Grid Token (www-tedxportland-com) */
  --container-4xl: 56rem; /* Layout / Spatial Grid Token (www-tedxportland-com) */
  --container-5xl: 64rem; /* Layout / Spatial Grid Token (www-tedxportland-com) */
  --container-6xl: 72rem; /* Layout / Spatial Grid Token (www-tedxportland-com) */
  --container-7xl: 80rem; /* Layout / Spatial Grid Token (www-tedxportland-com) */
  --text-xs: .75rem; /* Typography Ink Token (www-tedxportland-com) */
  --text-xs--line-height: calc(1 / .75); /* Typography Ink Token (www-tedxportland-com) */
  --text-sm: .875rem; /* Typography Ink Token (www-tedxportland-com) */
  --text-sm--line-height: calc(1.25 / .875); /* Typography Ink Token (www-tedxportland-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#000` — grounded in `var(--color-black)` in `:root`
- **Primary Typography Ink**: `#fff` — grounded in `var(--color-white)` in `:root`
- **Elevated Surface / Card Substrate**: `#ed000f` — grounded in `var(--color-ted-red)` in `:root`
- **Interactive Accent / Highlight**: `#be000c` — grounded in `var(--color-ted-red-dark)` in `:root`
- **Secondary / Muted Copy**: `#ff4f5b` — grounded in `var(--color-ted-red-light)` in `:root`
- **Structural Hairline Border**: `#151515` — grounded in `var(--color-ted-black)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×7830px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1023.98px` extracted from `www-tedxportland-com` stylesheet
- **Padding & Gutters**: `var(--spacing)` lateral canvas padding with `.75rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1023.98px`, `gap: .75rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--spacing)` horizontal padding
- **Media Queries**: `@media (prefers-reduced-motion:reduce)`, `@media (min-width:640px) and (max-width:1023.98px)`, `@media (min-width:1024px)`, `@media (prefers-reduced-motion:no-preference) and (hover:hover)`
- **Corner Radii**: `.25rem`, `var(--radius-2xl)`, `1.75rem`, `2rem`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `Helvetica Neue`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`
- **H2 Section Rule**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`font-size: 1.5rem`)
- **Body Copy Rule**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`; rule `p` (`letter-spacing: .015em`, `font-weight: 300`)
- **Metadata & Index Rule**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-tedxportland-com` (`TEDxPortland`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.site-header> — `www-tedxportland-com`)**:
   - DOM & Selectors: Landmark `<header class="site-header sticky">` hosting `TEDxPortland` navigation (`About · Gallery · Films · Salons · Patron Society`), DOM attributes (`data-nav="wide"`, `data-mc-endpoint="https://mc.us14.list-..."`, `data-mc-honey="b_5b58926d605dff78fd8..."`, `data-mc-success="Thank you for subscri..."`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.site-header> — `www-tedxportland-com`)` (`www-tedxportland-com`) adapts across `@media (prefers-reduced-motion:reduce)`, `@media (min-width:640px) and (max-width:1023.98px)`, `@media (min-width:1024px)`, `@media (prefers-reduced-motion:no-preference) and (hover:hover)` with `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)` transitions and links `About · Gallery · Films · Salons · Patron Society`.
2. **Hero Stage & Focal Lead (<section.relative> — `Tickets On Sale Now:`)**:
   - DOM & Selectors: Landmark `<section class="relative z-30">` presenting display lead `Tickets On Sale Now:` and copy excerpt *"Subscribe For Updates"* over `#000` canvas and `#fff` ink.
   - Responsive Contract: Hero stage (`1440×7830px` desktop / `390×2400px` mobile) sets `#000` background with `#fff` headline `Tickets On Sale Now:`.
3. **Primary Showcase & Content Grid (<section.scroll-mt-20> — `Our Legacy`)**:
   - DOM & Selectors: Landmark `<section class="scroll-mt-20 px-3">` rendering section `Our Legacy` with copy *"Year 15 Save the Date May 29, 2027"*, asset references (`0f458eb0-7b6e-4fd8-8afb-49134387e...`, `favicon-16x16.png`, `favicon-32x32.png`, `favicon-96x96.png`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.scroll-mt-20> — `Our Legacy`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1023.98px`, `gap: .75rem`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--spacing)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.scroll-mt-20> — `TEDxPortland Salons & Special Even`)**:
   - DOM & Selectors: Landmark `<section class="scroll-mt-20 bg-white">` framing `TEDxPortland Salons & Special Events` and `Gallery` (*"Save the Date May 29, 2027"*) with `#ed000f` surface cards, `#be000c` accents, and `strong { font-weight:bolder }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.scroll-mt-20> — `TEDxPortland Salons & Special Even`)` uses `.25rem`, `var(--radius-2xl)`, `1.75rem`, `2rem` radii, `#be000c` highlights, and assets (0f458eb0-7b6e-4fd8-8afb-49134387e..., favicon-16x16.png, favicon-32x32.png).
5. **Colophon & Global Directory Footer (<footer.mt-16> — `https://www.tedxportland.com/`)**:
   - DOM & Selectors: Landmark `<footer class="mt-16 bg-ted-black">` anchoring `TEDxPortland` footer links (`About · Gallery · Films · Salons · Patron Society`), copy *"Year 14 April 11, 2026"*, and `#151515` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.mt-16> — `https://www.tedxportland.com/`)` aligns to `1023.98px` extracted from `www-tedxportland-com` stylesheet with `var(--spacing)` lateral canvas padding with `.75rem` grid gap and attributes (data-nav="wide", data-mc-endpoint="https://mc.us14.list-...", data-mc-honey="b_5b58926d605dff78fd8...").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Subscribe For Updates"*
- Copy Excerpt 2: *"Year 15 Save the Date May 29, 2027"*
- Copy Excerpt 3: *"Save the Date May 29, 2027"*
- Copy Excerpt 4: *"Year 14 April 11, 2026"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`
- **Extracted Stylesheet Rules (`www-tedxportland-com`)**:
- `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `strong { font-weight:bolder }`
- `small { font-size:80% }`
- `sup { vertical-align:baseline;font-size:75%;line-height:0;position:relative }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: .15s` extracted from `www-tedxportland-com` stylesheet.
- **Selector `.prose-copy a`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `www-tedxportland-com` stylesheet.
- **Selector `data-reveal]`**: `transition: opacity .7s var(--ease-swift), transform .7s var(--ease-swift)` extracted from `www-tedxportland-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,1,1)`)**: Governs interactive state transitions across `<header.site-header>` and `<section.scroll-mt-20>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<section.relative>` and `<section.scroll-mt-20>` interactive targets.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-tedxportland-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
