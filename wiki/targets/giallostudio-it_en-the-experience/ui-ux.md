# UI & UX Architecture: giallostudio-it_en-the-experience

## Overview & Design Identity
- **Target**: `giallostudio-it_en-the-experience` (**The Experience: Milan lights up in yellow · Giallo**)
- **Production URL**: [https://giallostudio.it/en/the-experience](https://giallostudio.it/en/the-experience)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#050608` canvas, `#f2f1ea` ink, `#fb2c36` accent)
- **Summary**: A 3D journey over Milan, from the office where data is still copied by hand to a city lighting up in yellow. See what you could automate...
- **Total Clean CSS Variables Extracted**: `118` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `satoshi`
- **Body Font Stack**: `satoshi Fallback`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`font-size: clamp(2rem,4vw,3.5rem)`, `line-height: 1`, `font-weight: 600`)
- **Body Copy**: CSS variables `--xp-body: clamp(1.02rem, min(1.25vw, 2.3vh), 1.3rem)`, `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`; rule `p` (`line-height: var(--leading-relaxed)`)
- **Metadata & Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#050608` | `var(--ink)` in `:root` |
| **Primary Typography Ink** | `#f2f1ea` | `var(--paper)` in `:root` |
| **Elevated Surface / Card Substrate** | `#f5f505` | `var(--yellow)` in `:root` |
| **Interactive Accent / Highlight** | `#fb2c36` | `var(--color-red-500)` in `:root` |
| **Secondary / Muted Copy** | `#e40014` | `var(--color-red-600)` in `:root` |
| **Structural Hairline Border** | `#bf000f` | `var(--color-red-700)` in `:root` |
| **Variable Token (`--muted`)** | `#f2f1eabd` | `var(--muted)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
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
| `--font-satoshi` | `"satoshi", "satoshi Fallback", Inter, system-ui, sans-serif` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.fixed> — `giallostudio-it_en-the-experience`)**:
   - Landmark `<header class="fixed inset-x-0">` hosting `The Experience: Milan lights up in y` navigation (`Law firms Law firms · Retail Retail · Tourism Tourism · PMI PMI`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-cursor="hover"`), and stylesheet rule `.wa6Phq_stage { position:relative }`.
2. **Hero Stage & Focal Lead (<section.wa6Phq_chapter> — `One window still lit.`)**:
   - Landmark `<section class="wa6Phq_chapter">` presenting display lead `One window still lit.` and copy excerpt *"Skip the experience"* over `#050608` canvas and `#f2f1ea` ink.
3. **Primary Showcase & Content Grid (<section.wa6Phq_chapter> — `The work nobody sees.`)**:
   - Landmark `<section class="wa6Phq_chapter">` rendering section `The work nobody sees.` with copy *"The 3D didn't start on this device, so here's the simplified vers"*, asset references (`Satoshi_Variable-s.p.2ta4m073o532...`, `logo-black.svg`, `logo-solid-black.svg`, `logo-white.svg`), and grid rule `.wa6Phq_canvas { display:none }`.
4. **Interactive Detail & Feature Matrix (<section.wa6Phq_chapter> — `We'll take it from here.`)**:
   - Landmark `<section class="wa6Phq_chapter">` framing `We'll take it from here.` and `Then the rest lights up.` (*"The 3D didn't start on this device, so here's the simplified vers"*) with `#f5f505` surface cards, `#fb2c36` accents, and `.wa6Phq_hud { position:relative }`.
5. **Colophon & Global Directory Footer (<footer.relative> — `https://giallostudio.it/en/the-experience`)**:
   - Landmark `<footer class="relative overflow-hidden">` anchoring `The Experience: Milan lights up ` footer links (`Law firms Law firms · Retail Retail · Tourism Tourism · PMI PMI`), copy *"Someone is copying data from a PDF into Excel. Line by line."*, and `#bf000f` structural dividers.
