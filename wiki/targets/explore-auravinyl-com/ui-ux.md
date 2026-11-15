# UI & UX Architecture: explore-auravinyl-com

## Overview & Design Identity
- **Target**: `explore-auravinyl-com` (**Aura Vinyl Color Explorer**)
- **Production URL**: [https://explore.auravinyl.com](https://explore.auravinyl.com)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#0a0a0a` / `#1e1e1e`)
- **Summary**: Explore over 500 colors across matte, satin, and gloss finishes from Aura Premium Vinyl. Find vinyl wrap ideas and inspiration.
- **Total Clean CSS Variables Extracted**: `59` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Archivo`
- **Body Font Stack**: `Geist Mono`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **Hero Display (`H1`)**: rule `.title` (`font-size: 18px`, `line-height: 1.1`, `letter-spacing: -.02em`, `font-weight: 800`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `13px`, `18px`, `12px`, `10px`, `16px`)
- **Body Copy**: rule `.body` (`font-size: 13px`, `line-height: 1.5`, `font-weight: 500`)
- **Metadata & Labels**: CSS variables `--font-mono: "Geist Mono", ui-monospace, monospace`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#0a0a0a` | `var(--bg)` in `:root` |
| **Primary Typography Ink** | `#161616` | `var(--bg-raised)` in `:root` |
| **Elevated Surface / Card Substrate** | `#050505` | `var(--bg-sunken)` in `:root` |
| **Interactive Accent / Highlight** | `#1e1e1e` | `var(--raised)` in `:root` |
| **Secondary / Muted Copy** | `#262626` | `var(--line)` in `:root` |
| **Structural Hairline Border** | `#404040` | `var(--line-steel)` in `:root` |
| **Variable Token (`--line-strong`)** | `#6b6b6b` | `var(--line-strong)` in `:root` |
| **Variable Token (`--text`)** | `#f5f5f5` | `var(--text)` in `:root` |
| **Variable Token (`--text-2`)** | `#a3a3a3` | `var(--text-2)` in `:root` |
| **Variable Token (`--text-3`)** | `#808080` | `var(--text-3)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--enter-at` | `1100ms` | Motion / Timing Token |
| `--enter-from` | `48px 0` | Dimension / Scale Token |
| `--enter-order` | `1` | Design System Custom Token |
| `--ease-pull` | `cubic-bezier(.215, .61, .355, 1)` | Motion / Easing Token |
| `--ease-pull-back` | `cubic-bezier(.645, .045, .355, 1)` | Motion / Easing Token |
| `--under` | `0px` | Dimension / Scale Token |
| `--bg` | `#0a0a0a` | Canvas / Surface Token |
| `--bg-raised` | `#161616` | Canvas / Surface Token |
| `--bg-sunken` | `#050505` | Canvas / Surface Token |
| `--raised` | `#1e1e1e` | Color / Atmospheric Token |
| `--line` | `#262626` | Color / Atmospheric Token |
| `--line-steel` | `#404040` | Color / Atmospheric Token |
| `--line-strong` | `#6b6b6b` | Color / Atmospheric Token |
| `--text` | `#f5f5f5` | Typography Ink Token |
| `--text-2` | `#a3a3a3` | Typography Ink Token |
| `--text-3` | `#808080` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.head> — `explore-auravinyl-com`)**:
   - Landmark `<header class="head">` hosting `Aura Vinyl Color Explorer` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-perma="ultra-gloss-laguna-blue"`, `data-perma="ultra-gloss-white-pri..."`, `data-perma="ultra-gloss-laguna-blue"`), and stylesheet rule `.FormDialog.on { visibility:visible;opacity:1;pointer-events:auto;transition:opacity var(... }`.
2. **Hero Stage & Focal Lead (<section.mbar> — `Arctic Fire`)**:
   - Landmark `<section class="mbar">` presenting display lead `Arctic Fire` and copy excerpt *"Please enable javascript"* over `#0a0a0a` canvas and `#404040` ink.
3. **Primary Showcase & Content Grid (<section.card> — `No color`)**:
   - Landmark `<section class="card">` rendering section `No color` with copy *"Paint Metallic 190"*, asset references (`favicon.svg`, `180.png`, `152.png`, `167.png`), and grid rule `.FormDialog { padding:10px }`.
4. **Interactive Detail & Feature Matrix (<section.sec> — `Reference`)**:
   - Landmark `<section class="sec">` framing `Reference` and `Material` (*"White Prismatic Chrome"*) with `#050505` surface cards, `#1e1e1e` accents, and `.FormDialog .backdrop { position:absolute;inset:0;background:rgba(5,5,5,.8) }`.
5. **Colophon & Global Directory Footer (<footer.shell> — `https://explore.auravinyl.com`)**:
   - Landmark `<footer class="shell">` anchoring `Aura Vinyl Color Explorer` footer links (`Overview · Index · Archive · About · Contact`), copy *"Ultra Gloss / Chrome"*, and `#404040` structural dividers.
