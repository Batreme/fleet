# UI & UX Architecture: www-ataccama-com_fwrd2026

## Overview & Design Identity
- **Target**: `www-ataccama-com_fwrd2026` (**Ataccama FWRD 2026: Press play on what's next in data trust · Ataccama**)
- **Production URL**: [https://www.ataccama.com/fwrd2026](https://www.ataccama.com/fwrd2026)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#0d6efd` / `#fd7e14`)
- **Summary**: Rewind through the shifts in data quality, agentic data management, and governed context that shaped trusted AI in 2026, then fast-forwar...
- **Total Clean CSS Variables Extracted**: `323` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Poppins`
- **Body Font Stack**: `212529`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `,.h1` (`font-size: clamp(2.75rem,2.4vw + 1.58rem...`, `line-height: 1.2`, `font-weight: 400!important`)
- **Section Heading (`H2`)**: rule `,.h2` (`font-size: clamp(1.75rem,1.6vw + .97rem,...`, `line-height: 1.2`, `font-weight: 400!important`)
- **Body Copy**: CSS variables `--bs-body-font-size: 1rem`, `--bs-body-font-weight: 400`, `--bs-body-line-height: 1.5`; rule `p` (`font-size: 18px`, `line-height: 1.5`)
- **Metadata & Labels**: rule `small` (`font-weight: normal`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#0d6efd` | `var(--bs-blue)` in `:root` |
| **Primary Typography Ink** | `#6610f2` | `var(--bs-indigo)` in `:root` |
| **Elevated Surface / Card Substrate** | `#dc3545` | `var(--bs-red)` in `:root` |
| **Interactive Accent / Highlight** | `#fd7e14` | `var(--bs-orange)` in `:root` |
| **Secondary / Muted Copy** | `#ffc107` | `var(--bs-yellow)` in `:root` |
| **Structural Hairline Border** | `#198754` | `var(--bs-green)` in `:root` |
| **Variable Token (`--bs-teal`)** | `#20c997` | `var(--bs-teal)` in `:root` |
| **Variable Token (`--bs-cyan`)** | `#0dcaf0` | `var(--bs-cyan)` in `:root` |
| **Variable Token (`--bs-gray`)** | `#6c757d` | `var(--bs-gray)` in `:root` |
| **Variable Token (`--bs-gray-dark`)** | `#343a40` | `var(--bs-gray-dark)` in `:root` |
| **Variable Token (`--bs-gray-100`)** | `#f8f9fa` | `var(--bs-gray-100)` in `:root` |
| **Variable Token (`--bs-gray-200`)** | `#e9ecef` | `var(--bs-gray-200)` in `:root` |
| **Variable Token (`--bs-gray-300`)** | `#dee2e6` | `var(--bs-gray-300)` in `:root` |
| **Variable Token (`--bs-gray-400`)** | `#ced4da` | `var(--bs-gray-400)` in `:root` |
| **Variable Token (`--bs-gray-500`)** | `#adb5bd` | `var(--bs-gray-500)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bs-blue` | `#0d6efd` | Color / Atmospheric Token |
| `--bs-indigo` | `#6610f2` | Color / Atmospheric Token |
| `--bs-red` | `#dc3545` | Color / Atmospheric Token |
| `--bs-orange` | `#fd7e14` | Color / Atmospheric Token |
| `--bs-yellow` | `#ffc107` | Color / Atmospheric Token |
| `--bs-green` | `#198754` | Color / Atmospheric Token |
| `--bs-teal` | `#20c997` | Color / Atmospheric Token |
| `--bs-cyan` | `#0dcaf0` | Color / Atmospheric Token |
| `--bs-gray` | `#6c757d` | Color / Atmospheric Token |
| `--bs-gray-dark` | `#343a40` | Canvas / Surface Token |
| `--bs-gray-100` | `#f8f9fa` | Color / Atmospheric Token |
| `--bs-gray-200` | `#e9ecef` | Color / Atmospheric Token |
| `--bs-gray-300` | `#dee2e6` | Color / Atmospheric Token |
| `--bs-gray-400` | `#ced4da` | Color / Atmospheric Token |
| `--bs-gray-500` | `#adb5bd` | Color / Atmospheric Token |
| `--bs-gray-600` | `#6c757d` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.position-relative> — `www-ataccama-com_fwrd2026`)**:
   - Landmark `<header class="position-relative overflow-hidden">` hosting `Ataccama FWRD 2026: Press play on wh` navigation (`Register now`), DOM attributes (`data-hubspot-styled-components`, `data-wp-strategy="defer"`, `data-lottie-intro-src="/dist/images/other/an..."`, `data-lottie-loop-src="/dist/images/other/an..."`), and stylesheet rule `.container { max-width:1168px }`.
2. **Hero Stage & Focal Lead (<section.bg-white> — `Press play on what’s next in data `)**:
   - Landmark `<section class="bg-white overflow-hidden">` presenting display lead `Press play on what’s next in data trust` and copy excerpt *"NOV 5 · 10 AM ET · VIRTUAL"* over `#0d6efd` canvas and `#ffc107` ink.
3. **Primary Showcase & Content Grid (<section.pb-56> — `Hear from the leaders moving data `)**:
   - Landmark `<section class="pb-56 pb-sm-120">` rendering section `Hear from the leaders moving data and AI FWRD` with copy *"Join hundreds of data leaders at our biggest event of the year. L"*, asset references (`main-DPilGSmv.css`, `cdnjs.cloudflare.com`, `feed`, `embed`), and grid rule `root { --bs-breakpoint-xs: 0;--bs-breakpoint-sm: 780px;--bs-breakpoint-md: 1280px }`.
4. **Interactive Detail & Feature Matrix (<section.bg-navy> — `Isaac Gabay`)**:
   - Landmark `<section class="bg-navy overflow-hidden">` framing `Isaac Gabay` and `Camilla Björkqvist` (*"You're joining speakers and attendees from:"*) with `#dc3545` surface cards, `#fd7e14` accents, and `.col { flex:1 0 0 }`.
5. **Colophon & Global Directory Footer (<footer.page-id-13449> — `https://www.ataccama.com/fwrd2026`)**:
   - Landmark `<footer class="page-id-13449">` anchoring `Ataccama FWRD 2026: Press play o` footer links (`Register now`), copy *"Get an inside look at how data and AI strategies are evolvin"*, and `#198754` structural dividers.
