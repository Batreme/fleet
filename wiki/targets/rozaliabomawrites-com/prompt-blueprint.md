---
title: "UI Prompt Blueprint: rozaliabomawrites-com"
date: 2026-11-24
captured_at: 2026-11-24
target: "rozaliabomawrites-com"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
capture_mode: behavioral_journey_v2
asset_format: webp
scroll_driver: native
desktop_keyframes: 8
subpages_crawled: 3
http_status: 200
archetype: "Light-Gallery WebGL / Canvas Interactive Experience (`#f5dafb` / `#ffcc00`)"
---

# UI Design System & Master Generation Blueprint: rozaliabomawrites-com

> **Rozalia Boma — Multicultural Romance Author** (https://rozaliabomawrites.com/) — Official site of Rozalia Boma, author of multicultural YA romance. Books, diary entries, guestbook and newsletter.

![Desktop Journey Filmstrip (1280x6624)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x2616)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Rozalia Boma — Multicultural Romance Author** (`https://rozaliabomawrites.com/`). Official site of Rozalia Boma, author of multicultural YA romance. Books, diary entries, guestbook and newsletter.
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **Light-Gallery WebGL / Canvas Interactive Experience (`#f5dafb` / `#ffcc00`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#f5dafb` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#491237` primary typography and `#ffcc00` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Knewave` for display copy (`Rozalia Boma — writing multicultural`) with `Plus Jakarta Sans`.
  - **Calibrated Spatial Grid & Motion**: Combines `1368px` container bounds (`gap: .5rem`, padding `2rem`) with `cubic-bezier(.4,0,.6,1)` easing and Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface.

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×6624px` (`assets/desktop-journey.webp`, `8` keyframes up to `y=5129px` / doc `6121px`), Mobile `390×2616px` (`assets/mobile-journey.webp`, `3` keyframes).
- **Master Container Bounds**: `1368px` (measured widest bounded `<section>` landmark width on `1440px` desktop).
- **Canvas Lateral Padding & Spacing**: `2rem` lateral canvas padding with `.5rem` grid gap.
- **Border Radius Scale**: `var(--radius)`, `999px`, `14px`, `8px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1368px`, `gap: .5rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `2rem` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width: 640px)`, `@media (min-width: 1400px)`, `@media (min-width: 640px)`, `@media (min-width: 768px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f5dafb` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#491237` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `var(--normal-bg)` in `:root` |
| **Interactive Accent / Highlight** | `#ffcc00` | `crubber-button.ytp-swatch-backg... { background-color: #ffcc00 }` |
| **Secondary / Muted Copy** | `#fa3899` | live computed `h2` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#e5e7eb` | `:after { border-color: #e5e7eb }` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--background` | `290 80% 92%` | Canvas / Surface Token |
| `--foreground` | `320 60% 18%` | Typography Ink Token |
| `--card` | `0 0% 100%` | Dimension / Scale Token |
| `--card-foreground` | `320 60% 18%` | Typography Ink Token |
| `--popover` | `0 0% 100%` | Dimension / Scale Token |
| `--popover-foreground` | `320 60% 18%` | Typography Ink Token |
| `--primary` | `330 95% 60%` | Brand / Palette Token |
| `--primary-foreground` | `0 0% 100%` | Typography Ink Token |
| `--secondary` | `280 85% 78%` | Brand / Palette Token |
| `--secondary-foreground` | `320 60% 18%` | Typography Ink Token |
| `--muted` | `320 60% 95%` | Dimension / Scale Token |
| `--muted-foreground` | `320 25% 45%` | Typography Ink Token |
| `--accent` | `195 90% 75%` | Brand / Palette Token |
| `--accent-foreground` | `320 60% 18%` | Typography Ink Token |
| `--destructive` | `0 84% 60%` | Dimension / Scale Token |
| `--destructive-foreground` | `0 0% 100%` | Typography Ink Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Knewave`.
- **Primary Body Stack**: `Plus Jakarta Sans`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 96px`, `line-height: 96px`, `font-weight: 400`, `letter-spacing: -1.92px`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 93.9404px`, `line-height: 89.2434px`, `font-weight: 400`, `letter-spacing: 0.939404px`); rule `h2` (`letter-spacing: -.02em`, `font-weight: 400`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); rule `p` (`line-height: 1.65`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(0,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.btn-bubble`**: `transition: transform .12s ease,box-shadow .12s ease` extracted from `rozaliabomawrites-com` stylesheet.
- **Selector `.win98-btn`**: `transition: none` extracted from `rozaliabomawrites-com` stylesheet.
- **Selector `.y2k-textbox`**: `transition: transform .35s ease,box-shadow .35s ease` extracted from `rozaliabomawrites-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.6,1)`)**: Governs interactive state transitions across `<nav.top-0>` and `<section.overflow-x-clip>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `native` (max document height `6121px`, deepest scrollY reached `5129px` across `8` desktop keyframes).
- **Detected Scroll / Motion Libraries**: `Lenis`, `WebGL/Canvas`.
- **Interactive Control Probe (`carousel_next`)**: Tested `Next` (diff `1.689`).
- **Route Transition Architecture**: First internal navigation (`/blog`) measured as `direct` in `2852ms`.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Rozalia Boma — Multicultural Romance Autho │
│ ====================================================================== │
│ [ <nav.top-0> (1440x68px)             | Home · Author · Books · Blog ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.fixed> (w=1440px)                             | │
│ | H1: Rozalia Boma — writing multicultural romances                  | │
│ | Substrate: #f5dafb | Ink: #491237 | Accent: #ffcc00                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.overflow-x-clip>) max-w: 1368px            | │
│ | +------------------------------+  +------------------------------+ | │
│ | | ROZALIA BOMA WRITES IS LOADI |  | Rozalia Boma Writes is loadi | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.py-24>) — Beware! Black Eastern            | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.mt-8>       ) | https://rozaliabomawrites.com/       │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: .5rem)      │
│ ====================================================================== │
│ [ HEADER BAR (<nav.top-0>             ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.fixed>) — 390px Vertical Lead                 | │
│ | H1: Rozalia Boma — writing multicultural romances                  | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.overflow-x-cl) — 1-Col Stack              | │
│ | [ Item 1: ROZALIA BOMA WRITES IS LOADING                         ] | │
│ | [ Item 2: Rozalia Boma Writes is loading                         ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.py-24>) — 1-Col (Beware! Black East)        | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.mt-8>       ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<nav.top-0> — `rozaliabomawrites-com`)**:
   - Landmark `<nav class="top-0 left-0">` (`1440x68px`) hosting `Rozalia Boma — Multicultural Romance` navigation (`Home · Author · Books · Blog · Guestbook`), DOM attributes (`data-artifact-kind="dwl_content_hash"`, `data-artifact-id="db5c4db312500dfaed9e3..."`, `data-commit-sha="37366776bd44c18a989e4..."`, `data-context-token="v1.eyJwcm9qZWN0X2lkIj..."`), and stylesheet rule `after { box-sizing:border-box;border-width:0;border-style:solid;border-color:e5e7eb }`.
2. **Hero Stage & Focal Lead (<section.fixed> — `Rozalia Boma — writing multicultur`)**:
   - Landmark `<section class="fixed">` presenting display lead `Rozalia Boma — writing multicultural romances` and copy excerpt *"ROZALIA BOMA WRITES IS LOADING"* over `#f5dafb` canvas and `#491237` ink.
3. **Primary Showcase & Content Grid (<section.overflow-x-clip> — `ROZALIA BOMA WRITES IS LOADING`)**:
   - Landmark `<section class="overflow-x-clip overflow-y-visible">` rendering section `ROZALIA BOMA WRITES IS LOADING` with copy *"Rozalia Boma Writes is loading"*, asset references (`holo-sky-bg-C4iYYOxV.webp`, `fonts.googleapis.com`, `fonts.gstatic.com`, `sykz-yx0lLcxQaSIhS23-w.woff2`), and grid rule `body { margin:0;line-height:inherit }`.
4. **Interactive Detail & Feature Matrix (<section.py-24> — `Rozalia Boma Writes is loading`)**:
   - Landmark `<section class="py-24 relative">` framing `Rozalia Boma Writes is loading` and `Beware! Black Eastern European baddies on the ri` (*"Beware! Black Eastern European baddies on the rise!"*) with `#ffffff` surface cards, `#ffcc00` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.mt-8> — `https://rozaliabomawrites.com/`)**:
   - Landmark `<footer class="mt-8 relative">` anchoring `Rozalia Boma — Multicultural Rom` footer links (`Home · Author · Books · Blog · Guestbook`), copy *"w r i t i n g m u l t i c u l t u r a l"*, and `#e5e7eb` structural dividers.
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=0px`, `0%`): Active landmark `writing multicultural romances` · sticky/fixed elements: `4`
- **Step 02** (`y=850px`, `16%`): Active landmark `WE USE COOKIES` · sticky/fixed elements: `5`
- **Step 03** (`y=1700px`, `33%`): Active landmark `Hi! I'm Rozalia Boma.` · sticky/fixed elements: `5`
- **Step 04** (`y=2550px`, `49%`): Active landmark `The Book` · sticky/fixed elements: `5`
- **Step 05** (`y=3400px`, `66%`): Active landmark `WE USE COOKIES` · sticky/fixed elements: `5`
- **Step 06** (`y=4250px`, `82%`): Active landmark `GIRL, LET ME INTERVIEW MYSELF FOR YOU` · sticky/fixed elements: `5`
- **Step 07** (`y=5100px`, `99%`): Active landmark `Sign up to the newsletter` · sticky/fixed elements: `5`
- **Step 08** (`y=5129px`, `100%`): Active landmark `Sign up to the newsletter` · sticky/fixed elements: `5`

### Multi-Page Internal Route Map
- **Listing Route (`/blog`)**: `https://rozaliabomawrites.com/blog` — H1: `Blog`, scrollHeight `1714px`, transition `direct` (`2852ms`)
- **About Route (`/about`)**: `https://rozaliabomawrites.com/about` — H1: `About`, scrollHeight `1958px`, transition `direct` (`446ms`)
- **About Route (`/contact`)**: `https://rozaliabomawrites.com/contact` — H1: `Contact`, scrollHeight `1592px`, transition `direct` (`822ms`)

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: rozaliabomawrites-com (Rozalia Boma — Multicultural Romance Author)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `rozaliabomawrites-com` (**Rozalia Boma — Multicultural Romance Author** — `https://rozaliabomawrites.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f5dafb` / `#ffcc00`).
- **Identity & Domain Context**: Official site of Rozalia Boma, author of multicultural YA romance. Books, diary entries, guestbook and newsletter.
- **Primary Substrate**: `#f5dafb` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#491237`, **Accent / Highlight**: `#ffcc00`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#f5dafb` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#491237` primary typography and `#ffcc00` accents.
  - **Grounded Typographic Hierarchy**: Pairs `Knewave` for display copy (`Rozalia Boma — writing multicultural`) with `Plus Jakarta Sans`.
  - **Calibrated Spatial Grid & Motion**: Combines `1368px` container bounds (`gap: .5rem`, padding `2rem`) with `cubic-bezier(.4,0,.6,1)` easing and Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `rozaliabomawrites-com` in your global stylesheet:

:root {
  /* Rozalia Boma — Multicultural Romance Author (rozaliabomawrites-com) — Live-Grounded CSS Variables */
  --background: 290 80% 92%; /* Canvas / Surface Token (rozaliabomawrites-com) */
  --foreground: 320 60% 18%; /* Typography Ink Token (rozaliabomawrites-com) */
  --card: 0 0% 100%; /* Dimension / Scale Token (rozaliabomawrites-com) */
  --card-foreground: 320 60% 18%; /* Typography Ink Token (rozaliabomawrites-com) */
  --popover: 0 0% 100%; /* Dimension / Scale Token (rozaliabomawrites-com) */
  --popover-foreground: 320 60% 18%; /* Typography Ink Token (rozaliabomawrites-com) */
  --primary: 330 95% 60%; /* Brand / Palette Token (rozaliabomawrites-com) */
  --primary-foreground: 0 0% 100%; /* Typography Ink Token (rozaliabomawrites-com) */
  --secondary: 280 85% 78%; /* Brand / Palette Token (rozaliabomawrites-com) */
  --secondary-foreground: 320 60% 18%; /* Typography Ink Token (rozaliabomawrites-com) */
  --muted: 320 60% 95%; /* Dimension / Scale Token (rozaliabomawrites-com) */
  --muted-foreground: 320 25% 45%; /* Typography Ink Token (rozaliabomawrites-com) */
  --accent: 195 90% 75%; /* Brand / Palette Token (rozaliabomawrites-com) */
  --accent-foreground: 320 60% 18%; /* Typography Ink Token (rozaliabomawrites-com) */
  --destructive: 0 84% 60%; /* Dimension / Scale Token (rozaliabomawrites-com) */
  --destructive-foreground: 0 0% 100%; /* Typography Ink Token (rozaliabomawrites-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#f5dafb` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#491237` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#ffffff` — grounded in `var(--normal-bg)` in `:root`
- **Interactive Accent / Highlight**: `#ffcc00` — grounded in `crubber-button.ytp-swatch-backg... { background-color: #ffcc00 }`
- **Secondary / Muted Copy**: `#fa3899` — grounded in live computed `h2` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#e5e7eb` — grounded in `:after { border-color: #e5e7eb }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1280×6624px` (multi-frame vertical journey filmstrip (6624px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2616px` (multi-frame vertical journey filmstrip (2616px), `390px` standard mobile width).
- **Container Max-Width**: `1368px` (measured widest bounded `<section>` landmark width on `1440px` desktop)
- **Padding & Gutters**: `2rem` lateral canvas padding with `.5rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1368px`, `gap: .5rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `2rem` horizontal padding
- **Media Queries**: `@media (max-width: 640px)`, `@media (min-width: 1400px)`, `@media (min-width: 640px)`, `@media (min-width: 768px)`
- **Corner Radii**: `var(--radius)`, `999px`, `14px`, `8px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Knewave`
- **Body Font Stack**: `Plus Jakarta Sans`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: live computed `h1` (`font-size: 96px`, `line-height: 96px`, `font-weight: 400`, `letter-spacing: -1.92px`)
- **H2 Section Rule**: live computed `h2` (`font-size: 93.9404px`, `line-height: 89.2434px`, `font-weight: 400`, `letter-spacing: 0.939404px`); rule `h2` (`letter-spacing: -.02em`, `font-weight: 400`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); rule `p` (`line-height: 1.65`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `rozaliabomawrites-com` (`Rozalia Boma — Multicultural Romance Author`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<nav.top-0> — `rozaliabomawrites-com`)**:
   - DOM & Selectors: Landmark `<nav class="top-0 left-0">` (`1440x68px`) hosting `Rozalia Boma — Multicultural Romance` navigation (`Home · Author · Books · Blog · Guestbook`), DOM attributes (`data-artifact-kind="dwl_content_hash"`, `data-artifact-id="db5c4db312500dfaed9e3..."`, `data-commit-sha="37366776bd44c18a989e4..."`, `data-context-token="v1.eyJwcm9qZWN0X2lkIj..."`), and stylesheet rule `after { box-sizing:border-box;border-width:0;border-style:solid;border-color:e5e7eb }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<nav.top-0> — `rozaliabomawrites-com`)` (`rozaliabomawrites-com`) adapts across `@media (max-width: 640px)`, `@media (min-width: 1400px)`, `@media (min-width: 640px)`, `@media (min-width: 768px)` with `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(0,0,.2,1)` transitions and links `Home · Author · Books · Blog · Guestbook`.
2. **Hero Stage & Focal Lead (<section.fixed> — `Rozalia Boma — writing multicultur`)**:
   - DOM & Selectors: Landmark `<section class="fixed">` presenting display lead `Rozalia Boma — writing multicultural romances` and copy excerpt *"ROZALIA BOMA WRITES IS LOADING"* over `#f5dafb` canvas and `#491237` ink.
   - Responsive Contract: Hero stage (`1280×6624px` desktop / `390×2616px` mobile) sets `#f5dafb` background with `#491237` headline `Rozalia Boma — writing multicultural romances`.
3. **Primary Showcase & Content Grid (<section.overflow-x-clip> — `ROZALIA BOMA WRITES IS LOADING`)**:
   - DOM & Selectors: Landmark `<section class="overflow-x-clip overflow-y-visible">` rendering section `ROZALIA BOMA WRITES IS LOADING` with copy *"Rozalia Boma Writes is loading"*, asset references (`holo-sky-bg-C4iYYOxV.webp`, `fonts.googleapis.com`, `fonts.gstatic.com`, `sykz-yx0lLcxQaSIhS23-w.woff2`), and grid rule `body { margin:0;line-height:inherit }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.overflow-x-clip> — `ROZALIA BOMA WRITES IS LOADING`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1368px`, `gap: .5rem`) on desktop and Single-column vertical stack at `390px` viewport width with `2rem` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.py-24> — `Rozalia Boma Writes is loading`)**:
   - DOM & Selectors: Landmark `<section class="py-24 relative">` framing `Rozalia Boma Writes is loading` and `Beware! Black Eastern European baddies on the ri` (*"Beware! Black Eastern European baddies on the rise!"*) with `#ffffff` surface cards, `#ffcc00` accents, and `strong { font-weight:bolder }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.py-24> — `Rozalia Boma Writes is loading`)` uses `var(--radius)`, `999px`, `14px`, `8px` radii, `#ffcc00` highlights, and assets (holo-sky-bg-C4iYYOxV.webp, fonts.googleapis.com, fonts.gstatic.com).
5. **Colophon & Global Directory Footer (<footer.mt-8> — `https://rozaliabomawrites.com/`)**:
   - DOM & Selectors: Landmark `<footer class="mt-8 relative">` anchoring `Rozalia Boma — Multicultural Rom` footer links (`Home · Author · Books · Blog · Guestbook`), copy *"w r i t i n g m u l t i c u l t u r a l"*, and `#e5e7eb` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.mt-8> — `https://rozaliabomawrites.com/`)` aligns to `1368px` (measured widest bounded `<section>` landmark width on `1440px` desktop) with `2rem` lateral canvas padding with `.5rem` grid gap and attributes (data-artifact-kind="dwl_content_hash", data-artifact-id="db5c4db312500dfaed9e3...", data-commit-sha="37366776bd44c18a989e4...").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"ROZALIA BOMA WRITES IS LOADING"*
- Copy Excerpt 2: *"Rozalia Boma Writes is loading"*
- Copy Excerpt 3: *"Beware! Black Eastern European baddies on the rise!"*
- Copy Excerpt 4: *"w r i t i n g m u l t i c u l t u r a l"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.4,0,.6,1)`, `cubic-bezier(.4,0,.2,1)`, `cubic-bezier(0,0,.2,1)`
- **Extracted Stylesheet Rules (`rozaliabomawrites-com`)**:
- `after { box-sizing:border-box;border-width:0;border-style:solid;border-color:e5e7eb }`
- `body { margin:0;line-height:inherit }`
- `strong { font-weight:bolder }`
- `small { font-size:80% }`
- `sup { font-size:75%;line-height:0;position:relative;vertical-align:baseline }`
- **Per-Selector Transition Rules**:
- **Selector `.btn-bubble`**: `transition: transform .12s ease,box-shadow .12s ease` extracted from `rozaliabomawrites-com` stylesheet.
- **Selector `.win98-btn`**: `transition: none` extracted from `rozaliabomawrites-com` stylesheet.
- **Selector `.y2k-textbox`**: `transition: transform .35s ease,box-shadow .35s ease` extracted from `rozaliabomawrites-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.4,0,.6,1)`)**: Governs interactive state transitions across `<nav.top-0>` and `<section.overflow-x-clip>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), HTML5 `<canvas>` Interactive Viewport Surface with `prefers-reduced-motion: reduce` fallback guards.
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `native` vertical progression up to `6121px` across 8 distinct viewport chapters using Lenis, WebGL/Canvas.
- **Vertical Chapter Sequence**: writing multicultural romances (0%) -> WE USE COOKIES (16%) -> Hi! I'm Rozalia Boma. (33%) -> The Book (49%) -> WE USE COOKIES (66%) -> GIRL, LET ME INTERVIEW MYSE... (82%) -> Sign up to the newsletter (99%) -> Sign up to the newsletter (100%).
- **Multi-Page Routes**: Scaffold internal routes `/blog` (listing, direct), `/about` (about, direct), `/contact` (about, direct) sharing the global header/footer shell and design tokens.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `rozaliabomawrites-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `0px` | `0%` | writing multicultural romances | `4` | [desktop-step-01.webp](assets/desktop-step-01.webp) |
| `#02` | `850px` | `16%` | WE USE COOKIES | `5` | [desktop-step-02.webp](assets/desktop-step-02.webp) |
| `#03` | `1700px` | `33%` | Hi! I'm Rozalia Boma. | `5` | [desktop-step-03.webp](assets/desktop-step-03.webp) |
| `#04` | `2550px` | `49%` | The Book | `5` | [desktop-step-04.webp](assets/desktop-step-04.webp) |
| `#05` | `3400px` | `66%` | WE USE COOKIES | `5` | [desktop-step-05.webp](assets/desktop-step-05.webp) |
| `#06` | `4250px` | `82%` | GIRL, LET ME INTERVIEW MYSELF FOR YOU | `5` | [desktop-step-06.webp](assets/desktop-step-06.webp) |
| `#07` | `5100px` | `99%` | Sign up to the newsletter | `5` | [desktop-step-07.webp](assets/desktop-step-07.webp) |
| `#08` | `5129px` | `100%` | Sign up to the newsletter | `5` | [desktop-step-08.webp](assets/desktop-step-08.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `0px` | `0%` | writing multicultural romances | [mobile-step-01.webp](assets/mobile-step-01.webp) |
| `#02` | `2790px` | `50%` | The Book | [mobile-step-02.webp](assets/mobile-step-02.webp) |
| `#03` | `5504px` | `100%` | Sign up to the newsletter | [mobile-step-03.webp](assets/mobile-step-03.webp) |

### Internal Subpage Filmstrips (`1080px` Wide WebP)
| # | Template | Route URL | H1 / Title | Scroll Height | Transition | Filmstrip Asset |
| :-: | :---: | :--- | :--- | :---: | :---: | :--- |
| `1` | `listing` | `https://rozaliabomawrites.com/blog` | Blog | `1714px` | `direct` (`2852ms`) | [subpage-01-blog.webp](assets/subpage-01-blog.webp) |
| `2` | `about` | `https://rozaliabomawrites.com/about` | About | `1958px` | `direct` (`446ms`) | [subpage-02-about.webp](assets/subpage-02-about.webp) |
| `3` | `about` | `https://rozaliabomawrites.com/contact` | Contact | `1592px` | `direct` (`822ms`) | [subpage-03-contact.webp](assets/subpage-03-contact.webp) |

