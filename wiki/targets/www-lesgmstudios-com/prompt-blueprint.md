---
title: "UI Prompt Blueprint: www-lesgmstudios-com"
date: 2026-11-15
target: "www-lesgmstudios-com"
status: analyzed
capture: dom
capture_desktop: dom
capture_mobile: dom
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#0c0c0c` accent)"
---

# UI Design System & Master Generation Blueprint: www-lesgmstudios-com

> **GM Studios — Du contenu qui dépasse les chiffres** (https://www.lesgmstudios.com/) — Agence de contenu & studio d'enregistrement à Montréal. 1 milliard de vues générées pour nos clients.

![Desktop Viewport Capture](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **GM Studios — Du contenu qui dépasse les chiffres** (`https://www.lesgmstudios.com/`). Agence de contenu & studio d'enregistrement à Montréal. 1 milliard de vues générées pour nos clients.
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#0c0c0c` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--color-black)` in `:root`) paired with `#fff` primary typography and `#0c0c0c` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Geist` for display copy (`Du contenu qui dé p asse les chiffre`) with `Geist Fallback` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `40rem` container bounds (`gap: 0px (flush layout)`, padding `6rem`) with `cubic-bezier(.4,0,1,1)` easing and Swiper Touch Carousel Engine.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×7873px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `40rem` extracted from `www-lesgmstudios-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `6rem` lateral canvas padding with `0px (flush layout)` grid gap.
- **Border Radius Scale**: `50%`, `.25rem`, `var(--radius-2xl)`, `var(--radius-3xl)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: 0px (flush layout)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `6rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#070707` | `var(--color-bg)` in `:root` |
| **Interactive Accent / Highlight** | `#0c0c0c` | `var(--color-bg-page)` in `:root` |
| **Secondary / Muted Copy** | `#1d1d1d` | `var(--color-surface)` in `:root` |
| **Structural Hairline Border** | `#fff9` | `var(--color-text-muted)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-geist` | `"Geist", "Geist Fallback"` | Typography / Scale Token |
| `--font-clash` | `"clashDisplay", "clashDisplay Fallback"` | Typography / Scale Token |
| `--font-whisper` | `"Whisper", "Whisper Fallback"` | Typography / Scale Token |
| `--font-dm-sans` | `"DM Sans", "DM Sans Fallback"` | Typography / Scale Token |
| `--font-caveat` | `"Caveat", "Caveat Fallback"` | Typography / Scale Token |
| `--font-sans` | `var(--font-geist), system-ui, sans-serif` | Typography / Scale Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--container-4xl` | `56rem` | Layout / Spatial Grid Token |
| `--text-sm` | `.875rem` | Typography Ink Token |
| `--text-sm--line-height` | `calc(1.25 / .875)` | Typography Ink Token |
| `--font-weight-normal` | `400` | Typography / Scale Token |
| `--font-weight-medium` | `500` | Typography / Scale Token |
| `--font-weight-semibold` | `600` | Typography / Scale Token |
| `--font-weight-bold` | `700` | Typography / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Geist`.
- **Primary Body Stack**: `Geist Fallback`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--font-display: var(--font-clash), system-ui, sans-serif`.
- **Section Heading (`H2`)**: rule `h2` (`font-size: var(--h2-size,clamp(38px, 5.1...`).
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `var(--text-sm)`, `10.5px`).
- **Metadata & Navigation Labels**: CSS variables `--text-sm: .875rem`, `--text-sm--line-height: calc(1.25 / .875)`, `--default-mono-font-family: var(--font-mono)`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.swiper-wrapper`**: `transition: var(--swiper-wrapper-transition-timing-function,initial)` extracted from `www-lesgmstudios-com` stylesheet.
- **Selector `.swiper-free-mode>.swiper-wrapper`**: `transition: ease-out` extracted from `www-lesgmstudios-com` stylesheet.
- **Selector `layer theme`**: `transition: .15s` extracted from `www-lesgmstudios-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,1,1)`)**: Governs interactive state transitions across `<header.fixed>` and `<section.relative>`.
- **Runtime Interaction Engine**: Integrates Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — GM Studios — Du contenu qui dépasse les ch │
│ ====================================================================== │
│ [ <header.fixed>           | Accueil · Agence · Évènements · Cas cl ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.fixed>                                      |   │
│ | H1: Du contenu qui dé p asse les chiffres                        |   │
│ | Substrate: #000       | Ink: #fff       | Accent: #0c0c0c        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.relative>        ) max-w: 40rem          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Clients & Partenaires        |  | Bienvenue                    | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 0px (f) | │
│ | [<header.fixed>] -> [<section.fixed>] -> [<section.relative>] |      │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.relative>     ) | https://www.lesgmstudios.com/      │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.fixed> — `www-lesgmstudios-com`)**:
   - Landmark `<header class="fixed inset-x-0">` hosting `GM Studios — Du contenu qui dépasse ` navigation (`Accueil · Agence · Évènements · Cas clients · Équipe`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-transition-curtain="true"`), and stylesheet rule `root { --swiper-theme-color:007aff }`.
2. **Hero Stage & Focal Lead (<section.fixed> — `Du contenu qui dé p asse les chiff`)**:
   - Landmark `<section class="fixed inset-x-0">` presenting display lead `Du contenu qui dé p asse les chiffres` and copy excerpt *"Selon plus de 450 clients satisfaits"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.relative> — `Clients & Partenaires`)**:
   - Landmark `<section class="relative w-full">` rendering section `Clients & Partenaires` with copy *"Studio de production à Montréal"*, asset references (`ClashDisplay_Bold-s.p.2nvxwaktzfx...`, `ClashDisplay_Medium-s.p.0olkjtjdv...`, `ClashDisplay_Regular-s.p.2qbs-i2c...`, `ClashDisplay_Semibold-s.p.082yiqt...`), and grid rule `host { z-index:1;margin-left:auto;margin-right:auto;display:block;position:rela... }`.
4. **Interactive Detail & Feature Matrix (<section.noise-layer> — `Bienvenue`)**:
   - Landmark `<section class="noise-layer relative">` framing `Bienvenue` and `Nos services` (*"Du contenu qui dé p asse"*) with `#070707` surface cards, `#0c0c0c` accents, and `.swiper { z-index:1;margin-left:auto;margin-right:auto;padding:0;list-style:none;d... }`.
5. **Colophon & Global Directory Footer (<footer.relative> — `https://www.lesgmstudios.com/`)**:
   - Landmark `<footer class="relative flex">` anchoring `GM Studios — Du contenu qui dépa` footer links (`Accueil · Agence · Évènements · Cas clients · Équipe`), copy *"Nous transformons vos idées en contenus percutants qui capti"*, and `#fff9` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-lesgmstudios-com (GM Studios — Du contenu qui dépasse les chiffres)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-lesgmstudios-com` (**GM Studios — Du contenu qui dépasse les chiffres** — `https://www.lesgmstudios.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#0c0c0c` accent).
- **Identity & Domain Context**: Agence de contenu & studio d'enregistrement à Montréal. 1 milliard de vues générées pour nos clients.
- **Primary Substrate**: `#000` (`var(--color-black)` in `:root`), **Primary Ink**: `#fff`, **Accent / Highlight**: `#0c0c0c`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#000` (`var(--color-black)` in `:root`) paired with `#fff` primary typography and `#0c0c0c` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Geist` for display copy (`Du contenu qui dé p asse les chiffre`) with `Geist Fallback` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `40rem` container bounds (`gap: 0px (flush layout)`, padding `6rem`) with `cubic-bezier(.4,0,1,1)` easing and Swiper Touch Carousel Engine.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-lesgmstudios-com` in your global stylesheet:

:root {
  /* GM Studios — Du contenu qui dépasse les chiffres (www-lesgmstudios-com) — Ground-Truth Extracted CSS Variables */
  --font-geist: "Geist", "Geist Fallback"; /* Typography / Scale Token (www-lesgmstudios-com) */
  --font-clash: "clashDisplay", "clashDisplay Fallback"; /* Typography / Scale Token (www-lesgmstudios-com) */
  --font-whisper: "Whisper", "Whisper Fallback"; /* Typography / Scale Token (www-lesgmstudios-com) */
  --font-dm-sans: "DM Sans", "DM Sans Fallback"; /* Typography / Scale Token (www-lesgmstudios-com) */
  --font-caveat: "Caveat", "Caveat Fallback"; /* Typography / Scale Token (www-lesgmstudios-com) */
  --font-sans: var(--font-geist), system-ui, sans-serif; /* Typography / Scale Token (www-lesgmstudios-com) */
  --color-black: #000; /* Canvas / Surface Token (www-lesgmstudios-com) */
  --color-white: #fff; /* Canvas / Surface Token (www-lesgmstudios-com) */
  --spacing: .25rem; /* Layout / Spatial Grid Token (www-lesgmstudios-com) */
  --container-4xl: 56rem; /* Layout / Spatial Grid Token (www-lesgmstudios-com) */
  --text-sm: .875rem; /* Typography Ink Token (www-lesgmstudios-com) */
  --text-sm--line-height: calc(1.25 / .875); /* Typography Ink Token (www-lesgmstudios-com) */
  --font-weight-normal: 400; /* Typography / Scale Token (www-lesgmstudios-com) */
  --font-weight-medium: 500; /* Typography / Scale Token (www-lesgmstudios-com) */
  --font-weight-semibold: 600; /* Typography / Scale Token (www-lesgmstudios-com) */
  --font-weight-bold: 700; /* Typography / Scale Token (www-lesgmstudios-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#000` — grounded in `var(--color-black)` in `:root`
- **Primary Typography Ink**: `#fff` — grounded in `var(--color-white)` in `:root`
- **Elevated Surface / Card Substrate**: `#070707` — grounded in `var(--color-bg)` in `:root`
- **Interactive Accent / Highlight**: `#0c0c0c` — grounded in `var(--color-bg-page)` in `:root`
- **Secondary / Muted Copy**: `#1d1d1d` — grounded in `var(--color-surface)` in `:root`
- **Structural Hairline Border**: `#fff9` — grounded in `var(--color-text-muted)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×7873px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `40rem` extracted from `www-lesgmstudios-com` stylesheet
- **Padding & Gutters**: `6rem` lateral canvas padding with `0px (flush layout)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: 0px (flush layout)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `6rem` horizontal padding
- **Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)`
- **Corner Radii**: `50%`, `.25rem`, `var(--radius-2xl)`, `var(--radius-3xl)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Geist`
- **Body Font Stack**: `Geist Fallback`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: CSS variables `--font-display: var(--font-clash), system-ui, sans-serif`
- **H2 Section Rule**: rule `h2` (`font-size: var(--h2-size,clamp(38px, 5.1...`)
- **Body Copy Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `var(--text-sm)`, `10.5px`)
- **Metadata & Index Rule**: CSS variables `--text-sm: .875rem`, `--text-sm--line-height: calc(1.25 / .875)`, `--default-mono-font-family: var(--font-mono)`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-lesgmstudios-com` (`GM Studios — Du contenu qui dépasse les chiffres`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.fixed> — `www-lesgmstudios-com`)**:
   - DOM & Selectors: Landmark `<header class="fixed inset-x-0">` hosting `GM Studios — Du contenu qui dépasse ` navigation (`Accueil · Agence · Évènements · Cas clients · Équipe`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-transition-curtain="true"`), and stylesheet rule `root { --swiper-theme-color:007aff }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.fixed> — `www-lesgmstudios-com`)` (`www-lesgmstudios-com`) adapts across `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)` with `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)` transitions and links `Accueil · Agence · Évènements · Cas clients · Équipe`.
2. **Hero Stage & Focal Lead (<section.fixed> — `Du contenu qui dé p asse les chiff`)**:
   - DOM & Selectors: Landmark `<section class="fixed inset-x-0">` presenting display lead `Du contenu qui dé p asse les chiffres` and copy excerpt *"Selon plus de 450 clients satisfaits"* over `#000` canvas and `#fff` ink.
   - Responsive Contract: Hero stage (`1440×7873px` desktop / `390×2400px` mobile) sets `#000` background with `#fff` headline `Du contenu qui dé p asse les chiffres`.
3. **Primary Showcase & Content Grid (<section.relative> — `Clients & Partenaires`)**:
   - DOM & Selectors: Landmark `<section class="relative w-full">` rendering section `Clients & Partenaires` with copy *"Studio de production à Montréal"*, asset references (`ClashDisplay_Bold-s.p.2nvxwaktzfx...`, `ClashDisplay_Medium-s.p.0olkjtjdv...`, `ClashDisplay_Regular-s.p.2qbs-i2c...`, `ClashDisplay_Semibold-s.p.082yiqt...`), and grid rule `host { z-index:1;margin-left:auto;margin-right:auto;display:block;position:rela... }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.relative> — `Clients & Partenaires`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 40rem`, `gap: 0px (flush layout)`) on desktop and Single-column vertical stack at `390px` viewport width with `6rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.noise-layer> — `Bienvenue`)**:
   - DOM & Selectors: Landmark `<section class="noise-layer relative">` framing `Bienvenue` and `Nos services` (*"Du contenu qui dé p asse"*) with `#070707` surface cards, `#0c0c0c` accents, and `.swiper { z-index:1;margin-left:auto;margin-right:auto;padding:0;list-style:none;d... }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.noise-layer> — `Bienvenue`)` uses `50%`, `.25rem`, `var(--radius-2xl)`, `var(--radius-3xl)` radii, `#0c0c0c` highlights, and assets (ClashDisplay_Bold-s.p.2nvxwaktzfx..., ClashDisplay_Medium-s.p.0olkjtjdv..., ClashDisplay_Regular-s.p.2qbs-i2c...).
5. **Colophon & Global Directory Footer (<footer.relative> — `https://www.lesgmstudios.com/`)**:
   - DOM & Selectors: Landmark `<footer class="relative flex">` anchoring `GM Studios — Du contenu qui dépa` footer links (`Accueil · Agence · Évènements · Cas clients · Équipe`), copy *"Nous transformons vos idées en contenus percutants qui capti"*, and `#fff9` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.relative> — `https://www.lesgmstudios.com/`)` aligns to `40rem` extracted from `www-lesgmstudios-com` stylesheet with `6rem` lateral canvas padding with `0px (flush layout)` grid gap and attributes (data-precedence="next", data-precedence="next", data-precedence="next").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Selon plus de 450 clients satisfaits"*
- Copy Excerpt 2: *"Studio de production à Montréal"*
- Copy Excerpt 3: *"Du contenu qui dé p asse"*
- Copy Excerpt 4: *"Nous transformons vos idées en contenus percutants qui captivent votre audience et..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,1,1)`, `cubic-bezier(0,0,.2,1)`, `cubic-bezier(.4,0,.2,1)`
- **Extracted Stylesheet Rules (`www-lesgmstudios-com`)**:
- `root { --swiper-theme-color:007aff }`
- `host { z-index:1;margin-left:auto;margin-right:auto;display:block;position:rela... }`
- `.swiper { z-index:1;margin-left:auto;margin-right:auto;padding:0;list-style:none;d... }`
- `.swiper-vertical>.swiper-wrapper { flex-direction:column }`
- `.swiper-wrapper { transform:translate(0,0) }`
- **Per-Selector Transition Rules**:
- **Selector `.swiper-wrapper`**: `transition: var(--swiper-wrapper-transition-timing-function,initial)` extracted from `www-lesgmstudios-com` stylesheet.
- **Selector `.swiper-free-mode>.swiper-wrapper`**: `transition: ease-out` extracted from `www-lesgmstudios-com` stylesheet.
- **Selector `layer theme`**: `transition: .15s` extracted from `www-lesgmstudios-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,1,1)`)**: Governs interactive state transitions across `<header.fixed>` and `<section.relative>`.
- **Runtime Interaction Engine**: Integrates Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-lesgmstudios-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
