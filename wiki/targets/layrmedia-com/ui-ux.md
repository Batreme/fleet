# UI & UX Architecture: layrmedia-com

## Overview & Design Identity
- **Target**: `layrmedia-com` (**LAYR Media · Creative Photography & Videography Studio**)
- **Production URL**: [https://layrmedia.com/](https://layrmedia.com/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#fb2c36` / `#00c758`)
- **Summary**: A Toronto-based photography and video production studio creating high-quality commercial, brand, corporate and social content from concep...
- **Total Clean CSS Variables Extracted**: `37` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Koulen`
- **Body Font Stack**: `Koulen Fallback`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `.7vw`, `.8vw`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `.7vw`, `.8vw`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `.7vw`, `.8vw`)
- **Metadata & Labels**: CSS variables `--default-mono-font-family: var(--font-mono)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fb2c36` | `var(--color-red-500)` in `:root` |
| **Primary Typography Ink** | `#e40014` | `var(--color-red-600)` in `:root` |
| **Elevated Surface / Card Substrate** | `#461901` | `var(--color-amber-950)` in `:root` |
| **Interactive Accent / Highlight** | `#00c758` | `var(--color-green-500)` in `:root` |
| **Secondary / Muted Copy** | `#171717` | `var(--color-neutral-900)` in `:root` |
| **Structural Hairline Border** | `#0000` | `textarea { background-color: #0000 }` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-koulen` | `"Koulen", "Koulen Fallback"` | Typography / Scale Token |
| `--font-work-sans` | `"Work Sans", "Work Sans Fallback"` | Typography / Scale Token |
| `--color-red-500` | `#fb2c36` | Brand / Palette Token |
| `--color-red-600` | `#e40014` | Brand / Palette Token |
| `--color-amber-950` | `#461901` | Brand / Palette Token |
| `--color-green-500` | `#00c758` | Brand / Palette Token |
| `--color-neutral-900` | `#171717` | Brand / Palette Token |
| `--color-black` | `var(--color-black)` | Canvas / Surface Token |
| `--color-white` | `var(--color-white)` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--font-weight-light` | `300` | Canvas / Surface Token |
| `--font-weight-normal` | `400` | Typography / Scale Token |
| `--font-weight-medium` | `500` | Typography / Scale Token |
| `--font-weight-semibold` | `600` | Typography / Scale Token |
| `--font-weight-bold` | `700` | Typography / Scale Token |
| `--tracking-tighter` | `-.05em` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.relative> — `layrmedia-com`)**:
   - Landmark `<header class="relative w-full">` hosting `LAYR Media · Creative Photography & ` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-precedence="next"`, `data-engine="three.js r184"`, `data-original-fill="F8F7F6"`, `data-original-fill="F8F7F6"`), and stylesheet rule `ulen_aaaf4d07-module__jwNIZW__cla... { font-family:Koulen,Koulen Fallback;font-style:normal;font-weight:400 }`.
2. **Hero Stage & Focal Lead (<section.relative> — `LAYR . MEDIA`)**:
   - Landmark `<section class="relative">` presenting display lead `LAYR . MEDIA` and copy excerpt *"START A PROJECT START A PROJECT"* over `#fb2c36` canvas and `#171717` ink.
3. **Primary Showcase & Content Grid (<section.relative> — `We're LAYR .`)**:
   - Landmark `<section class="relative bg-black">` rendering section `We're LAYR .` with copy *"© 2026 LAYR — Toronto, CA"*, asset references (`6c6a3def8289aaff-s.p.42fhi38wiwr8...`, `7ddd198311ba7843-s.p.3kq6k02b2ysv...`, `1.jpg`, `2.jpg`), and grid rule `oulen_aaaf4d07-module__jwNIZW__va... { --font-koulen:"Koulen", "Koulen Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.group> — `THERE'S MORE WHERE THAT CAME FROM.`)**:
   - Landmark `<section class="group flex">` framing `THERE'S MORE WHERE THAT CAME FROM.` and `testimonial` (*"Creative Production Studio"*) with `#461901` surface cards, `#00c758` accents, and `sans_6c6a0eaa-module__Tqlsvq__cla... { font-family:Work Sans,Work Sans Fallback;font-style:normal }`.
5. **Colophon & Global Directory Footer (<footer.w-full> — `https://layrmedia.com/`)**:
   - Landmark `<footer class="w-full overflow-x-clip">` anchoring `LAYR Media · Creative Photograph` footer links (`Overview · Index · Archive · About · Contact`), copy *"[ Enter without sound ]"*, and `#0000` structural dividers.
