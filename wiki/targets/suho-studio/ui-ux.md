---
title: "UI & UX Architecture: suho-studio"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: suho-studio

## Overview & Design Identity
- **Target**: `suho-studio` (**Suho Video Editor**)
- **Production URL**: [https://suho.studio/](https://suho.studio/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×828px`, Mobile `390×1744px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#01040b` / `#d7401f`)
- **Summary**: Selected work by Suho, video editor and sound designer.
- **Total Clean CSS Variables Extracted**: `99` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Figtree Variable`
- **Body Font Stack**: `Figtree Variable`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 66.24px`, `line-height: 56.9664px`, `font-weight: 700`); CSS variables `--font-weight-display: 600`, `--tracking-display: -.083em`, `--type-display: clamp(3.3rem, 1.52857rem + 8.85714vw, 9.5rem)`; rule `h1` (`font-size: clamp(72px,9vw,170px)`, `line-height: 1`, `letter-spacing: -.03em`, `font-weight: 400`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 129.6px`, `line-height: 101.088px`, `font-weight: 400`, `letter-spacing: -9.72px`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--type-body: clamp(.95rem, .9rem + .25vw, 1.125rem)`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: normal`, `font-weight: 400`); CSS variables `--tracking-label: .07em`, `--type-label: clamp(.625rem, .589286rem + .178571vw, .75rem)`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#01040b` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#f7f7f4` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#07090d` | live computed `nav` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#d7401f` | `var(--film-accent)` in `:root` |
| **Secondary / Muted Copy** | `#111111` | live computed `a` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#898a8d` | `:hover { border-color: #898a8d }` |
| **Variable Token (`--color-paper`)** | `#f3f3ef` | `var(--color-paper)` in `:root` |
| **Variable Token (`--color-gallery-paper`)** | `#ebebeb` | `var(--color-gallery-paper)` in `:root` |
| **Variable Token (`--color-ink`)** | `#10100f` | `var(--color-ink)` in `:root` |
| **Variable Token (`--color-blue`)** | `#2f53ff` | `var(--color-blue)` in `:root` |
| **Variable Token (`--color-purple`)** | `#7d3fef` | `var(--color-purple)` in `:root` |
| **Variable Token (`--color-blue-soft`)** | `#99a8ff` | `var(--color-blue-soft)` in `:root` |
| **Variable Token (`--color-cyan`)** | `#19d9f3` | `var(--color-cyan)` in `:root` |
| **Variable Token (`--color-cyan-soft`)** | `#8decf8` | `var(--color-cyan-soft)` in `:root` |
| **Variable Token (`--color-night`)** | `#020b18` | `var(--color-night)` in `:root` |
| **Variable Token (`--color-sky`)** | `#020408` | `var(--color-sky)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-paper` | `#f3f3ef` | Canvas / Surface Token |
| `--color-gallery-paper` | `#ebebeb` | Canvas / Surface Token |
| `--color-ink` | `#10100f` | Typography Ink Token |
| `--color-blue` | `#2f53ff` | Brand / Palette Token |
| `--color-purple` | `#7d3fef` | Brand / Palette Token |
| `--color-blue-soft` | `#99a8ff` | Brand / Palette Token |
| `--color-cyan` | `#19d9f3` | Brand / Palette Token |
| `--color-cyan-soft` | `#8decf8` | Brand / Palette Token |
| `--color-night` | `#020b18` | Brand / Palette Token |
| `--color-void` | `#01040b` | Brand / Palette Token |
| `--color-sky` | `#020408` | Brand / Palette Token |
| `--grain-strength` | `.6` | Design System Custom Token |
| `--color-line` | `color-mix(in srgb, var(--color-ink) 16%, transparent)` | Brand / Palette Token |
| `--color-muted` | `color-mix(in srgb, var(--color-ink) 60%, transparent)` | Brand / Palette Token |
| `--color-paper-muted` | `color-mix(in srgb, var(--color-paper) 76%, transparent)` | Canvas / Surface Token |
| `--font-major` | `"Figtree Variable", "Helvetica Neue", Arial, sans-serif` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.skip-link> — `suho-studio`)**:
   - Landmark `<header class="skip-link">` (`240x148px`) hosting `Suho Video Editor` navigation (`Suho eyes Suho home · Home · Work W W o o r r k k · Get in touch`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-skip-link="true"`), and stylesheet rule `scene-module-scss-module__7nHW2G_... { pointer-events:none;width:100%;height:100%;position:absolute;inset:0 }`.
2. **Hero Stage & Focal Lead (<section.static-portfolio> — `Suho. VIDEO EDITOR.`)**:
   - Landmark `<section class="static-portfolio">` presenting display lead `Suho. VIDEO EDITOR.` and copy excerpt *"Editing stories through SFX, Storytelling, Motion Design and Soun"* over `#01040b` canvas and `#f7f7f4` ink.
3. **Primary Showcase & Content Grid (<section.sr-only> — `Suho Video Editor`)**:
   - Landmark `<section class="sr-only">` rendering section `Suho Video Editor` with copy *"Selected work by Suho, video editor and sound designer."*, asset references (`Figtree-VariableFont_wght.woff2`, `254drbfp0n4_4.css`, `161fswjwr-tnq.css`, `00ierz6vnepx8.css`), and grid rule `cene-module-scss-module__7nHW2G__... { opacity:1;transition:opacity 1.4s }`.
4. **Interactive Detail & Feature Matrix (<section.undefined> — `Selected work`)**:
   - Landmark `<section class="undefined">` framing `Selected work` and `Personal edits` (*"Featured commission Screens, text and graphics move together to s"*) with `#07090d` surface cards, `#d7401f` accents, and `module-scss-module__7nHW2G__error... { color:dce6f4;text-shadow:-.5px 0 5fbed280,.65px 0 637cd880 }`.
5. **Colophon & Global Directory Footer (<footer> — `https://suho.studio/`)**:
   - Landmark `<footer>` landmark anchoring `Suho Video Editor` footer links (`Suho eyes Suho home · Home · Work W W o o r r k k · Get in touch`), copy *"Screens, text and graphics move together to show a product i"*, and `#898a8d` structural dividers.
