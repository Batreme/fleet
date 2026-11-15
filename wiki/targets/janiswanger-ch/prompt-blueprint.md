---
title: "UI Prompt Blueprint: janiswanger-ch"
date: 2026-11-15
target: "janiswanger-ch"
status: analyzed
capture: dom
capture_desktop: dom
capture_mobile: dom
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#e5e5e5`)"
---

# UI Design System & Master Generation Blueprint: janiswanger-ch

> **Janis Wanger — Creative Engineer in Bern** (https://janiswanger.ch) — Portfolio of Janis Wanger, a creative Frontend Engineer in Bern working across design and code. Projects, experience, and how to get in t...

![Desktop Viewport Capture](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Janis Wanger — Creative Engineer in Bern** (`https://janiswanger.ch`). Portfolio of Janis Wanger, a creative Frontend Engineer in Bern working across design and code. Projects, experience, and how to get in t...
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#e5e5e5`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--color-black)` in `:root`) paired with `#fff` primary typography and `#e5e5e5` accents.
  - **Extracted Typographic Hierarchy**: Pairs `PolySans` for display copy (`Janis is a Bern-based creative Front`) with `Georgia` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `var(--container-2xl)` container bounds (`gap: var(--spacing)`, padding `var(--spacing-container-level-1)`) with `cubic-bezier(.22,1,.36,1)` easing and GSAP Timeline & ScrollTrigger, Swiper Touch Carousel Engine.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×9679px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `var(--container-2xl)` extracted from `janiswanger-ch` stylesheet.
- **Canvas Lateral Padding & Spacing**: `var(--spacing-container-level-1)` lateral canvas padding with `var(--spacing)` grid gap.
- **Border Radius Scale**: `50%`, `.25rem`, `999px`, `var(--radius-2xl)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: var(--container-2xl)`, `gap: var(--spacing)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--spacing-container-level-1)` horizontal padding.
- **Extracted CSS Media Queries**: `@media (width<48rem)`, `@media (prefers-reduced-motion:reduce)`, `@media (width>=48rem)`, `@media not all and (width>=64rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#5bb872` | `var(--color-focus)` in `:root` |
| **Interactive Accent / Highlight** | `#e5e5e5` | `var(--color-surface)` in `:root` |
| **Secondary / Muted Copy** | `#ff8a3d` | `var(--color-accent)` in `:root` |
| **Structural Hairline Border** | `#341804` | `var(--color-on-accent)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-sans` | `PolySans, ui-sans-serif, system-ui, sans-serif` | Typography / Scale Token |
| `--font-serif` | `Georgia, ui-serif, "Times New Roman", Times, serif` | Typography / Scale Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--text-xs` | `.75rem` | Typography Ink Token |
| `--text-xs--line-height` | `1.33333` | Typography Ink Token |
| `--text-sm` | `.875rem` | Typography Ink Token |
| `--text-sm--line-height` | `1.42857` | Typography Ink Token |
| `--text-base` | `1rem` | Typography Ink Token |
| `--text-base--line-height` | `1.5` | Typography Ink Token |
| `--text-lg` | `1.125rem` | Typography Ink Token |
| `--text-lg--line-height` | `1.55556` | Typography Ink Token |
| `--text-2xl` | `1.5rem` | Typography Ink Token |
| `--text-2xl--line-height` | `1.33333` | Typography Ink Token |
| `--font-weight-normal` | `400` | Typography / Scale Token |
| `--font-weight-medium` | `500` | Typography / Scale Token |
| `--font-weight-semibold` | `600` | Typography / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `PolySans`.
- **Primary Body Stack**: `Georgia`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1.36rem`, `1em`, `80%`, `75%`, `var(--text-xs)`).
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: 1.33333`.
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: 1.5`.
- **Metadata & Navigation Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: 1.33333`, `--text-sm: .875rem`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.hire-badge[data-v-163802bc]`**: `transition: transform .5s cubic-bezier(.22,1,.36,1)` extracted from `janiswanger-ch` stylesheet.
- **Selector `media (prefers-reduced-motion:red...`**: `transition: none` extracted from `janiswanger-ch` stylesheet.
- **Selector `layer theme`**: `transition: .15s` extracted from `janiswanger-ch` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.22,1,.36,1)`)**: Governs interactive state transitions across `<header.hero-home>` and `<section.py-32>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Swiper Touch Carousel Engine, HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Janis Wanger — Creative Engineer in Bern   │
│ ====================================================================== │
│ [ <header.hero-home>       | Main navigation · Skip to content      ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.py-32>                                      |   │
│ | H1: Janis is a Bern-based creative Frontend Engineer...          |   │
│ | Substrate: #000       | Ink: #fff       | Accent: #e5e5e5        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.py-32>           ) max-w: var(--containe |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Soft skills                  |  | Technical skills             | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: var(--) | │
│ | [<header.hero-home>] -> [<section.py-32>] -> [<section.py-32>] |     │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.site-footer>  ) | https://janiswanger.ch             │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.hero-home> — `janiswanger-ch`)**:
   - Landmark `<header class="hero-home relative">` hosting `Janis Wanger — Creative Engineer in ` navigation (`Main navigation · Skip to content`), DOM attributes (`data-hid="canonical"`, `data-hid="hreflang-de-CH"`, `data-hid="hreflang-en"`, `data-hid="hreflang-x-default"`), and stylesheet rule `webkit-media-controls { display:none!important }`.
2. **Hero Stage & Focal Lead (<section.py-32> — `Janis is a Bern-based creative Fro`)**:
   - Landmark `<section class="py-32 relative">` presenting display lead `Janis is a Bern-based creative Frontend Engineer...` and copy excerpt *"Janis Wanger Frontend Engineer"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.py-32> — `Soft skills`)**:
   - Landmark `<section class="py-32 relative">` rendering section `Soft skills` with copy *"O P E N T O G E T T I N G H I R E D ☆ ♡ ✧ O P E N T O G E T T I N"*, asset references (`entry.I4GIEjMK.css`, `HireBadge.BgIwIulx.css`, `AutoplayVideo.ulh4C2Gx.css`, `B7fVWpKZ.js`), and grid rule `it-media-controls-start-playback-... { display:none!important }`.
4. **Interactive Detail & Feature Matrix (<article.skills-enter> — `Technical skills`)**:
   - Landmark `<article class="skills-enter relative">` framing `Technical skills` and `Want to work together ?` (*"Sometimes the frequencies just match"*) with `#5bb872` surface cards, `#e5e5e5` accents, and `before { content:"";pointer-events:none;border-radius:50%;position:absolute;inset... }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://janiswanger.ch`)**:
   - Landmark `<footer class="site-footer relative">` anchoring `Janis Wanger — Creative Engineer` footer links (`Main navigation · Skip to content`), copy *"so beautiful patterns emerge."*, and `#341804` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: janiswanger-ch (Janis Wanger — Creative Engineer in Bern)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `janiswanger-ch` (**Janis Wanger — Creative Engineer in Bern** — `https://janiswanger.ch`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#e5e5e5`).
- **Identity & Domain Context**: Portfolio of Janis Wanger, a creative Frontend Engineer in Bern working across design and code. Projects, experience, and how to get in t...
- **Primary Substrate**: `#000` (`var(--color-black)` in `:root`), **Primary Ink**: `#fff`, **Accent / Highlight**: `#e5e5e5`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--color-black)` in `:root`) paired with `#fff` primary typography and `#e5e5e5` accents.
  - **Extracted Typographic Hierarchy**: Pairs `PolySans` for display copy (`Janis is a Bern-based creative Front`) with `Georgia` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `var(--container-2xl)` container bounds (`gap: var(--spacing)`, padding `var(--spacing-container-level-1)`) with `cubic-bezier(.22,1,.36,1)` easing and GSAP Timeline & ScrollTrigger, Swiper Touch Carousel Engine.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `janiswanger-ch` in your global stylesheet:

:root {
  /* Janis Wanger — Creative Engineer in Bern (janiswanger-ch) — Ground-Truth Extracted CSS Variables */
  --font-sans: PolySans, ui-sans-serif, system-ui, sans-serif; /* Typography / Scale Token (janiswanger-ch) */
  --font-serif: Georgia, ui-serif, "Times New Roman", Times, serif; /* Typography / Scale Token (janiswanger-ch) */
  --spacing: .25rem; /* Layout / Spatial Grid Token (janiswanger-ch) */
  --text-xs: .75rem; /* Typography Ink Token (janiswanger-ch) */
  --text-xs--line-height: 1.33333; /* Typography Ink Token (janiswanger-ch) */
  --text-sm: .875rem; /* Typography Ink Token (janiswanger-ch) */
  --text-sm--line-height: 1.42857; /* Typography Ink Token (janiswanger-ch) */
  --text-base: 1rem; /* Typography Ink Token (janiswanger-ch) */
  --text-base--line-height: 1.5; /* Typography Ink Token (janiswanger-ch) */
  --text-lg: 1.125rem; /* Typography Ink Token (janiswanger-ch) */
  --text-lg--line-height: 1.55556; /* Typography Ink Token (janiswanger-ch) */
  --text-2xl: 1.5rem; /* Typography Ink Token (janiswanger-ch) */
  --text-2xl--line-height: 1.33333; /* Typography Ink Token (janiswanger-ch) */
  --font-weight-normal: 400; /* Typography / Scale Token (janiswanger-ch) */
  --font-weight-medium: 500; /* Typography / Scale Token (janiswanger-ch) */
  --font-weight-semibold: 600; /* Typography / Scale Token (janiswanger-ch) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#000` — grounded in `var(--color-black)` in `:root`
- **Primary Typography Ink**: `#fff` — grounded in `var(--color-white)` in `:root`
- **Elevated Surface / Card Substrate**: `#5bb872` — grounded in `var(--color-focus)` in `:root`
- **Interactive Accent / Highlight**: `#e5e5e5` — grounded in `var(--color-surface)` in `:root`
- **Secondary / Muted Copy**: `#ff8a3d` — grounded in `var(--color-accent)` in `:root`
- **Structural Hairline Border**: `#341804` — grounded in `var(--color-on-accent)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×9679px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `var(--container-2xl)` extracted from `janiswanger-ch` stylesheet
- **Padding & Gutters**: `var(--spacing-container-level-1)` lateral canvas padding with `var(--spacing)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: var(--container-2xl)`, `gap: var(--spacing)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--spacing-container-level-1)` horizontal padding
- **Media Queries**: `@media (width<48rem)`, `@media (prefers-reduced-motion:reduce)`, `@media (width>=48rem)`, `@media not all and (width>=64rem)`
- **Corner Radii**: `50%`, `.25rem`, `999px`, `var(--radius-2xl)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `PolySans`
- **Body Font Stack**: `Georgia`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1.36rem`, `1em`, `80%`, `75%`, `var(--text-xs)`)
- **H2 Section Rule**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: 1.33333`
- **Body Copy Rule**: CSS variables `--text-base: 1rem`, `--text-base--line-height: 1.5`
- **Metadata & Index Rule**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: 1.33333`, `--text-sm: .875rem`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `janiswanger-ch` (`Janis Wanger — Creative Engineer in Bern`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.hero-home> — `janiswanger-ch`)**:
   - DOM & Selectors: Landmark `<header class="hero-home relative">` hosting `Janis Wanger — Creative Engineer in ` navigation (`Main navigation · Skip to content`), DOM attributes (`data-hid="canonical"`, `data-hid="hreflang-de-CH"`, `data-hid="hreflang-en"`, `data-hid="hreflang-x-default"`), and stylesheet rule `webkit-media-controls { display:none!important }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.hero-home> — `janiswanger-ch`)` (`janiswanger-ch`) adapts across `@media (width<48rem)`, `@media (prefers-reduced-motion:reduce)`, `@media (width>=48rem)`, `@media not all and (width>=64rem)` with `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)` transitions and links `Main navigation · Skip to content`.
2. **Hero Stage & Focal Lead (<section.py-32> — `Janis is a Bern-based creative Fro`)**:
   - DOM & Selectors: Landmark `<section class="py-32 relative">` presenting display lead `Janis is a Bern-based creative Frontend Engineer...` and copy excerpt *"Janis Wanger Frontend Engineer"* over `#000` canvas and `#fff` ink.
   - Responsive Contract: Hero stage (`1440×9679px` desktop / `390×2400px` mobile) sets `#000` background with `#fff` headline `Janis is a Bern-based creative Frontend Engineer...`.
3. **Primary Showcase & Content Grid (<section.py-32> — `Soft skills`)**:
   - DOM & Selectors: Landmark `<section class="py-32 relative">` rendering section `Soft skills` with copy *"O P E N T O G E T T I N G H I R E D ☆ ♡ ✧ O P E N T O G E T T I N"*, asset references (`entry.I4GIEjMK.css`, `HireBadge.BgIwIulx.css`, `AutoplayVideo.ulh4C2Gx.css`, `B7fVWpKZ.js`), and grid rule `it-media-controls-start-playback-... { display:none!important }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.py-32> — `Soft skills`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: var(--container-2xl)`, `gap: var(--spacing)`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--spacing-container-level-1)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<article.skills-enter> — `Technical skills`)**:
   - DOM & Selectors: Landmark `<article class="skills-enter relative">` framing `Technical skills` and `Want to work together ?` (*"Sometimes the frequencies just match"*) with `#5bb872` surface cards, `#e5e5e5` accents, and `before { content:"";pointer-events:none;border-radius:50%;position:absolute;inset... }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<article.skills-enter> — `Technical skills`)` uses `50%`, `.25rem`, `999px`, `var(--radius-2xl)` radii, `#e5e5e5` highlights, and assets (entry.I4GIEjMK.css, HireBadge.BgIwIulx.css, AutoplayVideo.ulh4C2Gx.css).
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://janiswanger.ch`)**:
   - DOM & Selectors: Landmark `<footer class="site-footer relative">` anchoring `Janis Wanger — Creative Engineer` footer links (`Main navigation · Skip to content`), copy *"so beautiful patterns emerge."*, and `#341804` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.site-footer> — `https://janiswanger.ch`)` aligns to `var(--container-2xl)` extracted from `janiswanger-ch` stylesheet with `var(--spacing-container-level-1)` lateral canvas padding with `var(--spacing)` grid gap and attributes (data-hid="canonical", data-hid="hreflang-de-CH", data-hid="hreflang-en").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Janis Wanger Frontend Engineer"*
- Copy Excerpt 2: *"O P E N T O G E T T I N G H I R E D ☆ ♡ ✧ O P E N T O G E T T I N G H I R E D ☆ ♡ ✧"*
- Copy Excerpt 3: *"Sometimes the frequencies just match"*
- Copy Excerpt 4: *"so beautiful patterns emerge."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`
- **Extracted Stylesheet Rules (`janiswanger-ch`)**:
- `webkit-media-controls { display:none!important }`
- `it-media-controls-start-playback-... { display:none!important }`
- `before { content:"";pointer-events:none;border-radius:50%;position:absolute;inset... }`
- `hover { color:var(--color-accent-inverted);transform:scale(1.06) }`
- `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- **Per-Selector Transition Rules**:
- **Selector `.hire-badge[data-v-163802bc]`**: `transition: transform .5s cubic-bezier(.22,1,.36,1)` extracted from `janiswanger-ch` stylesheet.
- **Selector `media (prefers-reduced-motion:red...`**: `transition: none` extracted from `janiswanger-ch` stylesheet.
- **Selector `layer theme`**: `transition: .15s` extracted from `janiswanger-ch` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.22,1,.36,1)`)**: Governs interactive state transitions across `<header.hero-home>` and `<section.py-32>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Swiper Touch Carousel Engine, HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `janiswanger-ch`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
