---
title: "UI Prompt Blueprint: www-eladiodieste-com"
date: 2026-11-15
target: "[[overview|www-eladiodieste-com]]"
archetype: "Structural Ceramic-Brick Archival Monograph & Expo-Ease Typography (`--background: #eadfd2` + `--foreground: #a55f2d`)"
---

# UI Design System & Master Generation Blueprint: www-eladiodieste-com

> **Eladio Dieste · La Intersección de Ingeniería con Arquitectura (1917–2000)** — An architectural monograph celebrating Uruguayan structural engineer Eladio Dieste (1917–2000), crafted entirely from two earthen pigments: warm mortar sand (`--background: #eadfd2`, `--off-white: #f1ece8`) and kiln-fired terracotta brick (`--foreground: #a55f2d`), choreographed with long-duration exponential character reveals (`--ease-out-expo: cubic-bezier(.19,1,.22,1)`).

![Desktop Viewport Capture (1440x14025)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Eladio Dieste · La Intersección de Ingeniería con Arquitectura (1917–2000)**. An architectural monograph celebrating Uruguayan structural engineer Eladio Dieste (1917–2000), crafted entirely from two earthen pigments: warm mortar sand (`--background: #eadfd2`, `--off-white: #f1ece8`) and kiln-fired terracotta brick (`--foreground: #a55f2d`), choreographed with long-duration exponential character reveals (`--ease-out-expo: cubic-bezier(.19,1,.22,1)`).
- **Visual Archetype**: **Structural Ceramic-Brick Archival Monograph & Expo-Ease Typography (`--background: #eadfd2` + `--foreground: #a55f2d`)**.
- **Anti-AI-Slop Differentiators**:
  1. **Bichromatic Earthen Materiality**: Every text node, divider line, and architectural diagram is rendered in burnt terracotta brick (`--foreground: #a55f2d`) over warm mortar sand (`--background: #eadfd2`) and soft lime (`--off-white: #f1ece8`).
  2. **250lvh Scroll-Pinned Hero Monograph**: Opens with `<section class="text-background invisible relative h-[250lvh]">` that pins and reveals `H1: Eladio Dieste` and `H2: → 1917-2000 Artigas, Uruguay`.
  3. **1.6-Second Exponential Split-Text Reveals**: Character and word masks (`.reveal-chars .char`, `.reveal-words .word`, `.reveal-divider`) animate over `1.4s`–`1.6s` using `--ease-out-expo: cubic-bezier(.19,1,.22,1)` with `--split-mask-pad: .08em`.
  4. **Bilingual Structural Catalog (`section#work`, `section#vida`)**: Chronicles landmark Gaussian vaults (`H2: Obras`, `H2: La intersección de ingeniería con arquitectura`, `H3: Vivienda Berlingieri (Próximamente)`).

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x10165)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Full-Page Dimensions**: Desktop `1440×14025px` (`assets/desktop.png`), Mobile `390×10165px` (`assets/mobile.png`).
- **Master Container Bounds**: Fluid full-viewport layout with `px-global` lateral padding and `--container-xl: 36rem` (576px) reading columns.
- **Canvas Lateral Padding & Spacing**: Global `px-global` horizontal padding with `--spacing: .25rem` (4px) base rhythm (`pt-6`, `pt-45`, `pb-40 md:pb-72`).
- **Border Radius Scale**: `--radius-md: .375rem` (6px) on archival plates; crisp `1px` terracotta rules (`.reveal-divider`).

### Responsive Breakpoint Architecture
- **Desktop Layout**: Asymmetric architectural index grid across `section#work` and `section#vida` with `gap-5` (`1.25rem`).
- **Mobile Layout**: Single-column archival stack below `@media (min-width:48rem)` with touch-adapted scroll sections.
- **Extracted CSS Media Queries**: `@media (min-width:40rem)` (640px), `@media (min-width:48rem)` (768px), `@media (min-width:64rem)` (1024px), `@media (min-width:80rem)` (1280px), `@media (min-width:96rem)` (1536px).

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| Primary Warm Mortar Sand Canvas | `#eadfd2` | `--background` (`:root`) |
| Secondary Lime Off-White Surface | `#f1ece8` | `--off-white` (`:root`) |
| Primary Terracotta Brick Ink & Accent | `#a55f2d` | `--foreground` / `--color-accent` (`:root`) |
| Pure Black Contrast Token | `#000` | `--color-black` (`:root`) |
| Pure White Contrast Token | `#fff` | `--color-white` (`:root`) |
| Elevation Drop Shadow | `0 25px 25px #00000026` | `--drop-shadow-2xl` (`:root`) |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--background` | `#eadfd2` | Primary warm mortar sand canvas substrate |
| `--foreground` | `#a55f2d` | Primary kiln-fired terracotta brick ink & border token |
| `--off-white` | `#f1ece8` | Secondary light archival card surface |
| `--color-accent` | `var(--foreground)` | Accent color mapped directly to terracotta `#a55f2d` |
| `--color-black` | `#000` | Black reference token |
| `--color-white` | `#fff` | White reference token |
| `--ease-out-expo` | `cubic-bezier(.19,1,.22,1)` | Primary 1.4s–1.6s character & divider reveal curve |
| `--ease-magic` | `cubic-bezier(.33,0,0,1)` | Active navigation indicator morph curve |
| `--ease-quart` | `cubic-bezier(.41,.35,.2,1)` | Scroll parallax & image reveal curve |
| `--ease-out` | `cubic-bezier(0,0,.2,1)` | Standard UI ease-out curve |
| `--default-transition-duration` | `.15s` | Base micro-interaction duration |
| `--default-transition-timing-function` | `cubic-bezier(.4,0,.2,1)` | Base timing curve |
| `--split-mask-pad` | `.08em` | Horizontal padding on split-text reveal masks |
| `--split-mask-bleed-y` | `.3em` | Vertical descender bleed allowance on text masks |
| `--container-xl` | `36rem` | 576px scholarly reading measure |
| `--tracking-tight` | `-.025em` | Display headline letter-spacing |
| `--text-5xl` | `3rem` | 48px chapter heading size (`line-height: 1`) |
| `--text-6xl` | `3.75rem` | 60px monument heading size (`line-height: 1`) |
| `--text-7xl` | `4.5rem` | 72px hero display size (`line-height: 1`) |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `var(--font-sans)` (`"font", "font Fallback", Helvetica, Arial, sans-serif`).
- **Primary Body Stack**: `var(--font-sans)` (`--default-font-family`).
- **Technical / Metadata Stack**: `var(--font-mono)` (`--default-mono-font-family`, archival dates `1917-2000`, GPS coordinates).

### Typographic Scale & Rules
- **Hero Display (`H1`)**: `var(--text-7xl)` (`4.5rem` / scaling up on `96rem` viewport), `font-weight: 500` (`--font-weight-medium`), `line-height: 1`, `letter-spacing: var(--tracking-tight)` (`-.025em`), `color: var(--foreground)` ("Eladio Dieste").
- **Section Heading (`H2`)**: `var(--text-5xl)` (`3rem`) to `var(--text-6xl)` (`3.75rem`), `line-height: 1` ("Obras", "→ 1917-2000 Artigas, Uruguay", "La intersección de ingeniería con arquitectura").
- **Body Copy**: `var(--text-lg)` (`1.125rem`), `line-height: calc(1.75/1.125)`, `max-width: var(--container-xl)` (`36rem`), `color: var(--foreground)`.
- **Metadata & Navigation Labels**: `var(--text-xs)` (`.75rem`), `font-family: var(--font-mono)`, uppercase archival catalog indices.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.19,1,.22,1)` (`--ease-out-expo`), `cubic-bezier(.33,0,0,1)` (`--ease-magic`), and `cubic-bezier(.41,.35,.2,1)` (`--ease-quart`).

### Per-Element Transition & Choreography Rules
- `body` -> `transition: background-color .7s, color .7s` (smooth surface polarity shifts between `#eadfd2` and `#a55f2d`)
- `.reveal-divider` -> `transition: transform 1.4s var(--ease-out-expo)` (horizontal hairline rule drawing)
- `.reveal-chars .char, .reveal-words .word` -> `transition: 1.6s var(--ease-out-expo) transform` (masked typographic entrance)
- `a[aria-current]:before` -> `transition: background-color .3s ease-in-out, transform .3s var(--ease-magic)`

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ <nav class="flex items-center justify-between font-medium">            │
│   [Eladio Dieste]                      [Obras (#work)] [Vida (#vida)]  │
├────────────────────────────────────────────────────────────────────────┤
│ <section class="text-background relative h-[250lvh]"> (Bg: #eadfd2)    │
│   H1: Eladio Dieste  |  H2: → 1917-2000 Artigas, Uruguay (Ink: #a55f2d │
├────────────────────────────────────────────────────────────────────────┤
│ <section class="px-global gap-5 pt-45">                                │
│   H2: La intersección de ingeniería con arquitectura (.reveal-words)   │
├────────────────────────────────────────────────────────────────────────┤
│ <section id="work" class="px-global"> H2: Obras (.reveal-divider 1.4s) │
│   [ Cristo Obrero Church ] [H3: Vivienda Berlingieri (Próximamente)]   │
├────────────────────────────────────────────────────────────────────────┤
│ <section id="vida" class="px-global pt-6 pb-40 md:pb-72"> Biography    │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Archival Top Navigation (`<nav class="flex items-center justify-between font-medium">`)**:
   - Minimalist header bar rendered in `--foreground: #a55f2d` with active dot indicator (`a[aria-current]:before`) animated via `--ease-magic: cubic-bezier(.33,0,0,1)`.
2. **250lvh Scroll-Pinned Hero (`<section class="text-background invisible relative h-[250lvh]">`)**:
   - Monumental opening chapter on `--background: #eadfd2` revealing `H1: Eladio Dieste` and `H2: → 1917-2000 Artigas, Uruguay` using `.reveal-chars .char` (`1.6s var(--ease-out-expo)`).
3. **Engineering Manifesto (`<section class="px-global gap-5 pt-45">`)**:
   - Presents `H2: La intersección de ingeniería con arquitectura` constrained to `--container-xl: 36rem` with `.reveal-divider` (`1.4s var(--ease-out-expo)`) rules.
4. **Structural Works Catalog (`<section id="work" class="px-global">`)**:
   - Chronicles Dieste’s reinforced ceramic vaults under `H2: Obras`, including `H3: Vivienda Berlingieri (Próximamente)` on `--off-white: #f1ece8` plates with `--radius-md: .375rem`.
5. **Biographical Timeline (`<section id="vida" class="px-global pt-6 pb-40 md:pb-72">`)**:
   - Historical archive of blueprints, structural calculations, and Uruguayan heritage with `body` polarity transitions (`transition: background-color .7s, color .7s`).

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-eladiodieste-com (Eladio Dieste · La Intersección de Ingeniería con Arquitectura (1917–2000))

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-eladiodieste-com` (Eladio Dieste · La Intersección de Ingeniería con Arquitectura (1917–2000)).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Structural Ceramic-Brick Archival Monograph & Expo-Ease Typography (`--background: #eadfd2` + `--foreground: #a55f2d`).
- **Primary Substrate**: `#eadfd2` (`--background` (`:root`)), **Primary Ink**: `#a55f2d`, **Accent / Highlight**: `0 25px 25px #00000026`.
- **Site-Specific Differentiators**:
  1. **Bichromatic Earthen Materiality**: Every text node, divider line, and architectural diagram is rendered in burnt terracotta brick (`--foreground: #a55f2d`) over warm mortar sand (`--background: #eadfd2`) and soft lime (`--off-white: #f1ece8`).
  2. **250lvh Scroll-Pinned Hero Monograph**: Opens with `<section class="text-background invisible relative h-[250lvh]">` that pins and reveals `H1: Eladio Dieste` and `H2: → 1917-2000 Artigas, Uruguay`.
  3. **1.6-Second Exponential Split-Text Reveals**: Character and word masks (`.reveal-chars .char`, `.reveal-words .word`, `.reveal-divider`) animate over `1.4s`–`1.6s` using `--ease-out-expo: cubic-bezier(.19,1,.22,1)` with `--split-mask-pad: .08em`.
  4. **Bilingual Structural Catalog (`section#work`, `section#vida`)**: Chronicles landmark Gaussian vaults (`H2: Obras`, `H2: La intersección de ingeniería con arquitectura`, `H3: Vivienda Berlingieri (Próximamente)`).

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-eladiodieste-com` in your global stylesheet:

:root {
  /* Eladio Dieste · La Intersección de Ingeniería con Arquitectura (1917–2000) — Ground-Truth Extracted CSS Variables */
  --background: #eadfd2; /* Primary warm mortar sand canvas substrate */
  --foreground: #a55f2d; /* Primary kiln-fired terracotta brick ink & border token */
  --off-white: #f1ece8; /* Secondary light archival card surface */
  --color-accent: var(--foreground); /* Accent color mapped directly to terracotta `#a55f2d` */
  --color-black: #000; /* Black reference token */
  --color-white: #fff; /* White reference token */
  --ease-out-expo: cubic-bezier(.19,1,.22,1); /* Primary 1.4s–1.6s character & divider reveal curve */
  --ease-magic: cubic-bezier(.33,0,0,1); /* Active navigation indicator morph curve */
  --ease-quart: cubic-bezier(.41,.35,.2,1); /* Scroll parallax & image reveal curve */
  --ease-out: cubic-bezier(0,0,.2,1); /* Standard UI ease-out curve */
  --default-transition-duration: .15s; /* Base micro-interaction duration */
  --default-transition-timing-function: cubic-bezier(.4,0,.2,1); /* Base timing curve */
  --split-mask-pad: .08em; /* Horizontal padding on split-text reveal masks */
  --split-mask-bleed-y: .3em; /* Vertical descender bleed allowance on text masks */
  --container-xl: 36rem; /* 576px scholarly reading measure */
  --tracking-tight: -.025em; /* Display headline letter-spacing */
  --text-5xl: 3rem; /* 48px chapter heading size (`line-height: 1`) */
  --text-6xl: 3.75rem; /* 60px monument heading size (`line-height: 1`) */
  --text-7xl: 4.5rem; /* 72px hero display size (`line-height: 1`) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Warm Mortar Sand Canvas**: `#eadfd2` — grounded in `--background` (`:root`)
- **Secondary Lime Off-White Surface**: `#f1ece8` — grounded in `--off-white` (`:root`)
- **Primary Terracotta Brick Ink & Accent**: `#a55f2d` — grounded in `--foreground` / `--color-accent` (`:root`)
- **Pure Black Contrast Token**: `#000` — grounded in `--color-black` (`:root`)
- **Pure White Contrast Token**: `#fff` — grounded in `--color-white` (`:root`)
- **Elevation Drop Shadow**: `0 25px 25px #00000026` — grounded in `--drop-shadow-2xl` (`:root`)

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×14025px` full-page capture (`1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×10165px` full-page capture (`390px` standard mobile width).
- **Container Max-Width**: Fluid full-viewport layout with `px-global` lateral padding and `--container-xl: 36rem` (576px) reading columns
- **Padding & Gutters**: Global `px-global` horizontal padding with `--spacing: .25rem` (4px) base rhythm (`pt-6`, `pt-45`, `pb-40 md:pb-72`)
- **Desktop Grid**: Asymmetric architectural index grid across `section#work` and `section#vida` with `gap-5` (`1.25rem`)
- **Mobile Adaptation**: Single-column archival stack below `@media (min-width:48rem)` with touch-adapted scroll sections
- **Media Queries**: `@media (min-width:40rem)` (640px), `@media (min-width:48rem)` (768px), `@media (min-width:64rem)` (1024px), `@media (min-width:80rem)` (1280px), `@media (min-width:96rem)` (1536px)
- **Corner Radii**: `--radius-md: .375rem` (6px) on archival plates; crisp `1px` terracotta rules (`.reveal-divider`)

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `var(--font-sans)` (`"font", "font Fallback", Helvetica, Arial, sans-serif`)
- **Body Font Stack**: `var(--font-sans)` (`--default-font-family`)
- **Monospace / Technical Font Stack**: `var(--font-mono)` (`--default-mono-font-family`, archival dates `1917-2000`, GPS coordinates)
- **H1 Display Rule**: `var(--text-7xl)` (`4.5rem` / scaling up on `96rem` viewport), `font-weight: 500` (`--font-weight-medium`), `line-height: 1`, `letter-spacing: var(--tracking-tight)` (`-.025em`), `color: var(--foreground)` ("Eladio Dieste")
- **H2 Section Rule**: `var(--text-5xl)` (`3rem`) to `var(--text-6xl)` (`3.75rem`), `line-height: 1` ("Obras", "→ 1917-2000 Artigas, Uruguay", "La intersección de ingeniería con arquitectura")
- **Body Copy Rule**: `var(--text-lg)` (`1.125rem`), `line-height: calc(1.75/1.125)`, `max-width: var(--container-xl)` (`36rem`), `color: var(--foreground)`
- **Metadata & Index Rule**: `var(--text-xs)` (`.75rem`), `font-family: var(--font-mono)`, uppercase archival catalog indices

### 6. Component Hierarchy & Real DOM Landmarks
Scaffold the interface with these exact structural regions and class selectors from `www-eladiodieste-com`:
1. **Archival Top Navigation (`<nav class="flex items-center justify-between font-medium">`)**:
   - Architecture & Selectors: Minimalist header bar rendered in `--foreground: #a55f2d` with active dot indicator (`a[aria-current]:before`) animated via `--ease-magic: cubic-bezier(.33,0,0,1)`.
   - Layout & State Contract: Sticky/fixed top header navigation adapting across `@media (min-width:40rem)` (640px), `@media (min-width:48rem)` (768px), `@media (min-width:64rem)` (1024px), `@media (min-width:80rem)` (1280px), `@media (min-width:96rem)` (1536px) with `cubic-bezier(.19,1,.22,1)` (`--ease-out-expo`), `cubic-bezier(.33,0,0,1)` (`--ease-magic`), and `cubic-bezier(.41,.35,.2,1)` (`--ease-quart`) menu transitions.
2. **250lvh Scroll-Pinned Hero (`<section class="text-background invisible relative h-[250lvh]">`)**:
   - Architecture & Selectors: Monumental opening chapter on `--background: #eadfd2` revealing `H1: Eladio Dieste` and `H2: → 1917-2000 Artigas, Uruguay` using `.reveal-chars .char` (`1.6s var(--ease-out-expo)`).
   - Layout & State Contract: Full-viewport hero stage (`1440px` desktop / `390px` mobile) pairing `#eadfd2` substrate with `#a55f2d` display typography (`H1`).
3. **Engineering Manifesto (`<section class="px-global gap-5 pt-45">`)**:
   - Architecture & Selectors: Presents `H2: La intersección de ingeniería con arquitectura` constrained to `--container-xl: 36rem` with `.reveal-divider` (`1.4s var(--ease-out-expo)`) rules.
   - Layout & State Contract: Primary showcase grid executing Asymmetric architectural index grid across `section#work` and `section#vida` with `gap-5` (`1.25rem`) on desktop and Single-column archival stack below `@media (min-width:48rem)` with touch-adapted scroll sections on mobile.
4. **Structural Works Catalog (`<section id="work" class="px-global">`)**:
   - Architecture & Selectors: Chronicles Dieste’s reinforced ceramic vaults under `H2: Obras`, including `H3: Vivienda Berlingieri (Próximamente)` on `--off-white: #f1ece8` plates with `--radius-md: .375rem`.
   - Layout & State Contract: Interactive specification & narrative module framed by `--radius-md: .375rem` (6px) on archival plates; crisp `1px` terracotta rules (`.reveal-divider`) and `0 25px 25px #00000026` highlights.
5. **Biographical Timeline (`<section id="vida" class="px-global pt-6 pb-40 md:pb-72">`)**:
   - Architecture & Selectors: Historical archive of blueprints, structural calculations, and Uruguayan heritage with `body` polarity transitions (`transition: background-color .7s, color .7s`).
   - Layout & State Contract: Footer directory and utility bar anchored to Fluid full-viewport layout with `px-global` lateral padding and `--container-xl: 36rem` (576px) reading columns with Global `px-global` horizontal padding with `--spacing: .25rem` (4px) base rhythm (`pt-6`, `pt-45`, `pb-40 md:pb-72`) lateral gutters.

### 7. Motion & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.19,1,.22,1)` (`--ease-out-expo`), `cubic-bezier(.33,0,0,1)` (`--ease-magic`), and `cubic-bezier(.41,.35,.2,1)` (`--ease-quart`)
- **Per-Selector Transition Rules**:
- `body` -> `transition: background-color .7s, color .7s` (smooth surface polarity shifts between `#eadfd2` and `#a55f2d`)
- `.reveal-divider` -> `transition: transform 1.4s var(--ease-out-expo)` (horizontal hairline rule drawing)
- `.reveal-chars .char, .reveal-words .word` -> `transition: 1.6s var(--ease-out-expo) transform` (masked typographic entrance)
- `a[aria-current]:before` -> `transition: background-color .3s ease-in-out, transform .3s var(--ease-magic)`

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
