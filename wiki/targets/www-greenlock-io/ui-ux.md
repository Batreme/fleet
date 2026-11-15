# UI & UX Architecture: www-greenlock-io

## Overview & Design Identity
- **Target**: `www-greenlock-io` (**Independent Wealth Oversight for Family Offices · GreenLock**)
- **Production URL**: [https://www.greenlock.io](https://www.greenlock.io)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#0c221b` canvas, `#e0faef` ink, `#0f3026` accent)
- **Summary**: GreenLock is a Swiss-based platform offering objective, independent oversight for Single Family Offices. Expose hidden costs, optimize pe...
- **Total Clean CSS Variables Extracted**: `62` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Reckless Neue Licensed`
- **Body Font Stack**: `Reckless Neue`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 2.5rem`, `line-height: 3.375rem`, `font-weight: 600`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 2.5rem`, `line-height: 3.375rem`, `font-weight: 600`)
- **Body Copy**: rule `p` (`font-size: 1.75rem`, `line-height: 3rem`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `2em`, `80%`, `75%`, `1em`, `14px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#0c221b` | `var(--green-700)` in `:root` |
| **Primary Typography Ink** | `#e0faef` | `var(--green-100)` in `:root` |
| **Elevated Surface / Card Substrate** | `#99f4c0` | `var(--green-200)` in `:root` |
| **Interactive Accent / Highlight** | `#0f3026` | `var(--green-600)` in `:root` |
| **Secondary / Muted Copy** | `#94a8a2` | `var(--gray-300)` in `:root` |
| **Structural Hairline Border** | `#5d9c78` | `var(--green-250)` in `:root` |
| **Variable Token (`--transparent`)** | `#0000` | `var(--transparent)` in `:root` |
| **Variable Token (`--gray-500`)** | `#132526` | `var(--gray-500)` in `:root` |
| **Variable Token (`--yellow-200`)** | `#fcf89c` | `var(--yellow-200)` in `:root` |
| **Variable Token (`--purple-400`)** | `#3f328d` | `var(--purple-400)` in `:root` |
| **Variable Token (`--gray-400`)** | `#1f3f32` | `var(--gray-400)` in `:root` |
| **Variable Token (`--gray-100`)** | `#f4f5f3` | `var(--gray-100)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--w-backdrop-animation` | `initial` | Motion / Easing Token |
| `--green-700` | `#0c221b` | Color / Atmospheric Token |
| `--manrope-grotesk` | `Manrope,sans-serif` | Design System Custom Token |
| `--green-100` | `#e0faef` | Color / Atmospheric Token |
| `--white` | `white` | Canvas / Surface Token |
| `--reckless-antiqua` | `"Reckless Neue Licensed",sans-serif` | Design System Custom Token |
| `--green-200` | `#99f4c0` | Color / Atmospheric Token |
| `--green-600` | `#0f3026` | Color / Atmospheric Token |
| `--gray-300` | `#94a8a2` | Color / Atmospheric Token |
| `--green-250` | `#5d9c78` | Color / Atmospheric Token |
| `--transparent` | `#0000` | Color / Atmospheric Token |
| `--gray-500` | `#132526` | Color / Atmospheric Token |
| `--yellow-200` | `#fcf89c` | Color / Atmospheric Token |
| `--purple-400` | `#3f328d` | Color / Atmospheric Token |
| `--gray-400` | `#1f3f32` | Color / Atmospheric Token |
| `--gray-100` | `#f4f5f3` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.w-mod-js> — `www-greenlock-io`)**:
   - Landmark `<header class="w-mod-js">` hosting `Independent Wealth Oversight for Fam` navigation (`Pricing · Insights · About us · Client portal`), DOM attributes (`data-wf-domain="www.greenlock.io"`, `data-wf-page="6816540e936df6252569dd87"`, `data-wf-site="63fca69523dfba725518d390"`, `data-domain="greenlock.io"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
2. **Hero Stage & Focal Lead (<section.v2-header-section> — `Fee`)**:
   - Landmark `<section class="v2-header-section">` presenting display lead `Fee` and copy excerpt *"Fee Benchmarking & Reduction"* over `#0c221b` canvas and `#e0faef` ink.
3. **Primary Showcase & Content Grid (<section.v2-hero-section> — `Benchmarking`)**:
   - Landmark `<section class="v2-hero-section full-height-fix">` rendering section `Benchmarking` with copy *"Investment Performance Audit"*, asset references (`cdn.prod.website-files.com`, `greenlock-site.webflow.shared.26f...`, `fonts.googleapis.com`, `fonts.gstatic.com`), and grid rule `summary { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.v2-ticker-section> — `& Reduction`)**:
   - Landmark `<section class="v2-ticker-section">` framing `& Reduction` and `Investment` (*"PE/VC Portfolio Optimization"*) with `#99f4c0` surface cards, `#0f3026` accents, and `video { vertical-align:baseline;display:inline-block }`.
5. **Colophon & Global Directory Footer (<footer.wf-manrope-n5-active> — `https://www.greenlock.io`)**:
   - Landmark `<footer class="wf-manrope-n5-active">` anchoring `Independent Wealth Oversight for` footer links (`Pricing · Insights · About us · Client portal`), copy *"Real Estate Assets Monitoring"*, and `#5d9c78` structural dividers.
