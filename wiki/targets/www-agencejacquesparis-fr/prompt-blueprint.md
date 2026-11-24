---
title: "UI Prompt Blueprint: www-agencejacquesparis-fr"
date: 2026-11-24
captured_at: 2026-11-24
target: "www-agencejacquesparis-fr"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
capture_mode: behavioral_journey_v2
asset_format: webp
scroll_driver: native
desktop_keyframes: 3
subpages_crawled: 2
http_status: 200
archetype: "Light-Substrate Editorial & Modular Grid System (`#f0f0dc` canvas, `#001847` ink, `#ffffff` accent)"
---

# UI Design System & Master Generation Blueprint: www-agencejacquesparis-fr

> **Jacques Paris - Agence à impact positif** (https://www.agencejacquesparis.fr/) — La créativité au service des marques qui veulent changer les choses et prendre soin de ce qui compte.

![Desktop Journey Filmstrip (1280x2484)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x1744)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Jacques Paris - Agence à impact positif** (`https://www.agencejacquesparis.fr/`). La créativité au service des marques qui veulent changer les choses et prendre soin de ce qui compte.
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#f0f0dc` canvas, `#001847` ink, `#ffffff` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#f0f0dc` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#001847` primary typography and `#ffffff` accents.
  - **Grounded Typographic Hierarchy**: Uses `ClashGrotesk` across display (`Jacques Paris - Agence à impact posi`) and body copy, paired with `SF Mono` for monospace/code.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: var(--space-lg)`, padding `var(--space-xl)`) with `cubic-bezier(0.25,0.1,0.25,1)` easing.

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×2484px` (`assets/desktop-journey.webp`, `3` keyframes up to `y=4500px` / doc `5400px`), Mobile `390×1744px` (`assets/mobile-journey.webp`, `2` keyframes).
- **Master Container Bounds**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport).
- **Canvas Lateral Padding & Spacing**: `var(--space-xl)` lateral canvas padding with `var(--space-lg)` grid gap.
- **Border Radius Scale**: `2px`, `0px 0px 4px 4px`, `50%`, `3px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: var(--space-lg)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `var(--space-xl)` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:1024px)`, `@media (prefers-reduced-motion:reduce)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f0f0dc` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#001847` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `.ZoneCard_caseBtn__MWFpY { background: #ffffff }` |
| **Interactive Accent / Highlight** | `#ffffff` | `.ZoneCard_caseBtn__MWFpY { background: #ffffff }` |
| **Secondary / Muted Copy** | `#ffffff` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#c0c5be` | `.InvitationForm_textarea__Xo0Zw { border-bottom: #c0c5be }` |
| **Variable Token (`--color-cream-light`)** | `#f7f7ed` | `var(--color-cream-light)` in `:root` |
| **Variable Token (`--color-cobalt-light`)** | `#1a3a6b` | `var(--color-cobalt-light)` in `:root` |
| **Variable Token (`--color-teal`)** | `#0e9aa7` | `var(--color-teal)` in `:root` |
| **Variable Token (`--color-coral`)** | `#e8442a` | `var(--color-coral)` in `:root` |

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
- **Primary Body Stack**: `ClashGrotesk`.
- **Technical / Metadata Stack**: `SF Mono`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: observed font-size ladder: `16px`, `22.4px`, `14px`, `13.3333px`, `var(--text-xs)`.
- **Section Heading (`H2`)**: rule `h2` (`font-size: var(--text-md)`, `letter-spacing: .01em`, `font-weight: 600`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--text-base: 15px`; rule `p` (`font-size: var(--text-base)`, `line-height: 1.7`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--text-xs: 11px`, `--text-sm: 14px`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.25,0.1,0.25,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.InvitationForm_textarea__Xo0Zw`**: `transition: border-color .2s ease` extracted from `www-agencejacquesparis-fr` stylesheet.
- **Selector `.InvitationForm_submit__OiJHX`**: `transition: background .2s ease` extracted from `www-agencejacquesparis-fr` stylesheet.
- **Selector `.ZoneCard_overviewCard__A2vTr`**: `transition: opacity .15s,transform .15s` extracted from `www-agencejacquesparis-fr` stylesheet.
- **Standard CSS Easing (`cubic-bezier(0.25,0.1,0.25,1)`)**: Default timing curve (no custom `cubic-bezier()` declared in captured CSS).
- **State & Hover Choreography**: Opacity and transform transitions on `<main.ScrollEngine_scrollSpace__HfjIP>` and `<main.ScrollEngine_viewport__JJVIB>` interactive targets.
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `native` (max document height `5400px`, deepest scrollY reached `4500px` across `3` desktop keyframes).
- **Detected Scroll / Motion Libraries**: Native browser scroll / standard CSS transitions.
- **Nav / Drawer Probe (`Menu`)**: Triggered visual change (pixel diff `53.14`, captured in `assets/state-nav.webp`); revealed links: Mentions légales, Politique de protecti..., CGU, Politique cookies, LinkedIn, Instagram.
- **Hover Physics (`primary_cta` · `L'Agence`)**: Computed transition `0.15s` / `ease` (no static color/transform shift captured at rest).
- **Route Transition Architecture**: First internal navigation (`/politique-de-confidentialite`) measured as `direct` in `503ms`.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Jacques Paris - Agence à impact positif    │
│ ====================================================================== │
│ [ <nav.Navbar_navbar__UM (1440x50px)  | Overview · Index · Archive · ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <main.ScrollEngine_scrollSpace__HfjI (w=1440px)        | │
│ | H1: Jacques Paris - Agence à impact positif                        | │
│ | Substrate: #f0f0dc | Ink: #001847 | Accent: #ffffff                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<main.ScrollEngine_viewpor) max-w: 1440px           | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Featured Work & Interactive  |  | Technical Architecture & Nar | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<main.PosterCanvas_canvas_) — Global Directory & Co | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.PosterCanvas) | https://www.agencejacquesparis.fr/   │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: var(--sp)   │
│ ====================================================================== │
│ [ HEADER BAR (<nav.Navbar_navbar__UMdI) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<main.ScrollEngine_scrol) — 390px Vertical Lead        | │
│ | H1: Jacques Paris - Agence à impact positif                        | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<main.ScrollEngine_vie) — 1-Col Stack              | │
│ | [ Item 1: Featured Work & Interactive Showcase                   ] | │
│ | [ Item 2: Technical Architecture & Narrative                     ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<main.PosterCanvas_canva) — 1-Col (Global Directory &) │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.PosterCanvas) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.Navbar_navbar__UMdIx> — `www-agencejacquesparis-fr`)**:
   - Landmark `<nav class="Navbar_navbar__UMdIx">` (`1440x50px`) hosting `Jacques Paris - Agence à impact posi` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-nscript="afterInteractive"`), and stylesheet rule `.PosterCanvas_canvas__BduZz { position:absolute;inset:0;overflow:hidden;background-color:var(--color-c... }`.
2. **Hero Stage & Focal Lead (<main.ScrollEngine_scrollSpace__HfjIP> — `Jacques Paris - Agence à impact po`)**:
   - Landmark `<main class="ScrollEngine_scrollSpace__HfjIP">` presenting display lead `Jacques Paris - Agence à impact positif` and copy excerpt *"Assistant Art Director"* over `#f0f0dc` canvas and `#001847` ink.
3. **Primary Showcase & Content Grid (<main.ScrollEngine_viewport__JJVIB> — `Featured Work & Interactive Showca`)**:
   - Landmark `<main class="ScrollEngine_viewport__JJVIB">` rendering section `Featured Work & Interactive Showcase` with copy *"Junior Business Partner"*, asset references (`jacques-logo.png`, `ad44a6578bd60804.css`, `074517235421c822.css`, `webpack-8fefb68f87553cee.js`), and grid rule `.ZoneLabel_primary__tb_mD { font-size:var(--text-xs);opacity:.35;letter-spacing:.05em }`.
4. **Interactive Detail & Feature Matrix (<main.PosterCanvas_canvas__BduZz> — `Technical Architecture & Narrative`)**:
   - Landmark `<main class="PosterCanvas_canvas__BduZz">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Creative Copywriter"*) with `#ffffff` surface cards, `#ffffff` accents, and `.ZoneLabel_secondary__sFo9Q { font-weight:300;color:var(--color-cobalt);line-height:1.4 }`.
5. **Colophon & Global Directory Footer (<footer.PosterCanvas_poster__O791U> — `https://www.agencejacquesparis.fr/`)**:
   - Landmark `<footer class="PosterCanvas_poster__O791U">` anchoring `Jacques Paris - Agence à impact ` footer links (`Overview · Index · Archive · About · Contact`), copy *"Senior Art Director"*, and `#c0c5be` structural dividers.
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=0px`, `0%`): Active landmark `Hero` · sticky/fixed elements: `6`
- **Step 02** (`y=850px`, `19%`): Active landmark `Section @ 19%` · sticky/fixed elements: `7`
- **Step 03** (`y=4500px`, `100%`): Active landmark `Footer / Bottom` · sticky/fixed elements: `7`

### Multi-Page Internal Route Map
- **Other Route (`/politique-de-confidentialite`)**: `https://www.agencejacquesparis.fr/politique-de-confidentialite` — H1: `Politique de protection des données personnelles`, scrollHeight `5138px`, transition `direct` (`503ms`)
- **Other Route (`/conditions-generales-utilisation`)**: `https://www.agencejacquesparis.fr/conditions-generales-utilisation` — H1: `Conditions générales d'utilisation`, scrollHeight `4542px`, transition `direct` (`349ms`)

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-agencejacquesparis-fr (Jacques Paris - Agence à impact positif)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-agencejacquesparis-fr` (**Jacques Paris - Agence à impact positif** — `https://www.agencejacquesparis.fr/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#f0f0dc` canvas, `#001847` ink, `#ffffff` accent).
- **Identity & Domain Context**: La créativité au service des marques qui veulent changer les choses et prendre soin de ce qui compte.
- **Primary Substrate**: `#f0f0dc` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#001847`, **Accent / Highlight**: `#ffffff`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#f0f0dc` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#001847` primary typography and `#ffffff` accents.
  - **Grounded Typographic Hierarchy**: Uses `ClashGrotesk` across display (`Jacques Paris - Agence à impact posi`) and body copy, paired with `SF Mono` for monospace/code.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: var(--space-lg)`, padding `var(--space-xl)`) with `cubic-bezier(0.25,0.1,0.25,1)` easing.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-agencejacquesparis-fr` in your global stylesheet:

:root {
  /* Jacques Paris - Agence à impact positif (www-agencejacquesparis-fr) — Live-Grounded CSS Variables */
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
- **Primary Canvas Substrate**: `#f0f0dc` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#001847` — grounded in live computed `main` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#ffffff` — grounded in `.ZoneCard_caseBtn__MWFpY { background: #ffffff }`
- **Interactive Accent / Highlight**: `#ffffff` — grounded in `.ZoneCard_caseBtn__MWFpY { background: #ffffff }`
- **Secondary / Muted Copy**: `#ffffff` — grounded in live computed `p` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#c0c5be` — grounded in `.InvitationForm_textarea__Xo0Zw { border-bottom: #c0c5be }`
- **Variable Token (`--color-cream-light`)**: `#f7f7ed` — grounded in `var(--color-cream-light)` in `:root`
- **Variable Token (`--color-cobalt-light`)**: `#1a3a6b` — grounded in `var(--color-cobalt-light)` in `:root`
- **Variable Token (`--color-teal`)**: `#0e9aa7` — grounded in `var(--color-teal)` in `:root`
- **Variable Token (`--color-coral`)**: `#e8442a` — grounded in `var(--color-coral)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1280×2484px` (multi-frame vertical journey filmstrip (2484px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×1744px` (full-page live capture (1744px), `390px` standard mobile width).
- **Container Max-Width**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport)
- **Padding & Gutters**: `var(--space-xl)` lateral canvas padding with `var(--space-lg)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: var(--space-lg)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `var(--space-xl)` horizontal padding
- **Media Queries**: `@media (min-width:1024px)`, `@media (prefers-reduced-motion:reduce)`
- **Corner Radii**: `2px`, `0px 0px 4px 4px`, `50%`, `3px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `ClashGrotesk`
- **Body Font Stack**: `ClashGrotesk`
- **Monospace / Technical Font Stack**: `SF Mono`
- **H1 Display Rule**: observed font-size ladder: `16px`, `22.4px`, `14px`, `13.3333px`, `var(--text-xs)`
- **H2 Section Rule**: rule `h2` (`font-size: var(--text-md)`, `letter-spacing: .01em`, `font-weight: 600`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--text-base: 15px`; rule `p` (`font-size: var(--text-base)`, `line-height: 1.7`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--text-xs: 11px`, `--text-sm: 14px`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-agencejacquesparis-fr` (`Jacques Paris - Agence à impact positif`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.Navbar_navbar__UMdIx> — `www-agencejacquesparis-fr`)**:
   - DOM & Selectors: Landmark `<nav class="Navbar_navbar__UMdIx">` (`1440x50px`) hosting `Jacques Paris - Agence à impact posi` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-nscript="afterInteractive"`), and stylesheet rule `.PosterCanvas_canvas__BduZz { position:absolute;inset:0;overflow:hidden;background-color:var(--color-c... }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.Navbar_navbar__UMdIx> — `www-agencejacquesparis-fr`)` (`www-agencejacquesparis-fr`) adapts across `@media (min-width:1024px)`, `@media (prefers-reduced-motion:reduce)` with `cubic-bezier(0.25,0.1,0.25,1)` transitions and links `Overview · Index · Archive · About · Contact`.
2. **Hero Stage & Focal Lead (<main.ScrollEngine_scrollSpace__HfjIP> — `Jacques Paris - Agence à impact po`)**:
   - DOM & Selectors: Landmark `<main class="ScrollEngine_scrollSpace__HfjIP">` presenting display lead `Jacques Paris - Agence à impact positif` and copy excerpt *"Assistant Art Director"* over `#f0f0dc` canvas and `#001847` ink.
   - Responsive Contract: Hero stage (`1280×2484px` desktop / `390×1744px` mobile) sets `#f0f0dc` background with `#001847` headline `Jacques Paris - Agence à impact positif`.
3. **Primary Showcase & Content Grid (<main.ScrollEngine_viewport__JJVIB> — `Featured Work & Interactive Showca`)**:
   - DOM & Selectors: Landmark `<main class="ScrollEngine_viewport__JJVIB">` rendering section `Featured Work & Interactive Showcase` with copy *"Junior Business Partner"*, asset references (`jacques-logo.png`, `ad44a6578bd60804.css`, `074517235421c822.css`, `webpack-8fefb68f87553cee.js`), and grid rule `.ZoneLabel_primary__tb_mD { font-size:var(--text-xs);opacity:.35;letter-spacing:.05em }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<main.ScrollEngine_viewport__JJVIB> — `Featured Work & Interactive Showca`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: var(--space-lg)`) on desktop and Single-column vertical stack at `390px` viewport width with `var(--space-xl)` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<main.PosterCanvas_canvas__BduZz> — `Technical Architecture & Narrative`)**:
   - DOM & Selectors: Landmark `<main class="PosterCanvas_canvas__BduZz">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Creative Copywriter"*) with `#ffffff` surface cards, `#ffffff` accents, and `.ZoneLabel_secondary__sFo9Q { font-weight:300;color:var(--color-cobalt);line-height:1.4 }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<main.PosterCanvas_canvas__BduZz> — `Technical Architecture & Narrative`)` uses `2px`, `0px 0px 4px 4px`, `50%`, `3px` radii, `#ffffff` highlights, and assets (jacques-logo.png, ad44a6578bd60804.css, 074517235421c822.css).
5. **Colophon & Global Directory Footer (<footer.PosterCanvas_poster__O791U> — `https://www.agencejacquesparis.fr/`)**:
   - DOM & Selectors: Landmark `<footer class="PosterCanvas_poster__O791U">` anchoring `Jacques Paris - Agence à impact ` footer links (`Overview · Index · Archive · About · Contact`), copy *"Senior Art Director"*, and `#c0c5be` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.PosterCanvas_poster__O791U> — `https://www.agencejacquesparis.fr/`)` aligns to `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport) with `var(--space-xl)` lateral canvas padding with `var(--space-lg)` grid gap and attributes (data-precedence="next", data-precedence="next", data-nscript="afterInteractive").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Assistant Art Director"*
- Copy Excerpt 2: *"Junior Business Partner"*
- Copy Excerpt 3: *"Creative Copywriter"*
- Copy Excerpt 4: *"Senior Art Director"*

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
- **Standard CSS Easing (`cubic-bezier(0.25,0.1,0.25,1)`)**: Default timing curve (no custom `cubic-bezier()` declared in captured CSS).
- **State & Hover Choreography**: Opacity and transform transitions on `<main.ScrollEngine_scrollSpace__HfjIP>` and `<main.ScrollEngine_viewport__JJVIB>` interactive targets.
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `native` vertical progression up to `5400px` across 3 distinct viewport chapters.
- **Vertical Chapter Sequence**: Hero (0%) -> Section @ 19% (19%) -> Footer / Bottom (100%).
- **Navigation Drawer / Menu State**: Replicate interactive menu toggle (`Menu`) with Escape-to-close keyboard handling.
- **Multi-Page Routes**: Scaffold internal routes `/politique-de-confidentialite` (other, direct), `/conditions-generales-utilisation` (other, direct) sharing the global header/footer shell and design tokens.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-agencejacquesparis-fr`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `0px` | `0%` | Hero | `6` | [desktop-step-01.webp](assets/desktop-step-01.webp) |
| `#02` | `850px` | `19%` | Section @ 19% | `7` | [desktop-step-02.webp](assets/desktop-step-02.webp) |
| `#03` | `4500px` | `100%` | Footer / Bottom | `7` | [desktop-step-03.webp](assets/desktop-step-03.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `0px` | `0%` | Hero | [mobile-step-01.webp](assets/mobile-step-01.webp) |
| `#02` | `4220px` | `100%` | Footer / Bottom | [mobile-step-02.webp](assets/mobile-step-02.webp) |

### Interactive UI State Captures (`1440×900` WebP)
| State Type | Trigger / Observation | Visual Asset |
| :--- | :--- | :--- |
| `nav_menu` | Nav/Menu opened (`Menu`, diff `53.14`) | [state-nav.webp](assets/state-nav.webp) |

### Internal Subpage Filmstrips (`1080px` Wide WebP)
| # | Template | Route URL | H1 / Title | Scroll Height | Transition | Filmstrip Asset |
| :-: | :---: | :--- | :--- | :---: | :---: | :--- |
| `2` | `other` | `https://www.agencejacquesparis.fr/politique-de-confidentialite` | Politique de protection des données p... | `5138px` | `direct` (`503ms`) | [subpage-02-politique-de-confidentialite.webp](assets/subpage-02-politique-de-confidentialite.webp) |
| `3` | `other` | `https://www.agencejacquesparis.fr/conditions-generales-utilisation` | Conditions générales d'utilisation | `4542px` | `direct` (`349ms`) | [subpage-03-conditions-generales-utilisation.webp](assets/subpage-03-conditions-generales-utilisation.webp) |

