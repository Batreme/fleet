---
title: "UI Prompt Blueprint: www-undplus-com"
date: 2026-11-15
target: "[[overview|www-undplus-com]]"
status: analyzed
archetype: "Light-Substrate Editorial & Modular Grid System (`#ca9df1` canvas, `#ffd650` ink, `#0daa75` accent)"
---

# UI Design System & Master Generation Blueprint: www-undplus-com

> **UNDPLUS — Brand Architecture & Spatial Design Studio** (https://www.undplus.com) — Studio for brand architecture, spatial design and live experiences. We build trade fair booths, brand spaces and installations from Berli...

![Desktop Viewport Capture (1440x10120)](file:///root/projects/fleet/wiki/targets/www-undplus-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **UNDPLUS — Brand Architecture & Spatial Design Studio** (`https://www.undplus.com`). Studio for brand architecture, spatial design and live experiences. We build trade fair booths, brand spaces and installations from Berli...
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#ca9df1` canvas, `#ffd650` ink, `#0daa75` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#ca9df1` (`var(--token-832a9c22-d657-4637-89aa-cbcc712eb257)` in `:root`) paired with `#ffd650` primary typography and `#0daa75` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Poppins Regular` for display copy (`UNDPLUS Studio for brand experiences`) with `Poppins Black` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `809.98px` container bounds (`gap: 10px`, padding `30px`) with `cubic-bezier(0.25,0.1,0.25,1)` easing and Framer Motion Layout Physics.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/www-undplus-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×10120px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `809.98px` extracted from `www-undplus-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `30px` lateral canvas padding with `10px` grid gap.
- **Border Radius Scale**: `8px`, `15px`, `0px`, `999px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 809.98px`, `gap: 10px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `30px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width:809.98px)`, `@media (max-width:1199px) and (min-width:810px)`, `@media (max-width:809px) and (min-width:0)`, `@media (min-width:810px) and (max-width:1199.98px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#ca9df1` | `var(--token-832a9c22-d657-4637-89aa-cbcc712eb257)` in `:root` |
| **Primary Typography Ink** | `#ffd650` | `var(--token-d9ed1eb8-0c54-4136-bf85-5e5373c04bfa)` in `:root` |
| **Elevated Surface / Card Substrate** | `#93d4f2` | `var(--token-fb37ef9f-b04f-4314-9731-cff242a9823b)` in `:root` |
| **Interactive Accent / Highlight** | `#0daa75` | `var(--token-86e11354-2bd9-45a6-a3ed-8f01f856a058)` in `:root` |
| **Secondary / Muted Copy** | `#f3c6b1` | `var(--token-d07c03e8-e9f2-468d-8b3a-4c5f89f3e77a)` in `:root` |
| **Structural Hairline Border** | `#f08fc7` | `var(--token-54b8b414-a4ad-4bad-a655-869fc0cbd561)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--token-832a9c22-d657-4637-89aa-cbcc712eb257` | `#ca9df1` | Color / Atmospheric Token |
| `--token-d9ed1eb8-0c54-4136-bf85-5e5373c04bfa` | `#ffd650` | Color / Atmospheric Token |
| `--token-fb37ef9f-b04f-4314-9731-cff242a9823b` | `#93d4f2` | Color / Atmospheric Token |
| `--token-86e11354-2bd9-45a6-a3ed-8f01f856a058` | `#0daa75` | Color / Atmospheric Token |
| `--token-d07c03e8-e9f2-468d-8b3a-4c5f89f3e77a` | `#f3c6b1` | Color / Atmospheric Token |
| `--token-54b8b414-a4ad-4bad-a655-869fc0cbd561` | `#f08fc7` | Color / Atmospheric Token |
| `--text-decoration-skip-ink` | `var(--framer-text-decoration-skip-ink)` | Typography Ink Token |
| `--text-underline-offset` | `var(--framer-text-decoration-offset)` | Typography Ink Token |
| `--font-family` | `var(--framer-font-family)` | Typography / Scale Token |
| `--font-style` | `var(--framer-font-style)` | Typography / Scale Token |
| `--font-weight` | `var(--framer-font-weight)` | Typography / Scale Token |
| `--text-color` | `var(--framer-text-color)` | Typography Ink Token |
| `--letter-spacing` | `var(--framer-letter-spacing)` | Typography / Scale Token |
| `--font-size` | `var(--framer-font-size)` | Typography / Scale Token |
| `--text-transform` | `var(--framer-text-transform)` | Typography Ink Token |
| `--line-height` | `var(--framer-line-height)` | Typography / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Poppins Regular`.
- **Primary Body Stack**: `Poppins Black`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 108px`, `line-height: 1.1em`, `letter-spacing: 0em`, `font-weight: 700`).
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `var(--font-size)`, `var(--framer-font-size)`, `16px`, `108px`).
- **Body Copy**: rule `p` (`font-size: 13px`, `line-height: 1.6em`, `letter-spacing: 0em`, `font-weight: 400`).
- **Metadata & Navigation Labels**: CSS variables `--letter-spacing: var(--framer-letter-spacing)`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.25,0.1,0.25,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `#__framer-editorbar-label`**: `transition: opacity 0.4s ease-out` extracted from `www-undplus-com` stylesheet.
- **Selector `style]`**: `transition: opacity 0.15s` extracted from `www-undplus-com` stylesheet.
- **Selector `style]`**: `transition: color 0.2s ease` extracted from `www-undplus-com` stylesheet.
- **Standard CSS Easing (`cubic-bezier(0.25,0.1,0.25,1)`)**: Default timing curve (no custom `cubic-bezier()` declared in static CSS).
- **Runtime Interaction Engine**: Integrates Framer Motion Layout Physics with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — UNDPLUS — Brand Architecture & Spatial Des │
│ ====================================================================== │
│ [ <header.framer-dYpKI>    | Brand Architecture · Retail & Hospital ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.framer-ap504g>                              |   │
│ | H1: UNDPLUS Studio for brand experiences in real life...         |   │
│ | Substrate: #ca9df1    | Ink: #ffd650    | Accent: #0daa75        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.framer-AYmJg>    ) max-w: 809.98px       |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | From concept to execution. I |  | 360° FULL SERVICE            | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 10px  ) | │
│ | [<header.framer-dYp] -> [<section.framer-ap] -> [<section.framer-AY] │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.framer-LFW7G> ) | https://www.undplus.com            │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.framer-dYpKI> — `www-undplus-com`)**:
   - Landmark `<header class="framer-dYpKI">` hosting `UNDPLUS — Brand Architecture & Spati` navigation (`Brand Architecture · Retail & Hospitality · Workplace & New Work`), DOM attributes (`data-redirect-timezone="1"`, `data-framer-font-css`, `data-framer-css-ssr-minified`, `data-framer-components="framer-lib-cursors-ho..."`), and stylesheet rule `main { box-sizing:border-box;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.framer-ap504g> — `UNDPLUS Studio for brand experienc`)**:
   - Landmark `<section class="framer-ap504g">` presenting display lead `UNDPLUS Studio for brand experiences in real life...` and copy excerpt *"brand experiences in real life b r a n d e x p e r i e n c e s i "* over `#ca9df1` canvas and `#ffd650` ink.
3. **Primary Showcase & Content Grid (<section.framer-AYmJg> — `From concept to execution. Ideas b`)**:
   - Landmark `<section class="framer-AYmJg">` rendering section `From concept to execution. Ideas become spaces. S...` with copy *"brand experiences in real life"*, asset references (`cXo2Pf7EWgS5at03i8N3qhgZg.svg`, `S6PCFl3VKfoljDTPsWBO3MD8eps.svg`, `gtm.js`, `script`), and grid rule `root { -webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale }`.
4. **Interactive Detail & Feature Matrix (<section.framer-3gfgd> — `360° FULL SERVICE`)**:
   - Landmark `<section class="framer-3gfgd">` framing `360° FULL SERVICE` and `Brand Architecture` (*"b r a n d e x p e r i e n c e s i n r e a l l i f e"*) with `#93d4f2` surface cards, `#0daa75` accents, and `button { font-family:sans-serif;font-size:12px }`.
5. **Colophon & Global Directory Footer (<footer.framer-LFW7G> — `https://www.undplus.com`)**:
   - Landmark `<footer class="framer-LFW7G">` anchoring `UNDPLUS — Brand Architecture & S` footer links (`Brand Architecture · Retail & Hospitality · Workplace & New Work`), copy *"e x p e r i e n c e s"*, and `#f08fc7` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-undplus-com (UNDPLUS — Brand Architecture & Spatial Design Studio)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-undplus-com` (**UNDPLUS — Brand Architecture & Spatial Design Studio** — `https://www.undplus.com`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#ca9df1` canvas, `#ffd650` ink, `#0daa75` accent).
- **Identity & Domain Context**: Studio for brand architecture, spatial design and live experiences. We build trade fair booths, brand spaces and installations from Berli...
- **Primary Substrate**: `#ca9df1` (`var(--token-832a9c22-d657-4637-89aa-cbcc712eb257)` in `:root`), **Primary Ink**: `#ffd650`, **Accent / Highlight**: `#0daa75`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#ca9df1` (`var(--token-832a9c22-d657-4637-89aa-cbcc712eb257)` in `:root`) paired with `#ffd650` primary typography and `#0daa75` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Poppins Regular` for display copy (`UNDPLUS Studio for brand experiences`) with `Poppins Black` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `809.98px` container bounds (`gap: 10px`, padding `30px`) with `cubic-bezier(0.25,0.1,0.25,1)` easing and Framer Motion Layout Physics.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-undplus-com` in your global stylesheet:

:root {
  /* UNDPLUS — Brand Architecture & Spatial Design Studio (www-undplus-com) — Ground-Truth Extracted CSS Variables */
  --token-832a9c22-d657-4637-89aa-cbcc712eb257: #ca9df1; /* Color / Atmospheric Token (www-undplus-com) */
  --token-d9ed1eb8-0c54-4136-bf85-5e5373c04bfa: #ffd650; /* Color / Atmospheric Token (www-undplus-com) */
  --token-fb37ef9f-b04f-4314-9731-cff242a9823b: #93d4f2; /* Color / Atmospheric Token (www-undplus-com) */
  --token-86e11354-2bd9-45a6-a3ed-8f01f856a058: #0daa75; /* Color / Atmospheric Token (www-undplus-com) */
  --token-d07c03e8-e9f2-468d-8b3a-4c5f89f3e77a: #f3c6b1; /* Color / Atmospheric Token (www-undplus-com) */
  --token-54b8b414-a4ad-4bad-a655-869fc0cbd561: #f08fc7; /* Color / Atmospheric Token (www-undplus-com) */
  --text-decoration-skip-ink: var(--framer-text-decoration-skip-ink); /* Typography Ink Token (www-undplus-com) */
  --text-underline-offset: var(--framer-text-decoration-offset); /* Typography Ink Token (www-undplus-com) */
  --font-family: var(--framer-font-family); /* Typography / Scale Token (www-undplus-com) */
  --font-style: var(--framer-font-style); /* Typography / Scale Token (www-undplus-com) */
  --font-weight: var(--framer-font-weight); /* Typography / Scale Token (www-undplus-com) */
  --text-color: var(--framer-text-color); /* Typography Ink Token (www-undplus-com) */
  --letter-spacing: var(--framer-letter-spacing); /* Typography / Scale Token (www-undplus-com) */
  --font-size: var(--framer-font-size); /* Typography / Scale Token (www-undplus-com) */
  --text-transform: var(--framer-text-transform); /* Typography Ink Token (www-undplus-com) */
  --line-height: var(--framer-line-height); /* Typography / Scale Token (www-undplus-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ca9df1` — grounded in `var(--token-832a9c22-d657-4637-89aa-cbcc712eb257)` in `:root`
- **Primary Typography Ink**: `#ffd650` — grounded in `var(--token-d9ed1eb8-0c54-4136-bf85-5e5373c04bfa)` in `:root`
- **Elevated Surface / Card Substrate**: `#93d4f2` — grounded in `var(--token-fb37ef9f-b04f-4314-9731-cff242a9823b)` in `:root`
- **Interactive Accent / Highlight**: `#0daa75` — grounded in `var(--token-86e11354-2bd9-45a6-a3ed-8f01f856a058)` in `:root`
- **Secondary / Muted Copy**: `#f3c6b1` — grounded in `var(--token-d07c03e8-e9f2-468d-8b3a-4c5f89f3e77a)` in `:root`
- **Structural Hairline Border**: `#f08fc7` — grounded in `var(--token-54b8b414-a4ad-4bad-a655-869fc0cbd561)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×10120px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `809.98px` extracted from `www-undplus-com` stylesheet
- **Padding & Gutters**: `30px` lateral canvas padding with `10px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 809.98px`, `gap: 10px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `30px` horizontal padding
- **Media Queries**: `@media (max-width:809.98px)`, `@media (max-width:1199px) and (min-width:810px)`, `@media (max-width:809px) and (min-width:0)`, `@media (min-width:810px) and (max-width:1199.98px)`
- **Corner Radii**: `8px`, `15px`, `0px`, `999px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Poppins Regular`
- **Body Font Stack**: `Poppins Black`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: rule `h1` (`font-size: 108px`, `line-height: 1.1em`, `letter-spacing: 0em`, `font-weight: 700`)
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `var(--font-size)`, `var(--framer-font-size)`, `16px`, `108px`)
- **Body Copy Rule**: rule `p` (`font-size: 13px`, `line-height: 1.6em`, `letter-spacing: 0em`, `font-weight: 400`)
- **Metadata & Index Rule**: CSS variables `--letter-spacing: var(--framer-letter-spacing)`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-undplus-com` (`UNDPLUS — Brand Architecture & Spatial Design Studio`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.framer-dYpKI> — `www-undplus-com`)**:
   - DOM & Selectors: Landmark `<header class="framer-dYpKI">` hosting `UNDPLUS — Brand Architecture & Spati` navigation (`Brand Architecture · Retail & Hospitality · Workplace & New Work`), DOM attributes (`data-redirect-timezone="1"`, `data-framer-font-css`, `data-framer-css-ssr-minified`, `data-framer-components="framer-lib-cursors-ho..."`), and stylesheet rule `main { box-sizing:border-box;margin:0;padding:0 }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.framer-dYpKI> — `www-undplus-com`)` (`www-undplus-com`) adapts across `@media (max-width:809.98px)`, `@media (max-width:1199px) and (min-width:810px)`, `@media (max-width:809px) and (min-width:0)`, `@media (min-width:810px) and (max-width:1199.98px)` with `cubic-bezier(0.25,0.1,0.25,1)` transitions and links `Brand Architecture · Retail & Hospitality · Workplace & New Work`.
2. **Hero Stage & Focal Lead (<section.framer-ap504g> — `UNDPLUS Studio for brand experienc`)**:
   - DOM & Selectors: Landmark `<section class="framer-ap504g">` presenting display lead `UNDPLUS Studio for brand experiences in real life...` and copy excerpt *"brand experiences in real life b r a n d e x p e r i e n c e s i "* over `#ca9df1` canvas and `#ffd650` ink.
   - Responsive Contract: Hero stage (`1440×10120px` desktop / `390×2400px` mobile) sets `#ca9df1` background with `#ffd650` headline `UNDPLUS Studio for brand experiences in real life...`.
3. **Primary Showcase & Content Grid (<section.framer-AYmJg> — `From concept to execution. Ideas b`)**:
   - DOM & Selectors: Landmark `<section class="framer-AYmJg">` rendering section `From concept to execution. Ideas become spaces. S...` with copy *"brand experiences in real life"*, asset references (`cXo2Pf7EWgS5at03i8N3qhgZg.svg`, `S6PCFl3VKfoljDTPsWBO3MD8eps.svg`, `gtm.js`, `script`), and grid rule `root { -webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.framer-AYmJg> — `From concept to execution. Ideas b`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 809.98px`, `gap: 10px`) on desktop and Single-column vertical stack at `390px` viewport width with `30px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.framer-3gfgd> — `360° FULL SERVICE`)**:
   - DOM & Selectors: Landmark `<section class="framer-3gfgd">` framing `360° FULL SERVICE` and `Brand Architecture` (*"b r a n d e x p e r i e n c e s i n r e a l l i f e"*) with `#93d4f2` surface cards, `#0daa75` accents, and `button { font-family:sans-serif;font-size:12px }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.framer-3gfgd> — `360° FULL SERVICE`)` uses `8px`, `15px`, `0px`, `999px` radii, `#0daa75` highlights, and assets (cXo2Pf7EWgS5at03i8N3qhgZg.svg, S6PCFl3VKfoljDTPsWBO3MD8eps.svg, gtm.js).
5. **Colophon & Global Directory Footer (<footer.framer-LFW7G> — `https://www.undplus.com`)**:
   - DOM & Selectors: Landmark `<footer class="framer-LFW7G">` anchoring `UNDPLUS — Brand Architecture & S` footer links (`Brand Architecture · Retail & Hospitality · Workplace & New Work`), copy *"e x p e r i e n c e s"*, and `#f08fc7` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.framer-LFW7G> — `https://www.undplus.com`)` aligns to `809.98px` extracted from `www-undplus-com` stylesheet with `30px` lateral canvas padding with `10px` grid gap and attributes (data-redirect-timezone="1", data-framer-font-css, data-framer-css-ssr-minified).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"brand experiences in real life b r a n d e x p e r i e n c e s i n r e a l l i f e"*
- Copy Excerpt 2: *"brand experiences in real life"*
- Copy Excerpt 3: *"b r a n d e x p e r i e n c e s i n r e a l l i f e"*
- Copy Excerpt 4: *"e x p e r i e n c e s"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.25,0.1,0.25,1)`
- **Extracted Stylesheet Rules (`www-undplus-com`)**:
- `main { box-sizing:border-box;margin:0;padding:0 }`
- `root { -webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale }`
- `button { font-family:sans-serif;font-size:12px }`
- `body { --framer-will-change-override:transform }`
- `h6 span { display:block }`
- **Per-Selector Transition Rules**:
- **Selector `#__framer-editorbar-label`**: `transition: opacity 0.4s ease-out` extracted from `www-undplus-com` stylesheet.
- **Selector `style]`**: `transition: opacity 0.15s` extracted from `www-undplus-com` stylesheet.
- **Selector `style]`**: `transition: color 0.2s ease` extracted from `www-undplus-com` stylesheet.
- **Standard CSS Easing (`cubic-bezier(0.25,0.1,0.25,1)`)**: Default timing curve (no custom `cubic-bezier()` declared in static CSS).
- **Runtime Interaction Engine**: Integrates Framer Motion Layout Physics with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-undplus-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
