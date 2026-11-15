# UI & UX Architecture: re-cycle-org

## Overview & Design Identity
- **Target**: `re-cycle-org` (**Re-Cycle · Changing Lives Through Bicycle Reuse**)
- **Production URL**: [https://re-cycle.org/](https://re-cycle.org/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#c8df0a` canvas, `#193838` ink, `#f8f8f8` accent)
- **Summary**: We are Re-Cycle. We collect unwanted bikes from across the UK and ship them to trusted partners in Africa. Donate a bike, change a life.
- **Total Clean CSS Variables Extracted**: `132` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Rubik`
- **Body Font Stack**: `DM Sans`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: 1.5`, `--color-body: var(--body)`; rule `p` (`font-size: var(--text-xl)`, `line-height: var(--leading-relaxed)`)
- **Metadata & Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`; rule `small` (`font-size: 15px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#c8df0a` | `var(--primary)` in `:root` |
| **Primary Typography Ink** | `#96cdcf` | `var(--secondary)` in `:root` |
| **Elevated Surface / Card Substrate** | `#e4f2f3` | `var(--secondary-light)` in `:root` |
| **Interactive Accent / Highlight** | `#f8f8f8` | `var(--light)` in `:root` |
| **Secondary / Muted Copy** | `#193838` | `var(--dark)` in `:root` |
| **Structural Hairline Border** | `#fff` | `var(--white)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-red-50` | `oklch(97.1% .013 17.38)` | Brand / Palette Token |
| `--color-red-100` | `oklch(93.6% .032 17.717)` | Brand / Palette Token |
| `--color-red-400` | `oklch(70.4% .191 22.216)` | Brand / Palette Token |
| `--color-red-500` | `oklch(63.7% .237 25.331)` | Brand / Palette Token |
| `--color-red-600` | `oklch(57.7% .245 27.325)` | Brand / Palette Token |
| `--color-red-900` | `oklch(39.6% .141 25.723)` | Brand / Palette Token |
| `--color-red-950` | `oklch(25.8% .092 26.042)` | Brand / Palette Token |
| `--color-yellow-400` | `oklch(85.2% .199 91.936)` | Brand / Palette Token |
| `--color-green-500` | `oklch(72.3% .219 149.579)` | Brand / Palette Token |
| `--color-green-600` | `oklch(62.7% .194 149.214)` | Brand / Palette Token |
| `--color-green-900` | `oklch(39.3% .095 152.535)` | Brand / Palette Token |
| `--color-gray-100` | `oklch(96.7% .003 264.542)` | Brand / Palette Token |
| `--color-gray-200` | `oklch(92.8% .006 264.531)` | Brand / Palette Token |
| `--color-gray-300` | `oklch(87.2% .01 258.338)` | Brand / Palette Token |
| `--color-gray-500` | `oklch(55.1% .027 264.364)` | Brand / Palette Token |
| `--color-black` | `var(--black)` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.inset-x-0> — `re-cycle-org`)**:
   - Landmark `<header class="inset-x-0 w-full">` hosting `Re-Cycle · Changing Lives Through Bi` navigation (`What We Do · How We Do It · Bikes to Africa · UK Community · Our Impact`), DOM attributes (`data-cfasync="false"`, `data-cookieconsent="ignore"`, `data-ezscrex="false"`, `data-no-defer="1"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.footer-main> — `Donate a bike. Change a life.`)**:
   - Landmark `<section class="footer-main relative">` presenting display lead `Donate a bike. Change a life.` and copy excerpt *"What We Do How We Do It Bikes to Africa UK Community"* over `#c8df0a` canvas and `#193838` ink.
3. **Primary Showcase & Content Grid (<section.footer-main> — `377`)**:
   - Landmark `<section class="footer-main relative">` rendering section `377` with copy *"Our Impact Projects Sustainability"*, asset references (`analytics.js`, `ct-bot-detector.min.js`, `gtm.js`, `543115586334417`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.footer-main> — `171,227`)**:
   - Landmark `<section class="footer-main relative">` framing `171,227` and `HOW IT WORKS` (*"Support Us Donate Fundraise Partner Volunteer Shop"*) with `#e4f2f3` surface cards, `#f8f8f8` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.relative> — `https://re-cycle.org/`)**:
   - Landmark `<footer class="relative z-20">` anchoring `Re-Cycle · Changing Lives Throug` footer links (`What We Do · How We Do It · Bikes to Africa · UK Community · Our Impact`), copy *"We collect unwanted bikes across the UK and send them to Afr"*, and `#fff` structural dividers.
