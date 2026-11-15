# UI & UX Architecture: lorenzolottici-it_en

## Overview & Design Identity
- **Target**: `lorenzolottici-it_en` (**Lorenzo Lottici · Order in chaos**)
- **Production URL**: [https://lorenzolottici.it/en](https://lorenzolottici.it/en)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#3080ff` / `#070707`)
- **Summary**: I bring order to the chaos in your business. Outside, a site people recognize at first glance. Inside, automations and AI agents that wor...
- **Total Clean CSS Variables Extracted**: `211` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `archivo`
- **Body Font Stack**: `archivo Fallback`
- **Monospace / Technical Font Stack**: `jetbrainsMono`
- **Hero Display (`H1`)**: CSS variables `--font-display: var(--font-grande)`, `--tipo-display: clamp(2.75rem,calc(1.2708rem + 6.5741vw),7.1875rem)`, `--lh-display: .98`; rule `h1` (`font-size: var(--tipo-titolo)`, `line-height: var(--lh-titolo)`, `letter-spacing: var(--ls-titolo)`, `font-weight: var(--peso-di...`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: var(--tipo-label)`, `line-height: var(--lh-label)`, `letter-spacing: var(--ls-label)`, `font-weight: var(--peso-la...`)
- **Body Copy**: rule `p` (`line-height: var(--lh-corpo)`)
- **Metadata & Labels**: CSS variables `--mono: var(--font-jetbrains-mono), ui-monospace, monospace`, `--font-jetbrains-mono: "jetbrainsMono", Courier New, ui-monospace, monospace`, `--text-xs: .75rem`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#3080ff` | `var(--color-blue-500)` in `:root` |
| **Primary Typography Ink** | `#000` | `var(--color-black)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fff` | `var(--color-white)` in `:root` |
| **Interactive Accent / Highlight** | `#070707` | `var(--fondo)` in `:root` |
| **Secondary / Muted Copy** | `#0b0c0f` | `var(--pietra)` in `:root` |
| **Structural Hairline Border** | `#14140f` | `var(--inchiostro)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--tenue` | `var(--avorio)` | Design System Custom Token |
| `--avorio-32` | `var(--avorio-10)` | Design System Custom Token |
| `--mono` | `var(--font-jetbrains-mono), ui-monospace, monospace` | Typography / Scale Token |
| `--bordo` | `clamp(8px, 1.2cqmin, 16px)` | Dimension / Scale Token |
| `--su-tocco` | `max(48px, 3rem)` | Dimension / Scale Token |
| `--su-icona` | `max(16px, 1.125rem)` | Dimension / Scale Token |
| `--th` | `clamp(72px, 9vh, 96px)` | Dimension / Scale Token |
| `--riga-h` | `56px` | Dimension / Scale Token |
| `--finestra` | `44svh` | Dimension / Scale Token |
| `--font-grotesk` | `"archivo", "archivo Fallback", system-ui, sans-serif` | Typography / Scale Token |
| `--font-jetbrains-mono` | `"jetbrainsMono", Courier New, ui-monospace, monospace` | Typography / Scale Token |
| `--font-serif` | `ui-serif,Georgia,Cambria,"Times New Roman",Times,serif` | Typography / Scale Token |
| `--color-blue-500` | `#3080ff` | Brand / Palette Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.indice-home> — `lorenzolottici-it_en`)**:
   - Landmark `<header class="indice-home indice-testata">` hosting `Lorenzo Lottici · Order in chaos` navigation (`What I do · Path · Work · Thinking · Let’s talk`), DOM attributes (`data-testata="1"`, `data-caricamento="1"`, `data-tre="1"`, `data-precedence="next"`), and stylesheet rule `.iLAgaa_colonna { max-width:80rem;margin:0 auto;position:relative }`.
2. **Hero Stage & Focal Lead (<section.dark> — `Websites and AI automation in Parm`)**:
   - Landmark `<section class="dark">` presenting display lead `Websites and AI automation in Parma` and copy excerpt *"I’m Lorenzo Lottici. I bring order to the chaos in your business:"* over `#3080ff` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.js> — `What I do`)**:
   - Landmark `<section class="js">` rendering section `What I do` with copy *"I give shape to your ideas. From solid corporate architecture to "*, asset references (`archivo_latin_var-s.p.3b1_7etm2gp...`, `jetbrains_mono_latin_var.p.0gbvn7...`, `polvere-carta.webp`, `420u9fgvjqgpl.js`), and grid rule `.iLAgaa_stelle { border-radius:50%;width:1px;height:1px;position:absolute;top:0;left:0 }`.
4. **Interactive Detail & Feature Matrix (<section.scroll-fermo> — `Websites & e-commerce`)**:
   - Landmark `<section class="scroll-fermo">` framing `Websites & e-commerce` and `AI & automation` (*"I take the weight off your hands. More time for people, zero oper"*) with `#fff` surface cards, `#070707` accents, and `.iLAgaa_pianeta { width:120vw;top:-74vw;right:-62vw }`.
5. **Colophon & Global Directory Footer (<footer.su-piede> — `https://lorenzolottici.it/en`)**:
   - Landmark `<footer class="su-piede indice-home">` anchoring `Lorenzo Lottici · Order in chaos` footer links (`What I do · Path · Work · Thinking · Let’s talk`), copy *"Roxam : the site of a company that’s been building trade sho"*, and `#14140f` structural dividers.
