# UI & UX Architecture: atmos-gallery

## Overview & Design Identity
- **Target**: `atmos-gallery` (**Atmos Gallery · Image Colour Palette Generator**)
- **Production URL**: [https://atmos.gallery](https://atmos.gallery)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f5f5f3` / `#1a1a1a`)
- **Summary**: Atmos Gallery extracts five colours from an image, checks WCAG contrast and exports palettes for Figma, CSS, Tailwind, design tokens and...
- **Total Clean CSS Variables Extracted**: `260` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Neue Montreal`
- **Body Font Stack**: `clamp(1.5rem`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: 2.5rem`, `--text-5xl: 3rem`; rule `h1` (`font-size: var(--text-story)`, `line-height: var(--text-story--lin...`, `letter-spacing: var(--track-statement)`, `font-weight: 500`)
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: 2rem`; rule `h2` (`font-size: var(--text-doc-heading)`, `line-height: var(--text-doc-headin...`, `letter-spacing: var(--track-statement)`, `font-weight: 500`)
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: 1.5rem`, `--track-body: 0px`; rule `p` (`font-size: var(--text-base)`, `line-height: var(--text-base--line...`, `letter-spacing: var(--track-body)`)
- **Metadata & Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: 1rem`, `--text-sm: .875rem`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#f5f5f3` | `var(--surface)` in `:root` |
| **Primary Typography Ink** | `#fafaf8` | `var(--surface-raised)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fff` | `var(--surface-white)` in `:root` |
| **Interactive Accent / Highlight** | `#1a1a1a` | `var(--on-surface)` in `:root` |
| **Secondary / Muted Copy** | `#c8322a` | `var(--danger)` in `:root` |
| **Structural Hairline Border** | `#ff6e62` | `var(--danger-inverse)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ease-standard` | `cubic-bezier(.22,1,.36,1)` | Motion / Easing Token |
| `--ease-entrance` | `cubic-bezier(.16,1,.3,1)` | Motion / Easing Token |
| `--ease-exit` | `cubic-bezier(.4,0,1,1)` | Motion / Easing Token |
| `--ease-button-hover` | `cubic-bezier(.675,.15,.1,1)` | Motion / Easing Token |
| `--ease-button-click` | `cubic-bezier(.4,0,.2,1)` | Motion / Easing Token |
| `--ease-button-focus` | `cubic-bezier(.32,.72,0,1)` | Motion / Easing Token |
| `--ease-fold` | `cubic-bezier(.625,.05,0,1)` | Motion / Easing Token |
| `--ease-overlay` | `cubic-bezier(.19,1,.22,1)` | Motion / Easing Token |
| `--ease-progress` | `cubic-bezier(.33,1,.68,1)` | Motion / Easing Token |
| `--ease-ambient` | `cubic-bezier(.42,0,.58,1)` | Motion / Easing Token |
| `--ease-flow-fade` | `cubic-bezier(.33,.67,.67,1)` | Motion / Easing Token |
| `--logo-w` | `136.5px` | Dimension / Scale Token |
| `--logo-h` | `26px` | Dimension / Scale Token |
| `--dur-micro` | `.12s` | Motion / Timing Token |
| `--dur-fast` | `.18s` | Motion / Timing Token |
| `--dur-state` | `.24s` | Motion / Timing Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.glass-bar> — `atmos-gallery`)**:
   - Landmark `<header class="glass-bar">` hosting `Atmos Gallery · Image Colour Palette` navigation (`Privacy Privacy · Terms Terms`), DOM attributes (`data-landing-cover`, `data-theme="light"`, `data-bytes="23488"`, `data-bytes="24820"`), and stylesheet rule `.site-foot { padding:0 var(--page-gutter,24px) }`.
2. **Hero Stage & Focal Lead (<section.lenis-stopped> — `Colour Read from Light and Atmosph`)**:
   - Landmark `<section class="lenis-stopped">` presenting display lead `Colour Read from Light and Atmosphere. In Seconds.` and copy excerpt *"Skip to Main Content"* over `#f5f5f3` canvas and `#1a1a1a` ink.
3. **Primary Showcase & Content Grid (<section.boot-inner> — `Library`)**:
   - Landmark `<section class="boot-inner">` rendering section `Library` with copy *"Colour Read from Light and Atmosphere."*, asset references (`atmos-gallery-fav.png`, `NeueMontreal-Regular.woff2`, `NeueMontreal-Medium.woff2`, `gsap.min.js`), and grid rule `.site-foot__brand { padding:44px 0 24px }`.
4. **Interactive Detail & Feature Matrix (<section.boot-row> — `Start here`)**:
   - Landmark `<section class="boot-row">` framing `Start here` and `Atmos Gallery` (*"How it Works How it Works"*) with `#fff` surface cards, `#1a1a1a` accents, and `.site-foot__brand a { line-height:0;text-decoration:none;display:block }`.
5. **Colophon & Global Directory Footer (<footer.site-foot> — `https://atmos.gallery`)**:
   - Landmark `<footer class="site-foot">` anchoring `Atmos Gallery · Image Colour Pal` footer links (`Privacy Privacy · Terms Terms`), copy *"Privacy Settings Privacy Settings"*, and `#ff6e62` structural dividers.
