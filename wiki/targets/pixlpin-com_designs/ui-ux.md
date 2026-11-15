# UI & UX Architecture: pixlpin-com_designs

## Overview & Design Identity
- **Target**: `pixlpin-com_designs` (**Pixlpin: 58K+ Free UI Designs, App Screens, Motion & Graphics**)
- **Production URL**: [https://pixlpin.com/designs](https://pixlpin.com/designs)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#fff` canvas, `#c9c9c9` ink, `#ebebeb` accent)
- **Summary**: Join free. Browse 58K+ real app screens, user flows, websites, motion, logos & 3D, curated from the internet and updated daily.
- **Total Clean CSS Variables Extracted**: `406` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `monoFont`
- **Body Font Stack**: `GeistSans`
- **Monospace / Technical Font Stack**: `monoFont`
- **Hero Display (`H1`)**: CSS variables `--text-size-display: 48px`, `--text-line-display: 56px`, `--text-track-display: -.06em`
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--text-size)`, `var(--text-size-heading)`, `var(--input-size)`, `var(--palette-input-size)`, `var(--field-size)`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--text-size)`, `var(--text-size-heading)`, `var(--input-size)`, `var(--palette-input-size)`, `var(--field-size)`)
- **Metadata & Labels**: CSS variables `--font-geist-mono: "monoFont", ui-monospace, SFMono-Regular, Menlo, monospace`, `--font-mono: var(--font-geist-mono), ui-monospace, monospace`, `--read-small-size: 15px`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--ds-background-100)` in `:root` |
| **Primary Typography Ink** | `#fafafa` | `var(--ds-background-200)` in `:root` |
| **Elevated Surface / Card Substrate** | `#f2f2f2` | `var(--ds-gray-100)` in `:root` |
| **Interactive Accent / Highlight** | `#ebebeb` | `var(--ds-gray-200)` in `:root` |
| **Secondary / Muted Copy** | `#e6e6e6` | `var(--ds-gray-300)` in `:root` |
| **Structural Hairline Border** | `#c9c9c9` | `var(--ds-gray-500)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--control-height` | `var(--topbar-control)` | Layout / Spatial Grid Token |
| `--palette-inset` | `max(var(--palette-top), (100svh - var(--palette-height)) / 2)` | Brand / Palette Token |
| `--control-padding-x` | `0px` | Layout / Spatial Grid Token |
| `--icon-size` | `0px` | Layout / Spatial Grid Token |
| `--text-size` | `var(--palette-input-size)` | Typography Ink Token |
| `--text-line` | `var(--palette-input-line)` | Typography Ink Token |
| `--palette-top` | `var(--space-4)` | Brand / Palette Token |
| `--text-wipe-time` | `var(--duration-swap)` | Typography Ink Token |
| `--text-wipe-delay` | `var(--duration-swap)` | Typography Ink Token |
| `--sweep-spread` | `3em` | Dimension / Scale Token |
| `--placeholder-spread` | `3em` | Dimension / Scale Token |
| `--button-bg` | `var(--color-accent)` | Canvas / Surface Token |
| `--button-shadow` | `var(--shadow-s)` | Elevation / Border Token |
| `--nav-pin-top` | `calc(var(--space-6) * -1)` | Layout / Spatial Grid Token |
| `--nav-fade-top` | `var(--space-12)` | Layout / Spatial Grid Token |
| `--main-pad-end` | `var(--space-5)` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.top-bar> — `pixlpin-com_designs`)**:
   - Landmark `<header class="top-bar">` hosting `Pixlpin: 58K+ Free UI Designs, App S` navigation (`All · Apps · AI · Productivity · Business and SaaS`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `.modal--narrow { width:min(440px, calc(100vw - var(--space-8)));border-radius:var(--radiu... }`.
2. **Hero Stage & Focal Lead (<section.sidebar__bottom> — `Featured Designs`)**:
   - Landmark `<section class="sidebar__bottom">` presenting display lead `Featured Designs` and copy excerpt *"Onboarding Onboarding"* over `#fff` canvas and `#c9c9c9` ink.
3. **Primary Showcase & Content Grid (<article.tile> — `Search Pixlpin`)**:
   - Landmark `<article class="tile tile--video">` rendering section `Search Pixlpin` with copy *"Join 1,000+ Members Join 1,000+ Members, Explore 58,000+ designs"*, asset references (`2hottykkrbx1p.css`, `349k6yv56b9jt.css`, `3l0ai14c31l8b.css`, `0ejnx84aea1e4.css`), and grid rule `.modal--wide { width:min(720px, calc(100vw - var(--space-8)));border-radius:var(--radiu... }`.
4. **Interactive Detail & Feature Matrix (<article.tile> — `Join 1,000+ Members Join 1,000+ Me`)**:
   - Landmark `<article class="tile tile--video">` framing `Join 1,000+ Members Join 1,000+ Members, Explore` and `Join 1,000+ Members` (*"Join 1,000+ Members"*) with `#f2f2f2` surface cards, `#ebebeb` accents, and `.modal::backdrop { background:var(--color-overlay) }`.
5. **Colophon & Global Directory Footer (<footer.shell-footer> — `https://pixlpin.com/designs`)**:
   - Landmark `<footer class="shell-footer">` anchoring `Pixlpin: 58K+ Free UI Designs, A` footer links (`All · Apps · AI · Productivity · Business and SaaS`), copy *"Join 1,000+ Members, Explore 58,000+ designs"*, and `#c9c9c9` structural dividers.
