# UI & UX Architecture: fondation-canadiens-com

## Overview & Design Identity
- **Target**: `fondation-canadiens-com` (**Fondation des Canadiens pour l'enfance - Bouger pour grandir**)
- **Production URL**: [https://fondation.canadiens.com/](https://fondation.canadiens.com/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#f4f4f4`)
- **Summary**: La Fondation des Canadiens de Montréal encourage l’activité physique et l’adoption de saines habitudes de vie chez les jeunes défavorisés...
- **Total Clean CSS Variables Extracted**: `190` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `bauhausvole`
- **Body Font Stack**: `Poppins`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: CSS variables `--text-h1: calc(var(--font-size-h1)/var(--rem)*1rem)`, `--text-h1--line-height: .85`, `--text-h1--letter-spacing: -.03em`; rule `h1` (`font-size: var(--text-h1)`, `line-height: var(--tw-leading,var(...`, `letter-spacing: var(--tw-tracking,var...`, `font-weight: var(--font-we...`)
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2/1.5)`, `--text-h2: calc(var(--font-size-h2)/var(--rem)*1rem)`; rule `h2` (`font-size: var(--text-h4)`, `line-height: var(--tw-leading,var(...`, `font-weight: var(--font-we...`)
- **Body Copy**: CSS variables `--text-body: 1rem`, `--text-body--line-height: 1.4`, `--font-size-body: 16`
- **Metadata & Labels**: CSS variables `--text-sm: .875rem`, `--text-sm--line-height: calc(1.25/.875)`, `--default-mono-font-family: var(--font-mono)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#ccc` | `var(--color-gray)` in `:root` |
| **Interactive Accent / Highlight** | `#f4f4f4` | `var(--color-gray-light)` in `:root` |
| **Secondary / Muted Copy** | `#dae7f6` | `var(--color-gray-blue)` in `:root` |
| **Structural Hairline Border** | `#570000` | `var(--color-red-1)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-sans` | `"Poppins",sans-serif` | Typography / Scale Token |
| `--color-red-50` | `oklch(97.1% .013 17.38)` | Brand / Palette Token |
| `--color-red-500` | `oklch(63.7% .237 25.331)` | Brand / Palette Token |
| `--color-red-800` | `oklch(44.4% .177 26.899)` | Brand / Palette Token |
| `--color-amber-500` | `oklch(76.9% .188 70.08)` | Brand / Palette Token |
| `--color-yellow-500` | `oklch(79.5% .184 86.047)` | Brand / Palette Token |
| `--color-green-500` | `oklch(72.3% .219 149.579)` | Brand / Palette Token |
| `--color-blue-500` | `oklch(62.3% .214 259.815)` | Brand / Palette Token |
| `--color-blue-600` | `oklch(54.6% .245 262.881)` | Brand / Palette Token |
| `--color-purple-500` | `oklch(62.7% .265 303.9)` | Brand / Palette Token |
| `--color-gray-50` | `oklch(98.5% .002 247.839)` | Brand / Palette Token |
| `--color-gray-100` | `oklch(96.7% .003 264.542)` | Brand / Palette Token |
| `--color-gray-200` | `oklch(92.8% .006 264.531)` | Brand / Palette Token |
| `--color-gray-300` | `oklch(87.2% .01 258.338)` | Brand / Palette Token |
| `--color-gray-400` | `oklch(70.7% .022 261.325)` | Brand / Palette Token |
| `--color-gray-600` | `oklch(44.6% .03 256.802)` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.absolute> — `fondation-canadiens-com`)**:
   - Landmark `<header class="absolute left-0">` hosting `Fondation des Canadiens pour l'enfan` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-sveltekit-preload-data="hover"`, `data-svg-origin="464 490"`, `data-svg-origin="857.5 277.5"`, `data-flip-id="auto-2"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<article.pt-margin> — `B o u g e r p o u r g r a n d i r`)**:
   - Landmark `<article class="pt-margin space-y-gutter">` presenting display lead `B o u g e r p o u r g r a n d i r` and copy excerpt *"Dons aux organismes"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<article.pt-margin> — `Nouvelles et histoires`)**:
   - Landmark `<article class="pt-margin space-y-gutter">` rendering section `Nouvelles et histoires` with copy *"Comment contribuer"*, asset references (`fonts.googleapis.com`, `fonts.gstatic.com`, `css2`, `favicon-96x96.png`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<article.pt-margin> — `Comment contribuer`)**:
   - Landmark `<article class="pt-margin space-y-gutter">` framing `Comment contribuer` and `Depuis plus de 25 ans, la Fondation des Canadien` (*"Depuis plus de 25 ans, la Fondation des Canadiens pour l’enfance "*) with `#ccc` surface cards, `#f4f4f4` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.px-margin> — `https://fondation.canadiens.com/`)**:
   - Landmark `<footer class="px-margin pb-30">` anchoring `Fondation des Canadiens pour l'e` footer links (`Overview · Index · Archive · About · Contact`), copy *"Derrière chaque patinoire et chaque programme, il y a une hi"*, and `#570000` structural dividers.
