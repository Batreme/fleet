# UI & UX Architecture: chandebootcamp-com

## Overview & Design Identity
- **Target**: `chandebootcamp-com` (**Chande Bootcamp 2026 by Mingg Patreon - Design Community in Vietnam**)
- **Production URL**: [http://chandebootcamp.com/](http://chandebootcamp.com/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#0f1513` / `#236c3c`)
- **Summary**: Chande Bootcamp by Mingg is a retreat that connects Vietnamese designers: three days to listen, share and show the love at Ke Retreat, Ha...
- **Total Clean CSS Variables Extracted**: `77` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Phudu`
- **Body Font Stack**: `Geist Mono`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **Hero Display (`H1`)**: CSS variables `--g3-display: 'Phudu', ui-sans-serif, system-ui, sans-serif`
- **Section Heading (`H2`)**: rule `h2` (`font-size: max(2.2rem, calc(80 * var(--u)))`, `line-height: .8`, `letter-spacing: -.04em`, `font-weight: 700`)
- **Body Copy**: rule `p` (`font-size: var(--lab)`, `line-height: .98`, `letter-spacing: -.02em`, `font-weight: 500`)
- **Metadata & Labels**: CSS variables `--mono: max(11px, calc(14 * var(--fu)))`, `--g3-mono: 'Geist Mono', ui-monospace, 'SFMono-Regular', Consolas, monospace`; rule `.mono` (`line-height: .96`, `letter-spacing: -.02em`, `font-weight: 500`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#0f1513` | `var(--ink)` in `:root` |
| **Primary Typography Ink** | `#f4f3eb` | `var(--cream)` in `:root` |
| **Elevated Surface / Card Substrate** | `#F7F3ED` | `var(--g3-floor)` in `:root` |
| **Interactive Accent / Highlight** | `#236c3c` | `var(--g3-green)` in `:root` |
| **Secondary / Muted Copy** | `#68f12b` | `var(--g3-lime)` in `:root` |
| **Structural Hairline Border** | `#c4372b` | `var(--g3-danger)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ink` | `#0f1513` | Typography Ink Token |
| `--line` | `rgba(15,21,19,.18)` | Color / Atmospheric Token |
| `--tb` | `1` | Design System Custom Token |
| `--fu` | `min(var(--u), calc((100svh - var(--bar)) / 1000))` | Dimension / Scale Token |
| `--cream` | `#f4f3eb` | Color / Atmospheric Token |
| `--mono` | `max(11px, calc(14 * var(--fu)))` | Typography / Scale Token |
| `--lab` | `max(12px, calc(16 * var(--fu)))` | Dimension / Scale Token |
| `--g3-floor` | `#F7F3ED` | Color / Atmospheric Token |
| `--g3-ink` | `#0f1513` | Typography Ink Token |
| `--g3-green` | `#236c3c` | Color / Atmospheric Token |
| `--g3-lime` | `#68f12b` | Color / Atmospheric Token |
| `--g3-cream` | `#f4f3eb` | Color / Atmospheric Token |
| `--g3-danger` | `#c4372b` | Color / Atmospheric Token |
| `--g3-hair` | `rgba(15, 21, 19, .18)` | Color / Atmospheric Token |
| `--g3-mute` | `rgba(15, 21, 19, .55)` | Color / Atmospheric Token |
| `--g3-mono` | `'Geist Mono', ui-monospace, 'SFMono-Regular', Consolas, monospace` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.abs> — `chandebootcamp-com`)**:
   - Landmark `<nav class="abs pills">` hosting `Chande Bootcamp 2026 by Mingg Patreo` navigation (`Explore Gallery · About us`), DOM attributes (`data-chande-loading`, `data-chande-transition`, `data-barba="wrapper"`, `data-transition-wrap`), and stylesheet rule `.fm__aside { grid-column:1 / span 5; align-self:start; position:sticky; top:calc(var(... }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Chande Bootcamp By. Mingg`)**:
   - Landmark `<section class="hero">` presenting display lead `Chande Bootcamp By. Mingg` and copy excerpt *"Special event organized by Mingg Patreon - Design community"* over `#0f1513` canvas and `#F7F3ED` ink.
3. **Primary Showcase & Content Grid (<section.hs> — `An event for all designers to conn`)**:
   - Landmark `<section class="hs hs-intro">` rendering section `An event for all designers to connect. Listen & s...` with copy *"2-4 October Ke Retreat - Hanoi, VN"*, asset references (`favicon.ico`, `favicon.svg`, `favicon-32.png`, `apple-touch-icon.png`), and grid rule `.fm__title em { font-style:normal; color:236c3c }`.
4. **Interactive Detail & Feature Matrix (<section.hs> — `06 years`)**:
   - Landmark `<section class="hs hs-story">` framing `06 years` and `Chande.` (*"A community connecting event for Vietnamese designers. In the mos"*) with `#F7F3ED` surface cards, `#236c3c` accents, and `.fm__lead { margin-top:1em }`.
5. **Colophon & Global Directory Footer (<footer.hs> — `http://chandebootcamp.com/`)**:
   - Landmark `<footer class="hs hs-foot">` anchoring `Chande Bootcamp 2026 by Mingg Pa` footer links (`Explore Gallery · About us`), copy *"[ UIUX design community ]"*, and `#c4372b` structural dividers.
