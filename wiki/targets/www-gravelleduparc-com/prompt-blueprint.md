---
title: "UI Prompt Blueprint: www-gravelleduparc-com"
date: 2026-11-24
captured_at: 2026-11-24
target: "www-gravelleduparc-com"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
capture_mode: behavioral_journey_v2
asset_format: webp
scroll_driver: native
desktop_keyframes: 8
subpages_crawled: 0
http_status: 200
archetype: "Light-Substrate Editorial & Modular Grid System (`#fffbf0` canvas, `#000000` ink, `#0000ee` accent)"
---

# UI Design System & Master Generation Blueprint: www-gravelleduparc-com

> **Gravelle du Parc · Événement gravel bike — 2-4 octobre 2026** (https://www.gravelleduparc.com/) — La Gravelle du Parc, c’est un week-end de gravel : vélo de gravelle le samedi, course à pied le dimanche. Plusieurs distances, expérience...

![Desktop Journey Filmstrip (1280x6624)](assets/desktop-journey.webp)

![Mobile Journey Filmstrip (390x2616)](assets/mobile-journey.webp)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Gravelle du Parc · Événement gravel bike — 2-4 octobre 2026** (`https://www.gravelleduparc.com/`). La Gravelle du Parc, c’est un week-end de gravel : vélo de gravelle le samedi, course à pied le dimanche. Plusieurs distances, expérience...
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-24`).
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#fffbf0` canvas, `#000000` ink, `#0000ee` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#fffbf0` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#0000ee` accents.
  - **Grounded Typographic Hierarchy**: Pairs `PP Frama Regular` for display copy (`GRAVELLE DU PARC`) with `PP Frama Regular Placeholder`.
  - **Calibrated Spatial Grid & Motion**: Combines `1408px` container bounds (`gap: 16px`, padding `2px`) with `cubic-bezier(0.44,0,0.56,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

### Viewport Allocation & Container Geometry
- **Captured Journey Filmstrips**: Desktop `1280×6624px` (`assets/desktop-journey.webp`, `8` keyframes up to `y=14400px` / doc `23080px`), Mobile `390×2616px` (`assets/mobile-journey.webp`, `3` keyframes).
- **Master Container Bounds**: `1408px` (measured widest bounded `<section>` landmark width on `1440px` desktop).
- **Canvas Lateral Padding & Spacing**: `2px` lateral canvas padding with `16px` grid gap.
- **Border Radius Scale**: `10px`, `50%`, `4px`, `12px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1408px`, `gap: 16px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `2px` horizontal padding.
- **Extracted CSS Media Queries**: `@media screen`, `@media screen and (forced-colors:active)`, `@media screen and (forced-colors:active) and (prefers-color-sche...`, `@media (prefers-reduced-motion:reduce)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#fffbf0` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#000000` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#baf1c5` | live computed `button` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#0000ee` | live computed `a` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#15663c` | live computed `button` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#222222` | `var(--border-color)` in `:root` |
| **Variable Token (`--token-801dfdec-b31d-4dcb-87a3-9e0e817b84a0`)** | `#cca7e4` | `var(--token-801dfdec-b31d-4dcb-87a3-9e0e817b84a0)` in `:root` |
| **Variable Token (`--token-955bd1bf-f5bd-48e1-aa7a-184730d5a46a`)** | `#a980c4` | `var(--token-955bd1bf-f5bd-48e1-aa7a-184730d5a46a)` in `:root` |
| **Variable Token (`--token-819cd3c1-358d-4fbc-829d-c778243cf65a`)** | `#7ede92` | `var(--token-819cd3c1-358d-4fbc-829d-c778243cf65a)` in `:root` |
| **Variable Token (`--token-59b8ee6e-2d8c-4453-b6ce-0800b1668299`)** | `#f8efda` | `var(--token-59b8ee6e-2d8c-4453-b6ce-0800b1668299)` in `:root` |
| **Variable Token (`--token-e2fce9db-4f7d-4508-8af5-6e27334c8d93`)** | `#f7ebff` | `var(--token-e2fce9db-4f7d-4508-8af5-6e27334c8d93)` in `:root` |
| **Variable Token (`--token-9e8de558-3943-41e7-b539-eba07384897f`)** | `#59396e` | `var(--token-9e8de558-3943-41e7-b539-eba07384897f)` in `:root` |
| **Variable Token (`--token-ebd8e842-7d03-4da2-a324-48cca40569ff`)** | `#84ba8f` | `var(--token-ebd8e842-7d03-4da2-a324-48cca40569ff)` in `:root` |
| **Variable Token (`--token-9a333514-96bd-43a4-9d9c-387c4eccd2bb`)** | `#363229` | `var(--token-9a333514-96bd-43a4-9d9c-387c4eccd2bb)` in `:root` |
| **Variable Token (`--token-a9a86cd5-8eaf-4794-a1ba-722f2e95e2eb`)** | `#dbd0b4` | `var(--token-a9a86cd5-8eaf-4794-a1ba-722f2e95e2eb)` in `:root` |
| **Variable Token (`--token-394b655e-eb71-48d0-ad1f-647e45a4f590`)** | `#f5fbff` | `var(--token-394b655e-eb71-48d0-ad1f-647e45a4f590)` in `:root` |
| **Variable Token (`--token-7271da1b-9f0a-41bd-91b9-d7098d8944de`)** | `#efedff` | `var(--token-7271da1b-9f0a-41bd-91b9-d7098d8944de)` in `:root` |
| **Variable Token (`--token-3d3e37dc-c784-4b46-95bf-180ff18227e6`)** | `#0b0b0b` | `var(--token-3d3e37dc-c784-4b46-95bf-180ff18227e6)` in `:root` |
| **Variable Token (`--token-a37e6c3e-a10c-437b-b258-07d1d49555da`)** | `#fcebef` | `var(--token-a37e6c3e-a10c-437b-b258-07d1d49555da)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--token-a5ac08d3-da39-4d23-ae40-d4bbcd8e3fd1` | `#fffbf0` | Color / Atmospheric Token |
| `--token-801dfdec-b31d-4dcb-87a3-9e0e817b84a0` | `#cca7e4` | Color / Atmospheric Token |
| `--token-b73f07c2-b1d7-4a83-b30a-c43c65cbb498` | `#15663c` | Color / Atmospheric Token |
| `--token-5eaeb86f-8e78-453e-95cb-73c07bed6a1e` | `#baf1c5` | Color / Atmospheric Token |
| `--token-955bd1bf-f5bd-48e1-aa7a-184730d5a46a` | `#a980c4` | Color / Atmospheric Token |
| `--token-819cd3c1-358d-4fbc-829d-c778243cf65a` | `#7ede92` | Color / Atmospheric Token |
| `--token-59b8ee6e-2d8c-4453-b6ce-0800b1668299` | `#f8efda` | Color / Atmospheric Token |
| `--token-e2fce9db-4f7d-4508-8af5-6e27334c8d93` | `#f7ebff` | Color / Atmospheric Token |
| `--token-9e8de558-3943-41e7-b539-eba07384897f` | `#59396e` | Color / Atmospheric Token |
| `--token-ebd8e842-7d03-4da2-a324-48cca40569ff` | `#84ba8f` | Color / Atmospheric Token |
| `--token-9a333514-96bd-43a4-9d9c-387c4eccd2bb` | `#363229` | Color / Atmospheric Token |
| `--token-a9a86cd5-8eaf-4794-a1ba-722f2e95e2eb` | `#dbd0b4` | Color / Atmospheric Token |
| `--token-394b655e-eb71-48d0-ad1f-647e45a4f590` | `#f5fbff` | Color / Atmospheric Token |
| `--token-7271da1b-9f0a-41bd-91b9-d7098d8944de` | `#efedff` | Color / Atmospheric Token |
| `--token-3d3e37dc-c784-4b46-95bf-180ff18227e6` | `#0b0b0b` | Color / Atmospheric Token |
| `--token-a37e6c3e-a10c-437b-b258-07d1d49555da` | `#fcebef` | Color / Atmospheric Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `PP Frama Regular`.
- **Primary Body Stack**: `PP Frama Regular Placeholder`.
- **Technical / Metadata Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`).

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 112px`, `line-height: 112px`, `font-weight: 400`); rule `h1` (`font-size: calc(var(--framer-root-font-s...`, `line-height: 1em`, `letter-spacing: 0em`, `font-weight: 400`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 80px`, `line-height: 96px`, `font-weight: 400`); rule `h2` (`font-size: calc(var(--framer-root-font-s...`, `line-height: 1.2em`, `letter-spacing: 0em`, `font-weight: 400`).
- **Body Copy**: live computed `body` (`font-size: 12px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: calc(var(--framer-root-font-s...`, `line-height: 1.2em`, `letter-spacing: 0em`, `font-weight: 700`).
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 12px`, `line-height: normal`, `font-weight: 400`); CSS variables `--letter-spacing: var(--framer-letter-spacing)`.

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.44,0,0.56,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.lenis.lenis-autoToggle`**: `transition: 1ms` extracted from `www-gravelleduparc-com` stylesheet.
- **Selector `.swiper-wrapper`**: `transition: var(--swiper-wrapper-transition-timing-function,initial)` extracted from `www-gravelleduparc-com` stylesheet.
- **Selector `.swiper-pagination`**: `transition: opacity .3s` extracted from `www-gravelleduparc-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.44,0,0.56,1)`)**: Governs interactive state transitions across `<header.lenis>` and `<section.framer-1qtcgda>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Swiper Touch Carousel Engine, Framer Motion Layout Physics with `prefers-reduced-motion: reduce` fallback guards.
### Measured Runtime Scroll & Interaction Telemetry (`behavioral_journey_v2`)
- **Scroll Driver Mode**: `native` (max document height `23080px`, deepest scrollY reached `14400px` across `8` desktop keyframes).
- **Detected Scroll / Motion Libraries**: `Lenis`, `GSAP/ScrollTrigger`, `Framer Motion`.
- **Hover Physics (`primary_cta` · `Découvrir l'événement`)**: Computed transition `0s` / `ease` (no static color/transform shift captured at rest).
- **Interactive Control Probe (`tab`)**: Tested `129 KM` (diff `1.425`).

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Gravelle du Parc · Événement gravel bike — │
│ ====================================================================== │
│ [ <header.lenis> (437x113px)          | Overview · Index · Archive · ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.framer-3c888> (w=1440px)                      | │
│ | H1: GRAVELLE DU PARC                                               | │
│ | Substrate: #fffbf0 | Ink: #000000 | Accent: #0000ee                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.framer-1qtcgda>) max-w: 1408px             | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Ils seront là! Et toi?       |  | Les expériences              | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<section.framer-597gjk>) — Commanditaire            | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.framer-17xvn) | https://www.gravelleduparc.com/      │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 16px)       │
│ ====================================================================== │
│ [ HEADER BAR (<header.lenis>          ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<section.framer-3c888>) — 390px Vertical Lead          | │
│ | H1: GRAVELLE DU PARC                                               | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<section.framer-1qtcgd) — 1-Col Stack              | │
│ | [ Item 1: Ils seront là! Et toi?                                 ] | │
│ | [ Item 2: Les expériences                                        ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<section.framer-597gjk>) — 1-Col (Commanditaire)     | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.framer-17xvn) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.lenis> — `www-gravelleduparc-com`)**:
   - Landmark `<header class="lenis">` (`437x113px`) hosting `Gravelle du Parc · Événement gravel ` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-framer-font-css`, `data-framer-breakpoint-css`, `data-framer-css-ssr-minified`, `data-framer-components="framer-lib-cursors-ho..."`), and stylesheet rule `html.lenis body { height: auto; }`.
2. **Hero Stage & Focal Lead (<section.framer-3c888> — `GRAVELLE DU PARC`)**:
   - Landmark `<section class="framer-3c888">` presenting display lead `GRAVELLE DU PARC` and copy excerpt *"2–4 octobre 2026 · Wakefield, QC"* over `#fffbf0` canvas and `#000000` ink.
3. **Primary Showcase & Content Grid (<section.framer-1qtcgda> — `Ils seront là! Et toi?`)**:
   - Landmark `<section class="framer-1qtcgda">` rendering section `Ils seront là! Et toi?` with copy *"Découvrir l'événement"*, asset references (`iM7hUimGereN8t0VwJyHekeIY.png`, `kPdF8fyktsGL7BKiYVgEs0g8Ozg.png`, `BPKxeJbv6FMQXmeKTCEyN570iaI.png`, `hls.min.js`), and grid rule `.lenis-stopped { overflow: clip; }`.
4. **Interactive Detail & Feature Matrix (<section.framer-597gjk> — `Les expériences`)**:
   - Landmark `<section class="framer-597gjk">` framing `Les expériences` and `Commanditaire` (*"S'inscrire maintenant"*) with `#baf1c5` surface cards, `#0000ee` accents, and `.lenis.lenis-smooth iframe { pointer-events: none; }`.
5. **Colophon & Global Directory Footer (<footer.framer-17xvneb-container> — `https://www.gravelleduparc.com/`)**:
   - Landmark `<footer class="framer-17xvneb-container">` anchoring `Gravelle du Parc · Événement gra` footer links (`Overview · Index · Archive · About · Contact`), copy *"Gravelle du Parc c'est pas juste une course. C'est un weeken"*, and `#222222` structural dividers.
### Full Vertical Scroll Sequence (Desktop `1440×900` Keyframes)
- **Step 01** (`y=0px`, `0%`): Active landmark `GRAVELLE DU PARC` · sticky/fixed elements: `1`
- **Step 02** (`y=850px`, `4%`): Active landmark `#video` · sticky/fixed elements: `2`
- **Step 03** (`y=3400px`, `16%`): Active landmark `#levenement` · sticky/fixed elements: `2`
- **Step 04** (`y=5950px`, `28%`): Active landmark `#schedule` · sticky/fixed elements: `4`
- **Step 05** (`y=8500px`, `39%`): Active landmark `Les expériences` · sticky/fixed elements: `1`
- **Step 06** (`y=11050px`, `50%`): Active landmark `#leparcours` · sticky/fixed elements: `1`
- **Step 07** (`y=13600px`, `61%`): Active landmark `LE WEEKEND` · sticky/fixed elements: `1`
- **Step 08** (`y=14400px`, `65%`): Active landmark `LE WEEKEND` · sticky/fixed elements: `1`

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-gravelleduparc-com (Gravelle du Parc · Événement gravel bike — 2-4 octobre 2026)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-gravelleduparc-com` (**Gravelle du Parc · Événement gravel bike — 2-4 octobre 2026** — `https://www.gravelleduparc.com/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#fffbf0` canvas, `#000000` ink, `#0000ee` accent).
- **Identity & Domain Context**: La Gravelle du Parc, c’est un week-end de gravel : vélo de gravelle le samedi, course à pied le dimanche. Plusieurs distances, expérience...
- **Primary Substrate**: `#fffbf0` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#000000`, **Accent / Highlight**: `#0000ee`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#fffbf0` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#000000` primary typography and `#0000ee` accents.
  - **Grounded Typographic Hierarchy**: Pairs `PP Frama Regular` for display copy (`GRAVELLE DU PARC`) with `PP Frama Regular Placeholder`.
  - **Calibrated Spatial Grid & Motion**: Combines `1408px` container bounds (`gap: 16px`, padding `2px`) with `cubic-bezier(0.44,0,0.56,1)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-gravelleduparc-com` in your global stylesheet:

:root {
  /* Gravelle du Parc · Événement gravel bike — 2-4 octobre 2026 (www-gravelleduparc-com) — Live-Grounded CSS Variables */
  --token-a5ac08d3-da39-4d23-ae40-d4bbcd8e3fd1: #fffbf0; /* Color / Atmospheric Token (www-gravelleduparc-com) */
  --token-801dfdec-b31d-4dcb-87a3-9e0e817b84a0: #cca7e4; /* Color / Atmospheric Token (www-gravelleduparc-com) */
  --token-b73f07c2-b1d7-4a83-b30a-c43c65cbb498: #15663c; /* Color / Atmospheric Token (www-gravelleduparc-com) */
  --token-5eaeb86f-8e78-453e-95cb-73c07bed6a1e: #baf1c5; /* Color / Atmospheric Token (www-gravelleduparc-com) */
  --token-955bd1bf-f5bd-48e1-aa7a-184730d5a46a: #a980c4; /* Color / Atmospheric Token (www-gravelleduparc-com) */
  --token-819cd3c1-358d-4fbc-829d-c778243cf65a: #7ede92; /* Color / Atmospheric Token (www-gravelleduparc-com) */
  --token-59b8ee6e-2d8c-4453-b6ce-0800b1668299: #f8efda; /* Color / Atmospheric Token (www-gravelleduparc-com) */
  --token-e2fce9db-4f7d-4508-8af5-6e27334c8d93: #f7ebff; /* Color / Atmospheric Token (www-gravelleduparc-com) */
  --token-9e8de558-3943-41e7-b539-eba07384897f: #59396e; /* Color / Atmospheric Token (www-gravelleduparc-com) */
  --token-ebd8e842-7d03-4da2-a324-48cca40569ff: #84ba8f; /* Color / Atmospheric Token (www-gravelleduparc-com) */
  --token-9a333514-96bd-43a4-9d9c-387c4eccd2bb: #363229; /* Color / Atmospheric Token (www-gravelleduparc-com) */
  --token-a9a86cd5-8eaf-4794-a1ba-722f2e95e2eb: #dbd0b4; /* Color / Atmospheric Token (www-gravelleduparc-com) */
  --token-394b655e-eb71-48d0-ad1f-647e45a4f590: #f5fbff; /* Color / Atmospheric Token (www-gravelleduparc-com) */
  --token-7271da1b-9f0a-41bd-91b9-d7098d8944de: #efedff; /* Color / Atmospheric Token (www-gravelleduparc-com) */
  --token-3d3e37dc-c784-4b46-95bf-180ff18227e6: #0b0b0b; /* Color / Atmospheric Token (www-gravelleduparc-com) */
  --token-a37e6c3e-a10c-437b-b258-07d1d49555da: #fcebef; /* Color / Atmospheric Token (www-gravelleduparc-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#fffbf0` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#000000` — grounded in live computed `main` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#baf1c5` — grounded in live computed `button` `background-color` (`computed_styles.json`)
- **Interactive Accent / Highlight**: `#0000ee` — grounded in live computed `a` `color` (`computed_styles.json`)
- **Secondary / Muted Copy**: `#15663c` — grounded in live computed `button` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#222222` — grounded in `var(--border-color)` in `:root`
- **Variable Token (`--token-801dfdec-b31d-4dcb-87a3-9e0e817b84a0`)**: `#cca7e4` — grounded in `var(--token-801dfdec-b31d-4dcb-87a3-9e0e817b84a0)` in `:root`
- **Variable Token (`--token-955bd1bf-f5bd-48e1-aa7a-184730d5a46a`)**: `#a980c4` — grounded in `var(--token-955bd1bf-f5bd-48e1-aa7a-184730d5a46a)` in `:root`
- **Variable Token (`--token-819cd3c1-358d-4fbc-829d-c778243cf65a`)**: `#7ede92` — grounded in `var(--token-819cd3c1-358d-4fbc-829d-c778243cf65a)` in `:root`
- **Variable Token (`--token-59b8ee6e-2d8c-4453-b6ce-0800b1668299`)**: `#f8efda` — grounded in `var(--token-59b8ee6e-2d8c-4453-b6ce-0800b1668299)` in `:root`
- **Variable Token (`--token-e2fce9db-4f7d-4508-8af5-6e27334c8d93`)**: `#f7ebff` — grounded in `var(--token-e2fce9db-4f7d-4508-8af5-6e27334c8d93)` in `:root`
- **Variable Token (`--token-9e8de558-3943-41e7-b539-eba07384897f`)**: `#59396e` — grounded in `var(--token-9e8de558-3943-41e7-b539-eba07384897f)` in `:root`
- **Variable Token (`--token-ebd8e842-7d03-4da2-a324-48cca40569ff`)**: `#84ba8f` — grounded in `var(--token-ebd8e842-7d03-4da2-a324-48cca40569ff)` in `:root`
- **Variable Token (`--token-9a333514-96bd-43a4-9d9c-387c4eccd2bb`)**: `#363229` — grounded in `var(--token-9a333514-96bd-43a4-9d9c-387c4eccd2bb)` in `:root`
- **Variable Token (`--token-a9a86cd5-8eaf-4794-a1ba-722f2e95e2eb`)**: `#dbd0b4` — grounded in `var(--token-a9a86cd5-8eaf-4794-a1ba-722f2e95e2eb)` in `:root`
- **Variable Token (`--token-394b655e-eb71-48d0-ad1f-647e45a4f590`)**: `#f5fbff` — grounded in `var(--token-394b655e-eb71-48d0-ad1f-647e45a4f590)` in `:root`
- **Variable Token (`--token-7271da1b-9f0a-41bd-91b9-d7098d8944de`)**: `#efedff` — grounded in `var(--token-7271da1b-9f0a-41bd-91b9-d7098d8944de)` in `:root`
- **Variable Token (`--token-3d3e37dc-c784-4b46-95bf-180ff18227e6`)**: `#0b0b0b` — grounded in `var(--token-3d3e37dc-c784-4b46-95bf-180ff18227e6)` in `:root`
- **Variable Token (`--token-a37e6c3e-a10c-437b-b258-07d1d49555da`)**: `#fcebef` — grounded in `var(--token-a37e6c3e-a10c-437b-b258-07d1d49555da)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1280×6624px` (multi-frame vertical journey filmstrip (6624px), `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2616px` (multi-frame vertical journey filmstrip (2616px), `390px` standard mobile width).
- **Container Max-Width**: `1408px` (measured widest bounded `<section>` landmark width on `1440px` desktop)
- **Padding & Gutters**: `2px` lateral canvas padding with `16px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1408px`, `gap: 16px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `2px` horizontal padding
- **Media Queries**: `@media screen`, `@media screen and (forced-colors:active)`, `@media screen and (forced-colors:active) and (prefers-color-sche...`, `@media (prefers-reduced-motion:reduce)`
- **Corner Radii**: `10px`, `50%`, `4px`, `12px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `PP Frama Regular`
- **Body Font Stack**: `PP Frama Regular Placeholder`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **H1 Display Rule**: live computed `h1` (`font-size: 112px`, `line-height: 112px`, `font-weight: 400`); rule `h1` (`font-size: calc(var(--framer-root-font-s...`, `line-height: 1em`, `letter-spacing: 0em`, `font-weight: 400`)
- **H2 Section Rule**: live computed `h2` (`font-size: 80px`, `line-height: 96px`, `font-weight: 400`); rule `h2` (`font-size: calc(var(--framer-root-font-s...`, `line-height: 1.2em`, `letter-spacing: 0em`, `font-weight: 400`)
- **Body Copy Rule**: live computed `body` (`font-size: 12px`, `line-height: normal`, `font-weight: 400`); rule `p` (`font-size: calc(var(--framer-root-font-s...`, `line-height: 1.2em`, `letter-spacing: 0em`, `font-weight: 700`)
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 12px`, `line-height: normal`, `font-weight: 400`); CSS variables `--letter-spacing: var(--framer-letter-spacing)`

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-gravelleduparc-com` (`Gravelle du Parc · Événement gravel bike — 2-4 octobre 2026`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.lenis> — `www-gravelleduparc-com`)**:
   - DOM & Selectors: Landmark `<header class="lenis">` (`437x113px`) hosting `Gravelle du Parc · Événement gravel ` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-framer-font-css`, `data-framer-breakpoint-css`, `data-framer-css-ssr-minified`, `data-framer-components="framer-lib-cursors-ho..."`), and stylesheet rule `html.lenis body { height: auto; }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.lenis> — `www-gravelleduparc-com`)` (`www-gravelleduparc-com`) adapts across `@media screen`, `@media screen and (forced-colors:active)`, `@media screen and (forced-colors:active) and (prefers-color-sche...`, `@media (prefers-reduced-motion:reduce)` with `cubic-bezier(0.44,0,0.56,1)` transitions and links `Overview · Index · Archive · About · Contact`.
2. **Hero Stage & Focal Lead (<section.framer-3c888> — `GRAVELLE DU PARC`)**:
   - DOM & Selectors: Landmark `<section class="framer-3c888">` presenting display lead `GRAVELLE DU PARC` and copy excerpt *"2–4 octobre 2026 · Wakefield, QC"* over `#fffbf0` canvas and `#000000` ink.
   - Responsive Contract: Hero stage (`1280×6624px` desktop / `390×2616px` mobile) sets `#fffbf0` background with `#000000` headline `GRAVELLE DU PARC`.
3. **Primary Showcase & Content Grid (<section.framer-1qtcgda> — `Ils seront là! Et toi?`)**:
   - DOM & Selectors: Landmark `<section class="framer-1qtcgda">` rendering section `Ils seront là! Et toi?` with copy *"Découvrir l'événement"*, asset references (`iM7hUimGereN8t0VwJyHekeIY.png`, `kPdF8fyktsGL7BKiYVgEs0g8Ozg.png`, `BPKxeJbv6FMQXmeKTCEyN570iaI.png`, `hls.min.js`), and grid rule `.lenis-stopped { overflow: clip; }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.framer-1qtcgda> — `Ils seront là! Et toi?`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1408px`, `gap: 16px`) on desktop and Single-column vertical stack at `390px` viewport width with `2px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.framer-597gjk> — `Les expériences`)**:
   - DOM & Selectors: Landmark `<section class="framer-597gjk">` framing `Les expériences` and `Commanditaire` (*"S'inscrire maintenant"*) with `#baf1c5` surface cards, `#0000ee` accents, and `.lenis.lenis-smooth iframe { pointer-events: none; }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.framer-597gjk> — `Les expériences`)` uses `10px`, `50%`, `4px`, `12px` radii, `#0000ee` highlights, and assets (iM7hUimGereN8t0VwJyHekeIY.png, kPdF8fyktsGL7BKiYVgEs0g8Ozg.png, BPKxeJbv6FMQXmeKTCEyN570iaI.png).
5. **Colophon & Global Directory Footer (<footer.framer-17xvneb-container> — `https://www.gravelleduparc.com/`)**:
   - DOM & Selectors: Landmark `<footer class="framer-17xvneb-container">` anchoring `Gravelle du Parc · Événement gra` footer links (`Overview · Index · Archive · About · Contact`), copy *"Gravelle du Parc c'est pas juste une course. C'est un weeken"*, and `#222222` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.framer-17xvneb-container> — `https://www.gravelleduparc.com/`)` aligns to `1408px` (measured widest bounded `<section>` landmark width on `1440px` desktop) with `2px` lateral canvas padding with `16px` grid gap and attributes (data-framer-font-css, data-framer-breakpoint-css, data-framer-css-ssr-minified).

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"2–4 octobre 2026 · Wakefield, QC"*
- Copy Excerpt 2: *"Découvrir l'événement"*
- Copy Excerpt 3: *"S'inscrire maintenant"*
- Copy Excerpt 4: *"Gravelle du Parc c'est pas juste une course. C'est un weekend complet dans ce que..."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.44,0,0.56,1)`
- **Extracted Stylesheet Rules (`www-gravelleduparc-com`)**:
- `html.lenis body { height: auto; }`
- `.lenis-stopped { overflow: clip; }`
- `.lenis.lenis-smooth iframe { pointer-events: none; }`
- `.lenis.lenis-autoToggle { transition-property: overflow; transition-duration: 1ms; transition-beha... }`
- `.icon-align-center-horizontal:before { content: "\eb1b"; }`
- **Per-Selector Transition Rules**:
- **Selector `.lenis.lenis-autoToggle`**: `transition: 1ms` extracted from `www-gravelleduparc-com` stylesheet.
- **Selector `.swiper-wrapper`**: `transition: var(--swiper-wrapper-transition-timing-function,initial)` extracted from `www-gravelleduparc-com` stylesheet.
- **Selector `.swiper-pagination`**: `transition: opacity .3s` extracted from `www-gravelleduparc-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.44,0,0.56,1)`)**: Governs interactive state transitions across `<header.lenis>` and `<section.framer-1qtcgda>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Swiper Touch Carousel Engine, Framer Motion Layout Physics with `prefers-reduced-motion: reduce` fallback guards.
### 7b. Full-Page Scroll Choreography, Interactive States & Multi-Page Routes
- **Scroll Mechanics**: Implement `native` vertical progression up to `23080px` across 8 distinct viewport chapters using Lenis, GSAP/ScrollTrigger, Framer Motion.
- **Vertical Chapter Sequence**: GRAVELLE DU PARC (0%) -> #video (4%) -> #levenement (16%) -> #schedule (28%) -> Les expériences (39%) -> #leparcours (50%) -> LE WEEKEND (61%) -> LE WEEKEND (65%).

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-gravelleduparc-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
---

## 8. Full-Page Scroll Journey, Interactive States & Subpage Inventory

### Desktop Scroll Keyframes (`1440×900` WebP)
| Step | Scroll Y | Progress | Active Landmark / Section | Sticky/Fixed | Visual Asset |
| :---: | :---: | :---: | :--- | :---: | :--- |
| `#01` | `0px` | `0%` | GRAVELLE DU PARC | `1` | [desktop-step-01.webp](assets/desktop-step-01.webp) |
| `#02` | `850px` | `4%` | #video | `2` | [desktop-step-02.webp](assets/desktop-step-02.webp) |
| `#03` | `3400px` | `16%` | #levenement | `2` | [desktop-step-03.webp](assets/desktop-step-03.webp) |
| `#04` | `5950px` | `28%` | #schedule | `4` | [desktop-step-04.webp](assets/desktop-step-04.webp) |
| `#05` | `8500px` | `39%` | Les expériences | `1` | [desktop-step-05.webp](assets/desktop-step-05.webp) |
| `#06` | `11050px` | `50%` | #leparcours | `1` | [desktop-step-06.webp](assets/desktop-step-06.webp) |
| `#07` | `13600px` | `61%` | LE WEEKEND | `1` | [desktop-step-07.webp](assets/desktop-step-07.webp) |
| `#08` | `14400px` | `65%` | LE WEEKEND | `1` | [desktop-step-08.webp](assets/desktop-step-08.webp) |

### Mobile Condensed Keyframes (`390×844` WebP)
| Step | Scroll Y | Progress | Active Landmark | Visual Asset |
| :---: | :---: | :---: | :--- | :--- |
| `#01` | `0px` | `0%` | GRAVELLE DU PARC | [mobile-step-01.webp](assets/mobile-step-01.webp) |
| `#02` | `7200px` | `50%` | Les expériences | [mobile-step-02.webp](assets/mobile-step-02.webp) |
| `#03` | `14400px` | `100%` | Commanditaire | [mobile-step-03.webp](assets/mobile-step-03.webp) |

