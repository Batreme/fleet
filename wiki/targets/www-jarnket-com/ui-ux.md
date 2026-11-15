# UI & UX Architecture: www-jarnket-com

## Overview & Design Identity
- **Target**: `www-jarnket-com` (**JarnKet · Ketsadaphone Boutpanyda, web engineer in Vientiane**)
- **Production URL**: [https://www.jarnket.com/](https://www.jarnket.com/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f4f5f7` / `#62666e`)
- **Summary**: Software engineer in Vientiane, Laos and WorldSkills ASEAN 2025 Web Technologies Expert, building fast, accessible React and Next.js inte...
- **Total Clean CSS Variables Extracted**: `87` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Geist`
- **Body Font Stack**: `Geist Fallback`
- **Monospace / Technical Font Stack**: `Geist Mono`
- **Hero Display (`H1`)**: CSS variables `--font-display: "Chakra Petch", "Chakra Petch Fallback"`
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `1.25em`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `100%`, `1.25em`)
- **Metadata & Labels**: CSS variables `--font-geist-mono: "Geist Mono", "Geist Mono Fallback"`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#f4f5f7` | `var(--jk-bg)` in `:root` |
| **Primary Typography Ink** | `#fcfcfe` | `var(--jk-raised)` in `:root` |
| **Elevated Surface / Card Substrate** | `#111418` | `var(--jk-fg)` in `:root` |
| **Interactive Accent / Highlight** | `#62666e` | `var(--jk-muted)` in `:root` |
| **Secondary / Muted Copy** | `#d7d9dc` | `var(--jk-line)` in `:root` |
| **Structural Hairline Border** | `#060e23` | `var(--jk-night)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-geist` | `"Geist", "Geist Fallback"` | Typography / Scale Token |
| `--font-geist-mono` | `"Geist Mono", "Geist Mono Fallback"` | Typography / Scale Token |
| `--background` | `0 0% 96%` | Canvas / Surface Token |
| `--foreground` | `0 0% 10%` | Typography Ink Token |
| `--card` | `0 0% 98%` | Dimension / Scale Token |
| `--card-foreground` | `0 0% 10%` | Typography Ink Token |
| `--popover` | `0 0% 98%` | Dimension / Scale Token |
| `--popover-foreground` | `0 0% 10%` | Typography Ink Token |
| `--primary` | `0 0% 10%` | Brand / Palette Token |
| `--primary-foreground` | `0 0% 96%` | Typography Ink Token |
| `--secondary` | `0 0% 92%` | Brand / Palette Token |
| `--secondary-foreground` | `0 0% 10%` | Typography Ink Token |
| `--muted` | `0 0% 91%` | Dimension / Scale Token |
| `--muted-foreground` | `0 0% 40%` | Typography Ink Token |
| `--accent` | `0 0% 90%` | Brand / Palette Token |
| `--accent-foreground` | `0 0% 10%` | Typography Ink Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.fixed> — `www-jarnket-com`)**:
   - Landmark `<header class="fixed inset-x-0">` hosting `JarnKet · Ketsadaphone Boutpanyda, w` navigation (`Index · Work · Field notes · Gallery · GitHub`), DOM attributes (`data-precedence="next"`, `data-href="/_next/static/immutab..."`, `data-sdkn="@vercel/analytics/react"`, `data-sdkv="2.0.1"`), and stylesheet rule `._8NX9hq_className { font-family:Geist,Geist Fallback;font-style:normal }`.
2. **Hero Stage & Focal Lead (<section.relative> — `JARN KET`)**:
   - Landmark `<section class="relative">` presenting display lead `JARN KET` and copy excerpt *"Vientiane, LA 17°58′N 102°36′E"* over `#f4f5f7` canvas and `#060e23` ink.
3. **Primary Showcase & Content Grid (<section.jk-flood> — `T o o l k i t`)**:
   - Landmark `<section class="jk-flood relative">` rendering section `T o o l k i t` with copy *"Warping the loom · woven from “ ສະບາຍດີ ”"*, asset references (`1ccf8ef962b3f693-s.p.2xt4dxqx4hw9...`, `797e433ab948586e-s.p.1v5bejj26fx9...`, `8457265da2739722-s.p.00okbctd204v...`, `caa3a2e1cccd8315-s.p.0zr6hhvz-h9n...`), and grid rule `._8NX9hq_variable { --font-geist:"Geist", "Geist Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.relative> — `Languages`)**:
   - Landmark `<section class="relative">` framing `Languages` and `Frameworks` (*"Software Engineer @BCEL Bank"*) with `#111418` surface cards, `#62666e` accents, and `.z61v7q_className { font-family:Geist Mono,Geist Mono Fallback;font-style:normal }`.
5. **Colophon & Global Directory Footer (<footer.jk-flood> — `https://www.jarnket.com/`)**:
   - Landmark `<footer class="jk-flood relative">` anchoring `JarnKet · Ketsadaphone Boutpanyd` footer links (`Index · Work · Field notes · Gallery · GitHub`), copy *"ketsadaphoneOfficial@gmail.com"*, and `#060e23` structural dividers.
