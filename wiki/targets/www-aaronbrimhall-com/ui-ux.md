# UI & UX Architecture: www-aaronbrimhall-com

## Overview & Design Identity
- **Target**: `www-aaronbrimhall-com` (**Aaron Brimhall · Action & Automotive Photographer**)
- **Production URL**: [https://www.aaronbrimhall.com/](https://www.aaronbrimhall.com/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#101010` / `#000`)
- **Summary**: Action and automotive photography by Aaron Brimhall: dynamic compositions, high-octane shoots and globe-trotting adventures. Fun fuels cr...
- **Total Clean CSS Variables Extracted**: `26` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter Variablefont Opsz Wght`
- **Body Font Stack**: `IBM Plex Mono`
- **Monospace / Technical Font Stack**: `IBM Plex Mono`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `2em`, `80%`, `75%`, `1em`, `14px`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `2em`, `80%`, `75%`, `1em`, `14px`)
- **Body Copy**: rule `.paragraph` (`letter-spacing: .01em`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `2em`, `80%`, `75%`, `1em`, `14px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#101010` | `var(--black)` in `:root` |
| **Primary Typography Ink** | `#fe019a` | `var(--pink)` in `:root` |
| **Elevated Surface / Card Substrate** | `#0000` | `a { background-color: #0000 }` |
| **Interactive Accent / Highlight** | `#000` | `mark { color: #000 }` |
| **Secondary / Muted Copy** | `#ff0` | `mark { background: #ff0 }` |
| **Structural Hairline Border** | `#333` | `body { color: #333 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--w-backdrop-animation` | `initial` | Motion / Easing Token |
| `--black` | `#101010` | Canvas / Surface Token |
| `--pink` | `#fe019a` | Typography Ink Token |
| `--font-family` | `"IBM Plex Mono",sans-serif` | Typography / Scale Token |
| `--ab-ldx-aw` | `max(96px,min(clamp(140px,44vw,210px),35.16dvh))` | Dimension / Scale Token |
| `--ab-pink` | `#fe019a` | Typography Ink Token |
| `--ab-black` | `#101010` | Canvas / Surface Token |
| `--ab-ease-osmo` | `cubic-bezier(0.625, 0.05, 0, 1)` | Motion / Easing Token |
| `--ab-ease-out` | `cubic-bezier(0.19, 1, 0.22, 1)` | Motion / Easing Token |
| `--tr-cover` | `#101010` | Color / Atmospheric Token |
| `--ab-edge` | `24px` | Dimension / Scale Token |
| `--ab-nav-ride` | `0.45s cubic-bezier(0.19, 1, 0.22, 1)` | Layout / Spatial Grid Token |
| `--hs-e` | `var(--ab-edge,24px)` | Dimension / Scale Token |
| `--hs-trim` | `4px` | Dimension / Scale Token |
| `--vf-i` | `clamp(24px,4vw,64px)` | Dimension / Scale Token |
| `--vf-t` | `max(var(--vf-i),60px)` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.ab-cs-socials> — `www-aaronbrimhall-com`)**:
   - Landmark `<nav class="ab-cs-socials">` hosting `Aaron Brimhall · Action & Automotive` navigation (`INSTAGRAM ↗ · TIKTOK ↗ · BEHANCE ↗ · YOUTUBE ↗`), DOM attributes (`data-wf-domain="www.aaronbrimhall.com"`, `data-wf-page="6941d6f273b44a2836ceae0d"`, `data-wf-site="6941d6f273b44a2836ceae16"`, `data-page="home"`), and stylesheet rule `html { -webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;font-family:sans... }`.
2. **Hero Stage & Focal Lead (<section.hero_section> — `TELL ME ABOUT THE PROJECT`)**:
   - Landmark `<section class="hero_section ab-hx-short">` presenting display lead `TELL ME ABOUT THE PROJECT` and copy excerpt *"TRANSMISSION RECEIVED"* over `#101010` canvas and `#ff0` ink.
3. **Primary Showcase & Content Grid (<section.hero-section_wrapper> — `T H O S E W H O G E T I T`)**:
   - Landmark `<section class="hero-section_wrapper">` rendering section `T H O S E W H O G E T I T` with copy *"SIGNAL LOST — TRY AGAIN"*, asset references (`cdn.prod.website-files.com`, `aaron-brimhall-site-09-25-f01e7c4...`, `fonts.googleapis.com`, `fonts.gstatic.com`), and grid rule `summary { display:block }`.
4. **Interactive Detail & Feature Matrix (<section.gallery_section> — `AB Training`)**:
   - Landmark `<section class="gallery_section">` framing `AB Training` and `Shop Prints` (*"I M A G E G E N E R A T O R →"*) with `#0000` surface cards, `#000` accents, and `video { vertical-align:baseline;display:inline-block }`.
5. **Colophon & Global Directory Footer (<footer.wf-ibmplexmono-n6-active> — `https://www.aaronbrimhall.com/`)**:
   - Landmark `<footer class="wf-ibmplexmono-n6-active">` anchoring `Aaron Brimhall · Action & Automo` footer links (`INSTAGRAM ↗ · TIKTOK ↗ · BEHANCE ↗ · YOUTUBE ↗`), copy *"I M A G E G E N E R A T O R"*, and `#333` structural dividers.
