---
title: "UI Prompt Blueprint: seedrouter-ai"
date: 2026-11-24
captured_at: 2026-11-24
target: "seedrouter-ai"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
capture_mode: behavioral_journey_v2
asset_format: webp
scroll_driver: native
desktop_keyframes: 8
subpages_crawled: 3
http_status: 200
archetype: "Light-Substrate Editorial & Modular Grid System (`#f7f5f1` canvas, `#090e12` ink, `#ffcc00` accent)"
---

# UI Design System & Master Generation Blueprint: seedrouter-ai

> **SeedRouter · One API for Image, Video, LLM and Audio Models** (https://seedrouter.ai) — SeedRouter puts image, video, language and audio models behind one API key with pay-per-request billing. Failed requests cost nothing. Ge...

![Desktop Journey Filmstrip (1280x6624)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x2616)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **SeedRouter · One API for Image, Video, LLM and Audio Models** (`https://seedrouter.ai`). SeedRouter puts image, video, language and audio models behind one API key with pay-per-request billing. Failed requests cost nothing. Ge...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#f7f5f1` canvas, `#090e12` ink, `#ffcc00` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#f7f5f1` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#090e12` primary typography and `#ffcc00` accents.
  - **Grounded Typographic Hierarchy**: Uses `Outfit` across display (`SeedRouter: one API for every model `) and body copy, paired with `JetBrains Mono` for monospace/code.
  - **Calibrated Spatial Grid & Motion**: Combines `96rem` container bounds (`gap: 20px`, padding `var(--card-spacing)`) with `cubic-bezier(0,0,.2,1)` easing and Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×6624px` (`assets/desktop-journey.webp`, `8` keyframes up to `y=9741px` / doc `10641px`), Mobile `390×2616px` (`assets/mobile-journey.webp`, `3` keyframes).
- **Master Container Bounds**: `96rem` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `var(--card-spacing)` lateral canvas padding with `20px` grid gap.
- **Border Radius Scale**: `3.35544e+07px`, `var(--radius)`, `.25rem`, `var(--cell-radius)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 96rem`, `gap: 20px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--card-spacing)` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f7f5f1` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#090e12` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#fffdf8` | `var(--card)` in `:root` |
| **Interactive Accent / Highlight** | `#ffcc00` | `crubber-button.ytp-swatch-backg... { background-color: #ffcc00 }` |
| **Secondary / Muted Copy** | `#737373` | `var(--color-fd-muted-foreground)` in `:root` |
| **Structural Hairline Border** | `#e2ded4` | `var(--border)` in `:root` |
| **Variable Token (`--primary`)** | `#18763a` | `var(--primary)` in `:root` |
| **Variable Token (`--secondary`)** | `#ece8df` | `var(--secondary)` in `:root` |
| **Variable Token (`--muted`)** | `#f0ede6` | `var(--muted)` in `:root` |
| **Variable Token (`--muted-foreground`)** | `#6b6a63` | `var(--muted-foreground)` in `:root` |
| **Variable Token (`--destructive`)** | `#d92d20` | `var(--destructive)` in `:root` |
| **Variable Token (`--destructive-foreground`)** | `#ffffff` | `var(--destructive-foreground)` in `:root` |
| **Variable Token (`--input`)** | `#d3cec1` | `var(--input)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--card` | `#fffdf8` | Color / Atmospheric Token |
| `--card-foreground` | `#090e12` | Typography Ink Token |
| `--popover` | `#fffdf8` | Color / Atmospheric Token |
| `--popover-foreground` | `#090e12` | Typography Ink Token |
| `--primary` | `#18763a` | Brand / Palette Token |
| `--primary-foreground` | `#f7f5f1` | Typography Ink Token |
| `--secondary` | `#ece8df` | Brand / Palette Token |
| `--secondary-foreground` | `#090e12` | Typography Ink Token |
| `--muted` | `#f0ede6` | Color / Atmospheric Token |
| `--muted-foreground` | `#6b6a63` | Typography Ink Token |
| `--accent` | `#f0ede6` | Brand / Palette Token |
| `--accent-foreground` | `#090e12` | Typography Ink Token |
| `--destructive` | `#d92d20` | Color / Atmospheric Token |
| `--destructive-foreground` | `#fff` | Typography Ink Token |
| `--border` | `#e2ded4` | Elevation / Border Token |
| `--input` | `#d3cec1` | Color / Atmospheric Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Outfit`.
- **Primary Body Stack**: `Outfit`.
- **Technical / Metadata Stack**: `JetBrains Mono`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 44.64px`, `line-height: 50.8896px`, `font-weight: 600`, `letter-spacing: -1.7856px`); CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`; rule `h1` (`letter-spacing: -.025em`, `font-weight: 500`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 40.32px`, `line-height: 44.352px`, `font-weight: 600`, `letter-spacing: -1.6128px`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`; rule `,h2` (`letter-spacing: -.02em`, `font-weight: 400`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--font-body-ext: "Nunito Sans", "Nunito Sans Fallback"`, `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`; rule `p` (`line-height: 18px`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--font-mono: var(--font-mono-label)`, `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.22,1,.36,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: .15s` extracted from `seedrouter-ai` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `seedrouter-ai` stylesheet.
- **Selector `transform\]`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `seedrouter-ai` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<header.sr-chrome>` and `<section.pb-16>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `native` (max document height `10641px`, deepest scrollY reached `9741px` across `8` desktop keyframes).
- **Detected Scroll / Motion Libraries**: Native browser scroll / standard CSS transitions.
- **Nav / Drawer Probe (`Tools`)**: Triggered visual change (pixel diff `10.331`, captured in `assets/state-nav.webp`); revealed links: AI Character Referenc..., Hotel Lobby AI, Raindance AI, All tools.
- **Hover Physics (`primary_cta` · `Models`)**: `boxShadow`: `none` -> `rgba(0, 0, 0, 0) 0px 0p...` (`transition-duration: 0.2s`, `timing: cubic-bezier(0.4, 0, 0.2, 1)`).
- **Interactive Control Probe (`tab`)**: Tested `Video` (diff `2.747`).
- **Theme Toggle Probe (`Dark`)**: Toggled body background `rgb(247, 245, 241)` -> `rgb(21, 24, 30)` and ink `rgb(9, 14, 18)` -> `rgb(243, 243, 243)`.
- **Route Transition Architecture**: First internal navigation (`/pricing`) measured as `SPA` in `1928ms`.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — SeedRouter · One API for Image, Video, LLM │
│ ====================================================================== │
│ [ <header.sr-chrome> (1440x65px)      | SeedRouter · Models · Pricin ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.sr-hero> (w=1440px)                           | │
│ | H1: SeedRouter: one API for every model your product...            | │
│ | Substrate: #f7f5f1 | Ink: #090e12 | Accent: #ffcc00                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.pb-16>) max-w: 96rem                       | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Models you can call on SeedR |  | Integration in 4 steps       | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.py-16>) — Create an API key                | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.sr-chrome-da) | https://seedrouter.ai                │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 20px)       │
│ ====================================================================== │
│ [ HEADER BAR (<header.sr-chrome>      ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.sr-hero>) — 390px Vertical Lead               | │
│ | H1: SeedRouter: one API for every model your product...            | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.pb-16>) — 1-Col Stack                     | │
│ | [ Item 1: Models you can call on SeedRouter today                ] | │
│ | [ Item 2: Integration in 4 steps                                 ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.py-16>) — 1-Col (Create an API key)         | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.sr-chrome-da) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.sr-chrome> — `seedrouter-ai`)**:
   - Landmark `<header class="sr-chrome inset-x-0">` (`1440x65px`) hosting `SeedRouter · One API for Image, Vide` navigation (`SeedRouter · Models · Pricing · Docs · Sign up`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-testid="announcement-dismiss"`, `data-nimg="1"`), and stylesheet rule `mono_744f2078-module__kLS_DW__cla... { font-family:JetBrains Mono,JetBrains Mono Fallback;font-style:normal }`.
2. **Hero Stage & Focal Lead (<section.sr-hero> — `SeedRouter: one API for every mode`)**:
   - Landmark `<section class="sr-hero sr-chrome-dark">` presenting display lead `SeedRouter: one API for every model your product...` and copy excerpt *"01 · Image, video, language and audio · one key"* over `#f7f5f1` canvas and `#090e12` ink.
3. **Primary Showcase & Content Grid (<section.pb-16> — `Models you can call on SeedRouter `)**:
   - Landmark `<section class="pb-16 pt-12">` rendering section `Models you can call on SeedRouter today` with copy *"Generate and edit video from text or a first frame, at the resolu"*, asset references (`0c8c4ded07fff55c-s.p.2tcyrya9o07v...`, `1b99372b3eaef0c8-s.p.1gsd1jahc5dg...`, `70bc3e132a0a741e-s.p.3t6q91iet4ns...`, `google.svg`), and grid rule `mono_744f2078-module__kLS_DW__var... { --font-code:"JetBrains Mono", "JetBrains Mono Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.py-16> — `Integration in 4 steps`)**:
   - Landmark `<section class="py-16">` framing `Integration in 4 steps` and `Create an API key` (*"$ POST /v1/videos/generations ✓ completed"*) with `#fffdf8` surface cards, `#ffcc00` accents, and `tfit_300d5b1f-module__eNyfuq__cla... { font-family:Outfit,Outfit Fallback;font-style:normal }`.
5. **Colophon & Global Directory Footer (<footer.sr-chrome-dark> — `https://seedrouter.ai`)**:
   - Landmark `<footer class="sr-chrome-dark relative">` anchoring `SeedRouter · One API for Image, ` footer links (`SeedRouter · Models · Pricing · Docs · Sign up`), copy *"$ POST /v1/videos/generations"*, and `#e2ded4` structural dividers.
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=0px`, `0%`): Active landmark `SeedRouter: one API for every model your product...` · sticky/fixed elements: `1`
- **Step 02** (`y=850px`, `9%`): Active landmark `Models you can call on SeedRouter today` · sticky/fixed elements: `1`
- **Step 03** (`y=2550px`, `26%`): Active landmark `Choose your integration` · sticky/fixed elements: `1`
- **Step 04** (`y=4250px`, `44%`): Active landmark `AI Image, Video and Text Models` · sticky/fixed elements: `1`
- **Step 05** (`y=5950px`, `61%`): Active landmark `Pay per use. No subscription.` · sticky/fixed elements: `1`
- **Step 06** (`y=7650px`, `79%`): Active landmark `Latest from the blog` · sticky/fixed elements: `1`
- **Step 07** (`y=9350px`, `96%`): Active landmark `Footer` · sticky/fixed elements: `1`
- **Step 08** (`y=9741px`, `100%`): Active landmark `Footer` · sticky/fixed elements: `1`

### Multi-Page Internal Route Map
- **Listing Route (`/pricing`)**: `https://seedrouter.ai/pricing` — H1: `Pay per use. No subscription.`, scrollHeight `12391px`, transition `SPA` (`1928ms`)
- **Detail Route (`/models/seedance-2-5`)**: `https://seedrouter.ai/models/seedance-2-5` — H1: `Seedance 2.5 — longer video with edit and extend`, scrollHeight `14748px`, transition `direct` (`3448ms`)
- **About Route (`/about`)**: `https://seedrouter.ai/about` — H1: `About SeedRouter`, scrollHeight `4136px`, transition `direct` (`1745ms`)

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: seedrouter-ai (SeedRouter · One API for Image, Video, LLM and Audio Models)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `seedrouter-ai` (**SeedRouter · One API for Image, Video, LLM and Audio Models** — `https://seedrouter.ai`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#f7f5f1` canvas, `#090e12` ink, `#ffcc00` accent).
- **Identity & Domain Context**: SeedRouter puts image, video, language and audio models behind one API key with pay-per-request billing. Failed requests cost nothing. Ge...
- **Primary Substrate**: `#f7f5f1` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#090e12`, **Accent / Highlight**: `#ffcc00`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#f7f5f1` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#090e12` primary typography and `#ffcc00` accents.
  - **Grounded Typographic Hierarchy**: Uses `Outfit` across display (`SeedRouter: one API for every model `) and body copy, paired with `JetBrains Mono` for monospace/code.
  - **Calibrated Spatial Grid & Motion**: Combines `96rem` container bounds (`gap: 20px`, padding `var(--card-spacing)`) with `cubic-bezier(0,0,.2,1)` easing and Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `seedrouter-ai` in your global stylesheet:

:root {
  /* SeedRouter · One API for Image, Video, LLM and Audio Models (seedrouter-ai) — Live-Grounded CSS Variables */
  --card: #fffdf8; /* Color / Atmospheric Token (seedrouter-ai) */
  --card-foreground: #090e12; /* Typography Ink Token (seedrouter-ai) */
  --popover: #fffdf8; /* Color / Atmospheric Token (seedrouter-ai) */
  --popover-foreground: #090e12; /* Typography Ink Token (seedrouter-ai) */
  --primary: #18763a; /* Brand / Palette Token (seedrouter-ai) */
  --primary-foreground: #f7f5f1; /* Typography Ink Token (seedrouter-ai) */
  --secondary: #ece8df; /* Brand / Palette Token (seedrouter-ai) */
  --secondary-foreground: #090e12; /* Typography Ink Token (seedrouter-ai) */
  --muted: #f0ede6; /* Color / Atmospheric Token (seedrouter-ai) */
  --muted-foreground: #6b6a63; /* Typography Ink Token (seedrouter-ai) */
  --accent: #f0ede6; /* Brand / Palette Token (seedrouter-ai) */
  --accent-foreground: #090e12; /* Typography Ink Token (seedrouter-ai) */
  --destructive: #d92d20; /* Color / Atmospheric Token (seedrouter-ai) */
  --destructive-foreground: #fff; /* Typography Ink Token (seedrouter-ai) */
  --border: #e2ded4; /* Elevation / Border Token (seedrouter-ai) */
  --input: #d3cec1; /* Color / Atmospheric Token (seedrouter-ai) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#f7f5f1` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#090e12` — grounded in live computed `main` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#fffdf8` — grounded in `var(--card)` in `:root`
- **Interactive Accent / Highlight**: `#ffcc00` — grounded in `crubber-button.ytp-swatch-backg... { background-color: #ffcc00 }`
- **Secondary / Muted Copy**: `#737373` — grounded in `var(--color-fd-muted-foreground)` in `:root`
- **Structural Hairline Border**: `#e2ded4` — grounded in `var(--border)` in `:root`
- **Variable Token (`--primary`)**: `#18763a` — grounded in `var(--primary)` in `:root`
- **Variable Token (`--secondary`)**: `#ece8df` — grounded in `var(--secondary)` in `:root`
- **Variable Token (`--muted`)**: `#f0ede6` — grounded in `var(--muted)` in `:root`
- **Variable Token (`--muted-foreground`)**: `#6b6a63` — grounded in `var(--muted-foreground)` in `:root`
- **Variable Token (`--destructive`)**: `#d92d20` — grounded in `var(--destructive)` in `:root`
- **Variable Token (`--destructive-foreground`)**: `#ffffff` — grounded in `var(--destructive-foreground)` in `:root`
- **Variable Token (`--input`)**: `#d3cec1` — grounded in `var(--input)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1280×6624px` (multi-frame vertical journey filmstrip (6624px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2616px` (multi-frame vertical journey filmstrip (2616px), `390px` standard mobile width).
- **Container Max-Width**: `96rem` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `var(--card-spacing)` lateral canvas padding with `20px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 96rem`, `gap: 20px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--card-spacing)` horizontal padding
- **Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)`
- **Corner Radii**: `3.35544e+07px`, `var(--radius)`, `.25rem`, `var(--cell-radius)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Outfit`
- **Body Font Stack**: `Outfit`
- **Monospace / Technical Font Stack**: `JetBrains Mono`
- **H1 Display Rule**: live computed `h1` (`font-size: 44.64px`, `line-height: 50.8896px`, `font-weight: 600`, `letter-spacing: -1.7856px`); CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`; rule `h1` (`letter-spacing: -.025em`, `font-weight: 500`)
- **H2 Section Rule**: live computed `h2` (`font-size: 40.32px`, `line-height: 44.352px`, `font-weight: 600`, `letter-spacing: -1.6128px`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`; rule `,h2` (`letter-spacing: -.02em`, `font-weight: 400`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--font-body-ext: "Nunito Sans", "Nunito Sans Fallback"`, `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`; rule `p` (`line-height: 18px`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--font-mono: var(--font-mono-label)`, `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `seedrouter-ai` (`SeedRouter · One API for Image, Video, LLM and Audio Models`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.sr-chrome> — `seedrouter-ai`)**:
   - DOM & Selectors: Landmark `<header class="sr-chrome inset-x-0">` (`1440x65px`) hosting `SeedRouter · One API for Image, Vide` navigation (`SeedRouter · Models · Pricing · Docs · Sign up`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-testid="announcement-dismiss"`, `data-nimg="1"`), and stylesheet rule `mono_744f2078-module__kLS_DW__cla... { font-family:JetBrains Mono,JetBrains Mono Fallback;font-style:normal }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.sr-chrome> — `seedrouter-ai`)` (`seedrouter-ai`) adapts across `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)` with `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.22,1,.36,1)` transitions and links `SeedRouter · Models · Pricing · Docs · Sign up`.
2. **Hero Stage & Focal Lead (<section.sr-hero> — `SeedRouter: one API for every mode`)**:
   - DOM & Selectors: Landmark `<section class="sr-hero sr-chrome-dark">` presenting display lead `SeedRouter: one API for every model your product...` and copy excerpt *"01 · Image, video, language and audio · one key"* over `#f7f5f1` canvas and `#090e12` ink.
   - Responsive Contract: Hero stage (`1280×6624px` desktop / `390×2616px` mobile) sets `#f7f5f1` background with `#090e12` headline `SeedRouter: one API for every model your product...`.
3. **Primary Showcase & Content Grid (<section.pb-16> — `Models you can call on SeedRouter `)**:
   - DOM & Selectors: Landmark `<section class="pb-16 pt-12">` rendering section `Models you can call on SeedRouter today` with copy *"Generate and edit video from text or a first frame, at the resolu"*, asset references (`0c8c4ded07fff55c-s.p.2tcyrya9o07v...`, `1b99372b3eaef0c8-s.p.1gsd1jahc5dg...`, `70bc3e132a0a741e-s.p.3t6q91iet4ns...`, `google.svg`), and grid rule `mono_744f2078-module__kLS_DW__var... { --font-code:"JetBrains Mono", "JetBrains Mono Fallback" }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.pb-16> — `Models you can call on SeedRouter `)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 96rem`, `gap: 20px`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--card-spacing)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.py-16> — `Integration in 4 steps`)**:
   - DOM & Selectors: Landmark `<section class="py-16">` framing `Integration in 4 steps` and `Create an API key` (*"$ POST /v1/videos/generations ✓ completed"*) with `#fffdf8` surface cards, `#ffcc00` accents, and `tfit_300d5b1f-module__eNyfuq__cla... { font-family:Outfit,Outfit Fallback;font-style:normal }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.py-16> — `Integration in 4 steps`)` uses `3.35544e+07px`, `var(--radius)`, `.25rem`, `var(--cell-radius)` radii, `#ffcc00` highlights, and assets (0c8c4ded07fff55c-s.p.2tcyrya9o07v..., 1b99372b3eaef0c8-s.p.1gsd1jahc5dg..., 70bc3e132a0a741e-s.p.3t6q91iet4ns...).
5. **Colophon & Global Directory Footer (<footer.sr-chrome-dark> — `https://seedrouter.ai`)**:
   - DOM & Selectors: Landmark `<footer class="sr-chrome-dark relative">` anchoring `SeedRouter · One API for Image, ` footer links (`SeedRouter · Models · Pricing · Docs · Sign up`), copy *"$ POST /v1/videos/generations"*, and `#e2ded4` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.sr-chrome-dark> — `https://seedrouter.ai`)` aligns to `96rem` (non-`@media` desktop container stylesheet rule) with `var(--card-spacing)` lateral canvas padding with `20px` grid gap and attributes (data-precedence="next", data-precedence="next", data-testid="announcement-dismiss").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"01 · Image, video, language and audio · one key"*
- Copy Excerpt 2: *"Generate and edit video from text or a first frame, at the resolutions and duratio..."*
- Copy Excerpt 3: *"$ POST /v1/videos/generations ✓ completed"*
- Copy Excerpt 4: *"$ POST /v1/videos/generations"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.22,1,.36,1)`
- **Extracted Stylesheet Rules (`seedrouter-ai`)**:
- `mono_744f2078-module__kLS_DW__cla... { font-family:JetBrains Mono,JetBrains Mono Fallback;font-style:normal }`
- `mono_744f2078-module__kLS_DW__var... { --font-code:"JetBrains Mono", "JetBrains Mono Fallback" }`
- `tfit_300d5b1f-module__eNyfuq__cla... { font-family:Outfit,Outfit Fallback;font-style:normal }`
- `utfit_300d5b1f-module__eNyfuq__va... { --font-outfit:"Outfit", "Outfit Fallback" }`
- `t323_f18b1ad5-module__HgsYcq__cla... { font-family:VT323,VT323 Fallback;font-style:normal;font-weight:400 }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: .15s` extracted from `seedrouter-ai` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `seedrouter-ai` stylesheet.
- **Selector `transform\]`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `seedrouter-ai` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<header.sr-chrome>` and `<section.pb-16>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `native` vertical progression up to `10641px` across 8 distinct viewport chapters.
- **Vertical Chapter Sequence**: SeedRouter: one API for eve... (0%) -> Models you can call on Seed... (9%) -> Choose your integration (26%) -> AI Image, Video and Text Mo... (44%) -> Pay per use. No subscription. (61%) -> Latest from the blog (79%) -> Footer (96%) -> Footer (100%).
- **Navigation Drawer / Menu State**: Replicate interactive menu toggle (`Tools`) with Escape-to-close keyboard handling.
- **Hover Micro-Interaction (`primary_cta`)**: Animate `boxShadow` with `0.2s cubic-bezier(0.4, 0, 0.2, 1)`.
- **Multi-Page Routes**: Scaffold internal routes `/pricing` (listing, SPA), `/models/seedance-2-5` (detail, direct), `/about` (about, direct) sharing the global header/footer shell and design tokens.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `seedrouter-ai`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `0px` | `0%` | SeedRouter: one API for every model your prod... | `1` | [desktop-step-01.webp](assets/desktop-step-01.webp) |
| `#02` | `850px` | `9%` | Models you can call on SeedRouter today | `1` | [desktop-step-02.webp](assets/desktop-step-02.webp) |
| `#03` | `2550px` | `26%` | Choose your integration | `1` | [desktop-step-03.webp](assets/desktop-step-03.webp) |
| `#04` | `4250px` | `44%` | AI Image, Video and Text Models | `1` | [desktop-step-04.webp](assets/desktop-step-04.webp) |
| `#05` | `5950px` | `61%` | Pay per use. No subscription. | `1` | [desktop-step-05.webp](assets/desktop-step-05.webp) |
| `#06` | `7650px` | `79%` | Latest from the blog | `1` | [desktop-step-06.webp](assets/desktop-step-06.webp) |
| `#07` | `9350px` | `96%` | Footer | `1` | [desktop-step-07.webp](assets/desktop-step-07.webp) |
| `#08` | `9741px` | `100%` | Footer | `1` | [desktop-step-08.webp](assets/desktop-step-08.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `0px` | `0%` | SeedRouter: one API for every model your... | [mobile-step-01.webp](assets/mobile-step-01.webp) |
| `#02` | `7200px` | `50%` | Prepaid, never expires | [mobile-step-02.webp](assets/mobile-step-02.webp) |
| `#03` | `14400px` | `100%` | Latest from the blog | [mobile-step-03.webp](assets/mobile-step-03.webp) |

### Interactive UI State Captures (`1440×900` WebP)
| State Type | Trigger / Observation | Visual Asset |
| :--- | :--- | :--- |
| `nav_menu` | Nav/Menu opened (`Tools`, diff `10.331`) | [state-nav.webp](assets/state-nav.webp) |

### Internal Subpage Filmstrips (`1080px` Wide WebP)
| # | Template | Route URL | H1 / Title | Scroll Height | Transition | Filmstrip Asset |
| :-: | :---: | :--- | :--- | :---: | :---: | :--- |
| `1` | `listing` | `https://seedrouter.ai/pricing` | Pay per use. No subscription. | `12391px` | `SPA` (`1928ms`) | [subpage-01-pricing.webp](assets/subpage-01-pricing.webp) |
| `2` | `detail` | `https://seedrouter.ai/models/seedance-2-5` | Seedance 2.5 — longer video with edit... | `14748px` | `direct` (`3448ms`) | [subpage-02-models-seedance-2-5.webp](assets/subpage-02-models-seedance-2-5.webp) |
| `3` | `about` | `https://seedrouter.ai/about` | About SeedRouter | `4136px` | `direct` (`1745ms`) | [subpage-03-about.webp](assets/subpage-03-about.webp) |

