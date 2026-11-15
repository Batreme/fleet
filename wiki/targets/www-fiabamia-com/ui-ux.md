# UI & UX Architecture: www-fiabamia-com

## Overview & Design Identity
- **Target**: `www-fiabamia-com` (**FiabaMia — Personalized bedtime stories for children**)
- **Production URL**: [https://www.fiabamia.com/](https://www.fiabamia.com/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffa3a3` / `#fffbeb`)
- **Summary**: Every night a brand-new bedtime story where your child is the hero: written in 30 seconds to fit their age, with music, interactive sound...
- **Total Clean CSS Variables Extracted**: `185` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Lora`
- **Body Font Stack**: `Lora Fallback`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`font-size: clamp(1.45rem,2.6vw,1.85rem)`, `line-height: 1.2`, `letter-spacing: -.02em`, `font-weight: 300`)
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`; rule `p` (`font-size: clamp(1.05rem,1.5vw,1.38rem)`, `line-height: 1.4`, `font-weight: 300`)
- **Metadata & Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`; rule `small` (`font-size: .42em`, `letter-spacing: 0`, `font-weight: 300`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#ffa3a3` | `var(--color-red-300)` in `:root` |
| **Primary Typography Ink** | `#ff6568` | `var(--color-red-400)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fb2c36` | `var(--color-red-500)` in `:root` |
| **Interactive Accent / Highlight** | `#fffbeb` | `var(--color-amber-50)` in `:root` |
| **Secondary / Muted Copy** | `#ffd236` | `var(--color-amber-300)` in `:root` |
| **Structural Hairline Border** | `#fcbb00` | `var(--color-amber-400)` in `:root` |
| **Variable Token (`--color-amber-500`)** | `#f99c00` | `var(--color-amber-500)` in `:root` |
| **Variable Token (`--color-amber-600`)** | `#dd7400` | `var(--color-amber-600)` in `:root` |
| **Variable Token (`--color-amber-700`)** | `#b75000` | `var(--color-amber-700)` in `:root` |
| **Variable Token (`--color-yellow-400`)** | `#fac800` | `var(--color-yellow-400)` in `:root` |
| **Variable Token (`--color-yellow-500`)** | `#edb200` | `var(--color-yellow-500)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-lora` | `"Lora", "Lora Fallback"` | Typography / Scale Token |
| `--font-cormorant-sc` | `"Cormorant SC", "Cormorant SC Fallback"` | Typography / Scale Token |
| `--font-nunito` | `"Nunito", "Nunito Fallback"` | Typography / Scale Token |
| `--font-sans` | `var(--font-nunito)` | Typography / Scale Token |
| `--font-serif` | `var(--font-lora)` | Typography / Scale Token |
| `--color-red-300` | `#ffa3a3` | Brand / Palette Token |
| `--color-red-400` | `#ff6568` | Brand / Palette Token |
| `--color-red-500` | `#fb2c36` | Brand / Palette Token |
| `--color-amber-50` | `#fffbeb` | Brand / Palette Token |
| `--color-amber-300` | `#ffd236` | Brand / Palette Token |
| `--color-amber-400` | `#fcbb00` | Brand / Palette Token |
| `--color-amber-500` | `#f99c00` | Brand / Palette Token |
| `--color-amber-600` | `#dd7400` | Brand / Palette Token |
| `--color-amber-700` | `#b75000` | Brand / Palette Token |
| `--color-yellow-400` | `#fac800` | Brand / Palette Token |
| `--color-yellow-500` | `#edb200` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.vg-testata> — `www-fiabamia-com`)**:
   - Landmark `<header class="vg-testata">` hosting `FiabaMia — Personalized bedtime stor` navigation (`Create a story`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `lora_59c43264-module__4gbARq__cla... { font-family:Lora,Lora Fallback;font-style:normal }`.
2. **Hero Stage & Focal Lead (<section.vg-hero> — `Personalized bedtime stories for c`)**:
   - Landmark `<section class="vg-hero">` presenting display lead `Personalized bedtime stories for children A fairy...` and copy excerpt *"FiabaMia · a bedtime fairy tale"* over `#ffa3a3` canvas and `#fb2c36` ink.
3. **Primary Showcase & Content Grid (<section.vg-lettura> — `A story made to measure: name, age`)**:
   - Landmark `<section class="vg-lettura">` rendering section `A story made to measure: name, age, value, place...` with copy *"No one has ever told it…"*, asset references (`07454f8ad8aaac57-s.p.0tqkxa-w3pk~...`, `25e51d4a4d803f16-s.p.01lzzy~hm0v2...`, `4917c4fe274b6773-s.p.03o7i-1ioayt...`, `54fc36028e2bb174-s.p.0nkps02--w45...`), and grid rule `.lora_59c43264-module__4gbARq__va... { --font-lora:"Lora", "Lora Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.vg-tunnel> — `Every story has its own music`)**:
   - Landmark `<section class="vg-tunnel">` framing `Every story has its own music` and `Words that come to life` (*"Listen with sound Sound on"*) with `#fb2c36` surface cards, `#fffbeb` accents, and `t_sc_8e09fe47-module__uQmyda__cla... { font-family:Cormorant SC,Cormorant SC Fallback;font-style:normal }`.
5. **Colophon & Global Directory Footer (<footer.vg-fondo> — `https://www.fiabamia.com/`)**:
   - Landmark `<footer class="vg-fondo site-footer">` anchoring `FiabaMia — Personalized bedtime ` footer links (`Create a story`), copy *"Personalized bedtime stories for children"*, and `#fcbb00` structural dividers.
