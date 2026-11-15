# UI & UX Architecture: www-worksruthi-com

## Overview & Design Identity
- **Target**: `www-worksruthi-com` (**meet Sruthi. a copywriter, marketer and artist with chutzpah.**)
- **Production URL**: [https://www.worksruthi.com/](https://www.worksruthi.com/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#82181a` / `#e33529`)
- **Summary**: you've built something good and nobody's talking about it yet? i write and design the art that helps capitalists sell their stuff. loudly.
- **Total Clean CSS Variables Extracted**: `117` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Impact`
- **Body Font Stack**: `Bayon`
- **Monospace / Technical Font Stack**: `Courier Prime`
- **Hero Display (`H1`)**: CSS variables `--font-display: "Impact", "Arial Narrow", sans-serif`, `--h1: calc(clamp(72px, calc(28.17px + 11.24vw), 190px) * var(--vp-scale))`
- **Section Heading (`H2`)**: CSS variables `--h2: calc(clamp(62px, calc(28.57px + 8.57vw), 152px) * var(--vp-scale))`
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `12px`, `42px`)
- **Metadata & Labels**: CSS variables `--default-mono-font-family: var(--font-mono)`, `--font-mono: "Geist Mono", "SF Mono", Menlo, monospace`, `--lh-small: 1.14`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#82181a` | `var(--color-red-900)` in `:root` |
| **Primary Typography Ink** | `#f3f3e9` | `var(--spring)` in `:root` |
| **Elevated Surface / Card Substrate** | `#1c1b1a` | `var(--ink)` in `:root` |
| **Interactive Accent / Highlight** | `#e33529` | `var(--cinnabar)` in `:root` |
| **Secondary / Muted Copy** | `#f4ced3` | `var(--cherub)` in `:root` |
| **Structural Hairline Border** | `#afd8fb` | `var(--sail)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--vp-100` | `0px` | Dimension / Scale Token |
| `--color-red-900` | `#82181a` | Brand / Palette Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--ease-in` | `cubic-bezier(.4, 0, 1, 1)` | Motion / Easing Token |
| `--ease-out` | `cubic-bezier(0, 0, .2, 1)` | Motion / Easing Token |
| `--ease-in-out` | `cubic-bezier(.4, 0, .2, 1)` | Motion / Easing Token |
| `--default-transition-duration` | `.15s` | Motion / Easing Token |
| `--default-transition-timing-function` | `cubic-bezier(.4, 0, .2, 1)` | Motion / Easing Token |
| `--default-font-family` | `var(--font-sans)` | Typography / Scale Token |
| `--default-mono-font-family` | `var(--font-mono)` | Typography / Scale Token |
| `--font-display` | `"Impact", "Arial Narrow", sans-serif` | Typography / Scale Token |
| `--font-bayon` | `"Bayon", "Arial Narrow", sans-serif` | Typography / Scale Token |
| `--font-sans` | `"Geist", "Helvetica Neue", Helvetica, Arial, sans-serif` | Typography / Scale Token |
| `--font-mono` | `"Geist Mono", "SF Mono", Menlo, monospace` | Typography / Scale Token |
| `--font-helvetica` | `"Helvetica Neue", Helvetica, Arial, sans-serif` | Typography / Scale Token |
| `--spring` | `#f3f3e9` | Elevation / Border Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.pl-lock> — `www-worksruthi-com`)**:
   - Landmark `<header class="pl-lock">` hosting `meet Sruthi. a copywriter, marketer ` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-sdkn="@vercel/analytics/next"`, `data-sdkv="2.0.1"`), and stylesheet rule `host { --vp-100:0px }`.
2. **Hero Stage & Focal Lead (<section.hero> — `sruthi`)**:
   - Landmark `<section class="hero in">` presenting display lead `sruthi` and copy excerpt *"P L A Y G R O U N D"* over `#82181a` canvas and `#f3f3e9` ink.
3. **Primary Showcase & Content Grid (<section.bq> — `I'M YOUR PERSON TO GET SH*T DONE`)**:
   - Landmark `<section class="bq">` rendering section `I'M YOUR PERSON TO GET SH*T DONE` with copy *"handmade with 🫀 and 🧠 and"*, asset references (`Impact.woff2`, `0_vr5kr4-0c-u.css`, `3y62y2uuds32t.css`, `1mlftcslf095m.js`), and grid rule `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
4. **Interactive Detail & Feature Matrix (<section.sfold> — `work i'm super proud of .`)**:
   - Landmark `<section class="sfold">` framing `work i'm super proud of .` and `before you ask . . .` (*"MY WEBSITE IS NOW ON AWWWARDS??!! VOTE FOR MEEE <3<3<3 MY WEBSITE"*) with `#1c1b1a` surface cards, `#e33529` accents, and `file-selector-button { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://www.worksruthi.com/`)**:
   - Landmark `<footer class="site-footer">` anchoring `meet Sruthi. a copywriter, marke` footer links (`Overview · Index · Archive · About · Contact`), copy *"MY WEBSITE IS NOW ON AWWWARDS??!! VOTE FOR MEEE <3<3<3"*, and `#afd8fb` structural dividers.
