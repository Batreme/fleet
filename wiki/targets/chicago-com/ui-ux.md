# UI & UX Architecture: chicago-com

## Overview & Design Identity
- **Target**: `chicago-com` (**chicago.com**)
- **Production URL**: [https://chicago.com/](https://chicago.com/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#fb2c36` canvas, `#c7d2ff` ink, `#00bb7f` accent)
- **Summary**: Local guides, community conversation, and news from every Chicago newsroom, gathered in one place.
- **Total Clean CSS Variables Extracted**: `385` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `tempo`
- **Body Font Stack**: `tempo Fallback`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--osano-display-position: bottom`
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `var(--cdc--font-size--16)`, `var(--cdc--font-size--18)`, `2.5rem`, `3.5rem`, `1.1875rem`)
- **Body Copy**: CSS variables `--color-body: #46423b`, `--loginForm--state-body--color: var(--cdc--color--text-secondary)`, `--loginForm--state-body--font-size: var(--cdc--font-size--14)`; rule `p` (`font-size: 16px`, `line-height: 22px`, `font-weight: 400`)
- **Metadata & Labels**: CSS variables `--font-mono: var(--font-dm-mono), ui-monospace, monospace`, `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fb2c36` | `var(--color-red-500)` in `:root` |
| **Primary Typography Ink** | `#e40014` | `var(--color-red-600)` in `:root` |
| **Elevated Surface / Card Substrate** | `#f99c00` | `var(--color-amber-500)` in `:root` |
| **Interactive Accent / Highlight** | `#00bb7f` | `var(--color-emerald-500)` in `:root` |
| **Secondary / Muted Copy** | `#c7d2ff` | `var(--color-indigo-200)` in `:root` |
| **Structural Hairline Border** | `#a4b3ff` | `var(--color-indigo-300)` in `:root` |
| **Variable Token (`--color-gray-100`)** | `#f3f4f6` | `var(--color-gray-100)` in `:root` |
| **Variable Token (`--color-gray-200`)** | `#e5e7eb` | `var(--color-gray-200)` in `:root` |
| **Variable Token (`--color-gray-300`)** | `#d1d5dc` | `var(--color-gray-300)` in `:root` |
| **Variable Token (`--color-gray-700`)** | `#364153` | `var(--color-gray-700)` in `:root` |
| **Variable Token (`--color-zinc-100`)** | `#f4f4f5` | `var(--color-zinc-100)` in `:root` |
| **Variable Token (`--color-zinc-300`)** | `#d4d4d8` | `var(--color-zinc-300)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--cdc--font--tempo` | `"tempo", "tempo Fallback"` | Typography / Scale Token |
| `--cdc--font--tenon` | `"tenon", "tenon Fallback"` | Typography / Scale Token |
| `--font-sans` | `var(--cdc--font--primary), ui-sans-serif, system-ui, sans-serif` | Typography / Scale Token |
| `--font-mono` | `var(--font-dm-mono), ui-monospace, monospace` | Typography / Scale Token |
| `--color-red-500` | `#fb2c36` | Brand / Palette Token |
| `--color-red-600` | `#e40014` | Brand / Palette Token |
| `--color-amber-500` | `#f99c00` | Brand / Palette Token |
| `--color-emerald-500` | `#00bb7f` | Brand / Palette Token |
| `--color-indigo-200` | `#c7d2ff` | Brand / Palette Token |
| `--color-indigo-300` | `#a4b3ff` | Brand / Palette Token |
| `--color-gray-100` | `#f3f4f6` | Brand / Palette Token |
| `--color-gray-200` | `#e5e7eb` | Brand / Palette Token |
| `--color-gray-300` | `#d1d5dc` | Brand / Palette Token |
| `--color-gray-700` | `#364153` | Brand / Palette Token |
| `--color-zinc-100` | `#f4f4f5` | Brand / Palette Token |
| `--color-zinc-300` | `#d4d4d8` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.osano-cm-window> — `chicago-com`)**:
   - Landmark `<header class="osano-cm-window">` hosting `chicago.com` navigation (`Guides and how-tos · Communities · Partners · News · Donate`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `module-scss-module__oyQcga__profi... { font-size:var(--cdc--font-size--18) }`.
2. **Hero Stage & Focal Lead (<section.osano-visually-hidden> — `Primary Navigation`)**:
   - Landmark `<section class="osano-visually-hidden">` presenting display lead `Primary Navigation` and copy excerpt *"Opens in a new window"* over `#fb2c36` canvas and `#c7d2ff` ink.
3. **Primary Showcase & Content Grid (<section.osano-cm-window__dialog> — `Join the conversation on your bloc`)**:
   - Landmark `<section class="osano-cm-window__dialog">` rendering section `Join the conversation on your block` with copy *"Opens an external website"*, asset references (`1027gyc7pyhue.css`, `3pi19zpjllrvw.css`, `2ffq2uh2507nl.css`, `3uvrwy_t3o4h_.css`), and grid rule `odule__oyQcga__profileCta:focus-v... { outline:2px solid var(--cdc--color--text-primary);outline-offset:2px }`.
4. **Interactive Detail & Feature Matrix (<article.osano-cm-dialog> — `Guides`)**:
   - Landmark `<article class="osano-cm-dialog">` framing `Guides` and `All ages` (*"Opens an external website in a new window"*) with `#f99c00` surface cards, `#00bb7f` accents, and `e-scss-module__oyQcga__profileCta... { background-color:var(--cdc--color--surface-brand);color:var(--cdc--color... }`.
5. **Colophon & Global Directory Footer (<footer.osano-cm-dialog--position_bottom> — `https://chicago.com/`)**:
   - Landmark `<footer class="osano-cm-dialog--position_bottom">` anchoring `chicago.com` footer links (`Guides and how-tos · Communities · Partners · News · Donate`), copy *"<!---->Close this consent banner<!---->"*, and `#a4b3ff` structural dividers.
