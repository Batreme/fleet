---
title: "UI & UX Architecture: miligram-pt"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: miligram-pt

## Overview & Design Identity
- **Target**: `miligram-pt` (**Miligram Brand Agency**)
- **Production URL**: [https://miligram.pt](https://miligram.pt)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f5f4f4` canvas, `#1a1a1a` ink, `#ff0000` accent)
- **Summary**: Somos uma agência de Branding, Design e Marketing Digital em Portugal. Criamos marcas, websites e experiências digitais que fazem negócio...
- **Total Clean CSS Variables Extracted**: `257` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `ivypresto-headline`
- **Body Font Stack**: `neue-haas-unica`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--page-title-display: block`, `--display: flex`; rule `h1` (`font-size: 86px`, `line-height: 1.1em`, `font-weight: 300`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 64px`, `line-height: 70.4px`, `font-weight: 300`, `letter-spacing: -0.2px`); rule `h2` (`font-size: 64px`)
- **Body Copy**: live computed `body` (`font-size: 18px`, `line-height: 25.2px`, `font-weight: 400`, `letter-spacing: -0.2px`); rule `body` (`font-size: 62.5%`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 18px`, `line-height: 25.2px`, `font-weight: 400`, `letter-spacing: -0.2px`); CSS variables `--e-global-typography-text-letter-spacing: -0.2px`, `--e-global-typography-f3906fe-letter-spacing: -0.2px`, `--e-global-typography-e59e9b9-letter-spacing: -0.2px`; rule `small` (`font-size: 15px`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f5f4f4` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#1a1a1a` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffffff` | `var(--wc-content-bg)` in `:root` |
| **Interactive Accent / Highlight** | `#ff0000` | `.woocommerce a.remove { color: red }` (`#ff0000`) |
| **Secondary / Muted Copy** | `#767676` | `var(--wc-subtext)` in `:root` |
| **Structural Hairline Border** | `#d5d8dc` | `var(--n-accordion-border-color)` in `:root` |
| **Variable Token (`--woocommerce`)** | `#720eec` | `var(--woocommerce)` in `:root` |
| **Variable Token (`--wc-green`)** | `#007518` | `var(--wc-green)` in `:root` |
| **Variable Token (`--wc-red`)** | `#aa0000` | `var(--wc-red)` in `:root` |
| **Variable Token (`--wc-orange`)** | `#ffba00` | `var(--wc-orange)` in `:root` |
| **Variable Token (`--wc-blue`)** | `#2ea2cc` | `var(--wc-blue)` in `:root` |
| **Variable Token (`--wc-primary-text`)** | `#fcfbfe` | `var(--wc-primary-text)` in `:root` |
| **Variable Token (`--wc-secondary`)** | `#e9e6ed` | `var(--wc-secondary)` in `:root` |
| **Variable Token (`--wc-secondary-text`)** | `#515151` | `var(--wc-secondary-text)` in `:root` |
| **Variable Token (`--wc-highlight`)** | `#958e09` | `var(--wc-highlight)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
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
| `--wc-form-border-radius` | `4px` | Elevation / Border Token |
| `--wc-form-border-width` | `1px` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.elementor> — `miligram-pt`)**:
   - Landmark `<header class="elementor elementor-282">` (`1440x0px`) hosting `Miligram Brand Agency` navigation (`Cultura · Serviços · Loja · Blog · PT`), DOM attributes (`data-wp-strategy="defer"`, `data-wp-strategy="defer"`, `data-wp-strategy="defer"`, `data-wp-strategy="defer"`), and stylesheet rule `html.lenis body { height:auto }`.
2. **Hero Stage & Focal Lead (<section.home> — `Real Brands Content Photos Videos `)**:
   - Landmark `<section class="home">` presenting display lead `Real Brands Content Photos Videos Design Websites` and copy excerpt *"O carrinho está vazio."* over `#f5f4f4` canvas and `#1a1a1a` ink.
3. **Primary Showcase & Content Grid (<section.miligram-evolua> — `for Real People`)**:
   - Landmark `<section class="miligram-evolua">` rendering section `for Real People` with copy *"Brands Content Photos Videos Design Websites"*, asset references (`insight.min.js`, `oaiq.min.js`, `1509416_miligram.pt.js`, `gcm.min.js`), and grid rule `.lenis.lenis-stopped { overflow:clip }`.
4. **Interactive Detail & Feature Matrix (<article.miligram-evolua__block> — `Aqui, o Branding é pensado como um`)**:
   - Landmark `<article class="miligram-evolua__block">` framing `Aqui, o Branding é pensado como um todo.` and `Não precisamos de sorte, temos um método .` (*"Mais de 20 anos a redefinir o conceito de Branding. Da estratégia"*) with `#ffffff` surface cards, `#ff0000` accents, and `.lenis.lenis-smooth iframe { pointer-events:none }`.
5. **Colophon & Global Directory Footer (<footer.elementor> — `https://miligram.pt`)**:
   - Landmark `<footer class="elementor elementor-371">` anchoring `Miligram Brand Agency` footer links (`Cultura · Serviços · Loja · Blog · PT`), copy *"Com mais de 20 anos de história, a Miligram tem redefinido o"*, and `#d5d8dc` structural dividers.
