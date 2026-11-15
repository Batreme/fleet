# UI & UX Architecture: awmedia-marketing

## Overview & Design Identity
- **Target**: `awmedia-marketing` (**AW Media & Marketing · UK Web Design Studio**)
- **Production URL**: [https://awmedia.marketing/](https://awmedia.marketing/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#fff` canvas, `#000` ink, `#d4d4d9` accent)
- **Summary**: Award-winning web design for ambitious UK businesses. Sheffield-based, UK-wide. Bespoke when the project demands it, AI-accelerated when...
- **Total Clean CSS Variables Extracted**: `65` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Rethink Sans`
- **Body Font Stack**: `Rethink Sans Fallback`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`font-size: clamp(38px,4.6vw,72px)`)
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`; rule `p` (`font-size: 16.5px`, `line-height: 1.62`)
- **Metadata & Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--color-white)` in `:root` |
| **Primary Typography Ink** | `#000` | `var(--background)` in `:root` |
| **Elevated Surface / Card Substrate** | `#ededed` | `var(--foreground)` in `:root` |
| **Interactive Accent / Highlight** | `#d4d4d9` | `var(--pink-dark)` in `:root` |
| **Secondary / Muted Copy** | `#111` | `var(--card-bg)` in `:root` |
| **Structural Hairline Border** | `#1a1a1a` | `var(--card-border)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-rethink-sans` | `"Rethink Sans", "Rethink Sans Fallback"` | Typography Ink Token |
| `--aw-angle` | `0deg` | Design System Custom Token |
| `--aw-n` | `0` | Design System Custom Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--container-md` | `28rem` | Layout / Spatial Grid Token |
| `--container-2xl` | `42rem` | Layout / Spatial Grid Token |
| `--container-3xl` | `48rem` | Layout / Spatial Grid Token |
| `--container-6xl` | `72rem` | Layout / Spatial Grid Token |
| `--container-7xl` | `80rem` | Layout / Spatial Grid Token |
| `--text-xs` | `.75rem` | Typography Ink Token |
| `--text-xs--line-height` | `calc(1 / .75)` | Typography Ink Token |
| `--text-sm` | `.875rem` | Typography Ink Token |
| `--text-sm--line-height` | `calc(1.25 / .875)` | Typography Ink Token |
| `--text-base` | `1rem` | Typography Ink Token |
| `--text-base--line-height` | `calc(1.5 / 1)` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.nav> — `awmedia-marketing`)**:
   - Landmark `<header class="nav">` hosting `AW Media & Marketing · UK Web Design` navigation (`How We Work · Industries · About · Blog`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-liquid="cursor"`, `data-liquid="pill"`), and stylesheet rule `sans_a7e6451-module__qxRvCW__clas... { font-family:Rethink Sans,Rethink Sans Fallback;font-style:normal }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Designed properly. Built faster.`)**:
   - Landmark `<section class="hero">` presenting display lead `Designed properly. Built faster.` and copy excerpt *"UK Web Design Studio · Since 2016"* over `#fff` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.built> — `Built like this.`)**:
   - Landmark `<section class="built">` rendering section `Built like this.` with copy *"Designed properly."*, asset references (`0dc02305a3505331-s.p.045lmq4bb63o...`, `aw-logo.png`, `04rv9lq_~p.97.css`, `0yrizplp3s9dt.css`), and grid rule `k_sans_a7e6451-module__qxRvCW__va... { --font-rethink-sans:"Rethink Sans", "Rethink Sans Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.trusted> — `Award-⁠winning design, AI-⁠acceler`)**:
   - Landmark `<section class="trusted">` framing `Award-⁠winning design, AI-⁠accelerated where it c...` and `From idea to live. Sites that ship.` (*"An award-⁠winning UK studio shipping bespoke websites at AI-⁠acce"*) with `#ededed` surface cards, `#d4d4d9` accents, and `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://awmedia.marketing/`)**:
   - Landmark `<footer class="footer">` anchoring `AW Media & Marketing · UK Web De` footer links (`How We Work · Industries · About · Blog`), copy *"450+ websites shipped"*, and `#1a1a1a` structural dividers.
