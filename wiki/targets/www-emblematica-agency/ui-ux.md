# UI & UX Architecture: www-emblematica-agency

## Overview & Design Identity
- **Target**: `www-emblematica-agency` (**emblematica — concept-led brand & web design agency in barcelona**)
- **Production URL**: [https://www.emblematica.agency](https://www.emblematica.agency)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#0e0c0d` canvas, `#fbfbfb` ink, `#d5ff69` accent)
- **Summary**: emblematica is a concept-led design agency in Barcelona creating brand identities and websites that help businesses stand out in competit...
- **Total Clean CSS Variables Extracted**: `60` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `InterTight`
- **Body Font Stack**: `Inter Tight`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `14px`, `clamp(calc(48 * var(--u)`, `13px`, `clamp(40px, 12.4vw, 72px)`, `15px`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: calc(58 * var(--u))`, `line-height: 0.92`)
- **Body Copy**: rule `body` (`font-weight: 800`)
- **Metadata & Labels**: CSS variables `--loop-caption-alpha: 0.000`; rule `.caption` (`font-size: calc(14 * var(--u))`, `line-height: 1.17`, `letter-spacing: 0`, `font-weight: inherit`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#0e0c0d` | `var(--ink)` in `:root` |
| **Primary Typography Ink** | `#dadada` | `var(--paper)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fbfbfb` | `var(--white)` in `:root` |
| **Interactive Accent / Highlight** | `#d5ff69` | `var(--acid)` in `:root` |
| **Secondary / Muted Copy** | `#2015FF` | `.t-checkbox__indicator { color: #2015FF }` |
| **Structural Hairline Border** | `#ff8562` | `.tn-nested-link { color: #ff8562 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--t-headline-font` | `'InterTight',Arial,sans-serif` | Typography / Scale Token |
| `--t-text-font` | `'InterTight',Arial,sans-serif` | Typography Ink Token |
| `--ink` | `#0e0c0d` | Typography Ink Token |
| `--paper` | `#dadada` | Canvas / Surface Token |
| `--white` | `#fbfbfb` | Canvas / Surface Token |
| `--acid` | `#d5ff69` | Color / Atmospheric Token |
| `--menu-edge-gap` | `calc(12 * var(--u))` | Layout / Spatial Grid Token |
| `--menu-anchor-left` | `calc(50vw - (45 * var(--u)))` | Dimension / Scale Token |
| `--menu-anchor-top` | `var(--menu-edge-gap)` | Design System Custom Token |
| `--menu-drawer-padding-left` | `calc(28 * var(--u))` | Layout / Spatial Grid Token |
| `--menu-origin-x` | `0px` | Dimension / Scale Token |
| `--menu-origin-y` | `0px` | Dimension / Scale Token |
| `--menu-origin-scale-x` | `0.12` | Design System Custom Token |
| `--menu-origin-scale-y` | `0.05` | Design System Custom Token |
| `--preloader-size` | `220` | Layout / Spatial Grid Token |
| `--preloader-delay` | `70ms` | Motion / Easing Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.t-records> — `www-emblematica-agency`)**:
   - Landmark `<header class="t-records t-records_animated">` hosting `emblematica — concept-led brand & we` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-hook="blocks-collection-con..."`, `data-tilda-project-id="13693937"`, `data-tilda-page-id="189979109"`, `data-tilda-formskey="f0b53f0bdbcb91ba7a098..."`), and stylesheet rule `.csssize { height:3344px }`.
2. **Hero Stage & Focal Lead (<section.manifesto> — `We create design, identities and w`)**:
   - Landmark `<section class="manifesto">` presenting display lead `We create design, identities and websites that he...` and copy excerpt *"concept-led design agency"* over `#0e0c0d` canvas and `#fbfbfb` ink.
3. **Primary Showcase & Content Grid (<section.manifesto-runout> — `Brand Creation`)**:
   - Landmark `<section class="manifesto-runout">` rendering section `Brand Creation` with copy *"let's meet in barcelona"*, asset references (`emblematica.agency`, `ws.tildacdn.com`, `static.tildacdn.com`, `Frame_2087327053.png`), and grid rule `body { --t-headline-font:'InterTight',Arial,sans-serif;--t-text-font:'InterTigh... }`.
4. **Interactive Detail & Feature Matrix (<section.services> — `Re- Brands`)**:
   - Landmark `<section class="services">` framing `Re- Brands` and `Web& Digital` (*"At Emblematica, we believe"*) with `#fbfbfb` surface cards, `#d5ff69` accents, and `.t-body { margin:0px }`.
5. **Colophon & Global Directory Footer (<footer.t-records> — `https://www.emblematica.agency`)**:
   - Landmark `<footer class="t-records">` anchoring `emblematica — concept-led brand ` footer links (`Overview · Index · Archive · About · Contact`), copy *"I n a w o r l d o f A I - g e n e r a t e d v i s u a l s , "*, and `#ff8562` structural dividers.
