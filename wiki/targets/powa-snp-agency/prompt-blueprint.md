---
title: "UI Prompt Blueprint: powa-snp-agency"
date: 2026-11-24
captured_at: 2026-11-24
target: "powa-snp-agency"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
capture_mode: behavioral_journey_v2
asset_format: webp
scroll_driver: native
desktop_keyframes: 8
subpages_crawled: 1
http_status: 200
archetype: "Light-Substrate Editorial & Modular Grid System (`#f6f4f2` canvas, `#242424` ink, `#a133ff` accent)"
---

# UI Design System & Master Generation Blueprint: powa-snp-agency

> **Donate to POWA & Stand for Women's Equality · Help End Gender-Based Viol...** (https://powa.snp.agency/) — Join POWA's campaign to stand against gender-based violence. Donate and create a symbol for women's equality. Together, we can make a dif...

![Desktop Journey Filmstrip (1280x6624)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x2616)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Donate to POWA & Stand for Women's Equality · Help End Gender-Based Viol...** (`https://powa.snp.agency/`). Join POWA's campaign to stand against gender-based violence. Donate and create a symbol for women's equality. Together, we can make a dif...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#f6f4f2` canvas, `#242424` ink, `#a133ff` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#f6f4f2` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#242424` primary typography and `#a133ff` accents.
  - **Grounded Typographic Hierarchy**: Uses `__figtree_6417dc` across display (`CREATE + DONATE`) and body copy.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 0px (flush layout)`, padding `0px`) with `cubic-bezier(0.55,0.085,0.68,0.53)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×6624px` (`assets/desktop-journey.webp`, `8` keyframes up to `y=4499px` / doc `8138px`), Mobile `390×2616px` (`assets/mobile-journey.webp`, `3` keyframes).
- **Master Container Bounds**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport).
- **Canvas Lateral Padding & Spacing**: `0px` lateral canvas padding with `0px (flush layout)` grid gap.
- **Border Radius Scale**: `50%`, `2px`, `100%`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 0px (flush layout)`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `0px` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen and (max-width:1024px)`, `@media screen and (max-width:1440px)`, `@media screen and (max-width:1024px)and (hover:hover)`, `@media screen and (min-width:768px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f6f4f2` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#242424` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `.WaterfallImageAnimation_item__... { background: #ffffff }` |
| **Interactive Accent / Highlight** | `#a133ff` | `var(--primary-purple)` in `:root` |
| **Secondary / Muted Copy** | `#adabaa` | `var(--secondary-grey)` in `:root` |
| **Structural Hairline Border** | `#acaba9` | `.StyledButton_preset-payment__z... { border: #acaba9 }` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--vw-screen` | `360` | Layout / Spatial Grid Token |
| `--logo-size` | `max(2.5rem,28px)` | Layout / Spatial Grid Token |
| `--z-preloader` | `10` | Elevation / Border Token |
| `--z-cursor` | `9` | Elevation / Border Token |
| `--z-page-transition` | `8` | Motion / Easing Token |
| `--z-overflow` | `7` | Elevation / Border Token |
| `--z-banner` | `6` | Elevation / Border Token |
| `--z-modal` | `5` | Elevation / Border Token |
| `--z-header` | `4` | Layout / Spatial Grid Token |
| `--z-transition` | `3` | Motion / Easing Token |
| `--z-header-dropdown` | `2` | Layout / Spatial Grid Token |
| `--z-selectors` | `1` | Elevation / Border Token |
| `--gap-4` | `calc(4 / var(--vw-screen) * 100 * 1vw)` | Layout / Spatial Grid Token |
| `--gap-8` | `calc(8 / var(--vw-screen) * 100 * 1vw)` | Layout / Spatial Grid Token |
| `--gap-12` | `calc(12 / var(--vw-screen) * 100 * 1vw)` | Layout / Spatial Grid Token |
| `--gap-16` | `calc(16 / var(--vw-screen) * 100 * 1vw)` | Layout / Spatial Grid Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `__figtree_6417dc`.
- **Primary Body Stack**: `__figtree_6417dc`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 131.25px`, `line-height: 105px`, `font-weight: 800`, `letter-spacing: -2.625px`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 131.25px`, `line-height: 105px`, `font-weight: 800`, `letter-spacing: -2.625px`).
- **Body Copy**: live computed `body` (`font-size: 15px`, `line-height: 15px`, `font-weight: 400`); rule `p` (`letter-spacing: -.02em`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 13.125px`, `line-height: 17.7188px`, `font-weight: 400`, `letter-spacing: -0.13125px`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.55,0.085,0.68,0.53)`, `cubic-bezier(0.55,0.055,0.675,0.19)`, `cubic-bezier(0.895,0.03,0.685,0.22)`.

### Per-Element Transition & Choreography Rules
- **Selector `::-webkit-input-placeholder`**: `transition: opacity .3s` extracted from `powa-snp-agency` stylesheet.
- **Selector `::-moz-input-placeholder`**: `transition: opacity .3s` extracted from `powa-snp-agency` stylesheet.
- **Selector `:-moz-placeholder`**: `transition: opacity .3s` extracted from `powa-snp-agency` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.55,0.085,0.68,0.53)`)**: Governs interactive state transitions across `<header.fonts-loaded>` and `<section.Intro_root__El5X_>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `native` (max document height `8138px`, deepest scrollY reached `4499px` across `8` desktop keyframes).
- **Detected Scroll / Motion Libraries**: `Lenis`.
- **Hover Physics (`primary_cta` · `DONATE AND CREATE`)**: `backgroundColor`: `rgb(161, 51, 255)` -> `rgb(179, 94, 253)` (`transition-duration: 0.38s`, `timing: cubic-bezier(0.215, 0.61, 0.355, 1)`).
- **Route Transition Architecture**: First internal navigation (`/donate-&-create`) measured as `SPA` in `1172ms`.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Donate to POWA & Stand for Women's Equalit │
│ ====================================================================== │
│ [ <header.fonts-loaded> (1440px)      | Get in touch · DONATE AND CR ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.Land_root__Wp6AW> (w=1440px)                  | │
│ | H1: CREATE + DONATE                                                | │
│ | Substrate: #f6f4f2 | Ink: #242424 | Accent: #a133ff                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.Intro_root__El5X_) max-w: 1440px           | │
│ | +------------------------------+  +------------------------------+ | │
│ | | together we can make a diffe |  | to fight the abuse against w | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.Intro_root__El5X_) — powa-snp-agency Archi | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.Cursor_inner) | https://powa.snp.agency/             │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 0px (flu)   │
│ ====================================================================== │
│ [ HEADER BAR (<header.fonts-loaded>   ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.Land_root__Wp6A) — 390px Vertical Lead        | │
│ | H1: CREATE + DONATE                                                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.Intro_root__E) — 1-Col Stack              | │
│ | [ Item 1: together we can make a difference                      ] | │
│ | [ Item 2: to fight the abuse against women                       ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.Intro_root__El5) — 1-Col (powa-snp-agency Ar) │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.Cursor_inner) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.fonts-loaded> — `powa-snp-agency`)**:
   - Landmark `<header class="fonts-loaded">` (`1440px`) hosting `Donate to POWA & Stand for Women's E` navigation (`Get in touch · DONATE AND CREATE`), DOM attributes (`data-next-font="size-adjust"`, `data-next-font="size-adjust"`, `data-next-font="size-adjust"`, `data-next-font="size-adjust"`), and stylesheet rule `.__className_6417dc { font-family:__figtree_6417dc,__figtree_Fallback_6417dc }`.
2. **Hero Stage & Focal Lead (<section.Land_root__Wp6AW> — `CREATE + DONATE`)**:
   - Landmark `<section class="Land_root__Wp6AW Home_land__wexsp">` presenting display lead `CREATE + DONATE` and copy excerpt *"A safe future for women won’t happen by itself. We have to design"* over `#f6f4f2` canvas and `#242424` ink.
3. **Primary Showcase & Content Grid (<section.Intro_root__El5X_> — `together we can make a difference`)**:
   - Landmark `<section class="Intro_root__El5X_">` rendering section `together we can make a difference` with copy *"to fight the abuse against women"*, asset references (`light-apple-touch-icon.png`, `light-favicon-32x32.png`, `light-favicon-16x16.png`, `light-site.webmanifest`), and grid rule `.__variable_6417dc { --primary-font:"__figtree_6417dc","__figtree_Fallback_6417dc" }`.
4. **Interactive Detail & Feature Matrix (<section.Intro_root__El5X_:nth(2)> — `to fight the abuse against women`)**:
   - Landmark `<section class="Intro_root__El5X_">` framing `to fight the abuse against women` and `powa-snp-agency Archive & Directory` (*"together we can make a difference"*) with `#ffffff` surface cards, `#a133ff` accents, and `before { box-sizing:inherit }`.
5. **Colophon & Global Directory Footer (<footer.Cursor_innerWrap__BCUuD> — `https://powa.snp.agency/`)**:
   - Landmark `<footer class="Cursor_innerWrap__BCUuD">` anchoring `Donate to POWA & Stand for Women` footer links (`Get in touch · DONATE AND CREATE`), copy *"to fight the abuse against women"*, and `#acaba9` structural dividers.
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=0px`, `0%`): Active landmark `CREATE + DONATE` · sticky/fixed elements: `1`
- **Step 02** (`y=850px`, `12%`): Active landmark `TOGETHER WE CAN MAKE A DIFFERENCE` · sticky/fixed elements: `2`
- **Step 03** (`y=1700px`, `23%`): Active landmark `TOGETHER WE CAN MAKE A DIFFERENCE` · sticky/fixed elements: `2`
- **Step 04** (`y=1790px`, `25%`): Active landmark `TOGETHER WE CAN MAKE A DIFFERENCE` · sticky/fixed elements: `2`
- **Step 05** (`y=1798px`, `25%`): Active landmark `TOGETHER WE CAN MAKE A DIFFERENCE` · sticky/fixed elements: `2`
- **Step 06** (`y=4250px`, `59%`): Active landmark `TOGETHER WE CAN MAKE A DIFFERENCE` · sticky/fixed elements: `2`
- **Step 07** (`y=4411px`, `61%`): Active landmark `TOGETHER WE CAN MAKE A DIFFERENCE` · sticky/fixed elements: `2`
- **Step 08** (`y=4499px`, `62%`): Active landmark `TOGETHER WE CAN MAKE A DIFFERENCE` · sticky/fixed elements: `2`

### Multi-Page Internal Route Map
- **Other Route (`/donate-&-create`)**: `https://powa.snp.agency/donate-&-create` — H1: `Donate & Create a Symbol for Women's Equality · S...`, scrollHeight `900px`, transition `SPA` (`1172ms`)

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: powa-snp-agency (Donate to POWA & Stand for Women's Equality · Help End Gender-Based Viol...)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `powa-snp-agency` (**Donate to POWA & Stand for Women's Equality · Help End Gender-Based Viol...** — `https://powa.snp.agency/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#f6f4f2` canvas, `#242424` ink, `#a133ff` accent).
- **Identity & Domain Context**: Join POWA's campaign to stand against gender-based violence. Donate and create a symbol for women's equality. Together, we can make a dif...
- **Primary Substrate**: `#f6f4f2` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#242424`, **Accent / Highlight**: `#a133ff`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#f6f4f2` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#242424` primary typography and `#a133ff` accents.
  - **Grounded Typographic Hierarchy**: Uses `__figtree_6417dc` across display (`CREATE + DONATE`) and body copy.
  - **Calibrated Spatial Grid & Motion**: Combines `1440px` container bounds (`gap: 0px (flush layout)`, padding `0px`) with `cubic-bezier(0.55,0.085,0.68,0.53)` easing and Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `powa-snp-agency` in your global stylesheet:

:root {
  /* Donate to POWA & Stand for Women's Equality · Help End Gender-Based Viol... (powa-snp-agency) — Live-Grounded CSS Variables */
  --vw-screen: 360; /* Layout / Spatial Grid Token (powa-snp-agency) */
  --logo-size: max(2.5rem,28px); /* Layout / Spatial Grid Token (powa-snp-agency) */
  --z-preloader: 10; /* Elevation / Border Token (powa-snp-agency) */
  --z-cursor: 9; /* Elevation / Border Token (powa-snp-agency) */
  --z-page-transition: 8; /* Motion / Easing Token (powa-snp-agency) */
  --z-overflow: 7; /* Elevation / Border Token (powa-snp-agency) */
  --z-banner: 6; /* Elevation / Border Token (powa-snp-agency) */
  --z-modal: 5; /* Elevation / Border Token (powa-snp-agency) */
  --z-header: 4; /* Layout / Spatial Grid Token (powa-snp-agency) */
  --z-transition: 3; /* Motion / Easing Token (powa-snp-agency) */
  --z-header-dropdown: 2; /* Layout / Spatial Grid Token (powa-snp-agency) */
  --z-selectors: 1; /* Elevation / Border Token (powa-snp-agency) */
  --gap-4: calc(4 / var(--vw-screen) * 100 * 1vw); /* Layout / Spatial Grid Token (powa-snp-agency) */
  --gap-8: calc(8 / var(--vw-screen) * 100 * 1vw); /* Layout / Spatial Grid Token (powa-snp-agency) */
  --gap-12: calc(12 / var(--vw-screen) * 100 * 1vw); /* Layout / Spatial Grid Token (powa-snp-agency) */
  --gap-16: calc(16 / var(--vw-screen) * 100 * 1vw); /* Layout / Spatial Grid Token (powa-snp-agency) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#f6f4f2` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#242424` — grounded in live computed `main` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#ffffff` — grounded in `.WaterfallImageAnimation_item__... { background: #ffffff }`
- **Interactive Accent / Highlight**: `#a133ff` — grounded in `var(--primary-purple)` in `:root`
- **Secondary / Muted Copy**: `#adabaa` — grounded in `var(--secondary-grey)` in `:root`
- **Structural Hairline Border**: `#acaba9` — grounded in `.StyledButton_preset-payment__z... { border: #acaba9 }`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1280×6624px` (multi-frame vertical journey filmstrip (6624px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2616px` (multi-frame vertical journey filmstrip (2616px), `390px` standard mobile width).
- **Container Max-Width**: `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport)
- **Padding & Gutters**: `0px` lateral canvas padding with `0px (flush layout)` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 0px (flush layout)`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `0px` horizontal padding
- **Media Queries**: `@media screen and (max-width:1024px)`, `@media screen and (max-width:1440px)`, `@media screen and (max-width:1024px)and (hover:hover)`, `@media screen and (min-width:768px)`
- **Corner Radii**: `50%`, `2px`, `100%`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `__figtree_6417dc`
- **Body Font Stack**: `__figtree_6417dc`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: live computed `h1` (`font-size: 131.25px`, `line-height: 105px`, `font-weight: 800`, `letter-spacing: -2.625px`)
- **H2 Section Rule**: live computed `h2` (`font-size: 131.25px`, `line-height: 105px`, `font-weight: 800`, `letter-spacing: -2.625px`)
- **Body Copy Rule**: live computed `body` (`font-size: 15px`, `line-height: 15px`, `font-weight: 400`); rule `p` (`letter-spacing: -.02em`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 13.125px`, `line-height: 17.7188px`, `font-weight: 400`, `letter-spacing: -0.13125px`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `powa-snp-agency` (`Donate to POWA & Stand for Women's Equality · Help End Gender-Based Viol...`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.fonts-loaded> — `powa-snp-agency`)**:
   - DOM & Selectors: Landmark `<header class="fonts-loaded">` (`1440px`) hosting `Donate to POWA & Stand for Women's E` navigation (`Get in touch · DONATE AND CREATE`), DOM attributes (`data-next-font="size-adjust"`, `data-next-font="size-adjust"`, `data-next-font="size-adjust"`, `data-next-font="size-adjust"`), and stylesheet rule `.__className_6417dc { font-family:__figtree_6417dc,__figtree_Fallback_6417dc }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.fonts-loaded> — `powa-snp-agency`)` (`powa-snp-agency`) adapts across `@media screen and (max-width:1024px)`, `@media screen and (max-width:1440px)`, `@media screen and (max-width:1024px)and (hover:hover)`, `@media screen and (min-width:768px)` with `cubic-bezier(0.55,0.085,0.68,0.53)`, `cubic-bezier(0.55,0.055,0.675,0.19)`, `cubic-bezier(0.895,0.03,0.685,0.22)` transitions and links `Get in touch · DONATE AND CREATE`.
2. **Hero Stage & Focal Lead (<section.Land_root__Wp6AW> — `CREATE + DONATE`)**:
   - DOM & Selectors: Landmark `<section class="Land_root__Wp6AW Home_land__wexsp">` presenting display lead `CREATE + DONATE` and copy excerpt *"A safe future for women won’t happen by itself. We have to design"* over `#f6f4f2` canvas and `#242424` ink.
   - Responsive Contract: Hero stage (`1280×6624px` desktop / `390×2616px` mobile) sets `#f6f4f2` background with `#242424` headline `CREATE + DONATE`.
3. **Primary Showcase & Content Grid (<section.Intro_root__El5X_> — `together we can make a difference`)**:
   - DOM & Selectors: Landmark `<section class="Intro_root__El5X_">` rendering section `together we can make a difference` with copy *"to fight the abuse against women"*, asset references (`light-apple-touch-icon.png`, `light-favicon-32x32.png`, `light-favicon-16x16.png`, `light-site.webmanifest`), and grid rule `.__variable_6417dc { --primary-font:"__figtree_6417dc","__figtree_Fallback_6417dc" }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.Intro_root__El5X_> — `together we can make a difference`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1440px`, `gap: 0px (flush layout)`) on desktop and Single-column vertical stack at `390px` viewport width with `0px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.Intro_root__El5X_:nth(2)> — `to fight the abuse against women`)**:
   - DOM & Selectors: Landmark `<section class="Intro_root__El5X_">` framing `to fight the abuse against women` and `powa-snp-agency Archive & Directory` (*"together we can make a difference"*) with `#ffffff` surface cards, `#a133ff` accents, and `before { box-sizing:inherit }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.Intro_root__El5X_:nth(2)> — `to fight the abuse against women`)` uses `50%`, `2px`, `100%` radii, `#a133ff` highlights, and assets (light-apple-touch-icon.png, light-favicon-32x32.png, light-favicon-16x16.png).
5. **Colophon & Global Directory Footer (<footer.Cursor_innerWrap__BCUuD> — `https://powa.snp.agency/`)**:
   - DOM & Selectors: Landmark `<footer class="Cursor_innerWrap__BCUuD">` anchoring `Donate to POWA & Stand for Women` footer links (`Get in touch · DONATE AND CREATE`), copy *"to fight the abuse against women"*, and `#acaba9` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.Cursor_innerWrap__BCUuD> — `https://powa.snp.agency/`)` aligns to `1440px` (full-bleed `100%` desktop stage measured on `1440px` viewport) with `0px` lateral canvas padding with `0px (flush layout)` grid gap and attributes (data-next-font="size-adjust", data-next-font="size-adjust", data-next-font="size-adjust").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"A safe future for women won’t happen by itself. We have to design it. Create and d..."*
- Copy Excerpt 2: *"to fight the abuse against women"*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.55,0.085,0.68,0.53)`, `cubic-bezier(0.55,0.055,0.675,0.19)`, `cubic-bezier(0.895,0.03,0.685,0.22)`
- **Extracted Stylesheet Rules (`powa-snp-agency`)**:
- `.__className_6417dc { font-family:__figtree_6417dc,__figtree_Fallback_6417dc }`
- `.__variable_6417dc { --primary-font:"__figtree_6417dc","__figtree_Fallback_6417dc" }`
- `before { box-sizing:inherit }`
- `html { box-sizing:border-box;height:100% }`
- `webkit-input-placeholder { color:inherit;opacity:1;-webkit-transition:opacity .3s;transition:opacit... }`
- **Per-Selector Transition Rules**:
- **Selector `::-webkit-input-placeholder`**: `transition: opacity .3s` extracted from `powa-snp-agency` stylesheet.
- **Selector `::-moz-input-placeholder`**: `transition: opacity .3s` extracted from `powa-snp-agency` stylesheet.
- **Selector `:-moz-placeholder`**: `transition: opacity .3s` extracted from `powa-snp-agency` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.55,0.085,0.68,0.53)`)**: Governs interactive state transitions across `<header.fonts-loaded>` and `<section.Intro_root__El5X_>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), Three.js / WebGL Canvas Pipeline with `prefers-reduced-motion: reduce` fallback guards.
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `native` vertical progression up to `8138px` across 8 distinct viewport chapters using Lenis.
- **Vertical Chapter Sequence**: CREATE + DONATE (0%) -> TOGETHER WE CAN MAKE A DIFF... (12%) -> TOGETHER WE CAN MAKE A DIFF... (23%) -> TOGETHER WE CAN MAKE A DIFF... (25%) -> TOGETHER WE CAN MAKE A DIFF... (25%) -> TOGETHER WE CAN MAKE A DIFF... (59%) -> TOGETHER WE CAN MAKE A DIFF... (61%) -> TOGETHER WE CAN MAKE A DIFF... (62%).
- **Hover Micro-Interaction (`primary_cta`)**: Animate `backgroundColor` with `0.38s cubic-bezier(0.215, 0.61, 0.355, 1)`.
- **Multi-Page Routes**: Scaffold internal routes `/donate-&-create` (other, SPA) sharing the global header/footer shell and design tokens.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `powa-snp-agency`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `0px` | `0%` | CREATE + DONATE | `1` | [desktop-step-01.webp](assets/desktop-step-01.webp) |
| `#02` | `850px` | `12%` | TOGETHER WE CAN MAKE A DIFFERENCE | `2` | [desktop-step-02.webp](assets/desktop-step-02.webp) |
| `#03` | `1700px` | `23%` | TOGETHER WE CAN MAKE A DIFFERENCE | `2` | [desktop-step-03.webp](assets/desktop-step-03.webp) |
| `#04` | `1790px` | `25%` | TOGETHER WE CAN MAKE A DIFFERENCE | `2` | [desktop-step-04.webp](assets/desktop-step-04.webp) |
| `#05` | `1798px` | `25%` | TOGETHER WE CAN MAKE A DIFFERENCE | `2` | [desktop-step-05.webp](assets/desktop-step-05.webp) |
| `#06` | `4250px` | `59%` | TOGETHER WE CAN MAKE A DIFFERENCE | `2` | [desktop-step-06.webp](assets/desktop-step-06.webp) |
| `#07` | `4411px` | `61%` | TOGETHER WE CAN MAKE A DIFFERENCE | `2` | [desktop-step-07.webp](assets/desktop-step-07.webp) |
| `#08` | `4499px` | `62%` | TOGETHER WE CAN MAKE A DIFFERENCE | `2` | [desktop-step-08.webp](assets/desktop-step-08.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `0px` | `0%` | CREATE + DONATE | [mobile-step-01.webp](assets/mobile-step-01.webp) |
| `#02` | `3376px` | `50%` | TOGETHER WE CAN MAKE A DIFFERENCE | [mobile-step-02.webp](assets/mobile-step-02.webp) |
| `#03` | `6752px` | `100%` | TOGETHER WE CAN MAKE A DIFFERENCE | [mobile-step-03.webp](assets/mobile-step-03.webp) |

### Internal Subpage Filmstrips (`1080px` Wide WebP)
| # | Template | Route URL | H1 / Title | Scroll Height | Transition | Filmstrip Asset |
| :-: | :---: | :--- | :--- | :---: | :---: | :--- |
| `1` | `other` | `https://powa.snp.agency/donate-&-create` | Donate & Create a Symbol for Women's... | `900px` | `SPA` (`1172ms`) | [subpage-01-donate-create.webp](assets/subpage-01-donate-create.webp) |

