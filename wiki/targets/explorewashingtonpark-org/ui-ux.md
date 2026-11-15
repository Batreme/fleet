# UI & UX Architecture: explorewashingtonpark-org

## Overview & Design Identity
- **Target**: `explorewashingtonpark-org` (**Explore Washington Park**)
- **Production URL**: [https://explorewashingtonpark.org](https://explorewashingtonpark.org)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f3c73e` canvas, `#243746` ink, `#aac0d2` accent)
- **Summary**: Washington Park in Portland, Oregon is home to the Oregon Zoo, Hoyt Arboretum, world-class gardens, museums, and miles of trails. Find ho...
- **Total Clean CSS Variables Extracted**: `1364` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `squarespace-ui-font`
- **Body Font Stack**: `FlodeskSans`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--sqsp-heading-1-color: hsla(var(--black-hsl),1)`, `--heading-1-size: 3.76rem`, `--heading-1-size-value: 3.76`; rule `.title` (`letter-spacing: .5px`, `font-weight: 500`)
- **Section Heading (`H2`)**: CSS variables `--image-block-collage-image-subtitle-color: hsla(var(--black-hsl),1)`, `--image-block-card-image-subtitle-color: hsla(var(--black-hsl),1)`, `--image-block-poster-image-subtitle-color: hsla(var(--white-hsl),1)`; rule `h2` (`font-size: 1.88em`)
- **Body Copy**: CSS variables `--paragraphSmallColor: hsla(var(--black-hsl),1)`, `--sqsp-paragraph-3-color: hsla(var(--black-hsl),1)`, `--paragraphLargeColor: hsla(var(--black-hsl),1)`; rule `p` (`line-height: 1.4`)
- **Metadata & Labels**: CSS variables `--itinerary-meta-text: #000`, `--it2-time-label-value-text: #24322b`, `--it2-slider-label-text: #24322b`; rule `.caption` (`font-size: 12px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#f3c73e` | `var(--yellow)` in `:root` |
| **Primary Typography Ink** | `#9bbd3c` | `var(--green)` in `:root` |
| **Elevated Surface / Card Substrate** | `#dc6638` | `var(--red)` in `:root` |
| **Interactive Accent / Highlight** | `#aac0d2` | `var(--blue)` in `:root` |
| **Secondary / Muted Copy** | `#7a8ea3` | `var(--mediumblue)` in `:root` |
| **Structural Hairline Border** | `#243746` | `var(--navy)` in `:root` |
| **Variable Token (`--darkgreen`)** | `#404d2e` | `var(--darkgreen)` in `:root` |
| **Variable Token (`--rollinghillsgreen`)** | `#869646` | `var(--rollinghillsgreen)` in `:root` |
| **Variable Token (`--black`)** | `#313232` | `var(--black)` in `:root` |
| **Variable Token (`--brown`)** | `#2e2925` | `var(--brown)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--palette-1` | `hsla(var(--white-hsl), 1)` | Brand / Palette Token |
| `--palette-2` | `hsla(var(--lightAccent-hsl), 1)` | Brand / Palette Token |
| `--palette-3` | `hsla(var(--accent-hsl), 1)` | Brand / Palette Token |
| `--palette-4` | `hsla(var(--darkAccent-hsl), 1)` | Brand / Palette Token |
| `--palette-5` | `hsla(var(--black-hsl), 1)` | Brand / Palette Token |
| `--yellow` | `#f3c73e` | Color / Atmospheric Token |
| `--green` | `#9bbd3c` | Color / Atmospheric Token |
| `--red` | `#dc6638` | Color / Atmospheric Token |
| `--blue` | `#aac0d2` | Color / Atmospheric Token |
| `--offwhite` | `linen` | Canvas / Surface Token |
| `--mediumblue` | `#7a8ea3` | Color / Atmospheric Token |
| `--navy` | `#243746` | Layout / Spatial Grid Token |
| `--darkgreen` | `#404d2e` | Canvas / Surface Token |
| `--rollinghillsgreen` | `#869646` | Color / Atmospheric Token |
| `--black` | `#313232` | Canvas / Surface Token |
| `--brown` | `#2e2925` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.white> — `explorewashingtonpark-org`)**:
   - Landmark `<header class="white header">` hosting `Explore Washington Park` navigation (`Plan Your Visit · Explore The Park`), DOM attributes (`data-tippy-stylesheet`, `data-name="static-context"`, `data-tawk-font-preconnect`, `data-animation-state="booted"`), and stylesheet rule `.list-item-content { padding:44px }`.
2. **Hero Stage & Focal Lead (<section.page-section> — `Portland’s Premier Park`)**:
   - Landmark `<section class="page-section full-bleed-section">` presenting display lead `Portland’s Premier Park` and copy excerpt *"Know Before You Go"* over `#f3c73e` canvas and `#243746` ink.
3. **Primary Showcase & Content Grid (<section.page-section> — `7 Spots to See Fall Color for Free`)**:
   - Landmark `<section class="page-section full-bleed-section">` rendering section `7 Spots to See Fall Color for Free` with copy *"Parking fills fast, and payment is required at all lots. The Wash"*, asset references (`twk-main.js`, `announcement-bar-ff2c04748aa19f8b...`, `popup-overlay-f39ec8cdc95ccd84-mi...`, `popup-overlay-7afaba259a8e252a-mi...`), and grid rule `.list-item-content__button-container { padding-top:22px }`.
4. **Interactive Detail & Feature Matrix (<section.page-section> — `Reservoir & Reflecting Pools Are N`)**:
   - Landmark `<section class="page-section full-bleed-section">` framing `Reservoir & Reflecting Pools Are Now Open` and `TriMet Gets You Here Faster` (*"Washington Park Free Shuttle"*) with `#dc6638` surface cards, `#aac0d2` accents, and `.accordion-title .text { text-overflow:unset !important }`.
5. **Colophon & Global Directory Footer (<footer.sections> — `https://explorewashingtonpark.org`)**:
   - Landmark `<footer class="sections">` anchoring `Explore Washington Park` footer links (`Plan Your Visit · Explore The Park`), copy *"View Parking Availability"*, and `#243746` structural dividers.
