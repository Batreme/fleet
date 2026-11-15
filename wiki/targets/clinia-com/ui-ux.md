# UI & UX Architecture: clinia-com

## Overview & Design Identity
- **Target**: `clinia-com` (**Patient Context for Healthcare AI · Clinia**)
- **Production URL**: [https://clinia.com](https://clinia.com)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#ff5c00`)
- **Summary**: Fragmented health data breaks AI. Clinia reconciles it into graph-based context so your healthcare AI agents stay reliable and support op...
- **Total Clean CSS Variables Extracted**: `231` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `NaN Serf B Text`
- **Body Font Stack**: `Circular XX`
- **Monospace / Technical Font Stack**: `Circular XX Mono`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `18px`)
- **Section Heading (`H2`)**: CSS variables `--has-subtitle: 0`, `--subtitle-height: 0px`; rule `h2` (`font-size: 22px`, `line-height: 1.1`)
- **Body Copy**: CSS variables `--ff-body: Circular XX,sans-serif`, `--body-text-color: light-dark(var(--color-primary),var(--color-white))`, `--body-bg-color: light-dark(var(--color-white),var(--gray-900))`
- **Metadata & Labels**: CSS variables `--ff-mono: Circular XX Mono,monospace`, `--hsf-default-field-label__color: currentColor!important`, `--hsf-default-field-label__font-family: Circular XX,sans-serif!important`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#1a1a1e` | `var(--color-primary)` in `:root` |
| **Interactive Accent / Highlight** | `#ff5c00` | `var(--color-secondary)` in `:root` |
| **Secondary / Muted Copy** | `#cca44f` | `var(--color-noble)` in `:root` |
| **Structural Hairline Border** | `#95795c` | `var(--color-trust)` in `:root` |
| **Variable Token (`--color-trust-dark`)** | `#53402c` | `var(--color-trust-dark)` in `:root` |
| **Variable Token (`--color-remedy`)** | `#fcf8ef` | `var(--color-remedy)` in `:root` |
| **Variable Token (`--color-remedy-dark`)** | `#ecd9b9` | `var(--color-remedy-dark)` in `:root` |
| **Variable Token (`--color-remedy-medium`)** | `#f2eee5` | `var(--color-remedy-medium)` in `:root` |
| **Variable Token (`--color-remedy-light`)** | `#f9f7f2` | `var(--color-remedy-light)` in `:root` |
| **Variable Token (`--color-aura`)** | `#f7f1ff` | `var(--color-aura)` in `:root` |
| **Variable Token (`--color-aura-dark`)** | `#cabbdb` | `var(--color-aura-dark)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-transparent` | `transparent` | Brand / Palette Token |
| `--color-current` | `currentColor` | Brand / Palette Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--color-primary` | `#1a1a1e` | Brand / Palette Token |
| `--color-secondary` | `#ff5c00` | Brand / Palette Token |
| `--color-vital` | `#ff5c00` | Brand / Palette Token |
| `--color-noble` | `#cca44f` | Brand / Palette Token |
| `--color-trust` | `#95795c` | Brand / Palette Token |
| `--color-trust-dark` | `#53402c` | Canvas / Surface Token |
| `--color-remedy` | `#fcf8ef` | Brand / Palette Token |
| `--color-remedy-dark` | `#ecd9b9` | Canvas / Surface Token |
| `--color-remedy-medium` | `#f2eee5` | Brand / Palette Token |
| `--color-remedy-light` | `#f9f7f2` | Canvas / Surface Token |
| `--color-aura` | `#f7f1ff` | Brand / Palette Token |
| `--color-aura-dark` | `#cabbdb` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `clinia-com`)**:
   - Landmark `<header class="site-header position-fixed">` hosting `Patient Context for Healthcare AI · ` navigation (`Documentation · Changelog · Blog · Trust Center · About us`), DOM attributes (`data-env="production"`, `data-wp-strategy="async"`, `data-site-loader`, `data-site-transition`), and stylesheet rule `webkit-scrollbar { display:none }`.
2. **Hero Stage & Focal Lead (<main.flex-grow-1> — `Health data, turned into a patient`)**:
   - Landmark `<main class="flex-grow-1">` presenting display lead `Health data, turned into a patient story` and copy excerpt *"Product Clinia Context Engine Product A health-specific context l"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<main.flex-grow-1> — `Engineered for AI agents in missio`)**:
   - Landmark `<main class="flex-grow-1">` rendering section `Engineered for AI agents in mission-critical heal...` with copy *"Clinia Context Engine"*, asset references (`humans.txt`, `xmlrpc.php`, `gtm.js`, `embed`), and grid rule `active { cursor:grabbing }`.
4. **Interactive Detail & Feature Matrix (<main.flex-grow-1> — `Health-native`)**:
   - Landmark `<main class="flex-grow-1">` framing `Health-native` and `Evaluation-first` (*"Product A health-specific context layer that sits between patient"*) with `#1a1a1e` surface cards, `#ff5c00` accents, and `blossom-dots>blossom-dot { display:none }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://clinia.com`)**:
   - Landmark `<footer class="site-footer container-fluid">` anchoring `Patient Context for Healthcare A` footer links (`Documentation · Changelog · Blog · Trust Center · About us`), copy *"A health-specific context layer that sits between patient da"*, and `#95795c` structural dividers.
