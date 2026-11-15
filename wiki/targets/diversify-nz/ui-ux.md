# UI & UX Architecture: diversify-nz

## Overview & Design Identity
- **Target**: `diversify-nz` (**diversify.nz**)
- **Production URL**: [https://diversify.nz](https://diversify.nz)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#21206c` canvas, `#cdccf0` ink, `#3937b9` accent)
- **Summary**: Think differently. Act courageously. Create lasting change.
- **Total Clean CSS Variables Extracted**: `52` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `martel-sans`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `.title` (`font-size: 18px`, `letter-spacing: 0`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 26px`)
- **Body Copy**: rule `p` (`font-size: 12px`, `line-height: 1.2`)
- **Metadata & Labels**: rule `.label` (`font-size: 20px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#21206c` | `var(--main-color)` in `:root` |
| **Primary Typography Ink** | `#09081b` | `var(--s-pre-color0)` in `:root` |
| **Elevated Surface / Card Substrate** | `#21206a` | `var(--s-pre-color1)` in `:root` |
| **Interactive Accent / Highlight** | `#3937b9` | `var(--s-pre-color2)` in `:root` |
| **Secondary / Muted Copy** | `#7f7dd8` | `var(--s-pre-color3)` in `:root` |
| **Structural Hairline Border** | `#cdccf0` | `var(--s-pre-color4)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--carousel-button-width` | `48px` | Layout / Spatial Grid Token |
| `--carousel-button-height` | `48px` | Layout / Spatial Grid Token |
| `--carousel-button-svg-width` | `24px` | Layout / Spatial Grid Token |
| `--carousel-button-svg-height` | `24px` | Layout / Spatial Grid Token |
| `--carousel-button-svg-stroke-width` | `2.5` | Layout / Spatial Grid Token |
| `--carousel-button-svg-filter` | `drop-shadow(1px 1px 1px rgba(0,0,0,0.4))` | Color / Atmospheric Token |
| `--main-color` | `#21206c` | Brand / Palette Token |
| `--s-pre-color0` | `#09081b` | Brand / Palette Token |
| `--s-pre-color0-rgb` | `9,8,27` | Brand / Palette Token |
| `--s-pre-color1` | `#21206a` | Brand / Palette Token |
| `--s-pre-color1-rgb` | `33,32,106` | Brand / Palette Token |
| `--s-pre-color2` | `#3937b9` | Brand / Palette Token |
| `--s-pre-color2-rgb` | `57,55,185` | Brand / Palette Token |
| `--s-pre-color3` | `#7f7dd8` | Brand / Palette Token |
| `--s-pre-color3-rgb` | `127,125,216` | Brand / Palette Token |
| `--s-pre-color4` | `#cdccf0` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.show> — `diversify-nz`)**:
   - Landmark `<header class="show">` hosting `diversify.nz` navigation (`Home · About · Services · Blog · Past work`), DOM attributes (`data-mobile-new-breakpoint-stage="1"`, `data-id="491220"`, `data-hypernova-key="SiteBootstrapper"`, `data-hypernova-id="396cda9e-3621-4d48-9c..."`), and stylesheet rule `.clearfix { position:relative }`.
2. **Hero Stage & Focal Lead (<div.locale-en> — `Think differently.`)**:
   - Landmark `<div class="locale-en">` presenting display lead `Think differently.` and copy excerpt *"… Home About Services Blog Past work Testimonials Media Contact"* over `#21206c` canvas and `#cdccf0` ink.
3. **Primary Showcase & Content Grid (<div.s-variation-default> — `Act courageously.`)**:
   - Landmark `<div class="s-variation-default">` rendering section `Act courageously.` with copy *"FOR MORE, CLICK THE PICS ABOVE Whakaanui kē. Think differently. M"*, asset references (`ga.js`, `static-fonts-css.strikinglycdn.com`, `main_v4.d0ac47e70d8a81a0e143.bund...`, `650606_331305.png`), and grid rule `.clearfix:after { display:table;content:"";clear:both }`.
4. **Interactive Detail & Feature Matrix (<div.s-custom-colors> — `Create lasting change.`)**:
   - Landmark `<div class="s-custom-colors">` framing `Create lasting change.` and `WHAT DIVERSIFY NZ BRINGS` (*"FOR MORE, CLICK THE PICS ABOVE"*) with `#21206a` surface cards, `#3937b9` accents, and `.ib { display:inline-block;zoom:1 }`.
5. **Colophon & Global Directory Footer (<footer.s-font-body-helvetica> — `https://diversify.nz`)**:
   - Landmark `<footer class="s-font-body-helvetica">` anchoring `diversify.nz` footer links (`Home · About · Services · Blog · Past work`), copy *"Think differently."*, and `#cdccf0` structural dividers.
