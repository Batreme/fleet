---
title: "UI & UX Architecture: peabodyhouse-com"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: peabodyhouse-com

## Overview & Design Identity
- **Target**: `peabodyhouse-com` (**Peabody House • Digital Brand World Implementation Studio**)
- **Production URL**: [https://peabodyhouse.com](https://peabodyhouse.com)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×1656px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#faf6f3` / `#0000ff`)
- **Summary**: Peabody House is a Milwaukee-based digital studio that turns brand aspirations into elevated, scalable design systems. Led by human expre...
- **Total Clean CSS Variables Extracted**: `220` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Peabody House`
- **Body Font Stack**: `PP Neue Montreal`
- **Monospace / Technical Font Stack**: `SpotifyMixMono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 68px`, `line-height: 76.5px`, `font-weight: 400`); CSS variables `--text-link-standalone-display: block`, `--encore-overlay-trigger-display: block`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 60.48px`, `line-height: 63.504px`, `font-weight: 400`); rule `,.h2` (`font-size: clamp(2.0257rem,1.4626rem + 2...`, `line-height: 1.125`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--font-body: "PP Neue Montreal", sans-serif`, `--font-size-base: 16px`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--encore-text-size-smaller-3: 0.625rem`, `--encore-text-size-smaller-2: 0.75rem`, `--encore-text-size-smaller: 0.875rem`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#faf6f3` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#26211e` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#c5f0c9` | `var(--encore-verified-badge-background)` in `:root` |
| **Interactive Accent / Highlight** | `#0000ff` | `.cta:hover .cta-line { color: blue }` (`#0000ff`) |
| **Secondary / Muted Copy** | `#f3727f` | `var(--text-negative)` in `:root` |
| **Structural Hairline Border** | `#008080` | `.cta:before { border-top-color: #008080 }` |
| **Variable Token (`--color-accent`)** | `#dc942f` | `var(--color-accent)` in `:root` |
| **Variable Token (`--color-blue`)** | `#517bb3` | `var(--color-blue)` in `:root` |
| **Variable Token (`--color-teal`)** | `#71c7b7` | `var(--color-teal)` in `:root` |
| **Variable Token (`--color-red`)** | `#a24250` | `var(--color-red)` in `:root` |
| **Variable Token (`--color-green`)** | `#455330` | `var(--color-green)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-primary` | `#26211E` | Brand / Palette Token |
| `--color-secondary` | `#FAF6F3` | Brand / Palette Token |
| `--color-accent` | `#DC942F` | Brand / Palette Token |
| `--color-background` | `#FAF6F3` | Canvas / Surface Token |
| `--color-text` | `#26211E` | Typography Ink Token |
| `--color-white` | `#FAF6F3` | Canvas / Surface Token |
| `--color-black` | `#26211E` | Canvas / Surface Token |
| `--color-black-20` | `rgba(38, 33, 30, .2)` | Canvas / Surface Token |
| `--color-orange` | `#DC942F` | Brand / Palette Token |
| `--color-blue` | `#517BB3` | Brand / Palette Token |
| `--color-teal` | `#71C7B7` | Brand / Palette Token |
| `--color-red` | `#A24250` | Brand / Palette Token |
| `--color-green` | `#455330` | Brand / Palette Token |
| `--font-heading` | `"Peabody House", sans-serif` | Typography Ink Token |
| `--font-body` | `"PP Neue Montreal", sans-serif` | Typography / Scale Token |
| `--font-size-base` | `16px` | Typography / Scale Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.svelte-126o6dr> — `peabodyhouse-com`)**:
   - Landmark `<header class="svelte-126o6dr">` (`1436x28px`) hosting `Peabody House • Digital Brand World ` navigation (`Expertise Expertise · Works Works · Studio Studio · Contact Contact · Expertise`), DOM attributes (`data-sveltekit-preload-data="hover"`, `data-text="Peabody House"`, `data-text="Expertise"`, `data-text="Works"`), and stylesheet rule `.search.svelte-1w6by2l { position:relative;display:inline-flex;align-items:center }`.
2. **Hero Stage & Focal Lead (<section.hero> — `Peabody House is a digital brand w`)**:
   - Landmark `<section class="hero svelte-x35jl1">` presenting display lead `Peabody House is a digital brand world implementa...` and copy excerpt *"Peabody House is a digital brand world implementation studio."* over `#faf6f3` canvas and `#26211e` ink.
3. **Primary Showcase & Content Grid (<section.subhero> — `The ordeal of being perceived.`)**:
   - Landmark `<section class="subhero svelte-x35jl1">` rendering section `The ordeal of being perceived.` with copy *"We future-proof brand aspirations into elevated, scalable design "*, asset references (`favicon.ico`, `favicon.svg`, `apple-touch-icon.png`, `site.webmanifest`), and grid rule `.search-panel.is-open.svelte-1w6by2l { opacity:1;visibility:visible;pointer-events:auto;transform:none }`.
4. **Interactive Detail & Feature Matrix (<section.service-cards> — `What does Peabody House do?`)**:
   - Landmark `<section class="service-cards svelte-1cpv9bu">` framing `What does Peabody House do?` and `Technical Implementation` (*"Your audience is more perceptible than you may think. How you aff"*) with `#c5f0c9` surface cards, `#0000ff` accents, and `arch-panel.is-positioned.svelte-1... { position:fixed;top:var(--panel-y);left:var(--panel-x);right:auto }`.
5. **Colophon & Global Directory Footer (<footer.js-line-displacement> — `https://peabodyhouse.com`)**:
   - Landmark `<footer class="js-line-displacement svelte-352yma">` anchoring `Peabody House • Digital Brand Wo` footer links (`Expertise Expertise · Works Works · Studio Studio · Contact Contact · Expertise`), copy *"People are more sensitive than ever to AI in 2026, and AI-pr"*, and `#008080` structural dividers.
