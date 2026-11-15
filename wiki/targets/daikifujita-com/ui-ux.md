# UI & UX Architecture: daikifujita-com

## Overview & Design Identity
- **Target**: `daikifujita-com` (**Daiki Fujita — Web & Interactive Designer**)
- **Production URL**: [https://daikifujita.com](https://daikifujita.com)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ecebe6` / `#0b0a0d`)
- **Summary**: Portfolio of Daiki Fujita, a Tokyo-based web & interactive designer. Read it awake, or float through it in a 3D dream.
- **Total Clean CSS Variables Extracted**: `60` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Noto Sans JP`
- **Body Font Stack**: `Noto Serif JP`
- **Monospace / Technical Font Stack**: `DM Mono`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `var(--font-size)`, `var(--framer-font-size)`, `16px`, `13px`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `var(--font-size)`, `var(--framer-font-size)`, `16px`, `13px`)
- **Body Copy**: rule `p` (`font-size: 13px`, `line-height: 1.45em`, `letter-spacing: 0em`, `font-weight: 400`)
- **Metadata & Labels**: CSS variables `--letter-spacing: var(--framer-letter-spacing)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#ecebe6` | `var(--token-dfed7a8a-d0f4-4bbe-b1a8-7f125b4dcf9c)` in `:root` |
| **Primary Typography Ink** | `#111` | `var(--token-09b1fdd2-64d9-4345-a0e9-61b5008f6c7f)` in `:root` |
| **Elevated Surface / Card Substrate** | `#7a7872` | `var(--token-89e81946-36e7-4367-b395-dfe5c069c887)` in `:root` |
| **Interactive Accent / Highlight** | `#0b0a0d` | `var(--token-8edb35f3-075c-46ed-a38f-cc7cf5377848)` in `:root` |
| **Secondary / Muted Copy** | `#7df9ff` | `var(--token-cef47311-5367-476e-bfaa-32cb261c2ae6)` in `:root` |
| **Structural Hairline Border** | `#ff4fa3` | `var(--token-012110b6-be3f-4bbf-9620-ec3cf67bd5ff)` in `:root` |
| **Variable Token (`--token-9350f153-bb96-4c30-9f32-0731279d6889`)** | `#11111124` | `var(--token-9350f153-bb96-4c30-9f32-0731279d6889)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--token-dfed7a8a-d0f4-4bbe-b1a8-7f125b4dcf9c` | `#ecebe6` | Color / Atmospheric Token |
| `--token-09b1fdd2-64d9-4345-a0e9-61b5008f6c7f` | `#111` | Color / Atmospheric Token |
| `--token-89e81946-36e7-4367-b395-dfe5c069c887` | `#7a7872` | Color / Atmospheric Token |
| `--token-9350f153-bb96-4c30-9f32-0731279d6889` | `#11111124` | Color / Atmospheric Token |
| `--token-8edb35f3-075c-46ed-a38f-cc7cf5377848` | `#0b0a0d` | Color / Atmospheric Token |
| `--token-cef47311-5367-476e-bfaa-32cb261c2ae6` | `#7df9ff` | Color / Atmospheric Token |
| `--token-012110b6-be3f-4bbf-9620-ec3cf67bd5ff` | `#ff4fa3` | Color / Atmospheric Token |
| `--text-decoration-skip-ink` | `var(--framer-text-decoration-skip-ink)` | Typography Ink Token |
| `--text-underline-offset` | `var(--framer-text-decoration-offset)` | Typography Ink Token |
| `--font-family` | `var(--framer-font-family)` | Typography / Scale Token |
| `--font-style` | `var(--framer-font-style)` | Typography / Scale Token |
| `--font-weight` | `var(--framer-font-weight)` | Typography / Scale Token |
| `--text-color` | `var(--framer-text-color)` | Typography Ink Token |
| `--letter-spacing` | `var(--framer-letter-spacing)` | Typography / Scale Token |
| `--font-size` | `var(--framer-font-size)` | Typography / Scale Token |
| `--text-transform` | `var(--framer-text-transform)` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.framer-v72h6k> — `daikifujita-com`)**:
   - Landmark `<header class="framer-v72h6k">` hosting `Daiki Fujita — Web & Interactive Des` navigation (`Work · About`), DOM attributes (`data-framer-generated-canonical`, `data-a7-fonts="1"`, `data-framer-font-css`, `data-framer-breakpoint-css`), and stylesheet rule `.hidden-72rtr7 { display:none!important }`.
2. **Hero Stage & Focal Lead (<section.a12-hero> — `S i t e s f o r w a k i n g . W o `)**:
   - Landmark `<section class="a12-hero">` presenting display lead `S i t e s f o r w a k i n g . W o r l d s f o r d...` and copy excerpt *"S i t e s f o r w a k i n g . W o r l d s f o r d r e a m i n g ."* over `#ecebe6` canvas and `#0b0a0d` ink.
3. **Primary Showcase & Content Grid (<section.a12-about> — `P o r t f o l i o v 2`)**:
   - Landmark `<section class="a12-about">` rendering section `P o r t f o l i o v 2` with copy *"S i t e s f o r w a k i n g . W o r l d s f o r d r e a m i n g ."*, asset references (`eVYj6CNzGc62XpZaIv01nduVWdE.png`, `roLES6HVvAZ1b2iqx3qK2NkfU.png`, `MgHTWMPbFXn5g22t0c6RJPZlpAQ.png`, `fonts.googleapis.com`), and grid rule `.hidden-1htmigo { display:none!important }`.
4. **Interactive Detail & Feature Matrix (<section.a12-disc> — `I N C E P T U R E`)**:
   - Landmark `<section class="a12-disc">` framing `I N C E P T U R E` and `P o r t f o l i o v 1` (*"Web & Interactive Designer — Tokyo"*) with `#7a7872` surface cards, `#0b0a0d` accents, and `.hidden-1y8oy23 { display:none!important }`.
5. **Colophon & Global Directory Footer (<footer.aw-grid> — `https://daikifujita.com`)**:
   - Landmark `<footer class="aw-grid aw-label">` anchoring `Daiki Fujita — Web & Interactive` footer links (`Work · About`), copy *"Web · Motion Interaction · 3D · UI/UX"*, and `#ff4fa3` structural dividers.
