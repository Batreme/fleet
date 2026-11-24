---
title: "UI & UX Architecture: manifesto-blandina-org"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: manifesto-blandina-org

## Overview & Design Identity
- **Target**: `manifesto-blandina-org` (**Connect, Create, Change: Manifesto of Blandina**)
- **Production URL**: [https://manifesto.blandina.org/](https://manifesto.blandina.org/)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1280×828px`, Mobile `390×872px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#edece8` / `#ffa500`)
- **Summary**: Manifesto of Blandina: connect with yourself, create the life you want, change the world. Yoga, mindfulness and meditation in Padua, the...
- **Total Clean CSS Variables Extracted**: `97` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Host Grotesk`
- **Body Font Stack**: `Host Grotesk`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 32px`, `line-height: 38.4px`, `font-weight: 700`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 100px`, `line-height: 100px`, `font-weight: 400`, `letter-spacing: -6%`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 19.2px`, `font-weight: 400`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 18px`, `line-height: 20px`, `font-weight: 400`, `letter-spacing: -4%`); CSS variables `--label-height: 20px`, `--meta-gap: 14px`, `--meta-gap-under: 19px`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#edece8` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#1d150c` | live computed `main` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ffa500` | `.-bg-purple { background-color: orange }` (`#ffa500`) |
| **Interactive Accent / Highlight** | `#ffa500` | `.-bg-purple { background-color: orange }` (`#ffa500`) |
| **Secondary / Muted Copy** | `#fa712a` | live computed `p` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#fa712a` | hairline divider derived from live computed `p` `color` (`computed_styles.json`) |
| **Variable Token (`--color-white`)** | `#ffffff` | `var(--color-white)` in `:root` |
| **Variable Token (`--color-bark-green`)** | `#4a4f32` | `var(--color-bark-green)` in `:root` |
| **Variable Token (`--color-field-green`)** | `#9c9873` | `var(--color-field-green)` in `:root` |
| **Variable Token (`--color-sand`)** | `#b59972` | `var(--color-sand)` in `:root` |
| **Variable Token (`--color-terracotta`)** | `#a54d25` | `var(--color-terracotta)` in `:root` |
| **Variable Token (`--color-black`)** | `#0f0f0f` | `var(--color-black)` in `:root` |

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
   - Landmark `<header class="inspirational-gallery__head">` (`1400x34px`) hosting `Connect, Create, Change: Manifesto o` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-v-cb3bbcd5`, `data-v-59ccf550`, `data-cursor="hide"`, `data-v-ba6e3b8d`), and stylesheet rule `property --line-bottom { syntax:"<length>";inherits:true;initial-value:360px }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Blandina`)**:
   - Landmark `<section class="hero hero--fx">` presenting display lead `Blandina` and copy excerpt *"CLICK ANYWHERE TO ENTER WITH SOUND"* over `#edece8` canvas and `#1d150c` ink.
3. **Primary Showcase & Content Grid (<section.the-intro> — `Everything begins within.`)**:
   - Landmark `<section class="the-intro home-h__panel">` rendering section `Everything begins within.` with copy *"Connect with yourself,Create the life you want,Change the world. "*, asset references (`embeds.iubenda.com`, `cdn.iubenda.com`, `entry.D6Uwv4sb.css`, `useSmokeLayer.C7tBsLdG.css`), and grid rule `.-is-hidden { display:none!important }`.
4. **Interactive Detail & Feature Matrix (<section.immersive-video> — `Connect with yourself`)**:
   - Landmark `<section class="immersive-video home-h__panel">` framing `Connect with yourself` and `Create the life you want` (*"Connect with yourself,Create the life you want,Change the world."*) with `#ffa500` surface cards, `#ffa500` accents, and `.-is-mobile { display:none!important }`.
5. **Colophon & Global Directory Footer (<footer.the-footer> — `https://manifesto.blandina.org/`)**:
   - Landmark `<footer class="the-footer">` anchoring `Connect, Create, Change: Manifes` footer links (`Overview · Index · Archive · About · Contact`), copy *"Connect with yourself,"*, and `#fa712a` structural dividers.
