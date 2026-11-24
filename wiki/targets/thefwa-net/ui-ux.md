---
title: "UI & UX Architecture: thefwa-net"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: thefwa-net

## Overview & Design Identity
- **Target**: `thefwa-net` (**FWA Wire — winners' newswire**)
- **Production URL**: [https://thefwa.net/](https://thefwa.net/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×4140px`, Mobile `390×2616px`)
- **Visual Archetype**: High-Contrast Obsidian / Atmospheric Design System (`#000000` canvas, `#ffcc00` ink, `#ff9900` accent)
- **Summary**: News from FWA winners — hires, launches, talks and work in progress. One post per person per day, newest first. No algorithm, no ranking.
- **Total Clean CSS Variables Extracted**: `13` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Silkscreen`
- **Body Font Stack**: `Verdana`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: observed font-size ladder: `11px`, `14px`, `12px`, `11.5px`, `8px`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 11px`, `line-height: 16.5px`, `font-weight: 700`, `letter-spacing: 2.42px`); rule `h2` (`font-size: 11px`, `letter-spacing: .22em`, `font-weight: 700`)
- **Body Copy**: live computed `body` (`font-size: 12px`, `line-height: 18px`, `font-weight: 400`); rule `body` (`font-size: 12px`, `line-height: 1.5`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 12px`, `line-height: 18px`, `font-weight: 400`); rule `.meta` (`font-size: 8px`, `letter-spacing: .06em`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#ffcc00` | live computed `h2` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#0c0c0c` | live computed `section` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#ff9900` | live computed `button` `color` (`computed_styles.json`) |
| **Secondary / Muted Copy** | `#7e7e7e` | live computed `a` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#303030` | `var(--line)` in `:root` |
| **Variable Token (`--inset`)** | `#151515` | `var(--inset)` in `:root` |
| **Variable Token (`--line-hi`)** | `#4a4a4a` | `var(--line-hi)` in `:root` |
| **Variable Token (`--body`)** | `#b4b4b4` | `var(--body)` in `:root` |
| **Variable Token (`--bright`)** | `#e6e6e6` | `var(--bright)` in `:root` |
| **Variable Token (`--yellow-dk`)** | `#8a6e00` | `var(--yellow-dk)` in `:root` |
| **Variable Token (`--green`)** | `#9acd00` | `var(--green)` in `:root` |

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
| `--thefwa-net-bg` | `#000000` | Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) |
| `--thefwa-net-ink` | `#ffcc00` | Primary Typography Ink (computed-derived) |
| `--thefwa-net-surface` | `#0c0c0c` | Surface Substrate (computed-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<nav.pager> — `thefwa-net`)**:
   - Landmark `<nav class="pager">` (`598x45px`) hosting `FWA Wire — winners' newswire` navigation (`older →`), DOM attributes (`data-id="90"`, `data-view="image"`, `data-seen="p90:image"`, `data-src="/media/posts/mwtbqeue..."`), and stylesheet rule `html { -webkit-text-size-adjust:100% }`.
2. **Hero Stage & Focal Lead (<section.panel> — `FWA // CANON_STATUS: VERIFIED`)**:
   - Landmark `<section class="panel">` presenting display lead `FWA // CANON_STATUS: VERIFIED` and copy excerpt *"CREDITSDaiki Fujita"* over `#000000` canvas and `#ffcc00` ink.
3. **Primary Showcase & Content Grid (<section.filters> — `A DAY — Seasons of Youth`)**:
   - Landmark `<section class="panel filters">` rendering section `A DAY — Seasons of Youth` with copy *"Posted by FWA winners >>> one post per person per day >>> newest "*, asset references (`favicon.ico`, `icon.svg`, `apple-touch-icon.png`, `manifest.webmanifest`), and grid rule `.px { font-family:'Silkscreen',monospace;font-weight:400;letter-spacing:.02em }`.
4. **Interactive Detail & Feature Matrix (<section.wire> — `Posted by FWA winners >>> one post`)**:
   - Landmark `<section class="panel wire">` framing `Posted by FWA winners >>> one post per person pe` and `Winners post here. One item a day, newest first.` (*"Winners post here. One item a day, newest first."*) with `#0c0c0c` surface cards, `#ff9900` accents, and `.shell { max-width:940px;margin:0 auto;padding:8px }`.
5. **Colophon & Global Directory Footer (<footer.ticker> — `https://thefwa.net/`)**:
   - Landmark `<footer class="ticker">` anchoring `FWA Wire — winners' newswire` footer links (`older →`), copy *"Credits Daiki Fujita"*, and `#303030` structural dividers.
