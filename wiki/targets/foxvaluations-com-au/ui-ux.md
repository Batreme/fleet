# UI & UX Architecture: foxvaluations-com-au

## Overview & Design Identity
- **Target**: `foxvaluations-com-au` (**Property valuations Brisbane · Fox Valuations**)
- **Production URL**: [https://foxvaluations.com.au](https://foxvaluations.com.au)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#16202F` canvas, `#FAFAF8` ink, `#FAFAF8` accent)
- **Summary**: Independent property valuations across Brisbane and South East Queensland by registered valuer Sebastian Fox. Fixed fee, quoted free.
- **Total Clean CSS Variables Extracted**: `29` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Instrument Sans`
- **Body Font Stack**: `Mona Sans`
- **Monospace / Technical Font Stack**: `Spline Sans Mono`
- **Hero Display (`H1`)**: CSS variables `--display-ls: -0.032em`; rule `h1` (`font-size: clamp(2.6rem, 6vw, 4.5rem)`, `line-height: 1.04`, `letter-spacing: -0.015em`, `font-weight: 500`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(1.5rem, 2.6vw, 2.05rem)`, `line-height: 1.12`, `letter-spacing: -0.01em`, `font-weight: 500`)
- **Body Copy**: CSS variables `--dark-body: #B8BFC9`; rule `p` (`font-size: 1rem`)
- **Metadata & Labels**: CSS variables `--mono: "Spline Sans Mono", "SF Mono", Consolas, monospace`, `--label: 0.8rem`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#16202F` | `var(--ink)` in `:root` |
| **Primary Typography Ink** | `#1C2839` | `var(--ink-2)` in `:root` |
| **Elevated Surface / Card Substrate** | `#2C3B50` | `var(--ink-line)` in `:root` |
| **Interactive Accent / Highlight** | `#FAFAF8` | `var(--paper)` in `:root` |
| **Secondary / Muted Copy** | `#F1F1ED` | `var(--plaster)` in `:root` |
| **Structural Hairline Border** | `#262E3C` | `var(--graphite)` in `:root` |
| **Variable Token (`--slate`)** | `#5B6473` | `var(--slate)` in `:root` |
| **Variable Token (`--rust`)** | `#B14D2B` | `var(--rust)` in `:root` |
| **Variable Token (`--rust-bright`)** | `#D96B3F` | `var(--rust-bright)` in `:root` |
| **Variable Token (`--line`)** | `#DAD8D0` | `var(--line)` in `:root` |
| **Variable Token (`--dark-body`)** | `#B8BFC9` | `var(--dark-body)` in `:root` |
| **Variable Token (`--dark-dim`)** | `#9AA3B0` | `var(--dark-dim)` in `:root` |
| **Variable Token (`--dark-bright`)** | `#F5F4F0` | `var(--dark-bright)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ink` | `#16202F` | Typography Ink Token |
| `--ink-2` | `#1C2839` | Typography Ink Token |
| `--ink-line` | `#2C3B50` | Typography Ink Token |
| `--paper` | `#FAFAF8` | Canvas / Surface Token |
| `--plaster` | `#F1F1ED` | Color / Atmospheric Token |
| `--graphite` | `#262E3C` | Color / Atmospheric Token |
| `--slate` | `#5B6473` | Color / Atmospheric Token |
| `--rust` | `#B14D2B` | Color / Atmospheric Token |
| `--rust-bright` | `#D96B3F` | Color / Atmospheric Token |
| `--line` | `#DAD8D0` | Color / Atmospheric Token |
| `--dark-body` | `#B8BFC9` | Canvas / Surface Token |
| `--dark-dim` | `#9AA3B0` | Canvas / Surface Token |
| `--dark-bright` | `#F5F4F0` | Canvas / Surface Token |
| `--mono` | `"Spline Sans Mono", "SF Mono", Consolas, monospace` | Typography / Scale Token |
| `--label` | `0.8rem` | Dimension / Scale Token |
| `--shell` | `1240px` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-head> — `foxvaluations-com-au`)**:
   - Landmark `<header class="site-head site-head-cine">` hosting `Property valuations Brisbane · Fox V` navigation (`Valuations · The standard · From the den · Tools · About`), DOM attributes (`data-website-id="dc310766-8aa8-41ef-af..."`, `data-portrait="1"`, `data-slot="svc-residential"`, `data-slot="svc-commercial"`), and stylesheet rule `html { scroll-behavior: smooth }`.
2. **Hero Stage & Focal Lead (<section.landing> — `What is your property worth?`)**:
   - Landmark `<section class="landing">` presenting display lead `What is your property worth?` and copy excerpt *"Request a valuation"* over `#16202F` canvas and `#FAFAF8` ink.
3. **Primary Showcase & Content Grid (<section.cred-strip> — `A figure you can act on.`)**:
   - Landmark `<section class="cred-strip">` rendering section `A figure you can act on.` with copy *"Email the practice"*, asset references (`favicon-rust.png`, `analytics.blackshard.com.au`, `fox-mark-rust.png`, `fox-run-first-v2.webp`), and grid rule `img { display: block;max-width: 100%;height: auto }`.
4. **Interactive Detail & Feature Matrix (<section.standard> — `What do you need valued?`)**:
   - Landmark `<section class="standard standard-band">` framing `What do you need valued?` and `Meet the director` (*"Level 1, 47 Brookes Street, Bowen Hills QLD 4006"*) with `#2C3B50` surface cards, `#FAFAF8` accents, and `focus-visible { outline: 2px solid var(--rust);outline-offset: 3px }`.
5. **Colophon & Global Directory Footer (<footer.site-foot> — `https://foxvaluations.com.au`)**:
   - Landmark `<footer class="site-foot">` anchoring `Property valuations Brisbane · F` footer links (`Valuations · The standard · From the den · Tools · About`), copy *"Independent property valuations by a registered valuer. Bris"*, and `#262E3C` structural dividers.
