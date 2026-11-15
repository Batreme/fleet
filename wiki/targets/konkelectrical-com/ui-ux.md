# UI & UX Architecture: konkelectrical-com

## Overview & Design Identity
- **Target**: `konkelectrical-com` (**Konk Electrical · Eastern Suburbs Electricians, Sydney**)
- **Production URL**: [https://konkelectrical.com/](https://konkelectrical.com/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#0b0b0c` canvas, `#f2f0eb` ink, `#26262a` accent)
- **Summary**: Electrical and automation specialists for high-end homes across Sydney's Eastern Suburbs. Lighting, smart home, data and audio visual, wi...
- **Total Clean CSS Variables Extracted**: `41` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Archivo`
- **Body Font Stack**: `Open\ Sans`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--cc-font-display: 'Archivo', sans-serif`
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `48px`, `24px`, `20px`, `14px`)
- **Body Copy**: rule `p` (`font-size: 13px`, `line-height: 1.3`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `48px`, `24px`, `20px`, `14px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#0b0b0c` | `var(--ink)` in `:root` |
| **Primary Typography Ink** | `#121214` | `var(--ink-2)` in `:root` |
| **Elevated Surface / Card Substrate** | `#17171a` | `var(--ink-3)` in `:root` |
| **Interactive Accent / Highlight** | `#26262a` | `var(--hair)` in `:root` |
| **Secondary / Muted Copy** | `#f2f0eb` | `var(--paper)` in `:root` |
| **Structural Hairline Border** | `#c89446` | `var(--brass)` in `:root` |
| **Variable Token (`--brass-hi`)** | `#e7b96f` | `var(--brass-hi)` in `:root` |
| **Variable Token (`--brass-dim`)** | `#8a6733` | `var(--brass-dim)` in `:root` |
| **Variable Token (`--bronze`)** | `#5b4a33` | `var(--bronze)` in `:root` |
| **Variable Token (`--text`)** | `#e9e7e2` | `var(--text)` in `:root` |
| **Variable Token (`--text-dim`)** | `#8c8a84` | `var(--text-dim)` in `:root` |
| **Variable Token (`--text-faint`)** | `#55534e` | `var(--text-faint)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ink` | `#0b0b0c` | Typography Ink Token |
| `--ink-2` | `#121214` | Typography Ink Token |
| `--ink-3` | `#17171a` | Typography Ink Token |
| `--hair` | `#26262a` | Color / Atmospheric Token |
| `--paper` | `#f2f0eb` | Canvas / Surface Token |
| `--brass` | `#c89446` | Color / Atmospheric Token |
| `--brass-hi` | `#e7b96f` | Color / Atmospheric Token |
| `--brass-dim` | `#8a6733` | Color / Atmospheric Token |
| `--bronze` | `#5b4a33` | Color / Atmospheric Token |
| `--text` | `#e9e7e2` | Typography Ink Token |
| `--text-dim` | `#8c8a84` | Typography Ink Token |
| `--text-faint` | `#55534e` | Typography Ink Token |
| `--s1` | `4px` | Dimension / Scale Token |
| `--s2` | `8px` | Dimension / Scale Token |
| `--s3` | `12px` | Dimension / Scale Token |
| `--s4` | `16px` | Dimension / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.hdr> — `konkelectrical-com`)**:
   - Landmark `<header class="hdr">` hosting `Konk Electrical · Eastern Suburbs El` navigation (`Home · About · Electrical · Automation · Data & Networking`), DOM attributes (`data-section="header"`, `data-label="Header"`, `data-locked`, `data-header`), and stylesheet rule `.sbi_lightbox button:focus-visible { outline:2px solid var(--sb-focus-ring)!important;outline-offset:2px!impo... }`.
2. **Hero Stage & Focal Lead (<section.tf> — `Electrical`)**:
   - Landmark `<section class="tf">` presenting display lead `Electrical` and copy excerpt *"05 Data & Networking"* over `#0b0b0c` canvas and `#f2f0eb` ink.
3. **Primary Showcase & Content Grid (<section.cc-page-home> — `Automation`)**:
   - Landmark `<section class="cc-page-home">` rendering section `Automation` with copy *"info@konkelectrical.com.au"*, asset references (`xfavicon.png,qv=1793266697.pagesp...`, `A.fonts.css,,qv==1793266697+style...`, `xkonk-logo-white.png,qv=179326669... (Konk Electrical)`, `xkonk-logo-white.png,qv=179326669... (Konk Electrical)`), and grid rule `sb_instagram { -webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:bord... }`.
4. **Interactive Detail & Feature Matrix (<section.konk-load> — `Data & Networking`)**:
   - Landmark `<section class="konk-load">` framing `Data & Networking` and `Audio Visual` (*"From repairs and alterations to complete renovations, new builds "*) with `#17171a` surface cards, `#26262a` accents, and `sb_instagram:after { clear:both;content:"";display:table }`.
5. **Colophon & Global Directory Footer (<footer.ftr> — `https://konkelectrical.com/`)**:
   - Landmark `<footer class="ftr">` anchoring `Konk Electrical · Eastern Suburb` footer links (`Home · About · Electrical · Automation · Data & Networking`), copy *"Effortless control"*, and `#c89446` structural dividers.
