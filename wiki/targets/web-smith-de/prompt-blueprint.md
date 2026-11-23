---
title: "UI Prompt Blueprint: web-smith-de"
date: 2026-11-23
captured_at: 2026-11-23
target: "web-smith-de"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#0a1320` ink, `#0000ff` accent)"
---

# UI Design System & Master Generation Blueprint: web-smith-de

> **Internetagentur Ostwestfalen: Websites & SEO · Web Smith** (https://web-smith.de) — Websites, SEO und individuelle Software: Web Smith ist deine Internetagentur aus Ostwestfalen – mit kostenlosem Website-Check und Konfigu...

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Internetagentur Ostwestfalen: Websites & SEO · Web Smith** (`https://web-smith.de`). Websites, SEO und individuelle Software: Web Smith ist deine Internetagentur aus Ostwestfalen – mit kostenlosem Website-Check und Konfigu...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#0a1320` ink, `#0000ff` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#0a1320` primary typography and `#0000ff` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Plus Jakarta Sans` for display copy (`WIR ENTWICKELN DIGITALE LÖSUNGEN DIE`) with `Plus Jakarta Sans` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 14px`, padding `34px`) with `cubic-bezier(.22,1,.36,1)` easing.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, clamped at 2400px live multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport).
- **Canvas Lateral Padding & Spacing**: `34px` lateral canvas padding with `14px` grid gap.
- **Border Radius Scale**: `10px`, `50%`, `18px`, `var(--radius)`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 14px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `34px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width:1100px)`, `@media (max-width:760px)`, `@media (max-width:560px)`, `@media (prefers-reduced-motion:reduce)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#0a1320` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f5f7fa` | `var(--bg-soft)` in `:root` |
| **Interactive Accent / Highlight** | `#0000ff` | `a:hover { color: blue }` (`#0000ff`) |
| **Secondary / Muted Copy** | `#aeb8c7` | live computed `footer` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#dce2ea` | `var(--line)` in `:root` |
| **Variable Token (`--navy-2`)** | `#121e31` | `var(--navy-2)` in `:root` |
| **Variable Token (`--blue`)** | `#1d4fd8` | `var(--blue)` in `:root` |
| **Variable Token (`--blue-dark`)** | `#163faf` | `var(--blue-dark)` in `:root` |
| **Variable Token (`--brand`)** | `#3478f6` | `var(--brand)` in `:root` |
| **Variable Token (`--blue-soft`)** | `#8fb5fa` | `var(--blue-soft)` in `:root` |
| **Variable Token (`--text`)** | `#4a5566` | `var(--text)` in `:root` |
| **Variable Token (`--line-2`)** | `#cbd3df` | `var(--line-2)` in `:root` |
| **Variable Token (`--bg-hero`)** | `#f7f8fa` | `var(--bg-hero)` in `:root` |
| **Variable Token (`--chip`)** | `#f2f5f9` | `var(--chip)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--navy` | `#0a1320` | Layout / Spatial Grid Token |
| `--navy-2` | `#121e31` | Layout / Spatial Grid Token |
| `--blue` | `#1d4fd8` | Color / Atmospheric Token |
| `--blue-dark` | `#163faf` | Canvas / Surface Token |
| `--brand` | `#3478f6` | Brand / Palette Token |
| `--blue-soft` | `#8fb5fa` | Color / Atmospheric Token |
| `--text` | `#4a5566` | Typography Ink Token |
| `--muted` | `#aeb8c7` | Color / Atmospheric Token |
| `--line` | `#dce2ea` | Color / Atmospheric Token |
| `--line-2` | `#cbd3df` | Color / Atmospheric Token |
| `--bg-soft` | `#f5f7fa` | Canvas / Surface Token |
| `--bg-hero` | `#f7f8fa` | Canvas / Surface Token |
| `--chip` | `#f2f5f9` | Color / Atmospheric Token |
| `--white` | `#fff` | Canvas / Surface Token |
| `--radius` | `28px` | Elevation / Border Token |
| `--wrap` | `1180px` | Layout / Spatial Grid Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Plus Jakarta Sans`.
- **Primary Body Stack**: `Plus Jakarta Sans`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 76px`, `line-height: 79.04px`, `font-weight: 800`, `letter-spacing: -1.52px`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 40px`, `line-height: 42.4px`, `font-weight: 800`, `letter-spacing: -0.8px`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 26.4px`, `font-weight: 400`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 26.4px`, `font-weight: 400`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(.34,1.56,.64,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.hero__down[data-astro-cid-lcdefpme]`**: `transition: border-color .2s,transform .2s` extracted from `web-smith-de` stylesheet.
- **Selector `.lz__row[data-astro-cid-lcdefpme]`**: `transition: background-color .2s` extracted from `web-smith-de` stylesheet.
- **Selector `o-cid-lcdefpme] h3[data-astro-cid...`**: `transition: color .2s` extracted from `web-smith-de` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.22,1,.36,1)`)**: Governs interactive state transitions across `<header.hd>` and `<section.mq>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<section.hero>` and `<section.mq>` interactive targets.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Internetagentur Ostwestfalen: Websites & S │
│ ====================================================================== │
│ [ <header.hd> (1440x72px)             | Referenzen · Über uns        ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.hero> (w=1440px)                              | │
│ | H1: WIR ENTWICKELN DIGITALE LÖSUNGEN DIE WIRKEN.                   | │
│ | Substrate: #ffffff | Ink: #0a1320 | Accent: #0000ff                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.mq>) max-w: 1440px                         | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Wir entwickeln digitale Lösu |  | Alles, was dein Unternehmen  | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.sec>) — Webentwicklung                     | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.ft>         ) | https://web-smith.de                 │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 14px)       │
│ ====================================================================== │
│ [ HEADER BAR (<header.hd>             ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.hero>) — 390px Vertical Lead                  | │
│ | H1: WIR ENTWICKELN DIGITALE LÖSUNGEN DIE WIRKEN.                   | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.mq>) — 1-Col Stack                        | │
│ | [ Item 1: Wir entwickeln digitale Lösungen die wirken .          ] | │
│ | [ Item 2: Alles, was dein Unternehmen online sichtbar macht.     ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.sec>) — 1-Col (Webentwicklung)              | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.ft>         ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.hd> — `web-smith-de`)**:
   - Landmark `<header class="hd is-scrolled">` (`1440x72px`) hosting `Internetagentur Ostwestfalen: Websit` navigation (`Referenzen · Über uns`), DOM attributes (`data-astro-cid-nen7h5rs`, `data-hd`, `data-dd-item`, `data-dd-btn`), and stylesheet rule `hover { border-color:var(--navy);color:var(--navy);transform:translateY(3px) }`.
2. **Hero Stage & Focal Lead (<section.hero> — `WIR ENTWICKELN DIGITALE LÖSUNGEN D`)**:
   - Landmark `<section class="hero">` presenting display lead `WIR ENTWICKELN DIGITALE LÖSUNGEN DIE WIRKEN.` and copy excerpt *"Websites, SEO und individuelle Software für Unternehmen – schnell"* over `#ffffff` canvas and `#0a1320` ink.
3. **Primary Showcase & Content Grid (<section.mq> — `Wir entwickeln digitale Lösungen d`)**:
   - Landmark `<section class="mq">` rendering section `Wir entwickeln digitale Lösungen die wirken .` with copy *"Webdesign, Webentwicklung, SEO & SEA, Branding, Apps & APIs, KI-L"*, asset references (`favicon.ico`, `favicon.svg`, `favicon-32.png`, `favicon-192.png`), and grid rule `webkit-scrollbar { display:none }`.
4. **Interactive Detail & Feature Matrix (<section.sec> — `Alles, was dein Unternehmen online`)**:
   - Landmark `<section class="sec sec--blob">` framing `Alles, was dein Unternehmen online sichtbar macht.` and `Webentwicklung` (*"online sichtbar macht."*) with `#f5f7fa` surface cards, `#0000ff` accents, and `placeholder { color:8a96a8 }`.
5. **Colophon & Global Directory Footer (<footer.ft> — `https://web-smith.de`)**:
   - Landmark `<footer class="ft">` anchoring `Internetagentur Ostwestfalen: We` footer links (`Referenzen · Über uns`), copy *"Moderne Websites, Shops und Systeme – schnell, sicher und ge"*, and `#dce2ea` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: web-smith-de (Internetagentur Ostwestfalen: Websites & SEO · Web Smith)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `web-smith-de` (**Internetagentur Ostwestfalen: Websites & SEO · Web Smith** — `https://web-smith.de`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#0a1320` ink, `#0000ff` accent).
- **Identity & Domain Context**: Websites, SEO und individuelle Software: Web Smith ist deine Internetagentur aus Ostwestfalen – mit kostenlosem Website-Check und Konfigu...
- **Primary Substrate**: `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#0a1320`, **Accent / Highlight**: `#0000ff`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#ffffff` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#0a1320` primary typography and `#0000ff` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Plus Jakarta Sans` for display copy (`WIR ENTWICKELN DIGITALE LÖSUNGEN DIE`) with `Plus Jakarta Sans` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 14px`, padding `34px`) with `cubic-bezier(.22,1,.36,1)` easing.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `web-smith-de` in your global stylesheet:

:root {
  /* Internetagentur Ostwestfalen: Websites & SEO · Web Smith (web-smith-de) — Live-Grounded CSS Variables */
  --navy: #0a1320; /* Layout / Spatial Grid Token (web-smith-de) */
  --navy-2: #121e31; /* Layout / Spatial Grid Token (web-smith-de) */
  --blue: #1d4fd8; /* Color / Atmospheric Token (web-smith-de) */
  --blue-dark: #163faf; /* Canvas / Surface Token (web-smith-de) */
  --brand: #3478f6; /* Brand / Palette Token (web-smith-de) */
  --blue-soft: #8fb5fa; /* Color / Atmospheric Token (web-smith-de) */
  --text: #4a5566; /* Typography Ink Token (web-smith-de) */
  --muted: #aeb8c7; /* Color / Atmospheric Token (web-smith-de) */
  --line: #dce2ea; /* Color / Atmospheric Token (web-smith-de) */
  --line-2: #cbd3df; /* Color / Atmospheric Token (web-smith-de) */
  --bg-soft: #f5f7fa; /* Canvas / Surface Token (web-smith-de) */
  --bg-hero: #f7f8fa; /* Canvas / Surface Token (web-smith-de) */
  --chip: #f2f5f9; /* Color / Atmospheric Token (web-smith-de) */
  --white: #fff; /* Canvas / Surface Token (web-smith-de) */
  --radius: 28px; /* Elevation / Border Token (web-smith-de) */
  --wrap: 1180px; /* Layout / Spatial Grid Token (web-smith-de) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ffffff` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#0a1320` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#f5f7fa` — grounded in `var(--bg-soft)` in `:root`
- **Interactive Accent / Highlight**: `#0000ff` — grounded in `a:hover { color: blue }` (`#0000ff`)
- **Secondary / Muted Copy**: `#aeb8c7` — grounded in live computed `footer` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#dce2ea` — grounded in `var(--line)` in `:root`
- **Variable Token (`--navy-2`)**: `#121e31` — grounded in `var(--navy-2)` in `:root`
- **Variable Token (`--blue`)**: `#1d4fd8` — grounded in `var(--blue)` in `:root`
- **Variable Token (`--blue-dark`)**: `#163faf` — grounded in `var(--blue-dark)` in `:root`
- **Variable Token (`--brand`)**: `#3478f6` — grounded in `var(--brand)` in `:root`
- **Variable Token (`--blue-soft`)**: `#8fb5fa` — grounded in `var(--blue-soft)` in `:root`
- **Variable Token (`--text`)**: `#4a5566` — grounded in `var(--text)` in `:root`
- **Variable Token (`--line-2`)**: `#cbd3df` — grounded in `var(--line-2)` in `:root`
- **Variable Token (`--bg-hero`)**: `#f7f8fa` — grounded in `var(--bg-hero)` in `:root`
- **Variable Token (`--chip`)**: `#f2f5f9` — grounded in `var(--chip)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (clamped at 2400px live multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport)
- **Padding & Gutters**: `34px` lateral canvas padding with `14px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 14px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `34px` horizontal padding
- **Media Queries**: `@media (max-width:1100px)`, `@media (max-width:760px)`, `@media (max-width:560px)`, `@media (prefers-reduced-motion:reduce)`
- **Corner Radii**: `10px`, `50%`, `18px`, `var(--radius)`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Plus Jakarta Sans`
- **Body Font Stack**: `Plus Jakarta Sans`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: live computed `h1` (`font-size: 76px`, `line-height: 79.04px`, `font-weight: 800`, `letter-spacing: -1.52px`)
- **H2 Section Rule**: live computed `h2` (`font-size: 40px`, `line-height: 42.4px`, `font-weight: 800`, `letter-spacing: -0.8px`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 26.4px`, `font-weight: 400`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: 26.4px`, `font-weight: 400`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `web-smith-de` (`Internetagentur Ostwestfalen: Websites & SEO · Web Smith`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.hd> — `web-smith-de`)**:
   - DOM & Selectors: Landmark `<header class="hd is-scrolled">` (`1440x72px`) hosting `Internetagentur Ostwestfalen: Websit` navigation (`Referenzen · Über uns`), DOM attributes (`data-astro-cid-nen7h5rs`, `data-hd`, `data-dd-item`, `data-dd-btn`), and stylesheet rule `hover { border-color:var(--navy);color:var(--navy);transform:translateY(3px) }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.hd> — `web-smith-de`)` (`web-smith-de`) adapts across `@media (max-width:1100px)`, `@media (max-width:760px)`, `@media (max-width:560px)`, `@media (prefers-reduced-motion:reduce)` with `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(.34,1.56,.64,1)` transitions and links `Referenzen · Über uns`.
2. **Hero Stage & Focal Lead (<section.hero> — `WIR ENTWICKELN DIGITALE LÖSUNGEN D`)**:
   - DOM & Selectors: Landmark `<section class="hero">` presenting display lead `WIR ENTWICKELN DIGITALE LÖSUNGEN DIE WIRKEN.` and copy excerpt *"Websites, SEO und individuelle Software für Unternehmen – schnell"* over `#ffffff` canvas and `#0a1320` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#ffffff` background with `#0a1320` headline `WIR ENTWICKELN DIGITALE LÖSUNGEN DIE WIRKEN.`.
3. **Primary Showcase & Content Grid (<section.mq> — `Wir entwickeln digitale Lösungen d`)**:
   - DOM & Selectors: Landmark `<section class="mq">` rendering section `Wir entwickeln digitale Lösungen die wirken .` with copy *"Webdesign, Webentwicklung, SEO & SEA, Branding, Apps & APIs, KI-L"*, asset references (`favicon.ico`, `favicon.svg`, `favicon-32.png`, `favicon-192.png`), and grid rule `webkit-scrollbar { display:none }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.mq> — `Wir entwickeln digitale Lösungen d`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 14px`) on desktop and Single-column vertical stack at `390px` viewport width with `34px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.sec> — `Alles, was dein Unternehmen online`)**:
   - DOM & Selectors: Landmark `<section class="sec sec--blob">` framing `Alles, was dein Unternehmen online sichtbar macht.` and `Webentwicklung` (*"online sichtbar macht."*) with `#f5f7fa` surface cards, `#0000ff` accents, and `placeholder { color:8a96a8 }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.sec> — `Alles, was dein Unternehmen online`)` uses `10px`, `50%`, `18px`, `var(--radius)` radii, `#0000ff` highlights, and assets (favicon.ico, favicon.svg, favicon-32.png).
5. **Colophon & Global Directory Footer (<footer.ft> — `https://web-smith.de`)**:
   - DOM & Selectors: Landmark `<footer class="ft">` anchoring `Internetagentur Ostwestfalen: We` footer links (`Referenzen · Über uns`), copy *"Moderne Websites, Shops und Systeme – schnell, sicher und ge"*, and `#dce2ea` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.ft> — `https://web-smith.de`)` aligns to `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport) with `34px` lateral canvas padding with `14px` grid gap and attributes (data-astro-cid-nen7h5rs, data-hd, data-dd-item).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Websites, SEO und individuelle Software für Unternehmen – schnell, sicher und so g..."*
- Copy Excerpt 2: *"Webdesign, Webentwicklung, SEO & SEA, Branding, Apps & APIs, KI-Lösungen, Prototyp..."*
- Copy Excerpt 3: *"online sichtbar macht."*
- Copy Excerpt 4: *"Moderne Websites, Shops und Systeme – schnell, sicher und genau auf dein Business..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.22,1,.36,1)`, `cubic-bezier(.34,1.56,.64,1)`
- **Extracted Stylesheet Rules (`web-smith-de`)**:
- `hover { border-color:var(--navy);color:var(--navy);transform:translateY(3px) }`
- `webkit-scrollbar { display:none }`
- `placeholder { color:8a96a8 }`
- `focus { border-color:var(--brand);outline:none }`
- `svg { color:7faaf9 }`
- **Per-Selector Transition Rules**:
- **Selector `.hero__down[data-astro-cid-lcdefpme]`**: `transition: border-color .2s,transform .2s` extracted from `web-smith-de` stylesheet.
- **Selector `.lz__row[data-astro-cid-lcdefpme]`**: `transition: background-color .2s` extracted from `web-smith-de` stylesheet.
- **Selector `o-cid-lcdefpme] h3[data-astro-cid...`**: `transition: color .2s` extracted from `web-smith-de` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.22,1,.36,1)`)**: Governs interactive state transitions across `<header.hd>` and `<section.mq>`.
- **State & Hover Choreography**: Opacity and transform transitions on `<section.hero>` and `<section.mq>` interactive targets.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `web-smith-de`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
