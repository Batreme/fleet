# UI & UX Architecture: www-197historiasilustradas-com

## Overview & Design Identity
- **Target**: `www-197historiasilustradas-com` (**197 Historias Ilustradas**)
- **Production URL**: [https://www.197historiasilustradas.com/](https://www.197historiasilustradas.com/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#d4d4d4` canvas, `#000` ink, `#fff` accent)
- **Summary**: 197 historias ilustradas es un proyecto que busca dar a conocer la vida de cada una de las personas detenidas desaparecidas nacidas en Ur...
- **Total Clean CSS Variables Extracted**: `32` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `font`
- **Body Font Stack**: `font Fallback`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `.875rem`, `.8125rem`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `.875rem`, `.8125rem`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `.875rem`, `.8125rem`)
- **Metadata & Labels**: CSS variables `--default-mono-font-family: var(--font-mono)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#d4d4d4` | `var(--color-neutral-300)` in `:root` |
| **Primary Typography Ink** | `#a1a1a1` | `var(--color-neutral-400)` in `:root` |
| **Elevated Surface / Card Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Interactive Accent / Highlight** | `#fff` | `var(--color-white)` in `:root` |
| **Secondary / Muted Copy** | `#171717` | `var(--foreground)` in `:root` |
| **Structural Hairline Border** | `#737373` | `var(--muted)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-neutral-300` | `#d4d4d4` | Brand / Palette Token |
| `--color-neutral-400` | `#a1a1a1` | Brand / Palette Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--font-weight-bold` | `700` | Typography / Scale Token |
| `--tracking-tighter` | `-.05em` | Typography / Scale Token |
| `--tracking-normal` | `0em` | Typography / Scale Token |
| `--leading-relaxed` | `1.625` | Typography / Scale Token |
| `--ease-in` | `cubic-bezier(.4,0,1,1)` | Motion / Easing Token |
| `--ease-out` | `cubic-bezier(0,0,.2,1)` | Motion / Easing Token |
| `--ease-in-out` | `cubic-bezier(.4,0,.2,1)` | Motion / Easing Token |
| `--default-transition-duration` | `.15s` | Motion / Easing Token |
| `--default-transition-timing-function` | `cubic-bezier(.4,0,.2,1)` | Motion / Easing Token |
| `--default-font-family` | `var(--font-sans)` | Typography / Scale Token |
| `--default-mono-font-family` | `var(--font-mono)` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.px-global> — `www-197historiasilustradas-com`)**:
   - Landmark `<header class="px-global fixed">` hosting `197 Historias Ilustradas` navigation (`[ Grilla ] · [ Listado ] · [ Galería ]`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-sdkn="@vercel/analytics/next"`, `data-sdkv="2.0.1"`), and stylesheet rule `host { --color-neutral-300:lab(84.92% 0 -.0000119209);--color-neutral-400:lab(6... }`.
2. **Hero Stage & Focal Lead (<div.is-ready> — `197 Historias Ilustradas`)**:
   - Landmark `<div class="is-ready">` presenting display lead `197 Historias Ilustradas` and copy excerpt *"197 Historias Ilustradas"* over `#d4d4d4` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<div.px-global> — `197 Historias Ilustradas`)**:
   - Landmark `<div class="px-global">` rendering section `197 Historias Ilustradas` with copy *"Historias Ilustradas"*, asset references (`882aee3e7e5fa64f.css`, `3068344f6b59fc28.css`, `a6a883b7ec42f0a6.js`, `1c40893e27076bb9.js`), and grid rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<div.fixed> — `Historias Ilustradas`)**:
   - Landmark `<div class="fixed">` framing `Historias Ilustradas` and `E n t r e l a s d é c a d a s d e 1 9 7 0 y 1 9 ` (*"E n t r e l a s d é c a d a s d e 1 9 7 0 y 1 9 8 0 , t a n t o U"*) with `#000` surface cards, `#fff` accents, and `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
5. **Colophon & Global Directory Footer (<footer.top-0> — `https://www.197historiasilustradas.com/`)**:
   - Landmark `<footer class="top-0">` anchoring `197 Historias Ilustradas` footer links (`[ Grilla ] · [ Listado ] · [ Galería ]`), copy *"R e c o r d a r e s v o l v e r a d a r v i d a ; p o r q u "*, and `#737373` structural dividers.
