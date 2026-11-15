# UI & UX Architecture: dreams-paulvl-eu

## Overview & Design Identity
- **Target**: `dreams-paulvl-eu` (**I'm having bad dreams**)
- **Production URL**: [https://dreams.paulvl.eu/](https://dreams.paulvl.eu/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#050507` / `#fff1c4`)
- **Summary**: An interactive story about a kid whose dreams break, and the fight to rebuild them without becoming someone else.
- **Total Clean CSS Variables Extracted**: `17` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Gloock`
- **Body Font Stack**: `Geist`
- **Monospace / Technical Font Stack**: `IBM Plex Mono`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `19px`, `var(--t-note)`, `var(--t-m)`, `var(--t-l)`, `var(--t-xl)`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `19px`, `var(--t-note)`, `var(--t-m)`, `var(--t-l)`, `var(--t-xl)`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `19px`, `var(--t-note)`, `var(--t-m)`, `var(--t-l)`, `var(--t-xl)`)
- **Metadata & Labels**: CSS variables `--mono: "IBM Plex Mono", ui-monospace, "SFMono-Regular", Menlo, Consolas, monospace`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#050507` | `var(--bg)` in `:root` |
| **Primary Typography Ink** | `#ece6dc` | `var(--ink)` in `:root` |
| **Elevated Surface / Card Substrate** | `#e9b95a` | `var(--gold)` in `:root` |
| **Interactive Accent / Highlight** | `#fff1c4` | `var(--gold-hi)` in `:root` |
| **Secondary / Muted Copy** | `#b3343f` | `var(--red)` in `:root` |
| **Structural Hairline Border** | `#ff0000` | `body.is-night .frame__brand em { color: red }` (`#ff0000`) |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bg` | `#050507` | Canvas / Surface Token |
| `--ink` | `#ece6dc` | Typography Ink Token |
| `--ink-dim` | `rgba(236, 230, 220, .58)` | Typography Ink Token |
| `--ink-faint` | `rgba(236, 230, 220, .2)` | Typography Ink Token |
| `--gold` | `#e9b95a` | Color / Atmospheric Token |
| `--gold-hi` | `#fff1c4` | Color / Atmospheric Token |
| `--red` | `#b3343f` | Color / Atmospheric Token |
| `--serif` | `"Geist", "Helvetica Neue", Arial, sans-serif` | Typography / Scale Token |
| `--italic` | `"Newsreader", Georgia, serif` | Design System Custom Token |
| `--mono` | `"IBM Plex Mono", ui-monospace, "SFMono-Regular", Menlo, Consolas, monospace` | Typography / Scale Token |
| `--gutter` | `clamp(16px, 3vw, 40px)` | Layout / Spatial Grid Token |
| `--t-note` | `15px` | Dimension / Scale Token |
| `--t-m` | `clamp(34px, 4.3vw, 74px)` | Dimension / Scale Token |
| `--t-l` | `clamp(44px, 8.4vw, 150px)` | Dimension / Scale Token |
| `--t-xl` | `clamp(56px, 11.5vw, 210px)` | Dimension / Scale Token |
| `--ease` | `cubic-bezier(.22, 1, .36, 1)` | Motion / Easing Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.frame> — `dreams-paulvl-eu`)**:
   - Landmark `<header class="frame frame--top">` hosting `I'm having bad dreams` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-website-id="ad73bfda-1ced-4e56-88..."`, `data-in="0"`, `data-out=".065"`, `data-in=".075"`), and stylesheet rule `after { box-sizing: border-box; margin: 0; padding: 0; }`.
2. **Hero Stage & Focal Lead (<main.lines> — `About: I'm having bad dreams`)**:
   - Landmark `<main class="lines">` presenting display lead `About: I'm having bad dreams` and copy excerpt *"i'm having bad dreams"* over `#050507` canvas and `#fff1c4` ink.
3. **Primary Showcase & Content Grid (<main.lines> — `I'm having bad dreams`)**:
   - Landmark `<main class="lines">` rendering section `I'm having bad dreams` with copy *"An interactive story about a kid whose dreams break, and the figh"*, asset references (`favicon.svg`, `favicon-32.png`, `apple-touch-icon.png`, `geist-var.woff2`), and grid rule `html { background: var(--bg); scrollbar-width: none; }`.
4. **Interactive Detail & Feature Matrix (<main.lines> — `An interactive story about a kid w`)**:
   - Landmark `<main class="lines">` framing `An interactive story about a kid whose dreams br` and `One room, drawn live in the browser with WebGPU,` (*"One room, drawn live in the browser with WebGPU, three.js and its"*) with `#e9b95a` surface cards, `#fff1c4` accents, and `html::-webkit-scrollbar { display: none; }`.
5. **Colophon & Global Directory Footer (<footer.frame> — `https://dreams.paulvl.eu/`)**:
   - Landmark `<footer class="frame frame--bottom">` anchoring `I'm having bad dreams` footer links (`Overview · Index · Archive · About · Contact`), copy *"No recordings. The clock, the glass, the wind and the birds "*, and `#ff0000` structural dividers.
