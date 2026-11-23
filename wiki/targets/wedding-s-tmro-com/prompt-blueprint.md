---
title: "UI Prompt Blueprint: wedding-s-tmro-com"
date: 2026-11-23
captured_at: 2026-11-23
target: "wedding-s-tmro-com"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#f7f7f7` / `#333333`)"
---

# UI Design System & Master Generation Blueprint: wedding-s-tmro-com

> **Wedding Invitation · Yuri & Tomoro** (https://wedding.s-tmro.com/) — 結婚式へのご招待です。日時は2026年11月29日（いい肉の日）、10:00に受付、10:30に開始です。会場は桜通線「国際センター」駅近くのレストラン「recipe」です。

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Wedding Invitation · Yuri & Tomoro** (`https://wedding.s-tmro.com/`). 結婚式へのご招待です。日時は2026年11月29日（いい肉の日）、10:00に受付、10:30に開始です。会場は桜通線「国際センター」駅近くのレストラン「recipe」です。
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#f7f7f7` / `#333333`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#f7f7f7` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#333333` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Stack Sans Notch` for display copy (`Wedding Invitation · Yuri & Tomoro`) with `Italianno` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 40px`, padding `10px`) with `cubic-bezier(0.4,0.4,0,1)` easing and Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, clamped at 2400px live multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport).
- **Canvas Lateral Padding & Spacing**: `10px` lateral canvas padding with `40px` grid gap.
- **Border Radius Scale**: `2px`, `6px`, `8px`, `0px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 40px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `10px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (prefers-reduced-motion: reduce)`, `@media (min-resolution: 1.5dppx)`, `@media (min-resolution: 1dppx) and (max-resolution: 1.5dppx)`, `@media (max-resolution: 1dppx)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f7f7f7` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `body` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `body { background: #ffffff }` |
| **Interactive Accent / Highlight** | `#333333` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#333333` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#cccccc` | `hr { border-top: #cccccc }` |
| **Variable Token (`--s-color-27b6cb51`)** | `#f2f2f2` | `var(--s-color-27b6cb51)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--s-font-c796e0a2` | `'Stack Sans Notch'` | Typography / Scale Token |
| `--s-font-c89837a8` | `'Stack Sans Headline'` | Typography / Scale Token |
| `--s-font-e28f2a0c` | `'Stack Sans Text'` | Typography / Scale Token |
| `--s-font-75b0f13c` | `Italianno` | Typography / Scale Token |
| `--s-font-11bbee0d` | `'Zen Old Mincho'` | Typography / Scale Token |
| `--s-color-34930474` | `#333333ff` | Brand / Palette Token |
| `--s-color-27b6cb51` | `#f2f2f2ff` | Brand / Palette Token |
| `--s-color-c8b6c400` | `#f7f7f7ff` | Brand / Palette Token |
| `--s-color-c69a0a1a` | `rgb(240, 240, 240)` | Brand / Palette Token |
| `--s-color-54b90296` | `linear-gradient(90deg, #ffffffff, #ffffffff)` | Brand / Palette Token |
| `--s-color-eea30069` | `rgba(150, 150, 150, 0)` | Brand / Palette Token |
| `--s-color-e2b900cc` | `#333333` | Brand / Palette Token |
| `--img-current` | `var(--img-small)` | Design System Custom Token |
| `--gap-h` | `0px` | Layout / Spatial Grid Token |
| `--gap-v` | `0px` | Layout / Spatial Grid Token |
| `--ha` | `1` | Design System Custom Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Stack Sans Notch`.
- **Primary Body Stack**: `Italianno`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 3em`, `font-weight: 700`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: 2em`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 16px`, `font-weight: 400`); rule `body` (`line-height: 1`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 36px`, `line-height: 36px`, `font-weight: 400`, `letter-spacing: 0.72px`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.4,0.4,0,1)`, `cubic-bezier(.4,.4,0,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.lenis.lenis-autoToggle`**: `transition: 1ms` extracted from `wedding-s-tmro-com` stylesheet.
- **Selector `body`**: `transition: background 0.5s cubic-bezier(0.4,0.4,0,1)` extracted from `wedding-s-tmro-com` stylesheet.
- **Selector `.video-container`**: `transition: all 0.3s cubic-bezier(0.4,0.4,0,1)` extracted from `wedding-s-tmro-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.4,0.4,0,1)`)**: Governs interactive state transitions across `<header.lenis>` and `<section.section:nth(2)>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Wedding Invitation · Yuri & Tomoro         │
│ ====================================================================== │
│ [ <header.lenis> (1440px)             | @recipe · MESSAGE · INFORMAT ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.section> (w=1440px)                           | │
│ | H1: Wedding Invitation · Yuri & Tomoro                             | │
│ | Substrate: #f7f7f7 | Ink: #000000 | Accent: #333333                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.section:nth(2)>) max-w: 1440px             | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Featured Work & Interactive  |  | Technical Architecture & Nar | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.section:nth(3)>) — Global Directory & Co   | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.section-inne) | https://wedding.s-tmro.com/          │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 40px)       │
│ ====================================================================== │
│ [ HEADER BAR (<header.lenis>          ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.section>) — 390px Vertical Lead               | │
│ | H1: Wedding Invitation · Yuri & Tomoro                             | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.section:nth(2) — 1-Col Stack              | │
│ | [ Item 1: Featured Work & Interactive Showcase                   ] | │
│ | [ Item 2: Technical Architecture & Narrative                     ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.section:nth(3)>) — 1-Col (Global Directory &) │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.section-inne) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.lenis> — `wedding-s-tmro-com`)**:
   - Landmark `<header class="lenis">` (`1440px`) hosting `Wedding Invitation · Yuri & Tomoro` navigation (`@recipe · MESSAGE · INFORMATION · YOUR REPLY · @recipe @recipe`), DOM attributes (`data-appear`, `data-inited-appear`, `data-sd-img-src="https://storage.googl..."`, `data-sd-img-src="https://storage.googl..."`), and stylesheet rule `html.lenis body { height: auto; }`.
2. **Hero Stage & Focal Lead (<section.section> — `Wedding Invitation · Yuri & Tomoro`)**:
   - Landmark `<section class="section">` presenting display lead `Wedding Invitation · Yuri & Tomoro` and copy excerpt *"Yuri Kunimatsu & Tomoro Sugawara Wedding Ceremony"* over `#f7f7f7` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.section:nth(2)> — `Featured Work & Interactive Showca`)**:
   - Landmark `<section class="section">` rendering section `Featured Work & Interactive Showcase` with copy *"“ii-fuku-nohi” & “ii-niku-nohi”"*, asset references (`84a82c89-316b-4152-8b5a-bb944f91e1b1`, `fonts.googleapis.com`, `fonts.gstatic.com`, `css2`), and grid rule `.lenis-stopped { overflow: clip; }`.
4. **Interactive Detail & Feature Matrix (<section.section:nth(3)> — `Technical Architecture & Narrative`)**:
   - Landmark `<section class="section">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"mixture restaurant"*) with `#ffffff` surface cards, `#333333` accents, and `.lenis.lenis-smooth iframe { pointer-events: none; }`.
5. **Colophon & Global Directory Footer (<footer.section-inner> — `https://wedding.s-tmro.com/`)**:
   - Landmark `<footer class="section-inner">` anchoring `Wedding Invitation · Yuri & Tomo` footer links (`@recipe · MESSAGE · INFORMATION · YOUR REPLY · @recipe @recipe`), copy *"Good clothes Good meats Good Fortunes"*, and `#cccccc` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: wedding-s-tmro-com (Wedding Invitation · Yuri & Tomoro)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `wedding-s-tmro-com` (**Wedding Invitation · Yuri & Tomoro** — `https://wedding.s-tmro.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f7f7f7` / `#333333`).
- **Identity & Domain Context**: 結婚式へのご招待です。日時は2026年11月29日（いい肉の日）、10:00に受付、10:30に開始です。会場は桜通線「国際センター」駅近くのレストラン「recipe」です。
- **Primary Substrate**: `#f7f7f7` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#000000`, **Accent / Highlight**: `#333333`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#f7f7f7` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#333333` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Stack Sans Notch` for display copy (`Wedding Invitation · Yuri & Tomoro`) with `Italianno` and not declared in live computed styles (uses primary stack / `ui-monospace`).
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 40px`, padding `10px`) with `cubic-bezier(0.4,0.4,0,1)` easing and Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `wedding-s-tmro-com` in your global stylesheet:

:root {
  /* Wedding Invitation · Yuri & Tomoro (wedding-s-tmro-com) — Live-Grounded CSS Variables */
  --s-font-c796e0a2: 'Stack Sans Notch'; /* Typography / Scale Token (wedding-s-tmro-com) */
  --s-font-c89837a8: 'Stack Sans Headline'; /* Typography / Scale Token (wedding-s-tmro-com) */
  --s-font-e28f2a0c: 'Stack Sans Text'; /* Typography / Scale Token (wedding-s-tmro-com) */
  --s-font-75b0f13c: Italianno; /* Typography / Scale Token (wedding-s-tmro-com) */
  --s-font-11bbee0d: 'Zen Old Mincho'; /* Typography / Scale Token (wedding-s-tmro-com) */
  --s-color-34930474: #333333ff; /* Brand / Palette Token (wedding-s-tmro-com) */
  --s-color-27b6cb51: #f2f2f2ff; /* Brand / Palette Token (wedding-s-tmro-com) */
  --s-color-c8b6c400: #f7f7f7ff; /* Brand / Palette Token (wedding-s-tmro-com) */
  --s-color-c69a0a1a: rgb(240, 240, 240); /* Brand / Palette Token (wedding-s-tmro-com) */
  --s-color-54b90296: linear-gradient(90deg, #ffffffff, #ffffffff); /* Brand / Palette Token (wedding-s-tmro-com) */
  --s-color-eea30069: rgba(150, 150, 150, 0); /* Brand / Palette Token (wedding-s-tmro-com) */
  --s-color-e2b900cc: #333333; /* Brand / Palette Token (wedding-s-tmro-com) */
  --img-current: var(--img-small); /* Design System Custom Token (wedding-s-tmro-com) */
  --gap-h: 0px; /* Layout / Spatial Grid Token (wedding-s-tmro-com) */
  --gap-v: 0px; /* Layout / Spatial Grid Token (wedding-s-tmro-com) */
  --ha: 1; /* Design System Custom Token (wedding-s-tmro-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#f7f7f7` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#000000` — grounded in live computed `body` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#ffffff` — grounded in `body { background: #ffffff }`
- **Interactive Accent / Highlight**: `#333333` — grounded in live computed `a` `color` (`computed_styles.json`)
- **Secondary / Muted Copy**: `#333333` — grounded in live computed `p` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#cccccc` — grounded in `hr { border-top: #cccccc }`
- **Variable Token (`--s-color-27b6cb51`)**: `#f2f2f2` — grounded in `var(--s-color-27b6cb51)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (clamped at 2400px live multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport)
- **Padding & Gutters**: `10px` lateral canvas padding with `40px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 40px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `10px` horizontal padding
- **Media Queries**: `@media (prefers-reduced-motion: reduce)`, `@media (min-resolution: 1.5dppx)`, `@media (min-resolution: 1dppx) and (max-resolution: 1.5dppx)`, `@media (max-resolution: 1dppx)`
- **Corner Radii**: `2px`, `6px`, `8px`, `0px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Stack Sans Notch`
- **Body Font Stack**: `Italianno`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: rule `h1` (`font-size: 3em`, `font-weight: 700`)
- **H2 Section Rule**: rule `h2` (`font-size: 2em`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 16px`, `font-weight: 400`); rule `body` (`line-height: 1`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 36px`, `line-height: 36px`, `font-weight: 400`, `letter-spacing: 0.72px`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `wedding-s-tmro-com` (`Wedding Invitation · Yuri & Tomoro`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.lenis> — `wedding-s-tmro-com`)**:
   - DOM & Selectors: Landmark `<header class="lenis">` (`1440px`) hosting `Wedding Invitation · Yuri & Tomoro` navigation (`@recipe · MESSAGE · INFORMATION · YOUR REPLY · @recipe @recipe`), DOM attributes (`data-appear`, `data-inited-appear`, `data-sd-img-src="https://storage.googl..."`, `data-sd-img-src="https://storage.googl..."`), and stylesheet rule `html.lenis body { height: auto; }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.lenis> — `wedding-s-tmro-com`)` (`wedding-s-tmro-com`) adapts across `@media (prefers-reduced-motion: reduce)`, `@media (min-resolution: 1.5dppx)`, `@media (min-resolution: 1dppx) and (max-resolution: 1.5dppx)`, `@media (max-resolution: 1dppx)` with `cubic-bezier(0.4,0.4,0,1)`, `cubic-bezier(.4,.4,0,1)` transitions and links `@recipe · MESSAGE · INFORMATION · YOUR REPLY · @recipe @recipe`.
2. **Hero Stage & Focal Lead (<section.section> — `Wedding Invitation · Yuri & Tomoro`)**:
   - DOM & Selectors: Landmark `<section class="section">` presenting display lead `Wedding Invitation · Yuri & Tomoro` and copy excerpt *"Yuri Kunimatsu & Tomoro Sugawara Wedding Ceremony"* over `#f7f7f7` canvas and `#000000` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#f7f7f7` background with `#000000` headline `Wedding Invitation · Yuri & Tomoro`.
3. **Primary Showcase & Content Grid (<section.section:nth(2)> — `Featured Work & Interactive Showca`)**:
   - DOM & Selectors: Landmark `<section class="section">` rendering section `Featured Work & Interactive Showcase` with copy *"“ii-fuku-nohi” & “ii-niku-nohi”"*, asset references (`84a82c89-316b-4152-8b5a-bb944f91e1b1`, `fonts.googleapis.com`, `fonts.gstatic.com`, `css2`), and grid rule `.lenis-stopped { overflow: clip; }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.section:nth(2)> — `Featured Work & Interactive Showca`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 40px`) on desktop and Single-column vertical stack at `390px` viewport width with `10px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.section:nth(3)> — `Technical Architecture & Narrative`)**:
   - DOM & Selectors: Landmark `<section class="section">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"mixture restaurant"*) with `#ffffff` surface cards, `#333333` accents, and `.lenis.lenis-smooth iframe { pointer-events: none; }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.section:nth(3)> — `Technical Architecture & Narrative`)` uses `2px`, `6px`, `8px`, `0px` radii, `#333333` highlights, and assets (84a82c89-316b-4152-8b5a-bb944f91e1b1, fonts.googleapis.com, fonts.gstatic.com).
5. **Colophon & Global Directory Footer (<footer.section-inner> — `https://wedding.s-tmro.com/`)**:
   - DOM & Selectors: Landmark `<footer class="section-inner">` anchoring `Wedding Invitation · Yuri & Tomo` footer links (`@recipe · MESSAGE · INFORMATION · YOUR REPLY · @recipe @recipe`), copy *"Good clothes Good meats Good Fortunes"*, and `#cccccc` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.section-inner> — `https://wedding.s-tmro.com/`)` aligns to `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport) with `10px` lateral canvas padding with `40px` grid gap and attributes (data-appear, data-inited-appear, data-sd-img-src="https://storage.googl...").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Yuri Kunimatsu & Tomoro Sugawara Wedding Ceremony"*
- Copy Excerpt 2: *"“ii-fuku-nohi” & “ii-niku-nohi”"*
- Copy Excerpt 3: *"mixture restaurant"*
- Copy Excerpt 4: *"Good clothes Good meats Good Fortunes"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.4,0.4,0,1)`, `cubic-bezier(.4,.4,0,1)`
- **Extracted Stylesheet Rules (`wedding-s-tmro-com`)**:
- `html.lenis body { height: auto; }`
- `.lenis-stopped { overflow: clip; }`
- `.lenis.lenis-smooth iframe { pointer-events: none; }`
- `.lenis.lenis-autoToggle { transition-property: overflow; transition-duration: 1ms; transition-beha... }`
- `html { height: 100%; padding: 0; margin: 0; scroll-behavior: smooth; -webkit-fo... }`
- **Per-Selector Transition Rules**:
- **Selector `.lenis.lenis-autoToggle`**: `transition: 1ms` extracted from `wedding-s-tmro-com` stylesheet.
- **Selector `body`**: `transition: background 0.5s cubic-bezier(0.4,0.4,0,1)` extracted from `wedding-s-tmro-com` stylesheet.
- **Selector `.video-container`**: `transition: all 0.3s cubic-bezier(0.4,0.4,0,1)` extracted from `wedding-s-tmro-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.4,0.4,0,1)`)**: Governs interactive state transitions across `<header.lenis>` and `<section.section:nth(2)>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `wedding-s-tmro-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
