# UI & UX Architecture: www-fieldrank-run

## Overview & Design Identity
- **Target**: `www-fieldrank-run` (**FieldRank: Trail and ultra rankings**)
- **Production URL**: [https://www.fieldrank.run](https://www.fieldrank.run)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#faf9f6` ink, `#faf9f6` accent)
- **Summary**: A season ranking of trail and ultra runners, built from race results. Overall and by distance.
- **Total Clean CSS Variables Extracted**: `89` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Geist`
- **Body Font Stack**: `Geist Fallback`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`
- **Metadata & Labels**: CSS variables `--font-mono: var(--font-mono)`, `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#f1efea` | `var(--background)` in `:root` |
| **Elevated Surface / Card Substrate** | `#1e1d1a` | `var(--foreground)` in `:root` |
| **Interactive Accent / Highlight** | `#faf9f6` | `var(--card)` in `:root` |
| **Secondary / Muted Copy** | `#e9e6df` | `var(--secondary)` in `:root` |
| **Structural Hairline Border** | `#66635d` | `var(--muted-foreground)` in `:root` |

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
| `--font-sans` | `var(--font-sans)` | Typography / Scale Token |
| `--font-mono` | `var(--font-mono)` | Typography / Scale Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--container-sm` | `24rem` | Layout / Spatial Grid Token |
| `--container-md` | `28rem` | Layout / Spatial Grid Token |
| `--container-6xl` | `72rem` | Layout / Spatial Grid Token |
| `--text-xs` | `.75rem` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.sticky> — `www-fieldrank-run`)**:
   - Landmark `<header class="sticky top-0">` hosting `FieldRank: Trail and ultra rankings` navigation (`Rankings · Races`), DOM attributes (`data-precedence="next"`, `data-site="KPVLKBUA"`, `data-auto="false"`, `data-slot="button"`), and stylesheet rule `host { --shimmer-angle:20deg }`.
2. **Hero Stage & Focal Lead (<div.light> — `Trail and ultra rankings`)**:
   - Landmark `<div class="light">` presenting display lead `Trail and ultra rankings` and copy excerpt *"Season in progress"* over `#000` canvas and `#faf9f6` ink.
3. **Primary Showcase & Content Grid (<div.min-h-screen> — `Season in progress`)**:
   - Landmark `<div class="min-h-screen">` rendering section `Season in progress` with copy *"A season ranking of trail and ultra runners, built from race resu"*, asset references (`2oz0lep7db5t2.css`, `0jvhpaew_uadu.js`, `script.js`, `19mx3mg6lkumu.js`), and grid rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<div.bg-background> — `A season ranking of trail and ultr`)**:
   - Landmark `<div class="bg-background">` framing `A season ranking of trail and ultra runners, bui` and `Mallorca - CDA 2026` (*"Mallorca - CDA 2026"*) with `#1e1d1a` surface cards, `#faf9f6` accents, and `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
5. **Colophon & Global Directory Footer (<footer.text-foreground> — `https://www.fieldrank.run`)**:
   - Landmark `<footer class="text-foreground">` anchoring `FieldRank: Trail and ultra ranki` footer links (`Rankings · Races`), copy *"2026-11-01 · Valldemossa, Spain · Marathon · 564 results"*, and `#66635d` structural dividers.
