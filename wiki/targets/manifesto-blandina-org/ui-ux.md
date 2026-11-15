# UI & UX Architecture: manifesto-blandina-org

## Overview & Design Identity
- **Target**: `manifesto-blandina-org` (**Connect, Create, Change: Manifesto of Blandina**)
- **Production URL**: [https://manifesto.blandina.org/](https://manifesto.blandina.org/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#fff` / `#edece8`)
- **Summary**: Manifesto of Blandina: connect with yourself, create the life you want, change the world. Yoga, mindfulness and meditation in Padua, the...
- **Total Clean CSS Variables Extracted**: `97` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Host Grotesk`
- **Body Font Stack**: `Host Grotesk Fallback\: BlinkMacSystemFont`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `65vw`, `50px`, `clamp(100px,6.94444vw,100px)`, `7vw`, `clamp(72px,5vw,72px)`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `65vw`, `50px`, `clamp(100px,6.94444vw,100px)`, `7vw`, `clamp(72px,5vw,72px)`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `65vw`, `50px`, `clamp(100px,6.94444vw,100px)`, `7vw`, `clamp(72px,5vw,72px)`)
- **Metadata & Labels**: CSS variables `--label-height: 20px`, `--meta-gap: 14px`, `--meta-gap-under: 19px`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#fff` | `var(--color-white)` in `:root` |
| **Primary Typography Ink** | `#4a4f32` | `var(--color-bark-green)` in `:root` |
| **Elevated Surface / Card Substrate** | `#9c9873` | `var(--color-field-green)` in `:root` |
| **Interactive Accent / Highlight** | `#edece8` | `var(--color-ivory)` in `:root` |
| **Secondary / Muted Copy** | `#b59972` | `var(--color-sand)` in `:root` |
| **Structural Hairline Border** | `#a54d25` | `var(--color-terracotta)` in `:root` |
| **Variable Token (`--color-white-10`)** | `#ffffff1a` | `var(--color-white-10)` in `:root` |
| **Variable Token (`--color-black`)** | `#0f0f0f` | `var(--color-black)` in `:root` |
| **Variable Token (`--color-soft-black`)** | `#1d150c` | `var(--color-soft-black)` in `:root` |
| **Variable Token (`--color-orange`)** | `#fa712a` | `var(--color-orange)` in `:root` |
| **Variable Token (`--color-orange-30`)** | `#fa712a4d` | `var(--color-orange-30)` in `:root` |
| **Variable Token (`--color-ivory-10`)** | `#edece81a` | `var(--color-ivory-10)` in `:root` |
| **Variable Token (`--color-ivory-30`)** | `#edece84d` | `var(--color-ivory-30)` in `:root` |
| **Variable Token (`--color-soft-black-10`)** | `#1d150c1a` | `var(--color-soft-black-10)` in `:root` |
| **Variable Token (`--color-soft-black-70`)** | `#1d150cb3` | `var(--color-soft-black-70)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-base` | `var(--font-sans)` | Typography / Scale Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--color-white-10` | `#ffffff1a` | Canvas / Surface Token |
| `--color-bark-green` | `#4a4f32` | Brand / Palette Token |
| `--color-field-green` | `#9c9873` | Brand / Palette Token |
| `--color-ivory` | `#edece8` | Brand / Palette Token |
| `--color-sand` | `#b59972` | Brand / Palette Token |
| `--color-terracotta` | `#a54d25` | Brand / Palette Token |
| `--color-black` | `#0f0f0f` | Canvas / Surface Token |
| `--color-soft-black` | `#1d150c` | Canvas / Surface Token |
| `--color-orange` | `#fa712a` | Brand / Palette Token |
| `--color-orange-30` | `#fa712a4d` | Brand / Palette Token |
| `--color-ivory-10` | `#edece81a` | Brand / Palette Token |
| `--color-ivory-30` | `#edece84d` | Brand / Palette Token |
| `--color-soft-black-10` | `#1d150c1a` | Canvas / Surface Token |
| `--color-soft-black-70` | `#1d150cb3` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.inspirational-gallery__head> — `manifesto-blandina-org`)**:
   - Landmark `<header class="inspirational-gallery__head">` hosting `Connect, Create, Change: Manifesto o` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-v-cb3bbcd5`, `data-v-59ccf550`, `data-cursor="hide"`, `data-v-ba6e3b8d`), and stylesheet rule `property --line-bottom { syntax:"<length>";inherits:true;initial-value:360px }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Blandina`)**:
   - Landmark `<section class="hero hero--fx">` presenting display lead `Blandina` and copy excerpt *"mindfulness conscious living."* over `#fff` canvas and `#4a4f32` ink.
3. **Primary Showcase & Content Grid (<section.the-intro> — `Everything begins within.`)**:
   - Landmark `<section class="the-intro home-h__panel">` rendering section `Everything begins within.` with copy *"C l i c k a n y w h e r e t o e n t e r w i t h s o u n d"*, asset references (`embeds.iubenda.com`, `cdn.iubenda.com`, `entry.D6Uwv4sb.css`, `useSmokeLayer.C7tBsLdG.css`), and grid rule `.-is-hidden { display:none!important }`.
4. **Interactive Detail & Feature Matrix (<section.immersive-video> — `Connect with yourself`)**:
   - Landmark `<section class="immersive-video home-h__panel">` framing `Connect with yourself` and `Create the life you want` (*"C l i c k a n y w h e r e"*) with `#9c9873` surface cards, `#edece8` accents, and `.-is-mobile { display:none!important }`.
5. **Colophon & Global Directory Footer (<footer.the-footer> — `https://manifesto.blandina.org/`)**:
   - Landmark `<footer class="the-footer">` anchoring `Connect, Create, Change: Manifes` footer links (`Overview · Index · Archive · About · Contact`), copy *"t o e n t e r w i t h"*, and `#a54d25` structural dividers.
