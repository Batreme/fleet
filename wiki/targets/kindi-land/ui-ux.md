# UI & UX Architecture: kindi-land

## Overview & Design Identity
- **Target**: `kindi-land` (**Kindi & Kitir — a confectionery manufacturer in Turkmenistan**)
- **Production URL**: [https://kindi.land/](https://kindi.land/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#e40014` / `#71717b`)
- **Summary**: We have been producing crackers, cookies, and rusks for local and international markets since 2019.
- **Total Clean CSS Variables Extracted**: `167` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `customFont`
- **Body Font Stack**: `customFont Fallback`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5/2.25)`, `--text-5xl: 3rem`
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2/1.5)`, `--text-3xl: 1.875rem`
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5/1)`
- **Metadata & Labels**: CSS variables `--font-mono: var(--font-mono)`, `--text-xs: .75rem`, `--text-xs--line-height: calc(1/.75)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#e40014` | `var(--color-red-600)` in `:root` |
| **Primary Typography Ink** | `#00a544` | `var(--color-green-600)` in `:root` |
| **Elevated Surface / Card Substrate** | `#e5e7eb` | `var(--color-gray-200)` in `:root` |
| **Interactive Accent / Highlight** | `#71717b` | `var(--color-zinc-500)` in `:root` |
| **Secondary / Muted Copy** | `#fff` | `var(--color-white)` in `:root` |
| **Structural Hairline Border** | `#171717` | `var(--foreground)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-custom` | `"customFont","customFont Fallback"` | Typography / Scale Token |
| `--font-custom2` | `"customFont2","customFont2 Fallback"` | Typography / Scale Token |
| `--font-sans` | `var(--font-sans)` | Typography / Scale Token |
| `--font-serif` | `var(--font-serif)` | Typography / Scale Token |
| `--font-mono` | `var(--font-mono)` | Typography / Scale Token |
| `--color-red-600` | `#e40014` | Brand / Palette Token |
| `--color-green-600` | `#00a544` | Brand / Palette Token |
| `--color-gray-200` | `#e5e7eb` | Brand / Palette Token |
| `--color-zinc-500` | `#71717b` | Brand / Palette Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--breakpoint-xl` | `80rem` | Dimension / Scale Token |
| `--container-xl` | `36rem` | Layout / Spatial Grid Token |
| `--container-2xl` | `42rem` | Layout / Spatial Grid Token |
| `--container-3xl` | `48rem` | Layout / Spatial Grid Token |
| `--container-4xl` | `56rem` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.staggered-menu-header> — `kindi-land`)**:
   - Landmark `<header class="staggered-menu-header pointer-events-none">` hosting `Kindi & Kitir — a confectionery manu` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-nimg="1"`, `data-nimg="1"`, `data-nimg="1"`), and stylesheet rule `font_69087933-module__VMELHW__cla... { font-family:customFont,customFont Fallback }`.
2. **Hero Stage & Focal Lead (<section.relative> — `confectionery manufacturer`)**:
   - Landmark `<section class="relative h-full">` presenting display lead `confectionery manufacturer` and copy excerpt *"WE OFFER QUALITY PARTNERSHIP"* over `#e40014` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.flex> — `We have been producing crackers, c`)**:
   - Landmark `<section class="flex items-start">` rendering section `We have been producing crackers, cookies, and cro...` with copy *"We source high‑quality grains and spices to create snacks you can"*, asset references (`49ed31c42e0eea42.css`, `e2dcd0ad6001165c.js`, `1175336dc77a2bf9.js`, `ac3a7ffed65b3ce5.js`), and grid rule `mfont_69087933-module__VMELHW__va... { --font-custom:"customFont","customFont Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.relative> — `Crackers`)**:
   - Landmark `<section class="relative w-full">` framing `Crackers` and `Cookies` (*"Every batch is tested so flavor, crunch, and freshness are always"*) with `#e5e7eb` surface cards, `#71717b` accents, and `font-face { font-family:customFont2;src:url(../media/custom2-s.p.afe4611e.woff2)form... }`.
5. **Colophon & Global Directory Footer (<footer.relative> — `https://kindi.land/`)**:
   - Landmark `<footer class="relative z-10">` anchoring `Kindi & Kitir — a confectionery ` footer links (`Overview · Index · Archive · About · Contact`), copy *"From kids to grown‑ups, our products are made to be shared a"*, and `#171717` structural dividers.
