# UI & UX Architecture: www-pistacchioecaffe-it

## Overview & Design Identity
- **Target**: `www-pistacchioecaffe-it` (**Pistacchio & Caffè**)
- **Production URL**: [http://www.pistacchioecaffe.it](http://www.pistacchioecaffe.it)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#465565` canvas, `#ffba00` ink, `#a00` accent)
- **Summary**: Scopri il mondo di Francesca, interior designer e stylist. Dal design d'interni allo styling personalizzato, troverai soluzioni creative...
- **Total Clean CSS Variables Extracted**: `35` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `utendobold`
- **Body Font Stack**: `utendolight`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 3vw`, `line-height: 1.2`, `font-weight: normal`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 2.5vw`)
- **Body Copy**: rule `body` (`font-size: 18px`, `line-height: 30px`, `font-weight: normal`)
- **Metadata & Labels**: rule `.label` (`font-size: 17px !important`, `line-height: 1 !important`, `font-weight: normal !impor...`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#465565` | `var(--text-main-color)` in `:root` |
| **Primary Typography Ink** | `#720eec` | `var(--woocommerce)` in `:root` |
| **Elevated Surface / Card Substrate** | `#007518` | `var(--wc-green)` in `:root` |
| **Interactive Accent / Highlight** | `#a00` | `var(--wc-red)` in `:root` |
| **Secondary / Muted Copy** | `#ffba00` | `var(--wc-orange)` in `:root` |
| **Structural Hairline Border** | `#2ea2cc` | `var(--wc-blue)` in `:root` |
| **Variable Token (`--wc-primary-text`)** | `#fcfbfe` | `var(--wc-primary-text)` in `:root` |
| **Variable Token (`--wc-secondary`)** | `#e9e6ed` | `var(--wc-secondary)` in `:root` |
| **Variable Token (`--wc-secondary-text`)** | `#515151` | `var(--wc-secondary-text)` in `:root` |
| **Variable Token (`--wc-highlight`)** | `#958e09` | `var(--wc-highlight)` in `:root` |
| **Variable Token (`--wc-content-bg`)** | `#fff` | `var(--wc-content-bg)` in `:root` |
| **Variable Token (`--wc-subtext`)** | `#767676` | `var(--wc-subtext)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--text-main-color` | `#465565` | Typography Ink Token |
| `--app-height` | `100%` | Layout / Spatial Grid Token |
| `--woocommerce` | `#720eec` | Color / Atmospheric Token |
| `--wc-green` | `#007518` | Color / Atmospheric Token |
| `--wc-red` | `#a00` | Color / Atmospheric Token |
| `--wc-orange` | `#ffba00` | Color / Atmospheric Token |
| `--wc-blue` | `#2ea2cc` | Color / Atmospheric Token |
| `--wc-primary` | `#720eec` | Brand / Palette Token |
| `--wc-primary-text` | `#fcfbfe` | Typography Ink Token |
| `--wc-secondary` | `#e9e6ed` | Brand / Palette Token |
| `--wc-secondary-text` | `#515151` | Typography Ink Token |
| `--wc-highlight` | `#958e09` | Canvas / Surface Token |
| `--wc-highligh-text` | `white` | Typography Ink Token |
| `--wc-content-bg` | `#fff` | Canvas / Surface Token |
| `--wc-subtext` | `#767676` | Typography Ink Token |
| `--wc-form-border-color` | `rgba(32, 7, 7, 0.8)` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `www-pistacchioecaffe-it`)**:
   - Landmark `<header class="site-header">` hosting `Pistacchio & Caffè` navigation (`contattami · 0,00 €`), DOM attributes (`data-cmp-ab="2"`, `data-cmp-info="10"`, `data-cmp-ab="2"`, `data-cmp-info="2"`), and stylesheet rule `urger.is-active .hamburger-inner:... { background-color: FFFAF0; }`.
2. **Hero Stage & Focal Lead (<article.post-7> — `Benvenuti nel mio mondo!`)**:
   - Landmark `<article class="post-7 page">` presenting display lead `Benvenuti nel mio mondo!` and copy excerpt *"Benvenuti nel mio mondo!"* over `#465565` canvas and `#ffba00` ink.
3. **Primary Showcase & Content Grid (<article.post-7> — `E colore sia.`)**:
   - Landmark `<article class="post-7 page">` rendering section `E colore sia.` with copy *"Ciao, sono Francesca, interior designer e stylist. Ascolto, proge"*, asset references (`30300652.js`, `core-it.js`, `recaptcha__en.js`, `jquery.min.js`), and grid rule `.hamburger-inner { display: block; top: 50%; margin-top: -1px; }`.
4. **Interactive Detail & Feature Matrix (<article.post-7> — `Osa.`)**:
   - Landmark `<article class="post-7 page">` framing `Osa.` and `Progetto per te.` (*"Amo disegnare e scrivere, ognuna di queste passioni è entrata pre"*) with `#007518` surface cards, `#a00` accents, and `.hamburger-inner::after { content: ""; display: block; }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `http://www.pistacchioecaffe.it`)**:
   - Landmark `<footer class="site-footer contenitore-flex">` anchoring `Pistacchio & Caffè` footer links (`contattami · 0,00 €`), copy *"Potrei definire il mio stile POP_MINIMALE ma non dimentico m"*, and `#2ea2cc` structural dividers.
