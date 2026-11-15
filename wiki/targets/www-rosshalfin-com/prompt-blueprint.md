---
title: "UI Prompt Blueprint: www-rosshalfin-com"
date: 2026-11-15
target: "[[overview|www-rosshalfin-com]]"
status: analyzed
archetype: "Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#161618` ink, `#161618` accent)"
---

# UI Design System & Master Generation Blueprint: www-rosshalfin-com

> **Ross Halfin Photography · Music Images + Fine Art Prints** (https://www.rosshalfin.com) — Unparalleled music photography by Ross Halfin - Limited edition Fine-Art prints, signed & embossed. Worldwide shipping

![Desktop Viewport Capture (1440x5728)](file:///root/projects/fleet/wiki/targets/www-rosshalfin-com/assets/desktop.png)

---

## 1. Executive Visual Persona & Design Archetype

- **Brand Essence & Persona**: **Ross Halfin Photography · Music Images + Fine Art Prints** (`https://www.rosshalfin.com`). Unparalleled music photography by Ross Halfin - Limited edition Fine-Art prints, signed & embossed. Worldwide shipping
- **Visual Archetype**: **Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#161618` ink, `#161618` accent)**.
- **Anti-AI-Slop Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#ffffff` (`var(--cmplz_banner_background_color)` in `:root`) paired with `#161618` primary typography and `#161618` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Barlow Semi Condensed` for display copy (`Welcome To Ross Halfin Photography`) with `Barlow` and `IBM Plex Sans`.
  - **Calibrated Spatial Grid & Motion**: Combines `var(--wp--style--global--wide-size)` container bounds (`gap: 30px`, padding `3px`) with `cubic-bezier(.33,0,.2,1)` easing and Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine.

---

## 2. Spatial Architecture & Modular Grid Mathematics

![Mobile Viewport Capture (390x2400)](file:///root/projects/fleet/wiki/targets/www-rosshalfin-com/assets/mobile.png)

### Viewport Allocation & Container Geometry
- **Captured Viewport Dimensions**: Desktop `1440×5728px` (`assets/desktop.png`, full-page scroll capture), Mobile `390×2400px` (`assets/mobile.png`, capped at 2400px multi-section capture).
- **Master Container Bounds**: `var(--wp--style--global--wide-size)` extracted from `www-rosshalfin-com` stylesheet.
- **Canvas Lateral Padding & Spacing**: `3px` lateral canvas padding with `30px` grid gap.
- **Border Radius Scale**: `3px`, `4px`, `6px`, `2px`.

### Responsive Breakpoint Architecture
- **Desktop Layout**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: var(--wp--style--global--wide-size)`, `gap: 30px`).
- **Mobile Layout**: Single-column vertical stack at `390px` viewport width with `3px` horizontal padding.
- **Extracted CSS Media Queries**: `@media (max-width:1099px)`, `@media (min-width:481px) and (max-width:600px)`, `@media (min-width:993px)`, `@media (max-width:992px)`.

---

## 3. Color System, Materiality & Atmospheric Lighting

### Semantic Palette & Source Grounding
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | `var(--cmplz_banner_background_color)` in `:root` |
| **Primary Typography Ink** | `#f2f2f2` | `var(--cmplz_banner_border_color)` in `:root` |
| **Elevated Surface / Card Substrate** | `#222222` | `var(--cmplz_text_color)` in `:root` |
| **Interactive Accent / Highlight** | `#161618` | `var(--cmplz_hyperlink_color)` in `:root` |
| **Secondary / Muted Copy** | `#f9f9f9` | `var(--cmplz_button_deny_background_color)` in `:root` |
| **Structural Hairline Border** | `#333333` | `var(--cmplz_button_settings_text_color)` in `:root` |

### Sanitized Root CSS Variables (`ui-ux.md` Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--cmplz_banner_width` | `490px` | Layout / Spatial Grid Token |
| `--cmplz_banner_background_color` | `#ffffff` | Canvas / Surface Token |
| `--cmplz_banner_border_color` | `#f2f2f2` | Brand / Palette Token |
| `--cmplz_banner_border_width` | `0px 0px 0px 0px` | Layout / Spatial Grid Token |
| `--cmplz_banner_border_radius` | `15px 15px 15px 15px` | Elevation / Border Token |
| `--cmplz_banner_margin` | `10px` | Layout / Spatial Grid Token |
| `--cmplz_categories-height` | `216px` | Layout / Spatial Grid Token |
| `--cmplz_title_font_size` | `15px` | Typography / Scale Token |
| `--cmplz_text_line_height` | `calc(var(--cmplz_text_font_size) * 1.5)` | Typography Ink Token |
| `--cmplz_text_color` | `#222222` | Typography Ink Token |
| `--cmplz_hyperlink_color` | `#161618` | Typography Ink Token |
| `--cmplz_text_font_size` | `12px` | Typography Ink Token |
| `--cmplz_link_font_size` | `12px` | Typography Ink Token |
| `--cmplz_category_body_font_size` | `12px` | Typography / Scale Token |
| `--cmplz_button_accept_background_color` | `#161618` | Canvas / Surface Token |
| `--cmplz_button_accept_border_color` | `#161618` | Brand / Palette Token |

---

## 4. Typographic Scale & Editorial Hierarchy

### Font Family Stacks
- **Display Typography**: `Barlow Semi Condensed`.
- **Primary Body Stack**: `Barlow`.
- **Technical / Metadata Stack**: `IBM Plex Sans`.

### Typographic Scale & Rules (Extracted from Stylesheet & Variables)
- **Hero Display (`H1`)**: rule `.title` (`font-size: large`, `font-weight: bold`).
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(1.375rem,.9939rem + 1.2...`, `letter-spacing: -.01em`).
- **Body Copy**: CSS variables `--cmplz_category_body_font_size: 12px`, `--wp--custom--line-height--body: 1.618`; rule `p` (`font-size: 12px`).
- **Metadata & Navigation Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `15px`, `14px`, `11px`, `12px`, `13px`).

---

## 5. Choreographed Motion & Interaction Physics

### Primary Easing Curves
- **Extracted Timing Functions**: `cubic-bezier(.33,0,.2,1)`, `cubic-bezier(.28,.75,.22,.95)`, `cubic-bezier(.4,0,.2,1)`.

### Per-Element Transition & Choreography Rules
- **Selector `.site .wc-block-grid__product`**: `transition: all .2s` extracted from `www-rosshalfin-com` stylesheet.
- **Selector `media (min-width:993px)`**: `transition: all .2s` extracted from `www-rosshalfin-com` stylesheet.
- **Selector `.wc-block-grid__product:hover:before`**: `transition: all .2s` extracted from `www-rosshalfin-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.33,0,.2,1)`)**: Governs interactive state transitions across `<header.site-header>` and `<section.pageSection>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

---

## 6. Component Wireframe & Structural DOM Map

### Visual Layout Schematic (Grounded in `dom.html` — `1440px` Desktop & `390px` Mobile Reflow)
```
┌────────────────────────────────────────────────────────────────────────┐
│ DESKTOP VIEWPORT (1440px) — Ross Halfin Photography · Music Images + F │
│ ====================================================================== │
│ [ <header.site-header>     | € 0.00 0                               ]  │
│ ---------------------------------------------------------------------- │
│ | HERO STAGE: <section.pageSection>                                |   │
│ | H1: Welcome To Ross Halfin Photography                           |   │
│ | Substrate: #ffffff    | Ink: #161618    | Accent: #161618        |   │
│ ---------------------------------------------------------------------- │
│ | SHOWCASE GRID (<section.pageSection>     ) max-w: var(--wp--styl |   │
│ | +------------------------------+  +------------------------------+ | │
│ | | Latest Diaries + Updates     |  | Most Popular Prints          | | │
│ | +------------------------------+  +------------------------------+ | │
│ ---------------------------------------------------------------------- │
│ | MOBILE VIEWPORT REFLOW (390px) — Single-Column Stack (gap: 30px  ) | │
│ | [<header.site-heade] -> [<section.pageSecti] -> [<section.pageSecti] │
│ ---------------------------------------------------------------------- │
│ [ FOOTER (<footer.page-template-) | https://www.rosshalfin.com         │
└────────────────────────────────────────────────────────────────────────┘
```

### Granular DOM Region Breakdown
1. **Brand Header & Navigation Bar (<header.site-header> — `www-rosshalfin-com`)**:
   - Landmark `<header class="site-header">` hosting `Ross Halfin Photography · Music Imag` navigation (`€ 0.00 0`), DOM attributes (`data-partner-attribution-id="PaymentPlugins_PCP"`, `data-uid-auto="uid_znuqasiucahxrfuik..."`, `data-wp-strategy="defer"`, `data-wp-strategy="defer"`), and stylesheet rule `body .is-layout-constrained>.alig... { max-width:var(--wp--style--global--wide-size) }`.
2. **Hero Stage & Focal Lead (<section.pageSection> — `Welcome To Ross Halfin Photography`)**:
   - Landmark `<section class="pageSection home__sec__hl">` presenting display lead `Welcome To Ross Halfin Photography` and copy excerpt *"We use cookies to improve site performance and functionality. You"* over `#ffffff` canvas and `#161618` ink.
3. **Primary Showcase & Content Grid (<section.pageSection> — `Latest Diaries + Updates`)**:
   - Landmark `<section class="pageSection home__sec__latest_news">` rendering section `Latest Diaries + Updates` with copy *"Functional Always active"*, asset references (`clarity.js`, `recaptcha__en.js`, `xmlrpc.php`, `banner-2-optin.css`), and grid rule `.has-text-align-center { text-align:center }`.
4. **Interactive Detail & Feature Matrix (<section.pageSection> — `Most Popular Prints`)**:
   - Landmark `<section class="pageSection home__sec__text">` framing `Most Popular Prints` and `Metallica` (*"Required to enable core site functionality and services you reque"*) with `#222222` surface cards, `#161618` accents, and `.site .wc-block-grid__products { display:grid;gap:30px;margin:0 }`.
5. **Colophon & Global Directory Footer (<footer.page-template-template-homepage> — `https://www.rosshalfin.com`)**:
   - Landmark `<footer class="page-template-template-homepage">` anchoring `Ross Halfin Photography · Music ` footer links (`€ 0.00 0`), copy *"Used to store your preferences, such as language or display "*, and `#333333` structural dividers.

---

## 7. Master Zero-Shot AI Generation Prompt

```markdown
# Master Zero-Shot Frontend Generation Prompt: www-rosshalfin-com (Ross Halfin Photography · Music Images + Fine Art Prints)

You are a principal frontend architect and design systems engineer. Build a complete, production-ready web application replicating the exact design system, DOM landmarks, typographic hierarchy, color tokens, and motion physics of `www-rosshalfin-com` (**Ross Halfin Photography · Music Images + Fine Art Prints** — `https://www.rosshalfin.com`).

### 1. Visual Archetype & Anti-AI-Slop Mandates
- **Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#161618` ink, `#161618` accent).
- **Identity & Domain Context**: Unparalleled music photography by Ross Halfin - Limited edition Fine-Art prints, signed & embossed. Worldwide shipping
- **Primary Substrate**: `#ffffff` (`var(--cmplz_banner_background_color)` in `:root`), **Primary Ink**: `#161618`, **Accent / Highlight**: `#161618`.
- **Site-Specific Differentiators**:
  - **Source-Grounded Chromatic Polarity**: Anchors the viewport in `#ffffff` (`var(--cmplz_banner_background_color)` in `:root`) paired with `#161618` primary typography and `#161618` accents.
  - **Extracted Typographic Hierarchy**: Pairs `Barlow Semi Condensed` for display copy (`Welcome To Ross Halfin Photography`) with `Barlow` and `IBM Plex Sans`.
  - **Calibrated Spatial Grid & Motion**: Combines `var(--wp--style--global--wide-size)` container bounds (`gap: 30px`, padding `3px`) with `cubic-bezier(.33,0,.2,1)` easing and Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine.

### 2. Ground-Truth CSS Variables (`:root` Token Contract)
Declare and consume these exact custom properties extracted from `www-rosshalfin-com` in your global stylesheet:

:root {
  /* Ross Halfin Photography · Music Images + Fine Art Prints (www-rosshalfin-com) — Ground-Truth Extracted CSS Variables */
  --cmplz_banner_width: 490px; /* Layout / Spatial Grid Token (www-rosshalfin-com) */
  --cmplz_banner_background_color: #ffffff; /* Canvas / Surface Token (www-rosshalfin-com) */
  --cmplz_banner_border_color: #f2f2f2; /* Brand / Palette Token (www-rosshalfin-com) */
  --cmplz_banner_border_width: 0px 0px 0px 0px; /* Layout / Spatial Grid Token (www-rosshalfin-com) */
  --cmplz_banner_border_radius: 15px 15px 15px 15px; /* Elevation / Border Token (www-rosshalfin-com) */
  --cmplz_banner_margin: 10px; /* Layout / Spatial Grid Token (www-rosshalfin-com) */
  --cmplz_categories-height: 216px; /* Layout / Spatial Grid Token (www-rosshalfin-com) */
  --cmplz_title_font_size: 15px; /* Typography / Scale Token (www-rosshalfin-com) */
  --cmplz_text_line_height: calc(var(--cmplz_text_font_size) * 1.5); /* Typography Ink Token (www-rosshalfin-com) */
  --cmplz_text_color: #222222; /* Typography Ink Token (www-rosshalfin-com) */
  --cmplz_hyperlink_color: #161618; /* Typography Ink Token (www-rosshalfin-com) */
  --cmplz_text_font_size: 12px; /* Typography Ink Token (www-rosshalfin-com) */
  --cmplz_link_font_size: 12px; /* Typography Ink Token (www-rosshalfin-com) */
  --cmplz_category_body_font_size: 12px; /* Typography / Scale Token (www-rosshalfin-com) */
  --cmplz_button_accept_background_color: #161618; /* Canvas / Surface Token (www-rosshalfin-com) */
  --cmplz_button_accept_border_color: #161618; /* Brand / Palette Token (www-rosshalfin-com) */
}

### 3. Semantic Color & Materiality Contract
Map every surface, ink, and border strictly to these source-grounded tokens:
- **Primary Canvas Substrate**: `#ffffff` — grounded in `var(--cmplz_banner_background_color)` in `:root`
- **Primary Typography Ink**: `#f2f2f2` — grounded in `var(--cmplz_banner_border_color)` in `:root`
- **Elevated Surface / Card Substrate**: `#222222` — grounded in `var(--cmplz_text_color)` in `:root`
- **Interactive Accent / Highlight**: `#161618` — grounded in `var(--cmplz_hyperlink_color)` in `:root`
- **Secondary / Muted Copy**: `#f9f9f9` — grounded in `var(--cmplz_button_deny_background_color)` in `:root`
- **Structural Hairline Border**: `#333333` — grounded in `var(--cmplz_button_settings_text_color)` in `:root`

### 4. Spatial Grid, Container Bounds & Responsive Breakpoints
- **Desktop Viewport Reference**: `1440×5728px` (full-page scroll capture, `1440px` standard desktop width).
- **Mobile Viewport Reference**: `390×2400px` (capped at 2400px multi-section capture, `390px` standard mobile width).
- **Container Max-Width**: `var(--wp--style--global--wide-size)` extracted from `www-rosshalfin-com` stylesheet
- **Padding & Gutters**: `3px` lateral canvas padding with `30px` grid gap
- **Desktop Grid**: Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: var(--wp--style--global--wide-size)`, `gap: 30px`)
- **Mobile Adaptation**: Single-column vertical stack at `390px` viewport width with `3px` horizontal padding
- **Media Queries**: `@media (max-width:1099px)`, `@media (min-width:481px) and (max-width:600px)`, `@media (min-width:993px)`, `@media (max-width:992px)`
- **Corner Radii**: `3px`, `4px`, `6px`, `2px`

### 5. Typography & Editorial Scale Contract
- **Display Font Stack**: `Barlow Semi Condensed`
- **Body Font Stack**: `Barlow`
- **Monospace / Technical Font Stack**: `IBM Plex Sans`
- **H1 Display Rule**: rule `.title` (`font-size: large`, `font-weight: bold`)
- **H2 Section Rule**: rule `h2` (`font-size: clamp(1.375rem,.9939rem + 1.2...`, `letter-spacing: -.01em`)
- **Body Copy Rule**: CSS variables `--cmplz_category_body_font_size: 12px`, `--wp--custom--line-height--body: 1.618`; rule `p` (`font-size: 12px`)
- **Metadata & Index Rule**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `15px`, `14px`, `11px`, `12px`, `13px`)

### 6. Component Hierarchy, Verbatim Copy & Real DOM Landmarks
Scaffold `www-rosshalfin-com` (`Ross Halfin Photography · Music Images + Fine Art Prints`) with these exact structural regions, extracted copy, and CSS rules from `dom.html`:
1. **Brand Header & Navigation Bar (<header.site-header> — `www-rosshalfin-com`)**:
   - DOM & Selectors: Landmark `<header class="site-header">` hosting `Ross Halfin Photography · Music Imag` navigation (`€ 0.00 0`), DOM attributes (`data-partner-attribution-id="PaymentPlugins_PCP"`, `data-uid-auto="uid_znuqasiucahxrfuik..."`, `data-wp-strategy="defer"`, `data-wp-strategy="defer"`), and stylesheet rule `body .is-layout-constrained>.alig... { max-width:var(--wp--style--global--wide-size) }`.
   - Responsive Contract: Header `Brand Header & Navigation Bar (<header.site-header> — `www-rosshalfin-com`)` (`www-rosshalfin-com`) adapts across `@media (max-width:1099px)`, `@media (min-width:481px) and (max-width:600px)`, `@media (min-width:993px)`, `@media (max-width:992px)` with `cubic-bezier(.33,0,.2,1)`, `cubic-bezier(.28,.75,.22,.95)`, `cubic-bezier(.4,0,.2,1)` transitions and links `€ 0.00 0`.
2. **Hero Stage & Focal Lead (<section.pageSection> — `Welcome To Ross Halfin Photography`)**:
   - DOM & Selectors: Landmark `<section class="pageSection home__sec__hl">` presenting display lead `Welcome To Ross Halfin Photography` and copy excerpt *"We use cookies to improve site performance and functionality. You"* over `#ffffff` canvas and `#161618` ink.
   - Responsive Contract: Hero stage (`1440×5728px` desktop / `390×2400px` mobile) sets `#ffffff` background with `#161618` headline `Welcome To Ross Halfin Photography`.
3. **Primary Showcase & Content Grid (<section.pageSection> — `Latest Diaries + Updates`)**:
   - DOM & Selectors: Landmark `<section class="pageSection home__sec__latest_news">` rendering section `Latest Diaries + Updates` with copy *"Functional Always active"*, asset references (`clarity.js`, `recaptcha__en.js`, `xmlrpc.php`, `banner-2-optin.css`), and grid rule `.has-text-align-center { text-align:center }`.
   - Responsive Contract: Showcase grid `Primary Showcase & Content Grid (<section.pageSection> — `Latest Diaries + Updates`)` applies Multi-column CSS Grid / Flexbox layout at `1440px` (`max-width: var(--wp--style--global--wide-size)`, `gap: 30px`) on desktop and Single-column vertical stack at `390px` viewport width with `3px` horizontal padding on mobile.
4. **Interactive Detail & Feature Matrix (<section.pageSection> — `Most Popular Prints`)**:
   - DOM & Selectors: Landmark `<section class="pageSection home__sec__text">` framing `Most Popular Prints` and `Metallica` (*"Required to enable core site functionality and services you reque"*) with `#222222` surface cards, `#161618` accents, and `.site .wc-block-grid__products { display:grid;gap:30px;margin:0 }`.
   - Responsive Contract: Detail module `Interactive Detail & Feature Matrix (<section.pageSection> — `Most Popular Prints`)` uses `3px`, `4px`, `6px`, `2px` radii, `#161618` highlights, and assets (clarity.js, recaptcha__en.js, xmlrpc.php).
5. **Colophon & Global Directory Footer (<footer.page-template-template-homepage> — `https://www.rosshalfin.com`)**:
   - DOM & Selectors: Landmark `<footer class="page-template-template-homepage">` anchoring `Ross Halfin Photography · Music ` footer links (`€ 0.00 0`), copy *"Used to store your preferences, such as language or display "*, and `#333333` structural dividers.
   - Responsive Contract: Footer `Colophon & Global Directory Footer (<footer.page-template-template-homepage> — `https://www.rosshalfin.com`)` aligns to `var(--wp--style--global--wide-size)` extracted from `www-rosshalfin-com` stylesheet with `3px` lateral canvas padding with `30px` grid gap and attributes (data-partner-attribution-id="PaymentPlugins_PCP", data-uid-auto="uid_znuqasiucahxrfuik...", data-wp-strategy="defer").

#### Verbatim DOM Copy Excerpts (`dom.html`)
- Copy Excerpt 1: *"We use cookies to improve site performance and functionality. You can manage your..."*
- Copy Excerpt 2: *"Functional Always active"*
- Copy Excerpt 3: *"Required to enable core site functionality and services you request."*
- Copy Excerpt 4: *"Used to store your preferences, such as language or display settings."*

### 7. Motion, Extracted Stylesheet Rules & Interaction Choreography
- **Primary Easing Functions**: `cubic-bezier(.33,0,.2,1)`, `cubic-bezier(.28,.75,.22,.95)`, `cubic-bezier(.4,0,.2,1)`
- **Extracted Stylesheet Rules (`www-rosshalfin-com`)**:
- `body .is-layout-constrained>.alig... { max-width:var(--wp--style--global--wide-size) }`
- `.has-text-align-center { text-align:center }`
- `.site .wc-block-grid__products { display:grid;gap:30px;margin:0 }`
- `.has-1-columns .wc-block-grid__pr... { grid-template-columns:repeat(1,1fr) }`
- `.has-2-columns .wc-block-grid__pr... { grid-template-columns:repeat(2,1fr) }`
- **Per-Selector Transition Rules**:
- **Selector `.site .wc-block-grid__product`**: `transition: all .2s` extracted from `www-rosshalfin-com` stylesheet.
- **Selector `media (min-width:993px)`**: `transition: all .2s` extracted from `www-rosshalfin-com` stylesheet.
- **Selector `.wc-block-grid__product:hover:before`**: `transition: all .2s` extracted from `www-rosshalfin-com` stylesheet.
- **Extracted Easing Curve (`cubic-bezier(.33,0,.2,1)`)**: Governs interactive state transitions across `<header.site-header>` and `<section.pageSection>`.
- **Runtime Interaction Engine**: Integrates Three.js / WebGL Canvas Pipeline, Swiper Touch Carousel Engine with `prefers-reduced-motion: reduce` fallback guards.

### 8. Technical Deliverables
- Implement in Next.js (App Router) with TypeScript and Tailwind CSS consuming the `:root` custom properties defined above for `www-rosshalfin-com`.
- Reproduce both the `1440px` desktop architecture and `390px` mobile breakpoint transitions, preserving semantic HTML5 landmarks (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`) and `prefers-reduced-motion` accessibility guards.
```
