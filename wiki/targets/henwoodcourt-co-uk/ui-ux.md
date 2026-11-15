# UI & UX Architecture: henwoodcourt-co-uk

## Overview & Design Identity
- **Target**: `henwoodcourt-co-uk` (**Henwood Court · Where financial freedom meets fulfilment**)
- **Production URL**: [https://henwoodcourt.co.uk](https://henwoodcourt.co.uk)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#705583` accent)
- **Summary**: You work hard for your money. At Henwood Court we work hard to turn your wealth into a life you love.
- **Total Clean CSS Variables Extracted**: `61` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Euclid Circular B`
- **Body Font Stack**: `Moulin Trial`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: CSS variables `--font-display: "Moulin Trial", Georgia, "Times New Roman", serif`
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `20px`, `1em`, `80%`, `75%`, `1rem`)
- **Body Copy**: CSS variables `--font-body: "Euclid Circular B", Arial, Helvetica, sans-serif`, `--text-body-small: 14px`
- **Metadata & Labels**: CSS variables `--default-mono-font-family: var(--font-mono)`, `--text-body-small: 14px`, `--text-label: 14px`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#48265f` | `var(--color-med-purple)` in `:root` |
| **Interactive Accent / Highlight** | `#705583` | `var(--color-light-purple)` in `:root` |
| **Secondary / Muted Copy** | `#280c3b` | `var(--color-dark-purple)` in `:root` |
| **Structural Hairline Border** | `#7b7283` | `var(--color-muted-purple)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-sans` | `var(--font-body)` | Typography / Scale Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--container-sm` | `24rem` | Layout / Spatial Grid Token |
| `--container-md` | `28rem` | Layout / Spatial Grid Token |
| `--container-lg` | `32rem` | Layout / Spatial Grid Token |
| `--container-xl` | `36rem` | Layout / Spatial Grid Token |
| `--container-2xl` | `42rem` | Layout / Spatial Grid Token |
| `--container-3xl` | `48rem` | Layout / Spatial Grid Token |
| `--container-4xl` | `56rem` | Layout / Spatial Grid Token |
| `--container-5xl` | `64rem` | Layout / Spatial Grid Token |
| `--container-6xl` | `72rem` | Layout / Spatial Grid Token |
| `--font-weight-light` | `300` | Canvas / Surface Token |
| `--font-weight-normal` | `400` | Typography / Scale Token |
| `--font-weight-medium` | `500` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.fixed> — `henwoodcourt-co-uk`)**:
   - Landmark `<header class="fixed top-0">` hosting `Henwood Court · Where financial free` navigation (`Manage your money · Plan your retirement · Our approach · Investment strategy · FAQs`), DOM attributes (`data-theme-url="https://henwoodcourt...."`, `data-ajax-url="https://henwoodcourt...."`, `data-ratio="xMidYMid meet"`, `data-path="https://henwoodcourt...."`), and stylesheet rule `.dashicons-admin-appearance:before { content:"\f100" }`.
2. **Hero Stage & Focal Lead (<article.bg-white> — `Where financial freedom meets fulf`)**:
   - Landmark `<article class="bg-white shadow-card">` presenting display lead `Where financial freedom meets fulfilment` and copy excerpt *"Financial planning Manage your money The next step for your busin"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<article.bg-white> — `Helping you live a rich life, not `)**:
   - Landmark `<article class="bg-white shadow-card">` rendering section `Helping you live a rich life, not just a wealthy one` with copy *"Financial planning"*, asset references (`euclid-circular-b-regular.woff2`, `euclid-circular-b-medium.woff2`, `moulin-light.woff2`, `player.vimeo.com`), and grid rule `.dashicons-admin-collapse:before { content:"\f148" }`.
4. **Interactive Detail & Feature Matrix (<article.bg-white> — `I’m a business owner`)**:
   - Landmark `<article class="bg-white shadow-card">` framing `I’m a business owner` and `I’m looking to invest` (*"The next step for your business"*) with `#48265f` surface cards, `#705583` accents, and `.dashicons-admin-comments:before { content:"\f101" }`.
5. **Colophon & Global Directory Footer (<footer.bg-linear-to-b> — `https://henwoodcourt.co.uk`)**:
   - Landmark `<footer class="bg-linear-to-b from-med-purple">` anchoring `Henwood Court · Where financial ` footer links (`Manage your money · Plan your retirement · Our approach · Investment strategy · FAQs`), copy *"Invest for your future"*, and `#7b7283` structural dividers.
