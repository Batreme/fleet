# UI & UX Architecture: www-imersion-io

## Overview & Design Identity
- **Target**: `www-imersion-io` (**Imersion — Get Immersed in the World's Most Beautiful Places**)
- **Production URL**: [https://www.imersion.io](https://www.imersion.io)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#007bff` canvas, `#6610f2` ink, `#e83e8c` accent)
- **Summary**: Get immersed in the most beautiful places on Earth — breathtaking landscapes, hidden hotels and surreal restaurants, each with its own st...
- **Total Clean CSS Variables Extracted**: `28` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Anton`
- **Body Font Stack**: `Bitcount Single`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **Hero Display (`H1`)**: rule `,h1` (`font-size: 2.5rem`)
- **Section Heading (`H2`)**: rule `,h2` (`font-size: 2rem`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1rem`, `80%`, `75%`, `1em`, `1.5rem`)
- **Metadata & Labels**: rule `,small` (`font-size: 80%`, `font-weight: 400`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#007bff` | `var(--blue)` in `:root` |
| **Primary Typography Ink** | `#6610f2` | `var(--indigo)` in `:root` |
| **Elevated Surface / Card Substrate** | `#6f42c1` | `var(--purple)` in `:root` |
| **Interactive Accent / Highlight** | `#e83e8c` | `var(--pink)` in `:root` |
| **Secondary / Muted Copy** | `#dc3545` | `var(--red)` in `:root` |
| **Structural Hairline Border** | `#fd7e14` | `var(--orange)` in `:root` |
| **Variable Token (`--yellow`)** | `#ffc107` | `var(--yellow)` in `:root` |
| **Variable Token (`--green`)** | `#28a745` | `var(--green)` in `:root` |
| **Variable Token (`--teal`)** | `#20c997` | `var(--teal)` in `:root` |
| **Variable Token (`--cyan`)** | `#17a2b8` | `var(--cyan)` in `:root` |
| **Variable Token (`--white`)** | `#fff` | `var(--white)` in `:root` |
| **Variable Token (`--gray`)** | `#6c757d` | `var(--gray)` in `:root` |
| **Variable Token (`--gray-dark`)** | `#343a40` | `var(--gray-dark)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--blue` | `#007bff` | Color / Atmospheric Token |
| `--indigo` | `#6610f2` | Color / Atmospheric Token |
| `--purple` | `#6f42c1` | Color / Atmospheric Token |
| `--pink` | `#e83e8c` | Typography Ink Token |
| `--red` | `#dc3545` | Color / Atmospheric Token |
| `--orange` | `#fd7e14` | Color / Atmospheric Token |
| `--yellow` | `#ffc107` | Color / Atmospheric Token |
| `--green` | `#28a745` | Color / Atmospheric Token |
| `--teal` | `#20c997` | Color / Atmospheric Token |
| `--cyan` | `#17a2b8` | Color / Atmospheric Token |
| `--white` | `#fff` | Canvas / Surface Token |
| `--gray` | `#6c757d` | Color / Atmospheric Token |
| `--gray-dark` | `#343a40` | Canvas / Surface Token |
| `--primary` | `#007bff` | Brand / Palette Token |
| `--secondary` | `#6c757d` | Brand / Palette Token |
| `--success` | `#28a745` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.hh> — `www-imersion-io`)**:
   - Landmark `<header class="hh">` hosting `Imersion — Get Immersed in the World` navigation (`Contact Contact`), DOM attributes (`data-n-head="%7B%22lang%22:%7B%22s..."`, `data-n-head="ssr"`, `data-n-head="ssr"`, `data-n-head="ssr"`), and stylesheet rule `before { box-sizing:border-box }`.
2. **Hero Stage & Focal Lead (<section.wow> — `G E T I M M E R S E D`)**:
   - Landmark `<section class="wow">` presenting display lead `G E T I M M E R S E D` and copy excerpt *"All places All places"* over `#007bff` canvas and `#6610f2` ink.
3. **Primary Showcase & Content Grid (<section.recent> — `A n i m m e r s i v e e x p e r i `)**:
   - Landmark `<section class="recent">` rendering section `A n i m m e r s i v e e x p e r i e n c e t h r o...` with copy *"Submit a place Submit a place"*, asset references (`favicon.ico`, `hero-poster.jpg`, `fonts.googleapis.com`, `fonts.gstatic.com`), and grid rule `html { font-family:sans-serif;line-height:1.15;-webkit-text-size-adjust:100%;-w... }`.
4. **Interactive Detail & Feature Matrix (<section.about> — `Recently added`)**:
   - Landmark `<section class="about">` framing `Recently added` and `A crew of autonomous AI agents` (*"Need a crew of AI agents? Need a crew of AI agents?"*) with `#6f42c1` surface cards, `#e83e8c` accents, and `section { display:block }`.
5. **Colophon & Global Directory Footer (<footer.hf> — `https://www.imersion.io`)**:
   - Landmark `<footer class="hf">` anchoring `Imersion — Get Immersed in the W` footer links (`Contact Contact`), copy *"Need a crew of AI agents?"*, and `#fd7e14` structural dividers.
