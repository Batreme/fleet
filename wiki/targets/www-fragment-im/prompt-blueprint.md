---
title: "UI Prompt Blueprint: www-fragment-im"
date: 2026-11-23
captured_at: 2026-11-23
target: "www-fragment-im"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "High-Contrast Obsidian / Atmospheric Design System (`#000000` canvas, `#c9d0d2` ink, `#0000ee` accent)"
---

# UI Design System & Master Generation Blueprint: www-fragment-im

> **Fragment Studio · Independent Designer for Visual Identity, Websites & P...** (https://www.fragment.im) — Independent multidisciplinary designer creating visual identities, websites and digital product experiences, from creative direction thro...

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Fragment Studio · Independent Designer for Visual Identity, Websites & P...** (`https://www.fragment.im`). Independent multidisciplinary designer creating visual identities, websites and digital product experiences, from creative direction thro...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **High-Contrast Obsidian / Atmospheric Design System (`#000000` canvas, `#c9d0d2` ink, `#0000ee` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#000000` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#c9d0d2` primary typography and `#0000ee` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Stack Sans Headline` for display copy (`One designer. Clear direction. Compl`) with `Fragment Mono` and `Fragment Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `1329px` container bounds (`gap: 48px`, padding `48px`) with `cubic-bezier(.25,0,0,1)` easing and Framer Motion Layout Physics.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, clamped at 2400px live multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `1329px` (measured widest bounded `<section>` landmark width on `1440px` desktop).
- **Canvas Lateral Padding & Spacing**: `48px` lateral canvas padding with `48px` grid gap.
- **Border Radius Scale**: `6px`, `8px`, `15px`, `0px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1329px`, `gap: 48px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `48px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width: 809px)`, `@media (max-width:809px)`, `@media (min-width: 1600px)`, `@media (min-width: 1200px) and (max-width: 1599.98px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#c9d0d2` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#000000` | transparent/inherited card surface over live computed `body` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#0000ee` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#0000ee` | live computed `a` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#c9d0d2` | `var(--border-color)` in `:root` (`var(--token-25c6a125-c456-4a8b-ab...`) |
| **Variable Token (`--token-fe4a4709-d130-45cb-b56c-f30ed01b9abe`)** | `#8d9496` | `var(--token-fe4a4709-d130-45cb-b56c-f30ed01b9abe)` in `:root` |
| **Variable Token (`--token-a95c7b0f-3d02-4bfd-a1a4-044fa7647703`)** | `#ffffff` | `var(--token-a95c7b0f-3d02-4bfd-a1a4-044fa7647703)` in `:root` |
| **Variable Token (`--token-d3018533-ccc9-45bc-9cdd-b1ac632fea09`)** | `#121516` | `var(--token-d3018533-ccc9-45bc-9cdd-b1ac632fea09)` in `:root` |
| **Variable Token (`--token-7114c3e6-2498-4350-a884-eb0ae0ab8a2a`)** | `#141515` | `var(--token-7114c3e6-2498-4350-a884-eb0ae0ab8a2a)` in `:root` |
| **Variable Token (`--token-095b07f5-0eeb-4dec-b4e4-b400a5a02e21`)** | `#687679` | `var(--token-095b07f5-0eeb-4dec-b4e4-b400a5a02e21)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--token-25c6a125-c456-4a8b-ab9f-41881ab19959` | `#c9d0d2` | Color / Atmospheric Token |
| `--token-89b67f64-c980-4093-a59b-826aca646ff7` | `#000` | Color / Atmospheric Token |
| `--token-f73340a2-29c6-4e1e-9122-76db6b3c3c9b` | `#c9d0d252` | Color / Atmospheric Token |
| `--token-fe4a4709-d130-45cb-b56c-f30ed01b9abe` | `#8d9496` | Color / Atmospheric Token |
| `--token-a95c7b0f-3d02-4bfd-a1a4-044fa7647703` | `#fff` | Color / Atmospheric Token |
| `--token-d3018533-ccc9-45bc-9cdd-b1ac632fea09` | `#121516` | Color / Atmospheric Token |
| `--token-7114c3e6-2498-4350-a884-eb0ae0ab8a2a` | `#14151529` | Color / Atmospheric Token |
| `--token-095b07f5-0eeb-4dec-b4e4-b400a5a02e21` | `#687679` | Color / Atmospheric Token |
| `--text-decoration-skip-ink` | `var(--framer-text-decoration-skip-ink)` | Typography Ink Token |
| `--text-underline-offset` | `var(--framer-text-decoration-offset)` | Typography Ink Token |
| `--font-family` | `var(--framer-font-family)` | Typography / Scale Token |
| `--font-style` | `var(--framer-font-style)` | Typography / Scale Token |
| `--font-weight` | `var(--framer-font-weight)` | Typography / Scale Token |
| `--text-color` | `var(--framer-text-color)` | Typography Ink Token |
| `--letter-spacing` | `var(--framer-letter-spacing)` | Typography / Scale Token |
| `--font-size` | `var(--framer-font-size)` | Typography / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Stack Sans Headline`.
- **Primary Body Stack**: `Fragment Mono`.
- **Technical / Metadata Stack**: `Fragment Mono`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 63px`, `line-height: 69.3px`, `font-weight: 200`); rule `h1` (`font-size: 44px`, `line-height: 1.1`, `letter-spacing: 0`, `font-weight: 200`).
- **Section Heading (`H2`)**: live computed `h3 (primary section heading)` (`font-size: 48.96px`, `line-height: 53.856px`, `font-weight: 200`).
- **Body Copy**: live computed `body` (`font-size: 12px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: 20px`, `line-height: 1.6`, `font-weight: 300`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 12px`, `line-height: normal`, `font-weight: 400`); CSS variables `--letter-spacing: var(--framer-letter-spacing)`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.25,0,0,1)`, `cubic-bezier(0.25,0,0,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `r-styles-preset-16vh2rd.rich-text...`**: `transition: color .4s cubic-bezier(.25,0,0,1)` extracted from `www-fragment-im` stylesheet.
- **Selector `er-styles-preset-hkk4oc.rich-text...`**: `transition: color .4s cubic-bezier(.25,0,0,1)` extracted from `www-fragment-im` stylesheet.
- **Selector `#__framer-editorbar-label`**: `transition: opacity 0.4s ease-out` extracted from `www-fragment-im` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.25,0,0,1)`)**: Governs interactive state transitions across `<nav.framer-tR7CP>` and `<section.framer-17uuuhg>`.
- **Runtime Interaction Engine**: Integrates Framer Motion Layout Physics with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Fragment Studio · Independent Designer for │
│ ====================================================================== │
│ [ <nav.framer-tR7CP> (1425x82px)      | Home Home · Work Work · Abou ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.framer-7o1u1h> (w=1425px)                     | │
│ | H1: One designer. Clear direction. Complete execution.             | │
│ | Substrate: #000000 | Ink: #c9d0d2 | Accent: #0000ee                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.framer-17uuuhg>) max-w: 1329px             | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Brand Identity               |  | Product Design               | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.framer-H4KuY>) — Bold brand and web de     | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.framer-V3ncb) | https://www.fragment.im              │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 48px)       │
│ ====================================================================== │
│ [ HEADER BAR (<nav.framer-tR7CP>      ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.framer-7o1u1h>) — 390px Vertical Lead         | │
│ | H1: One designer. Clear direction. Complete execution.             | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.framer-17uuuh) — 1-Col Stack              | │
│ | [ Item 1: Brand Identity                                         ] | │
│ | [ Item 2: Product Design                                         ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.framer-H4KuY>) — 1-Col (Bold brand and web) | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.framer-V3ncb) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.framer-tR7CP> — `www-fragment-im`)**:
   - Landmark `<nav class="framer-tR7CP framer-W48R1">` (`1425x82px`) hosting `Fragment Studio · Independent Design` navigation (`Home Home · Work Work · About About · Contact Contact · EN PL`), DOM attributes (`data-redirect-timezone="1"`, `data-framer-generated-canonical`, `data-framer-font-css`, `data-framer-breakpoint-css`), and stylesheet rule `focus-visible { outline: 2px solid 757575; outline-offset: 6px; border-radius: 6px; }`.
2. **Hero Stage & Focal Lead (<section.framer-7o1u1h> — `One designer. Clear direction. Com`)**:
   - Landmark `<section class="framer-7o1u1h mobile-hero">` presenting display lead `One designer. Clear direction. Complete execution.` and copy excerpt *"Consistent creative direction for brands across visual identity, "* over `#000000` canvas and `#c9d0d2` ink.
3. **Primary Showcase & Content Grid (<section.framer-17uuuhg> — `Brand Identity`)**:
   - Landmark `<section class="framer-17uuuhg">` rendering section `Brand Identity` with copy *"I’m a freelance multidisciplinary designer with 15 years of exper"*, asset references (`p1FP15nWl4LPFrB978NFoMKhMrE.png`, `GoVnPOGObUh1MO9i6ATNEe6r2g.png`, `3hSn8XTXecIOBHOo2uSnD8XPSc.png`, `fonts.gstatic.com`), and grid rule `.mobile-hero { height: 100svh !important; min-height: 100svh !important; }`.
4. **Interactive Detail & Feature Matrix (<section.framer-H4KuY> — `Product Design`)**:
   - Landmark `<section class="framer-H4KuY framer-tMFtv">` framing `Product Design` and `Bold brand and web design for science-driven asse...` (*"Features & recognitions"*) with `#000000` surface cards, `#0000ee` accents, and `html { scrollbar-gutter: stable; }`.
5. **Colophon & Global Directory Footer (<footer.framer-V3ncb> — `https://www.fragment.im`)**:
   - Landmark `<footer class="framer-V3ncb framer-QbbfG">` anchoring `Fragment Studio · Independent De` footer links (`Home Home · Work Work · About About · Contact Contact · EN PL`), copy *"Brands designed for, and counting…"*, and `#c9d0d2` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-fragment-im (Fragment Studio · Independent Designer for Visual Identity, Websites & P...)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-fragment-im` (**Fragment Studio · Independent Designer for Visual Identity, Websites & P...** — `https://www.fragment.im`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000000` canvas, `#c9d0d2` ink, `#0000ee` accent).
- **Identity & Domain Context**: Independent multidisciplinary designer creating visual identities, websites and digital product experiences, from creative direction thro...
- **Primary Substrate**: `#000000` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#c9d0d2`, **Accent / Highlight**: `#0000ee`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#000000` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#c9d0d2` primary typography and `#0000ee` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Stack Sans Headline` for display copy (`One designer. Clear direction. Compl`) with `Fragment Mono` and `Fragment Mono`.
  - **Calibrated Spatial Grid & Motion**: Combines `1329px` container bounds (`gap: 48px`, padding `48px`) with `cubic-bezier(.25,0,0,1)` easing and Framer Motion Layout Physics.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-fragment-im` in your global stylesheet:

:root {
  /* Fragment Studio · Independent Designer for Visual Identity, Websites & P... (www-fragment-im) — Live-Grounded CSS Variables */
  --token-25c6a125-c456-4a8b-ab9f-41881ab19959: #c9d0d2; /* Color / Atmospheric Token (www-fragment-im) */
  --token-89b67f64-c980-4093-a59b-826aca646ff7: #000; /* Color / Atmospheric Token (www-fragment-im) */
  --token-f73340a2-29c6-4e1e-9122-76db6b3c3c9b: #c9d0d252; /* Color / Atmospheric Token (www-fragment-im) */
  --token-fe4a4709-d130-45cb-b56c-f30ed01b9abe: #8d9496; /* Color / Atmospheric Token (www-fragment-im) */
  --token-a95c7b0f-3d02-4bfd-a1a4-044fa7647703: #fff; /* Color / Atmospheric Token (www-fragment-im) */
  --token-d3018533-ccc9-45bc-9cdd-b1ac632fea09: #121516; /* Color / Atmospheric Token (www-fragment-im) */
  --token-7114c3e6-2498-4350-a884-eb0ae0ab8a2a: #14151529; /* Color / Atmospheric Token (www-fragment-im) */
  --token-095b07f5-0eeb-4dec-b4e4-b400a5a02e21: #687679; /* Color / Atmospheric Token (www-fragment-im) */
  --text-decoration-skip-ink: var(--framer-text-decoration-skip-ink); /* Typography Ink Token (www-fragment-im) */
  --text-underline-offset: var(--framer-text-decoration-offset); /* Typography Ink Token (www-fragment-im) */
  --font-family: var(--framer-font-family); /* Typography / Scale Token (www-fragment-im) */
  --font-style: var(--framer-font-style); /* Typography / Scale Token (www-fragment-im) */
  --font-weight: var(--framer-font-weight); /* Typography / Scale Token (www-fragment-im) */
  --text-color: var(--framer-text-color); /* Typography Ink Token (www-fragment-im) */
  --letter-spacing: var(--framer-letter-spacing); /* Typography / Scale Token (www-fragment-im) */
  --font-size: var(--framer-font-size); /* Typography / Scale Token (www-fragment-im) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#000000` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#c9d0d2` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#000000` — grounded in transparent/inherited card surface over live computed `body` `background-color` (`computed_styles.json`)
- **Interactive Accent / Highlight**: `#0000ee` — grounded in live computed `a` `color` (`computed_styles.json`)
- **Secondary / Muted Copy**: `#0000ee` — grounded in live computed `a` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#c9d0d2` — grounded in `var(--border-color)` in `:root` (`var(--token-25c6a125-c456-4a8b-ab...`)
- **Variable Token (`--token-fe4a4709-d130-45cb-b56c-f30ed01b9abe`)**: `#8d9496` — grounded in `var(--token-fe4a4709-d130-45cb-b56c-f30ed01b9abe)` in `:root`
- **Variable Token (`--token-a95c7b0f-3d02-4bfd-a1a4-044fa7647703`)**: `#ffffff` — grounded in `var(--token-a95c7b0f-3d02-4bfd-a1a4-044fa7647703)` in `:root`
- **Variable Token (`--token-d3018533-ccc9-45bc-9cdd-b1ac632fea09`)**: `#121516` — grounded in `var(--token-d3018533-ccc9-45bc-9cdd-b1ac632fea09)` in `:root`
- **Variable Token (`--token-7114c3e6-2498-4350-a884-eb0ae0ab8a2a`)**: `#141515` — grounded in `var(--token-7114c3e6-2498-4350-a884-eb0ae0ab8a2a)` in `:root`
- **Variable Token (`--token-095b07f5-0eeb-4dec-b4e4-b400a5a02e21`)**: `#687679` — grounded in `var(--token-095b07f5-0eeb-4dec-b4e4-b400a5a02e21)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (clamped at 2400px live multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1329px` (measured widest bounded `<section>` landmark width on `1440px` desktop)
- **Padding & Gutters**: `48px` lateral canvas padding with `48px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1329px`, `gap: 48px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `48px` horizontal padding
- **Media Queries**: `@media (max-width: 809px)`, `@media (max-width:809px)`, `@media (min-width: 1600px)`, `@media (min-width: 1200px) and (max-width: 1599.98px)`
- **Corner Radii**: `6px`, `8px`, `15px`, `0px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Stack Sans Headline`
- **Body Font Stack**: `Fragment Mono`
- **Monospace / Technical Font Stack**: `Fragment Mono`
- **H1 Display Rule**: live computed `h1` (`font-size: 63px`, `line-height: 69.3px`, `font-weight: 200`); rule `h1` (`font-size: 44px`, `line-height: 1.1`, `letter-spacing: 0`, `font-weight: 200`)
- **H2 Section Rule**: live computed `h3 (primary section heading)` (`font-size: 48.96px`, `line-height: 53.856px`, `font-weight: 200`)
- **Body Copy Rule**: live computed `body` (`font-size: 12px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: 20px`, `line-height: 1.6`, `font-weight: 300`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 12px`, `line-height: normal`, `font-weight: 400`); CSS variables `--letter-spacing: var(--framer-letter-spacing)`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-fragment-im` (`Fragment Studio · Independent Designer for Visual Identity, Websites & P...`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.framer-tR7CP> — `www-fragment-im`)**:
   - DOM & Selectors: Landmark `<nav class="framer-tR7CP framer-W48R1">` (`1425x82px`) hosting `Fragment Studio · Independent Design` navigation (`Home Home · Work Work · About About · Contact Contact · EN PL`), DOM attributes (`data-redirect-timezone="1"`, `data-framer-generated-canonical`, `data-framer-font-css`, `data-framer-breakpoint-css`), and stylesheet rule `focus-visible { outline: 2px solid 757575; outline-offset: 6px; border-radius: 6px; }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.framer-tR7CP> — `www-fragment-im`)` (`www-fragment-im`) adapts across `@media (max-width: 809px)`, `@media (max-width:809px)`, `@media (min-width: 1600px)`, `@media (min-width: 1200px) and (max-width: 1599.98px)` with `cubic-bezier(.25,0,0,1)`, `cubic-bezier(0.25,0,0,1)` transitions and links `Home Home · Work Work · About About · Contact Contact · EN PL`.
2. **Hero Stage & Focal Lead (<section.framer-7o1u1h> — `One designer. Clear direction. Com`)**:
   - DOM & Selectors: Landmark `<section class="framer-7o1u1h mobile-hero">` presenting display lead `One designer. Clear direction. Complete execution.` and copy excerpt *"Consistent creative direction for brands across visual identity, "* over `#000000` canvas and `#c9d0d2` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#000000` background with `#c9d0d2` headline `One designer. Clear direction. Complete execution.`.
3. **Primary Showcase & Content Grid (<section.framer-17uuuhg> — `Brand Identity`)**:
   - DOM & Selectors: Landmark `<section class="framer-17uuuhg">` rendering section `Brand Identity` with copy *"I’m a freelance multidisciplinary designer with 15 years of exper"*, asset references (`p1FP15nWl4LPFrB978NFoMKhMrE.png`, `GoVnPOGObUh1MO9i6ATNEe6r2g.png`, `3hSn8XTXecIOBHOo2uSnD8XPSc.png`, `fonts.gstatic.com`), and grid rule `.mobile-hero { height: 100svh !important; min-height: 100svh !important; }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.framer-17uuuhg> — `Brand Identity`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1329px`, `gap: 48px`) on desktop and Single-column vertical stack at `390px` viewport width with `48px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.framer-H4KuY> — `Product Design`)**:
   - DOM & Selectors: Landmark `<section class="framer-H4KuY framer-tMFtv">` framing `Product Design` and `Bold brand and web design for science-driven asse...` (*"Features & recognitions"*) with `#000000` surface cards, `#0000ee` accents, and `html { scrollbar-gutter: stable; }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.framer-H4KuY> — `Product Design`)` uses `6px`, `8px`, `15px`, `0px` radii, `#0000ee` highlights, and assets (p1FP15nWl4LPFrB978NFoMKhMrE.png, GoVnPOGObUh1MO9i6ATNEe6r2g.png, 3hSn8XTXecIOBHOo2uSnD8XPSc.png).
5. **Colophon & Global Directory Footer (<footer.framer-V3ncb> — `https://www.fragment.im`)**:
   - DOM & Selectors: Landmark `<footer class="framer-V3ncb framer-QbbfG">` anchoring `Fragment Studio · Independent De` footer links (`Home Home · Work Work · About About · Contact Contact · EN PL`), copy *"Brands designed for, and counting…"*, and `#c9d0d2` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.framer-V3ncb> — `https://www.fragment.im`)` aligns to `1329px` (measured widest bounded `<section>` landmark width on `1440px` desktop) with `48px` lateral canvas padding with `48px` grid gap and attributes (data-redirect-timezone="1", data-framer-generated-canonical, data-framer-font-css).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"Consistent creative direction for brands across visual identity, websites and digi..."*
- Copy Excerpt 2: *"I’m a freelance multidisciplinary designer with 15 years of experience helping sta..."*
- Copy Excerpt 3: *"Features & recognitions"*
- Copy Excerpt 4: *"Brands designed for, and counting…"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.25,0,0,1)`, `cubic-bezier(0.25,0,0,1)`
- **Extracted Stylesheet Rules (`www-fragment-im`)**:
- `focus-visible { outline: 2px solid 757575; outline-offset: 6px; border-radius: 6px; }`
- `.mobile-hero { height: 100svh !important; min-height: 100svh !important; }`
- `html { scrollbar-gutter: stable; }`
- `html.fragment-loader-active::after { animation: fragment-loader-emergency-hide 1ms step-end 5s forwards !impo... }`
- `to { visibility: hidden; pointer-events: none; }`
- **Per-Selector Transition Rules**:
- **Selector `r-styles-preset-16vh2rd.rich-text...`**: `transition: color .4s cubic-bezier(.25,0,0,1)` extracted from `www-fragment-im` stylesheet.
- **Selector `er-styles-preset-hkk4oc.rich-text...`**: `transition: color .4s cubic-bezier(.25,0,0,1)` extracted from `www-fragment-im` stylesheet.
- **Selector `#__framer-editorbar-label`**: `transition: opacity 0.4s ease-out` extracted from `www-fragment-im` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.25,0,0,1)`)**: Governs interactive state transitions across `<nav.framer-tR7CP>` and `<section.framer-17uuuhg>`.
- **Runtime Interaction Engine**: Integrates Framer Motion Layout Physics with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-fragment-im`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
