# UI & UX Architecture: vadimcarazan-com

## Overview & Design Identity
- **Target**: `vadimcarazan-com` (**Vadim Carazan, Creative Director**)
- **Production URL**: [https://vadimcarazan.com/](https://vadimcarazan.com/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#0a0a0b` / `#000`)
- **Summary**: Vadim Carazan, creative director and founder of WeGrow. Fourteen years of brand identities, websites and products for founders.
- **Total Clean CSS Variables Extracted**: `14` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Instrument Serif`
- **Body Font Stack**: `Inter Tight`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `13px`, `16.5px`, `14px`, `15vw`, `clamp(56px, 6vw, 96px)`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(32px, 3vw, 46px)`, `line-height: 1.02`, `letter-spacing: -0.01em`, `font-weight: 400`)
- **Body Copy**: rule `.body` (`font-size: 15px`, `line-height: 1.6`)
- **Metadata & Labels**: rule `.label` (`font-size: 12px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#0a0a0b` | `var(--bg)` in `:root` |
| **Primary Typography Ink** | `#f2f2f2` | `var(--ink)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fff` | `.start:hover { border-color: #fff }` |
| **Interactive Accent / Highlight** | `#000` | `.start:hover i { color: #000 }` |
| **Secondary / Muted Copy** | `#ff9b92` | `.c-err { color: #ff9b92 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bg` | `#0a0a0b` | Canvas / Surface Token |
| `--ink` | `#f2f2f2` | Typography Ink Token |
| `--mute` | `rgba(242, 242, 242, 0.55)` | Color / Atmospheric Token |
| `--line` | `rgba(255, 255, 255, 0.12)` | Color / Atmospheric Token |
| `--serif` | `"Editorial Old Italic", "Instrument Serif", "Times New Roman", serif` | Typography / Scale Token |
| `--sans` | `"Inter Tight", "Inter", -apple-system, "Helvetica Neue", Arial, sans-serif` | Typography / Scale Token |
| `--pad` | `clamp(16px, 2vw, 32px)` | Layout / Spatial Grid Token |
| `--box-open` | `clamp(460px, 42vw, 780px)` | Dimension / Scale Token |
| `--ease` | `cubic-bezier(0.22, 1, 0.36, 1)` | Motion / Easing Token |
| `--bp` | `28px` | Dimension / Scale Token |
| `--hx` | `748.8px` | Dimension / Scale Token |
| `--hy` | `196.0px` | Dimension / Scale Token |
| `--hrx` | `203.9px` | Dimension / Scale Token |
| `--hry` | `272.8px` | Dimension / Scale Token |
| `--vadimcarazan-com-bg` | `#0a0a0b` | Canvas Substrate (from `var(--bg)` in `:root`) |
| `--vadimcarazan-com-ink` | `#fff` | Primary Typography Ink (stylesheet-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.topbar> — `vadimcarazan-com`)**:
   - Landmark `<header class="topbar">` hosting `Vadim Carazan, Creative Director` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-engine="three.js r169"`, `data-go="about"`, `data-go="about"`, `data-go="selected"`), and stylesheet rule `c.hot { cursor: pointer; }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Let's make the next one yours.`)**:
   - Landmark `<section class="hero">` presenting display lead `Let's make the next one yours.` and copy excerpt *"Creative Director, WeGrow"* over `#0a0a0b` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.view> — `A few to start with.`)**:
   - Landmark `<section class="view v-project">` rendering section `A few to start with.` with copy *"Cluj-Napoca, Romania ( 13:10 )"*, asset references (`track.js`, `favicon.ico`, `favicon-32.png`, `apple-touch-icon.png`), and grid rule `button { font: inherit; color: inherit; background: none; border: 0; padding: 0;... }`.
4. **Interactive Detail & Feature Matrix (<section.view> — `I make brands for founders who are`)**:
   - Landmark `<section class="view v-selected">` framing `I make brands for founders who are building somet...` and `Tell me what you're building.` (*"Selected , Work , About , Contact"*) with `#fff` surface cards, `#000` accents, and `.logo { width: 48px; height: auto; display: block; }`.
5. **Colophon & Global Directory Footer (<footer.logo> — `https://vadimcarazan.com/`)**:
   - Landmark `<footer class="logo">` anchoring `Vadim Carazan, Creative Director` footer links (`Overview · Index · Archive · About · Contact`), copy *"Fourteen years of brand identities, websites and products fo"*, and `#fff` structural dividers.
