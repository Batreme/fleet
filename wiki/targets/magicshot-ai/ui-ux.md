---
title: "UI & UX Architecture: magicshot-ai"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: magicshot-ai

## Overview & Design Identity
- **Target**: `magicshot-ai` (**AI Image, Video & Audio Generator all in One Plan**)
- **Production URL**: [https://magicshot.ai](https://magicshot.ai)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×872px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#0a0a0f` canvas, `#ffffff` ink, `#a22bff` accent)
- **Summary**: Generate images, video, and audio with top AI models and countless tools under one subscription. No five tabs, no five invoices, one plan...
- **Total Clean CSS Variables Extracted**: `159` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Archivo`
- **Body Font Stack**: `Archivo`
- **Monospace / Technical Font Stack**: `Martian Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 51.2px`, `line-height: 55.296px`, `font-weight: 800`, `letter-spacing: -1.792px`); CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 48px`, `line-height: 48px`, `font-weight: 700`, `letter-spacing: -1.44px`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`font-size: 1.5rem`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24.8px`, `font-weight: 400`); CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24.8px`, `font-weight: 400`); CSS variables `--font-mono: "Martian Mono", ui-monospace, SFMono-Regular, Menlo, Consolas, monospace`, `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`; rule `small` (`font-size: .625rem`, `letter-spacing: .16em`, `font-weight: 600`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#0a0a0f` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `h2` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#121218` | `var(--color-surface-900)` in `:root` |
| **Interactive Accent / Highlight** | `#a22bff` | `var(--color-brand-500)` in `:root` |
| **Secondary / Muted Copy** | `#8d8999` | `var(--color-ink-400)` in `:root` |
| **Structural Hairline Border** | `#7740a7` | `.key:hover { border-color: #7740a7 }` |

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
   - Landmark `<header class="site-header top-0">` (`1440x65px`) hosting `AI Image, Video & Audio Generator al` navigation (`Image · Video · Photoshoot · Photo Editing · Audio`), DOM attributes (`data-motion`, `data-id="DB8MR53C77UC0DK7DIE0"`, `data-navigate-track="reload"`, `data-navigate-track="reload"`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.section-y> — `Every AI model. One plan. Endless `)**:
   - Landmark `<section class="section-y pt-6">` presenting display lead `Every AI model. One plan. Endless content.` and copy excerpt *"Headshots, product shots, video ads and more, made in seconds fro"* over `#0a0a0f` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.section-y:nth(2)> — `Thanksgiving Feast Challenge is on`)**:
   - Landmark `<section class="section-y">` rendering section `Thanksgiving Feast Challenge is on` with copy *"Thanksgiving Feast Challenge · win 100k credits"*, asset references (`d2q9lphzn5ioni.cloudfront.net`, `favicon-96x96.png`, `favicon.svg`, `favicon.ico`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.section-y:nth(3)> — `Images, video, photoshoots, edits `)**:
   - Landmark `<section class="section-y">` framing `Images, video, photoshoots, edits and audio. One...` and `Generate images from a single prompt` (*"What will you create today?"*) with `#121218` surface cards, `#a22bff` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.border-surface-800> — `https://magicshot.ai`)**:
   - Landmark `<footer class="border-surface-800 bg-surface-950">` anchoring `AI Image, Video & Audio Generato` footer links (`Image · Video · Photoshoot · Photo Editing · Audio`), copy *"See What You Can Make"*, and `#7740a7` structural dividers.
