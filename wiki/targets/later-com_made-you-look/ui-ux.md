# UI & UX Architecture: later-com_made-you-look

## Overview & Design Identity
- **Target**: `later-com_made-you-look` (**Made You Look: Campaigns so good you break the algorithm.**)
- **Production URL**: [https://later.com/made-you-look/](https://later.com/made-you-look/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000000` canvas, `#fff6cc` ink, `#ffd200` accent)
- **Summary**: Meet the creators shaping culture through bold ideas and obsessive craft—and see how brands partner with them to build standout influence...
- **Total Clean CSS Variables Extracted**: `821` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Garamond`
- **Body Font Stack**: `Mondwest`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--h1-2xl: 3.5rem`, `--h1-xl: 3.125rem`, `--h1-l: 2.5rem`; rule `h1` (`font-size: 5rem`)
- **Section Heading (`H2`)**: CSS variables `--h2: 2.125rem`, `--h2-s: 1.875rem`, `--text-2xl: 1.25rem`; rule `h2` (`font-size: 13px`, `line-height: 15px`, `font-weight: 500`)
- **Body Copy**: CSS variables `--font-body: Inter Tight,Helvetica Neue,Helvetica,Arial,sans-serif`, `--body-line-height: 1.5`, `--body-letter-spacing: 0.01em`; rule `.paragraph` (`font-size: 14px`)
- **Metadata & Labels**: CSS variables `--text-xs: 0.875rem`, `--heading-letter-spacing: 0.005em`, `--body-letter-spacing: 0.01em`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | `var(--primary-color)` in `:root` |
| **Primary Typography Ink** | `#000` | `var(--w2w-start-background-color)` in `:root` |
| **Elevated Surface / Card Substrate** | `#a075ff` | `var(--outline-color)` in `:root` |
| **Interactive Accent / Highlight** | `#ffd200` | `var(--yellow)` in `:root` |
| **Secondary / Muted Copy** | `#ffe880` | `var(--yellow-secondary)` in `:root` |
| **Structural Hairline Border** | `#fff6cc` | `var(--yellow-20)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--primary-color` | `#000000` | Brand / Palette Token |
| `--text-color` | `#000000` | Typography Ink Token |
| `--squareDimension` | `25px` | Dimension / Scale Token |
| `--switchHeight` | `20px` | Layout / Spatial Grid Token |
| `--switchGutter` | `2px` | Layout / Spatial Grid Token |
| `--switchButtonDiameter` | `calc(var(--switchHeight) - var(--switchGutter) * 2)` | Dimension / Scale Token |
| `--td176b92ada598f8f` | `initial` | Design System Custom Token |
| `--td851cd75a8793667` | `initial` | Design System Custom Token |
| `--tc58f4bf5a9869b3e` | `initial` | Design System Custom Token |
| `--t3a480c2f814ef19c` | `initial` | Design System Custom Token |
| `--t77e217518bcd986b` | `initial` | Design System Custom Token |
| `--tc5e0863356bf5767` | `initial` | Design System Custom Token |
| `--t7a2234c5eadde886` | `initial` | Design System Custom Token |
| `--td340014d093b0821` | `initial` | Design System Custom Token |
| `--tf8c80baf678711b8` | `initial` | Design System Custom Token |
| `--t2986df03ecf88759` | `initial` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.lenis> — `later-com_made-you-look`)**:
   - Landmark `<header class="lenis">` hosting `Made You Look: Campaigns so good you` navigation (`halo perez-gallardo · Timothy Goodman · Jeremy Jankowski · Megna Paula · Julian McCleary`), DOM attributes (`data-root="true"`, `data-gatsby-head="true"`, `data-gatsby-head="true"`, `data-gatsby-head="true"`), and stylesheet rule `.button:hover { background-color: var(--primary-color); }`.
2. **Hero Stage & Focal Lead (<section.NnFvv> — `Campaigns so good you break the al`)**:
   - Landmark `<section class="NnFvv">` presenting display lead `Campaigns so good you break the algorithm.` and copy excerpt *"That’s what happens when brands stop chasing trends and start wor"* over `#000000` canvas and `#fff6cc` ink.
3. **Primary Showcase & Content Grid (<section.NnFvv> — `Made you look`)**:
   - Landmark `<section class="NnFvv">` rendering section `Made you look` with copy *"At Later, we help brands partner with those creators—bringing tog"*, asset references (`InterTight-VariableFont_wght.woff2`, `superx-extrabold.woff2`, `superx-semibold.woff2`, `rss.xml`), and grid rule `.button:hover span { color: ffffff; }`.
4. **Interactive Detail & Feature Matrix (<section.NnFvv> — `halo perez-gallardo`)**:
   - Landmark `<section class="NnFvv">` framing `halo perez-gallardo` and `Timothy Goodman` (*"Because breakthrough campaigns aren’t louder. They’re more credib"*) with `#a075ff` surface cards, `#ffd200` accents, and `.button-primary-text { font-size: 12px; font-weight: 700; }`.
5. **Colophon & Global Directory Footer (<footer.myl-header-cta> — `https://later.com/made-you-look/`)**:
   - Landmark `<footer class="myl-header-cta">` anchoring `Made You Look: Campaigns so good` footer links (`halo perez-gallardo · Timothy Goodman · Jeremy Jankowski · Megna Paula · Julian McCleary`), copy *"Learn more about Later's services"*, and `#fff6cc` structural dividers.
