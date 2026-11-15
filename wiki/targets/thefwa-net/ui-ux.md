# UI & UX Architecture: thefwa-net

## Overview & Design Identity
- **Target**: `thefwa-net` (**FWA Wire — winners' newswire**)
- **Production URL**: [https://thefwa.net/](https://thefwa.net/)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000000` canvas, `#7E7E7E` ink, `#303030` accent)
- **Summary**: News from FWA winners — hires, launches, talks and work in progress. One post per person per day, newest first. No algorithm, no ranking.
- **Total Clean CSS Variables Extracted**: `13` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Silkscreen`
- **Body Font Stack**: `B4B4B4`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: not explicitly declared on tag in static CSS (stylesheet font-size ladder: `12px`, `8px`, `11px`, `9px`, `14px`)
- **Section Heading (`H2`)**: rule `h2` (`font-size: 11px`, `letter-spacing: .22em`, `font-weight: 700`)
- **Body Copy**: CSS variables `--body: #B4B4B4`; rule `body` (`font-size: 12px`, `line-height: 1.5`)
- **Metadata & Labels**: rule `.meta` (`font-size: 8px`, `letter-spacing: .06em`)

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | `var(--void)` in `:root` |
| **Primary Typography Ink** | `#0C0C0C` | `var(--panel)` in `:root` |
| **Elevated Surface / Card Substrate** | `#151515` | `var(--inset)` in `:root` |
| **Interactive Accent / Highlight** | `#303030` | `var(--line)` in `:root` |
| **Secondary / Muted Copy** | `#4A4A4A` | `var(--line-hi)` in `:root` |
| **Structural Hairline Border** | `#7E7E7E` | `var(--dim)` in `:root` |
| **Variable Token (`--body`)** | `#B4B4B4` | `var(--body)` in `:root` |
| **Variable Token (`--bright`)** | `#E6E6E6` | `var(--bright)` in `:root` |
| **Variable Token (`--yellow`)** | `#FFCC00` | `var(--yellow)` in `:root` |
| **Variable Token (`--yellow-dk`)** | `#8A6E00` | `var(--yellow-dk)` in `:root` |
| **Variable Token (`--amber`)** | `#FF9900` | `var(--amber)` in `:root` |
| **Variable Token (`--green`)** | `#9ACD00` | `var(--green)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--void` | `#000000` | Color / Atmospheric Token |
| `--panel` | `#0C0C0C` | Color / Atmospheric Token |
| `--inset` | `#151515` | Color / Atmospheric Token |
| `--line` | `#303030` | Color / Atmospheric Token |
| `--line-hi` | `#4A4A4A` | Color / Atmospheric Token |
| `--dim` | `#7E7E7E` | Color / Atmospheric Token |
| `--body` | `#B4B4B4` | Color / Atmospheric Token |
| `--bright` | `#E6E6E6` | Color / Atmospheric Token |
| `--yellow` | `#FFCC00` | Color / Atmospheric Token |
| `--yellow-dk` | `#8A6E00` | Color / Atmospheric Token |
| `--amber` | `#FF9900` | Color / Atmospheric Token |
| `--green` | `#9ACD00` | Color / Atmospheric Token |
| `--logo-knockout` | `var(--inset)` | Design System Custom Token |
| `--thefwa-net-bg` | `#000000` | Canvas Substrate (from `var(--void)` in `:root`) |
| `--thefwa-net-ink` | `#7E7E7E` | Primary Typography Ink (stylesheet-derived) |
| `--thefwa-net-surface` | `#151515` | Surface Substrate (stylesheet-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.pager> — `thefwa-net`)**:
   - Landmark `<nav class="pager">` hosting `FWA Wire — winners' newswire` navigation (`older →`), DOM attributes (`data-id="84"`, `data-view="image"`, `data-seen="p84:image"`, `data-src="/media/posts/mwcmqskj..."`), and stylesheet rule `html { -webkit-text-size-adjust:100% }`.
2. **Hero Stage & Focal Lead (<section.panel> — `FWA Certified`)**:
   - Landmark `<section class="panel">` presenting display lead `FWA Certified` and copy excerpt *"Posted by FWA winners >>> one post per person per day >>> newest "* over `#000000` canvas and `#7E7E7E` ink.
3. **Primary Showcase & Content Grid (<section.panel> — `Incredible Space`)**:
   - Landmark `<section class="panel filters">` rendering section `Incredible Space` with copy *"Winners post here. One item a day, newest first."*, asset references (`favicon.ico`, `icon.svg`, `apple-touch-icon.png`, `manifest.webmanifest`), and grid rule `.px { font-family:'Silkscreen',monospace;font-weight:400;letter-spacing:.02em }`.
4. **Interactive Detail & Feature Matrix (<section.panel> — `Filter`)**:
   - Landmark `<section class="panel wire">` framing `Filter` and `The Wire` (*"Incredible Space is an interactive collection of procedural archi"*) with `#151515` surface cards, `#303030` accents, and `.shell { max-width:940px;margin:0 auto;padding:8px }`.
5. **Colophon & Global Directory Footer (<footer.ticker> — `https://thefwa.net/`)**:
   - Landmark `<footer class="ticker">` anchoring `FWA Wire — winners' newswire` footer links (`older →`), copy *"Website · Certified 14 November 2026"*, and `#7E7E7E` structural dividers.
