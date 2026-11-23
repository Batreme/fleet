---
title: "UI & UX Architecture: clinia-com"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: clinia-com

## Overview & Design Identity
- **Target**: `clinia-com` (**Patient Context for Healthcare AI · Clinia**)
- **Production URL**: [https://clinia.com](https://clinia.com)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Light-Gallery WebGL / Canvas Interactive Experience (`#ffffff` / `#785d24`)
- **Summary**: Fragmented health data breaks AI. Clinia reconciles it into graph-based context so your healthcare AI agents stay reliable and support op...
- **Total Clean CSS Variables Extracted**: `309` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `NaN Serf B Text`
- **Body Font Stack**: `Circular XX`
- **Monospace / Technical Font Stack**: `Circular XX Mono`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 56px`, `line-height: 61.6px`, `font-weight: 350`, `letter-spacing: -1.12px`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 40px`, `line-height: 44px`, `font-weight: 350`, `letter-spacing: -0.8px`); CSS variables `--has-subtitle: 0`, `--subtitle-height: 0px`; rule `h2` (`font-size: 22px`, `line-height: 1.1`)
- **Body Copy**: live computed `body` (`font-size: 18px`, `line-height: 22.5px`, `font-weight: 400`); CSS variables `--ff-body: Circular XX,sans-serif`, `--paragraph-height: 0px`; rule `p` (`font-size: inherit`, `font-weight: inherit`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 18px`, `line-height: 22.5px`, `font-weight: 400`); CSS variables `--ff-mono: Circular XX Mono,monospace`, `--hsf-default-field-label__font-family: Helvetica`, `--hsf-default-field-label__font-size: 1em`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#1a1a1e` | live computed `h1` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#ebf0f5` | `.hsfc-Step .hsfc-Step__Banner { background-color: #ebf0f5 }` |
| **Interactive Accent / Highlight** | `#785d24` | `.btn.--tag.--tag-noble { color: #785d24 }` |
| **Secondary / Muted Copy** | `#ff5c00` | `var(--color-secondary)` in `:root` |
| **Structural Hairline Border** | `#cccccc` | `var(--hsf-default-datepicker__border-color)` in `:root` |
| **Variable Token (`--color-black`)** | `#000000` | `var(--color-black)` in `:root` |
| **Variable Token (`--color-noble`)** | `#cca44f` | `var(--color-noble)` in `:root` |
| **Variable Token (`--color-trust`)** | `#95795c` | `var(--color-trust)` in `:root` |
| **Variable Token (`--color-trust-dark`)** | `#53402c` | `var(--color-trust-dark)` in `:root` |
| **Variable Token (`--color-remedy`)** | `#fcf8ef` | `var(--color-remedy)` in `:root` |
| **Variable Token (`--color-remedy-dark`)** | `#ecd9b9` | `var(--color-remedy-dark)` in `:root` |
| **Variable Token (`--color-remedy-medium`)** | `#f2eee5` | `var(--color-remedy-medium)` in `:root` |
| **Variable Token (`--color-remedy-light`)** | `#f9f7f2` | `var(--color-remedy-light)` in `:root` |
| **Variable Token (`--color-aura`)** | `#f7f1ff` | `var(--color-aura)` in `:root` |
| **Variable Token (`--color-aura-dark`)** | `#cabbdb` | `var(--color-aura-dark)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--color-transparent` | `transparent` | Brand / Palette Token |
| `--color-current` | `currentColor` | Brand / Palette Token |
| `--color-black` | `#000` | Canvas / Surface Token |
| `--color-white` | `#fff` | Canvas / Surface Token |
| `--color-primary` | `#1a1a1e` | Brand / Palette Token |
| `--color-secondary` | `#ff5c00` | Brand / Palette Token |
| `--color-vital` | `#ff5c00` | Brand / Palette Token |
| `--color-noble` | `#cca44f` | Brand / Palette Token |
| `--color-trust` | `#95795c` | Brand / Palette Token |
| `--color-trust-dark` | `#53402c` | Canvas / Surface Token |
| `--color-remedy` | `#fcf8ef` | Brand / Palette Token |
| `--color-remedy-dark` | `#ecd9b9` | Canvas / Surface Token |
| `--color-remedy-medium` | `#f2eee5` | Brand / Palette Token |
| `--color-remedy-light` | `#f9f7f2` | Canvas / Surface Token |
| `--color-aura` | `#f7f1ff` | Brand / Palette Token |
| `--color-aura-dark` | `#cabbdb` | Canvas / Surface Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.site-header> — `clinia-com`)**:
   - Landmark `<header class="site-header position-fixed">` (`1425x900px`) hosting `Patient Context for Healthcare AI · ` navigation (`Documentation · Changelog · Blog · Trust Center · About us`), DOM attributes (`data-env="production"`, `data-leadin-portal-id="8816539"`, `data-leadin-env="prod"`, `data-loader="hs-scriptloader"`), and stylesheet rule `webkit-scrollbar { display:none }`.
2. **Hero Stage & Focal Lead (<main.flex-grow-1> — `Health data, turned into a patient`)**:
   - Landmark `<main class="flex-grow-1">` presenting display lead `Health data, turned into a patient story` and copy excerpt *"PATIENT CONTEXT FOR HEALTHCARE AI"* over `#ffffff` canvas and `#1a1a1e` ink.
3. **Primary Showcase & Content Grid (<main.flex-grow-1:nth(2)> — `Engineered for AI agents in missio`)**:
   - Landmark `<main class="flex-grow-1">` rendering section `Engineered for AI agents in mission-critical heal...` with copy *"Patient Context for Healthcare AI"*, asset references (`humans.txt`, `xmlrpc.php`, `collectedforms.js`, `banner.js`), and grid rule `active { cursor:grabbing }`.
4. **Interactive Detail & Feature Matrix (<main.flex-grow-1:nth(3)> — `Health-native`)**:
   - Landmark `<main class="flex-grow-1">` framing `Health-native` and `Evaluation-first` (*"Assemble and serve the right context to your agents, so every run"*) with `#ebf0f5` surface cards, `#785d24` accents, and `blossom-dots>blossom-dot { display:none }`.
5. **Colophon & Global Directory Footer (<footer.site-footer> — `https://clinia.com`)**:
   - Landmark `<footer class="site-footer container-fluid">` anchoring `Patient Context for Healthcare A` footer links (`Documentation · Changelog · Blog · Trust Center · About us`), copy *"Built for frontier teams, trusted by ambitious builders"*, and `#cccccc` structural dividers.
