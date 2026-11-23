---
title: "UI & UX Architecture: seedrouter-ai"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: seedrouter-ai

## Overview & Design Identity
- **Target**: `seedrouter-ai` (**SeedRouter · One API for Image, Video, LLM and Audio Models**)
- **Production URL**: [https://seedrouter.ai](https://seedrouter.ai)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f7f5f1` canvas, `#090e12` ink, `#d1f53b` accent)
- **Summary**: SeedRouter puts image, video, language and audio models behind one API key with pay-per-request billing. Failed requests cost nothing. Ge...
- **Total Clean CSS Variables Extracted**: `377` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Outfit`
- **Body Font Stack**: `Outfit`
- **Monospace / Technical Font Stack**: `JetBrains Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 44.64px`, `line-height: 50.8896px`, `font-weight: 600`, `letter-spacing: -1.7856px`); CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`; rule `h1` (`letter-spacing: -.025em`, `font-weight: 500`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 40.32px`, `line-height: 44.352px`, `font-weight: 600`, `letter-spacing: -1.6128px`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`; rule `,h2` (`letter-spacing: -.02em`, `font-weight: 400`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--font-body-ext: "Nunito Sans", "Nunito Sans Fallback"`, `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--font-mono: var(--font-mono-label)`, `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f7f5f1` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#090e12` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#fffdf8` | `var(--card)` in `:root` |
| **Interactive Accent / Highlight** | `#d1f53b` | `var(--sr-hero-accent)` in `:root` |
| **Secondary / Muted Copy** | `#737373` | `var(--color-fd-muted-foreground)` in `:root` |
| **Structural Hairline Border** | `#e2ded4` | `var(--border)` in `:root` |
| **Variable Token (`--primary`)** | `#18763a` | `var(--primary)` in `:root` |
| **Variable Token (`--secondary`)** | `#ece8df` | `var(--secondary)` in `:root` |
| **Variable Token (`--muted`)** | `#f0ede6` | `var(--muted)` in `:root` |
| **Variable Token (`--muted-foreground`)** | `#6b6a63` | `var(--muted-foreground)` in `:root` |
| **Variable Token (`--destructive`)** | `#d92d20` | `var(--destructive)` in `:root` |
| **Variable Token (`--destructive-foreground`)** | `#ffffff` | `var(--destructive-foreground)` in `:root` |
| **Variable Token (`--input`)** | `#d3cec1` | `var(--input)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--card` | `#fffdf8` | Color / Atmospheric Token |
| `--card-foreground` | `#090e12` | Typography Ink Token |
| `--popover` | `#fffdf8` | Color / Atmospheric Token |
| `--popover-foreground` | `#090e12` | Typography Ink Token |
| `--primary` | `#18763a` | Brand / Palette Token |
| `--primary-foreground` | `#f7f5f1` | Typography Ink Token |
| `--secondary` | `#ece8df` | Brand / Palette Token |
| `--secondary-foreground` | `#090e12` | Typography Ink Token |
| `--muted` | `#f0ede6` | Color / Atmospheric Token |
| `--muted-foreground` | `#6b6a63` | Typography Ink Token |
| `--accent` | `#f0ede6` | Brand / Palette Token |
| `--accent-foreground` | `#090e12` | Typography Ink Token |
| `--destructive` | `#d92d20` | Color / Atmospheric Token |
| `--destructive-foreground` | `#fff` | Typography Ink Token |
| `--border` | `#e2ded4` | Elevation / Border Token |
| `--input` | `#d3cec1` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.sr-chrome> — `seedrouter-ai`)**:
   - Landmark `<header class="sr-chrome inset-x-0">` (`1440x65px`) hosting `SeedRouter · One API for Image, Vide` navigation (`SeedRouter · Models · Pricing · Docs · Sign up`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-testid="announcement-dismiss"`, `data-nimg="1"`), and stylesheet rule `mono_744f2078-module__kLS_DW__cla... { font-family:JetBrains Mono,JetBrains Mono Fallback;font-style:normal }`.
2. **Hero Stage & Focal Lead (<section.sr-hero> — `SeedRouter: one API for every mode`)**:
   - Landmark `<section class="sr-hero sr-chrome-dark">` presenting display lead `SeedRouter: one API for every model your product...` and copy excerpt *"01 · Image, video, language and audio · one key"* over `#f7f5f1` canvas and `#090e12` ink.
3. **Primary Showcase & Content Grid (<section.pb-16> — `Models you can call on SeedRouter `)**:
   - Landmark `<section class="pb-16 pt-12">` rendering section `Models you can call on SeedRouter today` with copy *"Generate and edit video from text or a first frame, at the resolu"*, asset references (`0c8c4ded07fff55c-s.p.2tcyrya9o07v...`, `1b99372b3eaef0c8-s.p.1gsd1jahc5dg...`, `70bc3e132a0a741e-s.p.3t6q91iet4ns...`, `google.svg`), and grid rule `mono_744f2078-module__kLS_DW__var... { --font-code:"JetBrains Mono", "JetBrains Mono Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.py-16> — `Integration in 4 steps`)**:
   - Landmark `<section class="py-16">` framing `Integration in 4 steps` and `Create an API key` (*"$ POST /v1/videos/generations ✓ completed"*) with `#fffdf8` surface cards, `#d1f53b` accents, and `tfit_300d5b1f-module__eNyfuq__cla... { font-family:Outfit,Outfit Fallback;font-style:normal }`.
5. **Colophon & Global Directory Footer (<footer.sr-chrome-dark> — `https://seedrouter.ai`)**:
   - Landmark `<footer class="sr-chrome-dark relative">` anchoring `SeedRouter · One API for Image, ` footer links (`SeedRouter · Models · Pricing · Docs · Sign up`), copy *"$ POST /v1/videos/generations"*, and `#e2ded4` structural dividers.
