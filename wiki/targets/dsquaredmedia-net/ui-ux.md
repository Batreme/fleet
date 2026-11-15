# UI & UX Architecture: dsquaredmedia-net

## Overview & Design Identity
- **Target**: `dsquaredmedia-net` (**South Florida Marketing Agency · Branding, Web & AI · Dsquared Media**)
- **Production URL**: [https://dsquaredmedia.net](https://dsquaredmedia.net)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#16161a`)
- **Summary**: Dsquared Media is a boutique West Palm Beach marketing agency serving South Florida. Branding, web design, growth, and AI, built as one s...
- **Total Clean CSS Variables Extracted**: `111` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `jakarta`
- **Body Font Stack**: `jakarta Fallback`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`; rule `,h1` (`font-size: 62px`, `line-height: 1.05`, `letter-spacing: -.03em`, `font-weight: 600`)
- **Section Heading (`H2`)**: rule `,h2` (`font-size: clamp(32px,4vw,56px)`, `line-height: 1.04`, `letter-spacing: -.025em`, `font-weight: 500`)
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`; rule `p` (`font-size: 16px`, `line-height: 1.7`)
- **Metadata & Labels**: CSS variables `--font-mono: var(--font-victor),ui-monospace,monospace`, `--default-mono-font-family: var(--font-mono)`; rule `small` (`font-size: 14px`, `letter-spacing: 0`, `font-weight: 500`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--color-white)` in `:root` |
| **Primary Typography Ink** | `#07090d` | `var(--color-bg)` in `:root` |
| **Elevated Surface / Card Substrate** | `#111113` | `var(--color-surface)` in `:root` |
| **Interactive Accent / Highlight** | `#16161a` | `var(--color-surface-2)` in `:root` |
| **Secondary / Muted Copy** | `#0e0e13` | `var(--color-surface-raised)` in `:root` |
| **Structural Hairline Border** | `#0c0d12` | `var(--color-surface-card)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-sans` | `var(--font-jakarta),system-ui,sans-serif` | Typography / Scale Token |
| `--font-mono` | `var(--font-victor),ui-monospace,monospace` | Typography / Scale Token |
| `--color-amber-50` | `oklch(98.7% .022 95.277)` | Brand / Palette Token |
| `--color-gray-100` | `oklch(96.7% .003 264.542)` | Brand / Palette Token |
| `--color-gray-600` | `oklch(44.6% .03 256.802)` | Brand / Palette Token |
| `--color-gray-900` | `oklch(21% .034 264.665)` | Brand / Palette Token |
| `--color-zinc-200` | `oklch(92% .004 286.32)` | Brand / Palette Token |
| `--color-zinc-900` | `oklch(21% .006 285.885)` | Brand / Palette Token |
| `--color-zinc-950` | `oklch(14.1% .005 285.823)` | Brand / Palette Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--container-7xl` | `80rem` | Layout / Spatial Grid Token |
| `--text-base` | `1rem` | Typography Ink Token |
| `--text-base--line-height` | `calc(1.5 / 1)` | Typography Ink Token |
| `--text-4xl` | `2.25rem` | Typography Ink Token |
| `--text-4xl--line-height` | `calc(2.5 / 2.25)` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.cap-fw-head> — `dsquaredmedia-net`)**:
   - Landmark `<header class="cap-fw-head">` hosting `South Florida Marketing Agency · Bra` navigation (`About · Services · Flex · The Hub · Work`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `before { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
2. **Hero Stage & Focal Lead (<section.hero> — `A South Florida marketing agency b`)**:
   - Landmark `<section class="hero hero-in">` presenting display lead `A South Florida marketing agency built to shape y...` and copy excerpt *"Consent Preferences"* over `#fff` canvas and `#07090d` ink.
3. **Primary Showcase & Content Grid (<section.statement> — `Branding, web, growth and AI, buil`)**:
   - Landmark `<section class="statement">` rendering section `Branding, web, growth and AI, built as one system.` with copy *"We live in a world shaped by perception."*, asset references (`636a5ac981f94f8b-s.p.woff2`, `8d2bb7cdfa09b0c5-s.p.woff2`, `ee62220d3ef0f600.css`, `182c5d4bd48e5167.css`), and grid rule `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.cap-fw> — `Graphic Design`)**:
   - Landmark `<section class="cap-fw anim">` framing `Graphic Design` and `Web Design & Development` (*"A full-service marketing agency in West Palm Beach, working with "*) with `#111113` surface cards, `#16161a` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.caf-footer> — `https://dsquaredmedia.net`)**:
   - Landmark `<footer class="caf-footer">` anchoring `South Florida Marketing Agency ·` footer links (`About · Services · Flex · The Hub · Work`), copy *"5.0 across 100+ client reviews"*, and `#0c0d12` structural dividers.
