# UI & UX Architecture: www-terakawaoffice-com_en

## Overview & Design Identity
- **Target**: `www-terakawaoffice-com_en` (**Architectural Photographer in Tokyo, Japan · TERAKAWA Photo Office**)
- **Production URL**: [https://www.terakawaoffice.com/en/](https://www.terakawaoffice.com/en/)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#141414` / `#6d6d6d`)
- **Summary**: Tokyo architectural photographer Naoki Terakawa. Completion photography, drone aerials, models, time-lapse — for architects and developer...
- **Total Clean CSS Variables Extracted**: `24` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `EB Garamond`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `16px`, `9px`, `13px`, `14px`, `10px`)
- **Section Heading (`H2`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `16px`, `9px`, `13px`, `14px`, `10px`)
- **Body Copy**: rule `p` (`font-size: 17px`, `line-height: 1.65`)
- **Metadata & Labels**: CSS variables `--bh-caption-gap: 36px`, `--tx-label: 'Inter',-apple-system,'Helvetica Neue',sans-serif`; rule `small` (`letter-spacing: .035em`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#141414` | `var(--ink)` in `:root` |
| **Primary Typography Ink** | `#3a3a3a` | `var(--ink-2)` in `:root` |
| **Elevated Surface / Card Substrate** | `#6b6b6b` | `var(--ink-soft)` in `:root` |
| **Interactive Accent / Highlight** | `#6d6d6d` | `var(--ink-mute)` in `:root` |
| **Secondary / Muted Copy** | `#e4e2dc` | `var(--line)` in `:root` |
| **Structural Hairline Border** | `#efede7` | `var(--line-soft)` in `:root` |
| **Variable Token (`--paper`)** | `#fbfaf7` | `var(--paper)` in `:root` |
| **Variable Token (`--paper-warm`)** | `#f5f2ea` | `var(--paper-warm)` in `:root` |
| **Variable Token (`--accent`)** | `#7e6538` | `var(--accent)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--bh-fill` | `0` | Design System Custom Token |
| `--bh-caption-gap` | `36px` | Layout / Spatial Grid Token |
| `--tx-text` | `var(--serif-en)` | Typography Ink Token |
| `--tx-rule` | `rgba(20,20,20,.16)` | Color / Atmospheric Token |
| `--tx-label` | `'Inter',-apple-system,'Helvetica Neue',sans-serif` | Dimension / Scale Token |
| `--tpo-ease` | `cubic-bezier(.16,1,.3,1)` | Motion / Easing Token |
| `--fin` | `20px` | Dimension / Scale Token |
| `--ink` | `#141414` | Typography Ink Token |
| `--ink-2` | `#3a3a3a` | Typography Ink Token |
| `--ink-soft` | `#6b6b6b` | Typography Ink Token |
| `--ink-mute` | `#6d6d6d` | Typography Ink Token |
| `--line` | `#e4e2dc` | Color / Atmospheric Token |
| `--line-soft` | `#efede7` | Color / Atmospheric Token |
| `--paper` | `#fbfaf7` | Canvas / Surface Token |
| `--paper-warm` | `#f5f2ea` | Canvas / Surface Token |
| `--accent` | `#7e6538` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.tpo-js> — `www-terakawaoffice-com_en`)**:
   - Landmark `<header class="tpo-js">` hosting `Architectural Photographer in Tokyo,` navigation (`Works · Services · Pricing · About · Contact`), DOM attributes (`data-tpo-field-worker`, `data-blue-hour`, `data-bh-mode="idle"`, `data-work-title="Nogeyama Zoological P..."`), and stylesheet rule `.tpo-bh-frame { position:absolute;left:0;right:0;top:var(--bh-frame-top,0px);bottom:0;ov... }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Architecture, as it truly is.`)**:
   - Landmark `<section class="hero">` presenting display lead `Architecture, as it truly is.` and copy excerpt *"Skip to main content"* over `#141414` canvas and `#efede7` ink.
3. **Primary Showcase & Content Grid (<section.trust-bar> — `Space and intent, in a single fram`)**:
   - Landmark `<section class="trust-bar">` rendering section `Space and intent, in a single frame.` with copy *"↓ Folio PDF 4.7 MB"*, asset references (`favicon.ico`, `favicon-96.png`, `favicon.svg`, `apple-touch-icon.png`), and grid rule `.hero-visual-caption { display:none!important }`.
4. **Interactive Detail & Feature Matrix (<section.works-index> — `Three reasons to work with TERAKAW`)**:
   - Landmark `<section class="works-index">` framing `Three reasons to work with TERAKAWA.` and `Fine detail, faithfully recorded.` (*"EN Language × 日本語 English 中文（简体） Español Français Português (Bras"*) with `#6b6b6b` surface cards, `#6d6d6d` accents, and `.hero-still { animation:none!important;transform:none!important;opacity:1;clip-path:in... }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://www.terakawaoffice.com/en/`)**:
   - Landmark `<footer class="site-footer">` anchoring `Architectural Photographer in To` footer links (`Works · Services · Pricing · About · Contact`), copy *"Português (Brasil)"*, and `#efede7` structural dividers.
