# UI & UX Architecture: gracefashion-ai

## Overview & Design Identity
- **Target**: `gracefashion-ai` (**KI-Fotostudio für Mode: Bilder ohne Shooting · grace ai**)
- **Production URL**: [https://gracefashion.ai](https://gracefashion.ai)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000` canvas, `#fff` ink, `#d1d3d4` accent)
- **Summary**: KI-Modefotografie aus deinen eigenen Teilen: On-Model-Bilder, Kampagnen und Videos. Als Software oder als Service, rund 80 Prozent unter...
- **Total Clean CSS Variables Extracted**: `11` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Instrument Sans`
- **Body Font Stack**: `Instrument Sans Fallback`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: CSS variables `--font-display: var(--font-sans)`
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(21px,16.62px + 1.124vw,...`, `line-height: 1.15`, `letter-spacing: -.026em`, `font-weight: 500`)
- **Body Copy**: rule `p` (`font-size: 18px`, `line-height: 1.5`, `letter-spacing: -.011em`, `font-weight: 400`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `clamp(32px,17.1px + 3.82vw,66px)`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#808285` | `var(--color-cool-gray)` in `:root` |
| **Interactive Accent / Highlight** | `#d1d3d4` | `var(--color-light-gray)` in `:root` |
| **Secondary / Muted Copy** | `#a7a9ac` | `var(--color-warm-gray)` in `:root` |
| **Structural Hairline Border** | `#e5e7eb` | `:after { border: #e5e7eb }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-instrument-sans` | `"Instrument Sans", "Instrument Sans Fallback"` | Typography / Scale Token |
| `--font-space-grotesk` | `"Space Grotesk", "Space Grotesk Fallback"` | Typography / Scale Token |
| `--ai-mark-w` | `70vw` | Dimension / Scale Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--color-cool-gray` | `#808285` | Brand / Palette Token |
| `--color-light-gray` | `#d1d3d4` | Canvas / Surface Token |
| `--color-warm-gray` | `#a7a9ac` | Brand / Palette Token |
| `--font-sans` | `var(--font-instrument-sans), "Instrument Sans", sans-serif` | Typography / Scale Token |
| `--font-display` | `var(--font-sans)` | Typography / Scale Token |
| `--orbit-frame` | `min(21vh, 16vw, 290px)` | Dimension / Scale Token |
| `--tw-border-spacing-x` | `0` | Layout / Spatial Grid Token |
| `--tw-border-spacing-y` | `0` | Layout / Spatial Grid Token |
| `--tw-translate-x` | `0` | Design System Custom Token |
| `--gracefashion-ai-bg` | `#000` | Canvas Substrate (from `var(--color-black)` in `:root`) |
| `--gracefashion-ai-ink` | `#fff` | Primary Typography Ink (stylesheet-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.fixed> — `gracefashion-ai`)**:
   - Landmark `<nav class="fixed top-0">` hosting `KI-Fotostudio für Mode: Bilder ohne ` navigation (`Software · Service · Ratgeber · Team · Demo buchen`), DOM attributes (`data-precedence="next"`), and stylesheet rule `.vGn8MW_className { font-family:Instrument Sans,Instrument Sans Fallback;font-style:normal }`.
2. **Hero Stage & Focal Lead (<section.page-surface> — `KI-Fotostudio für Modemarken: Soft`)**:
   - Landmark `<section class="page-surface px-8">` presenting display lead `KI-Fotostudio für Modemarken: Software und Servic...` and copy excerpt *"Wir verwenden Cookies 🍪"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.bg-black> — `Du entscheidest, was die Welt sehe`)**:
   - Landmark `<section class="bg-black">` rendering section `Du entscheidest, was die Welt sehen und tragen soll.` with copy *"Wir nutzen Cookies, um Ihre Erfahrung zu verbessern, das Nutzerve"*, asset references (`237858b39a32779d-s.p.1ii7211jqpzi...`, `4cf231d25563e07b-s.p.3uuun_-7zsf1...`, `62f37606a5bd6f6f-s.p.3wn_q526zaol...`, `92b6de9cb55945e2-s.p.44ks8kcggj01...`), and grid rule `.vGn8MW_variable { --font-instrument-sans:"Instrument Sans", "Instrument Sans Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.relative> — `Jedes Detail sitzt.`)**:
   - Landmark `<section class="relative h-screen">` framing `Jedes Detail sitzt.` and `Dasselbe Model. Jede Szene.` (*"Datenschutzerklärung"*) with `#808285` surface cards, `#d1d3d4` accents, and `.wdTYSa_className { font-family:Space Grotesk,Space Grotesk Fallback;font-style:normal }`.
5. **Colophon & Global Directory Footer (<footer.relative> — `https://gracefashion.ai`)**:
   - Landmark `<footer class="relative text-white">` anchoring `KI-Fotostudio für Mode: Bilder o` footer links (`Software · Service · Ratgeber · Team · Demo buchen`), copy *"Ein Studio ohne Set."*, and `#e5e7eb` structural dividers.
