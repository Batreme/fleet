# UI & UX Architecture: www-thelasttango-com

## Overview & Design Identity
- **Target**: `www-thelasttango-com` (**The Last Tango / For the one who made us happy.**)
- **Production URL**: [https://www.thelasttango.com/](https://www.thelasttango.com/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#eff6ff` / `#1447e6`)
- **Summary**: An interactive tribute to Lionel Messi and the World Cup that brought millions of people together again. Every point, every goal, and eve...
- **Total Clean CSS Variables Extracted**: `119` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `DM Sans`
- **Body Font Stack**: `DM Sans Fallback`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5/2.25)`, `--text-6xl: 3.75rem`
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `10px`, `16px`)
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5/1)`
- **Metadata & Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1/.75)`, `--text-sm: .875rem`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#eff6ff` | `var(--color-blue-50)` in `:root` |
| **Primary Typography Ink** | `#3080ff` | `var(--color-blue-500)` in `:root` |
| **Elevated Surface / Card Substrate** | `#155dfc` | `var(--color-blue-600)` in `:root` |
| **Interactive Accent / Highlight** | `#1447e6` | `var(--color-blue-700)` in `:root` |
| **Secondary / Muted Copy** | `#4a5565` | `var(--color-gray-600)` in `:root` |
| **Structural Hairline Border** | `#101828` | `var(--color-gray-900)` in `:root` |
| **Variable Token (`--color-neutral-600`)** | `#525252` | `var(--color-neutral-600)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-dm-sans` | `"DM Sans", "DM Sans Fallback"` | Typography / Scale Token |
| `--font-cormorant-garamond` | `"Cormorant Garamond", "Cormorant Garamond Fallback"` | Typography / Scale Token |
| `--font-darker-grotesque` | `"Darker Grotesque", "Darker Grotesque Fallback"` | Canvas / Surface Token |
| `--ctrl-desktop-max-w` | `1920px` | Layout / Spatial Grid Token |
| `--ctrl-tablet-max-w` | `100vw` | Layout / Spatial Grid Token |
| `--ctrl-mobile-max-w` | `100vw` | Layout / Spatial Grid Token |
| `--ctrl-desktop-max-h` | `100vh` | Dimension / Scale Token |
| `--ctrl-tablet-max-h` | `100vh` | Dimension / Scale Token |
| `--ctrl-mobile-max-h` | `90vh` | Dimension / Scale Token |
| `--color-blue-50` | `#eff6ff` | Brand / Palette Token |
| `--color-blue-500` | `#3080ff` | Brand / Palette Token |
| `--color-blue-600` | `#155dfc` | Brand / Palette Token |
| `--color-blue-700` | `#1447e6` | Brand / Palette Token |
| `--color-gray-600` | `#4a5565` | Brand / Palette Token |
| `--color-gray-900` | `#101828` | Brand / Palette Token |
| `--color-neutral-600` | `#525252` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.fixed> — `www-thelasttango-com`)**:
   - Landmark `<header class="fixed z-100000">` hosting `The Last Tango / For the one who mad` navigation (`Esp`), DOM attributes (`data-loader-scroll-lock="true"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `html.lenis body { height:auto }`.
2. **Hero Stage & Focal Lead (<main.lenis> — `The Last Tango / For the one who m`)**:
   - Landmark `<main class="lenis">` presenting display lead `The Last Tango / For the one who made us happy.` and copy excerpt *"Lionel Andrés Messi"* over `#eff6ff` canvas and `#101828` ink.
3. **Primary Showcase & Content Grid (<main.lenis-stopped> — `Featured Work & Interactive Showca`)**:
   - Landmark `<main class="lenis-stopped">` rendering section `Featured Work & Interactive Showcase` with copy *"Pride of Argentina"*, asset references (`187cmj4q350mm.css`, `0eqspdm2dt5_-.css`, `0kkv0xwvqoa86.css`, `14~g0x6k9zzx2.js`), and grid rule `.lenis-stopped { overflow:clip }`.
4. **Interactive Detail & Feature Matrix (<main.fonts-loaded> — `Technical Architecture & Narrative`)**:
   - Landmark `<main class="fonts-loaded">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"Millions of points come together to shape a tribute for"*) with `#155dfc` surface cards, `#1447e6` accents, and `.lenis.lenis-smooth iframe { pointer-events:none }`.
5. **Colophon & Global Directory Footer (<footer.pointer-events-auto> — `https://www.thelasttango.com/`)**:
   - Landmark `<footer class="pointer-events-auto">` anchoring `The Last Tango / For the one who` footer links (`Esp`), copy *"the one who made millions happy. A tribute to every"*, and `#101828` structural dividers.
