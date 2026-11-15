# UI & UX Architecture: helmetverse-ai

## Overview & Design Identity
- **Target**: `helmetverse-ai` (**Helmetverse · Design yours**)
- **Production URL**: [https://helmetverse.ai/](https://helmetverse.ai/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#5db389` / `#fd853a`)
- **Summary**: Type a prompt. The team rides what you imagine.
- **Total Clean CSS Variables Extracted**: `193` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `G42 Sans`
- **Body Font Stack**: `Space Grotesk`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: CSS variables `--text-display: 60px`, `--text-h1: 48px`
- **Section Heading (`H2`)**: CSS variables `--text-h2: 36px`; rule `h2` (`font-size: 15px`, `line-height: 1.3`, `letter-spacing: .02em`, `font-weight: 900`)
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`, `--text-body-lg: 18px`
- **Metadata & Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#5db389` | `var(--g42-hero-tint)` in `:root` |
| **Primary Typography Ink** | `#142a1c` | `var(--g42-hero-tint-dark)` in `:root` |
| **Elevated Surface / Card Substrate** | `#fff6ed` | `var(--color-orange-50)` in `:root` |
| **Interactive Accent / Highlight** | `#fd853a` | `var(--color-orange-400)` in `:root` |
| **Secondary / Muted Copy** | `#fb6514` | `var(--color-orange-500)` in `:root` |
| **Structural Hairline Border** | `#3080ff` | `var(--color-blue-500)` in `:root` |
| **Variable Token (`--color-gray-50`)** | `#f9fafb` | `var(--color-gray-50)` in `:root` |
| **Variable Token (`--color-gray-100`)** | `#f2f4f7` | `var(--color-gray-100)` in `:root` |
| **Variable Token (`--color-gray-200`)** | `#e4e7ec` | `var(--color-gray-200)` in `:root` |
| **Variable Token (`--color-gray-300`)** | `#d0d5dd` | `var(--color-gray-300)` in `:root` |
| **Variable Token (`--color-gray-400`)** | `#98a2b3` | `var(--color-gray-400)` in `:root` |
| **Variable Token (`--color-gray-500`)** | `#667085` | `var(--color-gray-500)` in `:root` |
| **Variable Token (`--color-gray-600`)** | `#475467` | `var(--color-gray-600)` in `:root` |
| **Variable Token (`--color-gray-700`)** | `#344054` | `var(--color-gray-700)` in `:root` |
| **Variable Token (`--color-gray-800`)** | `#1d2939` | `var(--color-gray-800)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--g42-hero-tint` | `#5db389` | Canvas / Surface Token |
| `--g42-hero-tint-dark` | `#142a1c` | Canvas / Surface Token |
| `--font-sans` | `"G42 Sans", "Space Grotesk", sans-serif` | Typography / Scale Token |
| `--color-orange-50` | `#fff6ed` | Brand / Palette Token |
| `--color-orange-400` | `#fd853a` | Brand / Palette Token |
| `--color-orange-500` | `#fb6514` | Brand / Palette Token |
| `--color-blue-500` | `#3080ff` | Brand / Palette Token |
| `--color-gray-50` | `#f9fafb` | Brand / Palette Token |
| `--color-gray-100` | `#f2f4f7` | Brand / Palette Token |
| `--color-gray-200` | `#e4e7ec` | Brand / Palette Token |
| `--color-gray-300` | `#d0d5dd` | Brand / Palette Token |
| `--color-gray-400` | `#98a2b3` | Brand / Palette Token |
| `--color-gray-500` | `#667085` | Brand / Palette Token |
| `--color-gray-600` | `#475467` | Brand / Palette Token |
| `--color-gray-700` | `#344054` | Brand / Palette Token |
| `--color-gray-800` | `#1d2939` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.jsx-25f90e9ce2076406> — `helmetverse-ai`)**:
   - Landmark `<nav class="jsx-25f90e9ce2076406 overflow-hidden">` hosting `Helmetverse · Design yours` navigation (`Home · Gallery · AI Studio · Leaderboard · About`), DOM attributes (`data-paper-shader`, `data-precedence="next"`, `data-precedence="next"`, `data-styled-jsx`), and stylesheet rule `host { --color-blue-500:lab(54.1736% 13.3369 -74.6839) }`.
2. **Hero Stage & Focal Lead (<main.relative> — `HELMETVERSE`)**:
   - Landmark `<main class="relative bg-bg-dark">` presenting display lead `HELMETVERSE` and copy excerpt *"H E L M E T V E R S E"* over `#5db389` canvas and `#142a1c` ink.
3. **Primary Showcase & Content Grid (<main.relative> — `DESIGN WITHOUT LIMITS`)**:
   - Landmark `<main class="relative bg-bg-dark">` rendering section `DESIGN WITHOUT LIMITS` with copy *"Win a trip to Abu Dhabi"*, asset references (`6577f91f-ad74-4868-93e8-13027534a...`, `79d7fc46-0103-4a7f-b9f7-d1012c6fa...`, `98da8316-c3f4-4946-adb6-727aa17a0...`, `b241f184-7659-4fb4-bdb4-cdf53d1fc...`), and grid rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<main.relative> — `A GLOBAL COMPETITION FOR THE MOST `)**:
   - Landmark `<main class="relative bg-bg-dark">` framing `A GLOBAL COMPETITION FOR THE MOST CREATIVE MINDS` and `FEATURED HELMET DESIGNS` (*"THE DESIGNS ARE IN. NOW YOU DECIDE WHO WINS."*) with `#fff6ed` surface cards, `#fd853a` accents, and `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
5. **Colophon & Global Directory Footer (<footer.text-text-primary-dark> — `https://helmetverse.ai/`)**:
   - Landmark `<footer class="text-text-primary-dark">` anchoring `Helmetverse · Design yours` footer links (`Home · Gallery · AI Studio · Leaderboard · About`), copy *"Submissions and voting are officially closed. Explore this y"*, and `#3080ff` structural dividers.
