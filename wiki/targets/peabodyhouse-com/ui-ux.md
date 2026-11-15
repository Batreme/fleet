# UI & UX Architecture: peabodyhouse-com

## Overview & Design Identity
- **Target**: `peabodyhouse-com` (**Peabody House • Digital Brand World Implementation Studio**)
- **Production URL**: [https://peabodyhouse.com](https://peabodyhouse.com)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#26211E` / `#517BB3`)
- **Summary**: Peabody House is a Milwaukee-based digital studio that turns brand aspirations into elevated, scalable design systems. Led by human expre...
- **Total Clean CSS Variables Extracted**: `53` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Peabody House`
- **Body Font Stack**: `DSEG7 Classic`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1rem`, `.6875rem`, `.8125rem`, `.75rem`, `.875rem`)
- **Section Heading (`H2`)**: rule `,.h2` (`font-size: clamp(2.0257rem,1.4626rem + 2...`, `line-height: 1.125`)
- **Body Copy**: CSS variables `--font-body: "PP Neue Montreal", sans-serif`, `--font-size-base: 16px`
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1rem`, `.6875rem`, `.8125rem`, `.75rem`, `.875rem`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#26211E` | `var(--color-primary)` in `:root` |
| **Primary Typography Ink** | `#FAF6F3` | `var(--color-secondary)` in `:root` |
| **Elevated Surface / Card Substrate** | `#DC942F` | `var(--color-accent)` in `:root` |
| **Interactive Accent / Highlight** | `#517BB3` | `var(--color-blue)` in `:root` |
| **Secondary / Muted Copy** | `#71C7B7` | `var(--color-teal)` in `:root` |
| **Structural Hairline Border** | `#A24250` | `var(--color-red)` in `:root` |
| **Variable Token (`--color-green`)** | `#455330` | `var(--color-green)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-primary` | `#26211E` | Brand / Palette Token |
| `--color-secondary` | `#FAF6F3` | Brand / Palette Token |
| `--color-accent` | `#DC942F` | Brand / Palette Token |
| `--color-background` | `#FAF6F3` | Canvas / Surface Token |
| `--color-text` | `#26211E` | Typography Ink Token |
| `--color-white` | `#FAF6F3` | Canvas / Surface Token |
| `--color-black` | `#26211E` | Canvas / Surface Token |
| `--color-black-20` | `rgba(38, 33, 30, .2)` | Canvas / Surface Token |
| `--color-orange` | `#DC942F` | Brand / Palette Token |
| `--color-blue` | `#517BB3` | Brand / Palette Token |
| `--color-teal` | `#71C7B7` | Brand / Palette Token |
| `--color-red` | `#A24250` | Brand / Palette Token |
| `--color-green` | `#455330` | Brand / Palette Token |
| `--font-heading` | `"Peabody House", sans-serif` | Typography Ink Token |
| `--font-body` | `"PP Neue Montreal", sans-serif` | Typography / Scale Token |
| `--font-size-base` | `16px` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.svelte-126o6dr> — `peabodyhouse-com`)**:
   - Landmark `<header class="svelte-126o6dr">` hosting `Peabody House • Digital Brand World ` navigation (`Expertise Expertise · Works Works · Studio Studio · Contact Contact · Expertise`), DOM attributes (`data-sveltekit-preload-data="hover"`, `data-text="Peabody House"`, `data-text="Expertise"`, `data-text="Works"`), and stylesheet rule `.search.svelte-1w6by2l { position:relative;display:inline-flex;align-items:center }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Peabody House is a digital brand w`)**:
   - Landmark `<section class="hero svelte-x35jl1">` presenting display lead `Peabody House is a digital brand world implementa...` and copy excerpt *"Peabody House Peabody House"* over `#26211E` canvas and `#FAF6F3` ink.
3. **Primary Showcase & Content Grid (<section.subhero> — `The ordeal of being perceived.`)**:
   - Landmark `<section class="subhero svelte-x35jl1">` rendering section `The ordeal of being perceived.` with copy *"Expertise Expertise"*, asset references (`favicon.ico`, `favicon.svg`, `apple-touch-icon.png`, `site.webmanifest`), and grid rule `.search-panel.is-open.svelte-1w6by2l { opacity:1;visibility:visible;pointer-events:auto;transform:none }`.
4. **Interactive Detail & Feature Matrix (<section.grid> — `What does Peabody House do?`)**:
   - Landmark `<section class="grid service-cards">` framing `What does Peabody House do?` and `Technical Implementation` (*"Type to search the site."*) with `#DC942F` surface cards, `#517BB3` accents, and `arch-panel.is-positioned.svelte-1... { position:fixed;top:var(--panel-y);left:var(--panel-x);right:auto }`.
5. **Colophon & Global Directory Footer (<footer.grid> — `https://peabodyhouse.com`)**:
   - Landmark `<footer class="grid js-line-displacement">` anchoring `Peabody House • Digital Brand Wo` footer links (`Expertise Expertise · Works Works · Studio Studio · Contact Contact · Expertise`), copy *"hello@peabodyhouse.com copied to clipboard."*, and `#A24250` structural dividers.
