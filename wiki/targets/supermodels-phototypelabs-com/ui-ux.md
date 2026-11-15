# UI & UX Architecture: supermodels-phototypelabs-com

## Overview & Design Identity
- **Target**: `supermodels-phototypelabs-com` (**SUPERMODELS — Image, Video, Voice & Music, Pay Per Use**)
- **Production URL**: [https://supermodels.phototypelabs.com](https://supermodels.phototypelabs.com)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f7f6f2` / `#000`)
- **Summary**: SUPERMODELS is a creative platform for images, video, voice, music, and text with leading models. Pay per use, with no subscription.
- **Total Clean CSS Variables Extracted**: `123` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Onest`
- **Body Font Stack**: `DM Sans`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--font-display: "Manrope", var(--font-sans)`
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `.75rem`, `.65rem`, `2rem`, `1.4rem`, `clamp(7rem,14vw,14rem)`)
- **Body Copy**: CSS variables `--landing-body-size: .9375rem`
- **Metadata & Labels**: CSS variables `--font-mono: var(--font-sans)`, `--landing-label-size: .75rem`, `--hero-brand-letter-spacing: 0.02em`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#f7f6f2` | `var(--studio-category-color)` in `:root` |
| **Primary Typography Ink** | `#283a2d` | `var(--category-tag-bg)` in `:root` |
| **Elevated Surface / Card Substrate** | `#57d778` | `var(--category-tag-ink)` in `:root` |
| **Interactive Accent / Highlight** | `#000` | `var(--site-frame)` in `:root` |
| **Secondary / Muted Copy** | `#ecebe7` | `var(--editorial-ground)` in `:root` |
| **Structural Hairline Border** | `#171715` | `var(--editorial-ink)` in `:root` |
| **Variable Token (`--landing-on-dark-muted`)** | `#f7f6f2bf` | `var(--landing-on-dark-muted)` in `:root` |
| **Variable Token (`--landing-dark-line`)** | `#f7f6f247` | `var(--landing-dark-line)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--category-dot` | `var(--editorial-paper)` | Design System Custom Token |
| `--landing-content-inset` | `clamp(24px, 4.2vw, 68px)` | Dimension / Scale Token |
| `--paper` | `var(--editorial-paper)` | Canvas / Surface Token |
| `--ink` | `var(--editorial-ink)` | Typography Ink Token |
| `--muted` | `var(--editorial-muted)` | Design System Custom Token |
| `--line` | `var(--editorial-rule)` | Design System Custom Token |
| `--serif` | `var(--font-editorial)` | Typography / Scale Token |
| `--sans` | `var(--font-sans)` | Typography / Scale Token |
| `--headline` | `var(--font-display)` | Design System Custom Token |
| `--font-mono` | `var(--font-sans)` | Typography / Scale Token |
| `--landing-dark` | `var(--editorial-ink)` | Canvas / Surface Token |
| `--landing-on-dark` | `var(--editorial-paper)` | Canvas / Surface Token |
| `--landing-on-dark-muted` | `#f7f6f2bf` | Canvas / Surface Token |
| `--landing-dark-line` | `#f7f6f247` | Canvas / Surface Token |
| `--landing-quiet` | `var(--editorial-paper-quiet)` | Design System Custom Token |
| `--landing-heading-size` | `clamp(2.35rem, 5.2vw, 5.25rem)` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.editorial-header> — `supermodels-phototypelabs-com`)**:
   - Landmark `<header class="editorial-header">` hosting `SUPERMODELS — Image, Video, Voice & ` navigation (`Models · Providers · Pricing · Examples · News`), DOM attributes (`data-landing-brand="SUPERMODELS"`, `data-landing-brand-weight="700"`, `data-landing-brand-spacing="0.02"`, `data-landing-font="Onest"`), and stylesheet rule `webkit-slider-runnable-track { background:0 0;height:.32rem }`.
2. **Hero Stage & Focal Lead (<section.editorial-hero> — `Your ideas. One creative platform.`)**:
   - Landmark `<section class="editorial-hero">` presenting display lead `Your ideas. One creative platform.` and copy excerpt *"Explore leading models for images, video, voice, music, and text."* over `#f7f6f2` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.principles-section> — `Pay per use`)**:
   - Landmark `<section class="principles-section platform-overview">` rendering section `Pay per use` with copy *"Pick a model. Type a prompt. Get a result."*, asset references (`favicon.svg`, `favicon.png`, `favicon.ico`, `apple-touch-icon.png`), and grid rule `moz-range-track { background:0 0;height:.32rem }`.
4. **Interactive Detail & Feature Matrix (<article.editorial-landing> — `Model choice`)**:
   - Landmark `<article class="editorial-landing">` framing `Model choice` and `Batch comparisons` (*"No subscription. Add wallet credit from $10 and see the estimated"*) with `#57d778` surface cards, `#000` accents, and `active::-webkit-slider-thumb { transform:scale(1.24) }`.
5. **Colophon & Global Directory Footer (<footer.creative-footer> — `https://supermodels.phototypelabs.com`)**:
   - Landmark `<footer class="creative-footer">` anchoring `SUPERMODELS — Image, Video, Voic` footer links (`Models · Providers · Pricing · Examples · News`), copy *"Explore about 47 published models from OpenAI, Google, Anthr"*, and `#171715` structural dividers.
