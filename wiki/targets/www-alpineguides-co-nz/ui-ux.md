# UI & UX Architecture: www-alpineguides-co-nz

## Overview & Design Identity
- **Target**: `www-alpineguides-co-nz` (**Alpine Guides Aoraki · NZ Mountain Guiding Since 1966**)
- **Production URL**: [https://www.alpineguides.co.nz/](https://www.alpineguides.co.nz/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#fcb124` canvas, `#1e1e1e` ink, `#dad9d9` accent)
- **Summary**: Explore guided ascents, mountaineering courses, ski touring, Tasman Glacier heli-hike and alpine adventures in Aoraki/Mount Cook with pro...
- **Total Clean CSS Variables Extracted**: `234` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Mozillaheadline Variablefont Wdth Wght`
- **Body Font Stack**: `Robotocondensed`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--_responsive---h1: 7rem`, `--_responsive---h1-line-height: .5rem`; rule `h1` (`font-size: 2em`)
- **Section Heading (`H2`)**: CSS variables `--_responsive---h2: 3rem`; rule `h2` (`font-size: 32px`, `line-height: 36px`)
- **Body Copy**: CSS variables `--_responsive---paragraph: 1.4rem`, `--_responsive---paragraph_small: 1rem`; rule `body` (`font-size: 14px`, `line-height: 20px`)
- **Metadata & Labels**: CSS variables `--_text-syle---letter-spacing: 0rem`, `--_responsive---spacer-small: .7rem`, `--_responsive---paragraph_small: 1rem`; rule `small` (`font-size: 80%`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fcb124` | `var(--_theme---agl-gold)` in `:root` |
| **Primary Typography Ink** | `#f2f2f3` | `var(--_theme---white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#1e1e1e` | `var(--_theme---carbon)` in `:root` |
| **Interactive Accent / Highlight** | `#dad9d9` | `var(--_theme---cloud)` in `:root` |
| **Secondary / Muted Copy** | `#888` | `var(--_theme---ash)` in `:root` |
| **Structural Hairline Border** | `#343435` | `var(--_theme---graphite)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--w-backdrop-animation` | `initial` | Motion / Easing Token |
| `--_text-syle---font-family` | `Robotocondensed, Arial, sans-serif` | Typography Ink Token |
| `--_theme---color--heading` | `var(--_theme---white)` | Typography Ink Token |
| `--_responsive---h1` | `7rem` | Typography / Scale Token |
| `--_text-syle---line-height` | `1.25` | Typography Ink Token |
| `--_text-syle---font-weight` | `200` | Typography Ink Token |
| `--_text-syle---letter-spacing` | `0rem` | Typography Ink Token |
| `--_responsive---h2` | `3rem` | Typography / Scale Token |
| `--_theme---color--eyebrow` | `var(--_theme---agl-gold)` | Brand / Palette Token |
| `--_text-syle---text-size` | `var(--_responsive---paragraph)` | Typography Ink Token |
| `--_theme---color--text` | `var(--_theme---white)` | Typography Ink Token |
| `--_responsive---paragraph` | `1.4rem` | Typography / Scale Token |
| `--_theme---agl-gold` | `#fcb124` | Brand / Palette Token |
| `--_theme---color--border` | `var(--_theme---ash)` | Brand / Palette Token |
| `--_theme---color--background` | `var(--_theme---black)` | Canvas / Surface Token |
| `--_theme---white` | `#f2f2f3` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.w-mod-js> — `www-alpineguides-co-nz`)**:
   - Landmark `<header class="w-mod-js">` hosting `Alpine Guides Aoraki · NZ Mountain G` navigation (`prepare · contact us · alpine hiking · learn the ropes · guided ascents`), DOM attributes (`data-wf-domain="www.alpineguides.co.nz"`, `data-wf-page="6948a91537f8a4167b84e785"`, `data-wf-site="6948a91537f8a4167b84e770"`, `data-page="home"`), and stylesheet rule `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`.
2. **Hero Stage & Focal Lead (<section.explore-mega> — `Expert Mountain Adventures Since 1`)**:
   - Landmark `<section class="explore-mega">` presenting display lead `Expert Mountain Adventures Since 1966` and copy excerpt *"Explore With The Experts"* over `#fcb124` canvas and `#1e1e1e` ink.
3. **Primary Showcase & Content Grid (<section.prepare-mega> — `From glaciers to legendary ascents`)**:
   - Landmark `<section class="prepare-mega">` rendering section `From glaciers to legendary ascents, our NZMGA/IFM...` with copy *"tasman glacier adventures"*, asset references (`cdn.prod.website-files.com`, `alpine-guides.webflow.shared.ac09...`, `www-widgetapi.js`, `recaptcha__en.js`), and grid rule `body { margin: 0; }`.
4. **Interactive Detail & Feature Matrix (<section.c-hero> — `Trips Worth Checking Out`)**:
   - Landmark `<section class="c-hero">` framing `Trips Worth Checking Out` and `Where We Guide` (*"private guiding · bespoke trips"*) with `#1e1e1e` surface cards, `#dad9d9` accents, and `summary { display: block; }`.
5. **Colophon & Global Directory Footer (<footer.footer> — `https://www.alpineguides.co.nz/`)**:
   - Landmark `<footer class="footer">` anchoring `Alpine Guides Aoraki · NZ Mounta` footer links (`prepare · contact us · alpine hiking · learn the ropes · guided ascents`), copy *"ski the southern alps"*, and `#343435` structural dividers.
