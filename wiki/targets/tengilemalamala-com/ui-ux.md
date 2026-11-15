# UI & UX Architecture: tengilemalamala-com

## Overview & Design Identity
- **Target**: `tengilemalamala-com` (**Luxury Safari Experiences in Greater Kruger & Sabi Sand · Tengile MalaMa...**)
- **Production URL**: [https://tengilemalamala.com/](https://tengilemalamala.com/)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#fbf8f6` canvas, `#48561a` ink, `#a5a593` accent)
- **Summary**: Discover luxury safari experiences in Greater Kruger and Sabi Sand. Wildlife, luxury accommodation and unforgettable Big Five encounters....
- **Total Clean CSS Variables Extracted**: `5` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `PP Fragment`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(3rem,12.5vw,5.2rem)`, `16px`, `12rem`, `16rem`, `11px`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(3rem,12.5vw,5.2rem)`, `16px`, `12rem`, `16rem`, `11px`)
- **Body Copy**: rule `p` (`letter-spacing: -.01em`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(3rem,12.5vw,5.2rem)`, `16px`, `12rem`, `16rem`, `11px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fbf8f6` | `eBanner-module-scss-module__3-R... { background-color: #fbf8f6 }` |
| **Primary Typography Ink** | `#5c6e21` | `css-module__3-RGkq__cookie a:fo... { color: #5c6e21 }` |
| **Elevated Surface / Card Substrate** | `#e3e1d4` | `Banner-module-scss-module__3-RG... { border-top: #e3e1d4 }` |
| **Interactive Accent / Highlight** | `#a5a593` | `module-scss-module__3-RGkq__set... { color: #a5a593 }` |
| **Secondary / Muted Copy** | `#f5eee9` | `:focus-visible { color: #f5eee9 }` |
| **Structural Hairline Border** | `#48561a` | `:focus-visible { background-color: #48561a }` |
| **Variable Token (`--plyr-video-progress-buffered-background`)** | `#fbf8f61a` | `var(--plyr-video-progress-buffered-background)` in stylesheet |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--offset` | `150dvw` | Dimension / Scale Token |
| `--lvh` | `1vh` | Layout / Spatial Grid Token |
| `--svh` | `1vh` | Layout / Spatial Grid Token |
| `--size` | `1440` | Layout / Spatial Grid Token |
| `--duration` | `120s` | Motion / Easing Token |
| `--plyr-color-main` | `#fbf8f6` | Brand / Palette Token |
| `--plyr-video-control-color` | `#fbf8f6` | Brand / Palette Token |
| `--plyr-font-size-small` | `14px` | Typography / Scale Token |
| `--plyr-range-track-height` | `2px` | Layout / Spatial Grid Token |
| `--plyr-range-thumb-height` | `0px` | Layout / Spatial Grid Token |
| `--plyr-video-progress-buffered-background` | `#fbf8f61a` | Canvas / Surface Token |
| `--tengilemalamala--bg` | `#fbf8f6` | Canvas Substrate (from `eBanner-module-scss-module__3-R... { background-color: #fbf8f6 }`) |
| `--tengilemalamala--ink` | `#48561a` | Primary Typography Ink (stylesheet-derived) |
| `--tengilemalamala--surface` | `#e3e1d4` | Surface Substrate (stylesheet-derived) |
| `--tengilemalamala--accent` | `#a5a593` | Interactive Accent (stylesheet-derived) |
| `--tengilemalamala--muted` | `#f5eee9` | Secondary Ink (stylesheet-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `tengilemalamala-com`)**:
   - Landmark `<header class="site-header">` hosting `Luxury Safari Experiences in Greater` navigation (`About · Accommodation · Experiences · Conservation · Partner Hub`), DOM attributes (`data-next-head`, `data-nscript="beforeInteractive"`, `data-n-g`, `data-n-css`), and stylesheet rule `nner-module-scss-module__3-RGkq__... { width:auto;right:1.6rem }`.
2. **Hero Stage & Focal Lead (<section.lenis-stopped> — `Khensani River Lodge`)**:
   - Landmark `<section class="lenis-stopped">` presenting display lead `Khensani River Lodge` and copy excerpt *"Skip to main content"* over `#fbf8f6` canvas and `#48561a` ink.
3. **Primary Showcase & Content Grid (<section.site-header> — `Tengile River Lodge`)**:
   - Landmark `<section class="site-header">` rendering section `Tengile River Lodge` with copy *"Khensani River Lodge"*, asset references (`icon-32.png`, `icon-16.png`, `inter-regular.woff2`, `inter-medium.woff2`), and grid rule `er-module-scss-module__3-RGkq__co... { text-decoration:underline;transition:color .3s }`.
4. **Interactive Detail & Feature Matrix (<section.no-lenis> — `Rattray's Lodge`)**:
   - Landmark `<section class="no-lenis">` framing `Rattray's Lodge` and `MalaMala Camp` (*"Tengile River Lodge"*) with `#e3e1d4` surface cards, `#a5a593` accents, and `module__3-RGkq__cookie a:focus-vi... { color:5c6e21 }`.
5. **Colophon & Global Directory Footer (<footer.action-card-click-label> — `https://tengilemalamala.com/`)**:
   - Landmark `<footer class="action-card-click-label">` anchoring `Luxury Safari Experiences in Gre` footer links (`About · Accommodation · Experiences · Conservation · Partner Hub`), copy *"U N M A T C H E D A B U N D A N C E"*, and `#48561a` structural dividers.
