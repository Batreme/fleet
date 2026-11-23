---
title: "UI & UX Architecture: www-lucaslima-design"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-lucaslima-design

## Overview & Design Identity
- **Target**: `www-lucaslima-design` (**Lucas Lima · Product designer and design engineer**)
- **Production URL**: [https://www.lucaslima.design/](https://www.lucaslima.design/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f4f4f2` / `#1570ef`)
- **Summary**: Brazilian product designer working across SaaS, finance and AI. I work directly in code, exploring live interfaces and bridging design an...
- **Total Clean CSS Variables Extracted**: `143` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `General Sans`
- **Body Font Stack**: `Inter Variable`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 102.237px`, `line-height: 92.0131px`, `font-weight: 500`, `letter-spacing: -4.60066px`); CSS variables `--brand-display: 4rem`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 14px`, `line-height: 20.3px`, `font-weight: 500`); rule `h2` (`letter-spacing: inherit`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--brand-body: 1rem`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 17px`, `line-height: 24.65px`, `font-weight: 400`, `letter-spacing: -0.17px`); CSS variables `--font-mono: "Inter Variable", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif`, `--brand-caption: .8125rem`, `--default-mono-font-family: var(--font-mono)`; rule `small` (`font-size: 12px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#f4f4f2` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#121211` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f2f3f5` | `var(--color-card-surface)` in `:root` |
| **Interactive Accent / Highlight** | `#1570ef` | `var(--brand)` in `:root` |
| **Secondary / Muted Copy** | `#8a8983` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#d7d7d0` | `var(--brand-divider)` in `:root` |
| **Variable Token (`--color-gray-50`)** | `#fafafb` | `var(--color-gray-50)` in `:root` |
| **Variable Token (`--color-gray-200`)** | `#e9ebee` | `var(--color-gray-200)` in `:root` |
| **Variable Token (`--color-gray-300`)** | `#dce0e5` | `var(--color-gray-300)` in `:root` |
| **Variable Token (`--color-gray-400`)** | `#c1c6ce` | `var(--color-gray-400)` in `:root` |
| **Variable Token (`--color-gray-500`)** | `#737b88` | `var(--color-gray-500)` in `:root` |
| **Variable Token (`--color-gray-600`)** | `#626a76` | `var(--color-gray-600)` in `:root` |
| **Variable Token (`--color-gray-700`)** | `#454c57` | `var(--color-gray-700)` in `:root` |
| **Variable Token (`--color-gray-800`)** | `#2c313a` | `var(--color-gray-800)` in `:root` |
| **Variable Token (`--color-gray-900`)** | `#1c2027` | `var(--color-gray-900)` in `:root` |
| **Variable Token (`--color-gray-950`)** | `#101318` | `var(--color-gray-950)` in `:root` |
| **Variable Token (`--cover-surface`)** | `#e9ebef` | `var(--cover-surface)` in `:root` |
| **Variable Token (`--cover-hover`)** | `#e3e6eb` | `var(--cover-hover)` in `:root` |

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
   - Landmark `<header class="st-header">` (`1361x44px`) hosting `Lucas Lima · Product designer and de` navigation (`Lucas Lima · Projects · Writing · About · Photography`), DOM attributes (`data-theme="light"`, `data-prerendered="true"`, `data-js="live"`, `data-intro="play"`), and stylesheet rule `html { scroll-behavior:auto;scrollbar-gutter:stable }`.
2. **Hero Stage & Focal Lead (<section.st-pad> — `SENIOR PRODUCT DESIGNER`)**:
   - Landmark `<section class="st-pad">` presenting display lead `SENIOR PRODUCT DESIGNER` and copy excerpt *"Lucas Lima is a Brazilian designer and psychologist with a soft s"* over `#f4f4f2` canvas and `#121211` ink.
3. **Primary Showcase & Content Grid (<section.st-pad:nth(2)> — `Senior Product Designer`)**:
   - Landmark `<section class="st-pad">` rendering section `Senior Product Designer` with copy *"hello@lucaslima.design Copied"*, asset references (`general-sans-500.woff2`, `general-sans-400.woff2`, `favicon.ico`, `favicon.svg`), and grid rule `body { font-family:var(--font-sans) }`.
4. **Interactive Detail & Feature Matrix (<section.st-pad:nth(3)> — `Selected work`)**:
   - Landmark `<section class="st-pad">` framing `Selected work` and `Things I make on the side` (*"hello@lucaslima.design"*) with `#f2f3f5` surface cards, `#1570ef` accents, and `.portfolio { min-height:100svh }`.
5. **Colophon & Global Directory Footer (<footer.st-footer> — `https://www.lucaslima.design/`)**:
   - Landmark `<footer class="st-footer">` anchoring `Lucas Lima · Product designer an` footer links (`Lucas Lima · Projects · Writing · About · Photography`), copy *"Internal tools & ops"*, and `#d7d7d0` structural dividers.
