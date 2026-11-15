# UI & UX Architecture: performeurope-eu

## Overview & Design Identity
- **Target**: `performeurope-eu` (**Perform Europe - Reimagine International Touring**)
- **Production URL**: [https://performeurope.eu/](https://performeurope.eu/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#CBF2D9` canvas, `#000` ink, `#7a00df` accent)
- **Summary**: Discover Perform Europe: a funding scheme for the European performing arts. Supporting inclusive, diverse and green touring projects via...
- **Total Clean CSS Variables Extracted**: `226` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Favorit`
- **Body Font Stack**: `ABC Favorit`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 2em`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 32px`, `line-height: 36px`)
- **Body Copy**: rule `.paragraph` (`font-size: 1rem`)
- **Metadata & Labels**: CSS variables `--wp--custom--spacing--small: max(1.5rem, 2vw)`, `--wp--custom--typography--line-height--small: 1.2`; rule `small` (`font-size: 80%`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#CBF2D9` | `var(--mint-color)` in `:root` |
| **Primary Typography Ink** | `#ff00ff` | `var(--magenta-color)` in `:root` |
| **Elevated Surface / Card Substrate** | `#000` | `var(--w2w-start-background-color)` in `:root` |
| **Interactive Accent / Highlight** | `#7a00df` | `var(--wp-block-synced-color)` in `:root` |
| **Secondary / Muted Copy** | `#ddd` | `var(--wp-editor-canvas-background)` in `:root` |
| **Structural Hairline Border** | `#007cba` | `var(--wp-admin-theme-color)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--mint-color` | `#CBF2D9` | Brand / Palette Token |
| `--magenta-color` | `#ff00ff` | Brand / Palette Token |
| `--magenta` | `#ff00ff` | Color / Atmospheric Token |
| `--light-blue` | `rgba(0, 0, 255, .0)` | Canvas / Surface Token |
| `--slider-padding` | `5rem` | Layout / Spatial Grid Token |
| `--slider-column-gap` | `5rem` | Layout / Spatial Grid Token |
| `--slide-width` | `33%` | Layout / Spatial Grid Token |
| `--slide-min-width` | `35rem` | Layout / Spatial Grid Token |
| `--td176b92ada598f8f` | `initial` | Design System Custom Token |
| `--td851cd75a8793667` | `initial` | Design System Custom Token |
| `--tc58f4bf5a9869b3e` | `initial` | Design System Custom Token |
| `--t3a480c2f814ef19c` | `initial` | Design System Custom Token |
| `--t77e217518bcd986b` | `initial` | Design System Custom Token |
| `--tc5e0863356bf5767` | `initial` | Design System Custom Token |
| `--t7a2234c5eadde886` | `initial` | Design System Custom Token |
| `--td340014d093b0821` | `initial` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.nav__cont> — `performeurope-eu`)**:
   - Landmark `<nav class="nav__cont">` hosting `Perform Europe - Reimagine Internati` navigation (`L o g i n · Home · About Us · who we are · Timeline`), DOM attributes (`data-speed="1.09"`, `data-lag="0"`, `data-speed="0.95"`, `data-lag="0"`), and stylesheet rule `.display_user_data { display:none; }`.
2. **Hero Stage & Focal Lead (<section.section-wrp> — `Dear performing arts communities a`)**:
   - Landmark `<section class="section-wrp s-landing-animation">` presenting display lead `Dear performing arts communities across Europe… hi!` and copy excerpt *"Press Enter to Menu"* over `#CBF2D9` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.section-wrp> — `Innovative`)**:
   - Landmark `<section class="section-wrp s-card">` rendering section `Innovative` with copy *"Press Enter to Content"*, asset references (`perform-europe-fav.png`, `cdnjs.cloudflare.com`, `embed`, `password-lost.css`), and grid rule `img.open-eyes.closed { display: none; }`.
4. **Interactive Detail & Feature Matrix (<section.section-wrp> — `Green`)**:
   - Landmark `<section class="section-wrp s-latest">` framing `Green` and `Diverse` (*"Press Enter to Footer"*) with `#000` surface cards, `#7a00df` accents, and `.s-profile-first h1.page__title { max-width: 800px; }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://performeurope.eu/`)**:
   - Landmark `<footer class="footer">` anchoring `Perform Europe - Reimagine Inter` footer links (`L o g i n · Home · About Us · who we are · Timeline`), copy *"P e r f o r m E u r o p e"*, and `#007cba` structural dividers.
