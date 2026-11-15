# UI & UX Architecture: superlogica-com

## Overview & Design Identity
- **Target**: `superlogica-com` (**Superlógica: Plataforma de Gestão para Condomínios e Imobiliárias**)
- **Production URL**: [https://superlogica.com/](https://superlogica.com/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#fff` canvas, `#121212` ink, `#3498db` accent)
- **Summary**: A plataforma parceira das administradoras de condomínios e imobiliárias, com gestão autônoma, financeira e customizável para escalar a su...
- **Total Clean CSS Variables Extracted**: `1` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `proxima-nova`
- **Body Font Stack**: `paralucent`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1.8rem`, `1.4rem`, `1.2rem`, `1.5rem`, `1.125rem`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 1.8rem`)
- **Body Copy**: rule `p` (`font-size: 1.125rem`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1.8rem`, `1.4rem`, `1.2rem`, `1.5rem`, `1.125rem`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `.Toastify__toast-container { color: #fff }` |
| **Primary Typography Ink** | `#121212` | `.Toastify__toast--dark { background: #121212 }` |
| **Elevated Surface / Card Substrate** | `#aaa` | `.Toastify__toast--default { color: #aaa }` |
| **Interactive Accent / Highlight** | `#3498db` | `.Toastify__toast--info { background: #3498db }` |
| **Secondary / Muted Copy** | `#07bc0c` | `.Toastify__toast--success { background: #07bc0c }` |
| **Structural Hairline Border** | `#f1c40f` | `.Toastify__toast--warning { background: #f1c40f }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--notification-height` | `34px` | Layout / Spatial Grid Token |
| `--superlogica-com-bg` | `#fff` | Canvas Substrate (from `.Toastify__toast-container { color: #fff }`) |
| `--superlogica-com-ink` | `#121212` | Primary Typography Ink (stylesheet-derived) |
| `--superlogica-com-surface` | `#aaa` | Surface Substrate (stylesheet-derived) |
| `--superlogica-com-accent` | `#3498db` | Interactive Accent (stylesheet-derived) |
| `--superlogica-com-muted` | `#07bc0c` | Secondary Ink (stylesheet-derived) |
| `--superlogica-com-border` | `#f1c40f` | Structural Border (stylesheet-derived) |
| `--superlogica-com-container` | `480px` | Container Bound (stylesheet-derived) |
| `--superlogica-com-gap` | `50px` | Grid Gutter (stylesheet-derived) |
| `--superlogica-com-pad` | `4px` | Lateral Padding (stylesheet-derived) |
| `--superlogica-com-ease` | `cubic-bezier(.215,.61,.355,1)` | Primary Easing Function |
| `--superlogica-com-radius` | `4px` | Corner Radius (stylesheet-derived) |
| `--superlogica-com-fs-base` | `1.8rem` | Observed Font Size Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.sc-12j0ex9-15> — `superlogica-com`)**:
   - Landmark `<header class="sc-12j0ex9-15 jCAcrk">` hosting `Superlógica: Plataforma de Gestão pa` navigation (`Produtos · Imobiliárias · Módulo Financeiro · Controle de acesso · Folha de Pagamento`), DOM attributes (`data-react-helmet="lang"`, `data-react-helmet="true"`, `data-react-helmet="true"`, `data-react-helmet="true"`), and stylesheet rule `.tk-proxima-nova { font-family: "proxima-nova",sans-serif; }`.
2. **Hero Stage & Focal Lead (<section.sc-jk3tv7-0> — `A evolução é sob medida`)**:
   - Landmark `<section class="sc-jk3tv7-0 hGoWlU">` presenting display lead `A evolução é sob medida` and copy excerpt *"Atualizações sobre a Reforma Tributária"* over `#fff` canvas and `#121212` ink.
3. **Primary Showcase & Content Grid (<section.sc-gc6j39-0> — `Estrutura que conecta customização`)**:
   - Landmark `<section class="sc-gc6j39-0 dJeiUC">` rendering section `Estrutura que conecta customização e automação pa...` with copy *"Produtos Produtos Superlógica com Nexus Professional Services Adm"*, asset references (`homem-bg-office-mobile.webp`, `insight.min.js`, `3453052.js`, `pixels.js`), and grid rule `.tk-paralucent { font-family: "paralucent",sans-serif; }`.
4. **Interactive Detail & Feature Matrix (<section.sc-f5frjq-0> — `Plataforma líder no mercado brasil`)**:
   - Landmark `<section class="sc-f5frjq-0 igGITI">` framing `Plataforma líder no mercado brasileiro, referênci...` and `O fim da operação manual.` (*"Superlógica com Nexus"*) with `#aaa` surface cards, `#3498db` accents, and `.tk-argumentum { font-family: "argumentum",sans-serif; }`.
5. **Colophon & Global Directory Footer (<footer.sc-17tfpbv-15> — `https://superlogica.com/`)**:
   - Landmark `<footer class="sc-17tfpbv-15 cQUIfz">` anchoring `Superlógica: Plataforma de Gestã` footer links (`Produtos · Imobiliárias · Módulo Financeiro · Controle de acesso · Folha de Pagamento`), copy *"Professional Services"*, and `#f1c40f` structural dividers.
