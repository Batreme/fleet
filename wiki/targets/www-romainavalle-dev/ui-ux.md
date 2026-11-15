# UI & UX Architecture: www-romainavalle-dev

## Overview & Design Identity
- **Target**: `www-romainavalle-dev` (**Romain Avalle - Interactive developper**)
- **Production URL**: [https://www.romainavalle.dev/](https://www.romainavalle.dev/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#000000`)
- **Summary**: Romain Avalle, interactive developer since 2006. Team Lead & Tech Lead at REF Digital in Montréal. Awwwards jury member, 40+ Awwwards and...
- **Total Clean CSS Variables Extracted**: `11` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `RemusVariableVF`
- **Body Font Stack**: `andale-mono`
- **Monospace / Technical Font Stack**: `andale-mono`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `1.2rem`, `1.6rem`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `1.2rem`, `1.6rem`)
- **Body Copy**: rule `,body` (`font-size: 1.6rem`, `line-height: 1.2`, `letter-spacing: -.03rem`, `font-weight: 600`)
- **Metadata & Labels**: CSS variables `--default-mono-font-family: var(--font-mono)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--color-white)` in `:root` |
| **Primary Typography Ink** | `#000` | `var(--color-black)` in `:root` |
| **Elevated Surface / Card Substrate** | `#0000` | `textarea { background-color: #0000 }` |
| **Interactive Accent / Highlight** | `#000000` | `.bg-black { background-color: black }` (`#000000`) |
| **Secondary / Muted Copy** | `#ffffff` | `.text-white { color: white }` (`#ffffff`) |
| **Structural Hairline Border** | `#f3f2f1` | `<meta name="theme-color" content="#f3f2f1">` in `dom.html` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--spacing` | `.1rem` | Layout / Spatial Grid Token |
| `--default-transition-duration` | `.15s` | Motion / Easing Token |
| `--default-transition-timing-function` | `cubic-bezier(.23, 1, .32, 1)` | Motion / Easing Token |
| `--default-font-family` | `var(--font-sans)` | Typography / Scale Token |
| `--default-mono-font-family` | `var(--font-mono)` | Typography / Scale Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--size` | `375` | Layout / Spatial Grid Token |
| `--lvh` | `1lvh` | Layout / Spatial Grid Token |
| `--dvh` | `1dvh` | Layout / Spatial Grid Token |
| `--svh` | `1svh` | Layout / Spatial Grid Token |
| `--tw-translate-x` | `0` | Design System Custom Token |
| `--tw-translate-y` | `0` | Design System Custom Token |
| `--tw-translate-z` | `0` | Design System Custom Token |
| `--www-romainavalle-bg` | `#fff` | Canvas Substrate (from `var(--color-white)` in `:root`) |
| `--www-romainavalle-ink` | `#000` | Primary Typography Ink (stylesheet-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.bg-black> — `www-romainavalle-dev`)**:
   - Landmark `<header class="bg-black text-white">` hosting `Romain Avalle - Interactive developp` navigation (`Let's talk`), DOM attributes (`data-v-54411a74`, `data-char="R"`, `data-char="o"`, `data-char="m"`), and stylesheet rule `.common-scene { height:100lvh }`.
2. **Hero Stage & Focal Lead (<section.white> — `R o m a i n A v a l l e`)**:
   - Landmark `<section class="white">` presenting display lead `R o m a i n A v a l l e` and copy excerpt *"Interactive Developer"* over `#fff` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.bg-black> — `I n t e r a c t i v e D e v e l o `)**:
   - Landmark `<section class="bg-black">` rendering section `I n t e r a c t i v e D e v e l o p e r` with copy *"█ █ █ █ █ █ █ █ █ █ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░"*, asset references (`gtm.js`, `_payload.json`, `BC66KIH3.js`, `B3W-aES6.js`), and grid rule `before { transform:scaleX(1) }`.
4. **Interactive Detail & Feature Matrix (<section.text-white> — `█ █ █ █ █ █ █ █ █ █ ░ ░ ░ ░ ░ ░ ░ `)**:
   - Landmark `<section class="text-white">` framing `█ █ █ █ █ █ █ █ █ █ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ` and `R o m a i n A v a l l e` (*"R o m a i n A v a l l e"*) with `#0000` surface cards, `#000000` accents, and `html.lenis body { height:auto }`.
5. **Colophon & Global Directory Footer (<footer.h-screen> — `https://www.romainavalle.dev/`)**:
   - Landmark `<footer class="h-screen relative">` anchoring `Romain Avalle - Interactive deve` footer links (`Let's talk`), copy *"I n t e r a c t i v e D e v e l o p e r"*, and `#f3f2f1` structural dividers.
