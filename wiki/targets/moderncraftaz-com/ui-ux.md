# UI & UX Architecture: moderncraftaz-com

## Overview & Design Identity
- **Target**: `moderncraftaz-com` (**Select A Location · AllHaus**)
- **Production URL**: [https://moderncraftaz.com/](https://moderncraftaz.com/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#4831B0` canvas, `#FFFFFF` ink, `#7a00df` accent)
- **Summary**: Crafting exceptional residences with unmatched service in Arizona, Montana, and beyond.
- **Total Clean CSS Variables Extracted**: `32` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `didot-01`
- **Body Font Stack**: `didot-02`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `54px`, `48px`, `40px`, `24px`, `64px`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `54px`, `48px`, `40px`, `24px`, `64px`)
- **Body Copy**: rule `body` (`font-size: 16px`)
- **Metadata & Labels**: rule `small` (`font-size: 80%`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#4831B0` | `var(--oxynav-brand-color)` in `:root` |
| **Primary Typography Ink** | `#FFFFFF` | `var(--oxynav-neutral-color)` in `:root` |
| **Elevated Surface / Card Substrate** | `#EFEDF4` | `var(--oxynav-activehover-color)` in `:root` |
| **Interactive Accent / Highlight** | `#7a00df` | `var(--wp-block-synced-color)` in `:root` |
| **Secondary / Muted Copy** | `#ddd` | `var(--wp-editor-canvas-background)` in `:root` |
| **Structural Hairline Border** | `#007cba` | `var(--wp-admin-theme-color)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--sk-color` | `currentColor` | Brand / Palette Token |
| `--sk-size` | `100%` | Layout / Spatial Grid Token |
| `--sk-wander-distance` | `calc(var(--sk-size) * 0.75)` | Design System Custom Token |
| `--oxynav-brand-color` | `#4831B0` | Brand / Palette Token |
| `--oxynav-neutral-color` | `#FFFFFF` | Brand / Palette Token |
| `--oxynav-activehover-color` | `#EFEDF4` | Brand / Palette Token |
| `--oxynav-background-color` | `#4831B0` | Canvas / Surface Token |
| `--oxynav-border-radius` | `0px` | Layout / Spatial Grid Token |
| `--oxynav-other-spacing` | `8px` | Layout / Spatial Grid Token |
| `--oxynav-transition-duration` | `0.3s` | Layout / Spatial Grid Token |
| `--oxynav-transition-timing-function` | `cubic-bezier(.84,.05,.31,.93)` | Layout / Spatial Grid Token |
| `--oxynav-animation-name` | `none` | Layout / Spatial Grid Token |
| `--extras-hide-accordion` | `block` | Design System Custom Token |
| `--wp-block-synced-color` | `#7a00df` | Brand / Palette Token |
| `--wp-block-synced-color--rgb` | `122,0,223` | Brand / Palette Token |
| `--wp-bound-block-color` | `var(--wp-block-synced-color)` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.yoast-schema-graph> — `moderncraftaz-com`)**:
   - Landmark `<header class="yoast-schema-graph">` hosting `Select A Location · AllHaus` navigation (`AZ AZ AZ · CO CO CO · MT MT MT`), DOM attributes (`data-again="always_show"`, `data-wait="load"`, `data-wait-sec="2"`, `data-nosnippet`), and stylesheet rule `section-2-27 > .ct-section-inner-... { max-width:100%;padding-top:0;padding-right:0;padding-bottom:0;padding-le... }`.
2. **Hero Stage & Focal Lead (<section.ct-section> — `Unparallelled Service For Exceptio`)**:
   - Landmark `<section class="ct-section">` presenting display lead `Unparallelled Service For Exceptional Homes` and copy excerpt *"Code Snippet ma-customfonts 3.4.2"* over `#4831B0` canvas and `#FFFFFF` ink.
3. **Primary Showcase & Content Grid (<section.ct-section> — `Code Snippet ma-customfonts 3.4.2`)**:
   - Landmark `<section class="ct-section">` rendering section `Code Snippet ma-customfonts 3.4.2` with copy *"Unparallelled Service For Exceptional Homes"*, asset references (`recaptcha__en.js`, `cdn.jsdelivr.net`, `embed`, `ma-customfonts.css`), and grid rule `section-2-27 { background-image:linear-gradient(180deg,rgba(77,37,93,0.5),rgba(77,37,93... }`.
4. **Interactive Detail & Feature Matrix (<section.ct-section> — `moderncraftaz-com Interactive Matr`)**:
   - Landmark `<section class="ct-section">` framing `moderncraftaz-com Interactive Matrix` and `moderncraftaz-com Archive & Directory` (*"Code Snippet ma-customfonts 3.4.2"*) with `#EFEDF4` surface cards, `#7a00df` accents, and `div_block-5-27 { width:100%;flex-direction:row;display:flex;align-items:center;justify-co... }`.
5. **Colophon & Global Directory Footer (<footer.page> — `https://moderncraftaz.com/`)**:
   - Landmark `<footer class="page">` anchoring `Select A Location · AllHaus` footer links (`AZ AZ AZ · CO CO CO · MT MT MT`), copy *"moderncraftaz-com Interactive Matrix"*, and `#007cba` structural dividers.
