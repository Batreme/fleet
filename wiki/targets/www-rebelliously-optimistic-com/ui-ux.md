# UI & UX Architecture: www-rebelliously-optimistic-com

## Overview & Design Identity
- **Target**: `www-rebelliously-optimistic-com` (**Rebelliously Optimistic — A movement for the human future**)
- **Production URL**: [https://www.rebelliously-optimistic.com/](https://www.rebelliously-optimistic.com/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#e5e7eb` / `#fff9`)
- **Summary**: A movement for the human future in the age of AI. Quarterly gatherings and Human Notes for people who refuse to let progress be anything...
- **Total Clean CSS Variables Extracted**: `5` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Bebas Neue`
- **Body Font Stack**: `Instrument Sans`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `1.5rem`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `1.5rem`)
- **Body Copy**: rule `p` (`font-size: calc(6em + 13.3px)`, `font-weight: 400`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `1.5rem`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#e5e7eb` | `:after { border: #e5e7eb }` |
| **Primary Typography Ink** | `#9ca3af` | `input::-moz-placeholder { color: #9ca3af }` |
| **Elevated Surface / Card Substrate** | `#fff3` | `20 { border-color: #fff3 }` |
| **Interactive Accent / Highlight** | `#fff9` | `60 { border-color: #fff9 }` |
| **Secondary / Muted Copy** | `#0003` | `20 { background-color: #0003 }` |
| **Structural Hairline Border** | `#0000` | `.bg-transparent { background-color: #0000 }` |
| **Variable Token (`--line`)** | `#3e1c2a40` | `var(--line)` in `:root` |
| **Variable Token (`--line-soft`)** | `#3e1c2a1f` | `var(--line-soft)` in `:root` |
| **Variable Token (`--line-faint`)** | `#3e1c2a14` | `var(--line-faint)` in `:root` |
| **Variable Token (`--line-cream`)** | `#f3ebd938` | `var(--line-cream)` in `:root` |
| **Variable Token (`--line-cream-soft`)** | `#f3ebd91f` | `var(--line-cream-soft)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--line` | `#3e1c2a40` | Color / Atmospheric Token |
| `--line-soft` | `#3e1c2a1f` | Color / Atmospheric Token |
| `--line-faint` | `#3e1c2a14` | Color / Atmospheric Token |
| `--line-cream` | `#f3ebd938` | Color / Atmospheric Token |
| `--line-cream-soft` | `#f3ebd91f` | Color / Atmospheric Token |
| `--tw-border-spacing-x` | `0` | Layout / Spatial Grid Token |
| `--tw-border-spacing-y` | `0` | Layout / Spatial Grid Token |
| `--tw-translate-x` | `0` | Design System Custom Token |
| `--tw-translate-y` | `0` | Design System Custom Token |
| `--tw-rotate` | `0` | Design System Custom Token |
| `--tw-skew-x` | `0` | Design System Custom Token |
| `--tw-skew-y` | `0` | Design System Custom Token |
| `--tw-scale-x` | `1` | Design System Custom Token |
| `--tw-scale-y` | `1` | Design System Custom Token |
| `--www-rebelliously-bg` | `#e5e7eb` | Canvas Substrate (from `:after { border: #e5e7eb }`) |
| `--www-rebelliously-ink` | `#fff3` | Primary Typography Ink (stylesheet-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.fixed> — `www-rebelliously-optimistic-com`)**:
   - Landmark `<header class="fixed top-0">` hosting `Rebelliously Optimistic — A movement` navigation (`The Experience · Human Notes`), DOM attributes (`data-sdkn="@vercel/analytics/react"`, `data-sdkv="2.0.1"`, `data-engine="three.js r184"`), and stylesheet rule `after { box-sizing:border-box;border:0 solid e5e7eb }`.
2. **Hero Stage & Focal Lead (<section.hidden> — `Our Story`)**:
   - Landmark `<section class="hidden relative">` presenting display lead `Our Story` and copy excerpt *"Rebelliously Optimistic."* over `#e5e7eb` canvas and `#fff3` ink.
3. **Primary Showcase & Content Grid (<section.relative> — `Four commitments. One movement.`)**:
   - Landmark `<section class="relative w-full">` rendering section `Four commitments. One movement.` with copy *"Become a partner Partner"*, asset references (`favicon.svg`, `favicon-32.png`, `favicon-16.png`, `apple-touch-icon.png`), and grid rule `body { line-height:inherit;margin:0 }`.
4. **Interactive Detail & Feature Matrix (<section.relative> — `Build human-first`)**:
   - Landmark `<section class="relative z-10">` framing `Build human-first` and `the Experience` (*"Elevating shared humanity in the age of AI."*) with `#fff3` surface cards, `#fff9` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.sticky> — `https://www.rebelliously-optimistic.com/`)**:
   - Landmark `<footer class="sticky bottom-0">` anchoring `Rebelliously Optimistic — A move` footer links (`The Experience · Human Notes`), copy *"W r i t e i t i n a h u m a n v o i c e ."*, and `#0000` structural dividers.
