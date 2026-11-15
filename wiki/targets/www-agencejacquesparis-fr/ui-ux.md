# UI & UX Architecture: www-agencejacquesparis-fr

## Overview & Design Identity
- **Target**: `www-agencejacquesparis-fr` (**Jacques Paris - Agence à impact positif**)
- **Production URL**: [https://www.agencejacquesparis.fr/](https://www.agencejacquesparis.fr/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#F0F0DC` canvas, `#001847` ink, `#1a3a6b` accent)
- **Summary**: La créativité au service des marques qui veulent changer les choses et prendre soin de ce qui compte.
- **Total Clean CSS Variables Extracted**: `21` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `ClashGrotesk`
- **Body Font Stack**: `SF Mono`
- **Monospace / Technical Font Stack**: `SF Mono`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--text-xs)`, `10px`, `var(--text-sm)`, `20px`, `var(--text-lg)`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: var(--text-md)`, `letter-spacing: .01em`, `font-weight: 600`)
- **Body Copy**: CSS variables `--text-base: 15px`; rule `p` (`font-size: var(--text-base)`, `line-height: 1.7`)
- **Metadata & Labels**: CSS variables `--text-xs: 11px`, `--text-sm: 14px`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#F0F0DC` | `var(--color-cream)` in `:root` |
| **Primary Typography Ink** | `#F7F7ED` | `var(--color-cream-light)` in `:root` |
| **Elevated Surface / Card Substrate** | `#001847` | `var(--color-cobalt)` in `:root` |
| **Interactive Accent / Highlight** | `#1a3a6b` | `var(--color-cobalt-light)` in `:root` |
| **Secondary / Muted Copy** | `#0E9AA7` | `var(--color-teal)` in `:root` |
| **Structural Hairline Border** | `#E8442A` | `var(--color-coral)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-cream` | `#F0F0DC` | Brand / Palette Token |
| `--color-cream-light` | `#F7F7ED` | Canvas / Surface Token |
| `--color-cobalt` | `#001847` | Brand / Palette Token |
| `--color-cobalt-light` | `#1a3a6b` | Canvas / Surface Token |
| `--color-teal` | `#0E9AA7` | Brand / Palette Token |
| `--color-coral` | `#E8442A` | Brand / Palette Token |
| `--space-zero` | `0` | Layout / Spatial Grid Token |
| `--space-xs` | `4px` | Layout / Spatial Grid Token |
| `--space-sm` | `8px` | Layout / Spatial Grid Token |
| `--space-md` | `16px` | Layout / Spatial Grid Token |
| `--space-lg` | `24px` | Layout / Spatial Grid Token |
| `--space-xl` | `40px` | Layout / Spatial Grid Token |
| `--space-2xl` | `64px` | Layout / Spatial Grid Token |
| `--space-3xl` | `96px` | Layout / Spatial Grid Token |
| `--text-xs` | `11px` | Typography Ink Token |
| `--text-sm` | `14px` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.Navbar_navbar__UMdIx> — `www-agencejacquesparis-fr`)**:
   - Landmark `<nav class="Navbar_navbar__UMdIx">` hosting `Jacques Paris - Agence à impact posi` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-nscript="afterInteractive"`), and stylesheet rule `.PosterCanvas_canvas__BduZz { position:absolute;inset:0;overflow:hidden;background-color:var(--color-c... }`.
2. **Hero Stage & Focal Lead (<main.ScrollEngine_scrollSpace__HfjIP> — `Jacques Paris - Agence à impact po`)**:
   - Landmark `<main class="ScrollEngine_scrollSpace__HfjIP">` presenting display lead `Jacques Paris - Agence à impact positif` and copy excerpt *"Politique de protection des données personnelles"* over `#F0F0DC` canvas and `#001847` ink.
3. **Primary Showcase & Content Grid (<main.ScrollEngine_viewport__JJVIB> — `Featured Work & Interactive Showca`)**:
   - Landmark `<main class="ScrollEngine_viewport__JJVIB">` rendering section `Featured Work & Interactive Showcase` with copy *"marine.moreau@jacques.com"*, asset references (`jacques-logo.png`, `ad44a6578bd60804.css`, `074517235421c822.css`, `webpack-8fefb68f87553cee.js`), and grid rule `.ZoneLabel_primary__tb_mD { font-size:var(--text-xs);opacity:.35;letter-spacing:.05em }`.
4. **Interactive Detail & Feature Matrix (<main.PosterCanvas_canvas__BduZz> — `Technical Architecture & Narrative`)**:
   - Landmark `<main class="PosterCanvas_canvas__BduZz">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Assistant Art Director"*) with `#001847` surface cards, `#1a3a6b` accents, and `.ZoneLabel_secondary__sFo9Q { font-weight:300;color:var(--color-cobalt);line-height:1.4 }`.
5. **Colophon & Global Directory Footer (<footer.PosterCanvas_poster__O791U> — `https://www.agencejacquesparis.fr/`)**:
   - Landmark `<footer class="PosterCanvas_poster__O791U">` anchoring `Jacques Paris - Agence à impact ` footer links (`Overview · Index · Archive · About · Contact`), copy *"adrien.jamin@jacques.com"*, and `#E8442A` structural dividers.
