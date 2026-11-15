# UI & UX Architecture: mont-rural-emblematica-agency

## Overview & Design Identity
- **Target**: `mont-rural-emblematica-agency` (**MontRural — Private Masia Among the Vineyards of Penedès**)
- **Production URL**: [https://mont-rural.emblematica.agency](https://mont-rural.emblematica.agency)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#443e2b` canvas, `#ffffff` ink, `#8f8637` accent)
- **Summary**: Rent a masia for a peaceful and cozy getaway just an hour's drive from Barcelona. Perfect for nature retreats, family gatherings, and int...
- **Total Clean CSS Variables Extracted**: `140` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Playfair`
- **Body Font Stack**: `Arial`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `13px`, `16px`, `18px`, `14px`, `22px`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `13px`, `16px`, `18px`, `14px`, `22px`)
- **Body Copy**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `13px`, `16px`, `18px`, `14px`, `22px`)
- **Metadata & Labels**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `13px`, `16px`, `18px`, `14px`, `22px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#443e2b` | `var(--uc-typo-color-Bi2HZBV1z)` in `:root` |
| **Primary Typography Ink** | `#f8e8c5` | `var(--uc-typo-color-BrelB1n4Inb)` in `:root` |
| **Elevated Surface / Card Substrate** | `#cfa65a` | `var(--uc-typo-color-sHMDDLSH)` in `:root` |
| **Interactive Accent / Highlight** | `#8f8637` | `var(--uc-color-color-nUIBOP3G)` in `:root` |
| **Secondary / Muted Copy** | `#37482f` | `var(--uc-color-color-XmYhOpFwF)` in `:root` |
| **Structural Hairline Border** | `#ffffff` | `var(--uc-button-color-IF7y4On)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--t-headline-font` | `'Playfair',Arial,sans-serif` | Typography / Scale Token |
| `--t-text-font` | `'Arial',Arial,sans-serif` | Typography Ink Token |
| `--uc-typo-fontsize-Bi2HZBV1z` | `82px` | Typography / Scale Token |
| `--uc-typo-fontweight-Bi2HZBV1z` | `400` | Typography / Scale Token |
| `--uc-typo-letterspacing-Bi2HZBV1z` | `-6.5px` | Layout / Spatial Grid Token |
| `--uc-typo-fontfamily-Bi2HZBV1z` | `var(--t-headline-font,Arial)` | Typography / Scale Token |
| `--uc-typo-lineheight-Bi2HZBV1z` | `.9` | Layout / Spatial Grid Token |
| `--uc-typo-color-Bi2HZBV1z` | `#443e2b` | Brand / Palette Token |
| `--uc-typo-fontsize-BrelB1n4Inb` | `98px` | Typography / Scale Token |
| `--uc-typo-fontweight-BrelB1n4Inb` | `400` | Typography / Scale Token |
| `--uc-typo-letterspacing-BrelB1n4Inb` | `-6.5px` | Layout / Spatial Grid Token |
| `--uc-typo-fontfamily-BrelB1n4Inb` | `var(--t-headline-font,Arial)` | Typography / Scale Token |
| `--uc-typo-lineheight-BrelB1n4Inb` | `.9` | Layout / Spatial Grid Token |
| `--uc-typo-color-BrelB1n4Inb` | `#f8e8c5` | Brand / Palette Token |
| `--uc-typo-fontsize-QLat9wWmu2vZ` | `82px` | Typography / Scale Token |
| `--uc-typo-fontweight-QLat9wWmu2vZ` | `400` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.t450__menu> — `mont-rural-emblematica-agency`)**:
   - Landmark `<nav class="t450__menu">` hosting `MontRural — Private Masia Among the ` navigation (`About · location · What's Inside · SERVICES · Contacts`), DOM attributes (`data-hook="blocks-collection-con..."`, `data-tilda-project-id="25144176"`, `data-tilda-page-id="139030856"`, `data-tilda-page-alias="en"`), and stylesheet rule `.t_datepicker__selected-day::after { display: none !important; content: none !important; }`.
2. **Hero Stage & Focal Lead (<div.t-records> — `MontRural — Private Masia Among th`)**:
   - Landmark `<div class="t-records t-records_animated">` presenting display lead `MontRural — Private Masia Among the Vineyards of` and copy excerpt *"CHECK AVAILABILITY"* over `#443e2b` canvas and `#ffffff` ink.
3. **Primary Showcase & Content Grid (<div.t-records> — `Featured Work & Interactive Showca`)**:
   - Landmark `<div class="t-records t-records_animated">` rendering section `Featured Work & Interactive Showcase` with copy *"R e n t a m a s i a f o r a p e a c e f u l a n d c o z y g e t a"*, asset references (`mont-rural.emblematica.agency`, `ws.tildacdn.com`, `static.tildacdn.com`, `Frame_1948756319.png`), and grid rule `.t_datepicker__header { background: transparent; border-bottom: 1px solid rgba(255,255,255,0.2); }`.
4. **Interactive Detail & Feature Matrix (<div.t-records> — `Technical Architecture & Narrative`)**:
   - Landmark `<div class="t-records t-records_animated">` framing `Technical Architecture & Narrative` and `Global Directory & Contact` (*"a n h o u r ' s d r i v e f r o m B a r c e l o n a . P e r f e c"*) with `#cfa65a` surface cards, `#8f8637` accents, and `.t_datepicker__label span { color: 8F8637; font-weight: 500; }`.
5. **Colophon & Global Directory Footer (<footer.t-records_visible> — `https://mont-rural.emblematica.agency`)**:
   - Landmark `<footer class="t-records_visible">` anchoring `MontRural — Private Masia Among ` footer links (`About · location · What's Inside · SERVICES · Contacts`), copy *"B a r c e l o n a ."*, and `#ffffff` structural dividers.
