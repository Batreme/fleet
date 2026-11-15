---
title: "UI Prompt Blueprint: www-agencejacquesparis-fr"
date: 2026-11-15
target: "www-agencejacquesparis-fr"
status: analyzed
capture: dom
archetype: "Light-Substrate Editorial & Modular Grid System (`#F0F0DC` canvas, `#001847` ink, `#1a3a6b` accent)"
---

# UI Design System & Master Generation Blueprint: www-agencejacquesparis-fr

> **Jacques Paris - Agence à impact positif** (https://www.agencejacquesparis.fr/) — La créativité au service des marques qui veulent changer les choses et prendre soin de ce qui compte.

![Desktop Viewport Capture](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Jacques Paris - Agence à impact positif** (`https://www.agencejacquesparis.fr/`). La créativité au service des marques qui veulent changer les choses et prendre soin de ce qui compte.
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#F0F0DC` canvas, `#001847` ink, `#1a3a6b` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#F0F0DC` (`var(--color-cream)` in `:root`) paired with `#001847` primary typography and `#1a3a6b` accents.
  - **Extracted Typographic Hierarchy**: Pairs `ClashGrotesk` for display copy (`Jacques Paris - Agence à impact posi`) with `SF Mono` and `SF Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `480px` container bounds (`gap: var(--space-lg)`, padding `var(--space-xl)`) with `cubic-bezier(0.25,0.1,0.25,1)` easing.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `480px` extracted from `www-agencejacquesparis-fr` stylesheet.
- **Canvas Lateral Padding & Spacing**: `var(--space-xl)` lateral canvas padding with `var(--space-lg)` grid gap.
- **Border Radius Scale**: `2px`, `50%`, `3px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 480px`, `gap: var(--space-lg)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--space-xl)` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:1024px)`, `@media (prefers-reduced-motion:reduce)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#F0F0DC` | `var(--color-cream)` in `:root` |
| **Primary Typography Ink** | `#F7F7ED` | `var(--color-cream-light)` in `:root` |
| **Elevated Surface / Card Substrate** | `#001847` | `var(--color-cobalt)` in `:root` |
| **Interactive Accent / Highlight** | `#1a3a6b` | `var(--color-cobalt-light)` in `:root` |
| **Secondary / Muted Copy** | `#0E9AA7` | `var(--color-teal)` in `:root` |
| **Structural Hairline Border** | `#E8442A` | `var(--color-coral)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-cream` | `#F0F0DC` | Brand / Palette Token |
| `--color-cream-light` | `#F7F7ED` | Canvas / Surface Token |
| `--color-cobalt` | `#001847` | Brand / Palette Token |
| `--color-cobalt-light` | `#1a3a6b` | Canvas / Surface Token |
| `--color-teal` | `#0E9AA7` | Brand / Palette Token |
| `--color-coral` | `#E8442A` | Brand / Palette Token |
| `--space-zero` | `0` | Layout / Spatial Grid Token |
| `--space-xs` | `4px` | Layout / Spatial Grid Token |
| `--space-sm` | `8px` | Layout / Spatial Grid Token |
| `--space-md` | `16px` | Layout / Spatial Grid Token |
| `--space-lg` | `24px` | Layout / Spatial Grid Token |
| `--space-xl` | `40px` | Layout / Spatial Grid Token |
| `--space-2xl` | `64px` | Layout / Spatial Grid Token |
| `--space-3xl` | `96px` | Layout / Spatial Grid Token |
| `--text-xs` | `11px` | Typography Ink Token |
| `--text-sm` | `14px` | Typography Ink Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `ClashGrotesk`.
- **Primary Body Stack**: `SF Mono`.
- **Technical / Metadata Stack**: `SF Mono`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--text-xs)`, `10px`, `var(--text-sm)`, `20px`, `var(--text-lg)`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: var(--text-md)`, `letter-spacing: .01em`, `font-weight: 600`).
- **Body Copy**: CSS variables `--text-base: 15px`; rule `p` (`font-size: var(--text-base)`, `line-height: 1.7`).
- **Metadata & Navigation Labels**: CSS variables `--text-xs: 11px`, `--text-sm: 14px`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.25,0.1,0.25,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.InvitationForm_textarea__Xo0Zw`**: `transition: border-color .2s ease` extracted from `www-agencejacquesparis-fr` stylesheet.
- **Selector `.InvitationForm_submit__OiJHX`**: `transition: background .2s ease` extracted from `www-agencejacquesparis-fr` stylesheet.
- **Selector `.ZoneCard_overviewCard__A2vTr`**: `transition: opacity .15s,transform .15s` extracted from `www-agencejacquesparis-fr` stylesheet.
- **Standard CSS Easing (`cubic-bezier(0.25,0.1,0.25,1)`)**: Default timing curve (no custom `cubic-bezier()` declared in static CSS).
- **State & Hover Choreography**: Opacity and transform transitions on `<main.ScrollEngine_scrollSpace__HfjIP>` and `<main.ScrollEngine_viewport__JJVIB>` interactive targets.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Jacques Paris - Agence à impact positif    │
│ ====================================================================== │
│ [ <nav.Navbar_navbar__UMdI | Overview · Index · Archive · About · C ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <main.ScrollEngine_scrollSpace__HfjIP>               |   │
│ | H1: Jacques Paris - Agence à impact positif                      |   │
│ | Substrate: #F0F0DC    | Ink: #001847    | Accent: #1a3a6b        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<main.ScrollEngine_viewpor) max-w: 480px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Featured Work & Interactive  |  | Technical Architecture & Nar | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: var(--) | │
│ | [<nav.Navbar_navbar] -> [<main.ScrollEngine] -> [<main.ScrollEngine] │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.PosterCanvas_p) | https://www.agencejacquesparis.fr/ │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.Navbar_navbar__UMdIx> — `www-agencejacquesparis-fr`)**:
   - Landmark `<nav class="Navbar_navbar__UMdIx">` hosting `Jacques Paris - Agence à impact posi` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-nscript="afterInteractive"`), and stylesheet rule `.PosterCanvas_canvas__BduZz { position:absolute;inset:0;overflow:hidden;background-color:var(--color-c... }`.
2. **Hero Stage & Focal Lead (<main.ScrollEngine_scrollSpace__HfjIP> — `Jacques Paris - Agence à impact po`)**:
   - Landmark `<main class="ScrollEngine_scrollSpace__HfjIP">` presenting display lead `Jacques Paris - Agence à impact positif` and copy excerpt *"Politique de protection des données personnelles"* over `#F0F0DC` canvas and `#001847` ink.
3. **Primary Showcase & Content Grid (<main.ScrollEngine_viewport__JJVIB> — `Featured Work & Interactive Showca`)**:
   - Landmark `<main class="ScrollEngine_viewport__JJVIB">` rendering section `Featured Work & Interactive Showcase` with copy *"marine.moreau@jacques.com"*, asset references (`jacques-logo.png`, `ad44a6578bd60804.css`, `074517235421c822.css`, `webpack-8fefb68f87553cee.js`), and grid rule `.ZoneLabel_primary__tb_mD { font-size:var(--text-xs);opacity:.35;letter-spacing:.05em }`.
4. **Interactive Detail & Feature Matrix (<main.PosterCanvas_canvas__BduZz> — `Technical Architecture & Narrative`)**:
   - Landmark `<main class="PosterCanvas_canvas__BduZz">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Assistant Art Director"*) with `#001847` surface cards, `#1a3a6b` accents, and `.ZoneLabel_secondary__sFo9Q { font-weight:300;color:var(--color-cobalt);line-height:1.4 }`.
5. **Colophon & Global Directory Footer (<footer.PosterCanvas_poster__O791U> — `https://www.agencejacquesparis.fr/`)**:
   - Landmark `<footer class="PosterCanvas_poster__O791U">` anchoring `Jacques Paris - Agence à impact ` footer links (`Overview · Index · Archive · About · Contact`), copy *"adrien.jamin@jacques.com"*, and `#E8442A` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-agencejacquesparis-fr (Jacques Paris - Agence à impact positif)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-agencejacquesparis-fr` (**Jacques Paris - Agence à impact positif** — `https://www.agencejacquesparis.fr/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#F0F0DC` canvas, `#001847` ink, `#1a3a6b` accent).
- **Identity & Domain Context**: La créativité au service des marques qui veulent changer les choses et prendre soin de ce qui compte.
- **Primary Substrate**: `#F0F0DC` (`var(--color-cream)` in `:root`), **Primary Ink**: `#001847`, **Accent / Highlight**: `#1a3a6b`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#F0F0DC` (`var(--color-cream)` in `:root`) paired with `#001847` primary typography and `#1a3a6b` accents.
  - **Extracted Typographic Hierarchy**: Pairs `ClashGrotesk` for display copy (`Jacques Paris - Agence à impact posi`) with `SF Mono` and `SF Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `480px` container bounds (`gap: var(--space-lg)`, padding `var(--space-xl)`) with `cubic-bezier(0.25,0.1,0.25,1)` easing.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-agencejacquesparis-fr` in your global stylesheet:

:root {
  /* Jacques Paris - Agence à impact positif (www-agencejacquesparis-fr) — Ground-Truth Extracted CSS Variables */
  --color-cream: #F0F0DC; /* Brand / Palette Token (www-agencejacquesparis-fr) */
  --color-cream-light: #F7F7ED; /* Canvas / Surface Token (www-agencejacquesparis-fr) */
  --color-cobalt: #001847; /* Brand / Palette Token (www-agencejacquesparis-fr) */
  --color-cobalt-light: #1a3a6b; /* Canvas / Surface Token (www-agencejacquesparis-fr) */
  --color-teal: #0E9AA7; /* Brand / Palette Token (www-agencejacquesparis-fr) */
  --color-coral: #E8442A; /* Brand / Palette Token (www-agencejacquesparis-fr) */
  --space-zero: 0; /* Layout / Spatial Grid Token (www-agencejacquesparis-fr) */
  --space-xs: 4px; /* Layout / Spatial Grid Token (www-agencejacquesparis-fr) */
  --space-sm: 8px; /* Layout / Spatial Grid Token (www-agencejacquesparis-fr) */
  --space-md: 16px; /* Layout / Spatial Grid Token (www-agencejacquesparis-fr) */
  --space-lg: 24px; /* Layout / Spatial Grid Token (www-agencejacquesparis-fr) */
  --space-xl: 40px; /* Layout / Spatial Grid Token (www-agencejacquesparis-fr) */
  --space-2xl: 64px; /* Layout / Spatial Grid Token (www-agencejacquesparis-fr) */
  --space-3xl: 96px; /* Layout / Spatial Grid Token (www-agencejacquesparis-fr) */
  --text-xs: 11px; /* Typography Ink Token (www-agencejacquesparis-fr) */
  --text-sm: 14px; /* Typography Ink Token (www-agencejacquesparis-fr) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#F0F0DC` — grounded in `var(--color-cream)` in `:root`
- **Primary Typography Ink**: `#F7F7ED` — grounded in `var(--color-cream-light)` in `:root`
- **Elevated Surface / Card Substrate**: `#001847` — grounded in `var(--color-cobalt)` in `:root`
- **Interactive Accent / Highlight**: `#1a3a6b` — grounded in `var(--color-cobalt-light)` in `:root`
- **Secondary / Muted Copy**: `#0E9AA7` — grounded in `var(--color-teal)` in `:root`
- **Structural Hairline Border**: `#E8442A` — grounded in `var(--color-coral)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `480px` extracted from `www-agencejacquesparis-fr` stylesheet
- **Padding & Gutters**: `var(--space-xl)` lateral canvas padding with `var(--space-lg)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 480px`, `gap: var(--space-lg)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--space-xl)` horizontal padding
- **Media Queries**: `@media (min-width:1024px)`, `@media (prefers-reduced-motion:reduce)`
- **Corner Radii**: `2px`, `50%`, `3px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `ClashGrotesk`
- **Body Font Stack**: `SF Mono`
- **Monospace / Technical Font Stack**: `SF Mono`
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--text-xs)`, `10px`, `var(--text-sm)`, `20px`, `var(--text-lg)`)
- **H2 Section Rule**: rule `h2` (`font-size: var(--text-md)`, `letter-spacing: .01em`, `font-weight: 600`)
- **Body Copy Rule**: CSS variables `--text-base: 15px`; rule `p` (`font-size: var(--text-base)`, `line-height: 1.7`)
- **Metadata & Index Rule**: CSS variables `--text-xs: 11px`, `--text-sm: 14px`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-agencejacquesparis-fr` (`Jacques Paris - Agence à impact positif`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.Navbar_navbar__UMdIx> — `www-agencejacquesparis-fr`)**:
   - DOM & Selectors: Landmark `<nav class="Navbar_navbar__UMdIx">` hosting `Jacques Paris - Agence à impact posi` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-nscript="afterInteractive"`), and stylesheet rule `.PosterCanvas_canvas__BduZz { position:absolute;inset:0;overflow:hidden;background-color:var(--color-c... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.Navbar_navbar__UMdIx> — `www-agencejacquesparis-fr`)` (`www-agencejacquesparis-fr`) adapts across `@media (min-width:1024px)`, `@media (prefers-reduced-motion:reduce)` with `cubic-bezier(0.25,0.1,0.25,1)` transitions and links `Overview · Index · Archive · About · Contact`.
2. **Hero Stage & Focal Lead (<main.ScrollEngine_scrollSpace__HfjIP> — `Jacques Paris - Agence à impact po`)**:
   - DOM & Selectors: Landmark `<main class="ScrollEngine_scrollSpace__HfjIP">` presenting display lead `Jacques Paris - Agence à impact positif` and copy excerpt *"Politique de protection des données personnelles"* over `#F0F0DC` canvas and `#001847` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#F0F0DC` background with `#001847` headline `Jacques Paris - Agence à impact positif`.
3. **Primary Showcase & Content Grid (<main.ScrollEngine_viewport__JJVIB> — `Featured Work & Interactive Showca`)**:
   - DOM & Selectors: Landmark `<main class="ScrollEngine_viewport__JJVIB">` rendering section `Featured Work & Interactive Showcase` with copy *"marine.moreau@jacques.com"*, asset references (`jacques-logo.png`, `ad44a6578bd60804.css`, `074517235421c822.css`, `webpack-8fefb68f87553cee.js`), and grid rule `.ZoneLabel_primary__tb_mD { font-size:var(--text-xs);opacity:.35;letter-spacing:.05em }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<main.ScrollEngine_viewport__JJVIB> — `Featured Work & Interactive Showca`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 480px`, `gap: var(--space-lg)`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--space-xl)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<main.PosterCanvas_canvas__BduZz> — `Technical Architecture & Narrative`)**:
   - DOM & Selectors: Landmark `<main class="PosterCanvas_canvas__BduZz">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Assistant Art Director"*) with `#001847` surface cards, `#1a3a6b` accents, and `.ZoneLabel_secondary__sFo9Q { font-weight:300;color:var(--color-cobalt);line-height:1.4 }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<main.PosterCanvas_canvas__BduZz> — `Technical Architecture & Narrative`)` uses `2px`, `50%`, `3px` radii, `#1a3a6b` highlights, and assets (jacques-logo.png, ad44a6578bd60804.css, 074517235421c822.css).
5. **Colophon & Global Directory Footer (<footer.PosterCanvas_poster__O791U> — `https://www.agencejacquesparis.fr/`)**:
   - DOM & Selectors: Landmark `<footer class="PosterCanvas_poster__O791U">` anchoring `Jacques Paris - Agence à impact ` footer links (`Overview · Index · Archive · About · Contact`), copy *"adrien.jamin@jacques.com"*, and `#E8442A` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.PosterCanvas_poster__O791U> — `https://www.agencejacquesparis.fr/`)` aligns to `480px` extracted from `www-agencejacquesparis-fr` stylesheet with `var(--space-xl)` lateral canvas padding with `var(--space-lg)` grid gap and attributes (data-precedence="next", data-precedence="next", data-nscript="afterInteractive").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Politique de protection des données personnelles"*
- Copy Excerpt 2: *"marine.moreau@jacques.com"*
- Copy Excerpt 3: *"Assistant Art Director"*
- Copy Excerpt 4: *"adrien.jamin@jacques.com"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.25,0.1,0.25,1)`
- **Extracted Stylesheet Rules (`www-agencejacquesparis-fr`)**:
- `.PosterCanvas_canvas__BduZz { position:absolute;inset:0;overflow:hidden;background-color:var(--color-c... }`
- `.ZoneLabel_primary__tb_mD { font-size:var(--text-xs);opacity:.35;letter-spacing:.05em }`
- `.ZoneLabel_secondary__sFo9Q { font-weight:300;color:var(--color-cobalt);line-height:1.4 }`
- `.InvitationForm_overlay__HwWr1 { position:absolute;inset:0;display:flex;align-items:center;justify-conten... }`
- `.InvitationForm_fields__y7A6P { display:flex;flex-direction:column;gap:var(--space-lg) }`
- **Per-Selector Transition Rules**:
- **Selector `.InvitationForm_textarea__Xo0Zw`**: `transition: border-color .2s ease` extracted from `www-agencejacquesparis-fr` stylesheet.
- **Selector `.InvitationForm_submit__OiJHX`**: `transition: background .2s ease` extracted from `www-agencejacquesparis-fr` stylesheet.
- **Selector `.ZoneCard_overviewCard__A2vTr`**: `transition: opacity .15s,transform .15s` extracted from `www-agencejacquesparis-fr` stylesheet.
- **Standard CSS Easing (`cubic-bezier(0.25,0.1,0.25,1)`)**: Default timing curve (no custom `cubic-bezier()` declared in static CSS).
- **State & Hover Choreography**: Opacity and transform transitions on `<main.ScrollEngine_scrollSpace__HfjIP>` and `<main.ScrollEngine_viewport__JJVIB>` interactive targets.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-agencejacquesparis-fr`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
