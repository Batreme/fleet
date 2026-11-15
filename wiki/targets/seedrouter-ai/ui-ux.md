# UI & UX Architecture: seedrouter-ai

## Overview & Design Identity
- **Target**: `seedrouter-ai` (**SeedRouter · One API for Image, Video, LLM and Audio Models**)
- **Production URL**: [https://seedrouter.ai](https://seedrouter.ai)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#fef2f2` canvas, `#e40014` ink, `#ff6568` accent)
- **Summary**: SeedRouter puts image, video, language and audio models behind one API key with pay-per-request billing. Failed requests cost nothing. Ge...
- **Total Clean CSS Variables Extracted**: `373` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `JetBrains Mono`
- **Body Font Stack**: `JetBrains Mono Fallback`
- **Monospace / Technical Font Stack**: `JetBrains Mono`
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`; rule `h1` (`letter-spacing: -.025em`, `font-weight: 500`)
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`; rule `,h2` (`letter-spacing: -.02em`, `font-weight: 400`)
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`, `--font-body-ext: "Nunito Sans", "Nunito Sans Fallback"`
- **Metadata & Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fef2f2` | `var(--color-red-50)` in `:root` |
| **Primary Typography Ink** | `#ffe2e2` | `var(--color-red-100)` in `:root` |
| **Elevated Surface / Card Substrate** | `#ffa3a3` | `var(--color-red-300)` in `:root` |
| **Interactive Accent / Highlight** | `#ff6568` | `var(--color-red-400)` in `:root` |
| **Secondary / Muted Copy** | `#fb2c36` | `var(--color-red-500)` in `:root` |
| **Structural Hairline Border** | `#e40014` | `var(--color-red-600)` in `:root` |
| **Variable Token (`--color-red-700`)** | `#bf000f` | `var(--color-red-700)` in `:root` |
| **Variable Token (`--color-red-950`)** | `#460809` | `var(--color-red-950)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--shimmer-angle` | `20deg` | Design System Custom Token |
| `--scroll-fade-t` | `0px` | Dimension / Scale Token |
| `--scroll-fade-b` | `0px` | Dimension / Scale Token |
| `--scroll-fade-s` | `0px` | Dimension / Scale Token |
| `--scroll-fade-e` | `0px` | Dimension / Scale Token |
| `--scroll-fade-mask` | `initial` | Design System Custom Token |
| `--shimmer-image` | `initial` | Design System Custom Token |
| `--shimmer-text-fill` | `initial` | Typography Ink Token |
| `--color-red-50` | `#fef2f2` | Brand / Palette Token |
| `--color-red-100` | `#ffe2e2` | Brand / Palette Token |
| `--color-red-300` | `#ffa3a3` | Brand / Palette Token |
| `--color-red-400` | `#ff6568` | Brand / Palette Token |
| `--color-red-500` | `#fb2c36` | Brand / Palette Token |
| `--color-red-600` | `#e40014` | Brand / Palette Token |
| `--color-red-700` | `#bf000f` | Brand / Palette Token |
| `--color-red-950` | `#460809` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.sr-chrome> — `seedrouter-ai`)**:
   - Landmark `<header class="sr-chrome sticky">` hosting `SeedRouter · One API for Image, Vide` navigation (`SeedRouter · Models · Pricing · Docs · Sign up`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-testid="announcement-dismiss"`, `data-nimg="1"`), and stylesheet rule `host { --shimmer-angle:20deg }`.
2. **Hero Stage & Focal Lead (<section.sr-hero> — `SeedRouter: one API for every mode`)**:
   - Landmark `<section class="sr-hero sr-chrome-dark">` presenting display lead `SeedRouter: one API for every model your product...` and copy excerpt *"Seedance 2.5 is live on SeedRouter Try Seedance 2.5"* over `#fef2f2` canvas and `#e40014` ink.
3. **Primary Showcase & Content Grid (<section.pb-16> — `Models you can call on SeedRouter `)**:
   - Landmark `<section class="pb-16 pt-10">` rendering section `Models you can call on SeedRouter today` with copy *"Seedance 2.5 is live on SeedRouter"*, asset references (`0c8c4ded07fff55c-s.p.2tcyrya9o07v...`, `1b99372b3eaef0c8-s.p.1gsd1jahc5dg...`, `70bc3e132a0a741e-s.p.3t6q91iet4ns...`, `bytedance.svg`), and grid rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.py-16> — `Integration in 4 steps`)**:
   - Landmark `<section class="py-16">` framing `Integration in 4 steps` and `Sign up` (*"01 · Image, video, language and audio · one key"*) with `#ffa3a3` surface cards, `#ff6568` accents, and `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
5. **Colophon & Global Directory Footer (<footer.sr-chrome-dark> — `https://seedrouter.ai`)**:
   - Landmark `<footer class="sr-chrome-dark relative">` anchoring `SeedRouter · One API for Image, ` footer links (`SeedRouter · Models · Pricing · Docs · Sign up`), copy *"one API for every model your product needs"*, and `#e40014` structural dividers.
