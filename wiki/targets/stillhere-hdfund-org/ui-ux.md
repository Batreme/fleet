# UI & UX Architecture: stillhere-hdfund-org

## Overview & Design Identity
- **Target**: `stillhere-hdfund-org` (**STILL HERE. · Three Years in Gaza · HDF**)
- **Production URL**: [https://stillhere.hdfund.org/](https://stillhere.hdfund.org/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#101210` canvas, `#eeeee8` ink, `#FED545` accent)
- **Summary**: Three years. One story. Experience three years of HDF’s work in Gaza from 2023–2026.
- **Total Clean CSS Variables Extracted**: `74` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Opening Barlow`
- **Body Font Stack**: `Opening Inter`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--display: Barlow,'Arial Narrow',Impact,sans-serif`; rule `h1` (`font-weight: 700`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: clamp(76px,8.8vw,156px)`, `line-height: .93`, `letter-spacing: -.015em`)
- **Body Copy**: CSS variables `--body: Inter,Arial,sans-serif`; rule `p` (`font-size: 14px`)
- **Metadata & Labels**: rule `small` (`font-size: 12px`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#101210` | `var(--ink)` in `:root` |
| **Primary Typography Ink** | `#eeeee8` | `var(--paper)` in `:root` |
| **Elevated Surface / Card Substrate** | `#a8aaa1` | `var(--muted)` in `:root` |
| **Interactive Accent / Highlight** | `#FED545` | `var(--gold)` in `:root` |
| **Secondary / Muted Copy** | `#2564AA` | `var(--blue)` in `:root` |
| **Structural Hairline Border** | `#111111` | `var(--n-ink)` in `:root` |
| **Variable Token (`--n-paper`)** | `#F7F5F0` | `var(--n-paper)` in `:root` |
| **Variable Token (`--campaign-red`)** | `#BB0305` | `var(--campaign-red)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--ink` | `#101210` | Typography Ink Token |
| `--paper` | `#eeeee8` | Canvas / Surface Token |
| `--muted` | `#a8aaa1` | Color / Atmospheric Token |
| `--gold` | `#FED545` | Color / Atmospheric Token |
| `--blue` | `#2564AA` | Color / Atmospheric Token |
| `--display` | `Barlow,'Arial Narrow',Impact,sans-serif` | Design System Custom Token |
| `--body` | `Inter,Arial,sans-serif` | Design System Custom Token |
| `--gutter` | `7.2vw` | Layout / Spatial Grid Token |
| `--n-ink` | `#111111` | Typography Ink Token |
| `--n-paper` | `#F7F5F0` | Canvas / Surface Token |
| `--n-blue` | `#2564AA` | Color / Atmospheric Token |
| `--n-yellow` | `#FED545` | Color / Atmospheric Token |
| `--n-gutter` | `clamp(26px,6.25vw,120px)` | Layout / Spatial Grid Token |
| `--chapter-gutter` | `var(--n-gutter)` | Layout / Spatial Grid Token |
| `--campaign-red` | `#BB0305` | Color / Atmospheric Token |
| `--doc-paper` | `#F7F5F0` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `stillhere-hdfund-org`)**:
   - Landmark `<header class="site-header">` hosting `STILL HERE. · Three Years in Gaza · ` navigation (`Overview · Index · Archive · About · Contact`), DOM attributes (`data-opening-bootstrap`, `data-site-webpage`, `data-campaign-identity="3e"`, `data-campaign-identity="3e"`), and stylesheet rule `html { scroll-padding-top:100px }`.
2. **Hero Stage & Focal Lead (<section.intro> — `THE WORLD WATCHED .`)**:
   - Landmark `<section class="intro scroll-scene">` presenting display lead `THE WORLD WATCHED .` and copy excerpt *"The opening couldn’t load."* over `#101210` canvas and `#eeeee8` ink.
3. **Primary Showcase & Content Grid (<section.first-days> — `THE FIRST DAYS`)**:
   - Landmark `<section class="first-days scroll-scene">` rendering section `THE FIRST DAYS` with copy *"TIME KEPT MOVING ."*, asset references (`door-leaf.webp`, `al-aqsa-wall-print.webp`, `door-leaf-mono.webp`, `al-aqsa-wall-print-mono.webp`), and grid rule `button:focus-visible { outline:2px solid var(--gold);outline-offset:7px }`.
4. **Interactive Detail & Feature Matrix (<section.timeline-intro> — `THREE YEARS . STILL HERE .`)**:
   - Landmark `<section class="timeline-intro">` framing `THREE YEARS . STILL HERE .` and `From the first water tanks to bread baked in Gaza.` (*"SCROLL UP TO BEGIN"*) with `#a8aaa1` surface cards, `#FED545` accents, and `img { display:block;max-width:100% }`.
5. **Colophon & Global Directory Footer (<footer.campaign-footer> — `https://stillhere.hdfund.org/`)**:
   - Landmark `<footer class="campaign-footer">` anchoring `STILL HERE. · Three Years in Gaz` footer links (`Overview · Index · Archive · About · Contact`), copy *"GAZA CRISIS RESPONSE"*, and `#111111` structural dividers.
