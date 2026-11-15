# UI & UX Architecture: www-andriimur-com

## Overview & Design Identity
- **Target**: `www-andriimur-com` (**Andrii Mur**)
- **Production URL**: [https://www.andriimur.com/](https://www.andriimur.com/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#4f4f4f` accent)
- **Summary**: Andrii Mur – Ukrainian street & documentary photographer in Tallinn, Estonia. From the information mess to how it feels to be Alive in an...
- **Total Clean CSS Variables Extracted**: `138` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `PT Serif`
- **Body Font Stack**: `PT Serif Fallback`
- **Monospace / Technical Font Stack**: `IBM Plex Mono`
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`
- **Metadata & Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--pswp-bg)` in `:root` |
| **Primary Typography Ink** | `#222` | `var(--pswp-placeholder-bg)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fff` | `var(--pswp-icon-color)` in `:root` |
| **Interactive Accent / Highlight** | `#4f4f4f` | `var(--pswp-icon-color-secondary)` in `:root` |
| **Secondary / Muted Copy** | `#fef9c2` | `var(--color-yellow-100)` in `:root` |
| **Structural Hairline Border** | `#a36100` | `var(--color-yellow-700)` in `:root` |
| **Variable Token (`--pswp-preloader-color`)** | `#4f4f4f66` | `var(--pswp-preloader-color)` in `:root` |
| **Variable Token (`--pswp-preloader-color-secondary`)** | `#ffffffe6` | `var(--pswp-preloader-color-secondary)` in `:root` |
| **Variable Token (`--color-blue-500`)** | `#3080ff` | `var(--color-blue-500)` in `:root` |
| **Variable Token (`--color-blue-800`)** | `#193cb8` | `var(--color-blue-800)` in `:root` |
| **Variable Token (`--color-slate-200`)** | `#e2e8f0` | `var(--color-slate-200)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--pswp-bg` | `#000` | Canvas / Surface Token |
| `--pswp-placeholder-bg` | `#222` | Canvas / Surface Token |
| `--pswp-root-z-index` | `100000` | Elevation / Border Token |
| `--pswp-preloader-color` | `#4f4f4f66` | Brand / Palette Token |
| `--pswp-preloader-color-secondary` | `#ffffffe6` | Brand / Palette Token |
| `--pswp-icon-color` | `#fff` | Brand / Palette Token |
| `--pswp-icon-color-secondary` | `#4f4f4f` | Brand / Palette Token |
| `--pswp-icon-stroke-color` | `#4f4f4f` | Brand / Palette Token |
| `--pswp-icon-stroke-width` | `2px` | Layout / Spatial Grid Token |
| `--pswp-error-text-color` | `var(--pswp-icon-color)` | Typography Ink Token |
| `--font-serif` | `ui-serif, Georgia, Cambria, "Times New Roman", Times, serif` | Typography / Scale Token |
| `--color-yellow-100` | `#fef9c2` | Brand / Palette Token |
| `--color-yellow-700` | `#a36100` | Brand / Palette Token |
| `--color-blue-500` | `#3080ff` | Brand / Palette Token |
| `--color-blue-800` | `#193cb8` | Brand / Palette Token |
| `--color-slate-200` | `#e2e8f0` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.sticky> — `www-andriimur-com`)**:
   - Landmark `<header class="sticky top-0">` hosting `Andrii Mur` navigation (`About · Monochrome · Drops of Melancholy · XA-23.4° · After Dusk`), DOM attributes (`data-theme="dark"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `.pswp img { max-width:none }`.
2. **Hero Stage & Focal Lead (<section.dark> — `Monochrome`)**:
   - Landmark `<section class="dark">` presenting display lead `Monochrome` and copy excerpt *"Drops of Melancholy"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.snap-showcase> — `Drops of Melancholy`)**:
   - Landmark `<section class="snap-showcase">` rendering section `Drops of Melancholy` with copy *"Fulfilling Emptiness"*, asset references (`m2ak1cq3.api.sanity.io`, `6ab71d031fe7ae3b-s.p.141jscyq52bj...`, `80bb744e92754df7-s.p.2eihtoujcocl...`, `83afe278b6a6bb3c-s.p.2bn3s6zvc0dy...`), and grid rule `.pswp--open { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.flex> — `XA-23.4°`)**:
   - Landmark `<section class="flex">` framing `XA-23.4°` and `After Dusk` (*"The Look From Silence"*) with `#fff` surface cards, `#4f4f4f` accents, and `.pswp__bg { will-change:opacity;transform:translateZ(0) }`.
5. **Colophon & Global Directory Footer (<footer.relative> — `https://www.andriimur.com/`)**:
   - Landmark `<footer class="relative bottom-0">` anchoring `Andrii Mur` footer links (`About · Monochrome · Drops of Melancholy · XA-23.4° · After Dusk`), copy *"Monochrome Black and White singles"*, and `#a36100` structural dividers.
