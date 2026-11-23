---
title: "UI & UX Architecture: reapi-ai_models-gpt-image-2-5"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: reapi-ai_models-gpt-image-2-5

## Overview & Design Identity
- **Target**: `reapi-ai_models-gpt-image-2-5` (**GPT Image 2.5 — Sharper Detail, Precise Editing**)
- **Production URL**: [https://reapi.ai/models/gpt-image-2-5](https://reapi.ai/models/gpt-image-2-5)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f7f5f1` / `#4a55cf`)
- **Summary**: GPT Image 2.5 is OpenAI's image generation and editing model with precision edits, reference fidelity and two speed tiers. Pay per image...
- **Total Clean CSS Variables Extracted**: `363` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `TASA Orbiter`
- **Body Font Stack**: `TASA Orbiter`
- **Monospace / Technical Font Stack**: `Space Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 30px`, `line-height: 37.5px`, `font-weight: 600`); CSS variables `--font-display-family: "Source Serif 4",Georgia,Times New Roman,serif`, `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5/2.25)`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 38px`, `line-height: 39.9px`, `font-weight: 600`, `letter-spacing: -0.95px`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2/1.5)`, `--text-3xl: 1.875rem`
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5/1)`, `--cpk-text-base: 1rem`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--font-mono-family: "Space Mono",ui-monospace,Menlo,monospace`, `--text-xs: .75rem`, `--text-xs--line-height: calc(1/.75)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f7f5f1` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#1f2033` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#fffdf8` | `var(--card)` in `:root` |
| **Interactive Accent / Highlight** | `#4a55cf` | `var(--brand-ink)` in `:root` |
| **Secondary / Muted Copy** | `#6b6a63` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#e2ded4` | `var(--border)` in `:root` |
| **Variable Token (`--primary`)** | `#5b66de` | `var(--primary)` in `:root` |
| **Variable Token (`--primary-foreground`)** | `#ffffff` | `var(--primary-foreground)` in `:root` |
| **Variable Token (`--secondary`)** | `#f0ede6` | `var(--secondary)` in `:root` |
| **Variable Token (`--accent`)** | `#ece8df` | `var(--accent)` in `:root` |
| **Variable Token (`--destructive`)** | `#e5484d` | `var(--destructive)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--background` | `#f7f5f1` | Canvas / Surface Token |
| `--foreground` | `#1f2033` | Typography Ink Token |
| `--card` | `#fffdf8` | Color / Atmospheric Token |
| `--card-foreground` | `#1f2033` | Typography Ink Token |
| `--popover` | `#fffdf8` | Color / Atmospheric Token |
| `--popover-foreground` | `#1f2033` | Typography Ink Token |
| `--primary` | `#5b66de` | Brand / Palette Token |
| `--primary-foreground` | `#fff` | Typography Ink Token |
| `--brand-ink` | `#4a55cf` | Typography Ink Token |
| `--secondary` | `#f0ede6` | Brand / Palette Token |
| `--secondary-foreground` | `#1f2033` | Typography Ink Token |
| `--muted` | `#f0ede6` | Color / Atmospheric Token |
| `--muted-foreground` | `#6b6a63` | Typography Ink Token |
| `--accent` | `#ece8df` | Brand / Palette Token |
| `--accent-foreground` | `#1f2033` | Typography Ink Token |
| `--destructive` | `#e5484d` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.inset-x-0> — `reapi-ai_models-gpt-image-2-5`)**:
   - Landmark `<header class="inset-x-0 top-0">` (`1440x74px`) hosting `GPT Image 2.5 — Sharper Detail, Prec` navigation (`r reAPI · Models · Agent · Pricing · Blog`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-site-id="7398c367fb45"`, `data-orientation="horizontal"`), and stylesheet rule `.typeface-sans { --font-sans-family:"TASA Orbiter",-apple-system,PingFang SC,Microsoft Ya... }`.
2. **Hero Stage & Focal Lead (<section.bg-background> — `GPT Image 2.5 — Sharper Detail, Pr`)**:
   - Landmark `<section class="bg-background relative">` presenting display lead `GPT Image 2.5 — Sharper Detail, Precise Editing` and copy excerpt *"GPT Image 2.5 is OpenAI's current image generation and editing mo"* over `#f7f5f1` canvas and `#1f2033` ink.
3. **Primary Showcase & Content Grid (<section.max-w-7xl> — `See what it generates`)**:
   - Landmark `<section class="max-w-7xl pt-2">` rendering section `See what it generates` with copy *"Transparent background"*, asset references (`2d53b00a79aaa16a.css`, `677a55ff8491e63d.css`, `b0188cb2d6a2b515.js`, `28b987a7ce424c5b.js`), and grid rule `.typeface-mono { --font-mono-family:"Space Mono",ui-monospace,Menlo,monospace }`.
4. **Interactive Detail & Feature Matrix (<section.border-b> — `What is GPT Image 2.5?`)**:
   - Landmark `<section class="border-b">` framing `What is GPT Image 2.5?` and `3 generation modes on one endpoint` (*"Custom sizes to 4K"*) with `#fffdf8` surface cards, `#4a55cf` accents, and `.typeface-display { --font-display-family:"Source Serif 4",Georgia,Times New Roman,serif }`.
5. **Colophon & Global Directory Footer (<footer.border-t> — `https://reapi.ai/models/gpt-image-2-5`)**:
   - Landmark `<footer class="border-t">` anchoring `GPT Image 2.5 — Sharper Detail, ` footer links (`r reAPI · Models · Agent · Pricing · Blog`), copy *"$0.02 - 0.02 per image"*, and `#e2ded4` structural dividers.
