# UI & UX Architecture: houseofgiants-com

## Overview & Design Identity
- **Target**: `houseofgiants-com` (**House of Giants · Product engineering partner**)
- **Production URL**: [https://houseofgiants.com](https://houseofgiants.com)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#0000` canvas, `#ffffff` ink, `#ffffff` accent)
- **Summary**: House of Giants designs and builds software products. We help you work out what to build, build it, and keep improving it.
- **Total Clean CSS Variables Extracted**: `188` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Archivo Black`
- **Body Font Stack**: `Geist Mono`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **Hero Display (`H1`)**: CSS variables `--text-5xl: 3rem`, `--text-5xl--line-height: 1`, `--text-display: clamp(3rem, 2.296rem + 3.005vw, 5rem)`
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`; rule `h2` (`font-size: var(--text-title-sm)`, `line-height: var(--text-title-sm--...`, `letter-spacing: var(--text-title-sm--...`)
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`, `--font-hog-body: "IBM Plex Sans", ui-sans-serif, system-ui, sans-serif`
- **Metadata & Labels**: CSS variables `--font-mono: var(--font-hog-mono)`, `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#0000` | `textarea { background-color: #0000 }` |
| **Primary Typography Ink** | `#ffffff` | `.thing-mark__white { fill: white }` (`#ffffff`) |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-mono` | `var(--font-hog-mono)` | Typography / Scale Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--container-md` | `28rem` | Layout / Spatial Grid Token |
| `--container-3xl` | `48rem` | Layout / Spatial Grid Token |
| `--container-7xl` | `80rem` | Layout / Spatial Grid Token |
| `--text-xs` | `.75rem` | Typography Ink Token |
| `--text-xs--line-height` | `calc(1 / .75)` | Typography Ink Token |
| `--text-sm` | `.875rem` | Typography Ink Token |
| `--text-sm--line-height` | `calc(1.25 / .875)` | Typography Ink Token |
| `--text-base` | `1rem` | Typography Ink Token |
| `--text-base--line-height` | `calc(1.5 / 1)` | Typography Ink Token |
| `--text-lg` | `1.125rem` | Typography Ink Token |
| `--text-lg--line-height` | `calc(1.75 / 1.125)` | Typography Ink Token |
| `--text-xl` | `1.25rem` | Typography Ink Token |
| `--text-xl--line-height` | `calc(1.75 / 1.25)` | Typography Ink Token |
| `--text-2xl` | `1.5rem` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-navigation> — `houseofgiants-com`)**:
   - Landmark `<header class="site-navigation absolute">` hosting `House of Giants · Product engineerin` navigation (`Work · How we decide · Services · Pricing · About`), DOM attributes (`data-precedence="default"`, `data-precedence="default"`, `data-status="active"`, `data-footprint-ready`), and stylesheet rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.home-hero> — `Big Ideas. Serious Software.`)**:
   - Landmark `<section class="home-hero px-4">` presenting display lead `Big Ideas. Serious Software.` and copy excerpt *"Request a fit call"* over `#0000` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<section.home-selected-work> — `The Living Proof`)**:
   - Landmark `<section class="home-selected-work bg-moss">` rendering section `The Living Proof` with copy *"We build software, systems and processes for teams that are sick "*, asset references (`thing-walk.svg`, `thing-tufts.svg`, `boulder.svg`, `thing-footprint-right.svg`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.home-process> — `Booking system app`)**:
   - Landmark `<section class="home-process overflow-clip">` framing `Booking system app` and `Cybersecurity buyer intelligence platform` (*"Request a Free Fit Call"*) with `#0000` surface cards, `#ffffff` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://houseofgiants.com`)**:
   - Landmark `<footer class="site-footer">` anchoring `House of Giants · Product engine` footer links (`Work · How we decide · Services · Pricing · About`), copy *"We've worked with hundreds of amazing brands over the years."*, and `#ffffff` structural dividers.
