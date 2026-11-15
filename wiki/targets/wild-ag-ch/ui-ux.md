# UI & UX Architecture: wild-ag-ch

## Overview & Design Identity
- **Target**: `wild-ag-ch` (**Wild AG – Entwicklung von Liegenschaften & Immobilien**)
- **Production URL**: [https://wild-ag.ch/](https://wild-ag.ch/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#faf9f4` canvas, `#2b221c` ink, `#a48a7a` accent)
- **Summary**: Die Wild AG analysiert und entwickelt Grundstücke mit Potenzial. Wir bewerten Areale strategisch und mit dem Ziel, Eigentümer eine nachha...
- **Total Clean CSS Variables Extracted**: `40` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inriaserif`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--_fonts---heading-1: 3.33em`, `--_fonts---heading-1-secondary: 1.08em`, `--_fonts---display: 7.06em`; rule `h1` (`font-size: 2em`)
- **Section Heading (`H2`)**: CSS variables `--_fonts---heading-2-serif: 3.06em`; rule `h2` (`font-size: 32px`, `line-height: 36px`)
- **Body Copy**: CSS variables `--_fonts---paragraph: 1em`; rule `body` (`font-size: 14px`, `line-height: 20px`)
- **Metadata & Labels**: CSS variables `--_fonts---label: .8em`; rule `small` (`font-size: 80%`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#faf9f4` | `var(--white)` in `:root` |
| **Primary Typography Ink** | `#6b6561` | `var(--grey)` in `:root` |
| **Elevated Surface / Card Substrate** | `#2b221c` | `var(--black)` in `:root` |
| **Interactive Accent / Highlight** | `#a48a7a` | `var(--brown)` in `:root` |
| **Secondary / Muted Copy** | `#cbbba0` | `var(--beige)` in `:root` |
| **Structural Hairline Border** | `#f5f1ed` | `var(--light)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--w-backdrop-animation` | `initial` | Motion / Easing Token |
| `--white` | `#faf9f4` | Canvas / Surface Token |
| `--_fonts---inter` | `Inter, Arial, sans-serif` | Typography / Scale Token |
| `--grey` | `#6b6561` | Color / Atmospheric Token |
| `--_other---main-size` | `1.51vw` | Layout / Spatial Grid Token |
| `--black` | `#2b221c` | Canvas / Surface Token |
| `--_fonts---label` | `.8em` | Typography / Scale Token |
| `--brown` | `#a48a7a` | Color / Atmospheric Token |
| `--_other---section-horizontal` | `1.66em` | Dimension / Scale Token |
| `--_fonts---heading-1` | `3.33em` | Typography Ink Token |
| `--_fonts---inria-serif` | `Inriaserif, "Times New Roman", sans-serif` | Typography / Scale Token |
| `--_fonts---heading-1-secondary` | `1.08em` | Typography Ink Token |
| `--_fonts---paragraph` | `1em` | Typography / Scale Token |
| `--_fonts---heading-2-serif` | `3.06em` | Typography Ink Token |
| `--beige` | `#cbbba0` | Color / Atmospheric Token |
| `--_fonts---heading-4` | `1.33em` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.w-mod-js> — `wild-ag-ch`)**:
   - Landmark `<header class="w-mod-js">` hosting `Wild AG – Entwicklung von Liegenscha` navigation (`Kontakt · Über uns · Team · Kompetenzen · Projekte`), DOM attributes (`data-wf-domain="wild-ag.ch"`, `data-wf-page="68ffa3d7dcafaaf81d62a851"`, `data-wf-site="68ffa3d5dcafaaf81d62a778"`, `data-w-id="e44b81a6-fdee-2457-52..."`), and stylesheet rule `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Projekt­entwicklung.`)**:
   - Landmark `<section class="hero">` presenting display lead `Projekt­entwicklung.` and copy excerpt *"Wir realisieren Bauvorhaben von der Vision bis zur Baureife, mit "* over `#faf9f4` canvas and `#2b221c` ink.
3. **Primary Showcase & Content Grid (<section.about> — `Finanzierung.`)**:
   - Landmark `<section class="about">` rendering section `Finanzierung.` with copy *"Dabei analysieren wir Standorte, erstellen Nutzungskonzepte, begl"*, asset references (`cdn.prod.website-files.com`, `wild-ag.webflow.shared.2b6b1ba80.css`, `693bea2fa812933b3861e659_favicon.png`, `693bea2af69043311afaf385_webclip.png`), and grid rule `body { margin: 0; }`.
4. **Interactive Detail & Feature Matrix (<section.team> — `Planung & Ausführung.`)**:
   - Landmark `<section class="team">` framing `Planung & Ausführung.` and `Renovation & Umbau.` (*"Wir unterstützen Bauherrschaften und Investoren bei der optimalen"*) with `#2b221c` surface cards, `#a48a7a` accents, and `summary { display: block; }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://wild-ag.ch/`)**:
   - Landmark `<footer class="footer">` anchoring `Wild AG – Entwicklung von Liegen` footer links (`Kontakt · Über uns · Team · Kompetenzen · Projekte`), copy *"Durch massgeschneiderte Finanzierungsmodelle und ein starkes"*, and `#f5f1ed` structural dividers.
