# UI & UX Architecture: jetalto-com

## Overview & Design Identity
- **Target**: `jetalto-com` (**JetALto, Private Jet Charter · Fly Anywhere, On Your Schedule**)
- **Production URL**: [https://jetalto.com/](https://jetalto.com/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ccc` canvas, `#0b1220` ink, `#122d4d` accent)
- **Summary**: Instant private jet charter quotes from vetted operators. On-demand flights to 5,000+ airports worldwide. Empty-leg alerts, transparent p...
- **Total Clean CSS Variables Extracted**: `47` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Cormorant Garamond`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: rule `h1` (`font-size: clamp(30px,4.4vw,52px)`, `line-height: 1.06`, `letter-spacing: -.01em`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 26px`, `letter-spacing: -.005em`, `font-weight: 600`)
- **Body Copy**: rule `body` (`font-size: 16px`, `line-height: 1.55`)
- **Metadata & Labels**: rule `small` (`font-size: 11px`, `letter-spacing: .06em`, `font-weight: 600`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#ccc` | `var(--iti-border-color)` in `:root` |
| **Primary Typography Ink** | `#555` | `var(--iti-icon-color)` in `:root` |
| **Elevated Surface / Card Substrate** | `#0a2540` | `var(--navy)` in `:root` |
| **Interactive Accent / Highlight** | `#122d4d` | `var(--navy-2)` in `:root` |
| **Secondary / Muted Copy** | `#1a3860` | `var(--navy-3)` in `:root` |
| **Structural Hairline Border** | `#0b1220` | `var(--ink)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--iti-flag-width` | `20px` | Layout / Spatial Grid Token |
| `--iti-flag-count` | `244` | Design System Custom Token |
| `--iti-flag-offset` | `0` | Design System Custom Token |
| `--iti-hover-color` | `rgba(0, 0, 0, 0.05)` | Brand / Palette Token |
| `--iti-border-color` | `#ccc` | Brand / Palette Token |
| `--iti-country-selector-bg` | `white` | Canvas / Surface Token |
| `--iti-icon-color` | `#555` | Brand / Palette Token |
| `--iti-spacer-horizontal` | `10px` | Layout / Spatial Grid Token |
| `--iti-flag-height` | `calc(var(--iti-flag-width) * 3 / 4)` | Layout / Spatial Grid Token |
| `--iti-globe-icon-size` | `17px` | Layout / Spatial Grid Token |
| `--iti-clear-icon-size` | `15px` | Layout / Spatial Grid Token |
| `--iti-close-icon-size` | `20px` | Layout / Spatial Grid Token |
| `--iti-border-width` | `1px` | Layout / Spatial Grid Token |
| `--iti-arrow-size` | `5px` | Layout / Spatial Grid Token |
| `--iti-arrow-width` | `1.5px` | Layout / Spatial Grid Token |
| `--iti-arrow-padding` | `7px` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `jetalto-com`)**:
   - Landmark `<header class="site-header">` hosting `JetALto, Private Jet Charter · Fly A` navigation (`Home · Our Fleet · Destinations · Blog · Get a Quote`), DOM attributes (`data-step-panel="1"`, `data-lat="50.0333"`, `data-lon="8.5706"`, `data-min="1"`), and stylesheet rule `root { --iti-flag-width: 20px; --iti-flag-count: 244; }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Private Jet Charters`)**:
   - Landmark `<section class="hero hero-wide">` presenting display lead `Private Jet Charters` and copy excerpt *"Global charter · 24 / 7 · Email support"* over `#ccc` canvas and `#0b1220` ink.
3. **Primary Showcase & Content Grid (<section.pad> — `Get a private jet charter quote`)**:
   - Landmark `<section class="pad step2-only">` rendering section `Get a private jet charter quote` with copy *"Home Get an instant charter quote"*, asset references (`favicon.ico`, `favicon-16.png`, `favicon-32.png`, `favicon-96.png`), and grid rule `.iti__ac { --iti-flag-offset: 0; }`.
4. **Interactive Detail & Feature Matrix (<section.pad> — `Almost done, where should we send `)**:
   - Landmark `<section class="pad section-dark">` framing `Almost done, where should we send it?` and `Aircraft options for your trip` (*"Get an instant charter quote"*) with `#0a2540` surface cards, `#122d4d` accents, and `.iti__ad { --iti-flag-offset: -1; }`.
5. **Colophon & Global Directory Footer (<footer.nav> — `https://jetalto.com/`)**:
   - Landmark `<footer class="nav">` anchoring `JetALto, Private Jet Charter · F` footer links (`Home · Our Fleet · Destinations · Blog · Get a Quote`), copy *"Our Fleet 6 classes, 18 models"*, and `#0b1220` structural dividers.
