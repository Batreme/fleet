# UI & UX Architecture: www-lucaslima-design

## Overview & Design Identity
- **Target**: `www-lucaslima-design` (**Lucas Lima · Product designer and design engineer**)
- **Production URL**: [https://www.lucaslima.design/](https://www.lucaslima.design/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fafafb` / `#dce0e5`)
- **Summary**: Brazilian product designer working across SaaS, finance and AI. I work directly in code, exploring live interfaces and bridging design an...
- **Total Clean CSS Variables Extracted**: `143` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `DM Sans Variable`
- **Body Font Stack**: `Inter Variable`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **Hero Display (`H1`)**: CSS variables `--brand-display: 4rem`
- **Section Heading (`H2`)**: rule `h2` (`letter-spacing: inherit`)
- **Body Copy**: CSS variables `--brand-body: 1rem`
- **Metadata & Labels**: CSS variables `--font-mono: "Inter Variable", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif`, `--brand-caption: .8125rem`, `--default-mono-font-family: var(--font-mono)`; rule `small` (`font-size: 12px`, `font-weight: 400`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fafafb` | `var(--color-gray-50)` in `:root` |
| **Primary Typography Ink** | `#f2f3f5` | `var(--color-gray-100)` in `:root` |
| **Elevated Surface / Card Substrate** | `#e9ebee` | `var(--color-gray-200)` in `:root` |
| **Interactive Accent / Highlight** | `#dce0e5` | `var(--color-gray-300)` in `:root` |
| **Secondary / Muted Copy** | `#c1c6ce` | `var(--color-gray-400)` in `:root` |
| **Structural Hairline Border** | `#737b88` | `var(--color-gray-500)` in `:root` |
| **Variable Token (`--color-gray-600`)** | `#626a76` | `var(--color-gray-600)` in `:root` |
| **Variable Token (`--color-gray-700`)** | `#454c57` | `var(--color-gray-700)` in `:root` |
| **Variable Token (`--color-gray-800`)** | `#2c313a` | `var(--color-gray-800)` in `:root` |
| **Variable Token (`--color-gray-900`)** | `#1c2027` | `var(--color-gray-900)` in `:root` |
| **Variable Token (`--color-gray-950`)** | `#101318` | `var(--color-gray-950)` in `:root` |
| **Variable Token (`--cover-surface`)** | `#e9ebef` | `var(--cover-surface)` in `:root` |
| **Variable Token (`--cover-hover`)** | `#e3e6eb` | `var(--cover-hover)` in `:root` |
| **Variable Token (`--hairline`)** | `#1c202710` | `var(--hairline)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-gray-50` | `#fafafb` | Brand / Palette Token |
| `--color-gray-100` | `#f2f3f5` | Brand / Palette Token |
| `--color-gray-200` | `#e9ebee` | Brand / Palette Token |
| `--color-gray-300` | `#dce0e5` | Brand / Palette Token |
| `--color-gray-400` | `#c1c6ce` | Brand / Palette Token |
| `--color-gray-500` | `#737b88` | Brand / Palette Token |
| `--color-gray-600` | `#626a76` | Brand / Palette Token |
| `--color-gray-700` | `#454c57` | Brand / Palette Token |
| `--color-gray-800` | `#2c313a` | Brand / Palette Token |
| `--color-gray-900` | `#1c2027` | Brand / Palette Token |
| `--color-gray-950` | `#101318` | Brand / Palette Token |
| `--color-card-surface` | `#f2f3f5` | Canvas / Surface Token |
| `--color-card-fade` | `#f2f3f5` | Brand / Palette Token |
| `--cover-surface` | `#e9ebef` | Canvas / Surface Token |
| `--cover-hover` | `#e3e6eb` | Color / Atmospheric Token |
| `--hairline` | `#1c202710` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.st-header> — `www-lucaslima-design`)**:
   - Landmark `<header class="st-header">` hosting `Lucas Lima · Product designer and de` navigation (`Lucas Lima · Projects · Writing · About · Photography`), DOM attributes (`data-theme="light"`, `data-prerendered="true"`, `data-js="live"`, `data-intro="play"`), and stylesheet rule `html { scroll-behavior:auto;scrollbar-gutter:stable }`.
2. **Hero Stage & Focal Lead (<section.st-pad> — `Senior Product Designer`)**:
   - Landmark `<section class="st-pad">` presenting display lead `Senior Product Designer` and copy excerpt *"hello@lucaslima.design Copied"* over `#fafafb` canvas and `#737b88` ink.
3. **Primary Showcase & Content Grid (<section.st-pad> — `Selected work`)**:
   - Landmark `<section class="st-pad">` rendering section `Selected work` with copy *"hello@lucaslima.design"*, asset references (`general-sans-500.woff2`, `general-sans-400.woff2`, `favicon.ico`, `favicon.svg`), and grid rule `body { font-family:var(--font-sans) }`.
4. **Interactive Detail & Feature Matrix (<section.st-pad> — `Things I make on the side`)**:
   - Landmark `<section class="st-pad">` framing `Things I make on the side` and `Writing` (*"And design engineer, designing in code"*) with `#e9ebee` surface cards, `#dce0e5` accents, and `.portfolio { min-height:100svh }`.
5. **Colophon & Global Directory Footer (<footer.st-footer> — `https://www.lucaslima.design/`)**:
   - Landmark `<footer class="st-footer">` anchoring `Lucas Lima · Product designer an` footer links (`Lucas Lima · Projects · Writing · About · Photography`), copy *"Lucas Lima is a Brazilian designer and psychologist with a s"*, and `#737b88` structural dividers.
