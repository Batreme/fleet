---
title: "UI Prompt Blueprint: www-dontlookup-app"
date: 2026-11-15
target: "[[overview|www-dontlookup-app]]"
status: analyzed
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#f4f3ef` / `#9abeef`)"
---

# UI Design System & Master Generation Blueprint: www-dontlookup-app

> **Don't Look Up — a game about keeping everyone looking down** (https://www.dontlookup.app/) — You are very rich, very tall, and standing on quite a lot of people. Keep them distracted and they keep paying. Let them look up, and the...

![Desktop Viewport Capture (1440x2400)](file:///root/projects/fleet/wiki/targets/www-dontlookup-app/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Don't Look Up — a game about keeping everyone looking down** (`https://www.dontlookup.app/`). You are very rich, very tall, and standing on quite a lot of people. Keep them distracted and they keep paying. Let them look up, and the...
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#f4f3ef` / `#9abeef`)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#f4f3ef` (`var(--paper)` in `:root`) paired with `#14140f` primary typography and `#9abeef` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Marsipan` for display copy (`Don't Look Up — a game about keeping`) with `Luckiest Guy` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `1060px` container bounds (`gap: 13px`, padding `5px`) with `cubic-bezier(0.2,1.5,0.32,1)` easing and GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/www-dontlookup-app/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, capped at 2400px multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `1060px` extracted from `www-dontlookup-app` stylesheet.
- **Canvas Lateral Padding & Spacing**: `5px` lateral canvas padding with `13px` grid gap.
- **Border Radius Scale**: `12px`, `17px`, `3px`, `11px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1060px`, `gap: 13px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `5px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (prefers-reduced-motion: reduce)`, `@media (max-width: 1060px)`, `@media (max-width: 820px)`, `@media (max-width: 820px), (pointer: coarse)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#f4f3ef` | `var(--paper)` in `:root` |
| **Primary Typography Ink** | `#14140f` | `var(--ink)` in `:root` |
| **Elevated Surface / Card Substrate** | `#c0342a` | `var(--red)` in `:root` |
| **Interactive Accent / Highlight** | `#9abeef` | `var(--convert)` in `:root` |
| **Secondary / Muted Copy** | `#2b5a9b` | `var(--follow)` in `:root` |
| **Structural Hairline Border** | `#f8e08a` | `var(--y1)` in `:root` |
| **Variable Token (`--y2`)** | `#f2c31a` | `var(--y2)` in `:root` |
| **Variable Token (`--y3`)** | `#c98f06` | `var(--y3)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--paper` | `#f4f3ef` | Canvas / Surface Token |
| `--ink` | `#14140f` | Typography Ink Token |
| `--red` | `#c0342a` | Color / Atmospheric Token |
| `--btn-h` | `44px` | Dimension / Scale Token |
| `--convert` | `#9abeef` | Color / Atmospheric Token |
| `--follow` | `#2b5a9b` | Color / Atmospheric Token |
| `--y1` | `#f8e08a` | Color / Atmospheric Token |
| `--y2` | `#f2c31a` | Color / Atmospheric Token |
| `--y3` | `#c98f06` | Color / Atmospheric Token |
| `--btn-r` | `14px` | Dimension / Scale Token |
| `--body` | `'Nunito', ui-rounded, "SF Pro Rounded", system-ui, sans-serif` | Dimension / Scale Token |
| `--font` | `var(--body)` | Typography / Scale Token |
| `--hand` | `var(--body)` | Design System Custom Token |
| `--bw` | `2.5px` | Dimension / Scale Token |
| `--lift` | `5px` | Dimension / Scale Token |
| `--rail-n` | `8` | Design System Custom Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Marsipan`.
- **Primary Body Stack**: `Luckiest Guy`.
- **Technical / Metadata Stack**: `SFMono-Regular`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `13px`, `16px`, `10px`, `clamp(24px, 3.4vw, 40px)`, `11px`).
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `13px`, `16px`, `10px`, `clamp(24px, 3.4vw, 40px)`, `11px`).
- **Body Copy**: CSS variables `--body: 'Nunito', ui-rounded, "SF Pro Rounded", system-ui, sans-serif`.
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `13px`, `16px`, `10px`, `clamp(24px, 3.4vw, 40px)`, `11px`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.2,1.5,0.32,1)`, `cubic-bezier(0.45,0.05,0.55,0.95)`, `cubic-bezier(0.33,1,0.68,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.bubble`**: `transition: opacity 140ms ease-out` extracted from `www-dontlookup-app` stylesheet.
- **Selector `#bar > i`**: `transition: width 220ms linear` extracted from `www-dontlookup-app` stylesheet.
- **Selector `fee-fill`**: `transition: width 200ms linear` extracted from `www-dontlookup-app` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.2,1.5,0.32,1)`)**: Governs interactive state transitions across `<header.mcell>` and `<div.legend>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Don't Look Up — a game about keeping every │
│ ====================================================================== │
│ [ <header.mcell>           | here                                   ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <div.lbl>                                            |   │
│ | H1: Don't Look Up — a game about keeping everyone lo             |   │
│ | Substrate: #f4f3ef    | Ink: #14140f    | Accent: #9abeef        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<div.legend>              ) max-w: 1060px         |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Featured Work & Interactive  |  | Technical Architecture & Nar | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 13px  ) | │
│ | [<header.mcell>] -> [<div.lbl>] -> [<div.legend>] |                  │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.lsw>          ) | https://www.dontlookup.app/        │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.mcell> — `www-dontlookup-app`)**:
   - Landmark `<header class="mcell">` hosting `Don't Look Up — a game about keeping` navigation (`here`), DOM attributes (`data-engine="three.js r170"`), and stylesheet rule `stage { position: fixed; inset: 0; }`.
2. **Hero Stage & Focal Lead (<div.lbl> — `Don't Look Up — a game about keepi`)**:
   - Landmark `<div class="lbl">` presenting display lead `Don't Look Up — a game about keeping everyone lo` and copy excerpt *"Plant a distraction space"* over `#f4f3ef` canvas and `#14140f` ink.
3. **Primary Showcase & Content Grid (<div.legend> — `Featured Work & Interactive Showca`)**:
   - Landmark `<div class="legend">` rendering section `Featured Work & Interactive Showcase` with copy *"Plant a distraction"*, asset references (`favicon.ico`, `favicon-32.png`, `icon-192.png`, `apple-touch-icon.png`), and grid rule `stage canvas { display: block; touch-action: none; }`.
4. **Interactive Detail & Feature Matrix (<div.lrow> — `Technical Architecture & Narrative`)**:
   - Landmark `<div class="lrow">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"We count runs, not people. Anonymously, through Google Analytics,"*) with `#c0342a` surface cards, `#9abeef` accents, and `bubbles { position: fixed; inset: 0; pointer-events: none; overflow: hidden; }`.
5. **Colophon & Global Directory Footer (<footer.lsw> — `https://www.dontlookup.app/`)**:
   - Landmark `<footer class="lsw">` anchoring `Don't Look Up — a game about kee` footer links (`here`), copy *"Yellow has noticed. Pays nothing, talks the others round, an"*, and `#f8e08a` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-dontlookup-app (Don't Look Up — a game about keeping everyone looking down)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-dontlookup-app` (**Don't Look Up — a game about keeping everyone looking down** — `https://www.dontlookup.app/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f4f3ef` / `#9abeef`).
- **Identity & Domain Context**: You are very rich, very tall, and standing on quite a lot of people. Keep them distracted and they keep paying. Let them look up, and the...
- **Primary Substrate**: `#f4f3ef` (`var(--paper)` in `:root`), **Primary Ink**: `#14140f`, **Accent / Highlight**: `#9abeef`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#f4f3ef` (`var(--paper)` in `:root`) paired with `#14140f` primary typography and `#9abeef` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Marsipan` for display copy (`Don't Look Up — a game about keeping`) with `Luckiest Guy` and `SFMono-Regular`.
  - **Calibrated Spatial Grid & Motion**: Combines `1060px` container bounds (`gap: 13px`, padding `5px`) with `cubic-bezier(0.2,1.5,0.32,1)` easing and GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-dontlookup-app` in your global stylesheet:

:root {
  /* Don't Look Up — a game about keeping everyone looking down (www-dontlookup-app) — Ground-Truth Extracted CSS Variables */
  --paper: #f4f3ef; /* Canvas / Surface Token (www-dontlookup-app) */
  --ink: #14140f; /* Typography Ink Token (www-dontlookup-app) */
  --red: #c0342a; /* Color / Atmospheric Token (www-dontlookup-app) */
  --btn-h: 44px; /* Dimension / Scale Token (www-dontlookup-app) */
  --convert: #9abeef; /* Color / Atmospheric Token (www-dontlookup-app) */
  --follow: #2b5a9b; /* Color / Atmospheric Token (www-dontlookup-app) */
  --y1: #f8e08a; /* Color / Atmospheric Token (www-dontlookup-app) */
  --y2: #f2c31a; /* Color / Atmospheric Token (www-dontlookup-app) */
  --y3: #c98f06; /* Color / Atmospheric Token (www-dontlookup-app) */
  --btn-r: 14px; /* Dimension / Scale Token (www-dontlookup-app) */
  --body: 'Nunito', ui-rounded, "SF Pro Rounded", system-ui, sans-serif; /* Dimension / Scale Token (www-dontlookup-app) */
  --font: var(--body); /* Typography / Scale Token (www-dontlookup-app) */
  --hand: var(--body); /* Design System Custom Token (www-dontlookup-app) */
  --bw: 2.5px; /* Dimension / Scale Token (www-dontlookup-app) */
  --lift: 5px; /* Dimension / Scale Token (www-dontlookup-app) */
  --rail-n: 8; /* Design System Custom Token (www-dontlookup-app) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#f4f3ef` — grounded in `var(--paper)` in `:root`
- **Primary Typography Ink**: `#14140f` — grounded in `var(--ink)` in `:root`
- **Elevated Surface / Card Substrate**: `#c0342a` — grounded in `var(--red)` in `:root`
- **Interactive Accent / Highlight**: `#9abeef` — grounded in `var(--convert)` in `:root`
- **Secondary / Muted Copy**: `#2b5a9b` — grounded in `var(--follow)` in `:root`
- **Structural Hairline Border**: `#f8e08a` — grounded in `var(--y1)` in `:root`
- **Variable Token (`--y2`)**: `#f2c31a` — grounded in `var(--y2)` in `:root`
- **Variable Token (`--y3`)**: `#c98f06` — grounded in `var(--y3)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (capped at 2400px multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1060px` extracted from `www-dontlookup-app` stylesheet
- **Padding & Gutters**: `5px` lateral canvas padding with `13px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1060px`, `gap: 13px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `5px` horizontal padding
- **Media Queries**: `@media (prefers-reduced-motion: reduce)`, `@media (max-width: 1060px)`, `@media (max-width: 820px)`, `@media (max-width: 820px), (pointer: coarse)`
- **Corner Radii**: `12px`, `17px`, `3px`, `11px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Marsipan`
- **Body Font Stack**: `Luckiest Guy`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **H1 Display Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `13px`, `16px`, `10px`, `clamp(24px, 3.4vw, 40px)`, `11px`)
- **H2 Section Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `13px`, `16px`, `10px`, `clamp(24px, 3.4vw, 40px)`, `11px`)
- **Body Copy Rule**: CSS variables `--body: 'Nunito', ui-rounded, "SF Pro Rounded", system-ui, sans-serif`
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `13px`, `16px`, `10px`, `clamp(24px, 3.4vw, 40px)`, `11px`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-dontlookup-app` (`Don't Look Up — a game about keeping everyone looking down`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.mcell> — `www-dontlookup-app`)**:
   - DOM & Selectors: Landmark `<header class="mcell">` hosting `Don't Look Up — a game about keeping` navigation (`here`), DOM attributes (`data-engine="three.js r170"`), and stylesheet rule `stage { position: fixed; inset: 0; }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.mcell> — `www-dontlookup-app`)` (`www-dontlookup-app`) adapts across `@media (prefers-reduced-motion: reduce)`, `@media (max-width: 1060px)`, `@media (max-width: 820px)`, `@media (max-width: 820px), (pointer: coarse)` with `cubic-bezier(0.2,1.5,0.32,1)`, `cubic-bezier(0.45,0.05,0.55,0.95)`, `cubic-bezier(0.33,1,0.68,1)` transitions and links `here`.
2. **Hero Stage & Focal Lead (<div.lbl> — `Don't Look Up — a game about keepi`)**:
   - DOM & Selectors: Landmark `<div class="lbl">` presenting display lead `Don't Look Up — a game about keeping everyone lo` and copy excerpt *"Plant a distraction space"* over `#f4f3ef` canvas and `#14140f` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#f4f3ef` background with `#14140f` headline `Don't Look Up — a game about keeping everyone lo`.
3. **Primary Showcase & Content Grid (<div.legend> — `Featured Work & Interactive Showca`)**:
   - DOM & Selectors: Landmark `<div class="legend">` rendering section `Featured Work & Interactive Showcase` with copy *"Plant a distraction"*, asset references (`favicon.ico`, `favicon-32.png`, `icon-192.png`, `apple-touch-icon.png`), and grid rule `stage canvas { display: block; touch-action: none; }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<div.legend> — `Featured Work & Interactive Showca`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1060px`, `gap: 13px`) on desktop and Single-column vertical stack at `390px` viewport width with `5px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<div.lrow> — `Technical Architecture & Narrative`)**:
   - DOM & Selectors: Landmark `<div class="lrow">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"We count runs, not people. Anonymously, through Google Analytics,"*) with `#c0342a` surface cards, `#9abeef` accents, and `bubbles { position: fixed; inset: 0; pointer-events: none; overflow: hidden; }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<div.lrow> — `Technical Architecture & Narrative`)` uses `12px`, `17px`, `3px`, `11px` radii, `#9abeef` highlights, and assets (favicon.ico, favicon-32.png, icon-192.png).
5. **Colophon & Global Directory Footer (<footer.lsw> — `https://www.dontlookup.app/`)**:
   - DOM & Selectors: Landmark `<footer class="lsw">` anchoring `Don't Look Up — a game about kee` footer links (`here`), copy *"Yellow has noticed. Pays nothing, talks the others round, an"*, and `#f8e08a` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.lsw> — `https://www.dontlookup.app/`)` aligns to `1060px` extracted from `www-dontlookup-app` stylesheet with `5px` lateral canvas padding with `13px` grid gap and attributes (data-engine="three.js r170").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Plant a distraction space"*
- Copy Excerpt 2: *"Plant a distraction"*
- Copy Excerpt 3: *"We count runs, not people. Anonymously, through Google Analytics, and only if you..."*
- Copy Excerpt 4: *"Yellow has noticed. Pays nothing, talks the others round, and walks to your feet."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.2,1.5,0.32,1)`, `cubic-bezier(0.45,0.05,0.55,0.95)`, `cubic-bezier(0.33,1,0.68,1)`
- **Extracted Stylesheet Rules (`www-dontlookup-app`)**:
- `stage { position: fixed; inset: 0; }`
- `stage canvas { display: block; touch-action: none; }`
- `bubbles { position: fixed; inset: 0; pointer-events: none; overflow: hidden; }`
- `.btail-fill { fill: fff; }`
- `.bubble.is-visible { opacity: 1; }`
- **Per-Selector Transition Rules**:
- **Selector `.bubble`**: `transition: opacity 140ms ease-out` extracted from `www-dontlookup-app` stylesheet.
- **Selector `#bar > i`**: `transition: width 220ms linear` extracted from `www-dontlookup-app` stylesheet.
- **Selector `fee-fill`**: `transition: width 200ms linear` extracted from `www-dontlookup-app` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.2,1.5,0.32,1)`)**: Governs interactive state transitions across `<header.mcell>` and `<div.legend>`.
- **Runtime Interaction Engine**: Integrates GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-dontlookup-app`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
