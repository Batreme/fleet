# UI & UX Architecture: stillform-homes

## Overview & Design Identity
- **Target**: `stillform-homes` (**STILL / FORM — Contemporary Architecture & Residences**)
- **Production URL**: [https://stillform.homes/](https://stillform.homes/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fffbeb` / `#1c398e`)
- **Summary**: Discover STILL / FORM, a study in contemporary residential architecture, considered spaces, material, and light. Explore the residences t...
- **Total Clean CSS Variables Extracted**: `72` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Familjen Grotesk`
- **Body Font Stack**: `Familjen Grotesk Fallback`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: calc(2.5 / 2.25)`, `--text-5xl: 3rem`
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: calc(2 / 1.5)`, `--text-3xl: 1.875rem`
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`
- **Metadata & Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fffbeb` | `var(--color-amber-50)` in `:root` |
| **Primary Typography Ink** | `#fcbb00` | `var(--color-amber-400)` in `:root` |
| **Elevated Surface / Card Substrate** | `#b75000` | `var(--color-amber-700)` in `:root` |
| **Interactive Accent / Highlight** | `#1c398e` | `var(--color-blue-900)` in `:root` |
| **Secondary / Muted Copy** | `#f9fafb` | `var(--color-gray-50)` in `:root` |
| **Structural Hairline Border** | `#f3f4f6` | `var(--color-gray-100)` in `:root` |
| **Variable Token (`--color-gray-200`)** | `#e5e7eb` | `var(--color-gray-200)` in `:root` |
| **Variable Token (`--color-gray-300`)** | `#d1d5dc` | `var(--color-gray-300)` in `:root` |
| **Variable Token (`--color-gray-400`)** | `#99a1af` | `var(--color-gray-400)` in `:root` |
| **Variable Token (`--color-gray-500`)** | `#6a7282` | `var(--color-gray-500)` in `:root` |
| **Variable Token (`--color-gray-700`)** | `#364153` | `var(--color-gray-700)` in `:root` |
| **Variable Token (`--color-gray-800`)** | `#1e2939` | `var(--color-gray-800)` in `:root` |
| **Variable Token (`--color-gray-900`)** | `#101828` | `var(--color-gray-900)` in `:root` |
| **Variable Token (`--color-black`)** | `#000` | `var(--color-black)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-familjen-grotesk` | `"Familjen Grotesk", "Familjen Grotesk Fallback"` | Typography / Scale Token |
| `--font-instrument-serif` | `"Instrument Serif", "Instrument Serif Fallback"` | Typography / Scale Token |
| `--color-amber-50` | `#fffbeb` | Brand / Palette Token |
| `--color-amber-400` | `#fcbb00` | Brand / Palette Token |
| `--color-amber-700` | `#b75000` | Brand / Palette Token |
| `--color-blue-900` | `#1c398e` | Brand / Palette Token |
| `--color-gray-50` | `#f9fafb` | Brand / Palette Token |
| `--color-gray-100` | `#f3f4f6` | Brand / Palette Token |
| `--color-gray-200` | `#e5e7eb` | Brand / Palette Token |
| `--color-gray-300` | `#d1d5dc` | Brand / Palette Token |
| `--color-gray-400` | `#99a1af` | Brand / Palette Token |
| `--color-gray-500` | `#6a7282` | Brand / Palette Token |
| `--color-gray-700` | `#364153` | Brand / Palette Token |
| `--color-gray-800` | `#1e2939` | Brand / Palette Token |
| `--color-gray-900` | `#101828` | Brand / Palette Token |
| `--color-black` | `#000` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.fixed> — `stillform-homes`)**:
   - Landmark `<nav class="fixed left-0">` hosting `STILL / FORM — Contemporary Architec` navigation (`STILL / FORM · S t a y s S t a y s · T o u r T o u r`), DOM attributes (`data-precedence="next"`, `data-boot-loader-complete="true"`, `data-hover-reveal="true"`, `data-hover-reveal-initialized="true"`), and stylesheet rule `tesk_f0527726-module__vHdTJa__cla... { font-family:Familjen Grotesk,Familjen Grotesk Fallback;font-style:normal }`.
2. **Hero Stage & Focal Lead (<section.sticky> — `S p a c e , C o n s i d e r e d .`)**:
   - Landmark `<section class="sticky top-0">` presenting display lead `S p a c e , C o n s i d e r e d .` and copy excerpt *"R e s i d e n c e R e s i d e n c e"* over `#fffbeb` canvas and `#1c398e` ink.
3. **Primary Showcase & Content Grid (<section.relative> — `Full View`)**:
   - Landmark `<section class="relative z-20">` rendering section `Full View` with copy *"S t a y s S t a y s"*, asset references (`7ebf22b5a21034f8-s.p.3j3877k49yy0...`, `e41d5df559864f9e-s.p.1g73gv09-xcb...`, `f5edcc6a132fb1ad-s.p.3ii__yurxaf4...`, `hero3.webp`), and grid rule `otesk_f0527726-module__vHdTJa__va... { --font-familjen-grotesk:"Familjen Grotesk", "Familjen Grotesk Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.relative> — `A study in form, light and proport`)**:
   - Landmark `<section class="relative">` framing `A study in form, light and proportion.` and `Rooms that hold the evening light.` (*"C o n t a c t C o n t a c t"*) with `#b75000` surface cards, `#1c398e` accents, and `erif_72bbfbb4-module__cRt5FG__cla... { font-family:Instrument Serif,Instrument Serif Fallback;font-weight:400 }`.
5. **Colophon & Global Directory Footer (<footer.relative> — `https://stillform.homes/`)**:
   - Landmark `<footer class="relative z-30">` anchoring `STILL / FORM — Contemporary Arch` footer links (`STILL / FORM · S t a y s S t a y s · T o u r T o u r`), copy *"E x p l o r e R e s i d e n c e E x p l o r e R e s i d e n "*, and `#f3f4f6` structural dividers.
