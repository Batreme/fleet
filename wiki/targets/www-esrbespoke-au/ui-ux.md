# UI & UX Architecture: www-esrbespoke-au

## Overview & Design Identity
- **Target**: `www-esrbespoke-au` (**ESR**)
- **Production URL**: [https://www.esrbespoke.au/](https://www.esrbespoke.au/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#9ca3af`)
- **Summary**: Three decades of restoring excellence and reigniting the joy of the drive.
- **Total Clean CSS Variables Extracted**: `8` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `__bodyFont_0f148b`
- **Body Font Stack**: `__bodyFont_Fallback_0f148b`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `2.375rem`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `2.375rem`)
- **Body Copy**: CSS variables `--body-font: "__bodyFont_0f148b","__bodyFont_Fallback_0f148b",helvetica,arial,sans-serif`
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `2.375rem`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--foreground)` in `:root` |
| **Primary Typography Ink** | `#ffffff` | `var(--background)` in `:root` |
| **Elevated Surface / Card Substrate** | `#29d` | `#nprogress .bar { background: #29d }` |
| **Interactive Accent / Highlight** | `#9ca3af` | `textarea::placeholder { color: #9ca3af }` |
| **Secondary / Muted Copy** | `#000` | `#nprogress .bar { background: #000 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--foreground-rgb` | `0,0,0` | Typography Ink Token |
| `--background-rgb` | `255,255,255` | Canvas / Surface Token |
| `--border-rgb` | `0,0,0` | Elevation / Border Token |
| `--scrollbarWidth` | `0px` | Layout / Spatial Grid Token |
| `--body-font` | `"__bodyFont_0f148b","__bodyFont_Fallback_0f148b",helvetica,arial,sans-serif` | Typography / Scale Token |
| `--foreground` | `#fff` | Typography Ink Token |
| `--background` | `#ffffff` | Canvas / Surface Token |
| `--border` | `rgba(0,0,0,0.1)` | Elevation / Border Token |
| `--tw-content` | `""` | Design System Custom Token |
| `--tw-border-spacing-x` | `0` | Layout / Spatial Grid Token |
| `--tw-border-spacing-y` | `0` | Layout / Spatial Grid Token |
| `--tw-translate-x` | `0` | Design System Custom Token |
| `--tw-translate-y` | `0` | Design System Custom Token |
| `--tw-rotate` | `0` | Design System Custom Token |
| `--www-esrbespoke-a-bg` | `#fff` | Canvas Substrate (from `var(--foreground)` in `:root`) |
| `--www-esrbespoke-a-ink` | `#000` | Primary Typography Ink (stylesheet-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.w-auto> — `www-esrbespoke-au`)**:
   - Landmark `<header class="w-auto grid-layout">` hosting `ESR` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-next-font="size-adjust"`, `data-next-font="size-adjust"`, `data-next-font="size-adjust"`, `data-next-font="size-adjust"`), and stylesheet rule `nprogress { pointer-events:none }`.
2. **Hero Stage & Focal Lead (<section.w-auto> — `E x c e p t i o n a l i s o u r s `)**:
   - Landmark `<section class="w-auto grid-layout">` presenting display lead `E x c e p t i o n a l i s o u r s t a n d a r d` and copy excerpt *"E S R B e s p o k e"* over `#fff` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.w-auto> — `ESR is recognised as an official P`)**:
   - Landmark `<section class="w-auto items-end">` rendering section `ESR is recognised as an official Porsche Certifie...` with copy *"A u t o m o t i v e G r o u p since 1989"*, asset references (`apple-touch-icon.png`, `favicon-32x32.png`, `favicon-16x16.png`, `favicon.ico`), and grid rule `nprogress .bar { background:29d;position:fixed;z-index:1031;top:0;left:0;width:100%;heigh... }`.
4. **Interactive Detail & Feature Matrix (<section.w-auto> — `At ESR, we offer a complete end-to`)**:
   - Landmark `<section class="w-auto mb-8">` framing `At ESR, we offer a complete end-to-end service ex...` and `@ e s r b e s p o k e` (*"@ e s r b e s p o k e"*) with `#29d` surface cards, `#9ca3af` accents, and `nprogress .spinner { display:block;position:fixed;z-index:1031;top:15px;right:15px }`.
5. **Colophon & Global Directory Footer (<footer.relative> — `https://www.esrbespoke.au/`)**:
   - Landmark `<footer class="relative clip">` anchoring `ESR` footer links (`Overview · Index · Archive · About · Contact`), copy *"( 0 2 ) 9 7 3 5 1 1 1 1 e n q u i r i e s @ e s r b e s p o "*, and `#000` structural dividers.
