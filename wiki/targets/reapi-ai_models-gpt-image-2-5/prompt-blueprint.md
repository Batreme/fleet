---
title: "UI Prompt Blueprint: reapi-ai_models-gpt-image-2-5"
date: 2026-11-15
target: "[[overview|reapi-ai_models-gpt-image-2-5]]"
status: analyzed
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#fef2f2` / `#ffa3a3`)"
---

# UI Design System & Master Generation Blueprint: reapi-ai_models-gpt-image-2-5

> **GPT Image 2.5 — Sharper Detail, Precise Editing** (https://reapi.ai/models/gpt-image-2-5) — GPT Image 2.5 is OpenAI's image generation and editing model with precision edits, reference fidelity and two speed tiers. Pay per image...

![Desktop Viewport Capture (1440x14542)](file:///root/projects/fleet/wiki/targets/reapi-ai_models-gpt-image-2-5/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **GPT Image 2.5 — Sharper Detail, Precise Editing** (`https://reapi.ai/models/gpt-image-2-5`). GPT Image 2.5 is OpenAI's image generation and editing model with precision edits, reference fidelity and two speed tiers. Pay per image...
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#fef2f2` / `#ffa3a3`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fef2f2` (`var(--color-red-50)` in `:root`) paired with `#fb2c36` primary typography and `#ffa3a3` accents.
  - **Extracted Typographic Hierarchy**: Pairs `TASA Orbiter` for display copy (`GPT Image 2.5 — Sharper Detail, Prec`) with `Space Mono` and `Space Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `40rem` container bounds (`gap: var(--gap)`, padding `3px`) with `cubic-bezier(0,0,.2,1)` easing and Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/reapi-ai_models-gpt-image-2-5/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×14542px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `40rem` extracted from `reapi-ai_models-gpt-image-2-5` stylesheet.
- **Canvas Lateral Padding & Spacing**: `3px` lateral canvas padding with `var(--gap)` grid gap.
- **Border Radius Scale**: `var(--radius)`, `.25rem`, `var(--cell-radius)`, `1px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: var(--gap)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `3px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fef2f2` | `var(--color-red-50)` in `:root` |
| **Primary Typography Ink** | `#ffe2e2` | `var(--color-red-100)` in `:root` |
| **Elevated Surface / Card Substrate** | `#ffcaca` | `var(--color-red-200)` in `:root` |
| **Interactive Accent / Highlight** | `#ffa3a3` | `var(--color-red-300)` in `:root` |
| **Secondary / Muted Copy** | `#ff6568` | `var(--color-red-400)` in `:root` |
| **Structural Hairline Border** | `#fb2c36` | `var(--color-red-500)` in `:root` |
| **Variable Token (`--color-red-600`)** | `#e40014` | `var(--color-red-600)` in `:root` |
| **Variable Token (`--color-red-700`)** | `#bf000f` | `var(--color-red-700)` in `:root` |
| **Variable Token (`--color-red-800`)** | `#9f0712` | `var(--color-red-800)` in `:root` |
| **Variable Token (`--color-orange-300`)** | `#ffb96d` | `var(--color-orange-300)` in `:root` |
| **Variable Token (`--color-orange-400`)** | `#ff8b1a` | `var(--color-orange-400)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-sans-family` | `"TASA Orbiter",-apple-system,PingFang SC,Microsoft YaHei,sans-serif` | Typography / Scale Token |
| `--font-mono-family` | `"Space Mono",ui-monospace,Menlo,monospace` | Typography / Scale Token |
| `--font-display-family` | `"Source Serif 4",Georgia,Times New Roman,serif` | Typography / Scale Token |
| `--font-sans` | `var(--font-sans-family)` | Typography / Scale Token |
| `--font-serif` | `var(--font-display-family)` | Typography / Scale Token |
| `--color-red-50` | `#fef2f2` | Brand / Palette Token |
| `--color-red-100` | `#ffe2e2` | Brand / Palette Token |
| `--color-red-200` | `#ffcaca` | Brand / Palette Token |
| `--color-red-300` | `#ffa3a3` | Brand / Palette Token |
| `--color-red-400` | `#ff6568` | Brand / Palette Token |
| `--color-red-500` | `#fb2c36` | Brand / Palette Token |
| `--color-red-600` | `#e40014` | Brand / Palette Token |
| `--color-red-700` | `#bf000f` | Brand / Palette Token |
| `--color-red-800` | `#9f0712` | Brand / Palette Token |
| `--color-orange-300` | `#ffb96d` | Brand / Palette Token |
| `--color-orange-400` | `#ff8b1a` | Brand / Palette Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `TASA Orbiter`.
- **Primary Body Stack**: `Space Mono`.
- **Technical / Metadata Stack**: `Space Mono`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--font-display-family: "Source Serif 4",Georgia,Times New Roman,serif`, `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5/2.25)`.
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2/1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`font-size: 1.75rem`).
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5/1)`, `--cpk-text-base: 1rem`.
- **Metadata & Navigation Labels**: CSS variables `--font-mono-family: "Space Mono",ui-monospace,Menlo,monospace`, `--text-xs: .75rem`, `--text-xs--line-height: calc(1/.75)`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.22,1,.36,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: .15s` extracted from `reapi-ai_models-gpt-image-2-5` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `reapi-ai_models-gpt-image-2-5` stylesheet.
- **Selector `box-shadow\]`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `reapi-ai_models-gpt-image-2-5` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<header.sticky>` and `<section.mx-auto>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — GPT Image 2.5 — Sharper Detail, Precise Ed │
│ ====================================================================== │
│ [ <header.sticky>          | r reAPI · Models · Agent · Pricing · B ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.relative>                                   |   │
│ | H1: GPT Image 2.5 — Sharper Detail, Precise Editing              |   │
│ | Substrate: #fef2f2    | Ink: #fb2c36    | Accent: #ffa3a3        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.mx-auto>         ) max-w: 40rem          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | See what it generates        |  | Pricing                      | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: var(--) | │
│ | [<header.sticky>] -> [<section.relative>] -> [<section.mx-auto>] |   │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.border-t>     ) | https://reapi.ai/models/gpt-image- │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.sticky> — `reapi-ai_models-gpt-image-2-5`)**:
   - Landmark `<header class="sticky inset-x-0">` hosting `GPT Image 2.5 — Sharper Detail, Prec` navigation (`r reAPI · Models · Agent · Pricing · Blog`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-site-id="7398c367fb45"`, `data-orientation="horizontal"`), and stylesheet rule `.typeface-sans { --font-sans-family:"TASA Orbiter",-apple-system,PingFang SC,Microsoft Ya... }`.
2. **Hero Stage & Focal Lead (<section.relative> — `GPT Image 2.5 — Sharper Detail, Pr`)**:
   - Landmark `<section class="relative isolate">` presenting display lead `GPT Image 2.5 — Sharper Detail, Precise Editing` and copy excerpt *"GPT Image 2.5 is live — OpenAI's newest image model, targeted edi"* over `#fef2f2` canvas and `#fb2c36` ink.
3. **Primary Showcase & Content Grid (<section.mx-auto> — `See what it generates`)**:
   - Landmark `<section class="mx-auto max-w-7xl">` rendering section `See what it generates` with copy *"Seedance 2.0 Eco — the same 720p / 1080p / 4K delivery on a cheap"*, asset references (`2d53b00a79aaa16a.css`, `b6699761ee55795a.css`, `b0188cb2d6a2b515.js`, `28b987a7ce424c5b.js`), and grid rule `.typeface-mono { --font-mono-family:"Space Mono",ui-monospace,Menlo,monospace }`.
4. **Interactive Detail & Feature Matrix (<section.border-b> — `Pricing`)**:
   - Landmark `<section class="border-b">` framing `Pricing` and `What is GPT Image 2.5?` (*"Seedance 2.0 Eco — the same 720p / 1080p / 4K delivery on a cheap"*) with `#ffcaca` surface cards, `#ffa3a3` accents, and `.typeface-display { --font-display-family:"Source Serif 4",Georgia,Times New Roman,serif }`.
5. **Colophon & Global Directory Footer (<footer.border-t> — `https://reapi.ai/models/gpt-image-2-5`)**:
   - Landmark `<footer class="border-t">` anchoring `GPT Image 2.5 — Sharper Detail, ` footer links (`r reAPI · Models · Agent · Pricing · Blog`), copy *"Seedance 2.5 is live — 30-second cinematic video with native"*, and `#fb2c36` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: reapi-ai_models-gpt-image-2-5 (GPT Image 2.5 — Sharper Detail, Precise Editing)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `reapi-ai_models-gpt-image-2-5` (**GPT Image 2.5 — Sharper Detail, Precise Editing** — `https://reapi.ai/models/gpt-image-2-5`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fef2f2` / `#ffa3a3`).
- **Identity & Domain Context**: GPT Image 2.5 is OpenAI's image generation and editing model with precision edits, reference fidelity and two speed tiers. Pay per image...
- **Primary Substrate**: `#fef2f2` (`var(--color-red-50)` in `:root`), **Primary Ink**: `#fb2c36`, **Accent / Highlight**: `#ffa3a3`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fef2f2` (`var(--color-red-50)` in `:root`) paired with `#fb2c36` primary typography and `#ffa3a3` accents.
  - **Extracted Typographic Hierarchy**: Pairs `TASA Orbiter` for display copy (`GPT Image 2.5 — Sharper Detail, Prec`) with `Space Mono` and `Space Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `40rem` container bounds (`gap: var(--gap)`, padding `3px`) with `cubic-bezier(0,0,.2,1)` easing and Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `reapi-ai_models-gpt-image-2-5` in your global stylesheet:

:root {
  /* GPT Image 2.5 — Sharper Detail, Precise Editing (reapi-ai_models-gpt-image-2-5) — Ground-Truth Extracted CSS Variables */
  --font-sans-family: "TASA Orbiter",-apple-system,PingFang SC,Microsoft YaHei,sans-serif; /* Typography / Scale Token (reapi-ai_models-gpt-image-2-5) */
  --font-mono-family: "Space Mono",ui-monospace,Menlo,monospace; /* Typography / Scale Token (reapi-ai_models-gpt-image-2-5) */
  --font-display-family: "Source Serif 4",Georgia,Times New Roman,serif; /* Typography / Scale Token (reapi-ai_models-gpt-image-2-5) */
  --font-sans: var(--font-sans-family); /* Typography / Scale Token (reapi-ai_models-gpt-image-2-5) */
  --font-serif: var(--font-display-family); /* Typography / Scale Token (reapi-ai_models-gpt-image-2-5) */
  --color-red-50: #fef2f2; /* Brand / Palette Token (reapi-ai_models-gpt-image-2-5) */
  --color-red-100: #ffe2e2; /* Brand / Palette Token (reapi-ai_models-gpt-image-2-5) */
  --color-red-200: #ffcaca; /* Brand / Palette Token (reapi-ai_models-gpt-image-2-5) */
  --color-red-300: #ffa3a3; /* Brand / Palette Token (reapi-ai_models-gpt-image-2-5) */
  --color-red-400: #ff6568; /* Brand / Palette Token (reapi-ai_models-gpt-image-2-5) */
  --color-red-500: #fb2c36; /* Brand / Palette Token (reapi-ai_models-gpt-image-2-5) */
  --color-red-600: #e40014; /* Brand / Palette Token (reapi-ai_models-gpt-image-2-5) */
  --color-red-700: #bf000f; /* Brand / Palette Token (reapi-ai_models-gpt-image-2-5) */
  --color-red-800: #9f0712; /* Brand / Palette Token (reapi-ai_models-gpt-image-2-5) */
  --color-orange-300: #ffb96d; /* Brand / Palette Token (reapi-ai_models-gpt-image-2-5) */
  --color-orange-400: #ff8b1a; /* Brand / Palette Token (reapi-ai_models-gpt-image-2-5) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#fef2f2` — grounded in `var(--color-red-50)` in `:root`
- **Primary Typography Ink**: `#ffe2e2` — grounded in `var(--color-red-100)` in `:root`
- **Elevated Surface / Card Substrate**: `#ffcaca` — grounded in `var(--color-red-200)` in `:root`
- **Interactive Accent / Highlight**: `#ffa3a3` — grounded in `var(--color-red-300)` in `:root`
- **Secondary / Muted Copy**: `#ff6568` — grounded in `var(--color-red-400)` in `:root`
- **Structural Hairline Border**: `#fb2c36` — grounded in `var(--color-red-500)` in `:root`
- **Variable Token (`--color-red-600`)**: `#e40014` — grounded in `var(--color-red-600)` in `:root`
- **Variable Token (`--color-red-700`)**: `#bf000f` — grounded in `var(--color-red-700)` in `:root`
- **Variable Token (`--color-red-800`)**: `#9f0712` — grounded in `var(--color-red-800)` in `:root`
- **Variable Token (`--color-orange-300`)**: `#ffb96d` — grounded in `var(--color-orange-300)` in `:root`
- **Variable Token (`--color-orange-400`)**: `#ff8b1a` — grounded in `var(--color-orange-400)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×14542px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `40rem` extracted from `reapi-ai_models-gpt-image-2-5` stylesheet
- **Padding & Gutters**: `3px` lateral canvas padding with `var(--gap)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: var(--gap)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `3px` horizontal padding
- **Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)`
- **Corner Radii**: `var(--radius)`, `.25rem`, `var(--cell-radius)`, `1px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `TASA Orbiter`
- **Body Font Stack**: `Space Mono`
- **Monospace / Technical Font Stack**: `Space Mono`
- **H1 Display Rule**: CSS variables `--font-display-family: "Source Serif 4",Georgia,Times New Roman,serif`, `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5/2.25)`
- **H2 Section Rule**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2/1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`font-size: 1.75rem`)
- **Body Copy Rule**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5/1)`, `--cpk-text-base: 1rem`
- **Metadata & Index Rule**: CSS variables `--font-mono-family: "Space Mono",ui-monospace,Menlo,monospace`, `--text-xs: .75rem`, `--text-xs--line-height: calc(1/.75)`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `reapi-ai_models-gpt-image-2-5` (`GPT Image 2.5 — Sharper Detail, Precise Editing`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.sticky> — `reapi-ai_models-gpt-image-2-5`)**:
   - DOM & Selectors: Landmark `<header class="sticky inset-x-0">` hosting `GPT Image 2.5 — Sharper Detail, Prec` navigation (`r reAPI · Models · Agent · Pricing · Blog`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-site-id="7398c367fb45"`, `data-orientation="horizontal"`), and stylesheet rule `.typeface-sans { --font-sans-family:"TASA Orbiter",-apple-system,PingFang SC,Microsoft Ya... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.sticky> — `reapi-ai_models-gpt-image-2-5`)` (`reapi-ai_models-gpt-image-2-5`) adapts across `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)` with `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.22,1,.36,1)` transitions and links `r reAPI · Models · Agent · Pricing · Blog`.
2. **Hero Stage & Focal Lead (<section.relative> — `GPT Image 2.5 — Sharper Detail, Pr`)**:
   - DOM & Selectors: Landmark `<section class="relative isolate">` presenting display lead `GPT Image 2.5 — Sharper Detail, Precise Editing` and copy excerpt *"GPT Image 2.5 is live — OpenAI's newest image model, targeted edi"* over `#fef2f2` canvas and `#fb2c36` ink.
   - Responsive Contract: Hero stage (`1440×14542px` desktop / `390×2400px` mobile) sets `#fef2f2` background with `#fb2c36` headline `GPT Image 2.5 — Sharper Detail, Precise Editing`.
3. **Primary Showcase & Content Grid (<section.mx-auto> — `See what it generates`)**:
   - DOM & Selectors: Landmark `<section class="mx-auto max-w-7xl">` rendering section `See what it generates` with copy *"Seedance 2.0 Eco — the same 720p / 1080p / 4K delivery on a cheap"*, asset references (`2d53b00a79aaa16a.css`, `b6699761ee55795a.css`, `b0188cb2d6a2b515.js`, `28b987a7ce424c5b.js`), and grid rule `.typeface-mono { --font-mono-family:"Space Mono",ui-monospace,Menlo,monospace }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.mx-auto> — `See what it generates`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: var(--gap)`) on desktop and Single-column vertical stack at `390px` viewport width with `3px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.border-b> — `Pricing`)**:
   - DOM & Selectors: Landmark `<section class="border-b">` framing `Pricing` and `What is GPT Image 2.5?` (*"Seedance 2.0 Eco — the same 720p / 1080p / 4K delivery on a cheap"*) with `#ffcaca` surface cards, `#ffa3a3` accents, and `.typeface-display { --font-display-family:"Source Serif 4",Georgia,Times New Roman,serif }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.border-b> — `Pricing`)` uses `var(--radius)`, `.25rem`, `var(--cell-radius)`, `1px` radii, `#ffa3a3` highlights, and assets (2d53b00a79aaa16a.css, b6699761ee55795a.css, b0188cb2d6a2b515.js).
5. **Colophon & Global Directory Footer (<footer.border-t> — `https://reapi.ai/models/gpt-image-2-5`)**:
   - DOM & Selectors: Landmark `<footer class="border-t">` anchoring `GPT Image 2.5 — Sharper Detail, ` footer links (`r reAPI · Models · Agent · Pricing · Blog`), copy *"Seedance 2.5 is live — 30-second cinematic video with native"*, and `#fb2c36` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.border-t> — `https://reapi.ai/models/gpt-image-2-5`)` aligns to `40rem` extracted from `reapi-ai_models-gpt-image-2-5` stylesheet with `3px` lateral canvas padding with `var(--gap)` grid gap and attributes (data-precedence="next", data-precedence="next", data-site-id="7398c367fb45").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"GPT Image 2.5 is live — OpenAI's newest image model, targeted edits that leave the..."*
- Copy Excerpt 2: *"Seedance 2.0 Eco — the same 720p / 1080p / 4K delivery on a cheaper tier from $0.0..."*
- Copy Excerpt 3: *"Seedance 2.0 Eco — the same 720p / 1080p / 4K delivery on a cheaper tier"*
- Copy Excerpt 4: *"Seedance 2.5 is live — 30-second cinematic video with native audio & real-person r..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.22,1,.36,1)`
- **Extracted Stylesheet Rules (`reapi-ai_models-gpt-image-2-5`)**:
- `.typeface-sans { --font-sans-family:"TASA Orbiter",-apple-system,PingFang SC,Microsoft Ya... }`
- `.typeface-mono { --font-mono-family:"Space Mono",ui-monospace,Menlo,monospace }`
- `.typeface-display { --font-display-family:"Source Serif 4",Georgia,Times New Roman,serif }`
- `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: .15s` extracted from `reapi-ai_models-gpt-image-2-5` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `reapi-ai_models-gpt-image-2-5` stylesheet.
- **Selector `box-shadow\]`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `reapi-ai_models-gpt-image-2-5` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<header.sticky>` and `<section.mx-auto>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `reapi-ai_models-gpt-image-2-5`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
