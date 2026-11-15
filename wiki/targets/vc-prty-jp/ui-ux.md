# UI & UX Architecture: vc-prty-jp

## Overview & Design Identity
- **Target**: `vc-prty-jp` (**PARTY STARTUP STUDIO FUND**)
- **Production URL**: [https://vc.prty.jp/](https://vc.prty.jp/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000` / `#171717`)
- **Summary**: 起業家とともに「未来の体験」をつくる創業・シード特化型VC
- **Total Clean CSS Variables Extracted**: `64` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Inter`
- **Body Font Stack**: `Inter Fallback`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `var(--text-base)`, `var(--text-sm)`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `1em`, `80%`, `75%`, `var(--text-base)`, `var(--text-sm)`)
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: calc(1.5 / 1)`
- **Metadata & Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: calc(1 / .75)`, `--text-sm: .875rem`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000` | `var(--color-black)` in `:root` |
| **Primary Typography Ink** | `#fff` | `var(--color-white)` in `:root` |
| **Elevated Surface / Card Substrate** | `#0a0a0a` | `var(--foreground)` in `:root` |
| **Interactive Accent / Highlight** | `#171717` | `var(--primary)` in `:root` |
| **Secondary / Muted Copy** | `#fafafa` | `var(--primary-foreground)` in `:root` |
| **Structural Hairline Border** | `#f5f5f5` | `var(--secondary)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-inter` | `"Inter", "Inter Fallback"` | Typography / Scale Token |
| `--font-sans` | `var(--font-inter)` | Typography / Scale Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--spacing` | `.25rem` | Layout / Spatial Grid Token |
| `--text-xs` | `.75rem` | Typography Ink Token |
| `--text-xs--line-height` | `calc(1 / .75)` | Typography Ink Token |
| `--text-sm` | `.875rem` | Typography Ink Token |
| `--text-sm--line-height` | `calc(1.25 / .875)` | Typography Ink Token |
| `--text-base` | `1rem` | Typography Ink Token |
| `--text-base--line-height` | `calc(1.5 / 1)` | Typography Ink Token |
| `--font-weight-normal` | `400` | Typography / Scale Token |
| `--font-weight-medium` | `500` | Typography / Scale Token |
| `--font-weight-semibold` | `600` | Typography / Scale Token |
| `--font-weight-bold` | `700` | Typography / Scale Token |
| `--tracking-wide` | `.025em` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.fixed> — `vc-prty-jp`)**:
   - Landmark `<nav class="fixed left-0">` hosting `PARTY STARTUP STUDIO FUND` navigation (`FUND · PORTFOLIO · COMPANY · CAREERS · CONTACT`), DOM attributes (`data-precedence="next"`, `data-engine="three.js r184"`, `data-section="hero"`, `data-capture-hide`), and stylesheet rule `nter_fe8b9d92-module__LINzvG__cla... { font-family:Inter,Inter Fallback;font-style:normal }`.
2. **Hero Stage & Focal Lead (<section.absolute> — `PARTY STARTUP STUDIO FUND`)**:
   - Landmark `<section class="absolute">` presenting display lead `PARTY STARTUP STUDIO FUND` and copy excerpt *"©PARTY STARTUP STUDIO FUND"* over `#000` canvas and `#fff` ink.
3. **Primary Showcase & Content Grid (<section.relative> — `Featured Work & Interactive Showca`)**:
   - Landmark `<section class="relative overflow-hidden">` rendering section `Featured Work & Interactive Showcase` with copy *"( PRIVACY POLICY )"*, asset references (`83afe278b6a6bb3c-s.p.0q-301v4kxxn...`, `02utwymhem5xp.css`, `0hkdb982chs.y.js`, `090~fvud_dp_4.js`), and grid rule `inter_fe8b9d92-module__LINzvG__va... { --font-inter:"Inter", "Inter Fallback" }`.
4. **Interactive Detail & Feature Matrix (<section.h-lvh> — `Technical Architecture & Narrative`)**:
   - Landmark `<section class="h-lvh">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"PORTFOLIO SEE MORE"*) with `#0a0a0a` surface cards, `#171717` accents, and `backdrop { box-sizing:border-box;border:0 solid;margin:0;padding:0 }`.
5. **Colophon & Global Directory Footer (<footer.relative> — `https://vc.prty.jp/`)**:
   - Landmark `<footer class="relative border-t">` anchoring `PARTY STARTUP STUDIO FUND` footer links (`FUND · PORTFOLIO · COMPANY · CAREERS · CONTACT`), copy *"Technical Architecture & Narrative"*, and `#f5f5f5` structural dividers.
