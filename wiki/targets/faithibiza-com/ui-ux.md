# UI & UX Architecture: faithibiza-com

## Overview & Design Identity
- **Target**: `faithibiza-com` (**Faith Ibiza · VIP Ibiza Concierge Services**)
- **Production URL**: [https://faithibiza.com/](https://faithibiza.com/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#7a00df` canvas, `#ddd` ink, `#006ba1` accent)
- **Summary**: Travelling to Ibiza and looking for a VIP experience? Our concierge services will ensure you experience all that the White Isle has to of...
- **Total Clean CSS Variables Extracted**: `242` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Afacad Flux`
- **Body Font Stack**: `Dream Orphans`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 2.5em`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 2em`)
- **Body Copy**: rule `p` (`font-size: 10px`)
- **Metadata & Labels**: CSS variables `--modal-size-small: 500px`, `--gf-label-width: 30%`, `--gf-label-req-gap: 6px`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#7a00df` | `var(--wp-block-synced-color)` in `:root` |
| **Primary Typography Ink** | `#ddd` | `var(--wp-editor-canvas-background)` in `:root` |
| **Elevated Surface / Card Substrate** | `#007cba` | `var(--wp-admin-theme-color)` in `:root` |
| **Interactive Accent / Highlight** | `#006ba1` | `var(--wp-admin-theme-color-darker-10)` in `:root` |
| **Secondary / Muted Copy** | `#005a87` | `var(--wp-admin-theme-color-darker-20)` in `:root` |
| **Structural Hairline Border** | `#001d39` | `var(--cookieadmin-primary-color)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--i-star` | `url(https://faithibiza.com/wp-content/themes/general-block-wp/img/star.svg)` | Dimension / Scale Token |
| `--wp-block-synced-color` | `#7a00df` | Brand / Palette Token |
| `--wp-block-synced-color--rgb` | `122,0,223` | Brand / Palette Token |
| `--wp-bound-block-color` | `var(--wp-block-synced-color)` | Brand / Palette Token |
| `--wp-editor-canvas-background` | `#ddd` | Canvas / Surface Token |
| `--wp-admin-theme-color` | `#007cba` | Brand / Palette Token |
| `--wp-admin-theme-color--rgb` | `0,124,186` | Brand / Palette Token |
| `--wp-admin-theme-color-darker-10` | `#006ba1` | Canvas / Surface Token |
| `--wp-admin-theme-color-darker-10--rgb` | `0,107,160.5` | Canvas / Surface Token |
| `--wp-admin-theme-color-darker-20` | `#005a87` | Canvas / Surface Token |
| `--wp-admin-theme-color-darker-20--rgb` | `0,90,135` | Canvas / Surface Token |
| `--wp-admin-border-width-focus` | `2px` | Layout / Spatial Grid Token |
| `--wp-admin--admin-bar--position-offset` | `var(--wp-admin--admin-bar--height,0px)` | Dimension / Scale Token |
| `--pt` | `0px !important` | Dimension / Scale Token |
| `--pb` | `0px !important` | Dimension / Scale Token |
| `--bg-opacity` | `.75` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `faithibiza-com`)**:
   - Landmark `<header class="site-header">` hosting `Faith Ibiza · VIP Ibiza Concierge Se` navigation (`About · About Us · Charity Work · Latest News · Where to stay`), DOM attributes (`data-optimized="1"`, `data-optimized="1"`, `data-optimized="2"`, `data-optimized="1"`), and stylesheet rule `ideo.background::-webkit-media-co... { display:none!important;opacity:0 }`.
2. **Hero Stage & Focal Lead (<main.site-main> — `For the best Ibiza experience...`)**:
   - Landmark `<main class="site-main">` presenting display lead `For the best Ibiza experience...` and copy excerpt *"About About Us Destination Management Corporate Experiences Chari"* over `#7a00df` canvas and `#ddd` ink.
3. **Primary Showcase & Content Grid (<main.site-main> — `Book with Faith`)**:
   - Landmark `<main class="site-main">` rendering section `Book with Faith` with copy *"Destination Management"*, asset references (`recaptcha__en.js`, `cdn.jsdelivr.net`, `unpkg.com`, `www.google.com`), and grid rule `it-media-controls-start-playback-... { display:none!important }`.
4. **Interactive Detail & Feature Matrix (<main.site-main> — `COME FOR THE BEACHES`)**:
   - Landmark `<main class="site-main">` framing `COME FOR THE BEACHES` and `Stay for the feeling` (*"Corporate Experiences"*) with `#007cba` surface cards, `#006ba1` accents, and `root { --wp-admin-border-width-focus:1.5px }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://faithibiza.com/`)**:
   - Landmark `<footer class="site-footer is-dark">` anchoring `Faith Ibiza · VIP Ibiza Concierg` footer links (`About · About Us · Charity Work · Latest News · Where to stay`), copy *"Where to stay Villas Hotels"*, and `#001d39` structural dividers.
