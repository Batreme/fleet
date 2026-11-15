# UI & UX Architecture: jockey-stuudio-xyz

## Overview & Design Identity
- **Target**: `jockey-stuudio-xyz` (**Jockey by TwelveLabs: The Video Intelligence Agent**)
- **Production URL**: [https://jockey.stuudio.xyz/](https://jockey.stuudio.xyz/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#a3a3a3` / `#000`)
- **Summary**: The TwelveLabs agent that organizes, searches, and assembles across your entire video library. Built on Pegasus and Marengo. Now in resea...
- **Total Clean CSS Variables Extracted**: `80` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Milling`
- **Body Font Stack**: `Milling Triplex`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: CSS variables `--font-display: "Milling Triplex","Milling","Suisse Intl",sans-serif`, `--text-display: 3rem`, `--text-display--line-height: 1.17`
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.875rem`, `--text-2xl--line-height: 1.15`, `--text-3xl: 3rem`
- **Body Copy**: CSS variables `--text-body: 1rem`, `--text-body--line-height: 1.5`, `--text-body--letter-spacing: .01em`
- **Metadata & Labels**: CSS variables `--text-sm: .875rem`, `--text-sm--line-height: 1.45`, `--default-mono-font-family: var(--font-mono)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#a3a3a3` | `var(--color-neutral-400)` in `:root` |
| **Primary Typography Ink** | `#737373` | `var(--color-neutral-500)` in `:root` |
| **Elevated Surface / Card Substrate** | `#404040` | `var(--color-neutral-700)` in `:root` |
| **Interactive Accent / Highlight** | `#000` | `var(--color-black)` in `:root` |
| **Secondary / Muted Copy** | `#fff` | `var(--color-white)` in `:root` |
| **Structural Hairline Border** | `#f4f3f3` | `var(--color-tag)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--rim-angle` | `0deg` | Design System Custom Token |
| `--font-sans` | `"Milling","Suisse Intl",ui-sans-serif,system-ui,sans-serif` | Typography / Scale Token |
| `--color-neutral-400` | `#a3a3a3` | Brand / Palette Token |
| `--color-neutral-500` | `#737373` | Brand / Palette Token |
| `--color-neutral-700` | `#404040` | Brand / Palette Token |
| `--color-neutral-900` | `oklch(20.5% 0 0)` | Brand / Palette Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--text-sm` | `.875rem` | Typography Ink Token |
| `--text-sm--line-height` | `1.45` | Typography Ink Token |
| `--text-lg` | `1.125rem` | Typography Ink Token |
| `--text-lg--line-height` | `1.5` | Typography Ink Token |
| `--text-xl` | `1.5rem` | Typography Ink Token |
| `--text-xl--line-height` | `1.25` | Typography Ink Token |
| `--text-2xl` | `1.875rem` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.flex> — `jockey-stuudio-xyz`)**:
   - Landmark `<nav class="flex flex-col">` hosting `Jockey by TwelveLabs: The Video Inte` navigation (`Use Cases · Integration · Models · FAQ · Get started`), DOM attributes (`data-precedence="next"`, `data-nav="dark"`, `data-engine="three.js r183"`, `data-nav="dark"`), and stylesheet rule `before { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.relative> — `The agent layer for video understa`)**:
   - Landmark `<section class="relative w-full">` presenting display lead `The agent layer for video understanding` and copy excerpt *"Jockey by TwelveLabs"* over `#a3a3a3` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.relative> — `Know every ad you've ever run.`)**:
   - Landmark `<section class="relative w-full">` rendering section `Know every ad you've ever run.` with copy *"Available in the Claude Connectors Directory"*, asset references (`c9ea9b6355867f69.css`, `webpack-3e3201efe76e74c7.js`, `uwt.js`, `1867067050739407`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.light> — `Automatic Ad Tagging`)**:
   - Landmark `<section class="light relative">` framing `Automatic Ad Tagging` and `Winning Hook Detection` (*"The same intelligence, pointed at your creative library."*) with `#404040` surface cards, `#000` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.relative> — `https://jockey.stuudio.xyz/`)**:
   - Landmark `<footer class="relative flex">` anchoring `Jockey by TwelveLabs: The Video ` footer links (`Use Cases · Integration · Models · FAQ · Get started`), copy *"Automatic Ad Tagging"*, and `#f4f3f3` structural dividers.
