---
title: "UI Prompt Blueprint: fondation-canadiens-com"
date: 2026-11-15
target: "fondation-canadiens-com"
status: analyzed
capture: dom
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#f4f4f4`)"
---

# UI Design System & Master Generation Blueprint: fondation-canadiens-com

> **Fondation des Canadiens pour l'enfance - Bouger pour grandir** (https://fondation.canadiens.com/) — La Fondation des Canadiens de Montréal encourage l’activité physique et l’adoption de saines habitudes de vie chez les jeunes défavorisés...

![Desktop Viewport Capture](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Fondation des Canadiens pour l'enfance - Bouger pour grandir** (`https://fondation.canadiens.com/`). La Fondation des Canadiens de Montréal encourage l’activité physique et l’adoption de saines habitudes de vie chez les jeunes défavorisés...
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#f4f4f4`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--color-black)` in `:root`) paired with `#fff` primary typography and `#f4f4f4` accents.
  - **Extracted Typographic Hierarchy**: Pairs `bauhausvole` for display copy (`B o u g e r p o u r g r a n d i r`) with `Poppins` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `64rem` container bounds (`gap: var(--spacing-margin)`, padding `1rem`) with `cubic-bezier(.32,0,.67,0)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×10722px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `64rem` extracted from `fondation-canadiens-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `1rem` lateral canvas padding with `var(--spacing-margin)` grid gap.
- **Border Radius Scale**: `var(--radius-md)`, `var(--radius-sm)`, `.25rem`, `var(--radius-lg)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 64rem`, `gap: var(--spacing-margin)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `1rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:64rem)`, `@media not all and (max-width:64rem)`, `@media (min-width:40rem)`, `@media (min-width:48rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#ccc` | `var(--color-gray)` in `:root` |
| **Interactive Accent / Highlight** | `#f4f4f4` | `var(--color-gray-light)` in `:root` |
| **Secondary / Muted Copy** | `#dae7f6` | `var(--color-gray-blue)` in `:root` |
| **Structural Hairline Border** | `#570000` | `var(--color-red-1)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-sans` | `"Poppins",sans-serif` | Typography / Scale Token |
| `--color-red-50` | `oklch(97.1% .013 17.38)` | Brand / Palette Token |
| `--color-red-500` | `oklch(63.7% .237 25.331)` | Brand / Palette Token |
| `--color-red-800` | `oklch(44.4% .177 26.899)` | Brand / Palette Token |
| `--color-amber-500` | `oklch(76.9% .188 70.08)` | Brand / Palette Token |
| `--color-yellow-500` | `oklch(79.5% .184 86.047)` | Brand / Palette Token |
| `--color-green-500` | `oklch(72.3% .219 149.579)` | Brand / Palette Token |
| `--color-blue-500` | `oklch(62.3% .214 259.815)` | Brand / Palette Token |
| `--color-blue-600` | `oklch(54.6% .245 262.881)` | Brand / Palette Token |
| `--color-purple-500` | `oklch(62.7% .265 303.9)` | Brand / Palette Token |
| `--color-gray-50` | `oklch(98.5% .002 247.839)` | Brand / Palette Token |
| `--color-gray-100` | `oklch(96.7% .003 264.542)` | Brand / Palette Token |
| `--color-gray-200` | `oklch(92.8% .006 264.531)` | Brand / Palette Token |
| `--color-gray-300` | `oklch(87.2% .01 258.338)` | Brand / Palette Token |
| `--color-gray-400` | `oklch(70.7% .022 261.325)` | Brand / Palette Token |
| `--color-gray-600` | `oklch(44.6% .03 256.802)` | Brand / Palette Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `bauhausvole`.
- **Primary Body Stack**: `Poppins`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--text-h1: calc(var(--font-size-h1)/var(--rem)*1rem)`, `--text-h1--line-height: .85`, `--text-h1--letter-spacing: -.03em`; rule `h1` (`font-size: var(--text-h1)`, `line-height: var(--tw-leading,var(...`, `letter-spacing: var(--tw-tracking,var...`, `font-weight: var(--font-we...`).
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2/1.5)`, `--text-h2: calc(var(--font-size-h2)/var(--rem)*1rem)`; rule `h2` (`font-size: var(--text-h4)`, `line-height: var(--tw-leading,var(...`, `font-weight: var(--font-we...`).
- **Body Copy**: CSS variables `--text-body: 1rem`, `--text-body--line-height: 1.4`, `--font-size-body: 16`.
- **Metadata & Navigation Labels**: CSS variables `--text-sm: .875rem`, `--text-sm--line-height: calc(1.25/.875)`, `--default-mono-font-family: var(--font-mono)`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.32,0,.67,0)`, `cubic-bezier(.33,1,.68,1)`, `cubic-bezier(.65,0,.35,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: var(--speed-normal)` extracted from `fondation-canadiens-com` stylesheet.
- **Selector `.lenis.lenis-autoToggle`**: `transition: 1ms` extracted from `fondation-canadiens-com` stylesheet.
- **Selector `swiper-pagination .swiper-paginat...`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `fondation-canadiens-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.32,0,.67,0)`)**: Governs interactive state transitions across `<header.absolute>` and `<article.pt-margin>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine, Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Fondation des Canadiens pour l'enfance - B │
│ ====================================================================== │
│ [ <header.absolute>        | Overview · Index · Archive · About · C ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <article.pt-margin>                                  |   │
│ | H1: B o u g e r p o u r g r a n d i r                            |   │
│ | Substrate: #000       | Ink: #fff       | Accent: #f4f4f4        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<article.pt-margin>       ) max-w: 64rem          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Nouvelles et histoires       |  | Comment contribuer           | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: var(--) | │
│ | [<header.absolute>] -> [<article.pt-margin] -> [<article.pt-margin]  │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.px-margin>    ) | https://fondation.canadiens.com/   │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.absolute> — `fondation-canadiens-com`)**:
   - Landmark `<header class="absolute left-0">` hosting `Fondation des Canadiens pour l'enfan` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-sveltekit-preload-data="hover"`, `data-svg-origin="464 490"`, `data-svg-origin="857.5 277.5"`, `data-flip-id="auto-2"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<article.pt-margin> — `B o u g e r p o u r g r a n d i r`)**:
   - Landmark `<article class="pt-margin space-y-gutter">` presenting display lead `B o u g e r p o u r g r a n d i r` and copy excerpt *"Dons aux organismes"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<article.pt-margin> — `Nouvelles et histoires`)**:
   - Landmark `<article class="pt-margin space-y-gutter">` rendering section `Nouvelles et histoires` with copy *"Comment contribuer"*, asset references (`fonts.googleapis.com`, `fonts.gstatic.com`, `css2`, `favicon-96x96.png`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<article.pt-margin> — `Comment contribuer`)**:
   - Landmark `<article class="pt-margin space-y-gutter">` framing `Comment contribuer` and `Depuis plus de 25 ans, la Fondation des Canadien` (*"Depuis plus de 25 ans, la Fondation des Canadiens pour l’enfance "*) with `#ccc` surface cards, `#f4f4f4` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.px-margin> — `https://fondation.canadiens.com/`)**:
   - Landmark `<footer class="px-margin pb-30">` anchoring `Fondation des Canadiens pour l'e` footer links (`Overview · Index · Archive · About · Contact`), copy *"Derrière chaque patinoire et chaque programme, il y a une hi"*, and `#570000` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: fondation-canadiens-com (Fondation des Canadiens pour l'enfance - Bouger pour grandir)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `fondation-canadiens-com` (**Fondation des Canadiens pour l'enfance - Bouger pour grandir** — `https://fondation.canadiens.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#f4f4f4`).
- **Identity & Domain Context**: La Fondation des Canadiens de Montréal encourage l’activité physique et l’adoption de saines habitudes de vie chez les jeunes défavorisés...
- **Primary Substrate**: `#000` (`var(--color-black)` in `:root`), **Primary Ink**: `#fff`, **Accent / Highlight**: `#f4f4f4`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--color-black)` in `:root`) paired with `#fff` primary typography and `#f4f4f4` accents.
  - **Extracted Typographic Hierarchy**: Pairs `bauhausvole` for display copy (`B o u g e r p o u r g r a n d i r`) with `Poppins` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `64rem` container bounds (`gap: var(--spacing-margin)`, padding `1rem`) with `cubic-bezier(.32,0,.67,0)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `fondation-canadiens-com` in your global stylesheet:

:root {
  /* Fondation des Canadiens pour l'enfance - Bouger pour grandir (fondation-canadiens-com) — Ground-Truth Extracted CSS Variables */
  --font-sans: "Poppins",sans-serif; /* Typography / Scale Token (fondation-canadiens-com) */
  --color-red-50: oklch(97.1% .013 17.38); /* Brand / Palette Token (fondation-canadiens-com) */
  --color-red-500: oklch(63.7% .237 25.331); /* Brand / Palette Token (fondation-canadiens-com) */
  --color-red-800: oklch(44.4% .177 26.899); /* Brand / Palette Token (fondation-canadiens-com) */
  --color-amber-500: oklch(76.9% .188 70.08); /* Brand / Palette Token (fondation-canadiens-com) */
  --color-yellow-500: oklch(79.5% .184 86.047); /* Brand / Palette Token (fondation-canadiens-com) */
  --color-green-500: oklch(72.3% .219 149.579); /* Brand / Palette Token (fondation-canadiens-com) */
  --color-blue-500: oklch(62.3% .214 259.815); /* Brand / Palette Token (fondation-canadiens-com) */
  --color-blue-600: oklch(54.6% .245 262.881); /* Brand / Palette Token (fondation-canadiens-com) */
  --color-purple-500: oklch(62.7% .265 303.9); /* Brand / Palette Token (fondation-canadiens-com) */
  --color-gray-50: oklch(98.5% .002 247.839); /* Brand / Palette Token (fondation-canadiens-com) */
  --color-gray-100: oklch(96.7% .003 264.542); /* Brand / Palette Token (fondation-canadiens-com) */
  --color-gray-200: oklch(92.8% .006 264.531); /* Brand / Palette Token (fondation-canadiens-com) */
  --color-gray-300: oklch(87.2% .01 258.338); /* Brand / Palette Token (fondation-canadiens-com) */
  --color-gray-400: oklch(70.7% .022 261.325); /* Brand / Palette Token (fondation-canadiens-com) */
  --color-gray-600: oklch(44.6% .03 256.802); /* Brand / Palette Token (fondation-canadiens-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#000` — grounded in `var(--color-black)` in `:root`
- **Primary Typography Ink**: `#fff` — grounded in `var(--color-white)` in `:root`
- **Elevated Surface / Card Substrate**: `#ccc` — grounded in `var(--color-gray)` in `:root`
- **Interactive Accent / Highlight**: `#f4f4f4` — grounded in `var(--color-gray-light)` in `:root`
- **Secondary / Muted Copy**: `#dae7f6` — grounded in `var(--color-gray-blue)` in `:root`
- **Structural Hairline Border**: `#570000` — grounded in `var(--color-red-1)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×10722px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `64rem` extracted from `fondation-canadiens-com` stylesheet
- **Padding & Gutters**: `1rem` lateral canvas padding with `var(--spacing-margin)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 64rem`, `gap: var(--spacing-margin)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `1rem` horizontal padding
- **Media Queries**: `@media (min-width:64rem)`, `@media not all and (max-width:64rem)`, `@media (min-width:40rem)`, `@media (min-width:48rem)`
- **Corner Radii**: `var(--radius-md)`, `var(--radius-sm)`, `.25rem`, `var(--radius-lg)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `bauhausvole`
- **Body Font Stack**: `Poppins`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: CSS variables `--text-h1: calc(var(--font-size-h1)/var(--rem)*1rem)`, `--text-h1--line-height: .85`, `--text-h1--letter-spacing: -.03em`; rule `h1` (`font-size: var(--text-h1)`, `line-height: var(--tw-leading,var(...`, `letter-spacing: var(--tw-tracking,var...`, `font-weight: var(--font-we...`)
- **H2 Section Rule**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2/1.5)`, `--text-h2: calc(var(--font-size-h2)/var(--rem)*1rem)`; rule `h2` (`font-size: var(--text-h4)`, `line-height: var(--tw-leading,var(...`, `font-weight: var(--font-we...`)
- **Body Copy Rule**: CSS variables `--text-body: 1rem`, `--text-body--line-height: 1.4`, `--font-size-body: 16`
- **Metadata & Index Rule**: CSS variables `--text-sm: .875rem`, `--text-sm--line-height: calc(1.25/.875)`, `--default-mono-font-family: var(--font-mono)`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `fondation-canadiens-com` (`Fondation des Canadiens pour l'enfance - Bouger pour grandir`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.absolute> — `fondation-canadiens-com`)**:
   - DOM & Selectors: Landmark `<header class="absolute left-0">` hosting `Fondation des Canadiens pour l'enfan` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-sveltekit-preload-data="hover"`, `data-svg-origin="464 490"`, `data-svg-origin="857.5 277.5"`, `data-flip-id="auto-2"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.absolute> — `fondation-canadiens-com`)` (`fondation-canadiens-com`) adapts across `@media (min-width:64rem)`, `@media not all and (max-width:64rem)`, `@media (min-width:40rem)`, `@media (min-width:48rem)` with `cubic-bezier(.32,0,.67,0)`, `cubic-bezier(.33,1,.68,1)`, `cubic-bezier(.65,0,.35,1)` transitions and links `Overview · Index · Archive · About · Contact`.
2. **Hero Stage & Focal Lead (<article.pt-margin> — `B o u g e r p o u r g r a n d i r`)**:
   - DOM & Selectors: Landmark `<article class="pt-margin space-y-gutter">` presenting display lead `B o u g e r p o u r g r a n d i r` and copy excerpt *"Dons aux organismes"* over `#000` canvas and `#fff` ink.
   - Responsive Contract: Hero stage (`1440×10722px` desktop / `390×2400px` mobile) sets `#000` background with `#fff` headline `B o u g e r p o u r g r a n d i r`.
3. **Primary Showcase & Content Grid (<article.pt-margin> — `Nouvelles et histoires`)**:
   - DOM & Selectors: Landmark `<article class="pt-margin space-y-gutter">` rendering section `Nouvelles et histoires` with copy *"Comment contribuer"*, asset references (`fonts.googleapis.com`, `fonts.gstatic.com`, `css2`, `favicon-96x96.png`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<article.pt-margin> — `Nouvelles et histoires`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 64rem`, `gap: var(--spacing-margin)`) on desktop and Single-column vertical stack at `390px` viewport width with `1rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<article.pt-margin> — `Comment contribuer`)**:
   - DOM & Selectors: Landmark `<article class="pt-margin space-y-gutter">` framing `Comment contribuer` and `Depuis plus de 25 ans, la Fondation des Canadien` (*"Depuis plus de 25 ans, la Fondation des Canadiens pour l’enfance "*) with `#ccc` surface cards, `#f4f4f4` accents, and `strong { font-weight:bolder }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<article.pt-margin> — `Comment contribuer`)` uses `var(--radius-md)`, `var(--radius-sm)`, `.25rem`, `var(--radius-lg)` radii, `#f4f4f4` highlights, and assets (fonts.googleapis.com, fonts.gstatic.com, css2).
5. **Colophon & Global Directory Footer (<footer.px-margin> — `https://fondation.canadiens.com/`)**:
   - DOM & Selectors: Landmark `<footer class="px-margin pb-30">` anchoring `Fondation des Canadiens pour l'e` footer links (`Overview · Index · Archive · About · Contact`), copy *"Derrière chaque patinoire et chaque programme, il y a une hi"*, and `#570000` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.px-margin> — `https://fondation.canadiens.com/`)` aligns to `64rem` extracted from `fondation-canadiens-com` stylesheet with `1rem` lateral canvas padding with `var(--spacing-margin)` grid gap and attributes (data-sveltekit-preload-data="hover", data-svg-origin="464 490", data-svg-origin="857.5 277.5").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Dons aux organismes"*
- Copy Excerpt 2: *"Comment contribuer"*
- Copy Excerpt 3: *"Depuis plus de 25 ans, la Fondation des Canadiens pour l’enfance aide les jeunes d..."*
- Copy Excerpt 4: *"Derrière chaque patinoire et chaque programme, il y a une histoire d’enfant qui dé..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.32,0,.67,0)`, `cubic-bezier(.33,1,.68,1)`, `cubic-bezier(.65,0,.35,1)`
- **Extracted Stylesheet Rules (`fondation-canadiens-com`)**:
- `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `strong { font-weight:bolder }`
- `small { font-size:80% }`
- `sup { vertical-align:baseline;font-size:75%;line-height:0;position:relative }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: var(--speed-normal)` extracted from `fondation-canadiens-com` stylesheet.
- **Selector `.lenis.lenis-autoToggle`**: `transition: 1ms` extracted from `fondation-canadiens-com` stylesheet.
- **Selector `swiper-pagination .swiper-paginat...`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `fondation-canadiens-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.32,0,.67,0)`)**: Governs interactive state transitions across `<header.absolute>` and `<article.pt-margin>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine, Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `fondation-canadiens-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
