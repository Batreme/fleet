---
title: "UI & UX Architecture: www-discoverforgiveness-org"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: www-discoverforgiveness-org

## Overview & Design Identity
- **Target**: `www-discoverforgiveness-org` (**Discover Forgiveness · Templeton World Charity Foundation**)
- **Production URL**: [https://www.discoverforgiveness.org/](https://www.discoverforgiveness.org/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#fefefb` canvas, `#433f35` ink, `#0082f3` accent)
- **Summary**: Explore the transformative power of forgiveness at Discover Forgiveness. Our experts, from psychologists to spiritual leaders, offer insi...
- **Total Clean CSS Variables Extracted**: `28` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Queens`
- **Body Font Stack**: `Area Normal`
- **Monospace / Technical Font Stack**: `IBM Plex Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 89.8064px`, `line-height: 89.8064px`, `font-weight: 400`); rule `h1` (`font-size: 2em`)
- **Section Heading (`H2`)**: live computed `h3 (primary section heading)` (`font-size: 22.4516px`, `line-height: 31.4323px`, `font-weight: 700`); rule `h2` (`font-size: 32px`, `line-height: 36px`)
- **Body Copy**: live computed `body` (`font-size: 14.9677px`, `line-height: 22.4516px`, `font-weight: 400`); rule `body` (`font-size: 14px`, `line-height: 20px`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16.8387px`, `line-height: 18.5226px`, `font-weight: 800`); rule `small` (`font-size: 80%`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#fefefb` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#433f35` | live computed `body` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f0f0e5` | live computed `header` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#0082f3` | `.w-dropdown-link.w--current { color: #0082f3 }` |
| **Secondary / Muted Copy** | `#777269` | live computed `h2` `color` (`computed_styles.json`) |
| **Structural Hairline Border** | `#e2e2e2` | `blockquote { border-left: #e2e2e2 }` |
| **Variable Token (`--purple3`)** | `#6251d2` | `var(--purple3)` in `:root` |
| **Variable Token (`--tan5`)** | `#abaa9c` | `var(--tan5)` in `:root` |
| **Variable Token (`--tan`)** | `#fbfaf4` | `var(--tan)` in `:root` |
| **Variable Token (`--purple_transp`)** | `#8170f0` | `var(--purple_transp)` in `:root` |
| **Variable Token (`--tan4`)** | `#cbc8be` | `var(--tan4)` in `:root` |
| **Variable Token (`--tan3`)** | `#e2e2d5` | `var(--tan3)` in `:root` |
| **Variable Token (`--transparent`)** | `#0000` | `var(--transparent)` in `:root` |
| **Variable Token (`--purple1`)** | `#d8d8e9` | `var(--purple1)` in `:root` |
| **Variable Token (`--purple2`)** | `#bfbee0` | `var(--purple2)` in `:root` |
| **Variable Token (`--pear2`)** | `#d9e273` | `var(--pear2)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--off-white` | `#fefefb` | Canvas / Surface Token |
| `--dark` | `#433f35` | Canvas / Surface Token |
| `--purple3` | `#6251d2` | Color / Atmospheric Token |
| `--black` | `black` | Canvas / Surface Token |
| `--white` | `white` | Canvas / Surface Token |
| `--tan5` | `#abaa9c` | Color / Atmospheric Token |
| `--tan` | `#fbfaf4` | Color / Atmospheric Token |
| `--purple_transp` | `#8170f033` | Color / Atmospheric Token |
| `--dk-gray` | `#777269` | Color / Atmospheric Token |
| `--tan4` | `#cbc8be` | Color / Atmospheric Token |
| `--tan3` | `#e2e2d5` | Color / Atmospheric Token |
| `--tan2` | `#f0f0e5` | Color / Atmospheric Token |
| `--transparent` | `#0000` | Color / Atmospheric Token |
| `--purple1` | `#d8d8e9` | Color / Atmospheric Token |
| `--purple2` | `#bfbee0` | Color / Atmospheric Token |
| `--pear2` | `#d9e273` | Color / Atmospheric Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.section_header37> — `www-discoverforgiveness-org`)**:
   - Landmark `<header class="section_header37">` (`1320x900px`) hosting `Discover Forgiveness · Templeton Wor` navigation (`Educators · Faith Leaders · Anthropology · Art · Digital Landscape`), DOM attributes (`data-wf-domain="www.discoverforgivene..."`, `data-wf-page="64b81f977202559487efb8c0"`, `data-wf-site="64b81f977202559487efb843"`, `data-animation="default"`), and stylesheet rule `html { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; font-family:... }`.
2. **Hero Stage & Focal Lead (<section.section_layout134> — `Discover Forgiveness`)**:
   - Landmark `<section class="section_layout134">` presenting display lead `Discover Forgiveness` and copy excerpt *"Frontline workers include mental health professionals, faith lead"* over `#fefefb` canvas and `#433f35` ink.
3. **Primary Showcase & Content Grid (<section.section_layout349> — `What is Discover forgiveness?`)**:
   - Landmark `<section class="section_layout349">` rendering section `What is Discover forgiveness?` with copy *"In this section, you will find videos from past Forgiveness Forum"*, asset references (`cdn.prod.website-files.com`, `discover-forgiveness.webflow.shar...`, `fonts.googleapis.com`, `fonts.gstatic.com`), and grid rule `body { margin: 0; }`.
4. **Interactive Detail & Feature Matrix (<section.section_blog41> — `In this section, you will find vid`)**:
   - Landmark `<section class="section_blog41">` framing `In this section, you will find videos from past ` and `Forgiveness is a powerful tool for personal grow` (*"Forgiveness is a powerful tool for personal growth and community "*) with `#f0f0e5` surface cards, `#0082f3` accents, and `summary { display: block; }`.
5. **Colophon & Global Directory Footer (<footer.footer3_component> — `https://www.discoverforgiveness.org/`)**:
   - Landmark `<footer class="footer3_component">` anchoring `Discover Forgiveness · Templeton` footer links (`Educators · Faith Leaders · Anthropology · Art · Digital Landscape`), copy *"What makes forgiveness possible? Why is it so important? Is "*, and `#e2e2e2` structural dividers.
