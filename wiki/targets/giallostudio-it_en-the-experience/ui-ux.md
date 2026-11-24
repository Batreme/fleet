---
title: "UI & UX Architecture: giallostudio-it_en-the-experience"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: giallostudio-it_en-the-experience

## Overview & Design Identity
- **Target**: `giallostudio-it_en-the-experience` (**The Experience: Milan lights up in yellow · Giallo**)
- **Production URL**: [https://giallostudio.it/en/the-experience](https://giallostudio.it/en/the-experience)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×6624px`, Mobile `390×2616px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#050608` canvas, `#ffffff` ink, `#f5f505` accent)
- **Summary**: A 3D journey over Milan, from the office where data is still copied by hand to a city lighting up in yellow. See what you could automate...
- **Total Clean CSS Variables Extracted**: `118` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `satoshi`
- **Body Font Stack**: `satoshi`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 146.88px`, `line-height: 135.13px`, `font-weight: 700`, `letter-spacing: -6.6096px`); CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 120.96px`, `line-height: 111.283px`, `font-weight: 700`, `letter-spacing: -5.4432px`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`font-size: clamp(2rem,4vw,3.5rem)`, `line-height: 1`, `font-weight: 600`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 26.4px`, `font-weight: 400`); CSS variables `--xp-body: clamp(1.02rem, min(1.25vw, 2.3vh), 1.3rem)`, `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`; rule `p` (`line-height: var(--leading-relaxed)`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 26.4px`, `font-weight: 400`); CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#050608` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffffff` | live computed `footer` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#000000` | live computed `footer` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#f5f505` | `.hWJL2G_badge { background: #f5f505 }` |
| **Secondary / Muted Copy** | `#f5f505` | `var(--lab-wipe-ink)` in `:root` |
| **Structural Hairline Border** | `#040507` | `var(--lab-line)` in `:root` (`00000021`) |
| **Variable Token (`--paper`)** | `#f2f1ea` | `var(--paper)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-satoshi` | `"satoshi", "satoshi Fallback", Inter, system-ui, sans-serif` | Typography / Scale Token |
| `--ink` | `#050608` | Typography Ink Token |
| `--paper` | `#f2f1ea` | Canvas / Surface Token |
| `--muted` | `#f2f1eabd` | Color / Atmospheric Token |
| `--yellow` | `#f5f505` | Color / Atmospheric Token |
| `--gutter` | `clamp(1.25rem, 5vw, 5.5rem)` | Layout / Spatial Grid Token |
| `--xp-top` | `calc(5rem + env(safe-area-inset-top,0px) + clamp(.75rem, 3.5vh, 2.75rem))` | Dimension / Scale Token |
| `--xp-bottom` | `calc(env(safe-area-inset-bottom,0px) + clamp(1.25rem, 5.5vh, 4rem))` | Dimension / Scale Token |
| `--xp-left` | `max(var(--gutter), calc(env(safe-area-inset-left,0px) + 1rem))` | Dimension / Scale Token |
| `--xp-right` | `max(var(--gutter), calc(env(safe-area-inset-right,0px) + 1rem))` | Dimension / Scale Token |
| `--xp-gap` | `clamp(.7rem, 2.2vh, 1.6rem)` | Layout / Spatial Grid Token |
| `--xp-title` | `clamp(3.4rem, min(8.4vw, 14.5vh), 9.25rem)` | Dimension / Scale Token |
| `--xp-title-hero` | `clamp(3.8rem, min(10.2vw, 16.5vh), 11rem)` | Dimension / Scale Token |
| `--xp-body` | `clamp(1.02rem, min(1.25vw, 2.3vh), 1.3rem)` | Dimension / Scale Token |
| `--sx` | `100%` | Dimension / Scale Token |
| `--sy` | `0%` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.inset-x-0> — `giallostudio-it_en-the-experience`)**:
   - Landmark `<header class="inset-x-0 top-0">` (`1440x81px`) hosting `The Experience: Milan lights up in y` navigation (`Law firms Law firms · Retail Retail · Tourism Tourism · PMI PMI`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-cursor="hover"`), and stylesheet rule `.STp5NW_className { font-family:satoshi,satoshi Fallback,Inter,system-ui,sans-serif }`.
2. **Hero Stage & Focal Lead (<section.wa6Phq_chapter> — `One window still lit.`)**:
   - Landmark `<section class="wa6Phq_chapter">` presenting display lead `One window still lit.` and copy excerpt *"The 3D didn't start on this device, so here's the simplified vers"* over `#050608` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.wa6Phq_chapter:nth(2)> — `The work nobody sees.`)**:
   - Landmark `<section class="wa6Phq_chapter">` rendering section `The work nobody sees.` with copy *"The 3D didn't start on this device, so here's the simplified vers"*, asset references (`Satoshi_Variable-s.p.2ta4m073o532...`, `logo-black.svg`, `logo-solid-black.svg`, `logo-white.svg`), and grid rule `.STp5NW_variable { --font-satoshi:"satoshi", "satoshi Fallback", Inter, system-ui, sans-serif }`.
4. **Interactive Detail & Feature Matrix (<section.wa6Phq_chapter:nth(3)> — `We'll take it from here.`)**:
   - Landmark `<section class="wa6Phq_chapter">` framing `We'll take it from here.` and `Then the rest lights up.` (*"Someone is copying data from a PDF into Excel. Line by line. Like"*) with `#000000` surface cards, `#f5f505` accents, and `.wa6Phq_stage { position:relative }`.
5. **Colophon & Global Directory Footer (<footer.bg-ink> — `https://giallostudio.it/en/the-experience`)**:
   - Landmark `<footer class="bg-ink text-paper">` anchoring `The Experience: Milan lights up ` footer links (`Law firms Law firms · Retail Retail · Tourism Tourism · PMI PMI`), copy *"Lighting up the city"*, and `#040507` structural dividers.
