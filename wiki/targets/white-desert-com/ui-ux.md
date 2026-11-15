# UI & UX Architecture: white-desert-com

## Overview & Design Identity
- **Target**: `white-desert-com` (**Luxury Adventures in Antarctica · White Desert**)
- **Production URL**: [https://white-desert.com/](https://white-desert.com/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#fff` canvas, `#0b0c0f` ink, `#6aa5ff` accent)
- **Summary**: White Desert is the world’s leading luxury Antarctic expedition company, offering once-in-a-lifetime journeys to the South Pole and Emper...
- **Total Clean CSS Variables Extracted**: `117` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter Tight`
- **Body Font Stack**: `Cardinal Classic Long`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `.title` (`font-size: var(--size-225)`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: var(--size-2)`, `line-height: var(--lh-120)`, `font-weight: 500`)
- **Body Copy**: rule `p` (`font-size: 14px`, `line-height: 1.4`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--size-2)`, `var(--size-0625)`, `14px`, `.875rem`, `var(--size-0875)`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--bg)` in `:root` |
| **Primary Typography Ink** | `#12141a` | `var(--surface)` in `:root` |
| **Elevated Surface / Card Substrate** | `#a8acb3` | `var(--muted)` in `:root` |
| **Interactive Accent / Highlight** | `#6aa5ff` | `var(--primary)` in `:root` |
| **Secondary / Muted Copy** | `#0b0c0f` | `var(--primary-contrast)` in `:root` |
| **Structural Hairline Border** | `#1f2330` | `var(--border)` in `:root` |
| **Variable Token (`--quote-accent`)** | `#1f2a44` | `var(--quote-accent)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--pulse-duration` | `2s` | Motion / Easing Token |
| `--pulse-stagger` | `.2s` | Motion / Timing Token |
| `--max-h` | `calc(100svh - var(--space-4)*2 - var(--space-4) - 2.5rem)` | Dimension / Scale Token |
| `--mask-position` | `-40` | Design System Custom Token |
| `--btn-border` | `.03125rem solid rgba(255,255,255,.2)` | Elevation / Border Token |
| `--glass-scale` | `1` | Design System Custom Token |
| `--glass-depth` | `.4` | Design System Custom Token |
| `--glass-highlight` | `rgba(255,255,255,.2)` | Canvas / Surface Token |
| `--bg` | `#fff` | Canvas / Surface Token |
| `--surface` | `#12141a` | Canvas / Surface Token |
| `--text` | `var(--wd_dark-blue)` | Typography Ink Token |
| `--quote-accent` | `var(--WD_Dark-Blue,#1f2a44)` | Brand / Palette Token |
| `--muted` | `#a8acb3` | Color / Atmospheric Token |
| `--primary` | `#6aa5ff` | Brand / Palette Token |
| `--primary-contrast` | `#0b0c0f` | Brand / Palette Token |
| `--border` | `#1f2330` | Elevation / Border Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.lenis> — `white-desert-com`)**:
   - Landmark `<nav class="lenis">` hosting `Luxury Adventures in Antarctica · Wh` navigation (`Rates · Enquire · Home · Enquire now · Dates & Prices`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `.basic-banner_bg { z-index:0;position:absolute;top:0;bottom:0;left:0;right:0 }`.
2. **Hero Stage & Focal Lead (<section.padding-top-large-bottom-medium> — `Antarctica`)**:
   - Landmark `<section class="padding-top-large-bottom-medium m-pb-625">` presenting display lead `Antarctica` and copy excerpt *"Luxury and adventure in the most remote place on Earth"* over `#fff` canvas and `#0b0c0f` ink.
3. **Primary Showcase & Content Grid (<section.tall-parallax-banner> — `Vast, majestic and unimaginably be`)**:
   - Landmark `<section class="tall-parallax-banner">` rendering section `Vast, majestic and unimaginably beautiful — setti...` with copy *"The Last Continent"*, asset references (`cabcbbbe485680be.css`, `7e7f4251c3582625.css`, `5dd7b716df5564d7.css`, `112bdbe21ebfd0e0.css`), and grid rule `.basic-banner_overlay { z-index:1;background-color:rgba(0,0,0,.2);position:absolute;top:0;bottom... }`.
4. **Interactive Detail & Feature Matrix (<section.padding-top-large-bottom-medium> — `Our Trips`)**:
   - Landmark `<section class="padding-top-large-bottom-medium bg-white">` framing `Our Trips` and `Baby Penguins & Blue Tunnels` (*"Between November and February, during the short polar summer, we "*) with `#a8acb3` surface cards, `#6aa5ff` accents, and `.basic-banner_content { z-index:2;width:100%;color:var(--white);text-align:center;position:relative }`.
5. **Colophon & Global Directory Footer (<footer.custom-cursor_dot> — `https://white-desert.com/`)**:
   - Landmark `<footer class="custom-cursor_dot">` anchoring `Luxury Adventures in Antarctica ` footer links (`Rates · Enquire · Home · Enquire now · Dates & Prices`), copy *"Baby Penguins & Blue Tunnels US $75,250 Early Season Witness"*, and `#1f2330` structural dividers.
