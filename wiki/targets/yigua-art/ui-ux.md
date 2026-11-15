# UI & UX Architecture: yigua-art

## Overview & Design Identity
- **Target**: `yigua-art` (**一卦**)
- **Production URL**: [https://yigua.art/?lang=en](https://yigua.art/?lang=en)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f3f0e8` canvas, `#171815` ink, `#171815` accent)
- **Summary**: 讓卦回到卦。一次起卦，只呈現卦象與原典；解讀留給你。
- **Total Clean CSS Variables Extracted**: `60` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Yigua Korean`
- **Body Font Stack**: `Songti TC`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: rule `h1` (`line-height: 1.12`, `letter-spacing: .025em`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(1.65rem,3vw,2.2rem)`, `letter-spacing: .12em`, `font-weight: 500`)
- **Body Copy**: rule `p` (`letter-spacing: .02em`)
- **Metadata & Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#f3f0e8` | `var(--paper)` in `:root` |
| **Primary Typography Ink** | `#e8e3d7` | `var(--paper-deep)` in `:root` |
| **Elevated Surface / Card Substrate** | `#f8f6ef` | `var(--paper-light)` in `:root` |
| **Interactive Accent / Highlight** | `#171815` | `var(--ink)` in `:root` |
| **Secondary / Muted Copy** | `#65645e` | `var(--ink-soft)` in `:root` |
| **Structural Hairline Border** | `#d6d0c4` | `var(--line)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-sans` | `var(--font-interface)` | Typography / Scale Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--text-xs` | `.75rem` | Typography Ink Token |
| `--text-xs--line-height` | `calc(1 / .75)` | Typography Ink Token |
| `--text-sm` | `.875rem` | Typography Ink Token |
| `--text-sm--line-height` | `calc(1.25 / .875)` | Typography Ink Token |
| `--font-weight-medium` | `500` | Typography / Scale Token |
| `--radius-md` | `calc(var(--radius) * .8)` | Elevation / Border Token |
| `--ease-out` | `cubic-bezier(0, 0, .2, 1)` | Motion / Easing Token |
| `--default-transition-duration` | `.15s` | Motion / Easing Token |
| `--default-transition-timing-function` | `cubic-bezier(.4, 0, .2, 1)` | Motion / Easing Token |
| `--default-font-family` | `var(--font-interface)` | Typography / Scale Token |
| `--default-mono-font-family` | `var(--font-mono)` | Typography / Scale Token |
| `--paper` | `#f3f0e8` | Canvas / Surface Token |
| `--paper-deep` | `#e8e3d7` | Canvas / Surface Token |
| `--paper-light` | `#f8f6ef` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `yigua-art`)**:
   - Landmark `<header class="site-header">` hosting `一卦` navigation (`64 Hexagrams · About Yi Gua · Privacy · Developer · Researchers`), DOM attributes (`data-locale="en"`, `data-startup-lifecycle-bound="true"`, `data-startup-booted="true"`, `data-text-size="medium"`), and stylesheet rule `before { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.casting-experience> — `Let the hexagram remain itself.`)**:
   - Landmark `<section class="casting-experience">` presenting display lead `Let the hexagram remain itself.` and copy excerpt *"One casting. Only the figure and original text; the interpretatio"* over `#f3f0e8` canvas and `#171815` ink.
3. **Primary Showcase & Content Grid (<section.casting-experience> — `One casting. Only the figure and o`)**:
   - Landmark `<section class="casting-experience">` rendering section `One casting. Only the figure and original text; ` with copy *"One casting. Only the figure and original text;"*, asset references (`index.B1O6CZI_.css`, `index-BdTq9GkK.js`, `rolldown-runtime-C60lm6uB.js`, `framework-D_rUT4EX.js`), and grid rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.casting-experience> — `One casting. Only the figure and o`)**:
   - Landmark `<section class="casting-experience">` framing `One casting. Only the figure and original text;` and `the interpretation is yours.` (*"the interpretation is yours."*) with `#f8f6ef` surface cards, `#171815` accents, and `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://yigua.art/?lang=en`)**:
   - Landmark `<footer class="site-footer">` anchoring `一卦` footer links (`64 Hexagrams · About Yi Gua · Privacy · Developer · Researchers`), copy *"Version 1.4.31 · Updated 2026-11-04 CC BY 4.0 · Original pre"*, and `#d6d0c4` structural dividers.
