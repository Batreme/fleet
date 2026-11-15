# UI & UX Architecture: jonmccormack-com

## Overview & Design Identity
- **Target**: `jonmccormack-com` (**Patterns - Jon McCormack**)
- **Production URL**: [https://jonmccormack.com/](https://jonmccormack.com/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#7a00df` canvas, `#ffffff` ink, `#006ba1` accent)
- **Summary**: Explore the intriguing repeating patterns in nature that captivate the eye and remind us of the awe and beauty in the world.
- **Total Clean CSS Variables Extracted**: `30` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Aeonik Pro`
- **Body Font Stack**: `Fira Code`
- **Monospace / Technical Font Stack**: `Fira Code`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(1.95rem, 1.6vw, 2.8rem)`, `var(--wp--preset--font-size--medium)`, `var(--wp--preset--font-size--small)`, `clamp(1.5rem, 2.2vw, 3rem)`, `var(--wp--preset--font-size--xx-l...`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(1.95rem, 1.6vw, 2.8rem)`, `var(--wp--preset--font-size--medium)`, `var(--wp--preset--font-size--small)`, `clamp(1.5rem, 2.2vw, 3rem)`, `var(--wp--preset--font-size--xx-l...`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(1.95rem, 1.6vw, 2.8rem)`, `var(--wp--preset--font-size--medium)`, `var(--wp--preset--font-size--small)`, `clamp(1.5rem, 2.2vw, 3rem)`, `var(--wp--preset--font-size--xx-l...`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(1.95rem, 1.6vw, 2.8rem)`, `var(--wp--preset--font-size--medium)`, `var(--wp--preset--font-size--small)`, `clamp(1.5rem, 2.2vw, 3rem)`, `var(--wp--preset--font-size--xx-l...`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#7a00df` | `var(--wp-block-synced-color)` in `:root` |
| **Primary Typography Ink** | `#ddd` | `var(--wp-editor-canvas-background)` in `:root` |
| **Elevated Surface / Card Substrate** | `#007cba` | `var(--wp-admin-theme-color)` in `:root` |
| **Interactive Accent / Highlight** | `#006ba1` | `var(--wp-admin-theme-color-darker-10)` in `:root` |
| **Secondary / Muted Copy** | `#005a87` | `var(--wp-admin-theme-color-darker-20)` in `:root` |
| **Structural Hairline Border** | `#ffffff` | `::selection { color: white }` (`#ffffff`) |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--gf-field-gap` | `1.5rem` | Layout / Spatial Grid Token |
| `--gf-input-padding` | `0.875rem 1rem` | Layout / Spatial Grid Token |
| `--gf-border-width` | `1px` | Layout / Spatial Grid Token |
| `--jm-shell-header` | `10vh` | Layout / Spatial Grid Token |
| `--jm-shell-content` | `80vh` | Dimension / Scale Token |
| `--jm-shell-footer` | `8vh` | Dimension / Scale Token |
| `--navigation-layout-justification-setting` | `flex-start` | Layout / Spatial Grid Token |
| `--navigation-layout-direction` | `row` | Layout / Spatial Grid Token |
| `--navigation-layout-wrap` | `wrap` | Layout / Spatial Grid Token |
| `--navigation-layout-justify` | `flex-start` | Layout / Spatial Grid Token |
| `--navigation-layout-align` | `center` | Layout / Spatial Grid Token |
| `--wp-block-synced-color` | `#7a00df` | Brand / Palette Token |
| `--wp-block-synced-color--rgb` | `122,0,223` | Brand / Palette Token |
| `--wp-bound-block-color` | `var(--wp-block-synced-color)` | Brand / Palette Token |
| `--wp-editor-canvas-background` | `#ddd` | Canvas / Surface Token |
| `--wp-admin-theme-color` | `#007cba` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.wp-block-template-part> — `jonmccormack-com`)**:
   - Landmark `<header class="wp-block-template-part">` hosting `Patterns - Jon McCormack` navigation (`Patterns · News · Book · Bio`), DOM attributes (`data-wp-strategy="defer"`, `data-wp-interactive="core/navigation"`, `data-wp-context="("overlayOpenedBy":("..."`, `data-wp-on--click="actions.openMenuOnClick"`), and stylesheet rule `html.jm-splash-viewed .jm-splash { display: none !important; }`.
2. **Hero Stage & Focal Lead (<article.jm-patterns-landing__item> — `A e r i a l P a t t e r n s`)**:
   - Landmark `<article class="jm-patterns-landing__item">` presenting display lead `A e r i a l P a t t e r n s` and copy excerpt *"A e r i a l P a t t e r n s"* over `#7a00df` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<article.jm-patterns-landing__item> — `T i n y P a t t e r n s`)**:
   - Landmark `<article class="jm-patterns-landing__item">` rendering section `T i n y P a t t e r n s` with copy *"T i n y P a t t e r n s"*, asset references (`cdnjs.cloudflare.com`, `www.googletagmanager.com`, `embed`, `splash.css`), and grid rule `textarea:focus { outline: none !important; box-shadow: none !important; }`.
4. **Interactive Detail & Feature Matrix (<article.jm-patterns-landing__item> — `P o l a r P a t t e r n s`)**:
   - Landmark `<article class="jm-patterns-landing__item">` framing `P o l a r P a t t e r n s` and `S m a l l P a t t e r n s` (*"P o l a r P a t t e r n s"*) with `#007cba` surface cards, `#006ba1` accents, and `selection { background: rgb(144, 144, 144); color: white; }`.
5. **Colophon & Global Directory Footer (<footer.wp-block-template-part> — `https://jonmccormack.com/`)**:
   - Landmark `<footer class="wp-block-template-part">` anchoring `Patterns - Jon McCormack` footer links (`Patterns · News · Book · Bio`), copy *"S m a l l P a t t e r n s"*, and `#ffffff` structural dividers.
