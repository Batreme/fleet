---
title: "UI Prompt Blueprint: www-unimaticwatches-com"
date: 2026-11-15
target: "[[overview|www-unimaticwatches-com]]"
archetype: "Milanese Industrial Horology Lab & Srgb Color-Mix Token Architecture (`Helvetica Neue` + `JetBrains Mono`)"
---

# UI Design System & Master Generation Blueprint: www-unimaticwatches-com

> **UNIMATIC Watches · Italian Minimalist Tool Watch Lab** — An industrial-grade horological design lab built on a light laboratory gray substrate (`--color-bg: #F6F6F6`), pure black dial ink (`--color-ink: #000000`), high-visibility lume volt-lime (`--color-accent: #AFFF00`), and a mathematically derived `color-mix(in srgb, ...)` opacity token ladder.

![Desktop Viewport Capture (1440x4841)](file:///root/projects/fleet/wiki/targets/www-unimaticwatches-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **UNIMATIC Watches · Italian Minimalist Tool Watch Lab**. An industrial-grade horological design lab built on a light laboratory gray substrate (`--color-bg: #F6F6F6`), pure black dial ink (`--color-ink: #000000`), high-visibility lume volt-lime (`--color-accent: #AFFF00`), and a mathematically derived `color-mix(in srgb, ...)` opacity token ladder.
- **Visual Archetype**: **Milanese Industrial Horology Lab & Srgb Color-Mix Token Architecture (`Helvetica Neue` + `JetBrains Mono`)**.
- **Anti-AI-Slop Differentiators**:
  1. **Programmatic `color-mix(in srgb)` Opacity Ladder**: Instead of arbitrary hex grays, every border, surface, and muted text token is computed via CSS Color 4 `color-mix(in srgb, var(--color-ink) N%, transparent)` (`70%`, `50%`, `40%`, `30%`, `20%`, `15%`, `5%`).
  2. **Super-LumiNova Volt-Lime Accent (`--color-accent**: #AFFF00`)**: Mirrors military dive-watch lume against laboratory gray (`--color-bg: #F6F6F6`), silver media wells (`--color-media: #D9D9D9`), and stark black ink (`#000000`).
  3. **Floating Pill Navigation (`nav.header__nav.nav-pill`)**: Uses translucent frosted glass (`--color-glass-80: color-mix(in srgb, var(--color-glass-base) 80%, transparent)`) split into primary `.header__nav.nav-pill` and `.header__actions.nav-pill--sm`.
  4. **Technical Horology Spec Typography**: Pairs `"Helvetica Neue"` with `"JetBrains Mono"` and `"IBM Plex Mono"` for waterproof ratings (`H3: Waterproof checked`), reference numbers, and batch editions (`H1: New Langhe Collection`, `H2: The ICON collection`).

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x6103)](file:///root/projects/fleet/wiki/targets/www-unimaticwatches-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Full-Page Dimensions**: Desktop `1440×4841px` (`assets/desktop.png`), Mobile `390×6103px` (`assets/mobile.png`).
- **Master Container Bounds**: Full-width industrial grid with `@media (min-width:768px)` and `@media (max-width:1099px)` responsive breakpoints.
- **Canvas Lateral Padding & Spacing**: Fluid horizontal padding with `1px` `--color-hairline` cell borders.
- **Border Radius Scale**: Pill radius (`999px`) on `.nav-pill` and `.drawer__pill`; crisp `0px`–`4px` corners on watch specification plates.

### Responsive Breakpoint Architecture
- **Desktop Layout**: 4-column tool-watch reference grid and 2-column campaign split (`New Langhe Collection` / `The ICON collection`).
- **Mobile Layout**: Collapses below `@media (max-width:767px)` into `<nav class="header__mobile">` and 2-up/1-up product cards.
- **Extracted CSS Media Queries**: `@media (max-width:767px)`, `@media (min-width:768px)`, `@media (max-width:1099px)`, `@media (prefers-color-scheme:dark)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| Primary Lab Gray Substrate | `#F6F6F6` | `--color-bg` / `--color-surface-page` (`:root`) |
| Product Media Well Surface | `#D9D9D9` | `--color-media` (`:root`) |
| Pure White Glass Base | `#ffffff` | `--color-white` / `--color-glass-base` (`:root`) |
| Primary Dial Black Ink | `#000000` | `--color-ink` (`:root`) |
| Secondary Ink (70% Srgb Mix) | `color-mix(in srgb, var(--color-ink) 70%, transparent)` | `--color-ink-70` (`:root`) |
| Muted Spec Ink (50% Srgb Mix) | `color-mix(in srgb, var(--color-ink) 50%, transparent)` | `--color-ink-50` (`:root`) |
| Hairline Grid Rule (15% Srgb Mix) | `color-mix(in srgb, var(--color-ink) 15%, transparent)` | `--color-hairline` (`:root`) |
| Component Border (20% Srgb Mix) | `color-mix(in srgb, var(--color-ink) 20%, transparent)` | `--color-border` (`:root`) |
| Subtle Card Fill (5% Srgb Mix) | `color-mix(in srgb, var(--color-ink) 5%, transparent)` | `--color-surface` (`:root`) |
| Super-LumiNova Volt-Lime Accent | `#AFFF00` | `--color-accent` (`:root`) |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-bg` | `#F6F6F6` | Primary laboratory light gray background |
| `--color-surface-page` | `#F6F6F6` | Page wrapper background surface |
| `--color-ink` | `#000000` | Primary pure black typography & icon ink |
| `--color-accent` | `#AFFF00` | High-visibility Super-LumiNova volt-lime accent |
| `--color-media` | `#D9D9D9` | Neutral gray backdrop for studio watch photography |
| `--color-white` | `#ffffff` | Pure white highlight surface |
| `--color-ink-70` | `color-mix(in srgb, var(--color-ink) 70%, transparent)` | Secondary body copy ink (70% black) |
| `--color-ink-50` | `color-mix(in srgb, var(--color-ink) 50%, transparent)` | Muted specification label ink (50% black) |
| `--color-ink-30` | `color-mix(in srgb, var(--color-ink) 30%, transparent)` | Disabled / inactive slider control ink |
| `--color-hairline` | `color-mix(in srgb, var(--color-ink) 15%, transparent)` | 1px structural grid hairline rule |
| `--color-border` | `color-mix(in srgb, var(--color-ink) 20%, transparent)` | Interactive button & input border |
| `--color-surface` | `color-mix(in srgb, var(--color-ink) 5%, transparent)` | Subtle elevated spec table surface |
| `--color-scrim` | `color-mix(in srgb, var(--color-ink) 60%, transparent)` | Modal & drawer backdrop scrim |
| `--color-glass-base` | `#FFFFFF` | Base color for frosted navigation pills |
| `--color-glass-80` | `color-mix(in srgb, var(--color-glass-base) 80%, transparent)` | 80% translucent frosted pill background |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `"Helvetica Neue", Helvetica, Arial, sans-serif` (`--font-sans`).
- **Primary Body Stack**: `"Helvetica Neue", Helvetica, Arial, sans-serif` (`.t-body`).
- **Technical / Metadata Stack**: `"JetBrains Mono", "IBM Plex Mono", monospace` (`--font-mono`).

### Typographic Scale & Rules
- **Hero Display (`H1`)**: `clamp(2.25rem, 5vw, 4.25rem)`, `font-family: "Helvetica Neue", sans-serif`, `font-weight: 500`, `line-height: 1.02`, `letter-spacing: -0.03em` ("New Langhe Collection").
- **Section Heading (`H2`)**: `clamp(1.5rem, 3vw, 2.5rem)`, `font-family: "Helvetica Neue", sans-serif`, `font-weight: 500` ("The ICON collection").
- **Body Copy**: `0.9375rem (15px)`, `font-family: "Helvetica Neue", sans-serif`, `line-height: 1.55`, `color: var(--color-ink-70)`.
- **Metadata & Navigation Labels**: `0.75rem (12px)`, `font-family: "JetBrains Mono", "IBM Plex Mono", monospace`, `letter-spacing: 0.06em`, `text-transform: uppercase` (`Modello Uno`, `300m / 1000ft`, `Waterproof checked`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.2,.9,.3,1)` (snappy mechanical dial click), `cubic-bezier(1, 0, 0, 1)`, and `220ms ease` (`--transition`).

### Per-Element Transition & Choreography Rules
- `:root` base transition -> `220ms ease` (`--transition`)
- `.slider__ctrl` -> `transition: background-color var(--transition), color var(--transition)`
- `.drawer__pill` -> `transition: color var(--transition)` (volt-lime `#AFFF00` active badge state)
- `Gallery & Drawer slides` -> `cubic-bezier(.2,.9,.3,1)` and `cubic-bezier(.3, 0, 0, 1)`

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ <header class="shopify-section-group-header-group"> (Glass: --color-gl │
│   <nav class="header__nav nav-pill"> [Watches] [Langhe] [ICON] [Lab]   │
│   <nav class="header__actions nav-pill nav-pill--sm"> [Search] [Bag (0 │
├────────────────────────────────────────────────────────────────────────┤
│ <main id="MainContent" class="main"> (Substrate: --color-bg #F6F6F6)   │
│   Hero Campaign: H1: New Langhe Collection  [ Badge: --color-accent #A │
│   H3: Some landscapes are defined less by what can be seen than felt.  │
├────────────────────────────────────────────────────────────────────────┤
│ <section class="icon-collection"> H2: The ICON collection              │
│   [ U1-Classic (--color-media #D9D9D9) ] │ [ U2-Classic (JetBrains Mon │
│   Border: --color-hairline (15% ink)     │ [ H3: Waterproof checked 30 │
├────────────────────────────────────────────────────────────────────────┤
│ <nav class="footer-column__links t-body"> © UNIMATIC Viaulli Milan     │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Floating Glass Pill Header (`<nav class="header__nav nav-pill">` and `<nav class="header__actions nav-pill nav-pill--sm">`)**:
   - Dual floating pill bars rendered in `--color-glass-80` (`color-mix(in srgb, var(--color-glass-base) 80%, transparent)`) with `backdrop-filter: blur(12px)` and `<nav class="header__mobile">` fallback below `767px`.
2. **New Langhe Collection Hero (`<main id="MainContent" class="main">`)**:
   - Full-width editorial campaign on `--color-bg: #F6F6F6` featuring `H1: New Langhe Collection` and `H3: Some landscapes are defined less by what can be seen than by what can be felt.`
3. **The ICON Collection Matrix (`H2: The ICON collection`)**:
   - Modular 4-column horological catalog where each watch rests on a `--color-media: #D9D9D9` studio well bounded by `--color-hairline` (`15%` srgb mix) borders and `JetBrains Mono` reference numbers.
4. **Technical Quality Verification (`H3: Waterproof checked`)**:
   - Industrial testing callouts highlighting 300m water resistance, Italian assembly, `.slider__ctrl` controls, and `--color-accent: #AFFF00` status pills (`.drawer__pill`).
5. **Milanese Lab Footer (`<nav class="footer-column__links t-body">` and `.footer-utilities__legal`)**:
   - Clean multi-column Swiss-Italian directory on `--color-surface` (`5%` ink mix).

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-unimaticwatches-com (UNIMATIC Watches · Italian Minimalist Tool Watch Lab)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-unimaticwatches-com` (UNIMATIC Watches · Italian Minimalist Tool Watch Lab).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Milanese Industrial Horology Lab & Srgb Color-Mix Token Architecture (`Helvetica Neue` + `JetBrains Mono`).
- **Primary Substrate**: `#F6F6F6` (`--color-bg` / `--color-surface-page` (`:root`)), **Primary Ink**: `#000000`, **Accent / Highlight**: `#AFFF00`.
- **Site-Specific Differentiators**:
  1. **Programmatic `color-mix(in srgb)` Opacity Ladder**: Instead of arbitrary hex grays, every border, surface, and muted text token is computed via CSS Color 4 `color-mix(in srgb, var(--color-ink) N%, transparent)` (`70%`, `50%`, `40%`, `30%`, `20%`, `15%`, `5%`).
  2. **Super-LumiNova Volt-Lime Accent (`--color-accent**: #AFFF00`)**: Mirrors military dive-watch lume against laboratory gray (`--color-bg: #F6F6F6`), silver media wells (`--color-media: #D9D9D9`), and stark black ink (`#000000`).
  3. **Floating Pill Navigation (`nav.header__nav.nav-pill`)**: Uses translucent frosted glass (`--color-glass-80: color-mix(in srgb, var(--color-glass-base) 80%, transparent)`) split into primary `.header__nav.nav-pill` and `.header__actions.nav-pill--sm`.
  4. **Technical Horology Spec Typography**: Pairs `"Helvetica Neue"` with `"JetBrains Mono"` and `"IBM Plex Mono"` for waterproof ratings (`H3: Waterproof checked`), reference numbers, and batch editions (`H1: New Langhe Collection`, `H2: The ICON collection`).

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-unimaticwatches-com` in your global stylesheet:

:root {
  /* UNIMATIC Watches · Italian Minimalist Tool Watch Lab — Ground-Truth Extracted CSS Variables */
  --color-bg: #F6F6F6; /* Primary laboratory light gray background */
  --color-surface-page: #F6F6F6; /* Page wrapper background surface */
  --color-ink: #000000; /* Primary pure black typography & icon ink */
  --color-accent: #AFFF00; /* High-visibility Super-LumiNova volt-lime accent */
  --color-media: #D9D9D9; /* Neutral gray backdrop for studio watch photography */
  --color-white: #ffffff; /* Pure white highlight surface */
  --color-ink-70: color-mix(in srgb, var(--color-ink) 70%, transparent); /* Secondary body copy ink (70% black) */
  --color-ink-50: color-mix(in srgb, var(--color-ink) 50%, transparent); /* Muted specification label ink (50% black) */
  --color-ink-30: color-mix(in srgb, var(--color-ink) 30%, transparent); /* Disabled / inactive slider control ink */
  --color-hairline: color-mix(in srgb, var(--color-ink) 15%, transparent); /* 1px structural grid hairline rule */
  --color-border: color-mix(in srgb, var(--color-ink) 20%, transparent); /* Interactive button & input border */
  --color-surface: color-mix(in srgb, var(--color-ink) 5%, transparent); /* Subtle elevated spec table surface */
  --color-scrim: color-mix(in srgb, var(--color-ink) 60%, transparent); /* Modal & drawer backdrop scrim */
  --color-glass-base: #FFFFFF; /* Base color for frosted navigation pills */
  --color-glass-80: color-mix(in srgb, var(--color-glass-base) 80%, transparent); /* 80% translucent frosted pill background */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Lab Gray Substrate**: `#F6F6F6` — grounded in `--color-bg` / `--color-surface-page` (`:root`)
- **Product Media Well Surface**: `#D9D9D9` — grounded in `--color-media` (`:root`)
- **Pure White Glass Base**: `#ffffff` — grounded in `--color-white` / `--color-glass-base` (`:root`)
- **Primary Dial Black Ink**: `#000000` — grounded in `--color-ink` (`:root`)
- **Secondary Ink (70% Srgb Mix)**: `color-mix(in srgb, var(--color-ink) 70%, transparent)` — grounded in `--color-ink-70` (`:root`)
- **Muted Spec Ink (50% Srgb Mix)**: `color-mix(in srgb, var(--color-ink) 50%, transparent)` — grounded in `--color-ink-50` (`:root`)
- **Hairline Grid Rule (15% Srgb Mix)**: `color-mix(in srgb, var(--color-ink) 15%, transparent)` — grounded in `--color-hairline` (`:root`)
- **Component Border (20% Srgb Mix)**: `color-mix(in srgb, var(--color-ink) 20%, transparent)` — grounded in `--color-border` (`:root`)
- **Subtle Card Fill (5% Srgb Mix)**: `color-mix(in srgb, var(--color-ink) 5%, transparent)` — grounded in `--color-surface` (`:root`)
- **Super-LumiNova Volt-Lime Accent**: `#AFFF00` — grounded in `--color-accent` (`:root`)

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×4841px` full-page capture (`1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×6103px` full-page capture (`390px` standard mobile width).
- **Container Max-Width**: Full-width industrial grid with `@media (min-width:768px)` and `@media (max-width:1099px)` responsive breakpoints
- **Padding & Gutters**: Fluid horizontal padding with `1px` `--color-hairline` cell borders
- **Desktop Grid**: 4-column tool-watch reference grid and 2-column campaign split (`New Langhe Collection` / `The ICON collection`)
- **Mobile Adaptation**: Collapses below `@media (max-width:767px)` into `<nav class="header__mobile">` and 2-up/1-up product cards
- **Media Queries**: `@media (max-width:767px)`, `@media (min-width:768px)`, `@media (max-width:1099px)`, `@media (prefers-color-scheme:dark)`
- **Corner Radii**: Pill radius (`999px`) on `.nav-pill` and `.drawer__pill`; crisp `0px`–`4px` corners on watch specification plates

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `"Helvetica Neue", Helvetica, Arial, sans-serif` (`--font-sans`)
- **Body Font Stack**: `"Helvetica Neue", Helvetica, Arial, sans-serif` (`.t-body`)
- **Monospace / Technical Font Stack**: `"JetBrains Mono", "IBM Plex Mono", monospace` (`--font-mono`)
- **H1 Display Rule**: `clamp(2.25rem, 5vw, 4.25rem)`, `font-family: "Helvetica Neue", sans-serif`, `font-weight: 500`, `line-height: 1.02`, `letter-spacing: -0.03em` ("New Langhe Collection")
- **H2 Section Rule**: `clamp(1.5rem, 3vw, 2.5rem)`, `font-family: "Helvetica Neue", sans-serif`, `font-weight: 500` ("The ICON collection")
- **Body Copy Rule**: `0.9375rem (15px)`, `font-family: "Helvetica Neue", sans-serif`, `line-height: 1.55`, `color: var(--color-ink-70)`
- **Metadata & Index Rule**: `0.75rem (12px)`, `font-family: "JetBrains Mono", "IBM Plex Mono", monospace`, `letter-spacing: 0.06em`, `text-transform: uppercase` (`Modello Uno`, `300m / 1000ft`, `Waterproof checked`)

### 6. Component Hierarchy & Real DOM Landmarks
Scaffold the interface with these exact structural regions and class selectors from `www-unimaticwatches-com`:
1. **Floating Glass Pill Header (`<nav class="header__nav nav-pill">` and `<nav class="header__actions nav-pill nav-pill--sm">`)**:
   - Architecture & Selectors: Dual floating pill bars rendered in `--color-glass-80` (`color-mix(in srgb, var(--color-glass-base) 80%, transparent)`) with `backdrop-filter: blur(12px)` and `<nav class="header__mobile">` fallback below `767px`.
   - Layout & State Contract: Sticky/fixed top header navigation adapting across `@media (max-width:767px)`, `@media (min-width:768px)`, `@media (max-width:1099px)`, `@media (prefers-color-scheme:dark)` with `cubic-bezier(.2,.9,.3,1)` (snappy mechanical dial click), `cubic-bezier(1, 0, 0, 1)`, and `220ms ease` (`--transition`) menu transitions.
2. **New Langhe Collection Hero (`<main id="MainContent" class="main">`)**:
   - Architecture & Selectors: Full-width editorial campaign on `--color-bg: #F6F6F6` featuring `H1: New Langhe Collection` and `H3: Some landscapes are defined less by what can be seen than by what can be felt.`
   - Layout & State Contract: Full-viewport hero stage (`1440px` desktop / `390px` mobile) pairing `#F6F6F6` substrate with `#000000` display typography (`H1`).
3. **The ICON Collection Matrix (`H2: The ICON collection`)**:
   - Architecture & Selectors: Modular 4-column horological catalog where each watch rests on a `--color-media: #D9D9D9` studio well bounded by `--color-hairline` (`15%` srgb mix) borders and `JetBrains Mono` reference numbers.
   - Layout & State Contract: Primary showcase grid executing 4-column tool-watch reference grid and 2-column campaign split (`New Langhe Collection` / `The ICON collection`) on desktop and Collapses below `@media (max-width:767px)` into `<nav class="header__mobile">` and 2-up/1-up product cards on mobile.
4. **Technical Quality Verification (`H3: Waterproof checked`)**:
   - Architecture & Selectors: Industrial testing callouts highlighting 300m water resistance, Italian assembly, `.slider__ctrl` controls, and `--color-accent: #AFFF00` status pills (`.drawer__pill`).
   - Layout & State Contract: Interactive specification & narrative module framed by Pill radius (`999px`) on `.nav-pill` and `.drawer__pill`; crisp `0px`–`4px` corners on watch specification plates and `#AFFF00` highlights.
5. **Milanese Lab Footer (`<nav class="footer-column__links t-body">` and `.footer-utilities__legal`)**:
   - Architecture & Selectors: Clean multi-column Swiss-Italian directory on `--color-surface` (`5%` ink mix).
   - Layout & State Contract: Footer directory and utility bar anchored to Full-width industrial grid with `@media (min-width:768px)` and `@media (max-width:1099px)` responsive breakpoints with Fluid horizontal padding with `1px` `--color-hairline` cell borders lateral gutters.

### 7. Motion & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.2,.9,.3,1)` (snappy mechanical dial click), `cubic-bezier(1, 0, 0, 1)`, and `220ms ease` (`--transition`)
- **Per-Selector Transition Rules**:
- `:root` base transition -> `220ms ease` (`--transition`)
- `.slider__ctrl` -> `transition: background-color var(--transition), color var(--transition)`
- `.drawer__pill` -> `transition: color var(--transition)` (volt-lime `#AFFF00` active badge state)
- `Gallery & Drawer slides` -> `cubic-bezier(.2,.9,.3,1)` and `cubic-bezier(.3, 0, 0, 1)`

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
