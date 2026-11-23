---
title: "UI Prompt Blueprint: gallery-play-be"
date: 2026-11-23
captured_at: 2026-11-23
target: "gallery-play-be"
status: analyzed
capture: live
capture_desktop: live
capture_mobile: live
capture_tier: tier1_fast
http_status: 200
archetype: "Dark-Substrate WebGL / Canvas Interactive Experience (`#1e1e1e` / `#ff3700`)"
---

# UI Design System & Master Generation Blueprint: gallery-play-be

> **Home - Gallery Play** (https://gallery-play.be/) — We craft bold campaigns, authentic stories and premium collaborations that move sport and culture forward.

![Desktop Viewport Capture (1440x2400)](assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Home - Gallery Play** (`https://gallery-play.be/`). We craft bold campaigns, authentic stories and premium collaborations that move sport and culture forward.
- **Capture Provenance**: Live browser capture (`tier1_fast`, HTTP `200`, captured `2026-11-23`).
- **Visual Archetype**: **Dark-Substrate WebGL / Canvas Interactive Experience (`#1e1e1e` / `#ff3700`)**.
- **Anti-AI-Slop Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#1e1e1e` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#ffffff` primary typography and `#ff3700` accents.
  - **Grounded Typographic Hierarchy**: Pairs `PP Telegraf` for display copy (`CULTURE-SHIFTING CREATIVITY FOR THE `) with `PP Telegraf` and `Inconsolata`.
  - **Calibrated Spatial Grid & Motion**: Combines `1800px` container bounds (`gap: .5rem`, padding `10px`) with `cubic-bezier(0.44,0.96,0.5,0.98)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×2400px` (`assets/desktop.png`, clamped at 2400px live multi-section capture), Mobile `390×2400px` (`assets/mobile.png`, clamped at 2400px live multi-section capture).
- **Master Container Bounds**: `1800px` (non-`@media` desktop container stylesheet rule).
- **Canvas Lateral Padding & Spacing**: `10px` lateral canvas padding with `.5rem` grid gap.
- **Border Radius Scale**: `4px`, `3px`, `var(--border-radius)`, `2px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1800px`, `gap: .5rem`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `10px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width:1024px)`, `@media (max-width:767px)`, `@media (max-width:576px)`, `@media (min-width:768px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#1e1e1e` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#55595c` | `on-dropdown ul.menu li.current-... { background: #55595c }` |
| **Interactive Accent / Highlight** | `#ff3700` | `var(--gradient-5)` in `:root` |
| **Secondary / Muted Copy** | `#cc3366` | live computed `a` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#f2f2f2` | `var(--cmplz_banner_border_color)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--direction-multiplier` | `1` | Design System Custom Token |
| `--page-title-display` | `block` | Design System Custom Token |
| `--cmplz_banner_width` | `526px` | Layout / Spatial Grid Token |
| `--cmplz_banner_background_color` | `#ffffff` | Canvas / Surface Token |
| `--cmplz_banner_border_color` | `#f2f2f2` | Brand / Palette Token |
| `--cmplz_banner_border_width` | `0px 0px 0px 0px` | Layout / Spatial Grid Token |
| `--cmplz_banner_border_radius` | `0px 0px 0px 0px` | Elevation / Border Token |
| `--cmplz_banner_margin` | `10px` | Layout / Spatial Grid Token |
| `--cmplz_categories-height` | `163px` | Layout / Spatial Grid Token |
| `--cmplz_title_font_size` | `15px` | Typography / Scale Token |
| `--cmplz_text_line_height` | `calc(var(--cmplz_text_font_size) * 1.5)` | Typography Ink Token |
| `--cmplz_text_color` | `#1e1e1e` | Typography Ink Token |
| `--cmplz_hyperlink_color` | `#1e1e1e` | Typography Ink Token |
| `--cmplz_text_font_size` | `12px` | Typography Ink Token |
| `--cmplz_link_font_size` | `12px` | Typography Ink Token |
| `--cmplz_category_body_font_size` | `12px` | Typography / Scale Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `PP Telegraf`.
- **Primary Body Stack**: `PP Telegraf`.
- **Technical / Metadata Stack**: `Inconsolata`.

### Typographic Scale & Rules (Live Computed & Stylesheet Grounded)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 64px`, `line-height: 57.6px`, `font-weight: 700`); CSS variables `--page-title-display: block`, `--display: flex`; rule `h1` (`font-size: var( --e-global-typography-pr...`, `line-height: var( --e-global-typog...`, `font-weight: var( --e-glob...`).
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 32px`, `line-height: 28.8px`, `font-weight: 700`); rule `h2` (`font-size: 32px`, `line-height: 0.9em`, `font-weight: 400`).
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 20px`, `font-weight: 300`); CSS variables `--cmplz_category_body_font_size: 12px`.
- **Metadata & Navigation Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 20px`, `font-weight: 300`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(0.44,0.96,0.5,0.98)`, `cubic-bezier(0.26,0.69,0.37,0.96)`, `cubic-bezier(0.83,0.08,0.16,0.97)`.

### Per-Element Transition & Choreography Rules
- **Selector `-holder .site-navigation-toggle-i...`**: `transition: all .2s ease-in-out` extracted from `gallery-play-be` stylesheet.
- **Selector `.site-navigation-dropdown`**: `transition: max-height .3s,transform .3s` extracted from `gallery-play-be` stylesheet.
- **Selector `.site-navigation-dropdown ul.menu...`**: `transition: max-height .3s,transform .3s` extracted from `gallery-play-be` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.44,0.96,0.5,0.98)`)**: Governs interactive state transitions across `<header.elementor>` and `<main.post-15>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine, Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic — Desktop (`1440px`, Grounded in `dom.html` & Landmark Bounding Boxes)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Home - Gallery Play                        │
│ ====================================================================== │
│ [ <header.elementor> (1440x0px)       | Projects · Services · Athlet ] │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <main.site-main> (w=1440px)                            | │
│ | H1: CULTURE-SHIFTING CREATIVITY FOR THE WORLD OF SPORTS            | │
│ | Substrate: #1e1e1e | Ink: #ffffff | Accent: #ff3700                | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<main.post-15>) max-w: 1800px                       | │
│ | +------------------------------+  +------------------------------+ | │
│ | | Culture-shifting creativity  |  | Rooted in top-level football | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | DETAIL MODULE (<main.page>) — Work that speaks loud                | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.elementor>  ) | https://gallery-play.be/             │
└────────────────────────────────────────────────────────────────────────┘
```

### Visual Layout Schematic — Mobile Reflow (`390px`)
```
┌────────────────────────────────────────────────────────────────────────┐
│ MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: .5rem)      │
│ ====================================================================== │
│ [ HEADER BAR (<header.elementor>      ) | Compact Menu (390px)         │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE (<main.site-main>) — 390px Vertical Lead                | │
│ | H1: CULTURE-SHIFTING CREATIVITY FOR THE WORLD OF SPORTS            | │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE STACK (<main.post-15>) — 1-Col Stack                      | │
│ | [ Item 1: Culture-shifting creativity for the world of sports    ] | │
│ | [ Item 2: Rooted in top-level football, fluent in branding,...   ] | │
│ ---------------------------------------------------------------------- │
│ | DETAIL STACK (<main.page>) — 1-Col (Work that speaks l)            | │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.elementor>  ) | Stacked 390px Colophon               │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.elementor> — `gallery-play-be`)**:
   - Landmark `<header class="elementor elementor-100">` (`1440x0px`) hosting `Home - Gallery Play` navigation (`Projects · Services · Athletes · Team · Contact`), DOM attributes (`data-mp="true"`, `data-cfasync="false"`, `data-mp="true"`, `data-cfasync="false"`), and stylesheet rule `.elementor-kit-5 e-page-transition { background-color:FFBC7D; }`.
2. **Hero Stage & Focal Lead (<main.site-main> — `CULTURE-SHIFTING CREATIVITY FOR TH`)**:
   - Landmark `<main class="site-main post-15">` presenting display lead `CULTURE-SHIFTING CREATIVITY FOR THE WORLD OF SPORTS` and copy excerpt *"We craft bold campaigns, authentic stories and premium collaborat"* over `#1e1e1e` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<main.post-15> — `Culture-shifting creativity for th`)**:
   - Landmark `<main class="site-main post-15">` rendering section `Culture-shifting creativity for the world of sports` with copy *"Start the conversation"*, asset references (`player.js`, `recaptcha__en.js`, `embed`, `cookieblocker.min.css`), and grid rule `or-section-boxed > .elementor-con... { max-width:1800px; }`.
4. **Interactive Detail & Feature Matrix (<main.page> — `Rooted in top-level football, flue`)**:
   - Landmark `<main class="site-main post-15">` framing `Rooted in top-level football, fluent in branding,...` and `Work that speaks louder than words.` (*"From shirt launches and transfer announcements to player branding"*) with `#55595c` surface cards, `#ff3700` accents, and `.elementor-element { --widgets-spacing:0px 0px;--widgets-spacing-row:0px;--widgets-spacing-co... }`.
5. **Colophon & Global Directory Footer (<footer.elementor> — `https://gallery-play.be/`)**:
   - Landmark `<footer class="elementor elementor-102">` anchoring `Home - Gallery Play` footer links (`Projects · Services · Athletes · Team · Contact`), copy *"We tailor every collaboration to the client. Brands, athlete"*, and `#f2f2f2` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: gallery-play-be (Home - Gallery Play)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `gallery-play-be` (**Home - Gallery Play** — `https://gallery-play.be/`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#1e1e1e` / `#ff3700`).
- **Identity & Domain Context**: We craft bold campaigns, authentic stories and premium collaborations that move sport and culture forward.
- **Primary Substrate**: `#1e1e1e` (live computed `body` `background-color` (`computed_styles.json`)), **Primary Ink**: `#ffffff`, **Accent / Highlight**: `#ff3700`.
- **Site-Specific Differentiators**:
  - **Live-Computed Chromatic Polarity**: Anchors the viewport in `#1e1e1e` (live computed `body` `background-color` (`computed_styles.json`)) paired with `#ffffff` primary typography and `#ff3700` accents.
  - **Grounded Typographic Hierarchy**: Pairs `PP Telegraf` for display copy (`CULTURE-SHIFTING CREATIVITY FOR THE `) with `PP Telegraf` and `Inconsolata`.
  - **Calibrated Spatial Grid & Motion**: Combines `1800px` container bounds (`gap: .5rem`, padding `10px`) with `cubic-bezier(0.44,0.96,0.5,0.98)` easing and Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `gallery-play-be` in your global stylesheet:

:root {
  /* Home - Gallery Play (gallery-play-be) — Live-Grounded CSS Variables */
  --direction-multiplier: 1; /* Design System Custom Token (gallery-play-be) */
  --page-title-display: block; /* Design System Custom Token (gallery-play-be) */
  --cmplz_banner_width: 526px; /* Layout / Spatial Grid Token (gallery-play-be) */
  --cmplz_banner_background_color: #ffffff; /* Canvas / Surface Token (gallery-play-be) */
  --cmplz_banner_border_color: #f2f2f2; /* Brand / Palette Token (gallery-play-be) */
  --cmplz_banner_border_width: 0px 0px 0px 0px; /* Layout / Spatial Grid Token (gallery-play-be) */
  --cmplz_banner_border_radius: 0px 0px 0px 0px; /* Elevation / Border Token (gallery-play-be) */
  --cmplz_banner_margin: 10px; /* Layout / Spatial Grid Token (gallery-play-be) */
  --cmplz_categories-height: 163px; /* Layout / Spatial Grid Token (gallery-play-be) */
  --cmplz_title_font_size: 15px; /* Typography / Scale Token (gallery-play-be) */
  --cmplz_text_line_height: calc(var(--cmplz_text_font_size) * 1.5); /* Typography Ink Token (gallery-play-be) */
  --cmplz_text_color: #1e1e1e; /* Typography Ink Token (gallery-play-be) */
  --cmplz_hyperlink_color: #1e1e1e; /* Typography Ink Token (gallery-play-be) */
  --cmplz_text_font_size: 12px; /* Typography Ink Token (gallery-play-be) */
  --cmplz_link_font_size: 12px; /* Typography Ink Token (gallery-play-be) */
  --cmplz_category_body_font_size: 12px; /* Typography / Scale Token (gallery-play-be) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#1e1e1e` — grounded in live computed `body` `background-color` (`computed_styles.json`)
- **Primary Typography Ink**: `#ffffff` — grounded in live computed `h1` `color` (`computed_styles.json`)
- **Elevated Surface / Card Substrate**: `#55595c` — grounded in `on-dropdown ul.menu li.current-... { background: #55595c }`
- **Interactive Accent / Highlight**: `#ff3700` — grounded in `var(--gradient-5)` in `:root`
- **Secondary / Muted Copy**: `#cc3366` — grounded in live computed `a` `color` (`computed_styles.json`)
- **Structural Hairline Border**: `#f2f2f2` — grounded in `var(--cmplz_banner_border_color)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×2400px` (clamped at 2400px live multi-section capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (clamped at 2400px live multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `1800px` (non-`@media` desktop container stylesheet rule)
- **Padding & Gutters**: `10px` lateral canvas padding with `.5rem` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1800px`, `gap: .5rem`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `10px` horizontal padding
- **Media Queries**: `@media (max-width:1024px)`, `@media (max-width:767px)`, `@media (max-width:576px)`, `@media (min-width:768px)`
- **Corner Radii**: `4px`, `3px`, `var(--border-radius)`, `2px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `PP Telegraf`
- **Body Font Stack**: `PP Telegraf`
- **Monospace / Technical Font Stack**: `Inconsolata`
- **H1 Display Rule**: live computed `h1` (`font-size: 64px`, `line-height: 57.6px`, `font-weight: 700`); CSS variables `--page-title-display: block`, `--display: flex`; rule `h1` (`font-size: var( --e-global-typography-pr...`, `line-height: var( --e-global-typog...`, `font-weight: var( --e-glob...`)
- **H2 Section Rule**: live computed `h2` (`font-size: 32px`, `line-height: 28.8px`, `font-weight: 700`); rule `h2` (`font-size: 32px`, `line-height: 0.9em`, `font-weight: 400`)
- **Body Copy Rule**: live computed `body` (`font-size: 16px`, `line-height: 20px`, `font-weight: 300`); CSS variables `--cmplz_category_body_font_size: 12px`
- **Metadata & Index Rule**: live computed `nav/a` (`font-size: 16px`, `line-height: 20px`, `font-weight: 300`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `gallery-play-be` (`Home - Gallery Play`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.elementor> — `gallery-play-be`)**:
   - DOM & Selectors: Landmark `<header class="elementor elementor-100">` (`1440x0px`) hosting `Home - Gallery Play` navigation (`Projects · Services · Athletes · Team · Contact`), DOM attributes (`data-mp="true"`, `data-cfasync="false"`, `data-mp="true"`, `data-cfasync="false"`), and stylesheet rule `.elementor-kit-5 e-page-transition { background-color:FFBC7D; }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.elementor> — `gallery-play-be`)` (`gallery-play-be`) adapts across `@media (max-width:1024px)`, `@media (max-width:767px)`, `@media (max-width:576px)`, `@media (min-width:768px)` with `cubic-bezier(0.44,0.96,0.5,0.98)`, `cubic-bezier(0.26,0.69,0.37,0.96)`, `cubic-bezier(0.83,0.08,0.16,0.97)` transitions and links `Projects · Services · Athletes · Team · Contact`.
2. **Hero Stage & Focal Lead (<main.site-main> — `CULTURE-SHIFTING CREATIVITY FOR TH`)**:
   - DOM & Selectors: Landmark `<main class="site-main post-15">` presenting display lead `CULTURE-SHIFTING CREATIVITY FOR THE WORLD OF SPORTS` and copy excerpt *"We craft bold campaigns, authentic stories and premium collaborat"* over `#1e1e1e` canvas and `#ffffff` ink.
   - Responsive Contract: Hero stage (`1440×2400px` desktop / `390×2400px` mobile) sets `#1e1e1e` background with `#ffffff` headline `CULTURE-SHIFTING CREATIVITY FOR THE WORLD OF SPORTS`.
3. **Primary Showcase & Content Grid (<main.post-15> — `Culture-shifting creativity for th`)**:
   - DOM & Selectors: Landmark `<main class="site-main post-15">` rendering section `Culture-shifting creativity for the world of sports` with copy *"Start the conversation"*, asset references (`player.js`, `recaptcha__en.js`, `embed`, `cookieblocker.min.css`), and grid rule `or-section-boxed > .elementor-con... { max-width:1800px; }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<main.post-15> — `Culture-shifting creativity for th`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: 1800px`, `gap: .5rem`) on desktop and Single-column vertical stack at `390px` viewport width with `10px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<main.page> — `Rooted in top-level football, flue`)**:
   - DOM & Selectors: Landmark `<main class="site-main post-15">` framing `Rooted in top-level football, fluent in branding,...` and `Work that speaks louder than words.` (*"From shirt launches and transfer announcements to player branding"*) with `#55595c` surface cards, `#ff3700` accents, and `.elementor-element { --widgets-spacing:0px 0px;--widgets-spacing-row:0px;--widgets-spacing-co... }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<main.page> — `Rooted in top-level football, flue`)` uses `4px`, `3px`, `var(--border-radius)`, `2px` radii, `#ff3700` highlights, and assets (player.js, recaptcha__en.js, embed).
5. **Colophon & Global Directory Footer (<footer.elementor> — `https://gallery-play.be/`)**:
   - DOM & Selectors: Landmark `<footer class="elementor elementor-102">` anchoring `Home - Gallery Play` footer links (`Projects · Services · Athletes · Team · Contact`), copy *"We tailor every collaboration to the client. Brands, athlete"*, and `#f2f2f2` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.elementor> — `https://gallery-play.be/`)` aligns to `1800px` (non-`@media` desktop container stylesheet rule) with `10px` lateral canvas padding with `.5rem` grid gap and attributes (data-mp="true", data-cfasync="false", data-mp="true").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"We craft bold campaigns, authentic stories and premium collaborations that move sp..."*
- Copy Excerpt 2: *"Start the conversation"*
- Copy Excerpt 3: *"From shirt launches and transfer announcements to player branding and cultural col..."*
- Copy Excerpt 4: *"We tailor every collaboration to the client. Brands, athletes, clubs and federations."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(0.44,0.96,0.5,0.98)`, `cubic-bezier(0.26,0.69,0.37,0.96)`, `cubic-bezier(0.83,0.08,0.16,0.97)`
- **Extracted Stylesheet Rules (`gallery-play-be`)**:
- `.elementor-kit-5 e-page-transition { background-color:FFBC7D; }`
- `or-section-boxed > .elementor-con... { max-width:1800px; }`
- `.elementor-element { --widgets-spacing:0px 0px;--widgets-spacing-row:0px;--widgets-spacing-co... }`
- `h1.entry-title { display:var(--page-title-display); }`
- `.site-header .site-branding { flex-direction:column;align-items:stretch; }`
- **Per-Selector Transition Rules**:
- **Selector `-holder .site-navigation-toggle-i...`**: `transition: all .2s ease-in-out` extracted from `gallery-play-be` stylesheet.
- **Selector `.site-navigation-dropdown`**: `transition: max-height .3s,transform .3s` extracted from `gallery-play-be` stylesheet.
- **Selector `.site-navigation-dropdown ul.menu...`**: `transition: max-height .3s,transform .3s` extracted from `gallery-play-be` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(0.44,0.96,0.5,0.98)`)**: Governs interactive state transitions across `<header.elementor>` and `<main.post-15>`.
- **Runtime Interaction Engine**: Integrates Lenis Smooth Scroll (`data-lenis`), GSAP Timeline & ScrollTrigger, Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine, Lottie Vector Animation Player with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `gallery-play-be`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
