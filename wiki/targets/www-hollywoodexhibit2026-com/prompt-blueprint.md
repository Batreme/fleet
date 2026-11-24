---
title: "UI Prompt Blueprint: www-hollywoodexhibit2026-com"
date: 2026-11-24
captured_at: 2026-11-24
target: "www-hollywoodexhibit2026-com"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
capture_mode: behavioral_journey_v2
asset_format: webp
scroll_driver: wheel
desktop_keyframes: 1
subpages_crawled: 0
http_status: 200
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#ffffff`)"
---

# UI Design System & Master Generation Blueprint: www-hollywoodexhibit2026-com

> **ELLE & Esquire, The New Hollywood Photography Exhibition** (https://www.hollywoodexhibit2026.com) — Hearst Galleries presented a joint photography exhibition for ELLE and Esquire, ELLE: The New Hollywood and Esquire Goes to Hollywood, fe...

![Desktop Journey Filmstrip (1280x828)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x872)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **ELLE & Esquire, The New Hollywood Photography Exhibition** (`https://www.hollywoodexhibit2026.com`). Hearst Galleries presented a joint photography exhibition for ELLE and Esquire, ELLE: The New Hollywood and Esquire Goes to Hollywood, fe...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#ffffff`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#000000` (live computed `html` `background-color` (`computed_styles.json`)) paired with `#ffffff` primary typography and `#ffffff` accents.
  - **Grounded Typographic Hierarchy**: Pairs `abcArizona` for display copy (`Choose which gallery you want to exp`) with `Apple Color Emoji` and `safiraMarch`.
  - **Calibrated Spatial Grid & Motion**: Combines `96rem` container bounds (`gap: 80px`, padding `0px`) with `cubic-bezier(.4,0,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×828px` (`assets/desktop-journey.webp`, `1` keyframes up to `y=0px` / doc `900px`), Mobile `390×872px` (`assets/mobile-journey.webp`, `1` keyframes).
- **Master Container Bounds**: `96rem` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `0px` lateral canvas padding with `80px` grid gap.
- **Border Radius Scale**: `var(--radius-8)`, `var(--radius-full)`, `50%`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 96rem`, `gap: 80px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `0px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `html` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h2` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#e7e7e7` | `:disabled { background-color: #e7e7e7 }` |
| **Interactive Accent / Highlight** | `#ffffff` | live computed `button` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#909090` | `:disabled { color: #909090 }` |
| **Structural Hairline Border** | `#808080` | `50 { border-color: #808080 }` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--spacing` | `.0625rem` | Layout / Spatial Grid Token |
| `--font-weight-light` | `300` | Canvas / Surface Token |
| `--animate-spin` | `spin 1s linear infinite` | Motion / Easing Token |
| `--default-transition-duration` | `.15s` | Motion / Easing Token |
| `--default-transition-timing-function` | `cubic-bezier(.4,0,.2,1)` | Motion / Easing Token |
| `--fluid-min-w` | `var(--layout-min-w,375)` | Design System Custom Token |
| `--fluid-max-w` | `var(--layout-max-w,1920)` | Layout / Spatial Grid Token |
| `--text-label--font-weight` | `400` | Typography Ink Token |
| `--text-label--line-height` | `1` | Typography Ink Token |
| `--text-label--letter-spacing` | `.03em` | Typography Ink Token |
| `--text-body-10--font-weight` | `400` | Typography Ink Token |
| `--text-body-10--line-height` | `1.25` | Typography Ink Token |
| `--text-body-10--letter-spacing` | `-2%` | Typography Ink Token |
| `--text-headline-10--font-weight` | `400` | Typography Ink Token |
| `--text-headline-10--line-height` | `1` | Typography Ink Token |
| `--text-headline-10--letter-spacing` | `normal` | Typography Ink Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `abcArizona`.
- **Primary Body Stack**: `Apple Color Emoji`.
- **Technical / Metadata Stack**: `safiraMarch`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: observed font-size ladder: `18.7573px`, `1em`, `80%`, `75%`, `var(--text-headline-10)`.
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 18.7573px`, `line-height: 23.4466px`, `font-weight: 400`, `letter-spacing: -2%`).
- **Body Copy**: live computed `body` (`font-size: 18.7573px`, `line-height: 23.4466px`, `font-weight: 400`, `letter-spacing: -2%`); CSS variables `--text-body-10--font-weight: 400`, `--text-body-10--line-height: 1.25`, `--text-body-10--letter-spacing: -2%`.
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 18.7573px`, `line-height: 23.4466px`, `font-weight: 400`, `letter-spacing: -2%`); CSS variables `--text-label--font-weight: 400`, `--text-label--line-height: 1`, `--text-label--letter-spacing: .03em`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.39,.57,.56,1)`, `cubic-bezier(.77,0,.18,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `layer theme`**: `transition: .15s` extracted from `www-hollywoodexhibit2026-com` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `www-hollywoodexhibit2026-com` stylesheet.
- **Selector `.transition-colors`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `www-hollywoodexhibit2026-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<header.wf-helveticaltpro-i4-active>` and `<main.wf-ivyprestodisplay-n3-active>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `wheel` (max document height `900px`, deepest scrollY reached `0px` across `1` desktop keyframes).
- **Detected Scroll / Motion Libraries**: `WebGL/Canvas`.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — ELLE & Esquire, The New Hollywood Photogra │
│ ====================================================================== │
│ [ <header.wf-helveticalt (1440px)     | Overview · Index · Archive · ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <main.wf-helveticaltpro-n7-active> (w=1440px)          | │
│ | H1: Choose which gallery you want to explore                       | │
│ | Substrate: #000000 | Ink: #ffffff | Accent: #ffffff                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<main.wf-ivyprestodisplay-) max-w: 96rem            | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Choose which gallery you     |  | www-hollywoodexhibit2026-com | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<main.wf-helveticaltpro-n3) — www-hollywoodexhibit2 | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.wf-ivypresto) | https://www.hollywoodexhibit2026.co  │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 80px)       │
│ ====================================================================== │
│ [ HEADER BAR (<header.wf-helveticaltpr) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<main.wf-helveticaltpro-) — 390px Vertical Lead        | │
│ | H1: Choose which gallery you want to explore                       | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<main.wf-ivyprestodisp) — 1-Col Stack              | │
│ | [ Item 1: Choose which gallery you                               ] | │
│ | [ Item 2: www-hollywoodexhibit2026-com Interactive Matrix        ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<main.wf-helveticaltpro-) — 1-Col (www-hollywoodexhib) │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.wf-ivypresto) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.wf-helveticaltpro-i4-active> — `www-hollywoodexhibit2026-com`)**:
   - Landmark `<header class="wf-helveticaltpro-i4-active">` (`1440px`) hosting `ELLE & Esquire, The New Hollywood Ph` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-engine="three.js r182"`, `data-nimg="fill"`, `data-nimg="fill"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<main.wf-helveticaltpro-n7-active> — `Choose which gallery you want to e`)**:
   - Landmark `<main class="wf-helveticaltpro-n7-active">` presenting display lead `Choose which gallery you want to explore` and copy excerpt *"Choose which gallery you"* over `#000000` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<main.wf-ivyprestodisplay-n3-active> — `Choose which gallery you`)**:
   - Landmark `<main class="wf-ivyprestodisplay-n3-active">` rendering section `Choose which gallery you` with copy *"Choose which gallery you want to explore"*, asset references (`ABCArizonaVariable-s.p.6844b0f6.w...`, `Haigrast-s.p.42f2de84.woff2`, `IvyPrestoHeadline_Thin-s.p.830ff3...`, `IvyPrestoText_Thin-s.p.3ba47ad4.w...`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<main.wf-helveticaltpro-n3-active> — `www-hollywoodexhibit2026-com Inter`)**:
   - Landmark `<main class="wf-helveticaltpro-n3-active">` framing `www-hollywoodexhibit2026-com Interactive Matrix` and `www-hollywoodexhibit2026-com Archive & Directory` (*"Choose which gallery you"*) with `#e7e7e7` surface cards, `#ffffff` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.wf-ivyprestodisplay-n4-active> — `https://www.hollywoodexhibit2026.com`)**:
   - Landmark `<footer class="wf-ivyprestodisplay-n4-active">` anchoring `ELLE & Esquire, The New Hollywoo` footer links (`Overview · Index · Archive · About · Contact`), copy *"www-hollywoodexhibit2026-com Interactive Matrix"*, and `#808080` structural dividers.
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=0px`, `0%`): Active landmark `Choose which gallery you want to explore` · sticky/fixed elements: `7`

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-hollywoodexhibit2026-com (ELLE & Esquire, The New Hollywood Photography Exhibition)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-hollywoodexhibit2026-com` (**ELLE & Esquire, The New Hollywood Photography Exhibition** — `https://www.hollywoodexhibit2026.com`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#ffffff`).
- **Identity & Domain Context**: Hearst Galleries presented a joint photography exhibition for ELLE and Esquire, ELLE: The New Hollywood and Esquire Goes to Hollywood, fe...
- **Primary Substrate**: `#000000` (live computed `html` `background-color` (`computed_styles.json`)), **Primary Ink**: `#ffffff`, **Accent / Highlight**: `#ffffff`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#000000` (live computed `html` `background-color` (`computed_styles.json`)) paired with `#ffffff` primary typography and `#ffffff` accents.
  - **Grounded Typographic Hierarchy**: Pairs `abcArizona` for display copy (`Choose which gallery you want to exp`) with `Apple Color Emoji` and `safiraMarch`.
  - **Calibrated Spatial Grid & Motion**: Combines `96rem` container bounds (`gap: 80px`, padding `0px`) with `cubic-bezier(.4,0,.2,1)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-hollywoodexhibit2026-com` in your global stylesheet:

:root {
  /* ELLE & Esquire, The New Hollywood Photography Exhibition (www-hollywoodexhibit2026-com) — Live-Grounded CSS Variables */
  --spacing: .0625rem; /* Layout / Spatial Grid Token (www-hollywoodexhibit2026-com) */
  --font-weight-light: 300; /* Canvas / Surface Token (www-hollywoodexhibit2026-com) */
  --animate-spin: spin 1s linear infinite; /* Motion / Easing Token (www-hollywoodexhibit2026-com) */
  --default-transition-duration: .15s; /* Motion / Easing Token (www-hollywoodexhibit2026-com) */
  --default-transition-timing-function: cubic-bezier(.4,0,.2,1); /* Motion / Easing Token (www-hollywoodexhibit2026-com) */
  --fluid-min-w: var(--layout-min-w,375); /* Design System Custom Token (www-hollywoodexhibit2026-com) */
  --fluid-max-w: var(--layout-max-w,1920); /* Layout / Spatial Grid Token (www-hollywoodexhibit2026-com) */
  --text-label--font-weight: 400; /* Typography Ink Token (www-hollywoodexhibit2026-com) */
  --text-label--line-height: 1; /* Typography Ink Token (www-hollywoodexhibit2026-com) */
  --text-label--letter-spacing: .03em; /* Typography Ink Token (www-hollywoodexhibit2026-com) */
  --text-body-10--font-weight: 400; /* Typography Ink Token (www-hollywoodexhibit2026-com) */
  --text-body-10--line-height: 1.25; /* Typography Ink Token (www-hollywoodexhibit2026-com) */
  --text-body-10--letter-spacing: -2%; /* Typography Ink Token (www-hollywoodexhibit2026-com) */
  --text-headline-10--font-weight: 400; /* Typography Ink Token (www-hollywoodexhibit2026-com) */
  --text-headline-10--line-height: 1; /* Typography Ink Token (www-hollywoodexhibit2026-com) */
  --text-headline-10--letter-spacing: normal; /* Typography Ink Token (www-hollywoodexhibit2026-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#000000` — grounded in live computed `html` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#ffffff` — grounded in live computed `h2` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#e7e7e7` — grounded in `:disabled { background-color: #e7e7e7 }`
- **Interactive Accent / Highlight**: `#ffffff` — grounded in live computed `button` `color` (`computed_styles.json`)
- **Secondary / Muted Copy**: `#909090` — grounded in `:disabled { color: #909090 }`
- **Structural Hairline Border**: `#808080` — grounded in `50 { border-color: #808080 }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1280×828px` (single-viewport 100vh live capture (900px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×872px` (full-page live capture (872px), `390px` standard mobile width).
- **Container Max-Width**: `96rem` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `0px` lateral canvas padding with `80px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 96rem`, `gap: 80px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `0px` horizontal padding
- **Media Queries**: `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)`
- **Corner Radii**: `var(--radius-8)`, `var(--radius-full)`, `50%`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `abcArizona`
- **Body Font Stack**: `Apple Color Emoji`
- **Monospace / Technical Font Stack**: `safiraMarch`
- **H1 Display Rule**: observed font-size ladder: `18.7573px`, `1em`, `80%`, `75%`, `var(--text-headline-10)`
- **H2 Section Rule**: live computed `h2` (`font-size: 18.7573px`, `line-height: 23.4466px`, `font-weight: 400`, `letter-spacing: -2%`)
- **Body Copy Rule**: live computed `body` (`font-size: 18.7573px`, `line-height: 23.4466px`, `font-weight: 400`, `letter-spacing: -2%`); CSS variables `--text-body-10--font-weight: 400`, `--text-body-10--line-height: 1.25`, `--text-body-10--letter-spacing: -2%`
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 18.7573px`, `line-height: 23.4466px`, `font-weight: 400`, `letter-spacing: -2%`); CSS variables `--text-label--font-weight: 400`, `--text-label--line-height: 1`, `--text-label--letter-spacing: .03em`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-hollywoodexhibit2026-com` (`ELLE & Esquire, The New Hollywood Photography Exhibition`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.wf-helveticaltpro-i4-active> — `www-hollywoodexhibit2026-com`)**:
   - DOM & Selectors: Landmark `<header class="wf-helveticaltpro-i4-active">` (`1440px`) hosting `ELLE & Esquire, The New Hollywood Ph` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-engine="three.js r182"`, `data-nimg="fill"`, `data-nimg="fill"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.wf-helveticaltpro-i4-active> — `www-hollywoodexhibit2026-com`)` (`www-hollywoodexhibit2026-com`) adapts across `@media (min-width:40rem)`, `@media (min-width:48rem)`, `@media (min-width:64rem)`, `@media (min-width:80rem)` with `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.39,.57,.56,1)`, `cubic-bezier(.77,0,.18,1)` transitions and links `Overview · Index · Archive · About · Contact`.
2. **Hero Stage & Focal Lead (<main.wf-helveticaltpro-n7-active> — `Choose which gallery you want to e`)**:
   - DOM & Selectors: Landmark `<main class="wf-helveticaltpro-n7-active">` presenting display lead `Choose which gallery you want to explore` and copy excerpt *"Choose which gallery you"* over `#000000` canvas and `#ffffff` ink.
   - Responsive Contract: Hero stage (`1280×828px` desktop / `390×872px` mobile) sets `#000000` background with `#ffffff` headline `Choose which gallery you want to explore`.
3. **Primary Showcase & Content Grid (<main.wf-ivyprestodisplay-n3-active> — `Choose which gallery you`)**:
   - DOM & Selectors: Landmark `<main class="wf-ivyprestodisplay-n3-active">` rendering section `Choose which gallery you` with copy *"Choose which gallery you want to explore"*, asset references (`ABCArizonaVariable-s.p.6844b0f6.w...`, `Haigrast-s.p.42f2de84.woff2`, `IvyPrestoHeadline_Thin-s.p.830ff3...`, `IvyPrestoText_Thin-s.p.3ba47ad4.w...`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<main.wf-ivyprestodisplay-n3-active> — `Choose which gallery you`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 96rem`, `gap: 80px`) on desktop and Single-column vertical stack at `390px` viewport width with `0px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<main.wf-helveticaltpro-n3-active> — `www-hollywoodexhibit2026-com Inter`)**:
   - DOM & Selectors: Landmark `<main class="wf-helveticaltpro-n3-active">` framing `www-hollywoodexhibit2026-com Interactive Matrix` and `www-hollywoodexhibit2026-com Archive & Directory` (*"Choose which gallery you"*) with `#e7e7e7` surface cards, `#ffffff` accents, and `strong { font-weight:bolder }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<main.wf-helveticaltpro-n3-active> — `www-hollywoodexhibit2026-com Inter`)` uses `var(--radius-8)`, `var(--radius-full)`, `50%` radii, `#ffffff` highlights, and assets (ABCArizonaVariable-s.p.6844b0f6.w..., Haigrast-s.p.42f2de84.woff2, IvyPrestoHeadline_Thin-s.p.830ff3...).
5. **Colophon & Global Directory Footer (<footer.wf-ivyprestodisplay-n4-active> — `https://www.hollywoodexhibit2026.com`)**:
   - DOM & Selectors: Landmark `<footer class="wf-ivyprestodisplay-n4-active">` anchoring `ELLE & Esquire, The New Hollywoo` footer links (`Overview · Index · Archive · About · Contact`), copy *"www-hollywoodexhibit2026-com Interactive Matrix"*, and `#808080` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.wf-ivyprestodisplay-n4-active> — `https://www.hollywoodexhibit2026.com`)` aligns to `96rem` (non-`@media` desktop container stylesheet rule) with `0px` lateral canvas padding with `80px` grid gap and attributes (data-precedence="next", data-engine="three.js r182", data-nimg="fill").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Choose which gallery you"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(.39,.57,.56,1)`, `cubic-bezier(.77,0,.18,1)`
- **Extracted Stylesheet Rules (`www-hollywoodexhibit2026-com`)**:
- `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`
- `strong { font-weight:bolder }`
- `small { font-size:80% }`
- `sup { vertical-align:baseline;font-size:75%;line-height:0;position:relative }`
- **Per-Selector Transition Rules**:
- **Selector `layer theme`**: `transition: .15s` extracted from `www-hollywoodexhibit2026-com` stylesheet.
- **Selector `.transition`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `www-hollywoodexhibit2026-com` stylesheet.
- **Selector `.transition-colors`**: `transition: var(--tw-ease,var(--default-transition-timing-function))` extracted from `www-hollywoodexhibit2026-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.2,1)`)**: Governs interactive state transitions across `<header.wf-helveticaltpro-i4-active>` and `<main.wf-ivyprestodisplay-n3-active>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `wheel` vertical progression up to `900px` across 1 distinct viewport chapters using WebGL/Canvas.
- **Vertical Chapter Sequence**: Choose which gallery you wa... (0%).

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-hollywoodexhibit2026-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `0px` | `0%` | Choose which gallery you want to explore | `7` | [desktop-step-01.webp](assets/desktop-step-01.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `0px` | `0%` | THE ELLE ESQUIRE HOLLYWOOD | [mobile-step-01.webp](assets/mobile-step-01.webp) |

