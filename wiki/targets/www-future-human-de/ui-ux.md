# UI & UX Architecture: www-future-human-de

## Overview & Design Identity
- **Target**: `www-future-human-de` (**FUTURE HUMAN · A Shared Year of Co-Creation & Presence**)
- **Production URL**: [https://www.future-human.de/](https://www.future-human.de/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#fff9ea` canvas, `#000` ink, `#fff` accent)
- **Summary**: A one-year training for multidimensional coaching & co-creation. 8 modules, 16 participants, at Das HILLA near Kassel. Starts Oct 30, 2026.
- **Total Clean CSS Variables Extracted**: `30` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Spectral`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: rule `h1` (`font-size: 32px`, `line-height: 110%`, `letter-spacing: -.04em`, `font-weight: 300`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `var(--font-size)`, `var(--framer-font-size)`, `32px`, `28px`)
- **Body Copy**: rule `p` (`font-size: 18px`, `line-height: 140%`, `letter-spacing: -.02em`, `font-weight: 300`)
- **Metadata & Labels**: CSS variables `--letter-spacing: var(--framer-letter-spacing)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff9ea` | `var(--token-0ae2222e-ae06-4270-a415-3dc68910790b)` in `:root` |
| **Primary Typography Ink** | `#121212` | `var(--token-5d91ee23-be21-4524-9b74-738a7ee13f13)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fffefc` | `var(--token-30996a26-1fe4-4007-9944-c80e3f142e44)` in `:root` |
| **Interactive Accent / Highlight** | `#fff` | `var(--token-5f5766cb-e316-4651-8423-ae295a71112c)` in `:root` |
| **Secondary / Muted Copy** | `#09f` | `.framer-S82Lr .framer-jkecn2 { color: #09f }` |
| **Structural Hairline Border** | `#000` | `:hover { color: #000 }` |
| **Variable Token (`--token-b6e76abb-dcfc-435b-9de5-4434133bc927`)** | `#fff9eacc` | `var(--token-b6e76abb-dcfc-435b-9de5-4434133bc927)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--token-0ae2222e-ae06-4270-a415-3dc68910790b` | `#fff9ea` | Color / Atmospheric Token |
| `--token-b6e76abb-dcfc-435b-9de5-4434133bc927` | `#fff9eacc` | Color / Atmospheric Token |
| `--token-5d91ee23-be21-4524-9b74-738a7ee13f13` | `#121212` | Color / Atmospheric Token |
| `--token-30996a26-1fe4-4007-9944-c80e3f142e44` | `#fffefc` | Color / Atmospheric Token |
| `--token-5f5766cb-e316-4651-8423-ae295a71112c` | `#fff` | Color / Atmospheric Token |
| `--text-decoration-skip-ink` | `var(--framer-text-decoration-skip-ink)` | Typography Ink Token |
| `--text-underline-offset` | `var(--framer-text-decoration-offset)` | Typography Ink Token |
| `--font-family` | `var(--framer-font-family)` | Typography / Scale Token |
| `--font-style` | `var(--framer-font-style)` | Typography / Scale Token |
| `--font-weight` | `var(--framer-font-weight)` | Typography / Scale Token |
| `--text-color` | `var(--framer-text-color)` | Typography Ink Token |
| `--letter-spacing` | `var(--framer-letter-spacing)` | Typography / Scale Token |
| `--font-size` | `var(--framer-font-size)` | Typography / Scale Token |
| `--text-transform` | `var(--framer-text-transform)` | Typography Ink Token |
| `--line-height` | `var(--framer-line-height)` | Typography / Scale Token |
| `--overflow-clip-fallback` | `hidden` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.framer-1m76co> — `www-future-human-de`)**:
   - Landmark `<nav class="framer-1m76co">` hosting `FUTURE HUMAN · A Shared Year of Co-C` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-framer-font-css`, `data-framer-breakpoint-css`, `data-framer-css-ssr-minified`, `data-framer-components="framer-lib-cursors-ho..."`), and stylesheet rule `.hidden-72rtr7 { display:none!important }`.
2. **Hero Stage & Focal Lead (<section.framer-16vyecu> — `T H E F U T U R E I S H U M A N .`)**:
   - Landmark `<section class="framer-16vyecu sct-room">` presenting display lead `T H E F U T U R E I S H U M A N .` and copy excerpt *"D i e W e l t b r a u c h t d e i n e e i n z i g a r t i g e G a"* over `#fff9ea` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.framer-1omsice> — `T h e M u l t i d i m e n s i o n `)**:
   - Landmark `<section class="framer-1omsice sct-room">` rendering section `T h e M u l t i d i m e n s i o n a l H u m a n` with copy *"e i n z i g a r t i g e"*, asset references (`GAHKwEi2fQdp0x0qCbx0ph5tnCs.png`, `fonts.gstatic.com`, `hls.min.js`, `script`), and grid rule `.hidden-181529u { display:none!important }`.
4. **Interactive Detail & Feature Matrix (<section.framer-i64cag> — `T h e C o l l e c t i v e F i e l `)**:
   - Landmark `<section class="framer-i64cag sct-room">` framing `T h e C o l l e c t i v e F i e l d` and `T h e P a t h & T h e S a n c t u a r y` (*"M u l t i d i m e n s i o n a l"*) with `#fffefc` surface cards, `#fff` accents, and `.hidden-126ue0n { display:none!important }`.
5. **Colophon & Global Directory Footer (<footer.framer-1818ei9> — `https://www.future-human.de/`)**:
   - Landmark `<footer class="framer-1818ei9">` anchoring `FUTURE HUMAN · A Shared Year of ` footer links (`Overview · Index · Archive · About · Contact`), copy *"C o l l e c t i v e"*, and `#000` structural dividers.
