# UI & UX Architecture: skhiladze-com

## Overview & Design Identity
- **Target**: `skhiladze-com` (**Luka Skhiladze, motion designer and product engineer**)
- **Production URL**: [https://skhiladze.com](https://skhiladze.com)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#090c12` / `#9aa0aa`)
- **Summary**: Motion design, AI film, 3D and original sound, plus the website or app to go with them. Tbilisi, working worldwide.
- **Total Clean CSS Variables Extracted**: `36` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Martian Display`
- **Body Font Stack**: `Martian Grotesk`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--s-display: clamp(58px, 9.4vw, 180px)`
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--s-body)`, `var(--s-small)`, `17px`, `12px`, `var(--s-lead)`)
- **Body Copy**: CSS variables `--s-body: clamp(16px, .15vw + 15.4px, 17px)`
- **Metadata & Labels**: CSS variables `--s-small: 14px`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#090c12` | `var(--bg)` in `:root` |
| **Primary Typography Ink** | `#11151c` | `var(--bg-2)` in `:root` |
| **Elevated Surface / Card Substrate** | `#f2f2ef` | `var(--ink)` in `:root` |
| **Interactive Accent / Highlight** | `#9aa0aa` | `var(--muted)` in `:root` |
| **Secondary / Muted Copy** | `#fb5e28` | `var(--accent)` in `:root` |
| **Structural Hairline Border** | `#ff7a4d` | `var(--accent-hi)` in `:root` |
| **Variable Token (`--inv-muted`)** | `#4d525b` | `var(--inv-muted)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bg` | `#090c12` | Canvas / Surface Token |
| `--bg-2` | `#11151c` | Canvas / Surface Token |
| `--ink` | `#f2f2ef` | Typography Ink Token |
| `--muted` | `#9aa0aa` | Color / Atmospheric Token |
| `--accent` | `#fb5e28` | Brand / Palette Token |
| `--accent-hi` | `#ff7a4d` | Brand / Palette Token |
| `--accent-ink` | `#090c12` | Typography Ink Token |
| `--inv-bg` | `#f2f2ef` | Canvas / Surface Token |
| `--inv-ink` | `#090c12` | Typography Ink Token |
| `--inv-muted` | `#4d525b` | Color / Atmospheric Token |
| `--scrim` | `rgba(9, 12, 18, .64)` | Color / Atmospheric Token |
| `--clear` | `calc(80px + env(safe-area-inset-bottom, 0px))` | Dimension / Scale Token |
| `--s-small` | `14px` | Dimension / Scale Token |
| `--s-body` | `clamp(16px, .15vw + 15.4px, 17px)` | Dimension / Scale Token |
| `--s-lead` | `clamp(20px, .9vw + 12px, 26px)` | Dimension / Scale Token |
| `--s-head` | `clamp(30px, 2.2vw + 14px, 46px)` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.bar> — `skhiladze-com`)**:
   - Landmark `<header class="bar">` hosting `Luka Skhiladze, motion designer and ` navigation (`01 Work · 02 About`), DOM attributes (`data-base`, `data-av1="loop,film,teaser"`, `data-av1-same="film/bassface film/bo..."`, `data-gl="soft"`), and stylesheet rule `after { box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Luka Skhiladze, motion designer an`)**:
   - Landmark `<section class="hero is-top">` presenting display lead `Luka Skhiladze, motion designer and product engineer` and copy excerpt *"Enter without sound"* over `#090c12` canvas and `#f2f2ef` ink.
3. **Primary Showcase & Content Grid (<section.make> — `What I make`)**:
   - Landmark `<section class="make no-field">` rendering section `What I make` with copy *"Motion on Motion off"*, asset references (`favicon.svg`, `favicon-32.png`, `apple-touch-icon.png`, `martian-display-lat.woff2`), and grid rule `html.lenis body { height:auto }`.
4. **Interactive Detail & Feature Matrix (<section.op> — `About`)**:
   - Landmark `<section class="op">` framing `About` and `All work` (*"Logicor Park 08 Client, AI"*) with `#f2f2ef` surface cards, `#9aa0aa` accents, and `.lenis.lenis-smooth { scroll-behavior:auto!important }`.
5. **Colophon & Global Directory Footer (<footer.no-gl> — `https://skhiladze.com`)**:
   - Landmark `<footer class="no-gl">` anchoring `Luka Skhiladze, motion designer ` footer links (`01 Work · 02 About`), copy *"Coffee prices Spec"*, and `#ff7a4d` structural dividers.
