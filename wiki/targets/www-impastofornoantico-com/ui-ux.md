# UI & UX Architecture: www-impastofornoantico-com

## Overview & Design Identity
- **Target**: `www-impastofornoantico-com` (**Handcrafted Bread with Soul - Impasto**)
- **Production URL**: [https://www.impastofornoantico.com/](https://www.impastofornoantico.com/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#efefe7` canvas, `#312426` ink, `#494341` accent)
- **Summary**: Discover Impasto’s soulful, handcrafted bread - Rye, Focaccia, Sourdough. Experience the rhythm of baking with care. Order or contact us...
- **Total Clean CSS Variables Extracted**: `236` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `aaux-next`
- **Body Font Stack**: `ff-scala`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--h1--margin-bottom: var(--space--3)`, `--h1--font-family: var(--all-headings--heading-font-family)`, `--h1--font-size: var(--size--5rem)`
- **Section Heading (`H2`)**: CSS variables `--h2--margin-bottom: var(--space--3)`, `--h2--font-family: var(--all-headings--heading-font-family)`, `--h2--font-size: var(--size--4rem)`
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `2em`, `80%`, `75%`, `1em`, `14px`)
- **Metadata & Labels**: CSS variables `--text-main--letter-spacing: var(--letter-spacing--0em)`, `--h1--letter-spacing: var(--all-headings--heading-letter-spacing)`, `--h2--letter-spacing: var(--all-headings--heading-letter-spacing)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#efefe7` | `var(--swatch--light)` in `:root` |
| **Primary Typography Ink** | `#d9cec3` | `var(--swatch--light-two)` in `:root` |
| **Elevated Surface / Card Substrate** | `#312426` | `var(--swatch--dark)` in `:root` |
| **Interactive Accent / Highlight** | `#494341` | `var(--swatch--dark-three)` in `:root` |
| **Secondary / Muted Copy** | `#9e948a` | `var(--swatch--dark-two)` in `:root` |
| **Structural Hairline Border** | `#0000` | `a { background-color: #0000 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--w-backdrop-animation` | `initial` | Motion / Easing Token |
| `--theme--background` | `var(--swatch--light)` | Canvas / Surface Token |
| `--text-main--font-family` | `var(--font--second-family)` | Typography Ink Token |
| `--theme--text` | `var(--swatch--dark)` | Typography Ink Token |
| `--text-main--font-size` | `1.2rem` | Typography Ink Token |
| `--text-main--line-height` | `var(--line-height--1-5)` | Typography Ink Token |
| `--text-main--font-weight` | `var(--font--primary-regular)` | Typography Ink Token |
| `--text-main--letter-spacing` | `var(--letter-spacing--0em)` | Typography Ink Token |
| `--h1--margin-bottom` | `var(--space--3)` | Typography / Scale Token |
| `--h1--font-family` | `var(--all-headings--heading-font-family)` | Typography / Scale Token |
| `--h1--font-size` | `var(--size--5rem)` | Typography / Scale Token |
| `--h1--line-height` | `var(--all-headings--heading-line-height)` | Typography / Scale Token |
| `--h1--font-weight` | `var(--font--primary-medium)` | Typography / Scale Token |
| `--h1--letter-spacing` | `var(--all-headings--heading-letter-spacing)` | Typography / Scale Token |
| `--h2--margin-bottom` | `var(--space--3)` | Typography / Scale Token |
| `--h2--font-family` | `var(--all-headings--heading-font-family)` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.navigation> — `www-impastofornoantico-com`)**:
   - Landmark `<nav class="navigation">` hosting `Handcrafted Bread with Soul - Impast` navigation (`Home · About · Products · Stockists · Wholesale`), DOM attributes (`data-wf-domain="www.impastofornoantic..."`, `data-wf-page="6774ded4742b832f88f9825e"`, `data-wf-site="6774ded4742b832f88f98269"`, `data-navigation-status="not-active"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
2. **Hero Stage & Focal Lead (<section.hero> — `FOCACCIA`)**:
   - Landmark `<section class="hero">` presenting display lead `FOCACCIA` and copy excerpt *"For generations, the Villani family has followed a time-honored m"* over `#efefe7` canvas and `#312426` ink.
3. **Primary Showcase & Content Grid (<section.scaling-element-header> — `CIABATTA`)**:
   - Landmark `<section class="scaling-element-header">` rendering section `CIABATTA` with copy *"It’s a method rooted in patience, respect for ingredients, and a "*, asset references (`cdn.prod.website-files.com`, `impasto-tag.webflow.shared.02cb07...`, `recaptcha__en.js`, `gvw6vxl.js`), and grid rule `summary { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.scaling-element-video> — `SOURDOUGH`)**:
   - Landmark `<section class="scaling-element-video">` framing `SOURDOUGH` and `From baking bread to breaking bread.` (*"Our ongoing pursuit of quality ensures that our bread evolves wit"*) with `#312426` surface cards, `#494341` accents, and `video { vertical-align:baseline;display:inline-block }`.
5. **Colophon & Global Directory Footer (<footer.footer_component> — `https://www.impastofornoantico.com/`)**:
   - Landmark `<footer class="footer_component">` anchoring `Handcrafted Bread with Soul - Im` footer links (`Home · About · Products · Stockists · Wholesale`), copy *"Today, a new approach is taking shape — one that still value"*, and `#0000` structural dividers.
