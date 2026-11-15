# UI & UX Architecture: magicshot-ai

## Overview & Design Identity
- **Target**: `magicshot-ai` (**AI Image, Video & Audio Generator all in One Plan**)
- **Production URL**: [https://magicshot.ai](https://magicshot.ai)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#d7b0ff` accent)
- **Summary**: Generate images, video, and audio with top AI models and countless tools under one subscription. No five tabs, no five invoices, one plan...
- **Total Clean CSS Variables Extracted**: `147` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Archivo`
- **Body Font Stack**: `Martian Mono`
- **Monospace / Technical Font Stack**: `Martian Mono`
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`font-size: 1.5rem`)
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`
- **Metadata & Labels**: CSS variables `--font-mono: "Martian Mono", ui-monospace, SFMono-Regular, Menlo, Consolas, monospace`, `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#ecd9ff` | `var(--color-brand-100)` in `:root` |
| **Interactive Accent / Highlight** | `#d7b0ff` | `var(--color-brand-200)` in `:root` |
| **Secondary / Muted Copy** | `#c187ff` | `var(--color-brand-300)` in `:root` |
| **Structural Hairline Border** | `#b14dff` | `var(--color-brand-400)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-serif` | `ui-serif, Georgia, Cambria, "Times New Roman", Times, serif` | Typography / Scale Token |
| `--font-mono` | `"Martian Mono", ui-monospace, SFMono-Regular, Menlo, Consolas, monospace` | Typography / Scale Token |
| `--color-red-300` | `oklch(80.8% .114 19.571)` | Brand / Palette Token |
| `--color-red-400` | `oklch(70.4% .191 22.216)` | Brand / Palette Token |
| `--color-red-500` | `oklch(63.7% .237 25.331)` | Brand / Palette Token |
| `--color-amber-300` | `oklch(87.9% .169 91.605)` | Brand / Palette Token |
| `--color-amber-400` | `oklch(82.8% .189 84.429)` | Brand / Palette Token |
| `--color-sky-400` | `oklch(74.6% .16 232.661)` | Brand / Palette Token |
| `--color-blue-300` | `oklch(80.9% .105 251.813)` | Brand / Palette Token |
| `--color-blue-700` | `oklch(48.8% .243 264.376)` | Brand / Palette Token |
| `--color-blue-800` | `oklch(42.4% .199 265.638)` | Brand / Palette Token |
| `--color-gray-50` | `oklch(98.5% .002 247.839)` | Brand / Palette Token |
| `--color-gray-100` | `oklch(96.7% .003 264.542)` | Brand / Palette Token |
| `--color-gray-200` | `oklch(92.8% .006 264.531)` | Brand / Palette Token |
| `--color-gray-300` | `oklch(87.2% .01 258.338)` | Brand / Palette Token |
| `--color-gray-400` | `oklch(70.7% .022 261.325)` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `magicshot-ai`)**:
   - Landmark `<header class="site-header sticky">` hosting `AI Image, Video & Audio Generator al` navigation (`Image · Video · Photoshoot · Photo Editing · Audio`), DOM attributes (`data-motion`, `data-navigate-track="reload"`, `data-navigate-track="reload"`, `data-animate`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.relative> — `Every AI model. One plan. Endless `)**:
   - Landmark `<section class="relative isolate">` presenting display lead `Every AI model. One plan. Endless content.` and copy excerpt *"JUST DROPPED Generate lifelike visuals with Seedream 5.5 ⚡"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.section-y> — `Images, video, photoshoots, edits `)**:
   - Landmark `<section class="section-y">` rendering section `Images, video, photoshoots, edits and audio. One...` with copy *"Generate lifelike visuals with Seedream 5.5 ⚡"*, asset references (`d2q9lphzn5ioni.cloudfront.net`, `favicon-96x96.png`, `favicon.svg`, `favicon.ico`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.section-y> — `Generate images from a single prom`)**:
   - Landmark `<section class="section-y">` framing `Generate images from a single prompt` and `Bring images and ideas to life as video` (*"GPT Image 2.6 Sunburst Faster, consistent edits ⚡"*) with `#ecd9ff` surface cards, `#d7b0ff` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.border-t> — `https://magicshot.ai`)**:
   - Landmark `<footer class="border-t border-surface-800">` anchoring `AI Image, Video & Audio Generato` footer links (`Image · Video · Photoshoot · Photo Editing · Audio`), copy *"GPT Image 2.6 Sunburst"*, and `#b14dff` structural dividers.
