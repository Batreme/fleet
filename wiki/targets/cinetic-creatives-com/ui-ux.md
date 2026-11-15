# UI & UX Architecture: cinetic-creatives-com

## Overview & Design Identity
- **Target**: `cinetic-creatives-com` (**Home - Cinetic Creatives**)
- **Production URL**: [https://cinetic-creatives.com/](https://cinetic-creatives.com/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#7a00df` / `#006ba1`)
- **Summary**: Geneva-based creative house where advertising, cinema and experience design come together through powerful storytelling. Reveal the invis...
- **Total Clean CSS Variables Extracted**: `36` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Zalando Sans Expanded`
- **Body Font Stack**: `Arial !important`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--wp--preset--font-size--medium)`, `20px`, `13.3333px`, `1rem`, `14px`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--wp--preset--font-size--medium)`, `20px`, `13.3333px`, `1rem`, `14px`)
- **Body Copy**: rule `p` (`font-size: 16px`, `line-height: 1.25`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--wp--preset--font-size--medium)`, `20px`, `13.3333px`, `1rem`, `14px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#7a00df` | `var(--wp-block-synced-color)` in `:root` |
| **Primary Typography Ink** | `#ddd` | `var(--wp-editor-canvas-background)` in `:root` |
| **Elevated Surface / Card Substrate** | `#007cba` | `var(--wp-admin-theme-color)` in `:root` |
| **Interactive Accent / Highlight** | `#006ba1` | `var(--wp-admin-theme-color-darker-10)` in `:root` |
| **Secondary / Muted Copy** | `#005a87` | `var(--wp-admin-theme-color-darker-20)` in `:root` |
| **Structural Hairline Border** | `#d9d9d9` | `cc-timeline::-webkit-slider-run... { background: #d9d9d9 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--cc-progress` | `0%` | Dimension / Scale Token |
| `--team-gap` | `40px` | Layout / Spatial Grid Token |
| `--navigation-layout-justification-setting` | `flex-start` | Layout / Spatial Grid Token |
| `--navigation-layout-direction` | `row` | Layout / Spatial Grid Token |
| `--navigation-layout-wrap` | `wrap` | Layout / Spatial Grid Token |
| `--navigation-layout-justify` | `flex-start` | Layout / Spatial Grid Token |
| `--navigation-layout-align` | `center` | Layout / Spatial Grid Token |
| `--column-start` | `5` | Layout / Spatial Grid Token |
| `--column-end` | `-5` | Layout / Spatial Grid Token |
| `--wp-block-synced-color` | `#7a00df` | Brand / Palette Token |
| `--wp-block-synced-color--rgb` | `122,0,223` | Brand / Palette Token |
| `--wp-bound-block-color` | `var(--wp-block-synced-color)` | Brand / Palette Token |
| `--wp-editor-canvas-background` | `#ddd` | Canvas / Surface Token |
| `--wp-admin-theme-color` | `#007cba` | Brand / Palette Token |
| `--wp-admin-theme-color--rgb` | `0,124,186` | Brand / Palette Token |
| `--wp-admin-theme-color-darker-10` | `#006ba1` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.wp-block-template-part> — `cinetic-creatives-com`)**:
   - Landmark `<header class="wp-block-template-part">` hosting `Home - Cinetic Creatives` navigation (`About · Services`), DOM attributes (`data-index="0"`, `data-index="1"`, `data-index="2"`, `data-index="3"`), and stylesheet rule `.cc-fullscreen { display: flex; align-items: center; margin-left: 4px; cursor: pointer; }`.
2. **Hero Stage & Focal Lead (<article.post-preview-item> — `E B E L – 1 9 1 1 C H R O N O G R `)**:
   - Landmark `<article class="post-preview-item">` presenting display lead `E B E L – 1 9 1 1 C H R O N O G R A P H I C E B L...` and copy excerpt *"D i s c o v e r a l l t h e p r o j e c t s"* over `#7a00df` canvas and `#ddd` ink.
3. **Primary Showcase & Content Grid (<article.post-preview-item> — `M B & F – H M 1 1`)**:
   - Landmark `<article class="post-preview-item">` rendering section `M B & F – H M 1 1` with copy *"Rue des Vieux-Grenadiers 10 1205 . Geneva – Switzerland"*, asset references (`cdn.jsdelivr.net`, `embed`, `main-2xzhBolw.css`, `style.min.css`), and grid rule `fullscreen .cc-fullscreen .cc-fs-... { display: none; }`.
4. **Interactive Detail & Feature Matrix (<article.post-preview-item> — `V A C H E R O N C O N S T A N T I `)**:
   - Landmark `<article class="post-preview-item">` framing `V A C H E R O N C O N S T A N T I N – P A T R I M...` and `N E S C E N S x L A R E S E R V E` (*"TERMS & CONDITIONS"*) with `#007cba` surface cards, `#006ba1` accents, and `s-fullscreen .cc-fullscreen .cc-f... { display: block; }`.
5. **Colophon & Global Directory Footer (<footer.wp-block-template-part> — `https://cinetic-creatives.com/`)**:
   - Landmark `<footer class="wp-block-template-part">` anchoring `Home - Cinetic Creatives` footer links (`About · Services`), copy *"Designed by Bonhomme"*, and `#d9d9d9` structural dividers.
