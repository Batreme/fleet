# UI & UX Architecture: www-qissa-co-uk

## Overview & Design Identity
- **Target**: `www-qissa-co-uk` (**Indian Restaurant in Sevenoaks, Kent · Qissa**)
- **Production URL**: [https://www.qissa.co.uk/](https://www.qissa.co.uk/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#05091A` / `#16224A`)
- **Summary**: Qissa — A Tale of Food. Modern Indian dining beneath the blossoms in the heart of Sevenoaks, Kent. Reserve a table or order takeaway. Rat...
- **Total Clean CSS Variables Extracted**: `26` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Cormorant Garamond`
- **Body Font Stack**: `Manrope`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--f-display: 'Cormorant Garamond', 'Times New Roman', serif`; rule `.hero-title` (`font-size: clamp(2rem,9vw,7.6rem)`, `letter-spacing: -.02em`)
- **Section Heading (`H2`)**: rule `.h2` (`font-size: clamp(2rem,4.6vw,3.6rem)`, `letter-spacing: -.015em`, `font-weight: 340`)
- **Body Copy**: CSS variables `--f-body: 'Manrope', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif`; rule `body` (`line-height: 1.6`, `font-weight: 350`)
- **Metadata & Labels**: rule `small` (`font-size: .7rem`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#05091A` | `var(--ink)` in `:root` |
| **Primary Typography Ink** | `#0A1230` | `var(--navy)` in `:root` |
| **Elevated Surface / Card Substrate** | `#0E1838` | `var(--navy-2)` in `:root` |
| **Interactive Accent / Highlight** | `#16224A` | `var(--navy-3)` in `:root` |
| **Secondary / Muted Copy** | `#1E2C57` | `var(--navy-line)` in `:root` |
| **Structural Hairline Border** | `#C9A24B` | `var(--gold)` in `:root` |
| **Variable Token (`--gold-hi`)** | `#EFD79A` | `var(--gold-hi)` in `:root` |
| **Variable Token (`--gold-deep`)** | `#9A7A34` | `var(--gold-deep)` in `:root` |
| **Variable Token (`--amber`)** | `#E9A85C` | `var(--amber)` in `:root` |
| **Variable Token (`--blossom`)** | `#E7A6C4` | `var(--blossom)` in `:root` |
| **Variable Token (`--blossom-2`)** | `#F2C6D9` | `var(--blossom-2)` in `:root` |
| **Variable Token (`--cream`)** | `#F6F1E7` | `var(--cream)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ink` | `#05091A` | Typography Ink Token |
| `--navy` | `#0A1230` | Layout / Spatial Grid Token |
| `--navy-2` | `#0E1838` | Layout / Spatial Grid Token |
| `--navy-3` | `#16224A` | Layout / Spatial Grid Token |
| `--navy-line` | `#1E2C57` | Layout / Spatial Grid Token |
| `--gold` | `#C9A24B` | Color / Atmospheric Token |
| `--gold-hi` | `#EFD79A` | Color / Atmospheric Token |
| `--gold-deep` | `#9A7A34` | Color / Atmospheric Token |
| `--amber` | `#E9A85C` | Color / Atmospheric Token |
| `--blossom` | `#E7A6C4` | Color / Atmospheric Token |
| `--blossom-2` | `#F2C6D9` | Color / Atmospheric Token |
| `--cream` | `#F6F1E7` | Color / Atmospheric Token |
| `--cream-dim` | `rgba(246,241,231,.70)` | Color / Atmospheric Token |
| `--cream-faint` | `rgba(246,241,231,.42)` | Color / Atmospheric Token |
| `--line` | `rgba(201,162,75,.22)` | Color / Atmospheric Token |
| `--line-soft` | `rgba(246,241,231,.10)` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `www-qissa-co-uk`)**:
   - Landmark `<header class="site-header">` hosting `Indian Restaurant in Sevenoaks, Kent` navigation (`00 Home · 01 Our Story · 02 The Menu · Food Menu · Drinks Menu`), DOM attributes (`data-u="contact"`, `data-d="qissa.co.uk"`, `data-tilt`, `data-count="4.8"`), and stylesheet rule `after { box-sizing:border-box;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Qissa`)**:
   - Landmark `<section class="hero">` presenting display lead `Qissa` and copy excerpt *"06 Visit & Contact"* over `#05091A` canvas and `#C9A24B` ink.
3. **Primary Showcase & Content Grid (<section.section> — `A word that means a tale.`)**:
   - Landmark `<section class="section">` rendering section `A word that means a tale.` with copy *"4 Carlton Parade, St John's Hill Sevenoaks, TN13 3NZ, Kent"*, asset references (`gtm.js`, `hero-poster.webp`, `favicon-96.png`, `favicon-32.png`), and grid rule `html { scroll-behavior:smooth;-webkit-text-size-adjust:100% }`.
4. **Interactive Detail & Feature Matrix (<section.section> — `Crafted icons & signature plates.`)**:
   - Landmark `<section class="section masterpieces">` framing `Crafted icons & signature plates.` and `Explore the menu, course by course.` (*"01732 74 09 74 contact qissa.co.uk"*) with `#0E1838` surface cards, `#16224A` accents, and `img { display:block;max-width:100%;height:auto }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://www.qissa.co.uk/`)**:
   - Landmark `<footer class="site-footer">` anchoring `Indian Restaurant in Sevenoaks, ` footer links (`00 Home · 01 Our Story · 02 The Menu · Food Menu · Drinks Menu`), copy *"contact qissa.co.uk"*, and `#C9A24B` structural dividers.
