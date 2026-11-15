# UI & UX Architecture: clipdance-ai

## Overview & Design Identity
- **Target**: `clipdance-ai` (**Seedance 2.0 - Free AI Video Generator · Text/Image to Video**)
- **Production URL**: [https://clipdance.ai](https://clipdance.ai)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fef2f2` / `#ff6568`)
- **Summary**: Create cinematic AI videos with Seedance 2.0. Text-to-video, image-to-video, native audio. The Seedance 2.0 AI video generator. Free to s...
- **Total Clean CSS Variables Extracted**: `287` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `fontInter`
- **Body Font Stack**: `fontInter Fallback`
- **Monospace / Technical Font Stack**: `Noto Sans Mono`
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5/2.25)`, `--text-5xl: 3rem`
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2/1.5)`, `--text-3xl: 1.875rem`
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5/1)`; rule `p` (`line-height: var(--leading-relaxed)`)
- **Metadata & Labels**: CSS variables `--font-noto-sans-mono: "Noto Sans Mono", "Noto Sans Mono Fallback"`, `--text-xs: .75rem`, `--text-xs--line-height: calc(1/.75)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fef2f2` | `var(--color-red-50)` in `:root` |
| **Primary Typography Ink** | `#ffcaca` | `var(--color-red-200)` in `:root` |
| **Elevated Surface / Card Substrate** | `#ffa3a3` | `var(--color-red-300)` in `:root` |
| **Interactive Accent / Highlight** | `#ff6568` | `var(--color-red-400)` in `:root` |
| **Secondary / Muted Copy** | `#fb2c36` | `var(--color-red-500)` in `:root` |
| **Structural Hairline Border** | `#e40014` | `var(--color-red-600)` in `:root` |
| **Variable Token (`--color-red-700`)** | `#bf000f` | `var(--color-red-700)` in `:root` |
| **Variable Token (`--color-red-800`)** | `#9f0712` | `var(--color-red-800)` in `:root` |
| **Variable Token (`--color-red-950`)** | `#460809` | `var(--color-red-950)` in `:root` |
| **Variable Token (`--color-orange-400`)** | `#ff8b1a` | `var(--color-orange-400)` in `:root` |
| **Variable Token (`--color-orange-500`)** | `#fe6e00` | `var(--color-orange-500)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-inter` | `"fontInter", "fontInter Fallback"` | Typography / Scale Token |
| `--font-montserrat` | `"Montserrat", "Montserrat Fallback"` | Typography / Scale Token |
| `--font-unbounded` | `"Unbounded", "Unbounded Fallback"` | Typography / Scale Token |
| `--font-noto-sans-mono` | `"Noto Sans Mono", "Noto Sans Mono Fallback"` | Typography / Scale Token |
| `--font-sans` | `var(--font-inter)` | Typography / Scale Token |
| `--color-red-50` | `#fef2f2` | Brand / Palette Token |
| `--color-red-200` | `#ffcaca` | Brand / Palette Token |
| `--color-red-300` | `#ffa3a3` | Brand / Palette Token |
| `--color-red-400` | `#ff6568` | Brand / Palette Token |
| `--color-red-500` | `#fb2c36` | Brand / Palette Token |
| `--color-red-600` | `#e40014` | Brand / Palette Token |
| `--color-red-700` | `#bf000f` | Brand / Palette Token |
| `--color-red-800` | `#9f0712` | Brand / Palette Token |
| `--color-red-950` | `#460809` | Brand / Palette Token |
| `--color-orange-400` | `#ff8b1a` | Brand / Palette Token |
| `--color-orange-500` | `#fe6e00` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.sticky> — `clipdance-ai`)**:
   - Landmark `<header class="sticky inset-x-0">` hosting `Seedance 2.0 - Free AI Video Generat` navigation (`Seedance 2.5 · Blog · Pricing · My Creations`), DOM attributes (`data-precedence="next"`, `data-href="/_next/static/chunks/..."`, `data-state="closed"`, `data-slot="sheet-trigger"`), and stylesheet rule `nter_a1c1f49b-module__H0XvcG__cla... { font-family:fontInter,fontInter Fallback;font-style:normal }`.
2. **Hero Stage & Focal Lead (<section.relative> — `Free Seedance 2.0 AI Video Generat`)**:
   - Landmark `<section class="relative w-full">` presenting display lead `Free Seedance 2.0 AI Video Generator` and copy excerpt *"Skip to main content"* over `#fef2f2` canvas and `#e40014` ink.
3. **Primary Showcase & Content Grid (<section.w-full> — `Wan 3.0 30% OFF`)**:
   - Landmark `<section class="w-full mx-auto">` rendering section `Wan 3.0 30% OFF` with copy *"We’ve moved. Seedance2.so is now ClipDance.ai — same account, sam"*, asset references (`3455abe1a79cd15c-s.p.2fxd9z3s4zhc...`, `InterVariable-s.p.2c0y96ae70xfx.w...`, `e8f2fbee2754df70-s.p.1dqa_6e_ad4s...`, `seedance.png`), and grid rule `inter_a1c1f49b-module__H0XvcG__va... { --font-inter:"fontInter", "fontInter Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.py-5> — `Get Up to 8,000 Credits Every Mont`)**:
   - Landmark `<section class="py-5">` framing `Get Up to 8,000 Credits Every Month.` and `Popular AI Models` (*"Seedance2.so is now"*) with `#ffa3a3` surface cards, `#ff6568` accents, and `rrat_84fd8339-module__Za0QWW__cla... { font-family:Montserrat,Montserrat Fallback;font-style:normal }`.
5. **Colophon & Global Directory Footer (<footer.border-t> — `https://clipdance.ai`)**:
   - Landmark `<footer class="border-t">` anchoring `Seedance 2.0 - Free AI Video Gen` footer links (`Seedance 2.5 · Blog · Pricing · My Creations`), copy *"— same account, same credits, new address."*, and `#e40014` structural dividers.
