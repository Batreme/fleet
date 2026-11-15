# UI & UX Architecture: www-hauntedbouldercity-com

## Overview & Design Identity
- **Target**: `www-hauntedbouldercity-com` (**Boulder City Ghost & UFO Walking Tour · Haunted Boulder City**)
- **Production URL**: [https://www.hauntedbouldercity.com/](https://www.hauntedbouldercity.com/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#090f0e` canvas, `#e7e9d8` ink, `#a7b3a7` accent)
- **Summary**: Meet the stranger side of Boulder City. Discover local ghost stories, desert mysteries and UFO folklore on a one-hour walking tour with B...
- **Total Clean CSS Variables Extracted**: `20` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Display`
- **Body Font Stack**: `Manticore`
- **Monospace / Technical Font Stack**: `SpaceMono`
- **Hero Display (`H1`)**: CSS variables `--display: Display,Impact,'Arial Narrow',sans-serif`; rule `h1` (`line-height: .92`, `font-weight: 400`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(58px,8.7vw,162px)`, `line-height: 1.02`, `letter-spacing: -.01em`)
- **Body Copy**: rule `p` (`font-size: 18px`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `clamp(16px,1.35vw,20px)`, `12px`, `30px`, `15px`, `16px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#090f0e` | `var(--ink)` in `:root` |
| **Primary Typography Ink** | `#b9cbb7` | `var(--accent)` in `:root` |
| **Elevated Surface / Card Substrate** | `#e7e9d8` | `var(--paper)` in `:root` |
| **Interactive Accent / Highlight** | `#a7b3a7` | `var(--muted)` in `:root` |
| **Secondary / Muted Copy** | `#35463d` | `var(--line)` in `:root` |
| **Structural Hairline Border** | `#d9b47b` | `var(--amber)` in `:root` |
| **Variable Token (`--mist`)** | `#c4d1c0` | `var(--mist)` in `:root` |
| **Variable Token (`--surface`)** | `#192a23` | `var(--surface)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ink` | `#090f0e` | Typography Ink Token |
| `--accent` | `#b9cbb7` | Brand / Palette Token |
| `--paper` | `#e7e9d8` | Canvas / Surface Token |
| `--muted` | `#a7b3a7` | Color / Atmospheric Token |
| `--line` | `#35463d` | Color / Atmospheric Token |
| `--amber` | `#d9b47b` | Color / Atmospheric Token |
| `--mist` | `#c4d1c0` | Color / Atmospheric Token |
| `--surface` | `#192a23` | Canvas / Surface Token |
| `--pad` | `clamp(24px,4.6vw,88px)` | Layout / Spatial Grid Token |
| `--display` | `Display,Impact,'Arial Narrow',sans-serif` | Design System Custom Token |
| `--logo-width` | `136px` | Layout / Spatial Grid Token |
| `--dir` | `1` | Design System Custom Token |
| `--spirit-duration` | `2800ms` | Motion / Easing Token |
| `--spirit-peak` | `.9` | Design System Custom Token |
| `--spirit-linger` | `14vh` | Dimension / Scale Token |
| `--spirit-side` | `0px` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `www-hauntedbouldercity-com`)**:
   - Landmark `<header class="site-header">` hosting `Boulder City Ghost & UFO Walking Tou` navigation (`Get tickets · Directions`), DOM attributes (`data-src="/assets/ufo-night.mp4"`, `data-src-small="/assets/ufo-night-960..."`, `data-story="0"`, `data-story="1"`), and stylesheet rule `html { scroll-behavior:smooth;scroll-padding-top:88px }`.
2. **Hero Stage & Focal Lead (<section.hero> — `HAUNTED BOULDER CITY`)**:
   - Landmark `<section class="hero">` presenting display lead `HAUNTED BOULDER CITY` and copy excerpt *"Gathering the mist"* over `#090f0e` canvas and `#e7e9d8` ink.
3. **Primary Showcase & Content Grid (<section.intro> — `NICE LITTLE TOWN. STRANGE LITTLE S`)**:
   - Landmark `<section class="intro section-pad">` rendering section `NICE LITTLE TOWN. STRANGE LITTLE SECRETS.` with copy *"01 The tour One hour on foot, full of stories"*, asset references (`fog.webp`, `manticore.woff2`, `display.ttf`, `favicon-32.png`), and grid rule `selection { background:var(--accent);color:var(--ink) }`.
4. **Interactive Detail & Feature Matrix (<section.stories-scroll> — `NOT EVERY LOCAL IS LIVING.`)**:
   - Landmark `<section class="stories-scroll">` framing `NOT EVERY LOCAL IS LIVING.` and `THE PAST DOESN’T STAY BURIED.` (*"One hour on foot, full of stories"*) with `#e7e9d8` surface cards, `#a7b3a7` accents, and `button { font:inherit;cursor:pointer }`.
5. **Colophon & Global Directory Footer (<footer.loader-veil> — `https://www.hauntedbouldercity.com/`)**:
   - Landmark `<footer class="loader-veil">` anchoring `Boulder City Ghost & UFO Walking` footer links (`Get tickets · Directions`), copy *"02 The strange stuff Ghosts, dark history & UFOs"*, and `#d9b47b` structural dividers.
