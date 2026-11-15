# UI & UX Architecture: miligram-pt

## Overview & Design Identity
- **Target**: `miligram-pt` (**Miligram Brand Agency**)
- **Production URL**: [https://miligram.pt](https://miligram.pt)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#720eec` canvas, `#fcfbfe` ink, `#ffba00` accent)
- **Summary**: Somos uma agência de Branding, Design e Marketing Digital em Portugal. Criamos marcas, websites e experiências digitais que fazem negócio...
- **Total Clean CSS Variables Extracted**: `257` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `WooCommerce`
- **Body Font Stack**: `neue-haas-unica`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--page-title-display: block`, `--display: flex`; rule `h1` (`font-size: 86px`, `line-height: 1.1em`, `font-weight: 300`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 64px`)
- **Body Copy**: rule `body` (`font-size: 62.5%`)
- **Metadata & Labels**: CSS variables `--e-global-typography-text-letter-spacing: -0.2px`, `--e-global-typography-f3906fe-letter-spacing: -0.2px`, `--e-global-typography-e59e9b9-letter-spacing: -0.2px`; rule `small` (`font-size: 15px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#720eec` | `var(--woocommerce)` in `:root` |
| **Primary Typography Ink** | `#007518` | `var(--wc-green)` in `:root` |
| **Elevated Surface / Card Substrate** | `#a00` | `var(--wc-red)` in `:root` |
| **Interactive Accent / Highlight** | `#ffba00` | `var(--wc-orange)` in `:root` |
| **Secondary / Muted Copy** | `#2ea2cc` | `var(--wc-blue)` in `:root` |
| **Structural Hairline Border** | `#fcfbfe` | `var(--wc-primary-text)` in `:root` |
| **Variable Token (`--wc-secondary`)** | `#e9e6ed` | `var(--wc-secondary)` in `:root` |
| **Variable Token (`--wc-secondary-text`)** | `#515151` | `var(--wc-secondary-text)` in `:root` |
| **Variable Token (`--wc-highlight`)** | `#958e09` | `var(--wc-highlight)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--column-gap` | `0px!important` | Layout / Spatial Grid Token |
| `--columns` | `1` | Layout / Spatial Grid Token |
| `--gap` | `20px` | Layout / Spatial Grid Token |
| `--spinner-color` | `rgba(100, 100, 100, 0.8)` | Brand / Palette Token |
| `--spinner-size` | `36px` | Layout / Spatial Grid Token |
| `--row-gap` | `20px` | Layout / Spatial Grid Token |
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

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.elementor> — `miligram-pt`)**:
   - Landmark `<header class="elementor elementor-282">` hosting `Miligram Brand Agency` navigation (`Cultura · Serviços · Loja · Blog · PT`), DOM attributes (`data-wp-strategy="defer"`, `data-wp-strategy="defer"`, `data-wp-strategy="defer"`, `data-wp-strategy="defer"`), and stylesheet rule `html.lenis body { height:auto }`.
2. **Hero Stage & Focal Lead (<section.home> — `Carrinho`)**:
   - Landmark `<section class="home">` presenting display lead `Carrinho` and copy excerpt *"Pular para o conteúdo"* over `#720eec` canvas and `#fcfbfe` ink.
3. **Primary Showcase & Content Grid (<section.miligram-evolua> — `Real Brands Content Photos Videos `)**:
   - Landmark `<section class="miligram-evolua">` rendering section `Real Brands Content Photos Videos Design Websites` with copy *"O carrinho está vazio."*, asset references (`insight.min.js`, `oaiq.min.js`, `1509416_miligram.pt.js`, `gcm.min.js`), and grid rule `.lenis.lenis-stopped { overflow:clip }`.
4. **Interactive Detail & Feature Matrix (<article.miligram-evolua__block> — `for Real People`)**:
   - Landmark `<article class="miligram-evolua__block">` framing `for Real People` and `Aqui, o Branding é pensado como um todo.` (*"Brands Content Photos Videos Design Websites"*) with `#a00` surface cards, `#ffba00` accents, and `.lenis.lenis-smooth iframe { pointer-events:none }`.
5. **Colophon & Global Directory Footer (<footer.elementor> — `https://miligram.pt`)**:
   - Landmark `<footer class="elementor elementor-371">` anchoring `Miligram Brand Agency` footer links (`Cultura · Serviços · Loja · Blog · PT`), copy *"Mais de 20 anos a redefinir o conceito de Branding. Da estra"*, and `#fcfbfe` structural dividers.
