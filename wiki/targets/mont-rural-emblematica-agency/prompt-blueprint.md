---
title: "UI Prompt Blueprint: mont-rural-emblematica-agency"
date: 2026-11-15
target: "[[overview|mont-rural-emblematica-agency]]"
status: analyzed
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#443e2b` canvas, `#ffffff` ink, `#8f8637` accent)"
---

# UI Design System & Master Generation Blueprint: mont-rural-emblematica-agency

> **MontRural — Private Masia Among the Vineyards of Penedès** (https://mont-rural.emblematica.agency) — Rent a masia for a peaceful and cozy getaway just an hour's drive from Barcelona. Perfect for nature retreats, family gatherings, and int...

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/mont-rural-emblematica-agency/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **MontRural — Private Masia Among the Vineyards of Penedès** (`https://mont-rural.emblematica.agency`). Rent a masia for a peaceful and cozy getaway just an hour's drive from Barcelona. Perfect for nature retreats, family gatherings, and int...
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#443e2b` canvas, `#ffffff` ink, `#8f8637` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#443e2b` (`var(--uc-typo-color-Bi2HZBV1z)` in `:root`) paired with `#ffffff` primary typography and `#8f8637` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Playfair` for display copy (`MontRural — Private Masia Among the `) with `Arial` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `959px` container bounds (`gap: 10px`, padding `22px`) with `cubic-bezier(.19,1,.22,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/mont-rural-emblematica-agency/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `959px` extracted from `mont-rural-emblematica-agency` stylesheet.
- **Canvas Lateral Padding & Spacing**: `22px` lateral canvas padding with `10px` grid gap.
- **Border Radius Scale**: `4px`, `6px`, `100px`, `1000px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 959px`, `gap: 10px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `22px` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen and (min-width:980px)`, `@media screen and (max-width:959px)`, `@media screen and (max-width:479px)`, `@media screen and (max-width:1024px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#443e2b` | `var(--uc-typo-color-Bi2HZBV1z)` in `:root` |
| **Primary Typography Ink** | `#f8e8c5` | `var(--uc-typo-color-BrelB1n4Inb)` in `:root` |
| **Elevated Surface / Card Substrate** | `#cfa65a` | `var(--uc-typo-color-sHMDDLSH)` in `:root` |
| **Interactive Accent / Highlight** | `#8f8637` | `var(--uc-color-color-nUIBOP3G)` in `:root` |
| **Secondary / Muted Copy** | `#37482f` | `var(--uc-color-color-XmYhOpFwF)` in `:root` |
| **Structural Hairline Border** | `#ffffff` | `var(--uc-button-color-IF7y4On)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--t-headline-font` | `'Playfair',Arial,sans-serif` | Typography / Scale Token |
| `--t-text-font` | `'Arial',Arial,sans-serif` | Typography Ink Token |
| `--uc-typo-fontsize-Bi2HZBV1z` | `82px` | Typography / Scale Token |
| `--uc-typo-fontweight-Bi2HZBV1z` | `400` | Typography / Scale Token |
| `--uc-typo-letterspacing-Bi2HZBV1z` | `-6.5px` | Layout / Spatial Grid Token |
| `--uc-typo-fontfamily-Bi2HZBV1z` | `var(--t-headline-font,Arial)` | Typography / Scale Token |
| `--uc-typo-lineheight-Bi2HZBV1z` | `.9` | Layout / Spatial Grid Token |
| `--uc-typo-color-Bi2HZBV1z` | `#443e2b` | Brand / Palette Token |
| `--uc-typo-fontsize-BrelB1n4Inb` | `98px` | Typography / Scale Token |
| `--uc-typo-fontweight-BrelB1n4Inb` | `400` | Typography / Scale Token |
| `--uc-typo-letterspacing-BrelB1n4Inb` | `-6.5px` | Layout / Spatial Grid Token |
| `--uc-typo-fontfamily-BrelB1n4Inb` | `var(--t-headline-font,Arial)` | Typography / Scale Token |
| `--uc-typo-lineheight-BrelB1n4Inb` | `.9` | Layout / Spatial Grid Token |
| `--uc-typo-color-BrelB1n4Inb` | `#f8e8c5` | Brand / Palette Token |
| `--uc-typo-fontsize-QLat9wWmu2vZ` | `82px` | Typography / Scale Token |
| `--uc-typo-fontweight-QLat9wWmu2vZ` | `400` | Typography / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Playfair`.
- **Primary Body Stack**: `Arial`.
- **Technical / Metadata Stack**: not declared in static CSS (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `13px`, `16px`, `18px`, `14px`, `22px`).
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `13px`, `16px`, `18px`, `14px`, `22px`).
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `13px`, `16px`, `18px`, `14px`, `22px`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `13px`, `16px`, `18px`, `14px`, `22px`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.19,1,.22,1)`, `cubic-bezier(.22,.65,.2,1)`, `cubic-bezier(.22,1,.36,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.t_datepicker__day-cell`**: `transition: 0.2s` extracted from `mont-rural-emblematica-agency` stylesheet.
- **Selector `media screen and (min-width:980px)`**: `transition: 1s` extracted from `mont-rural-emblematica-agency` stylesheet.
- **Selector `.t-title.t-animate`**: `transition: 1.2s` extracted from `mont-rural-emblematica-agency` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.19,1,.22,1)`)**: Governs interactive state transitions across `<nav.t450__menu>` and `<div.t-records>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — MontRural — Private Masia Among the Vineya │
│ ====================================================================== │
│ [ <nav.t450__menu>         | About · location · What's Inside · SER ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <div.t-records>                                      |   │
│ | H1: MontRural — Private Masia Among the Vineyards of             |   │
│ | Substrate: #443e2b    | Ink: #ffffff    | Accent: #8f8637        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<div.t-records>           ) max-w: 959px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Featured Work & Interactive  |  | Technical Architecture & Nar | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 10px  ) | │
│ | [<nav.t450__menu>] -> [<div.t-records>] -> [<div.t-records>] |       │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.t-records_visi) | https://mont-rural.emblematica.age │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.t450__menu> — `mont-rural-emblematica-agency`)**:
   - Landmark `<nav class="t450__menu">` hosting `MontRural — Private Masia Among the ` navigation (`About · location · What's Inside · SERVICES · Contacts`), DOM attributes (`data-hook="blocks-collection-con..."`, `data-tilda-project-id="25144176"`, `data-tilda-page-id="139030856"`, `data-tilda-page-alias="en"`), and stylesheet rule `.t_datepicker__selected-day::after { display: none !important; content: none !important; }`.
2. **Hero Stage & Focal Lead (<div.t-records> — `MontRural — Private Masia Among th`)**:
   - Landmark `<div class="t-records t-records_animated">` presenting display lead `MontRural — Private Masia Among the Vineyards of` and copy excerpt *"CHECK AVAILABILITY"* over `#443e2b` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<div.t-records> — `Featured Work & Interactive Showca`)**:
   - Landmark `<div class="t-records t-records_animated">` rendering section `Featured Work & Interactive Showcase` with copy *"R e n t a m a s i a f o r a p e a c e f u l a n d c o z y g e t a"*, asset references (`mont-rural.emblematica.agency`, `ws.tildacdn.com`, `static.tildacdn.com`, `Frame_1948756319.png`), and grid rule `.t_datepicker__header { background: transparent; border-bottom: 1px solid rgba(255,255,255,0.2); }`.
4. **Interactive Detail & Feature Matrix (<div.t-records> — `Technical Architecture & Narrative`)**:
   - Landmark `<div class="t-records t-records_animated">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"a n h o u r ' s d r i v e f r o m B a r c e l o n a . P e r f e c"*) with `#cfa65a` surface cards, `#8f8637` accents, and `.t_datepicker__label span { color: 8F8637; font-weight: 500; }`.
5. **Colophon & Global Directory Footer (<footer.t-records_visible> — `https://mont-rural.emblematica.agency`)**:
   - Landmark `<footer class="t-records_visible">` anchoring `MontRural — Private Masia Among ` footer links (`About · location · What's Inside · SERVICES · Contacts`), copy *"B a r c e l o n a ."*, and `#ffffff` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: mont-rural-emblematica-agency (MontRural — Private Masia Among the Vineyards of Penedès)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `mont-rural-emblematica-agency` (**MontRural — Private Masia Among the Vineyards of Penedès** — `https://mont-rural.emblematica.agency`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#443e2b` canvas, `#ffffff` ink, `#8f8637` accent).
- **Identity & Domain Context**: Rent a masia for a peaceful and cozy getaway just an hour's drive from Barcelona. Perfect for nature retreats, family gatherings, and int...
- **Primary Substrate**: `#443e2b` (`var(--uc-typo-color-Bi2HZBV1z)` in `:root`), **Primary Ink**: `#ffffff`, **Accent / Highlight**: `#8f8637`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#443e2b` (`var(--uc-typo-color-Bi2HZBV1z)` in `:root`) paired with `#ffffff` primary typography and `#8f8637` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Playfair` for display copy (`MontRural — Private Masia Among the `) with `Arial` and not declared in static CSS (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `959px` container bounds (`gap: 10px`, padding `22px`) with `cubic-bezier(.19,1,.22,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `mont-rural-emblematica-agency` in your global stylesheet:

:root {
  /* MontRural — Private Masia Among the Vineyards of Penedès (mont-rural-emblematica-agency) — Ground-Truth Extracted CSS Variables */
  --t-headline-font: 'Playfair',Arial,sans-serif; /* Typography / Scale Token (mont-rural-emblematica-agency) */
  --t-text-font: 'Arial',Arial,sans-serif; /* Typography Ink Token (mont-rural-emblematica-agency) */
  --uc-typo-fontsize-Bi2HZBV1z: 82px; /* Typography / Scale Token (mont-rural-emblematica-agency) */
  --uc-typo-fontweight-Bi2HZBV1z: 400; /* Typography / Scale Token (mont-rural-emblematica-agency) */
  --uc-typo-letterspacing-Bi2HZBV1z: -6.5px; /* Layout / Spatial Grid Token (mont-rural-emblematica-agency) */
  --uc-typo-fontfamily-Bi2HZBV1z: var(--t-headline-font,Arial); /* Typography / Scale Token (mont-rural-emblematica-agency) */
  --uc-typo-lineheight-Bi2HZBV1z: .9; /* Layout / Spatial Grid Token (mont-rural-emblematica-agency) */
  --uc-typo-color-Bi2HZBV1z: #443e2b; /* Brand / Palette Token (mont-rural-emblematica-agency) */
  --uc-typo-fontsize-BrelB1n4Inb: 98px; /* Typography / Scale Token (mont-rural-emblematica-agency) */
  --uc-typo-fontweight-BrelB1n4Inb: 400; /* Typography / Scale Token (mont-rural-emblematica-agency) */
  --uc-typo-letterspacing-BrelB1n4Inb: -6.5px; /* Layout / Spatial Grid Token (mont-rural-emblematica-agency) */
  --uc-typo-fontfamily-BrelB1n4Inb: var(--t-headline-font,Arial); /* Typography / Scale Token (mont-rural-emblematica-agency) */
  --uc-typo-lineheight-BrelB1n4Inb: .9; /* Layout / Spatial Grid Token (mont-rural-emblematica-agency) */
  --uc-typo-color-BrelB1n4Inb: #f8e8c5; /* Brand / Palette Token (mont-rural-emblematica-agency) */
  --uc-typo-fontsize-QLat9wWmu2vZ: 82px; /* Typography / Scale Token (mont-rural-emblematica-agency) */
  --uc-typo-fontweight-QLat9wWmu2vZ: 400; /* Typography / Scale Token (mont-rural-emblematica-agency) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#443e2b` — grounded in `var(--uc-typo-color-Bi2HZBV1z)` in `:root`
- **Primary Typography Ink**: `#f8e8c5` — grounded in `var(--uc-typo-color-BrelB1n4Inb)` in `:root`
- **Elevated Surface / Card Substrate**: `#cfa65a` — grounded in `var(--uc-typo-color-sHMDDLSH)` in `:root`
- **Interactive Accent / Highlight**: `#8f8637` — grounded in `var(--uc-color-color-nUIBOP3G)` in `:root`
- **Secondary / Muted Copy**: `#37482f` — grounded in `var(--uc-color-color-XmYhOpFwF)` in `:root`
- **Structural Hairline Border**: `#ffffff` — grounded in `var(--uc-button-color-IF7y4On)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `959px` extracted from `mont-rural-emblematica-agency` stylesheet
- **Padding & Gutters**: `22px` lateral canvas padding with `10px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 959px`, `gap: 10px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `22px` horizontal padding
- **Media Queries**: `@media screen and (min-width:980px)`, `@media screen and (max-width:959px)`, `@media screen and (max-width:479px)`, `@media screen and (max-width:1024px)`
- **Corner Radii**: `4px`, `6px`, `100px`, `1000px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Playfair`
- **Body Font Stack**: `Arial`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `13px`, `16px`, `18px`, `14px`, `22px`)
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `13px`, `16px`, `18px`, `14px`, `22px`)
- **Body Copy Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `13px`, `16px`, `18px`, `14px`, `22px`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `13px`, `16px`, `18px`, `14px`, `22px`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `mont-rural-emblematica-agency` (`MontRural — Private Masia Among the Vineyards of Penedès`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.t450__menu> — `mont-rural-emblematica-agency`)**:
   - DOM & Selectors: Landmark `<nav class="t450__menu">` hosting `MontRural — Private Masia Among the ` navigation (`About · location · What's Inside · SERVICES · Contacts`), DOM attributes (`data-hook="blocks-collection-con..."`, `data-tilda-project-id="25144176"`, `data-tilda-page-id="139030856"`, `data-tilda-page-alias="en"`), and stylesheet rule `.t_datepicker__selected-day::after { display: none !important; content: none !important; }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.t450__menu> — `mont-rural-emblematica-agency`)` (`mont-rural-emblematica-agency`) adapts across `@media screen and (min-width:980px)`, `@media screen and (max-width:959px)`, `@media screen and (max-width:479px)`, `@media screen and (max-width:1024px)` with `cubic-bezier(.19,1,.22,1)`, `cubic-bezier(.22,.65,.2,1)`, `cubic-bezier(.22,1,.36,1)` transitions and links `About · location · What's Inside · SERVICES · Contacts`.
2. **Hero Stage & Focal Lead (<div.t-records> — `MontRural — Private Masia Among th`)**:
   - DOM & Selectors: Landmark `<div class="t-records t-records_animated">` presenting display lead `MontRural — Private Masia Among the Vineyards of` and copy excerpt *"CHECK AVAILABILITY"* over `#443e2b` canvas and `#ffffff` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#443e2b` background with `#ffffff` headline `MontRural — Private Masia Among the Vineyards of`.
3. **Primary Showcase & Content Grid (<div.t-records> — `Featured Work & Interactive Showca`)**:
   - DOM & Selectors: Landmark `<div class="t-records t-records_animated">` rendering section `Featured Work & Interactive Showcase` with copy *"R e n t a m a s i a f o r a p e a c e f u l a n d c o z y g e t a"*, asset references (`mont-rural.emblematica.agency`, `ws.tildacdn.com`, `static.tildacdn.com`, `Frame_1948756319.png`), and grid rule `.t_datepicker__header { background: transparent; border-bottom: 1px solid rgba(255,255,255,0.2); }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<div.t-records> — `Featured Work & Interactive Showca`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 959px`, `gap: 10px`) on desktop and Single-column vertical stack at `390px` viewport width with `22px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<div.t-records> — `Technical Architecture & Narrative`)**:
   - DOM & Selectors: Landmark `<div class="t-records t-records_animated">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"a n h o u r ' s d r i v e f r o m B a r c e l o n a . P e r f e c"*) with `#cfa65a` surface cards, `#8f8637` accents, and `.t_datepicker__label span { color: 8F8637; font-weight: 500; }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<div.t-records> — `Technical Architecture & Narrative`)` uses `4px`, `6px`, `100px`, `1000px` radii, `#8f8637` highlights, and assets (mont-rural.emblematica.agency, ws.tildacdn.com, static.tildacdn.com).
5. **Colophon & Global Directory Footer (<footer.t-records_visible> — `https://mont-rural.emblematica.agency`)**:
   - DOM & Selectors: Landmark `<footer class="t-records_visible">` anchoring `MontRural — Private Masia Among ` footer links (`About · location · What's Inside · SERVICES · Contacts`), copy *"B a r c e l o n a ."*, and `#ffffff` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.t-records_visible> — `https://mont-rural.emblematica.agency`)` aligns to `959px` extracted from `mont-rural-emblematica-agency` stylesheet with `22px` lateral canvas padding with `10px` grid gap and attributes (data-hook="blocks-collection-con...", data-tilda-project-id="25144176", data-tilda-page-id="139030856").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"CHECK AVAILABILITY"*
- Copy Excerpt 2: *"R e n t a m a s i a f o r a p e a c e f u l a n d c o z y g e t a w a y j u s t"*
- Copy Excerpt 3: *"a n h o u r ' s d r i v e f r o m B a r c e l o n a . P e r f e c t f o r n a t u r e"*
- Copy Excerpt 4: *"B a r c e l o n a ."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.19,1,.22,1)`, `cubic-bezier(.22,.65,.2,1)`, `cubic-bezier(.22,1,.36,1)`
- **Extracted Stylesheet Rules (`mont-rural-emblematica-agency`)**:
- `.t_datepicker__selected-day::after { display: none !important; content: none !important; }`
- `.t_datepicker__header { background: transparent; border-bottom: 1px solid rgba(255,255,255,0.2); }`
- `.t_datepicker__label span { color: 8F8637; font-weight: 500; }`
- `.t_datepicker__arrow { filter: brightness(0) saturate(100%) invert(53%) sepia(20%) saturate(400... }`
- `.t_datepicker__arrow:hover { opacity: 1; }`
- **Per-Selector Transition Rules**:
- **Selector `.t_datepicker__day-cell`**: `transition: 0.2s` extracted from `mont-rural-emblematica-agency` stylesheet.
- **Selector `media screen and (min-width:980px)`**: `transition: 1s` extracted from `mont-rural-emblematica-agency` stylesheet.
- **Selector `.t-title.t-animate`**: `transition: 1.2s` extracted from `mont-rural-emblematica-agency` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.19,1,.22,1)`)**: Governs interactive state transitions across `<nav.t450__menu>` and `<div.t-records>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `mont-rural-emblematica-agency`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
