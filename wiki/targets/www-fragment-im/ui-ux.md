# UI & UX Architecture: www-fragment-im

## Overview & Design Identity
- **Target**: `www-fragment-im` (**Fragment Studio · Independent Designer for Visual Identity, Websites & P...**)
- **Production URL**: [https://www.fragment.im](https://www.fragment.im)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#c9d0d2` canvas, `#000` ink, `#fff` accent)
- **Summary**: Independent multidisciplinary designer creating visual identities, websites and digital product experiences, from creative direction thro...
- **Total Clean CSS Variables Extracted**: `35` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `FragmentNoticeHeadline`
- **Body Font Stack**: `FragmentNoticeText`
- **Monospace / Technical Font Stack**: `Fragment Mono`
- **Hero Display (`H1`)**: rule `h1` (`font-size: 44px`, `line-height: 1.1`, `letter-spacing: 0`, `font-weight: 200`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `44px`, `20px`, `28px`, `16px`, `32px`)
- **Body Copy**: rule `p` (`font-size: 20px`, `line-height: 1.6`, `font-weight: 300`)
- **Metadata & Labels**: CSS variables `--letter-spacing: var(--framer-letter-spacing)`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#c9d0d2` | `var(--token-25c6a125-c456-4a8b-ab9f-41881ab19959)` in `:root` |
| **Primary Typography Ink** | `#000` | `var(--token-89b67f64-c980-4093-a59b-826aca646ff7)` in `:root` |
| **Elevated Surface / Card Substrate** | `#8d9496` | `var(--token-fe4a4709-d130-45cb-b56c-f30ed01b9abe)` in `:root` |
| **Interactive Accent / Highlight** | `#fff` | `var(--token-a95c7b0f-3d02-4bfd-a1a4-044fa7647703)` in `:root` |
| **Secondary / Muted Copy** | `#121516` | `var(--token-d3018533-ccc9-45bc-9cdd-b1ac632fea09)` in `:root` |
| **Structural Hairline Border** | `#687679` | `var(--token-095b07f5-0eeb-4dec-b4e4-b400a5a02e21)` in `:root` |
| **Variable Token (`--token-f73340a2-29c6-4e1e-9122-76db6b3c3c9b`)** | `#c9d0d252` | `var(--token-f73340a2-29c6-4e1e-9122-76db6b3c3c9b)` in `:root` |
| **Variable Token (`--token-7114c3e6-2498-4350-a884-eb0ae0ab8a2a`)** | `#14151529` | `var(--token-7114c3e6-2498-4350-a884-eb0ae0ab8a2a)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--token-25c6a125-c456-4a8b-ab9f-41881ab19959` | `#c9d0d2` | Color / Atmospheric Token |
| `--token-89b67f64-c980-4093-a59b-826aca646ff7` | `#000` | Color / Atmospheric Token |
| `--token-f73340a2-29c6-4e1e-9122-76db6b3c3c9b` | `#c9d0d252` | Color / Atmospheric Token |
| `--token-fe4a4709-d130-45cb-b56c-f30ed01b9abe` | `#8d9496` | Color / Atmospheric Token |
| `--token-a95c7b0f-3d02-4bfd-a1a4-044fa7647703` | `#fff` | Color / Atmospheric Token |
| `--token-d3018533-ccc9-45bc-9cdd-b1ac632fea09` | `#121516` | Color / Atmospheric Token |
| `--token-7114c3e6-2498-4350-a884-eb0ae0ab8a2a` | `#14151529` | Color / Atmospheric Token |
| `--token-095b07f5-0eeb-4dec-b4e4-b400a5a02e21` | `#687679` | Color / Atmospheric Token |
| `--text-decoration-skip-ink` | `var(--framer-text-decoration-skip-ink)` | Typography Ink Token |
| `--text-underline-offset` | `var(--framer-text-decoration-offset)` | Typography Ink Token |
| `--font-family` | `var(--framer-font-family)` | Typography / Scale Token |
| `--font-style` | `var(--framer-font-style)` | Typography / Scale Token |
| `--font-weight` | `var(--framer-font-weight)` | Typography / Scale Token |
| `--text-color` | `var(--framer-text-color)` | Typography Ink Token |
| `--letter-spacing` | `var(--framer-letter-spacing)` | Typography / Scale Token |
| `--font-size` | `var(--framer-font-size)` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.framer-tR7CP> — `www-fragment-im`)**:
   - Landmark `<nav class="framer-tR7CP framer-W48R1">` hosting `Fragment Studio · Independent Design` navigation (`Home Home · Work Work · About About · Contact Contact · EN PL`), DOM attributes (`data-redirect-timezone="1"`, `data-framer-font-css`, `data-framer-css-ssr-minified`, `data-framer-components="framer-lib-cursors-ho..."`), and stylesheet rule `focus-visible { outline: 2px solid 757575; outline-offset: 6px; border-radius: 6px; }`.
2. **Hero Stage & Focal Lead (<section.framer-7o1u1h> — `One designer. Clear direction. Com`)**:
   - Landmark `<section class="framer-7o1u1h mobile-hero">` presenting display lead `One designer. Clear direction. Complete execution.` and copy excerpt *"Consistent creative direction for brands across visual identity, "* over `#c9d0d2` canvas and `#000` ink.
3. **Primary Showcase & Content Grid (<section.framer-17uuuhg> — `About me`)**:
   - Landmark `<section class="framer-17uuuhg">` rendering section `About me` with copy *"Start a Project Start a Project"*, asset references (`p1FP15nWl4LPFrB978NFoMKhMrE.png`, `GoVnPOGObUh1MO9i6ATNEe6r2g.png`, `3hSn8XTXecIOBHOo2uSnD8XPSc.png`, `fonts.gstatic.com`), and grid rule `.mobile-hero { height: 100svh !important; min-height: 100svh !important; }`.
4. **Interactive Detail & Feature Matrix (<section.framer-H4KuY> — `What I Do`)**:
   - Landmark `<section class="framer-H4KuY framer-tMFtv">` framing `What I Do` and `Brand Identity` (*"I’m a freelance multidisciplinary designer with 15 years of exper"*) with `#8d9496` surface cards, `#fff` accents, and `html { scrollbar-gutter: stable; }`.
5. **Colophon & Global Directory Footer (<footer.framer-V3ncb> — `https://www.fragment.im`)**:
   - Landmark `<footer class="framer-V3ncb framer-QbbfG">` anchoring `Fragment Studio · Independent De` footer links (`Home Home · Work Work · About About · Contact Contact · EN PL`), copy *"Learn More → Learn More →"*, and `#687679` structural dividers.
