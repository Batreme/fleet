# UI & UX Architecture: sixescricket-com

## Overview & Design Identity
- **Target**: `sixescricket-com` (**Sixes Party Cricket · Let's Play · Nets & Simulator · Sixes Social Cricket**)
- **Production URL**: [https://sixescricket.com/](https://sixescricket.com/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffa3a3` / `#e40014`)
- **Summary**: Cricket, but not as you know it. We've re-imagined the age old game of cricket for the modern socialite.
- **Total Clean CSS Variables Extracted**: `240` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `Inter Fallback`
- **Monospace / Technical Font Stack**: `fontSoehneMono`
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-6xl: 3.75rem`
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`font-size: 1.75rem`)
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`
- **Metadata & Labels**: CSS variables `--font-soehne-mono: "fontSoehneMono", "fontSoehneMono Fallback"`, `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#ffa3a3` | `var(--color-red-300)` in `:root` |
| **Primary Typography Ink** | `#ff6568` | `var(--color-red-400)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fb2c36` | `var(--color-red-500)` in `:root` |
| **Interactive Accent / Highlight** | `#e40014` | `var(--color-red-600)` in `:root` |
| **Secondary / Muted Copy** | `#fef3c6` | `var(--color-amber-100)` in `:root` |
| **Structural Hairline Border** | `#fcbb00` | `var(--color-amber-400)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-inter` | `"Inter", "Inter Fallback"` | Typography / Scale Token |
| `--font-soehne-mono` | `"fontSoehneMono", "fontSoehneMono Fallback"` | Typography / Scale Token |
| `--fa-font-solid` | `normal 900 1em/1 "Font Awesome 7 Free"` | Typography / Scale Token |
| `--fa-font-regular` | `normal 400 1em/1 "Font Awesome 7 Free"` | Typography / Scale Token |
| `--fa-font-light` | `normal 300 1em/1 "Font Awesome 7 Pro"` | Canvas / Surface Token |
| `--fa-font-thin` | `normal 100 1em/1 "Font Awesome 7 Pro"` | Typography / Scale Token |
| `--fa-font-duotone` | `normal 900 1em/1 "Font Awesome 7 Duotone"` | Typography / Scale Token |
| `--fa-font-duotone-regular` | `normal 400 1em/1 "Font Awesome 7 Duotone"` | Typography / Scale Token |
| `--fa-font-duotone-light` | `normal 300 1em/1 "Font Awesome 7 Duotone"` | Canvas / Surface Token |
| `--fa-font-duotone-thin` | `normal 100 1em/1 "Font Awesome 7 Duotone"` | Typography / Scale Token |
| `--fa-font-brands` | `normal 400 1em/1 "Font Awesome 7 Brands"` | Brand / Palette Token |
| `--fa-font-sharp-solid` | `normal 900 1em/1 "Font Awesome 7 Sharp"` | Typography / Scale Token |
| `--fa-font-sharp-regular` | `normal 400 1em/1 "Font Awesome 7 Sharp"` | Typography / Scale Token |
| `--fa-font-sharp-light` | `normal 300 1em/1 "Font Awesome 7 Sharp"` | Canvas / Surface Token |
| `--fa-font-sharp-thin` | `normal 100 1em/1 "Font Awesome 7 Sharp"` | Typography / Scale Token |
| `--fa-font-sharp-duotone-solid` | `normal 900 1em/1 "Font Awesome 7 Sharp Duotone"` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.sticky> — `sixescricket-com`)**:
   - Landmark `<header class="sticky top-0">` hosting `Sixes Party Cricket · Let's Play · N` navigation (`Venues · Cricket · Food & Drink · Events · Live Sport`), DOM attributes (`data-scroll-behavior="smooth"`, `data-sentry-component="RootLayout"`, `data-sentry-source-file="layout.tsx"`, `data-precedence="next"`), and stylesheet rule `.elmvdc0 { white-space:nowrap;text-overflow:ellipsis;display:block;overflow:clip }`.
2. **Hero Stage & Focal Lead (<section.relative> — `Sixes Social Cricket`)**:
   - Landmark `<section class="relative stack">` presenting display lead `Sixes Social Cricket` and copy excerpt *"Necessary 9 Necessary cookies help make a website usable by enabl"* over `#ffa3a3` canvas and `#e40014` ink.
3. **Primary Showcase & Content Grid (<article.overlay> — `Nothing Beats Hitting Sixes`)**:
   - Landmark `<article class="overlay overlay-b">` rendering section `Nothing Beats Hitting Sixes` with copy *"Google 4 Learn more about this provider Some of the data collecte"*, asset references (`6gknobew.api.sanity.io`, `83afe278b6a6bb3c-s.p.45535valc9rz...`, `soehne_mono-s.p.1h8tgkdilcgxe.woff2`, `0dvybyowk9yut.css`), and grid rule `._1b6o2se1 { animation:.5s linear infinite _1b6o2se0 }`.
4. **Interactive Detail & Feature Matrix (<article.overlay> — `Book Party Cricket`)**:
   - Landmark `<article class="overlay overlay-b">` framing `Book Party Cricket` and `Swing your heart out` (*"Learn more about this provider"*) with `#fb2c36` surface cards, `#e40014` accents, and `._1lyk8y0 { align-items:center }`.
5. **Colophon & Global Directory Footer (<footer.relative> — `https://sixescricket.com/`)**:
   - Landmark `<footer class="relative bg-mahogany-500">` anchoring `Sixes Party Cricket · Let's Play` footer links (`Venues · Cricket · Food & Drink · Events · Live Sport`), copy *"Some of the data collected by this provider is for the purpo"*, and `#fcbb00` structural dividers.
