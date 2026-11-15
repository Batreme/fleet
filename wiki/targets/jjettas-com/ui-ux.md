# UI & UX Architecture: jjettas-com

## Overview & Design Identity
- **Target**: `jjettas-com` (**Justin Jefferson**)
- **Production URL**: [https://jjettas.com](https://jjettas.com)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#171220`)
- **Summary**: Justin Jefferson, wide receiver for the Minnesota Vikings. Records, career stats, partnerships, the JJets Foundation and his journal.
- **Total Clean CSS Variables Extracted**: `179` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `fontBody`
- **Body Font Stack**: `fontBody Fallback`
- **Monospace / Technical Font Stack**: `fontMono`
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`; rule `h2` (`font-size: calc(20.5 * var(--pu))`)
- **Body Copy**: CSS variables `--font-body-family: "fontBody","fontBody Fallback"`, `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`
- **Metadata & Labels**: CSS variables `--font-mono-family: "fontMono","fontMono Fallback"`, `--font-numono: "fontNuMono","fontNuMono Fallback"`, `--font-mono: var(--font-mono-family),ui-monospace,SFMono-Regular,Menlo,monospace`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#0b0a0f` | `var(--color-ink)` in `:root` |
| **Interactive Accent / Highlight** | `#171220` | `var(--color-ink-deep)` in `:root` |
| **Secondary / Muted Copy** | `#f4efe6` | `var(--color-bone)` in `:root` |
| **Structural Hairline Border** | `#d3c8ba` | `var(--color-sand)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-body-family` | `"fontBody","fontBody Fallback"` | Typography / Scale Token |
| `--font-mono-family` | `"fontMono","fontMono Fallback"` | Typography / Scale Token |
| `--font-numono` | `"fontNuMono","fontNuMono Fallback"` | Typography / Scale Token |
| `--font-sans` | `var(--font-body)` | Typography / Scale Token |
| `--font-mono` | `var(--font-mono-family),ui-monospace,SFMono-Regular,Menlo,monospace` | Typography / Scale Token |
| `--color-lime-300` | `oklch(89.7% .196 126.665)` | Brand / Palette Token |
| `--color-emerald-400` | `oklch(76.5% .177 163.223)` | Brand / Palette Token |
| `--color-emerald-500` | `oklch(69.6% .17 162.48)` | Brand / Palette Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--container-sm` | `24rem` | Layout / Spatial Grid Token |
| `--container-md` | `28rem` | Layout / Spatial Grid Token |
| `--container-xl` | `36rem` | Layout / Spatial Grid Token |
| `--container-2xl` | `42rem` | Layout / Spatial Grid Token |
| `--container-3xl` | `48rem` | Layout / Spatial Grid Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.pointer-events-none> — `jjettas-com`)**:
   - Landmark `<header class="pointer-events-none fixed">` hosting `Justin Jefferson` navigation (`Home · On-Field On-Field · Off-Field Off-Field · Journal Journal · Inquiries Inquiries`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `.light-overlay_light01__pSQNv { background-image:url(/textures/light-01.webp) }`.
2. **Hero Stage & Focal Lead (<section.relative> — `Justin Jefferson`)**:
   - Landmark `<section class="relative w-full">` presenting display lead `Justin Jefferson` and copy excerpt *"Off-Field Off-Field"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.relative> — `Signature Moments`)**:
   - Landmark `<section class="relative flex">` rendering section `Signature Moments` with copy *"Foundation Foundation"*, asset references (`0ad3faa61cd26fd6-s.p.woff2`, `34310d7f0559b2f8-s.p.woff2`, `45f4bf9bd5d902fa-s.p.woff2`, `c39007f2e37cc928-s.p.otf`), and grid rule `.__className_cf619f { font-family:fontBody,fontBody Fallback }`.
4. **Interactive Detail & Feature Matrix (<section.relative> — `Building something that lasts`)**:
   - Landmark `<section class="relative w-full">` framing `Building something that lasts` and `The JJets Foundation` (*"Partnerships Partnerships"*) with `#0b0a0f` surface cards, `#171220` accents, and `.__variable_cf619f { --font-body-family:"fontBody","fontBody Fallback" }`.
5. **Colophon & Global Directory Footer (<footer.relative> — `https://jjettas.com`)**:
   - Landmark `<footer class="relative flex">` anchoring `Justin Jefferson` footer links (`Home · On-Field On-Field · Off-Field Off-Field · Journal Journal · Inquiries Inquiries`), copy *"Inquiries Inquiries"*, and `#d3c8ba` structural dividers.
