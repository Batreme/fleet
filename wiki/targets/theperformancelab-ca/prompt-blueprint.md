---
title: "UI Prompt Blueprint: theperformancelab-ca"
date: 2026-11-24
captured_at: 2026-11-24
target: "theperformancelab-ca"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
capture_mode: behavioral_journey_v2
asset_format: webp
scroll_driver: wheel
desktop_keyframes: 2
subpages_crawled: 3
http_status: 200
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#171717` canvas, `#f2f2f2` ink, `#ff0000` accent)"
---

# UI Design System & Master Generation Blueprint: theperformancelab-ca

> **The Performance Lab — Sports Science & Athletic Testing in Toronto** (https://theperformancelab.ca/) — The Performance Lab is a Toronto sports science centre offering 3D motion-capture testing, performance training, and sports therapy — tru...

![Desktop Journey Filmstrip (1280x1656)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x2616)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **The Performance Lab — Sports Science & Athletic Testing in Toronto** (`https://theperformancelab.ca/`). The Performance Lab is a Toronto sports science centre offering 3D motion-capture testing, performance training, and sports therapy — tru...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#171717` canvas, `#f2f2f2` ink, `#ff0000` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#171717` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#f2f2f2` primary typography and `#ff0000` accents.
  - **Grounded Typographic Hierarchy**: Uses `display` across display (`UNLOCKNEXT LEVELPERFORMANCE`) and body copy, paired with `mono` for monospace/code.
  - **Calibrated Spatial Grid & Motion**: Combines `96rem` container bounds (`gap: 12px`, padding `21px`) with `cubic-bezier(.4,0,1,1)` easing and Lenis Smooth Scroll (`data-lenis`).

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×1656px` (`assets/desktop-journey.webp`, `2` keyframes up to `y=750px` / doc `10368px`), Mobile `390×2616px` (`assets/mobile-journey.webp`, `3` keyframes).
- **Master Container Bounds**: `96rem` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `21px` lateral canvas padding with `12px` grid gap.
- **Border Radius Scale**: `0px` (sharp unrounded corners).

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 96rem`, `gap: 12px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `21px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#171717` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#f2f2f2` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#000000` | `20 { background-color: black }` (`#000000`) |
| **Interactive Accent / Highlight** | `#ff0000` | `:hover { background-color: red }` (`#ff0000`) |
| **Secondary / Muted Copy** | `#bbbbbb` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#bbbbbb` | hairline divider derived from live computed `p` `color` (`computed_styles.json`) |
| **Variable Token (`--color-base-white-01`)** | `#e0e0e0` | `var(--color-base-white-01)` in `:root` |
| **Variable Token (`--color-neutral-grey`)** | `#979797` | `var(--color-neutral-grey)` in `:root` |
| **Variable Token (`--color-neutral-grey-01`)** | `#727272` | `var(--color-neutral-grey-01)` in `:root` |
| **Variable Token (`--color-neutral-grey-03`)** | `#292929` | `var(--color-neutral-grey-03)` in `:root` |
| **Variable Token (`--color-performance-red`)** | `#ff350d` | `var(--color-performance-red)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-base-white` | `#f2f2f2` | Canvas / Surface Token |
| `--color-base-white-01` | `#e0e0e0` | Canvas / Surface Token |
| `--color-base-white-02` | `#bbb` | Canvas / Surface Token |
| `--color-neutral-grey` | `#979797` | Brand / Palette Token |
| `--color-neutral-grey-01` | `#727272` | Brand / Palette Token |
| `--color-neutral-grey-03` | `#292929` | Brand / Palette Token |
| `--color-core-black` | `#171717` | Canvas / Surface Token |
| `--color-performance-red` | `#ff350d` | Brand / Palette Token |
| `--font-display` | `var(--font-display-family)` | Typography / Scale Token |
| `--font-mono` | `var(--font-mono-family)` | Typography / Scale Token |
| `--font-diatype` | `var(--font-diatype-family)` | Typography / Scale Token |
| `--ease-out-expo` | `cubic-bezier(.16,1,.3,1)` | Motion / Easing Token |
| `--ease-in-out-quart` | `cubic-bezier(.76,0,.24,1)` | Motion / Easing Token |
| `--background` | `var(--color-core-black)` | Canvas / Surface Token |
| `--foreground` | `var(--color-base-white)` | Typography Ink Token |
| `--font-display-family` | `"display","display Fallback"` | Typography / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `display`.
- **Primary Body Stack**: `display`.
- **Technical / Metadata Stack**: `mono`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 39px`, `line-height: 31.2px`, `font-weight: 500`, `letter-spacing: -1.56px`); CSS variables `--font-display: var(--font-display-family)`, `--font-display-family: "display","display Fallback"`.
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 135px`, `line-height: 108px`, `font-weight: 500`, `letter-spacing: -5.4px`).
- **Body Copy**: live computed `body` (`font-size: 12px`, `line-height: 18px`, `font-weight: 400`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 12px`, `line-height: 18px`, `font-weight: 400`); CSS variables `--font-mono: var(--font-mono-family)`, `--font-mono-family: "mono","mono Fallback"`, `--default-mono-font-family: var(--font-mono)`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: .15s` extracted from `theperformancelab-ca` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `theperformancelab-ca` stylesheet.
- **Selector `.transition-\[filter\]`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `theperformancelab-ca` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,1,1)`)**: Governs interactive state transitions across `<header.inset-x-0>` and `<section.hidden>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`) with `prefers-reduced-motion: reduce` fallback guards.
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `wheel` (max document height `10368px`, deepest scrollY reached `750px` across `2` desktop keyframes).
- **Detected Scroll / Motion Libraries**: `Lenis`.
- **Interactive Control Probe (`carousel_next`)**: Tested `Next testimonial` (diff `0.0`).
- **Route Transition Architecture**: First internal navigation (`/blog`) measured as `direct` in `2278ms`.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — The Performance Lab — Sports Science & Ath │
│ ====================================================================== │
│ [ <header.inset-x-0> (1440x62px)      | H O M E · W H O W E A R E ·  ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.mx-auto> (w=1440px)                           | │
│ | H1: UNLOCKNEXT LEVELPERFORMANCE                                    | │
│ | Substrate: #171717 | Ink: #f2f2f2 | Accent: #ff0000                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.hidden>) max-w: 96rem                      | │
│ | +------------------------------+  +------------------------------+ | │
│ | | UNLOCK NEXT LEVEL PERFORMANC |  | Helping you move better, rec | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.relative>) — Reach your goals. Whe         | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.mx-auto>    ) | https://theperformancelab.ca/        │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 12px)       │
│ ====================================================================== │
│ [ HEADER BAR (<header.inset-x-0>      ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.mx-auto>) — 390px Vertical Lead               | │
│ | H1: UNLOCKNEXT LEVELPERFORMANCE                                    | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.hidden>) — 1-Col Stack                    | │
│ | [ Item 1: UNLOCK NEXT LEVEL PERFORMANCE                          ] | │
│ | [ Item 2: Helping you move better, recover smarter, and per...   ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.relative>) — 1-Col (Reach your goals. )     | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.mx-auto>    ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.inset-x-0> — `theperformancelab-ca`)**:
   - Landmark `<header class="inset-x-0 top-0">` (`1440x62px`) hosting `The Performance Lab — Sports Science` navigation (`H O M E · W H O W E A R E · B L O G · C O N T A C T`), DOM attributes (`data-precedence="next"`, `data-theme="dark"`, `data-services-open="false"`, `data-scroll-state="false"`), and stylesheet rule `.__className_9dcdb7 { font-family:display,display Fallback }`.
2. **Hero Stage & Focal Lead (<section.mx-auto> — `UNLOCKNEXT LEVELPERFORMANCE`)**:
   - Landmark `<section class="mx-auto relative">` presenting display lead `UNLOCKNEXT LEVELPERFORMANCE` and copy excerpt *"EVERYTHING YOUR BODY NEEDS TO PERFORM, RECOVER, AND LAST."* over `#171717` canvas and `#f2f2f2` ink.
3. **Primary Showcase & Content Grid (<section.hidden> — `UNLOCK NEXT LEVEL PERFORMANCE`)**:
   - Landmark `<section class="hidden relative">` rendering section `UNLOCK NEXT LEVEL PERFORMANCE` with copy *"B O O K A C O N S U L T A T I O N"*, asset references (`desktop.jpg`, `i1.webp`, `i2.webp`, `i3.webp`), and grid rule `.__variable_9dcdb7 { --font-display-family:"display","display Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.relative> — `Helping you move better, recover s`)**:
   - Landmark `<section class="mx-auto relative">` framing `Helping you move better, recover smarter, and per...` and `Reach your goals. Whether you’re pursuing profess...` (*"Everything your body needs to perform, recover, and last."*) with `#000000` surface cards, `#ff0000` accents, and `.__className_ac1fe6 { font-family:mono,mono Fallback;font-weight:400;font-style:normal }`.
5. **Colophon & Global Directory Footer (<footer.mx-auto> — `https://theperformancelab.ca/`)**:
   - Landmark `<footer class="mx-auto flex">` anchoring `The Performance Lab — Sports Sci` footer links (`H O M E · W H O W E A R E · B L O G · C O N T A C T`), copy *"The Performance Lab specializes in elite diagnostics, person"*, and `#bbbbbb` structural dividers.
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=0px`, `0%`): Active landmark `Hero` · sticky/fixed elements: `1`
- **Step 02** (`y=750px`, `7%`): Active landmark `Hero` · sticky/fixed elements: `1`

### Multi-Page Internal Route Map
- **Listing Route (`/blog`)**: `https://theperformancelab.ca/blog` — H1: `INSIGHTS FROM THE LAB`, scrollHeight `3259px`, transition `direct` (`2278ms`)
- **About Route (`/about`)**: `https://theperformancelab.ca/about` — H1: `BEYOND THE LIMITS OF HUMAN PERFORMANCE`, scrollHeight `8967px`, transition `direct` (`841ms`)
- **Listing Route (`/services/testing`)**: `https://theperformancelab.ca/services/testing` — H1: `PERFORMANCETESTING`, scrollHeight `10881px`, transition `direct` (`457ms`)

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: theperformancelab-ca (The Performance Lab — Sports Science & Athletic Testing in Toronto)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `theperformancelab-ca` (**The Performance Lab — Sports Science & Athletic Testing in Toronto** — `https://theperformancelab.ca/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#171717` canvas, `#f2f2f2` ink, `#ff0000` accent).
- **Identity & Domain Context**: The Performance Lab is a Toronto sports science centre offering 3D motion-capture testing, performance training, and sports therapy — tru...
- **Primary Substrate**: `#171717` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#f2f2f2`, **Accent / Highlight**: `#ff0000`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#171717` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#f2f2f2` primary typography and `#ff0000` accents.
  - **Grounded Typographic Hierarchy**: Uses `display` across display (`UNLOCKNEXT LEVELPERFORMANCE`) and body copy, paired with `mono` for monospace/code.
  - **Calibrated Spatial Grid & Motion**: Combines `96rem` container bounds (`gap: 12px`, padding `21px`) with `cubic-bezier(.4,0,1,1)` easing and Lenis Smooth Scroll (`data-lenis`).

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `theperformancelab-ca` in your global stylesheet:

:root {
  /* The Performance Lab — Sports Science & Athletic Testing in Toronto (theperformancelab-ca) — Live-Grounded CSS Variables */
  --color-base-white: #f2f2f2; /* Canvas / Surface Token (theperformancelab-ca) */
  --color-base-white-01: #e0e0e0; /* Canvas / Surface Token (theperformancelab-ca) */
  --color-base-white-02: #bbb; /* Canvas / Surface Token (theperformancelab-ca) */
  --color-neutral-grey: #979797; /* Brand / Palette Token (theperformancelab-ca) */
  --color-neutral-grey-01: #727272; /* Brand / Palette Token (theperformancelab-ca) */
  --color-neutral-grey-03: #292929; /* Brand / Palette Token (theperformancelab-ca) */
  --color-core-black: #171717; /* Canvas / Surface Token (theperformancelab-ca) */
  --color-performance-red: #ff350d; /* Brand / Palette Token (theperformancelab-ca) */
  --font-display: var(--font-display-family); /* Typography / Scale Token (theperformancelab-ca) */
  --font-mono: var(--font-mono-family); /* Typography / Scale Token (theperformancelab-ca) */
  --font-diatype: var(--font-diatype-family); /* Typography / Scale Token (theperformancelab-ca) */
  --ease-out-expo: cubic-bezier(.16,1,.3,1); /* Motion / Easing Token (theperformancelab-ca) */
  --ease-in-out-quart: cubic-bezier(.76,0,.24,1); /* Motion / Easing Token (theperformancelab-ca) */
  --background: var(--color-core-black); /* Canvas / Surface Token (theperformancelab-ca) */
  --foreground: var(--color-base-white); /* Typography Ink Token (theperformancelab-ca) */
  --font-display-family: "display","display Fallback"; /* Typography / Scale Token (theperformancelab-ca) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#171717` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#f2f2f2` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#000000` — grounded in `20 { background-color: black }` (`#000000`)
- **Interactive Accent / Highlight**: `#ff0000` — grounded in `:hover { background-color: red }` (`#ff0000`)
- **Secondary / Muted Copy**: `#bbbbbb` — grounded in live computed `p` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#bbbbbb` — grounded in hairline divider derived from live computed `p` `color` (`computed_styles.json`)
- **Variable Token (`--color-base-white-01`)**: `#e0e0e0` — grounded in `var(--color-base-white-01)` in `:root`
- **Variable Token (`--color-neutral-grey`)**: `#979797` — grounded in `var(--color-neutral-grey)` in `:root`
- **Variable Token (`--color-neutral-grey-01`)**: `#727272` — grounded in `var(--color-neutral-grey-01)` in `:root`
- **Variable Token (`--color-neutral-grey-03`)**: `#292929` — grounded in `var(--color-neutral-grey-03)` in `:root`
- **Variable Token (`--color-performance-red`)**: `#ff350d` — grounded in `var(--color-performance-red)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1280×1656px` (full-page live capture (1656px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2616px` (multi-frame vertical journey filmstrip (2616px), `390px` standard mobile width).
- **Container Max-Width**: `96rem` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `21px` lateral canvas padding with `12px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 96rem`, `gap: 12px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `21px` horizontal padding
- **Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)`
- **Corner Radii**: `0px` (sharp unrounded corners)

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `display`
- **Body Font Stack**: `display`
- **Monospace / Technical Font Stack**: `mono`
- **H1 Display Rule**: live computed `h1` (`font-size: 39px`, `line-height: 31.2px`, `font-weight: 500`, `letter-spacing: -1.56px`); CSS variables `--font-display: var(--font-display-family)`, `--font-display-family: "display","display Fallback"`
- **H2 Section Rule**: live computed `h2` (`font-size: 135px`, `line-height: 108px`, `font-weight: 500`, `letter-spacing: -5.4px`)
- **Body Copy Rule**: live computed `body` (`font-size: 12px`, `line-height: 18px`, `font-weight: 400`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 12px`, `line-height: 18px`, `font-weight: 400`); CSS variables `--font-mono: var(--font-mono-family)`, `--font-mono-family: "mono","mono Fallback"`, `--default-mono-font-family: var(--font-mono)`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `theperformancelab-ca` (`The Performance Lab — Sports Science & Athletic Testing in Toronto`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.inset-x-0> — `theperformancelab-ca`)**:
   - DOM & Selectors: Landmark `<header class="inset-x-0 top-0">` (`1440x62px`) hosting `The Performance Lab — Sports Science` navigation (`H O M E · W H O W E A R E · B L O G · C O N T A C T`), DOM attributes (`data-precedence="next"`, `data-theme="dark"`, `data-services-open="false"`, `data-scroll-state="false"`), and stylesheet rule `.__className_9dcdb7 { font-family:display,display Fallback }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.inset-x-0> — `theperformancelab-ca`)` (`theperformancelab-ca`) adapts across `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)` with `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)` transitions and links `H O M E · W H O W E A R E · B L O G · C O N T A C T`.
2. **Hero Stage & Focal Lead (<section.mx-auto> — `UNLOCKNEXT LEVELPERFORMANCE`)**:
   - DOM & Selectors: Landmark `<section class="mx-auto relative">` presenting display lead `UNLOCKNEXT LEVELPERFORMANCE` and copy excerpt *"EVERYTHING YOUR BODY NEEDS TO PERFORM, RECOVER, AND LAST."* over `#171717` canvas and `#f2f2f2` ink.
   - Responsive Contract: Hero stage (`1280×1656px` desktop / `390×2616px` mobile) sets `#171717` background with `#f2f2f2` headline `UNLOCKNEXT LEVELPERFORMANCE`.
3. **Primary Showcase & Content Grid (<section.hidden> — `UNLOCK NEXT LEVEL PERFORMANCE`)**:
   - DOM & Selectors: Landmark `<section class="hidden relative">` rendering section `UNLOCK NEXT LEVEL PERFORMANCE` with copy *"B O O K A C O N S U L T A T I O N"*, asset references (`desktop.jpg`, `i1.webp`, `i2.webp`, `i3.webp`), and grid rule `.__variable_9dcdb7 { --font-display-family:"display","display Fallback" }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.hidden> — `UNLOCK NEXT LEVEL PERFORMANCE`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 96rem`, `gap: 12px`) on desktop and Single-column vertical stack at `390px` viewport width with `21px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.relative> — `Helping you move better, recover s`)**:
   - DOM & Selectors: Landmark `<section class="mx-auto relative">` framing `Helping you move better, recover smarter, and per...` and `Reach your goals. Whether you’re pursuing profess...` (*"Everything your body needs to perform, recover, and last."*) with `#000000` surface cards, `#ff0000` accents, and `.__className_ac1fe6 { font-family:mono,mono Fallback;font-weight:400;font-style:normal }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.relative> — `Helping you move better, recover s`)` uses `0px` (sharp unrounded corners) radii, `#ff0000` highlights, and assets (desktop.jpg, i1.webp, i2.webp).
5. **Colophon & Global Directory Footer (<footer.mx-auto> — `https://theperformancelab.ca/`)**:
   - DOM & Selectors: Landmark `<footer class="mx-auto flex">` anchoring `The Performance Lab — Sports Sci` footer links (`H O M E · W H O W E A R E · B L O G · C O N T A C T`), copy *"The Performance Lab specializes in elite diagnostics, person"*, and `#bbbbbb` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.mx-auto> — `https://theperformancelab.ca/`)` aligns to `96rem` (non-`@media` desktop container stylesheet rule) with `21px` lateral canvas padding with `12px` grid gap and attributes (data-precedence="next", data-theme="dark", data-services-open="false").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"EVERYTHING YOUR BODY NEEDS TO PERFORM, RECOVER, AND LAST."*
- Copy Excerpt 2: *"B O O K A C O N S U L T A T I O N"*
- Copy Excerpt 3: *"Everything your body needs to perform, recover, and last."*
- Copy Excerpt 4: *"The Performance Lab specializes in elite diagnostics, personalized training, and a..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`
- **Extracted Stylesheet Rules (`theperformancelab-ca`)**:
- `.__className_9dcdb7 { font-family:display,display Fallback }`
- `.__variable_9dcdb7 { --font-display-family:"display","display Fallback" }`
- `.__className_ac1fe6 { font-family:mono,mono Fallback;font-weight:400;font-style:normal }`
- `.__variable_ac1fe6 { --font-mono-family:"mono","mono Fallback" }`
- `.__className_fdb907 { font-family:diatype,diatype Fallback;font-weight:400;font-style:normal }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: .15s` extracted from `theperformancelab-ca` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `theperformancelab-ca` stylesheet.
- **Selector `.transition-\[filter\]`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `theperformancelab-ca` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,1,1)`)**: Governs interactive state transitions across `<header.inset-x-0>` and `<section.hidden>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`) with `prefers-reduced-motion: reduce` fallback guards.
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `wheel` vertical progression up to `10368px` across 2 distinct viewport chapters using Lenis.
- **Vertical Chapter Sequence**: Hero (0%) -> Hero (7%).
- **Multi-Page Routes**: Scaffold internal routes `/blog` (listing, direct), `/about` (about, direct), `/services/testing` (listing, direct) sharing the global header/footer shell and design tokens.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `theperformancelab-ca`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `0px` | `0%` | Hero | `1` | [desktop-step-01.webp](assets/desktop-step-01.webp) |
| `#02` | `750px` | `7%` | Hero | `1` | [desktop-step-02.webp](assets/desktop-step-02.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `0px` | `0%` | UNLOCK NEXT LEVEL PERFORMANCE | [mobile-step-01.webp](assets/mobile-step-01.webp) |
| `#02` | `5652px` | `50%` | #our-team-mobile | [mobile-step-02.webp](assets/mobile-step-02.webp) |
| `#03` | `11305px` | `100%` | Footer | [mobile-step-03.webp](assets/mobile-step-03.webp) |

### Internal Subpage Filmstrips (`1080px` Wide WebP)
| # | Template | Route URL | H1 / Title | Scroll Height | Transition | Filmstrip Asset |
| :-: | :---: | :--- | :--- | :---: | :---: | :--- |
| `1` | `listing` | `https://theperformancelab.ca/blog` | INSIGHTS FROM THE LAB | `3259px` | `direct` (`2278ms`) | [subpage-01-blog.webp](assets/subpage-01-blog.webp) |
| `2` | `about` | `https://theperformancelab.ca/about` | BEYOND THE LIMITS OF HUMAN PERFORMANCE | `8967px` | `direct` (`841ms`) | [subpage-02-about.webp](assets/subpage-02-about.webp) |
| `3` | `listing` | `https://theperformancelab.ca/services/testing` | PERFORMANCETESTING | `10881px` | `direct` (`457ms`) | [subpage-03-services-testing.webp](assets/subpage-03-services-testing.webp) |

