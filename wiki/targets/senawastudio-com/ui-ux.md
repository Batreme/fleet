# UI & UX Architecture: senawastudio-com

## Overview & Design Identity
- **Target**: `senawastudio-com` (**Senawa · Architecture & Interior Design Studio in Jakarta**)
- **Production URL**: [https://senawastudio.com](https://senawastudio.com)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#f6f2eb` canvas, `#302620` ink, `#a8967e` accent)
- **Summary**: Architecture made for how people actually live. An architecture, interior, and furniture design studio in the Greater Jakarta area.
- **Total Clean CSS Variables Extracted**: `58` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `Inter Fallback`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--font-display: var(--font-sora), "Sora", var(--font-sans), "Helvetica Neue", sans-serif`
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `10px`, `clamp(1.25rem,1.7vw,1.625rem)`, `12px`, `13px`, `clamp(.9375rem,1vw,1.0625rem)`)
- **Body Copy**: CSS variables `--font-body: var(--font-sans), "Inter", "Helvetica Neue", sans-serif`, `--leading-body: 1.75`; rule `p` (`font-size: clamp(.9375rem,1vw,1.0625rem)`, `line-height: var(--leading-body)`, `font-weight: 300`)
- **Metadata & Labels**: CSS variables `--color-text-caption: var(--slate)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#f6f2eb` | `var(--wool)` in `:root` |
| **Primary Typography Ink** | `#ede6d8` | `var(--linen)` in `:root` |
| **Elevated Surface / Card Substrate** | `#d4c9b4` | `var(--sand)` in `:root` |
| **Interactive Accent / Highlight** | `#a8967e` | `var(--oak)` in `:root` |
| **Secondary / Muted Copy** | `#6b5a48` | `var(--walnut)` in `:root` |
| **Structural Hairline Border** | `#302620` | `var(--slate)` in `:root` |
| **Variable Token (`--s-dim`)** | `#302620b8` | `var(--s-dim)` in `:root` |
| **Variable Token (`--s-line`)** | `#30262024` | `var(--s-line)` in `:root` |
| **Variable Token (`--b-ink-soft`)** | `#302620b3` | `var(--b-ink-soft)` in `:root` |
| **Variable Token (`--b-ink-faint`)** | `#30262057` | `var(--b-ink-faint)` in `:root` |
| **Variable Token (`--b-line-wake`)** | `#30262038` | `var(--b-line-wake)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-sans` | `"Inter", "Inter Fallback"` | Typography / Scale Token |
| `--font-sora` | `"Sora", "Sora Fallback"` | Typography / Scale Token |
| `--s-dim` | `#302620b8` | Color / Atmospheric Token |
| `--s-dim2` | `#302620b8` | Color / Atmospheric Token |
| `--s-line` | `#30262024` | Color / Atmospheric Token |
| `--studio-ink` | `82, 80, 80` | Typography Ink Token |
| `--b-ease` | `var(--ease-out,cubic-bezier(.16, 1, .3, 1))` | Motion / Easing Token |
| `--b-ink` | `var(--slate)` | Typography Ink Token |
| `--b-ink-soft` | `#302620b3` | Typography Ink Token |
| `--b-ink-faint` | `#30262057` | Typography Ink Token |
| `--b-line-wake` | `#30262038` | Color / Atmospheric Token |
| `--b-dot` | `var(--slate)` | Design System Custom Token |
| `--b-t-slow` | `.84s` | Motion / Timing Token |
| `--b-t-mid` | `var(--duration-mid)` | Design System Custom Token |
| `--crop-ease` | `var(--ease-out)` | Motion / Easing Token |
| `--wool` | `#f6f2eb` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.Nav-module__bLoQaq__nav> — `senawastudio-com`)**:
   - Landmark `<nav class="Nav-module__bLoQaq__nav Nav-module__bLoQaq__navHome">` hosting `Senawa · Architecture & Interior Des` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-href="/_next/static/chunks/..."`, `data-active`, `data-hero`), and stylesheet rule `nter_c21b1aaa-module__0pqmKW__cla... { font-family:Inter,Inter Fallback;font-style:normal }`.
2. **Hero Stage & Focal Lead (<section.antialiased> — `Senawa, Architecture & Interior De`)**:
   - Landmark `<section class="antialiased">` presenting display lead `Senawa, Architecture & Interior Design Studio in...` and copy excerpt *"contact.senawastudio@gmail.com"* over `#f6f2eb` canvas and `#302620` ink.
3. **Primary Showcase & Content Grid (<section.skip-link> — `contact.senawastudio@gmail.com`)**:
   - Landmark `<section class="skip-link">` rendering section `contact.senawastudio@gmail.com` with copy *"BSD, Tangerang Selatan"*, asset references (`clarity.js`, `xmr8ny30a5`, `0ha4m18glnjqn.js`, `3r7r9eemmq-97.js`), and grid rule `inter_c21b1aaa-module__0pqmKW__va... { --font-sans:"Inter", "Inter Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.Nav-module__bLoQaq__nav> — `BSD, Tangerang Selatan`)**:
   - Landmark `<section class="Nav-module__bLoQaq__nav">` framing `BSD, Tangerang Selatan` and `→ AA House Bintaro Residential · 2025` (*"→ AA House Bintaro Residential · 2025"*) with `#d4c9b4` surface cards, `#a8967e` accents, and `sora_2a023f4c-module__BGqKYq__cla... { font-family:Sora,Sora Fallback;font-style:normal }`.
5. **Colophon & Global Directory Footer (<footer.Nav-module__bLoQaq__navHome> — `https://senawastudio.com`)**:
   - Landmark `<footer class="Nav-module__bLoQaq__navHome">` anchoring `Senawa · Architecture & Interior` footer links (`Overview · Index · Archive · About · Contact`), copy *"Residential · 2025"*, and `#302620` structural dividers.
