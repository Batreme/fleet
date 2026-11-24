---
title: "UI Prompt Blueprint: www-andriimur-com"
date: 2026-11-24
captured_at: 2026-11-24
target: "www-andriimur-com"
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
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#262626` canvas, `#ffffff` ink, `#829f62` accent)"
---

# UI Design System & Master Generation Blueprint: www-andriimur-com

> **Andrii Mur** (https://www.andriimur.com/) — Andrii Mur – Ukrainian street & documentary photographer in Tallinn, Estonia. From the information mess to how it feels to be Alive in an...

![Desktop Journey Filmstrip (1280x6624)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x2616)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Andrii Mur** (`https://www.andriimur.com/`). Andrii Mur – Ukrainian street & documentary photographer in Tallinn, Estonia. From the information mess to how it feels to be Alive in an...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#262626` canvas, `#ffffff` ink, `#829f62` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#262626` (live computed `html` `background-color` (`computed_styles.json`)) paired with `#ffffff` primary typography and `#829f62` accents.
  - **Grounded Typographic Hierarchy**: Uses `Inter` across display (`Andrii Mur`) and body copy, paired with `IBM Plex Mono` for monospace/code.
  - **Calibrated Spatial Grid & Motion**: Combines `96rem` container bounds (`gap: normal 20px`, padding `64px`) with `cubic-bezier(0,0,.2,1)` easing.

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×6624px` (`assets/desktop-journey.webp`, `8` keyframes up to `y=7119px` / doc `8019px`), Mobile `390×2616px` (`assets/mobile-journey.webp`, `3` keyframes).
- **Master Container Bounds**: `96rem` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `64px` lateral canvas padding with `normal 20px` grid gap.
- **Border Radius Scale**: `.25rem`, `3px`, `var(--radius-lg)`, `var(--radius-md)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: 2-column persistent left sidebar (`364px`, <nav.inset-0>) + `1076px` main content stage at `1440px` (`max-width: 96rem`, `gap: normal 20px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with collapsed `<nav.inset-0>` drawer navigation and `64px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#262626` | live computed `html` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `header` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#000000` | `var(--pswp-bg)` in `:root` |
| **Interactive Accent / Highlight** | `#829f62` | `var(--color-accent)` in `:root` |
| **Secondary / Muted Copy** | `#9ca3af` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#4f4f4f` | `var(--pswp-icon-stroke-color)` in `:root` |
| **Variable Token (`--color-yellow-100`)** | `#fef9c2` | `var(--color-yellow-100)` in `:root` |
| **Variable Token (`--color-yellow-700`)** | `#a36100` | `var(--color-yellow-700)` in `:root` |
| **Variable Token (`--color-blue-500`)** | `#3080ff` | `var(--color-blue-500)` in `:root` |
| **Variable Token (`--color-blue-800`)** | `#193cb8` | `var(--color-blue-800)` in `:root` |
| **Variable Token (`--color-slate-200`)** | `#e2e8f0` | `var(--color-slate-200)` in `:root` |
| **Variable Token (`--color-gray-50`)** | `#f9fafb` | `var(--color-gray-50)` in `:root` |
| **Variable Token (`--color-gray-100`)** | `#f3f4f6` | `var(--color-gray-100)` in `:root` |
| **Variable Token (`--color-gray-200`)** | `#e5e7eb` | `var(--color-gray-200)` in `:root` |
| **Variable Token (`--color-gray-300`)** | `#d1d5dc` | `var(--color-gray-300)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--z-page-background` | `-1` | Canvas / Surface Token |
| `--z-chrome` | `10` | Elevation / Border Token |
| `--z-overlay` | `15` | Elevation / Border Token |
| `--vf-dial-gutter` | `2.75rem` | Layout / Spatial Grid Token |
| `--vf-frame-max-w` | `min(calc(100cqh * 1.5), calc(100cqw - var(--vf-dial-gutter) * 2))` | Layout / Spatial Grid Token |
| `--vf-dial-inset` | `max(1rem, calc(50vw - 75svh - var(--vf-dial-gutter)))` | Dimension / Scale Token |
| `--font-serif` | `ui-serif, Georgia, Cambria, "Times New Roman", Times, serif` | Typography / Scale Token |
| `--color-yellow-100` | `#fef9c2` | Brand / Palette Token |
| `--color-yellow-700` | `#a36100` | Brand / Palette Token |
| `--color-blue-500` | `#3080ff` | Brand / Palette Token |
| `--color-blue-800` | `#193cb8` | Brand / Palette Token |
| `--color-slate-200` | `#e2e8f0` | Brand / Palette Token |
| `--color-gray-50` | `#f9fafb` | Brand / Palette Token |
| `--color-gray-100` | `#f3f4f6` | Brand / Palette Token |
| `--color-gray-200` | `#e5e7eb` | Brand / Palette Token |
| `--color-gray-300` | `#d1d5dc` | Brand / Palette Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Inter`.
- **Primary Body Stack**: `Inter`.
- **Technical / Metadata Stack**: `IBM Plex Mono`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`.
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 48px`, `line-height: 48px`, `font-weight: 800`, `letter-spacing: -1.2px`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`.
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`.
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.4,0,.22,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: .15s` extracted from `www-andriimur-com` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `www-andriimur-com` stylesheet.
- **Selector `background-color\]`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `www-andriimur-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<header.top-0>` and `<section.snap-showcase>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<section.dark>` and `<section.snap-showcase>` interactive targets.
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `native` (max document height `8019px`, deepest scrollY reached `7119px` across `8` desktop keyframes).
- **Detected Scroll / Motion Libraries**: Native browser scroll / standard CSS transitions.
- **Nav / Drawer Probe (`Projects`)**: Triggered visual change (pixel diff `14.488`, captured in `assets/state-nav.webp`); revealed links: About, Monochrome Black and..., Drops of Melancholy E....
- **Hover Physics (`primary_cta` · `About`)**: `color`: `lab(65.9269 -0.832707 -...` -> `rgb(255, 255, 255)`; `borderColor`: `lab(65.9269 -0.832707 -...` -> `rgb(255, 255, 255)` (`transition-duration: 0s`, `timing: ease`).
- **Route Transition Architecture**: First internal navigation (`/projects/monochrome`) measured as `direct` in `1175ms`.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Sidebar (364px) + Main (1076px)            │
│ ====================================================================== │
│ +--[ SIDEBAR (364px) ]--+--[ MAIN CONTENT STAGE (1076px) ]-----------+ │
│ | <nav.inset-0>         | [ <header.top-0> | About · Monochrome ]    | │
│ | - About               | ------------------------------------------ | │
│ | - Monochrome          | HERO STAGE: <section.dark>                 | │
│ | - Drops of Melancholy | H1: Andrii Mur                             | │
│ | - XA-23.4°            | Bg:#262626 Ink:#ffffff Acc:#829f62         | │
│ | x=-388 h=772px rail   | ------------------------------------------ | │
│ |                       | SHOWCASE: <section.snap-showca max:96rem   | │
│ |                       | [Featured Work & In] [Technical Architec]  | │
│ |                       | DETAIL: <section.flex>                     | │
│ +-----------------------+--------------------------------------------+ │
│ [ FOOTER (<footer.bottom-0>   ) | https://www.andriimur.com/           │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Collapsed Sidebar + 1-Col Stack       │
│ ====================================================================== │
│ [ DRAWER (<nav.inset-0>         ) | <header.top-0>                     │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.dark>) — 390px Full-Width                     | │
│ | H1: Andrii Mur                                                     | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.snap-showcase) — 1-Col (gap: normal 20p)  | │
│ | [ Card 1: Featured Work & Interactive Showcase                   ] | │
│ | [ Card 2: Technical Architecture & Narrative                     ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.flex>) — 1-Col (Global Directory &)         | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.bottom-0>     ) | Stacked 390px Colophon             │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Persistent Left Sidebar Navigation (<nav.inset-0> — `364×772px` at `x=-388`)**:
   - Fixed/sticky left rail `<nav class="inset-0 items-end">` (`364px` wide) paired with top bar `<header class="top-0 gap-x-5">` hosting `Andrii Mur` navigation (`About · Monochrome · Drops of Melancholy · XA-23.4° · After Dusk`), DOM attributes (`data-theme="dark"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.dark> — `Andrii Mur`)**:
   - Landmark `<section class="dark">` inside `1076px` main stage presenting display lead `Andrii Mur` and copy excerpt *"Black and White singles"* over `#262626` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.snap-showcase> — `Featured Work & Interactive Showca`)**:
   - Landmark `<section class="snap-showcase">` rendering section `Featured Work & Interactive Showcase` with copy *"Tripod left at Home"*, asset references (`m2ak1cq3.api.sanity.io`, `6ab71d031fe7ae3b-s.p.141jscyq52bj...`, `80bb744e92754df7-s.p.2eihtoujcocl...`, `83afe278b6a6bb3c-s.p.2bn3s6zvc0dy...`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.flex> — `Technical Architecture & Narrative`)**:
   - Landmark `<section class="flex">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Between duality of Space and Time"*) with `#000000` surface cards, `#829f62` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.bottom-0> — `https://www.andriimur.com/`)**:
   - Landmark `<footer class="bottom-0 bg-neutral-900">` anchoring `Andrii Mur` footer links (`About · Monochrome · Drops of Melancholy · XA-23.4° · After Dusk`), copy *"a Quiet gaze from Within"*, and `#4f4f4f` structural dividers.
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=2px`, `0%`): Active landmark `Monochrome` · sticky/fixed elements: `1`
- **Step 02** (`y=653px`, `9%`): Active landmark `Drops of Melancholy` · sticky/fixed elements: `1`
- **Step 03** (`y=1961px`, `28%`): Active landmark `After Dusk` · sticky/fixed elements: `1`
- **Step 04** (`y=3269px`, `46%`): Active landmark `35mm` · sticky/fixed elements: `1`
- **Step 05** (`y=4250px`, `60%`): Active landmark `The Look From Silence` · sticky/fixed elements: `1`
- **Step 06** (`y=5885px`, `83%`): Active landmark `We are Ukrainians` · sticky/fixed elements: `1`
- **Step 07** (`y=6539px`, `92%`): Active landmark `Imaginary Friend` · sticky/fixed elements: `1`
- **Step 08** (`y=7119px`, `100%`): Active landmark `Colour Street` · sticky/fixed elements: `1`

### Multi-Page Internal Route Map
- **Detail Route (`/projects/monochrome`)**: `https://www.andriimur.com/projects/monochrome` — H1: `Monochrome · Andrii Mur`, scrollHeight `3115px`, transition `direct` (`1175ms`)
- **About Route (`/about`)**: `https://www.andriimur.com/about` — H1: `About · Andrii Mur`, scrollHeight `1994px`, transition `direct` (`1490ms`)
- **Detail Route (`/projects/drops-of-melancholy`)**: `https://www.andriimur.com/projects/drops-of-melancholy` — H1: `Drops of Melancholy · Andrii Mur`, scrollHeight `4105px`, transition `direct` (`702ms`)

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-andriimur-com (Andrii Mur)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-andriimur-com` (**Andrii Mur** — `https://www.andriimur.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#262626` canvas, `#ffffff` ink, `#829f62` accent).
- **Identity & Domain Context**: Andrii Mur – Ukrainian street & documentary photographer in Tallinn, Estonia. From the information mess to how it feels to be Alive in an...
- **Primary Substrate**: `#262626` (live computed `html` `background-color` (`computed_styles.json`)), **Primary Ink**: `#ffffff`, **Accent / Highlight**: `#829f62`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#262626` (live computed `html` `background-color` (`computed_styles.json`)) paired with `#ffffff` primary typography and `#829f62` accents.
  - **Grounded Typographic Hierarchy**: Uses `Inter` across display (`Andrii Mur`) and body copy, paired with `IBM Plex Mono` for monospace/code.
  - **Calibrated Spatial Grid & Motion**: Combines `96rem` container bounds (`gap: normal 20px`, padding `64px`) with `cubic-bezier(0,0,.2,1)` easing.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-andriimur-com` in your global stylesheet:

:root {
  /* Andrii Mur (www-andriimur-com) — Live-Grounded CSS Variables */
  --z-page-background: -1; /* Canvas / Surface Token (www-andriimur-com) */
  --z-chrome: 10; /* Elevation / Border Token (www-andriimur-com) */
  --z-overlay: 15; /* Elevation / Border Token (www-andriimur-com) */
  --vf-dial-gutter: 2.75rem; /* Layout / Spatial Grid Token (www-andriimur-com) */
  --vf-frame-max-w: min(calc(100cqh * 1.5), calc(100cqw - var(--vf-dial-gutter) * 2)); /* Layout / Spatial Grid Token (www-andriimur-com) */
  --vf-dial-inset: max(1rem, calc(50vw - 75svh - var(--vf-dial-gutter))); /* Dimension / Scale Token (www-andriimur-com) */
  --font-serif: ui-serif, Georgia, Cambria, "Times New Roman", Times, serif; /* Typography / Scale Token (www-andriimur-com) */
  --color-yellow-100: #fef9c2; /* Brand / Palette Token (www-andriimur-com) */
  --color-yellow-700: #a36100; /* Brand / Palette Token (www-andriimur-com) */
  --color-blue-500: #3080ff; /* Brand / Palette Token (www-andriimur-com) */
  --color-blue-800: #193cb8; /* Brand / Palette Token (www-andriimur-com) */
  --color-slate-200: #e2e8f0; /* Brand / Palette Token (www-andriimur-com) */
  --color-gray-50: #f9fafb; /* Brand / Palette Token (www-andriimur-com) */
  --color-gray-100: #f3f4f6; /* Brand / Palette Token (www-andriimur-com) */
  --color-gray-200: #e5e7eb; /* Brand / Palette Token (www-andriimur-com) */
  --color-gray-300: #d1d5dc; /* Brand / Palette Token (www-andriimur-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#262626` — grounded in live computed `html` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#ffffff` — grounded in live computed `header` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#000000` — grounded in `var(--pswp-bg)` in `:root`
- **Interactive Accent / Highlight**: `#829f62` — grounded in `var(--color-accent)` in `:root`
- **Secondary / Muted Copy**: `#9ca3af` — grounded in live computed `p` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#4f4f4f` — grounded in `var(--pswp-icon-stroke-color)` in `:root`
- **Variable Token (`--color-yellow-100`)**: `#fef9c2` — grounded in `var(--color-yellow-100)` in `:root`
- **Variable Token (`--color-yellow-700`)**: `#a36100` — grounded in `var(--color-yellow-700)` in `:root`
- **Variable Token (`--color-blue-500`)**: `#3080ff` — grounded in `var(--color-blue-500)` in `:root`
- **Variable Token (`--color-blue-800`)**: `#193cb8` — grounded in `var(--color-blue-800)` in `:root`
- **Variable Token (`--color-slate-200`)**: `#e2e8f0` — grounded in `var(--color-slate-200)` in `:root`
- **Variable Token (`--color-gray-50`)**: `#f9fafb` — grounded in `var(--color-gray-50)` in `:root`
- **Variable Token (`--color-gray-100`)**: `#f3f4f6` — grounded in `var(--color-gray-100)` in `:root`
- **Variable Token (`--color-gray-200`)**: `#e5e7eb` — grounded in `var(--color-gray-200)` in `:root`
- **Variable Token (`--color-gray-300`)**: `#d1d5dc` — grounded in `var(--color-gray-300)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1280×6624px` (multi-frame vertical journey filmstrip (6624px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2616px` (multi-frame vertical journey filmstrip (2616px), `390px` standard mobile width).
- **Container Max-Width**: `96rem` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `64px` lateral canvas padding with `normal 20px` grid gap
- **Desktop Grid**: 2-column persistent left sidebar (`364px`, <nav.inset-0>) + `1076px` main content stage at `1440px` (`max-width: 96rem`, `gap: normal 20px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with collapsed `<nav.inset-0>` drawer navigation and `64px` horizontal padding
- **Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)`
- **Corner Radii**: `.25rem`, `3px`, `var(--radius-lg)`, `var(--radius-md)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: `IBM Plex Mono`
- **H1 Display Rule**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`
- **H2 Section Rule**: live computed `h2` (`font-size: 48px`, `line-height: 48px`, `font-weight: 800`, `letter-spacing: -1.2px`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-andriimur-com` (`Andrii Mur`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Persistent Left Sidebar Navigation (<nav.inset-0> — `364×772px` at `x=-388`)**:
   - DOM & Selectors: Fixed/sticky left rail `<nav class="inset-0 items-end">` (`364px` wide) paired with top bar `<header class="top-0 gap-x-5">` hosting `Andrii Mur` navigation (`About · Monochrome · Drops of Melancholy · XA-23.4° · After Dusk`), DOM attributes (`data-theme="dark"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Header `Persistent Left Sidebar Navigation (<nav.inset-0> — `364×772px` at `x=-388`)` (`www-andriimur-com`) adapts across `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)` with `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.4,0,.22,1)` transitions and links `About · Monochrome · Drops of Melancholy · XA-23.4° · After Dusk`.
2. **Hero Stage & Focal Lead (<section.dark> — `Andrii Mur`)**:
   - DOM & Selectors: Landmark `<section class="dark">` inside `1076px` main stage presenting display lead `Andrii Mur` and copy excerpt *"Black and White singles"* over `#262626` canvas and `#ffffff` ink.
   - Responsive Contract: Hero stage (`1280×6624px` desktop / `390×2616px` mobile) sets `#262626` background with `#ffffff` headline `Andrii Mur`.
3. **Primary Showcase & Content Grid (<section.snap-showcase> — `Featured Work & Interactive Showca`)**:
   - DOM & Selectors: Landmark `<section class="snap-showcase">` rendering section `Featured Work & Interactive Showcase` with copy *"Tripod left at Home"*, asset references (`m2ak1cq3.api.sanity.io`, `6ab71d031fe7ae3b-s.p.141jscyq52bj...`, `80bb744e92754df7-s.p.2eihtoujcocl...`, `83afe278b6a6bb3c-s.p.2bn3s6zvc0dy...`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.snap-showcase> — `Featured Work & Interactive Showca`)` applies 2-column persistent left sidebar (`364px`, <nav.inset-0>) + `1076px` main content stage at `1440px` (`max-width: 96rem`, `gap: normal 20px`) on desktop and Single-column vertical stack at `390px` viewport width with collapsed `<nav.inset-0>` drawer navigation and `64px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.flex> — `Technical Architecture & Narrative`)**:
   - DOM & Selectors: Landmark `<section class="flex">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Between duality of Space and Time"*) with `#000000` surface cards, `#829f62` accents, and `strong { font-weight:bolder }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.flex> — `Technical Architecture & Narrative`)` uses `.25rem`, `3px`, `var(--radius-lg)`, `var(--radius-md)` radii, `#829f62` highlights, and assets (m2ak1cq3.api.sanity.io, 6ab71d031fe7ae3b-s.p.141jscyq52bj..., 80bb744e92754df7-s.p.2eihtoujcocl...).
5. **Colophon & Global Directory Footer (<footer.bottom-0> — `https://www.andriimur.com/`)**:
   - DOM & Selectors: Landmark `<footer class="bottom-0 bg-neutral-900">` anchoring `Andrii Mur` footer links (`About · Monochrome · Drops of Melancholy · XA-23.4° · After Dusk`), copy *"a Quiet gaze from Within"*, and `#4f4f4f` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.bottom-0> — `https://www.andriimur.com/`)` aligns to `96rem` (non-`@media` desktop container stylesheet rule) with `64px` lateral canvas padding with `normal 20px` grid gap and attributes (data-theme="dark", data-precedence="next", data-precedence="next").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Black and White singles"*
- Copy Excerpt 2: *"Tripod left at Home"*
- Copy Excerpt 3: *"Between duality of Space and Time"*
- Copy Excerpt 4: *"a Quiet gaze from Within"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.4,0,.22,1)`
- **Extracted Stylesheet Rules (`www-andriimur-com`)**:
- `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `strong { font-weight:bolder }`
- `small { font-size:80% }`
- `sup { vertical-align:baseline;font-size:75%;line-height:0;position:relative }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: .15s` extracted from `www-andriimur-com` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `www-andriimur-com` stylesheet.
- **Selector `background-color\]`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `www-andriimur-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0,0,.2,1)`)**: Governs interactive state transitions across `<header.top-0>` and `<section.snap-showcase>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<section.dark>` and `<section.snap-showcase>` interactive targets.
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `native` vertical progression up to `8019px` across 8 distinct viewport chapters.
- **Vertical Chapter Sequence**: Monochrome (0%) -> Drops of Melancholy (9%) -> After Dusk (28%) -> 35mm (46%) -> The Look From Silence (60%) -> We are Ukrainians (83%) -> Imaginary Friend (92%) -> Colour Street (100%).
- **Navigation Drawer / Menu State**: Replicate interactive menu toggle (`Projects`) with Escape-to-close keyboard handling.
- **Hover Micro-Interaction (`primary_cta`)**: Animate `color, borderColor` with `0s ease`.
- **Multi-Page Routes**: Scaffold internal routes `/projects/monochrome` (detail, direct), `/about` (about, direct), `/projects/drops-of-melancholy` (detail, direct) sharing the global header/footer shell and design tokens.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-andriimur-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `2px` | `0%` | Monochrome | `1` | [desktop-step-01.webp](assets/desktop-step-01.webp) |
| `#02` | `653px` | `9%` | Drops of Melancholy | `1` | [desktop-step-02.webp](assets/desktop-step-02.webp) |
| `#03` | `1961px` | `28%` | After Dusk | `1` | [desktop-step-03.webp](assets/desktop-step-03.webp) |
| `#04` | `3269px` | `46%` | 35mm | `1` | [desktop-step-04.webp](assets/desktop-step-04.webp) |
| `#05` | `4250px` | `60%` | The Look From Silence | `1` | [desktop-step-05.webp](assets/desktop-step-05.webp) |
| `#06` | `5885px` | `83%` | We are Ukrainians | `1` | [desktop-step-06.webp](assets/desktop-step-06.webp) |
| `#07` | `6539px` | `92%` | Imaginary Friend | `1` | [desktop-step-07.webp](assets/desktop-step-07.webp) |
| `#08` | `7119px` | `100%` | Colour Street | `1` | [desktop-step-08.webp](assets/desktop-step-08.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `0px` | `0%` | Monochrome | [mobile-step-01.webp](assets/mobile-step-01.webp) |
| `#02` | `1763px` | `50%` | 35mm | [mobile-step-02.webp](assets/mobile-step-02.webp) |
| `#03` | `3526px` | `100%` | Imaginary Friend | [mobile-step-03.webp](assets/mobile-step-03.webp) |

### Interactive UI State Captures (`1440×900` WebP)
| State Type | Trigger / Observation | Visual Asset |
| :--- | :--- | :--- |
| `nav_menu` | Nav/Menu opened (`Projects`, diff `14.488`) | [state-nav.webp](assets/state-nav.webp) |

### Internal Subpage Filmstrips (`1080px` Wide WebP)
| # | Template | Route URL | H1 / Title | Scroll Height | Transition | Filmstrip Asset |
| :-: | :---: | :--- | :--- | :---: | :---: | :--- |
| `1` | `detail` | `https://www.andriimur.com/projects/monochrome` | Monochrome · Andrii Mur | `3115px` | `direct` (`1175ms`) | [subpage-01-projects-monochrome.webp](assets/subpage-01-projects-monochrome.webp) |
| `2` | `about` | `https://www.andriimur.com/about` | About · Andrii Mur | `1994px` | `direct` (`1490ms`) | [subpage-02-about.webp](assets/subpage-02-about.webp) |
| `3` | `detail` | `https://www.andriimur.com/projects/drops-of-melancholy` | Drops of Melancholy · Andrii Mur | `4105px` | `direct` (`702ms`) | [subpage-03-projects-drops-of-melancholy.webp](assets/subpage-03-projects-drops-of-melancholy.webp) |

