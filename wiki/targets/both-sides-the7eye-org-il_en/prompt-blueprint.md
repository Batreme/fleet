---
title: "UI Prompt Blueprint: both-sides-the7eye-org-il_en"
date: 2026-11-15
target: "both-sides-the7eye-org-il_en"
status: analyzed
capture: specimen
capture_desktop: dom
capture_mobile: specimen
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#FDFCFF` / `#E1E1E1`)"
---

# UI Design System & Master Generation Blueprint: both-sides-the7eye-org-il_en

> **Extremists on Both Sides** (https://both-sides.the7eye.org.il/en/) — We collected thousands of political actions carried out in public space over the past four years. Decide for yourself — who are the extre...

![Desktop Viewport Capture](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Extremists on Both Sides** (`https://both-sides.the7eye.org.il/en/`). We collected thousands of political actions carried out in public space over the past four years. Decide for yourself — who are the extre...
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#FDFCFF` / `#E1E1E1`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#FDFCFF` (`var(--bg)` in `:root`) paired with `#111` primary typography and `#E1E1E1` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Assistant` for display copy (`Text description of the data`) with `Josefin Slab` and `IBM Plex Sans Arabic`.
  - **Calibrated Spatial Grid & Motion**: Combines `600px` container bounds (`gap: 8px`, padding `2px`) with `cubic-bezier(0.22,1,0.36,1)` easing and Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Design Specimen (Offline WebGL/JS Fallback — not live site capture)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×21770px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `600px` extracted from `both-sides-the7eye-org-il_en` stylesheet.
- **Canvas Lateral Padding & Spacing**: `2px` lateral canvas padding with `8px` grid gap.
- **Border Radius Scale**: `4px`, `6px`, `8px`, `20px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 600px`, `gap: 8px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `2px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width: 600px)`, `@media (max-width: 600px) and (hover: hover) and (pointer: fine)`, `@media (min-width: 601px)`, `@media (min-width: 640px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#FDFCFF` | `var(--bg)` in `:root` |
| **Primary Typography Ink** | `#111` | `var(--ink)` in `:root` |
| **Elevated Surface / Card Substrate** | `#767676` | `var(--muted-ui)` in `:root` |
| **Interactive Accent / Highlight** | `#E1E1E1` | `var(--line-light)` in `:root` |
| **Secondary / Muted Copy** | `#25D366` | `var(--brand)` in `:root` |
| **Structural Hairline Border** | `#393239` | `var(--se-ink)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bg` | `#FDFCFF` | Canvas / Surface Token |
| `--card-w` | `min(456px, 100vw - 48px)` | Dimension / Scale Token |
| `--card-top` | `4.4vh` | Dimension / Scale Token |
| `--ink` | `#111` | Typography Ink Token |
| `--ink-soft` | `rgba(0, 0, 0, 0.81)` | Typography Ink Token |
| `--ink-note` | `rgba(0, 0, 0, 0.85)` | Typography Ink Token |
| `--muted-ui` | `#767676` | Color / Atmospheric Token |
| `--line-light` | `#E1E1E1` | Canvas / Surface Token |
| `--font-body` | `'Assistant', sans-serif` | Typography / Scale Token |
| `--font-title` | `'Discordia', serif` | Typography / Scale Token |
| `--font-ar` | `'IBM Plex Sans Arabic', 'Assistant', sans-serif` | Typography / Scale Token |
| `--ui-fade-ms` | `180ms` | Motion / Timing Token |
| `--tray-ms` | `.85s` | Motion / Timing Token |
| `--tray-ease` | `cubic-bezier(0.22, 1, 0.36, 1)` | Motion / Easing Token |
| `--fade-ms` | `.35s` | Motion / Timing Token |
| `--p9-pop-ms` | `280ms` | Motion / Timing Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Assistant`.
- **Primary Body Stack**: `Josefin Slab`.
- **Technical / Metadata Stack**: `IBM Plex Sans Arabic`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: CSS variables `--se-cap-display: block`.
- **Section Heading (`H2`)**: rule `.section-title` (`font-size: 36px`, `line-height: 1.2`).
- **Body Copy**: CSS variables `--font-body: 'Assistant', sans-serif`.
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `18px`, `16px`, `36px`, `26px`, `14px`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.22,1,0.36,1)`, `cubic-bezier(0.37,0,0.63,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.page9-title-row .page9-header-su...`**: `transition: opacity var(--fade-ms) ease-out` extracted from `both-sides-the7eye-org-il_en` stylesheet.
- **Selector `-title-row .text-card .text-card-...`**: `transition: opacity var(--fade-ms) ease-out` extracted from `both-sides-the7eye-org-il_en` stylesheet.
- **Selector `page9-title-row .text-card .text-...`**: `transition: background var(--fade-ms) ease-out` extracted from `both-sides-the7eye-org-il_en` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.22,1,0.36,1)`)**: Governs interactive state transitions across `<nav.lang-wrap>` and `<section.text-section>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Extremists on Both Sides                   │
│ ====================================================================== │
│ [ <nav.lang-wrap>          | עברית · English · العربية              ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.a11y-only>                                  |   │
│ | H1: Text description of the data                                 |   │
│ | Substrate: #FDFCFF    | Ink: #111       | Accent: #E1E1E1        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.text-section>    ) max-w: 600px          |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | By camp and group            |  | The Netanyahu Coalition — 8, | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 8px   ) | │
│ | [<nav.lang-wrap>] -> [<section.a11y-only] -> [<section.text-sect] |  │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.page0-dots-ove) | https://both-sides.the7eye.org.il/ │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.lang-wrap> — `both-sides-the7eye-org-il_en`)**:
   - Landmark `<nav class="lang-wrap">` hosting `Extremists on Both Sides` navigation (`עברית · English · العربية`), DOM attributes (`data-page="0"`, `data-page="1"`, `data-page="2"`, `data-page="3"`), and stylesheet rule `html { touch-action: pan-x pan-y; }`.
2. **Hero Stage & Focal Lead (<section.a11y-only> — `Text description of the data`)**:
   - Landmark `<section class="a11y-only">` presenting display lead `Text description of the data` and copy excerpt *"The project shows 14,300 documented political actions that took p"* over `#FDFCFF` canvas and `#111` ink.
3. **Primary Showcase & Content Grid (<section.text-section> — `By camp and group`)**:
   - Landmark `<section class="text-section">` rendering section `By camp and group` with copy *"Haredi Jewish protesters: 492 documented actions"*, asset references (`favicon.svg`, `favicon-32.png`, `favicon-192.png`, `apple-touch-icon.png`), and grid rule `body { background: var(--bg); }`.
4. **Interactive Detail & Feature Matrix (<section.text-section> — `The Netanyahu Coalition — 8,499 do`)**:
   - Landmark `<section class="text-section">` framing `The Netanyahu Coalition — 8,499 documented actions` and `The Change Bloc — 5,801 documented actions` (*"West Bank settler movements: 7,698 documented actions"*) with `#767676` surface cards, `#E1E1E1` accents, and `after { -webkit-user-select: none !important; user-select: none !important; -web... }`.
5. **Colophon & Global Directory Footer (<footer.page0-dots-overlay> — `https://both-sides.the7eye.org.il/en/`)**:
   - Landmark `<footer class="page0-dots-overlay">` anchoring `Extremists on Both Sides` footer links (`עברית · English · العربية`), copy *"Conservative right-wing groups: 309 documented actions"*, and `#393239` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: both-sides-the7eye-org-il_en (Extremists on Both Sides)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `both-sides-the7eye-org-il_en` (**Extremists on Both Sides** — `https://both-sides.the7eye.org.il/en/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#FDFCFF` / `#E1E1E1`).
- **Identity & Domain Context**: We collected thousands of political actions carried out in public space over the past four years. Decide for yourself — who are the extre...
- **Primary Substrate**: `#FDFCFF` (`var(--bg)` in `:root`), **Primary Ink**: `#111`, **Accent / Highlight**: `#E1E1E1`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#FDFCFF` (`var(--bg)` in `:root`) paired with `#111` primary typography and `#E1E1E1` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Assistant` for display copy (`Text description of the data`) with `Josefin Slab` and `IBM Plex Sans Arabic`.
  - **Calibrated Spatial Grid & Motion**: Combines `600px` container bounds (`gap: 8px`, padding `2px`) with `cubic-bezier(0.22,1,0.36,1)` easing and Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `both-sides-the7eye-org-il_en` in your global stylesheet:

:root {
  /* Extremists on Both Sides (both-sides-the7eye-org-il_en) — Ground-Truth Extracted CSS Variables */
  --bg: #FDFCFF; /* Canvas / Surface Token (both-sides-the7eye-org-il_en) */
  --card-w: min(456px, 100vw - 48px); /* Dimension / Scale Token (both-sides-the7eye-org-il_en) */
  --card-top: 4.4vh; /* Dimension / Scale Token (both-sides-the7eye-org-il_en) */
  --ink: #111; /* Typography Ink Token (both-sides-the7eye-org-il_en) */
  --ink-soft: rgba(0, 0, 0, 0.81); /* Typography Ink Token (both-sides-the7eye-org-il_en) */
  --ink-note: rgba(0, 0, 0, 0.85); /* Typography Ink Token (both-sides-the7eye-org-il_en) */
  --muted-ui: #767676; /* Color / Atmospheric Token (both-sides-the7eye-org-il_en) */
  --line-light: #E1E1E1; /* Canvas / Surface Token (both-sides-the7eye-org-il_en) */
  --font-body: 'Assistant', sans-serif; /* Typography / Scale Token (both-sides-the7eye-org-il_en) */
  --font-title: 'Discordia', serif; /* Typography / Scale Token (both-sides-the7eye-org-il_en) */
  --font-ar: 'IBM Plex Sans Arabic', 'Assistant', sans-serif; /* Typography / Scale Token (both-sides-the7eye-org-il_en) */
  --ui-fade-ms: 180ms; /* Motion / Timing Token (both-sides-the7eye-org-il_en) */
  --tray-ms: .85s; /* Motion / Timing Token (both-sides-the7eye-org-il_en) */
  --tray-ease: cubic-bezier(0.22, 1, 0.36, 1); /* Motion / Easing Token (both-sides-the7eye-org-il_en) */
  --fade-ms: .35s; /* Motion / Timing Token (both-sides-the7eye-org-il_en) */
  --p9-pop-ms: 280ms; /* Motion / Timing Token (both-sides-the7eye-org-il_en) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#FDFCFF` — grounded in `var(--bg)` in `:root`
- **Primary Typography Ink**: `#111` — grounded in `var(--ink)` in `:root`
- **Elevated Surface / Card Substrate**: `#767676` — grounded in `var(--muted-ui)` in `:root`
- **Interactive Accent / Highlight**: `#E1E1E1` — grounded in `var(--line-light)` in `:root`
- **Secondary / Muted Copy**: `#25D366` — grounded in `var(--brand)` in `:root`
- **Structural Hairline Border**: `#393239` — grounded in `var(--se-ink)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×21770px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `600px` extracted from `both-sides-the7eye-org-il_en` stylesheet
- **Padding & Gutters**: `2px` lateral canvas padding with `8px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 600px`, `gap: 8px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `2px` horizontal padding
- **Media Queries**: `@media (max-width: 600px)`, `@media (max-width: 600px) and (hover: hover) and (pointer: fine)`, `@media (min-width: 601px)`, `@media (min-width: 640px)`
- **Corner Radii**: `4px`, `6px`, `8px`, `20px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Assistant`
- **Body Font Stack**: `Josefin Slab`
- **Monospace / Technical Font Stack**: `IBM Plex Sans Arabic`
- **H1 Display Rule**: CSS variables `--se-cap-display: block`
- **H2 Section Rule**: rule `.section-title` (`font-size: 36px`, `line-height: 1.2`)
- **Body Copy Rule**: CSS variables `--font-body: 'Assistant', sans-serif`
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `18px`, `16px`, `36px`, `26px`, `14px`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `both-sides-the7eye-org-il_en` (`Extremists on Both Sides`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.lang-wrap> — `both-sides-the7eye-org-il_en`)**:
   - DOM & Selectors: Landmark `<nav class="lang-wrap">` hosting `Extremists on Both Sides` navigation (`עברית · English · العربية`), DOM attributes (`data-page="0"`, `data-page="1"`, `data-page="2"`, `data-page="3"`), and stylesheet rule `html { touch-action: pan-x pan-y; }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.lang-wrap> — `both-sides-the7eye-org-il_en`)` (`both-sides-the7eye-org-il_en`) adapts across `@media (max-width: 600px)`, `@media (max-width: 600px) and (hover: hover) and (pointer: fine)`, `@media (min-width: 601px)`, `@media (min-width: 640px)` with `cubic-bezier(0.22,1,0.36,1)`, `cubic-bezier(0.37,0,0.63,1)` transitions and links `עברית · English · العربية`.
2. **Hero Stage & Focal Lead (<section.a11y-only> — `Text description of the data`)**:
   - DOM & Selectors: Landmark `<section class="a11y-only">` presenting display lead `Text description of the data` and copy excerpt *"The project shows 14,300 documented political actions that took p"* over `#FDFCFF` canvas and `#111` ink.
   - Responsive Contract: Hero stage (`1440×21770px` desktop / `390×2400px` mobile) sets `#FDFCFF` background with `#111` headline `Text description of the data`.
3. **Primary Showcase & Content Grid (<section.text-section> — `By camp and group`)**:
   - DOM & Selectors: Landmark `<section class="text-section">` rendering section `By camp and group` with copy *"Haredi Jewish protesters: 492 documented actions"*, asset references (`favicon.svg`, `favicon-32.png`, `favicon-192.png`, `apple-touch-icon.png`), and grid rule `body { background: var(--bg); }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.text-section> — `By camp and group`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 600px`, `gap: 8px`) on desktop and Single-column vertical stack at `390px` viewport width with `2px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.text-section> — `The Netanyahu Coalition — 8,499 do`)**:
   - DOM & Selectors: Landmark `<section class="text-section">` framing `The Netanyahu Coalition — 8,499 documented actions` and `The Change Bloc — 5,801 documented actions` (*"West Bank settler movements: 7,698 documented actions"*) with `#767676` surface cards, `#E1E1E1` accents, and `after { -webkit-user-select: none !important; user-select: none !important; -web... }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.text-section> — `The Netanyahu Coalition — 8,499 do`)` uses `4px`, `6px`, `8px`, `20px` radii, `#E1E1E1` highlights, and assets (favicon.svg, favicon-32.png, favicon-192.png).
5. **Colophon & Global Directory Footer (<footer.page0-dots-overlay> — `https://both-sides.the7eye.org.il/en/`)**:
   - DOM & Selectors: Landmark `<footer class="page0-dots-overlay">` anchoring `Extremists on Both Sides` footer links (`עברית · English · العربية`), copy *"Conservative right-wing groups: 309 documented actions"*, and `#393239` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.page0-dots-overlay> — `https://both-sides.the7eye.org.il/en/`)` aligns to `600px` extracted from `both-sides-the7eye-org-il_en` stylesheet with `2px` lateral canvas padding with `8px` grid gap and attributes (data-page="0", data-page="1", data-page="2").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"The project shows 14,300 documented political actions that took place in public sp..."*
- Copy Excerpt 2: *"Haredi Jewish protesters: 492 documented actions"*
- Copy Excerpt 3: *"West Bank settler movements: 7,698 documented actions"*
- Copy Excerpt 4: *"Conservative right-wing groups: 309 documented actions"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.22,1,0.36,1)`, `cubic-bezier(0.37,0,0.63,1)`
- **Extracted Stylesheet Rules (`both-sides-the7eye-org-il_en`)**:
- `html { touch-action: pan-x pan-y; }`
- `body { background: var(--bg); }`
- `after { -webkit-user-select: none !important; user-select: none !important; -web... }`
- `.fold-number-badge.is-visible { display: block; }`
- `.fold-number-badge.is-dot { display: none; }`
- **Per-Selector Transition Rules**:
- **Selector `.page9-title-row .page9-header-su...`**: `transition: opacity var(--fade-ms) ease-out` extracted from `both-sides-the7eye-org-il_en` stylesheet.
- **Selector `-title-row .text-card .text-card-...`**: `transition: opacity var(--fade-ms) ease-out` extracted from `both-sides-the7eye-org-il_en` stylesheet.
- **Selector `page9-title-row .text-card .text-...`**: `transition: background var(--fade-ms) ease-out` extracted from `both-sides-the7eye-org-il_en` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.22,1,0.36,1)`)**: Governs interactive state transitions across `<nav.lang-wrap>` and `<section.text-section>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `both-sides-the7eye-org-il_en`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
