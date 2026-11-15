# UI & UX Architecture: book-sequel-co

## Overview & Design Identity
- **Target**: `book-sequel-co` (**The First Fifty**)
- **Production URL**: [https://book.sequel.co/](https://book.sequel.co/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#0d0d0d` / `#ffffff`)
- **Summary**: The film can't play in this viewer. Open on desktop
- **Total Clean CSS Variables Extracted**: `30` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Geist Mono`
- **Body Font Stack**: `Bradford`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **Hero Display (`H1`)**: CSS variables `--display: "HD Colton", "VisueltPro", system-ui, sans-serif`, `--type-display: clamp(4rem, 9vw, 7rem)`; rule `h1` (`font-size: clamp(1.75rem, 2.6vw, 2.5rem)`, `line-height: 1.02`, `letter-spacing: -.02em`, `font-weight: 500`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(2rem, 4.4vw, 3.5rem)`, `line-height: 1`, `letter-spacing: .01em`, `font-weight: 900`)
- **Body Copy**: CSS variables `--type-body: 1rem`; rule `body` (`font-size: var(--type-body)`, `line-height: 1.5`)
- **Metadata & Labels**: CSS variables `--mono: "Geist Mono", ui-monospace, monospace`, `--type-label: .875rem`, `--type-meta: .8125rem`; rule `small` (`font-size: .5625rem`, `letter-spacing: .14em`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#0d0d0d` | `var(--black)` in `:root` |
| **Primary Typography Ink** | `#181818` | `var(--dark-grey)` in `:root` |
| **Elevated Surface / Card Substrate** | `#282828` | `var(--mid-grey)` in `:root` |
| **Interactive Accent / Highlight** | `#ffffff` | `var(--white)` in `:root` |
| **Secondary / Muted Copy** | `#faf9f5` | `body { background: #faf9f5 }` |
| **Structural Hairline Border** | `#141413` | `body { color: #141413 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--black` | `#0d0d0d` | Canvas / Surface Token |
| `--dark-grey` | `#181818` | Canvas / Surface Token |
| `--mid-grey` | `#282828` | Color / Atmospheric Token |
| `--white` | `#ffffff` | Canvas / Surface Token |
| `--white-60` | `rgba(255,255,255,.6)` | Canvas / Surface Token |
| `--paper` | `#0d0d0d` | Canvas / Surface Token |
| `--ink` | `#ffffff` | Typography Ink Token |
| `--ink-60` | `rgba(255,255,255,.6)` | Typography Ink Token |
| `--ink-08` | `rgba(255,255,255,.08)` | Typography Ink Token |
| `--sans` | `"VisueltPro", system-ui, sans-serif` | Typography / Scale Token |
| `--mono` | `"Geist Mono", ui-monospace, monospace` | Typography / Scale Token |
| `--display` | `"HD Colton", "VisueltPro", system-ui, sans-serif` | Dimension / Scale Token |
| `--type-display` | `clamp(4rem, 9vw, 7rem)` | Typography / Scale Token |
| `--type-lede` | `1.25rem` | Typography / Scale Token |
| `--type-body` | `1rem` | Typography / Scale Token |
| `--type-label` | `.875rem` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.hero-top> — `book-sequel-co`)**:
   - Landmark `<header class="hero-top">` hosting `The First Fifty` navigation (`Book · Cast · Posters`), DOM attributes (`data-page="home"`, `data-page="home"`, `data-page="home"`, `data-page="cast"`), and stylesheet rule `html { scroll-padding-top:env(safe-area-inset-top,0px) }`.
2. **Hero Stage & Focal Lead (<section.chero> — `Register for early access`)**:
   - Landmark `<section class="chero">` presenting display lead `Register for early access` and copy excerpt *"The film can't play in this viewer. Open on desktop"* over `#0d0d0d` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.hero> — `Thank you,`)**:
   - Landmark `<section class="hero">` rendering section `Thank you,` with copy *"Limited edition book 01:11"*, asset references (`favicon.png`, `script.js`, `fonts.googleapis.com`, `fonts.gstatic.com`), and grid rule `body { margin:0;padding:0;font:14px -apple-system,BlinkMacSystemFont,sans-serif... }`.
4. **Interactive Detail & Feature Matrix (<section.page-home> — `The First Fifty`)**:
   - Landmark `<section class="page-home">` framing `The First Fifty` and `The main characters. 50, Volume I, a sequel coffe...` (*"VOLUME I · LIMITED EDITION"*) with `#282828` surface cards, `#ffffff` accents, and `img { max-width:100% }`.
5. **Colophon & Global Directory Footer (<footer.sf> — `https://book.sequel.co/`)**:
   - Landmark `<footer class="sf js">` anchoring `The First Fifty` footer links (`Book · Cast · Posters`), copy *"Be first to hear when The First Fifty, the posters and the f"*, and `#141413` structural dividers.
