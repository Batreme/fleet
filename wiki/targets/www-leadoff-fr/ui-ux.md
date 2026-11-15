# UI & UX Architecture: www-leadoff-fr

## Overview & Design Identity
- **Target**: `www-leadoff-fr` (**Agence digitale à Vannes : web, mobile & acquisition · LEADOFF**)
- **Production URL**: [https://www.leadoff.fr](https://www.leadoff.fr)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#00f` canvas, `#ff0` ink, `#7a00df` accent)
- **Summary**: LEADOFF conçoit des applications web et mobiles, sites e-commerce et stratégies d’acquisition. Une équipe digitale experte basée à Vannes.
- **Total Clean CSS Variables Extracted**: `24` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `NewTitle-Variable`
- **Body Font Stack**: `GeneralSans-Variable`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `16px`, `20px`, `13px`, `12px`, `10px`)
- **Section Heading (`H2`)**: rule `,h2` (`font-size: max(80px,min(10vw,100vw))`, `font-weight: 650`)
- **Body Copy**: rule `,p` (`font-size: max(18px,min(.9vw,100vw))`, `line-height: 1.5`, `letter-spacing: .03em`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `16px`, `20px`, `13px`, `12px`, `10px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#00f` | `var(--focus-color)` in `:root` |
| **Primary Typography Ink** | `#ff0` | `var(--menu-focus-color)` in `:root` |
| **Elevated Surface / Card Substrate** | `#000` | `var(--menu-focus-contrast)` in `:root` |
| **Interactive Accent / Highlight** | `#7a00df` | `var(--wp-block-synced-color)` in `:root` |
| **Secondary / Muted Copy** | `#ddd` | `var(--wp-editor-canvas-background)` in `:root` |
| **Structural Hairline Border** | `#007cba` | `var(--wp-admin-theme-color)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--focus-color` | `#00f` | Brand / Palette Token |
| `--focus-ring-color` | `var(--focus-color)` | Brand / Palette Token |
| `--menu-focus-color` | `#ff0` | Brand / Palette Token |
| `--menu-focus-contrast` | `#000` | Color / Atmospheric Token |
| `--expandable-focus-color` | `#ff0` | Brand / Palette Token |
| `--editorial-expandable-focus-color` | `#ff0` | Brand / Palette Token |
| `--highlight-focus-color` | `#ff0` | Canvas / Surface Token |
| `--highlight-focus-contrast` | `#000` | Canvas / Surface Token |
| `--highlight-list-height` | `100vh` | Canvas / Surface Token |
| `--highlight-item-width` | `max(320px,min(84vw,420px))` | Canvas / Surface Token |
| `--highlight-image-height` | `max(240px,min(20vw,100vw))` | Canvas / Surface Token |
| `--wp-block-synced-color` | `#7a00df` | Brand / Palette Token |
| `--wp-block-synced-color--rgb` | `122,0,223` | Brand / Palette Token |
| `--wp-bound-block-color` | `var(--wp-block-synced-color)` | Brand / Palette Token |
| `--wp-editor-canvas-background` | `#ddd` | Canvas / Surface Token |
| `--wp-admin-theme-color` | `#007cba` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.yoast-schema-graph> — `www-leadoff-fr`)**:
   - Landmark `<header class="yoast-schema-graph">` hosting `Agence digitale à Vannes : web, mobi` navigation (`Services · Applications mobiles · Applications web · Sites e-commerce · Sites vitrine`), DOM attributes (`data-barba="wrapper"`, `data-storage-key="leadoff.loaderIntroSh..."`, `data-session-duration="1800000"`, `data-icon="false"`), and stylesheet rule `.loader.loader--hidden { opacity:0;-webkit-transform:scale(.98);transform:scale(.98) }`.
2. **Hero Stage & Focal Lead (<section.observe-section> — `Des applications et des sites qui `)**:
   - Landmark `<section class="observe-section bg-blue">` presenting display lead `Des applications et des sites qui performent` and copy excerpt *"Chargement du site"* over `#00f` canvas and `#ff0` ink.
3. **Primary Showcase & Content Grid (<section.editorial-pitch> — `On conçoit des solutions pensées p`)**:
   - Landmark `<section class="editorial-pitch observe-section">` rendering section `On conçoit des solutions pensées pour durer` with copy *"Services Applications mobiles Applications web Sites e-commerce S"*, asset references (`bundle.68ec1454.css`, `jquery.min.js`, `jquery-migrate.min.js`, `cropped-FAVICON-1-32x32.jpg`), and grid rule `.loader .loader-word { display:-webkit-box;display:-ms-flexbox;display:flex;overflow:hidden }`.
4. **Interactive Detail & Feature Matrix (<section.editorial-highlight> — `Ce qu’on fait (et bien)`)**:
   - Landmark `<section class="editorial-highlight observe-section">` framing `Ce qu’on fait (et bien)` and `Pourquoi LEADOFF et pas un autre` (*"Applications mobiles"*) with `#000` surface cards, `#7a00df` accents, and `.loader .loader-skip:focus-visible { color:ff0;outline:none }`.
5. **Colophon & Global Directory Footer (<footer.observe-section> — `https://www.leadoff.fr`)**:
   - Landmark `<footer class="observe-section bg-blue">` anchoring `Agence digitale à Vannes : web, ` footer links (`Services · Applications mobiles · Applications web · Sites e-commerce · Sites vitrine`), copy *"Sites pour collectivités"*, and `#007cba` structural dividers.
