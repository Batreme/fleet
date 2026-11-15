# UI & UX Architecture: karma-tracks-com

## Overview & Design Identity
- **Target**: `karma-tracks-com` (**karma tracks**)
- **Production URL**: [https://karma-tracks.com/](https://karma-tracks.com/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffcaca` / `#fb2c36`)
- **Summary**: the tracks of one music producer from the last ten years, every one of them drawn as a card.
- **Total Clean CSS Variables Extracted**: `77` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Gloock`
- **Body Font Stack**: `Gloock Fallback`
- **Monospace / Technical Font Stack**: `Space Mono`
- **Hero Display (`H1`)**: CSS variables `--font-display: var(--font-gloock), Georgia, serif`
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`
- **Metadata & Labels**: CSS variables `--font-space-mono: "Space Mono", "Space Mono Fallback"`, `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#ffcaca` | `var(--color-red-200)` in `:root` |
| **Primary Typography Ink** | `#ffa3a3` | `var(--color-red-300)` in `:root` |
| **Elevated Surface / Card Substrate** | `#ff6568` | `var(--color-red-400)` in `:root` |
| **Interactive Accent / Highlight** | `#fb2c36` | `var(--color-red-500)` in `:root` |
| **Secondary / Muted Copy** | `#fee685` | `var(--color-amber-200)` in `:root` |
| **Structural Hairline Border** | `#ffd236` | `var(--color-amber-300)` in `:root` |
| **Variable Token (`--color-amber-400`)** | `#fcbb00` | `var(--color-amber-400)` in `:root` |
| **Variable Token (`--color-amber-500`)** | `#f99c00` | `var(--color-amber-500)` in `:root` |
| **Variable Token (`--color-green-200`)** | `#b9f8cf` | `var(--color-green-200)` in `:root` |
| **Variable Token (`--color-green-500`)** | `#00c758` | `var(--color-green-500)` in `:root` |
| **Variable Token (`--color-emerald-200`)** | `#a4f4cf` | `var(--color-emerald-200)` in `:root` |
| **Variable Token (`--color-emerald-400`)** | `#00d294` | `var(--color-emerald-400)` in `:root` |
| **Variable Token (`--color-emerald-500`)** | `#00bb7f` | `var(--color-emerald-500)` in `:root` |
| **Variable Token (`--color-sky-200`)** | `#b8e6fe` | `var(--color-sky-200)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-gloock` | `"Gloock", "Gloock Fallback"` | Typography / Scale Token |
| `--font-space-mono` | `"Space Mono", "Space Mono Fallback"` | Typography / Scale Token |
| `--color-red-200` | `#ffcaca` | Brand / Palette Token |
| `--color-red-300` | `#ffa3a3` | Brand / Palette Token |
| `--color-red-400` | `#ff6568` | Brand / Palette Token |
| `--color-red-500` | `#fb2c36` | Brand / Palette Token |
| `--color-amber-200` | `#fee685` | Brand / Palette Token |
| `--color-amber-300` | `#ffd236` | Brand / Palette Token |
| `--color-amber-400` | `#fcbb00` | Brand / Palette Token |
| `--color-amber-500` | `#f99c00` | Brand / Palette Token |
| `--color-green-200` | `#b9f8cf` | Brand / Palette Token |
| `--color-green-500` | `#00c758` | Brand / Palette Token |
| `--color-emerald-200` | `#a4f4cf` | Brand / Palette Token |
| `--color-emerald-400` | `#00d294` | Brand / Palette Token |
| `--color-emerald-500` | `#00bb7f` | Brand / Palette Token |
| `--color-sky-200` | `#b8e6fe` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.h-full> — `karma-tracks-com`)**:
   - Landmark `<header class="h-full">` hosting `karma tracks` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-engine="three.js r184"`, `data-lenis-prevent="true"`, `data-inspect-panel="true"`), and stylesheet rule `oock_a2ed214b-module__p916ta__cla... { font-family:Gloock,Gloock Fallback;font-style:normal;font-weight:400 }`.
2. **Hero Stage & Focal Lead (<section.antialiased> — `karma tracks`)**:
   - Landmark `<section class="antialiased">` presenting display lead `karma tracks` and copy excerpt *"these are my tracks from the last ten years. every one of them is"* over `#ffcaca` canvas and `#fb2c36` ink.
3. **Primary Showcase & Content Grid (<section.lenis> — `Featured Work & Interactive Showca`)**:
   - Landmark `<section class="lenis">` rendering section `Featured Work & Interactive Showcase` with copy *"by conversation telegram instagram"*, asset references (`8d05cfa5faa8406c-s.p.0kbulo~7o8gi...`, `c5bca4b73401f535-s.p.0ld0~zebno3h...`, `dc0d9adbac686440-s.p.0~z396rbj0t4...`, `16_jj7v3ye6b5.css`), and grid rule `loock_a2ed214b-module__p916ta__va... { --font-gloock:"Gloock", "Gloock Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.has-rail> — `Technical Architecture & Narrative`)**:
   - Landmark `<section class="has-rail">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"telegram instagram"*) with `#ff6568` surface cards, `#fb2c36` accents, and `mono_754f223c-module__vnF5cq__cla... { font-family:Space Mono,Space Mono Fallback;font-style:normal }`.
5. **Colophon & Global Directory Footer (<footer.has-custom-cursor> — `https://karma-tracks.com/`)**:
   - Landmark `<footer class="has-custom-cursor">` anchoring `karma tracks` footer links (`Overview · Index · Archive · About · Contact`), copy *"browse all 166 tracks"*, and `#ffd236` structural dividers.
