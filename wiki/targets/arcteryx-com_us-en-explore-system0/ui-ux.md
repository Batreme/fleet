# UI & UX Architecture: arcteryx-com_us-en-explore-system0

## Overview & Design Identity
- **Target**: `arcteryx-com_us-en-explore-system0` (**System 0 · Arc’teryx**)
- **Production URL**: [https://arcteryx.com/us/en/explore/system0](https://arcteryx.com/us/en/explore/system0)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#fdfdfd` canvas, `#0c0c0c` ink, `#565656` accent)
- **Summary**: System 0 is the Arc’teryx platform linking our products, services, and guest experience together in a committed, synchronized journey tow...
- **Total Clean CSS Variables Extracted**: `96` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Elan ITC Pro`
- **Body Font Stack**: `Helvetica Now Display`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--font-helvetica-now-display: "Helvetica Now Display", helvetica, sans-serif`, `--type-font-size-display-1: 34px`, `--type-font-size-display-2: 20px`; rule `h1` (`font-size: 1.5rem`, `line-height: 1.2`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 1.5rem`, `line-height: 1.25`)
- **Body Copy**: CSS variables `--type-font-size-body-1: 18px`, `--type-font-size-body-2: 14px`, `--type-line-height-body-1: 22px`; rule `,p` (`line-height: inherit`, `letter-spacing: inherit`, `font-weight: inherit`)
- **Metadata & Labels**: CSS variables `--type-letter-spacing-display-1: .4px`, `--type-letter-spacing-display-2: .4px`, `--type-letter-spacing-body-1: .25px`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fdfdfd` | `html { color: #fdfdfd }` |
| **Primary Typography Ink** | `#0c0c0c` | `html { background: #0c0c0c }` |
| **Elevated Surface / Card Substrate** | `#1f96db` | `-banner-sdk .onetrust-vendors-l... { color: #1f96db }` |
| **Interactive Accent / Highlight** | `#565656` | `#ot-sync-ntfy .ot-pc-footer-log... { color: #565656 }` |
| **Secondary / Muted Copy** | `#fff` | `#ot-sdk-btn.optanon-show-settings { color: #fff }` |
| **Structural Hairline Border** | `#468254` | `#ot-sdk-btn.optanon-show-settings { background-color: #468254 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--dot-overlap-offset-horizontal` | `12px` | Dimension / Scale Token |
| `--dot-overlap-offset-vertical` | `14px` | Dimension / Scale Token |
| `--dot-overlap-offset-relative` | `calc( var(--dot-overlap-offset-horizontal) + .5% )` | Dimension / Scale Token |
| `--circle-size` | `var(--button-circle-small-size)` | Layout / Spatial Grid Token |
| `--circle-border-opacity` | `1` | Elevation / Border Token |
| `--circle-border-interact` | `.2` | Elevation / Border Token |
| `--circle-content-opacity` | `1` | Design System Custom Token |
| `--circle-content-interact` | `1` | Design System Custom Token |
| `--pill-background` | `rgb(26, 26, 26)` | Canvas / Surface Token |
| `--pill-color` | `rgb(253, 253, 253)` | Brand / Palette Token |
| `--pill-background-active` | `rgb(212, 212, 212)` | Canvas / Surface Token |
| `--pill-color-active` | `rgb(12, 12, 12)` | Brand / Palette Token |
| `--pill-background-hover` | `rgb(253, 253, 253)` | Canvas / Surface Token |
| `--pill-color-hover` | `rgb(12, 12, 12)` | Brand / Palette Token |
| `--pill-background-disabled` | `rgb(253, 253, 253)` | Canvas / Surface Token |
| `--pill-color-disabled` | `rgb(212, 212, 212)` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.onetrust-pc-dark-filter> — `arcteryx-com_us-en-explore-system0`)**:
   - Landmark `<header class="onetrust-pc-dark-filter">` hosting `System 0 · Arc’teryx` navigation (`PROCESS · MISSION · SPERRO SV · ARC’TERYX · ReBIRD`), DOM attributes (`data-signup-tag="4467"`, `data-is-header-visible="true"`, `data-document-language="true"`, `data-language-detection="true"`), and stylesheet rule `._container_ybue0_1 { display:grid;width:100% }`.
2. **Hero Stage & Focal Lead (<section.ot-hide> — `The Revolution is Circular`)**:
   - Landmark `<section class="ot-hide">` presenting display lead `The Revolution is Circular` and copy excerpt *"Our journey toward circularity"* over `#fdfdfd` canvas and `#0c0c0c` ink.
3. **Primary Showcase & Content Grid (<section.ot-fade-in> — `Find preferred materials`)**:
   - Landmark `<section class="ot-fade-in">` rendering section `Find preferred materials` with copy *"System 0™ is our platform linking our products, services, and gue"*, asset references (`Loading.zo8phPeo.css`, `footer-with-infinity-loop.BY7Pus-...`, `use-process-exit.mlCI1y1L.css`, `index.K17Bkq0c.css`), and grid rule `._asset_ybue0_9 { opacity:0;transition:opacity .2s cubic-bezier(.42,0,.58,1) }`.
4. **Interactive Detail & Feature Matrix (<section.ot-hide> — `Design for durability`)**:
   - Landmark `<section class="ot-hide ot-pc-scrollbar">` framing `Design for durability` and `Prioritize repairability` (*"we’re changing the way we create and support our products to prot"*) with `#1f96db` surface cards, `#565656` accents, and `._picture_ybue0_18 { display:contents }`.
5. **Colophon & Global Directory Footer (<footer.otRelFont> — `https://arcteryx.com/us/en/explore/system0`)**:
   - Landmark `<footer class="otRelFont">` anchoring `System 0 · Arc’teryx` footer links (`PROCESS · MISSION · SPERRO SV · ARC’TERYX · ReBIRD`), copy *"I. Find preferred materials"*, and `#468254` structural dividers.
