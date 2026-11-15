# UI & UX Architecture: www-jasmin-karatas-ch

## Overview & Design Identity
- **Target**: `www-jasmin-karatas-ch` (**Jasmin Deniz Karatas – Product Designer, Gamification Specialist & Keyno...**)
- **Production URL**: [http://www.jasmin-karatas.ch](http://www.jasmin-karatas.ch)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#5ee9b5` / `#fff`)
- **Summary**: Jasmin Deniz Karatas (JayKay): product designer, gamification specialist and keynote speaker. Keynotes, workshops and books on gaming the...
- **Total Clean CSS Variables Extracted**: `86` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `larsseit`
- **Body Font Stack**: `larsseit Fallback`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`
- **Metadata & Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#5ee9b5` | `var(--color-emerald-300)` in `:root` |
| **Primary Typography Ink** | `#00d294` | `var(--color-emerald-400)` in `:root` |
| **Elevated Surface / Card Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Interactive Accent / Highlight** | `#fff` | `var(--color-white)` in `:root` |
| **Secondary / Muted Copy** | `#070b16` | `var(--color-navy-900)` in `:root` |
| **Structural Hairline Border** | `#171717` | `var(--foreground)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-larsseit` | `"larsseit", "larsseit Fallback"` | Typography / Scale Token |
| `--font-interphases` | `"interphases", "interphases Fallback"` | Typography / Scale Token |
| `--font-wanted-serif` | `"Tinos", "Tinos Fallback"` | Typography / Scale Token |
| `--font-wanted-condensed` | `"Stint Ultra Condensed", "Stint Ultra Condensed Fallback"` | Typography / Scale Token |
| `--font-wanted-bounty` | `"Questrial", "Questrial Fallback"` | Typography / Scale Token |
| `--font-wanted-fine` | `"Oswald", "Oswald Fallback"` | Typography / Scale Token |
| `--font-sans` | `var(--font-interphases), sans-serif` | Typography / Scale Token |
| `--color-emerald-300` | `#5ee9b5` | Brand / Palette Token |
| `--color-emerald-400` | `#00d294` | Brand / Palette Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--container-xs` | `20rem` | Layout / Spatial Grid Token |
| `--container-sm` | `24rem` | Layout / Spatial Grid Token |
| `--container-md` | `28rem` | Layout / Spatial Grid Token |
| `--container-xl` | `36rem` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.fixed> — `www-jasmin-karatas-ch`)**:
   - Landmark `<header class="fixed inset-x-0">` hosting `Jasmin Deniz Karatas – Product Desig` navigation (`Privacy · Imprint`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-sdkn="@vercel/analytics/next"`), and stylesheet rule `html.lenis body { height:auto }`.
2. **Hero Stage & Focal Lead (<section.relative> — `JAYKAY – Jasmin Deniz Karatas`)**:
   - Landmark `<section class="relative">` presenting display lead `JAYKAY – Jasmin Deniz Karatas` and copy excerpt *"04 Content Creation"* over `#5ee9b5` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.relative> — `Keynotes, workshops and gamificati`)**:
   - Landmark `<section class="relative flex">` rendering section `Keynotes, workshops and gamification concepts.` with copy *"Product Designer, Gamification Specialist & Keynote Speaker"*, asset references (`2f19417f17ff8e58-s.p.3gn-3bwpf0f0...`, `581c3ae769a58b7e-s.p.2ow53ya-6whs...`, `96cd250007373f76-s.p.13j832optq1i...`, `Larsseit_Bold-s.p.3wzp25uvg6vh4.w...`), and grid rule `.lenis-stopped { overflow:clip }`.
4. **Interactive Detail & Feature Matrix (<section.relative> — `Gamification Keynotes`)**:
   - Landmark `<section class="relative flex">` framing `Gamification Keynotes` and `Game Changing – Rise of a Business Nerd.` (*"Start voyage ENTER"*) with `#000` surface cards, `#fff` accents, and `.lenis.lenis-smooth iframe { pointer-events:none }`.
5. **Colophon & Global Directory Footer (<footer.relative> — `http://www.jasmin-karatas.ch`)**:
   - Landmark `<footer class="relative overflow-clip">` anchoring `Jasmin Deniz Karatas – Product D` footer links (`Privacy · Imprint`), copy *"Not in the mood for games? Simple Website Version →"*, and `#171717` structural dividers.
