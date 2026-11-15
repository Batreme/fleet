# UI & UX Architecture: serus-ai

## Overview & Design Identity
- **Target**: `serus-ai` (**Serus — Agentic Privacy & Intelligence**)
- **Production URL**: [https://serus.ai/](https://serus.ai/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fff0f0` / `#fdd8d8`)
- **Summary**: Your own privacy agent: finds what's exposed, removes it, watches for more and lets you check who you're dealing with. Protection and int...
- **Total Clean CSS Variables Extracted**: `140` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Geist Variable`
- **Body Font Stack**: `Geist Mono Variable`
- **Monospace / Technical Font Stack**: `Geist Mono Variable`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `72px`, `64px`)
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`; rule `h2` (`font-size: 30px`, `line-height: 40px`, `letter-spacing: -.6px`)
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`; rule `p` (`line-height: 1.625`)
- **Metadata & Labels**: CSS variables `--font-mono: "Geist Mono Variable", ui-monospace, monospace`, `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff0f0` | `var(--color-red-100)` in `:root` |
| **Primary Typography Ink** | `#ffebeb` | `var(--color-red-200)` in `:root` |
| **Elevated Surface / Card Substrate** | `#ffe6e6` | `var(--color-red-300)` in `:root` |
| **Interactive Accent / Highlight** | `#fdd8d8` | `var(--color-red-400)` in `:root` |
| **Secondary / Muted Copy** | `#f8b9b9` | `var(--color-red-500)` in `:root` |
| **Structural Hairline Border** | `#f87275` | `var(--color-red-600)` in `:root` |
| **Variable Token (`--color-red-700`)** | `#e5484d` | `var(--color-red-700)` in `:root` |
| **Variable Token (`--color-red-800`)** | `#da2f35` | `var(--color-red-800)` in `:root` |
| **Variable Token (`--color-red-900`)** | `#cb2a2f` | `var(--color-red-900)` in `:root` |
| **Variable Token (`--color-amber-100`)** | `#fff6e6` | `var(--color-amber-100)` in `:root` |
| **Variable Token (`--color-amber-900`)** | `#a35200` | `var(--color-amber-900)` in `:root` |
| **Variable Token (`--color-green-100`)** | `#effbef` | `var(--color-green-100)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-sans` | `"Geist Variable", ui-sans-serif, system-ui, sans-serif` | Typography / Scale Token |
| `--font-mono` | `"Geist Mono Variable", ui-monospace, monospace` | Typography / Scale Token |
| `--color-red-50` | `oklch(97.1% .013 17.38)` | Brand / Palette Token |
| `--color-red-100` | `#fff0f0` | Brand / Palette Token |
| `--color-red-200` | `#ffebeb` | Brand / Palette Token |
| `--color-red-300` | `#ffe6e6` | Brand / Palette Token |
| `--color-red-400` | `#fdd8d8` | Brand / Palette Token |
| `--color-red-500` | `#f8b9b9` | Brand / Palette Token |
| `--color-red-600` | `#f87275` | Brand / Palette Token |
| `--color-red-700` | `#e5484d` | Brand / Palette Token |
| `--color-red-800` | `#da2f35` | Brand / Palette Token |
| `--color-red-900` | `#cb2a2f` | Brand / Palette Token |
| `--color-red-950` | `oklch(25.8% .092 26.042)` | Brand / Palette Token |
| `--color-amber-100` | `#fff6e6` | Brand / Palette Token |
| `--color-amber-900` | `#a35200` | Brand / Palette Token |
| `--color-green-100` | `#effbef` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.sticky> — `serus-ai`)**:
   - Landmark `<header class="sticky top-0">` hosting `Serus — Agentic Privacy & Intelligen` navigation (`People Meet the team · Blog News & guides`), DOM attributes (`data-category="analytics marketing"`, `data-category="analytics"`, `data-astro-cid-nen7h5rs`, `data-nav-menu`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.prot-hero> — `H e l l o , I ' m S e r u s`)**:
   - Landmark `<section class="prot-hero relative">` presenting display lead `H e l l o , I ' m S e r u s` and copy excerpt *"Product Protection Find, monitor & remove your data Intelligence "* over `#fff0f0` canvas and `#f87275` ink.
3. **Primary Showcase & Content Grid (<section.flex-col> — `What to search`)**:
   - Landmark `<section class="flex-col">` rendering section `What to search` with copy *"Protection Find, monitor & remove your data"*, asset references (`23e9b6c532a183c280b129fec77fdf385...`, `favicon.svg`, `apple-touch-icon.png`, `cdn.sanity.io`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.mx-auto> — `Protection`)**:
   - Landmark `<section class="mx-auto px-4">` framing `Protection` and `Surveillance` (*"Find, monitor & remove your data"*) with `#ffe6e6` surface cards, `#fdd8d8` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.px-6> — `https://serus.ai/`)**:
   - Landmark `<footer class="px-6 pb-6">` anchoring `Serus — Agentic Privacy & Intell` footer links (`People Meet the team · Blog News & guides`), copy *"Intelligence Agentic & AI-powered OSINT"*, and `#f87275` structural dividers.
