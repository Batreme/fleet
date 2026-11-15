# UI & UX Architecture: abhayrohit-com

## Overview & Design Identity
- **Target**: `abhayrohit-com` (**Abhay Rohit — Creative Product Engineer**)
- **Production URL**: [https://abhayrohit.com/](https://abhayrohit.com/)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#f5ead6` / `#d1c5ac`)
- **Summary**: Abhay Rohit is a creative product engineer in Indore, India, specializing in frontend engineering and interactive design with React, Next...
- **Total Clean CSS Variables Extracted**: `188` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `instrumentSans`
- **Body Font Stack**: `instrumentSans Fallback`
- **Monospace / Technical Font Stack**: `jetbrainsMono`
- **Hero Display (`H1`)**: CSS variables `--qi-font-display: "anton", "anton Fallback", Impact, Arial Narrow, sans-serif`, `--qi-font-studio-display: "antonStudio", "antonStudio Fallback"`, `--archive-display: "display", "display Fallback", Impact`; rule `h1` (`font-size: clamp(58px,8.8vw,144px)`)
- **Section Heading (`H2`)**: CSS variables `--opening-subtitle: clamp(34.72px,3.224cqw,59.52px)`; rule `h2` (`font-size: clamp(36px,5vw,80px)`)
- **Body Copy**: rule `p` (`font-size: clamp(16px,1.8vw,25px)`)
- **Metadata & Labels**: CSS variables `--qi-font-mono: "jetbrainsMono", ui-monospace, monospace`, `--archive-mono: "mono", "mono Fallback", Courier New`; rule `small` (`font-size: clamp(10px,.8vw,14px)`, `line-height: 1.4`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#f5ead6` | `var(--ink)` in `:root` |
| **Primary Typography Ink** | `#241910` | `var(--paper)` in `:root` |
| **Elevated Surface / Card Substrate** | `#f9ebd2` | `var(--text)` in `:root` |
| **Interactive Accent / Highlight** | `#d1c5ac` | `var(--rail-accent)` in `:root` |
| **Secondary / Muted Copy** | `#c1b8a6` | `var(--rail-ink)` in `:root` |
| **Structural Hairline Border** | `#20251f` | `var(--rail-active-ink)` in `:root` |
| **Variable Token (`--edge`)** | `#dcb67c66` | `var(--edge)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ink` | `#f5ead6` | Typography Ink Token |
| `--paper` | `#241910` | Canvas / Surface Token |
| `--text` | `#f9ebd2` | Typography Ink Token |
| `--edge` | `#dcb67c66` | Color / Atmospheric Token |
| `--ease` | `cubic-bezier(.22, 1, .36, 1)` | Motion / Easing Token |
| `--cursor-paper` | `242 237 222` | Canvas / Surface Token |
| `--cursor-ink` | `39 40 33` | Typography Ink Token |
| `--cursor-accent` | `167 45 40` | Brand / Palette Token |
| `--cursor-ease` | `cubic-bezier(.2, .8, .2, 1)` | Motion / Easing Token |
| `--cursor-fill` | `rgb(var(--cursor-paper) / .96)` | Color / Atmospheric Token |
| `--cursor-text` | `rgb(var(--cursor-ink))` | Typography Ink Token |
| `--cursor-line` | `rgb(var(--cursor-paper) / .9)` | Color / Atmospheric Token |
| `--cursor-edge` | `rgb(var(--cursor-ink) / .48)` | Color / Atmospheric Token |
| `--cursor-mark` | `rgb(var(--cursor-accent))` | Color / Atmospheric Token |
| `--chapter-index` | `0` | Design System Custom Token |
| `--chapter-progress` | `0` | Design System Custom Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.MLPEba_header> — `abhayrohit-com`)**:
   - Landmark `<header class="MLPEba_header">` hosting `Abhay Rohit — Creative Product Engin` navigation (`Website · Patient portal · Care team · Operations · Read the case study`), DOM attributes (`data-film-entry="cold-home"`, `data-paint-loader="active"`, `data-preload-tier="desktop"`, `data-preload-bytes="153382"`), and stylesheet rule `.RaGumW_cue .RaGumW_frame { opacity:.36 }`.
2. **Hero Stage & Focal Lead (<section.MLPEba_hero> — `A B H A Y R O H I T`)**:
   - Landmark `<section class="MLPEba_hero">` presenting display lead `A B H A Y R O H I T` and copy excerpt *"Skip to the written portfolio"* over `#f5ead6` canvas and `#241910` ink.
3. **Primary Showcase & Content Grid (<section.KKuYoa_variable> — `My first engineering job.`)**:
   - Landmark `<section class="KKuYoa_variable">` rendering section `My first engineering job.` with copy *"Drag or tap Drag the grip to explore; release to return home. Tap"*, asset references (`anton_full_entry_subset-s.p.0dq58...`, `anton_kinetic_margin-s.p.1o1u0v9k...`, `instrument_sans_latin_wdth_normal...`, `jetbrains_mono_latin_wght_normal_...`), and grid rule `.RaGumW_cue { --ink:38251d;--paper:38251d;--text:fff1d8;--edge:38251d66 }`.
4. **Interactive Detail & Feature Matrix (<article.rojSVa_variable> — `Where care begins.`)**:
   - Landmark `<article class="rojSVa_variable">` framing `Where care begins.` and `A clearer experience for patients.` (*"Drag the grip to explore; release to return home. Tap to visit th"*) with `#f9ebd2` surface cards, `#d1c5ac` accents, and `.RaGumW_frame { transition:opacity .42s var(--ease);position:absolute;inset:0 }`.
5. **Colophon & Global Directory Footer (<footer.jFvPUW_footer> — `https://abhayrohit.com/`)**:
   - Landmark `<footer class="jFvPUW_footer">` anchoring `Abhay Rohit — Creative Product E` footer links (`Website · Patient portal · Care team · Operations · Read the case study`), copy *"Gaming . A miniature world of music, gaming, photography and"*, and `#20251f` structural dividers.
