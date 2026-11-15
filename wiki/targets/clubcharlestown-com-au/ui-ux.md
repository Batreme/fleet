# UI & UX Architecture: clubcharlestown-com-au

## Overview & Design Identity
- **Target**: `clubcharlestown-com-au` (**Home · Club Charlestown**)
- **Production URL**: [https://clubcharlestown.com.au/](https://clubcharlestown.com.au/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000000` canvas, `#98A2B3` ink, `#344054` accent)
- **Summary**: We're a vibrant, family-friendly club where everyone belongs. Come in and discover a place to relax, have fun, and connect with friends a...
- **Total Clean CSS Variables Extracted**: `429` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Roboto`
- **Body Font Stack**: `gotham-xnarrow`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--page-title-display: block`, `--display: flex`, `--n-menu-wrapper-display: flex`
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `2.5em`, `100px`, `15px`, `13px`, `16px`)
- **Body Copy**: rule `p` (`font-size: var(--form-desc-size)`)
- **Metadata & Labels**: CSS variables `--label-color: #344054`, `--label-padding: 0px 0px 5px 0px`, `--check-label-color: #1D2939`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | `var(--fieldset-color)` in `:root` |
| **Primary Typography Ink** | `#444444` | `var(--title-color)` in `:root` |
| **Elevated Surface / Card Substrate** | `#98A2B3` | `var(--form-desc-color)` in `:root` |
| **Interactive Accent / Highlight** | `#344054` | `var(--label-color)` in `:root` |
| **Secondary / Muted Copy** | `#F04438` | `var(--required-color)` in `:root` |
| **Structural Hairline Border** | `#667085` | `var(--description-color)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--direction-multiplier` | `1` | Design System Custom Token |
| `--flex-direction` | `initial` | Design System Custom Token |
| `--flex-wrap` | `initial` | Layout / Spatial Grid Token |
| `--justify-content` | `initial` | Design System Custom Token |
| `--align-items` | `initial` | Design System Custom Token |
| `--align-content` | `initial` | Design System Custom Token |
| `--gap` | `initial` | Layout / Spatial Grid Token |
| `--flex-basis` | `initial` | Design System Custom Token |
| `--flex-grow` | `initial` | Design System Custom Token |
| `--flex-shrink` | `initial` | Typography Ink Token |
| `--order` | `initial` | Design System Custom Token |
| `--align-self` | `initial` | Design System Custom Token |
| `--page-title-display` | `block` | Design System Custom Token |
| `--border-radius` | `0` | Elevation / Border Token |
| `--border-top-width` | `0px` | Layout / Spatial Grid Token |
| `--border-right-width` | `0px` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.elementor> — `clubcharlestown-com-au`)**:
   - Landmark `<header class="elementor elementor-27">` hosting `Home · Club Charlestown` navigation (`What's On What's On · What's On · Functions · Courtesy Bus · Bowls Bowls`), DOM attributes (`data-elementor-device-mode="desktop"`, `data-elementor-type="header"`, `data-elementor-id="27"`, `data-elementor-post-type="elementor_library"`), and stylesheet rule `.tk-gotham-xnarrow { font-family: "gotham-xnarrow",sans-serif; }`.
2. **Hero Stage & Focal Lead (<main.site-main> — `Welcome to Club Charlestown`)**:
   - Landmark `<main class="site-main post-7">` presenting display lead `Welcome to Club Charlestown` and copy excerpt *"Club Lambton Venue Club Lambton Venue"* over `#000000` canvas and `#98A2B3` ink.
3. **Primary Showcase & Content Grid (<main.site-main> — `Beyond a Club, It's a Community`)**:
   - Landmark `<main class="site-main post-7">` rendering section `Beyond a Club, It's a Community` with copy *"Club Lambton Venue"*, asset references (`recaptcha__en.js`, `www.googletagmanager.com`, `embed`, `ckx4srt.css`), and grid rule `.tk-gotham-narrow { font-family: "gotham-narrow",sans-serif; }`.
4. **Interactive Detail & Feature Matrix (<main.site-main> — `Club Lambton`)**:
   - Landmark `<main class="site-main post-7">` framing `Club Lambton` and `Where Locals Meet` (*"Drink & Dine Drink & Dine"*) with `#98A2B3` surface cards, `#344054` accents, and `.tk-gotham-condensed { font-family: "gotham-condensed",sans-serif; }`.
5. **Colophon & Global Directory Footer (<footer.elementor> — `https://clubcharlestown.com.au/`)**:
   - Landmark `<footer class="elementor elementor-63">` anchoring `Home · Club Charlestown` footer links (`What's On What's On · What's On · Functions · Courtesy Bus · Bowls Bowls`), copy *"Memberships Memberships"*, and `#667085` structural dividers.
