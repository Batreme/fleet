# UI & UX Architecture: concretaceramiche-it

## Overview & Design Identity
- **Target**: `concretaceramiche-it` (**Concreta Ceramiche Artigianali Fatte a Mano**)
- **Production URL**: [https://concretaceramiche.it/](https://concretaceramiche.it/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#720eec` canvas, `#fcfbfe` ink, `#ffba00` accent)
- **Summary**: Ceramiche artigianali uniche, realizzate a mano nei Castelli Romani. Gres, stampa 3D e tradizione familiare in ogni pezzo. Scopri la coll...
- **Total Clean CSS Variables Extracted**: `68` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Elgoc`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: rule `h1` (`font-size: 25px`, `line-height: 32px`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `14px`, `1rem`, `80%`, `75%`, `1em`)
- **Body Copy**: CSS variables `--cmplz_category_body_font_size: 12px`; rule `p` (`font-weight: 500`)
- **Metadata & Labels**: rule `small` (`font-size: 15px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#720eec` | `var(--woocommerce)` in `:root` |
| **Primary Typography Ink** | `#008a20` | `var(--wc-green)` in `:root` |
| **Elevated Surface / Card Substrate** | `#a00` | `var(--wc-red)` in `:root` |
| **Interactive Accent / Highlight** | `#ffba00` | `var(--wc-orange)` in `:root` |
| **Secondary / Muted Copy** | `#2ea2cc` | `var(--wc-blue)` in `:root` |
| **Structural Hairline Border** | `#fcfbfe` | `var(--wc-primary-text)` in `:root` |
| **Variable Token (`--wc-secondary`)** | `#e9e6ed` | `var(--wc-secondary)` in `:root` |
| **Variable Token (`--wc-secondary-text`)** | `#515151` | `var(--wc-secondary-text)` in `:root` |
| **Variable Token (`--wc-highlight`)** | `#958e09` | `var(--wc-highlight)` in `:root` |
| **Variable Token (`--wc-content-bg`)** | `#fff` | `var(--wc-content-bg)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--border-radius` | `10px` | Elevation / Border Token |
| `--border-radius-md` | `20px` | Elevation / Border Token |
| `--padding-top-hero` | `102px` | Layout / Spatial Grid Token |
| `--padding-top-hero-home` | `380px` | Layout / Spatial Grid Token |
| `--woocommerce` | `#720eec` | Color / Atmospheric Token |
| `--wc-green` | `#008a20` | Color / Atmospheric Token |
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

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.fixed> — `concretaceramiche-it`)**:
   - Landmark `<header class="fixed">` hosting `Concreta Ceramiche Artigianali Fatte` navigation (`h o m e h o m e · c o r s i c o r s i · S h o p S h o p · EN · Home`), DOM attributes (`data-wp-strategy="defer"`, `data-wp-strategy="defer"`, `data-wp-strategy="defer"`, `data-wp-strategy="defer"`), and stylesheet rule `.cmplz-video.cmplz-iframe-styles { background-color:transparent }`.
2. **Hero Stage & Focal Lead (<section.rank-math-schema> — `ConCreta ceramiche artigianali Rom`)**:
   - Landmark `<section class="rank-math-schema">` presenting display lead `ConCreta ceramiche artigianali Roma` and copy excerpt *"Funzionale Sempre attivo"* over `#720eec` canvas and `#fcfbfe` ink.
3. **Primary Showcase & Content Grid (<section.logo> — `La ceramica artigianale prende for`)**:
   - Landmark `<section class="logo">` rendering section `La ceramica artigianale prende forma tra gesti an...` with copy *"L'archiviazione tecnica o l'accesso sono strettamente necessari a"*, asset references (`Elgoc-Bold.woff2`, `Elgoc-Regular.woff2`, `Inter28pt-Medium.woff2`, `Inter28pt-Regular.woff2`), and grid rule `.cmplz-video.cmplz-hidden { visibility:hidden !important }`.
4. **Interactive Detail & Feature Matrix (<section.wp-singular> — `Oggetti in ceramica nati dall’inco`)**:
   - Landmark `<section class="wp-singular">` framing `Oggetti in ceramica nati dall’incontro tra tecnic...` and `Un luogo dove la terra diventa forma e prende vita` (*"L'archiviazione tecnica o l'accesso sono necessari per lo scopo l"*) with `#a00` surface cards, `#ffba00` accents, and `.cmplz-blocked-content-notice { display:none }`.
5. **Colophon & Global Directory Footer (<footer.page-template> — `https://concretaceramiche.it/`)**:
   - Landmark `<footer class="page-template">` anchoring `Concreta Ceramiche Artigianali F` footer links (`h o m e h o m e · c o r s i c o r s i · S h o p S h o p · EN · Home`), copy *"L'archiviazione tecnica o l'accesso che viene utilizzato esc"*, and `#fcfbfe` structural dividers.
