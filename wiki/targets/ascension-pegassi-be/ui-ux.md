# UI & UX Architecture: ascension-pegassi-be

## Overview & Design Identity
- **Target**: `ascension-pegassi-be` (**Ascension — Pegassi**)
- **Production URL**: [https://ascension.pegassi.be/](https://ascension.pegassi.be/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#232323`)
- **Summary**: The debut EP from Belgian electronic artist Pegassi. Four tracks — Ascension, Circles, Forest Walk, Twinflame. Out 4 September 2026.
- **Total Clean CSS Variables Extracted**: `46` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `sans`
- **Body Font Stack**: `mono`
- **Monospace / Technical Font Stack**: `mono`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `1.3rem`, `1.7rem`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `1.3rem`, `1.7rem`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `1.3rem`, `1.7rem`)
- **Metadata & Labels**: CSS variables `--font-mono: "mono", monospace`, `--default-mono-font-family: var(--font-mono)`, `--label: 100`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#7d7d7d` | `var(--color-ink)` in `:root` |
| **Interactive Accent / Highlight** | `#232323` | `var(--color-ink-dim)` in `:root` |
| **Secondary / Muted Copy** | `#121314` | `var(--color-surface)` in `:root` |
| **Structural Hairline Border** | `#1d1f21` | `var(--color-surface-2)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--gl-feather` | `0px` | Dimension / Scale Token |
| `--reveal` | `0` | Design System Custom Token |
| `--font-sans` | `"sans", sans-serif` | Typography / Scale Token |
| `--font-mono` | `"mono", monospace` | Typography / Scale Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.1rem` | Layout / Spatial Grid Token |
| `--font-weight-bold` | `700` | Typography / Scale Token |
| `--ease-out` | `cubic-bezier(0, 0, .2, 1)` | Motion / Easing Token |
| `--blur-sm` | `8px` | Elevation / Border Token |
| `--default-transition-duration` | `.15s` | Motion / Easing Token |
| `--default-transition-timing-function` | `cubic-bezier(.4, 0, .2, 1)` | Motion / Easing Token |
| `--default-font-family` | `var(--font-sans)` | Typography / Scale Token |
| `--default-mono-font-family` | `var(--font-mono)` | Typography / Scale Token |
| `--breakpoint-s` | `650px` | Dimension / Scale Token |
| `--color-ink` | `#7d7d7d` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.absolute> — `ascension-pegassi-be`)**:
   - Landmark `<header class="absolute top-0">` hosting `Ascension — Pegassi` navigation (`Listen · Sequencer · About · Buy`), DOM attributes (`data-gl-host`, `data-engine="three.js r185"`, `data-v-337fa076`, `data-mask="0"`), and stylesheet rule `before { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Pegassi — Ascension EP`)**:
   - Landmark `<section class="hero relative">` presenting display lead `Pegassi — Ascension EP` and copy excerpt *"This EP is all about showing my versatility as an artist. With “A"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.site-max> — `This EP is all about showing my ve`)**:
   - Landmark `<section class="site-max site-grid">` rendering section `This EP is all about showing my versatility as a` with copy *"The title track 1 combines that uplifting yet heavy-hitting energ"*, asset references (`entry.mTHQBrhg.css`, `record-disc.BO204g5c.css`, `site-foot.CthBkmXY.css`, `PPNeueMontreal-Bold.l3ulKZJq.woff2`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.site-max> — `The title track 1 combines that up`)**:
   - Landmark `<section class="site-max site-grid">` framing `The title track 1 combines that uplifting yet he` and `“Circles” 2 is only the second time in my career` (*"“Circles” 2 is only the second time in my career I've stepped on "*) with `#7d7d7d` surface cards, `#232323` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.site-max> — `https://ascension.pegassi.be/`)**:
   - Landmark `<footer class="site-max site-grid">` anchoring `Ascension — Pegassi` footer links (`Listen · Sequencer · About · Buy`), copy *"A1 Ascension (03:01) B1 Forest Walk (03:10)"*, and `#1d1f21` structural dividers.
