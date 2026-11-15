---
title: "UI Prompt Blueprint: www-esrbespoke-au"
date: 2026-11-15
target: "[[overview|www-esrbespoke-au]]"
status: analyzed
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#9ca3af`)"
---

# UI Design System & Master Generation Blueprint: www-esrbespoke-au

> **ESR** (https://www.esrbespoke.au/) — Three decades of restoring excellence and reigniting the joy of the drive.

![Desktop Viewport Capture (1440x7770)](file:///root/projects/fleet/wiki/targets/www-esrbespoke-au/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **ESR** (`https://www.esrbespoke.au/`). Three decades of restoring excellence and reigniting the joy of the drive.
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#9ca3af`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fff` (`var(--foreground)` in `:root`) paired with `#000` primary typography and `#9ca3af` accents.
  - **Extracted Typographic Hierarchy**: Pairs `__bodyFont_0f148b` for display copy (`E x c e p t i o n a l i s o u r s t `) with `__bodyFont_Fallback_0f148b` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `14ch` container bounds (`gap: 1rem`, padding `1.125rem`) with `cubic-bezier(.4,0,.6,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/www-esrbespoke-au/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×7770px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `14ch` extracted from `www-esrbespoke-au` stylesheet.
- **Canvas Lateral Padding & Spacing**: `1.125rem` lateral canvas padding with `1rem` grid gap.
- **Border Radius Scale**: `50%`, `2px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 14ch`, `gap: 1rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `1.125rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:1024px)`, `@media (max-width:1023px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--foreground)` in `:root` |
| **Primary Typography Ink** | `#ffffff` | `var(--background)` in `:root` |
| **Elevated Surface / Card Substrate** | `#29d` | `#nprogress .bar { background: #29d }` |
| **Interactive Accent / Highlight** | `#9ca3af` | `textarea::placeholder { color: #9ca3af }` |
| **Secondary / Muted Copy** | `#000` | `#nprogress .bar { background: #000 }` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--foreground-rgb` | `0,0,0` | Typography Ink Token |
| `--background-rgb` | `255,255,255` | Canvas / Surface Token |
| `--border-rgb` | `0,0,0` | Elevation / Border Token |
| `--scrollbarWidth` | `0px` | Layout / Spatial Grid Token |
| `--body-font` | `"__bodyFont_0f148b","__bodyFont_Fallback_0f148b",helvetica,arial,sans-serif` | Typography / Scale Token |
| `--foreground` | `#fff` | Typography Ink Token |
| `--background` | `#ffffff` | Canvas / Surface Token |
| `--border` | `rgba(0,0,0,0.1)` | Elevation / Border Token |
| `--tw-content` | `""` | Design System Custom Token |
| `--tw-border-spacing-x` | `0` | Layout / Spatial Grid Token |
| `--tw-border-spacing-y` | `0` | Layout / Spatial Grid Token |
| `--tw-translate-x` | `0` | Design System Custom Token |
| `--tw-translate-y` | `0` | Design System Custom Token |
| `--tw-rotate` | `0` | Design System Custom Token |
| `--www-esrbespoke-a-bg` | `#fff` | Canvas Substrate (from `var(--foreground)` in `:root`) |
| `--www-esrbespoke-a-ink` | `#000` | Primary Typography Ink (stylesheet-derived) |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `__bodyFont_0f148b`.
- **Primary Body Stack**: `__bodyFont_Fallback_0f148b`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `2.375rem`).
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `2.375rem`).
- **Body Copy**: CSS variables `--body-font: "__bodyFont_0f148b","__bodyFont_Fallback_0f148b",helvetica,arial,sans-serif`.
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `2.375rem`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.16,1,.3,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.transition`**: `transition: cubic-bezier(.4,0,.6,1)` extracted from `www-esrbespoke-au` stylesheet.
- **Selector `ansition-\[margin\2c transform\2c...`**: `transition: cubic-bezier(.4,0,.6,1)` extracted from `www-esrbespoke-au` stylesheet.
- **Selector `.transition-colors`**: `transition: cubic-bezier(.4,0,.6,1)` extracted from `www-esrbespoke-au` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.6,1)`)**: Governs interactive state transitions across `<header.w-auto>` and `<section.w-auto>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — ESR                                        │
│ ====================================================================== │
│ [ <header.w-auto>          | Overview · Index · Archive · About · C ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.w-auto>                                     |   │
│ | H1: E x c e p t i o n a l i s o u r s t a n d a r d              |   │
│ | Substrate: #fff       | Ink: #000       | Accent: #9ca3af        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.w-auto>          ) max-w: 14ch           |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | ESR is recognised as an offi |  | At ESR, we offer a complete  | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 1rem  ) | │
│ | [<header.w-auto>] -> [<section.w-auto>] -> [<section.w-auto>] |      │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.relative>     ) | https://www.esrbespoke.au/         │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.w-auto> — `www-esrbespoke-au`)**:
   - Landmark `<header class="w-auto grid-layout">` hosting `ESR` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-next-font="size-adjust"`, `data-next-font="size-adjust"`, `data-next-font="size-adjust"`, `data-next-font="size-adjust"`), and stylesheet rule `nprogress { pointer-events:none }`.
2. **Hero Stage & Focal Lead (<section.w-auto> — `E x c e p t i o n a l i s o u r s `)**:
   - Landmark `<section class="w-auto grid-layout">` presenting display lead `E x c e p t i o n a l i s o u r s t a n d a r d` and copy excerpt *"E S R B e s p o k e"* over `#fff` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.w-auto> — `ESR is recognised as an official P`)**:
   - Landmark `<section class="w-auto items-end">` rendering section `ESR is recognised as an official Porsche Certifie...` with copy *"A u t o m o t i v e G r o u p since 1989"*, asset references (`apple-touch-icon.png`, `favicon-32x32.png`, `favicon-16x16.png`, `favicon.ico`), and grid rule `nprogress .bar { background:29d;position:fixed;z-index:1031;top:0;left:0;width:100%;heigh... }`.
4. **Interactive Detail & Feature Matrix (<section.w-auto> — `At ESR, we offer a complete end-to`)**:
   - Landmark `<section class="w-auto mb-8">` framing `At ESR, we offer a complete end-to-end service ex...` and `@ e s r b e s p o k e` (*"@ e s r b e s p o k e"*) with `#29d` surface cards, `#9ca3af` accents, and `nprogress .spinner { display:block;position:fixed;z-index:1031;top:15px;right:15px }`.
5. **Colophon & Global Directory Footer (<footer.relative> — `https://www.esrbespoke.au/`)**:
   - Landmark `<footer class="relative clip">` anchoring `ESR` footer links (`Overview · Index · Archive · About · Contact`), copy *"( 0 2 ) 9 7 3 5 1 1 1 1 e n q u i r i e s @ e s r b e s p o "*, and `#000` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-esrbespoke-au (ESR)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-esrbespoke-au` (**ESR** — `https://www.esrbespoke.au/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#9ca3af`).
- **Identity & Domain Context**: Three decades of restoring excellence and reigniting the joy of the drive.
- **Primary Substrate**: `#fff` (`var(--foreground)` in `:root`), **Primary Ink**: `#000`, **Accent / Highlight**: `#9ca3af`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#fff` (`var(--foreground)` in `:root`) paired with `#000` primary typography and `#9ca3af` accents.
  - **Extracted Typographic Hierarchy**: Pairs `__bodyFont_0f148b` for display copy (`E x c e p t i o n a l i s o u r s t `) with `__bodyFont_Fallback_0f148b` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `14ch` container bounds (`gap: 1rem`, padding `1.125rem`) with `cubic-bezier(.4,0,.6,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-esrbespoke-au` in your global stylesheet:

:root {
  /* ESR (www-esrbespoke-au) — Ground-Truth Extracted CSS Variables */
  --foreground-rgb: 0,0,0; /* Typography Ink Token (www-esrbespoke-au) */
  --background-rgb: 255,255,255; /* Canvas / Surface Token (www-esrbespoke-au) */
  --border-rgb: 0,0,0; /* Elevation / Border Token (www-esrbespoke-au) */
  --scrollbarWidth: 0px; /* Layout / Spatial Grid Token (www-esrbespoke-au) */
  --body-font: "__bodyFont_0f148b","__bodyFont_Fallback_0f148b",helvetica,arial,sans-serif; /* Typography / Scale Token (www-esrbespoke-au) */
  --foreground: #fff; /* Typography Ink Token (www-esrbespoke-au) */
  --background: #ffffff; /* Canvas / Surface Token (www-esrbespoke-au) */
  --border: rgba(0,0,0,0.1); /* Elevation / Border Token (www-esrbespoke-au) */
  --tw-content: ""; /* Design System Custom Token (www-esrbespoke-au) */
  --tw-border-spacing-x: 0; /* Layout / Spatial Grid Token (www-esrbespoke-au) */
  --tw-border-spacing-y: 0; /* Layout / Spatial Grid Token (www-esrbespoke-au) */
  --tw-translate-x: 0; /* Design System Custom Token (www-esrbespoke-au) */
  --tw-translate-y: 0; /* Design System Custom Token (www-esrbespoke-au) */
  --tw-rotate: 0; /* Design System Custom Token (www-esrbespoke-au) */
  --www-esrbespoke-a-bg: #fff; /* Canvas Substrate (from `var(--foreground)` in `:root`) (www-esrbespoke-au) */
  --www-esrbespoke-a-ink: #000; /* Primary Typography Ink (stylesheet-derived) (www-esrbespoke-au) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#fff` — grounded in `var(--foreground)` in `:root`
- **Primary Typography Ink**: `#ffffff` — grounded in `var(--background)` in `:root`
- **Elevated Surface / Card Substrate**: `#29d` — grounded in `#nprogress .bar { background: #29d }`
- **Interactive Accent / Highlight**: `#9ca3af` — grounded in `textarea::placeholder { color: #9ca3af }`
- **Secondary / Muted Copy**: `#000` — grounded in `#nprogress .bar { background: #000 }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×7770px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `14ch` extracted from `www-esrbespoke-au` stylesheet
- **Padding & Gutters**: `1.125rem` lateral canvas padding with `1rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 14ch`, `gap: 1rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `1.125rem` horizontal padding
- **Media Queries**: `@media (min-width:1024px)`, `@media (max-width:1023px)`
- **Corner Radii**: `50%`, `2px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `__bodyFont_0f148b`
- **Body Font Stack**: `__bodyFont_Fallback_0f148b`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `2.375rem`)
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `2.375rem`)
- **Body Copy Rule**: CSS variables `--body-font: "__bodyFont_0f148b","__bodyFont_Fallback_0f148b",helvetica,arial,sans-serif`
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `2.375rem`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-esrbespoke-au` (`ESR`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.w-auto> — `www-esrbespoke-au`)**:
   - DOM & Selectors: Landmark `<header class="w-auto grid-layout">` hosting `ESR` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-next-font="size-adjust"`, `data-next-font="size-adjust"`, `data-next-font="size-adjust"`, `data-next-font="size-adjust"`), and stylesheet rule `nprogress { pointer-events:none }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.w-auto> — `www-esrbespoke-au`)` (`www-esrbespoke-au`) adapts across `@media (min-width:1024px)`, `@media (max-width:1023px)` with `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.16,1,.3,1)` transitions and links `Overview · Index · Archive · About · Contact`.
2. **Hero Stage & Focal Lead (<section.w-auto> — `E x c e p t i o n a l i s o u r s `)**:
   - DOM & Selectors: Landmark `<section class="w-auto grid-layout">` presenting display lead `E x c e p t i o n a l i s o u r s t a n d a r d` and copy excerpt *"E S R B e s p o k e"* over `#fff` canvas and `#000` ink.
   - Responsive Contract: Hero stage (`1440×7770px` desktop / `390×2400px` mobile) sets `#fff` background with `#000` headline `E x c e p t i o n a l i s o u r s t a n d a r d`.
3. **Primary Showcase & Content Grid (<section.w-auto> — `ESR is recognised as an official P`)**:
   - DOM & Selectors: Landmark `<section class="w-auto items-end">` rendering section `ESR is recognised as an official Porsche Certifie...` with copy *"A u t o m o t i v e G r o u p since 1989"*, asset references (`apple-touch-icon.png`, `favicon-32x32.png`, `favicon-16x16.png`, `favicon.ico`), and grid rule `nprogress .bar { background:29d;position:fixed;z-index:1031;top:0;left:0;width:100%;heigh... }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.w-auto> — `ESR is recognised as an official P`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 14ch`, `gap: 1rem`) on desktop and Single-column vertical stack at `390px` viewport width with `1.125rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.w-auto> — `At ESR, we offer a complete end-to`)**:
   - DOM & Selectors: Landmark `<section class="w-auto mb-8">` framing `At ESR, we offer a complete end-to-end service ex...` and `@ e s r b e s p o k e` (*"@ e s r b e s p o k e"*) with `#29d` surface cards, `#9ca3af` accents, and `nprogress .spinner { display:block;position:fixed;z-index:1031;top:15px;right:15px }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.w-auto> — `At ESR, we offer a complete end-to`)` uses `50%`, `2px` radii, `#9ca3af` highlights, and assets (apple-touch-icon.png, favicon-32x32.png, favicon-16x16.png).
5. **Colophon & Global Directory Footer (<footer.relative> — `https://www.esrbespoke.au/`)**:
   - DOM & Selectors: Landmark `<footer class="relative clip">` anchoring `ESR` footer links (`Overview · Index · Archive · About · Contact`), copy *"( 0 2 ) 9 7 3 5 1 1 1 1 e n q u i r i e s @ e s r b e s p o "*, and `#000` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.relative> — `https://www.esrbespoke.au/`)` aligns to `14ch` extracted from `www-esrbespoke-au` stylesheet with `1.125rem` lateral canvas padding with `1rem` grid gap and attributes (data-next-font="size-adjust", data-next-font="size-adjust", data-next-font="size-adjust").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"E S R B e s p o k e"*
- Copy Excerpt 2: *"A u t o m o t i v e G r o u p since 1989"*
- Copy Excerpt 3: *"@ e s r b e s p o k e"*
- Copy Excerpt 4: *"( 0 2 ) 9 7 3 5 1 1 1 1 e n q u i r i e s @ e s r b e s p o k e . a u 8 a m – 5 p..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.16,1,.3,1)`
- **Extracted Stylesheet Rules (`www-esrbespoke-au`)**:
- `nprogress { pointer-events:none }`
- `nprogress .bar { background:29d;position:fixed;z-index:1031;top:0;left:0;width:100%;heigh... }`
- `nprogress .spinner { display:block;position:fixed;z-index:1031;top:15px;right:15px }`
- `.nprogress-custom-parent { overflow:hidden;position:relative }`
- `before { box-sizing:border-box;border:0 solid }`
- **Per-Selector Transition Rules**:
- **Selector `.transition`**: `transition: cubic-bezier(.4,0,.6,1)` extracted from `www-esrbespoke-au` stylesheet.
- **Selector `ansition-\[margin\2c transform\2c...`**: `transition: cubic-bezier(.4,0,.6,1)` extracted from `www-esrbespoke-au` stylesheet.
- **Selector `.transition-colors`**: `transition: cubic-bezier(.4,0,.6,1)` extracted from `www-esrbespoke-au` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.6,1)`)**: Governs interactive state transitions across `<header.w-auto>` and `<section.w-auto>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-esrbespoke-au`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
