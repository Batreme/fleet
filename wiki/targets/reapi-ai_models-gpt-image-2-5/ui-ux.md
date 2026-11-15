# UI & UX Architecture: reapi-ai_models-gpt-image-2-5

## Overview & Design Identity
- **Target**: `reapi-ai_models-gpt-image-2-5` (**GPT Image 2.5 — Sharper Detail, Precise Editing**)
- **Production URL**: [https://reapi.ai/models/gpt-image-2-5](https://reapi.ai/models/gpt-image-2-5)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fef2f2` / `#ffa3a3`)
- **Summary**: GPT Image 2.5 is OpenAI's image generation and editing model with precision edits, reference fidelity and two speed tiers. Pay per image...
- **Total Clean CSS Variables Extracted**: `425` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `TASA Orbiter`
- **Body Font Stack**: `Space Mono`
- **Monospace / Technical Font Stack**: `Space Mono`
- **Hero Display (`H1`)**: CSS variables `--font-display-family: "Source Serif 4",Georgia,Times New Roman,serif`, `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5/2.25)`
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2/1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`font-size: 1.75rem`)
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5/1)`, `--cpk-text-base: 1rem`
- **Metadata & Labels**: CSS variables `--font-mono-family: "Space Mono",ui-monospace,Menlo,monospace`, `--text-xs: .75rem`, `--text-xs--line-height: calc(1/.75)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fef2f2` | `var(--color-red-50)` in `:root` |
| **Primary Typography Ink** | `#ffe2e2` | `var(--color-red-100)` in `:root` |
| **Elevated Surface / Card Substrate** | `#ffcaca` | `var(--color-red-200)` in `:root` |
| **Interactive Accent / Highlight** | `#ffa3a3` | `var(--color-red-300)` in `:root` |
| **Secondary / Muted Copy** | `#ff6568` | `var(--color-red-400)` in `:root` |
| **Structural Hairline Border** | `#fb2c36` | `var(--color-red-500)` in `:root` |
| **Variable Token (`--color-red-600`)** | `#e40014` | `var(--color-red-600)` in `:root` |
| **Variable Token (`--color-red-700`)** | `#bf000f` | `var(--color-red-700)` in `:root` |
| **Variable Token (`--color-red-800`)** | `#9f0712` | `var(--color-red-800)` in `:root` |
| **Variable Token (`--color-orange-300`)** | `#ffb96d` | `var(--color-orange-300)` in `:root` |
| **Variable Token (`--color-orange-400`)** | `#ff8b1a` | `var(--color-orange-400)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-sans-family` | `"TASA Orbiter",-apple-system,PingFang SC,Microsoft YaHei,sans-serif` | Typography / Scale Token |
| `--font-mono-family` | `"Space Mono",ui-monospace,Menlo,monospace` | Typography / Scale Token |
| `--font-display-family` | `"Source Serif 4",Georgia,Times New Roman,serif` | Typography / Scale Token |
| `--font-sans` | `var(--font-sans-family)` | Typography / Scale Token |
| `--font-serif` | `var(--font-display-family)` | Typography / Scale Token |
| `--color-red-50` | `#fef2f2` | Brand / Palette Token |
| `--color-red-100` | `#ffe2e2` | Brand / Palette Token |
| `--color-red-200` | `#ffcaca` | Brand / Palette Token |
| `--color-red-300` | `#ffa3a3` | Brand / Palette Token |
| `--color-red-400` | `#ff6568` | Brand / Palette Token |
| `--color-red-500` | `#fb2c36` | Brand / Palette Token |
| `--color-red-600` | `#e40014` | Brand / Palette Token |
| `--color-red-700` | `#bf000f` | Brand / Palette Token |
| `--color-red-800` | `#9f0712` | Brand / Palette Token |
| `--color-orange-300` | `#ffb96d` | Brand / Palette Token |
| `--color-orange-400` | `#ff8b1a` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.sticky> — `reapi-ai_models-gpt-image-2-5`)**:
   - Landmark `<header class="sticky inset-x-0">` hosting `GPT Image 2.5 — Sharper Detail, Prec` navigation (`r reAPI · Models · Agent · Pricing · Blog`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-site-id="7398c367fb45"`, `data-orientation="horizontal"`), and stylesheet rule `.typeface-sans { --font-sans-family:"TASA Orbiter",-apple-system,PingFang SC,Microsoft Ya... }`.
2. **Hero Stage & Focal Lead (<section.relative> — `GPT Image 2.5 — Sharper Detail, Pr`)**:
   - Landmark `<section class="relative isolate">` presenting display lead `GPT Image 2.5 — Sharper Detail, Precise Editing` and copy excerpt *"GPT Image 2.5 is live — OpenAI's newest image model, targeted edi"* over `#fef2f2` canvas and `#fb2c36` ink.
3. **Primary Showcase & Content Grid (<section.mx-auto> — `See what it generates`)**:
   - Landmark `<section class="mx-auto max-w-7xl">` rendering section `See what it generates` with copy *"Seedance 2.0 Eco — the same 720p / 1080p / 4K delivery on a cheap"*, asset references (`2d53b00a79aaa16a.css`, `b6699761ee55795a.css`, `b0188cb2d6a2b515.js`, `28b987a7ce424c5b.js`), and grid rule `.typeface-mono { --font-mono-family:"Space Mono",ui-monospace,Menlo,monospace }`.
4. **Interactive Detail & Feature Matrix (<section.border-b> — `Pricing`)**:
   - Landmark `<section class="border-b">` framing `Pricing` and `What is GPT Image 2.5?` (*"Seedance 2.0 Eco — the same 720p / 1080p / 4K delivery on a cheap"*) with `#ffcaca` surface cards, `#ffa3a3` accents, and `.typeface-display { --font-display-family:"Source Serif 4",Georgia,Times New Roman,serif }`.
5. **Colophon & Global Directory Footer (<footer.border-t> — `https://reapi.ai/models/gpt-image-2-5`)**:
   - Landmark `<footer class="border-t">` anchoring `GPT Image 2.5 — Sharper Detail, ` footer links (`r reAPI · Models · Agent · Pricing · Blog`), copy *"Seedance 2.5 is live — 30-second cinematic video with native"*, and `#fb2c36` structural dividers.
