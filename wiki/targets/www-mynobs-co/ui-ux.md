# UI & UX Architecture: www-mynobs-co

## Overview & Design Identity
- **Target**: `www-mynobs-co` (**NoBS - No Brief Shit**)
- **Production URL**: [https://www.mynobs.co](https://www.mynobs.co)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#7E5AF2` canvas, `#FACC15` ink, `#EC4899` accent)
- **Summary**: 💩 It's simple: drop in the buzzword-stuffed brief, and NoBS cuts the BS, handing back only what you need to know to start your job.
- **Total Clean CSS Variables Extracted**: `25` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Sugra`
- **Body Font Stack**: `Sugra Fallback`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `.hero-title` (`font-size: 150px`, `line-height: 0.92`, `letter-spacing: 5px`, `font-weight: normal`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `14px`, `12px`, `9px`, `22px`, `11px`)
- **Body Copy**: CSS variables `--fs-body: 18px`, `--lh-body: 1.55`
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `14px`, `12px`, `9px`, `22px`, `11px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#7E5AF2` | `var(--purple)` in `:root` |
| **Primary Typography Ink** | `#5B3BC4` | `var(--purple-deep)` in `:root` |
| **Elevated Surface / Card Substrate** | `#2D1B69` | `var(--purple-dark)` in `:root` |
| **Interactive Accent / Highlight** | `#EC4899` | `var(--pink)` in `:root` |
| **Secondary / Muted Copy** | `#FACC15` | `var(--yellow)` in `:root` |
| **Structural Hairline Border** | `#C2A011` | `var(--yellow-deep)` in `:root` |
| **Variable Token (`--peach-deep`)** | `#C2691A` | `var(--peach-deep)` in `:root` |
| **Variable Token (`--pink-deep`)** | `#B8276F` | `var(--pink-deep)` in `:root` |
| **Variable Token (`--peach`)** | `#FB923C` | `var(--peach)` in `:root` |
| **Variable Token (`--lime`)** | `#84CC16` | `var(--lime)` in `:root` |
| **Variable Token (`--sky`)** | `#0EA5E9` | `var(--sky)` in `:root` |
| **Variable Token (`--cream`)** | `#FCFAF7` | `var(--cream)` in `:root` |
| **Variable Token (`--cream-darker`)** | `#F5F1E8` | `var(--cream-darker)` in `:root` |
| **Variable Token (`--ink`)** | `#0A0A0A` | `var(--ink)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--purple` | `#7E5AF2` | Color / Atmospheric Token |
| `--purple-deep` | `#5B3BC4` | Color / Atmospheric Token |
| `--purple-dark` | `#2D1B69` | Canvas / Surface Token |
| `--pink` | `#EC4899` | Typography Ink Token |
| `--yellow` | `#FACC15` | Color / Atmospheric Token |
| `--yellow-deep` | `#C2A011` | Color / Atmospheric Token |
| `--peach-deep` | `#C2691A` | Color / Atmospheric Token |
| `--pink-deep` | `#B8276F` | Typography Ink Token |
| `--peach` | `#FB923C` | Color / Atmospheric Token |
| `--lime` | `#84CC16` | Color / Atmospheric Token |
| `--sky` | `#0EA5E9` | Color / Atmospheric Token |
| `--cream` | `#FCFAF7` | Color / Atmospheric Token |
| `--cream-darker` | `#F5F1E8` | Canvas / Surface Token |
| `--ink` | `#0A0A0A` | Typography Ink Token |
| `--fs-body` | `18px` | Dimension / Scale Token |
| `--lh-body` | `1.55` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.nbs-topbar> — `www-mynobs-co`)**:
   - Landmark `<header class="nbs-topbar">` hosting `NoBS - No Brief Shit` navigation (`Exit demo · New brief · WHAT IS NoBS · Drop a brief · Play Brief Toss`), DOM attributes (`data-nobs-sentry-sdk="1"`, `data-page="login"`, `data-auth="out"`, `data-nav="exit-demo"`), and stylesheet rule `html { font-synthesis: none; -webkit-font-smoothing: antialiased; -moz-osx-font... }`.
2. **Hero Stage & Focal Lead (<section.hero> — `IF YOUR BRIEF IS A LET'S CUT THE B`)**:
   - Landmark `<section class="hero">` presenting display lead `IF YOUR BRIEF IS A LET'S CUT THE BS` and copy excerpt *"💩 FOLLOW US ON IG @nobriefshit 💩"* over `#7E5AF2` canvas and `#FACC15` ink.
3. **Primary Showcase & Content Grid (<section.hero> — `Forgot ?`)**:
   - Landmark `<section class="hero">` rendering section `Forgot ?` with copy *"Type, paste, or drop your brief. No Brief Shit (or N o BS , if we"*, asset references (`favicon.svg`, `fonts.googleapis.com`, `fonts.gstatic.com`, `css2`), and grid rule `body { font-family: 'Inter', sans-serif; color: var(--ink); background: var(--c... }`.
4. **Interactive Detail & Feature Matrix (<section.hero> — `C💩💩KIES Yes, we use some.`)**:
   - Landmark `<section class="hero">` framing `C💩💩KIES Yes, we use some.` and `Forgot my password` (*"Forgot my password"*) with `#2D1B69` surface cards, `#EC4899` accents, and `.page-back-wrap { display: block; width: 100%; text-align: center; margin-top: var(--page-... }`.
5. **Colophon & Global Directory Footer (<footer.nbs-footer> — `https://www.mynobs.co`)**:
   - Landmark `<footer class="nbs-footer">` anchoring `NoBS - No Brief Shit` footer links (`Exit demo · New brief · WHAT IS NoBS · Drop a brief · Play Brief Toss`), copy *"Drop your email. If we know it, you'll get a reset link in t"*, and `#C2A011` structural dividers.
