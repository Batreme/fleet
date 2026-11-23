---
title: "UI & UX Architecture: crun-ai"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: crun-ai

## Overview & Design Identity
- **Target**: `crun-ai` (**One API for All Top AI Models – Cost-Effective AI API · Crun**)
- **Production URL**: [https://crun.ai](https://crun.ai)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1440×2400px`, Mobile `390×2400px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#141414` ink, `#337ecc` accent)
- **Summary**: One API to access all top AI models—video, image, audio, and text. Fast integration, 30–70% cost savings, high-performance, and developer...
- **Total Clean CSS Variables Extracted**: `811` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Poppins`
- **Body Font Stack**: `Poppins`
- **Monospace / Technical Font Stack**: not declared in live computed styles (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 60px`, `line-height: 75px`, `font-weight: 700`, `letter-spacing: -1.5px`); CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: 1.11111`, `--text-5xl: 3rem`; rule `h1` (`font-size: 2em`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 36px`, `line-height: 40px`, `font-weight: 700`); CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: 1.33333`, `--text-3xl: 1.875rem`; rule `h2` (`font-size: 1.5em`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--el-font-size-base: 14px`, `--text-base: 1rem`, `--text-base--line-height: 1.5`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--el-font-size-small: 13px`, `--el-font-size-extra-small: 12px`, `--el-border-radius-small: 2px`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#141414` | live computed `body` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#e6e8eb` | `var(--bgColor-15)` in `:root` |
| **Interactive Accent / Highlight** | `#337ecc` | `var(--el-color-primary-dark-2)` in `:root` |
| **Secondary / Muted Copy** | `#8d9095` | `var(--el-text-color-placeholder)` in `:root` |
| **Structural Hairline Border** | `#d1d5db` | `var(--border-color)` in `:root` |
| **Variable Token (`--themeColor`)** | `#2563eb` | `var(--themeColor)` in `:root` |
| **Variable Token (`--themeColor-100`)** | `#f0f7ff` | `var(--themeColor-100)` in `:root` |
| **Variable Token (`--themeColor-200`)** | `#cce3ff` | `var(--themeColor-200)` in `:root` |
| **Variable Token (`--themeColor-300`)** | `#a3c9ff` | `var(--themeColor-300)` in `:root` |
| **Variable Token (`--themeColor-400`)** | `#7aadff` | `var(--themeColor-400)` in `:root` |
| **Variable Token (`--themeColor-500`)** | `#4f8af7` | `var(--themeColor-500)` in `:root` |
| **Variable Token (`--themeColor-700`)** | `#1647c4` | `var(--themeColor-700)` in `:root` |
| **Variable Token (`--themeColor-800`)** | `#092f9e` | `var(--themeColor-800)` in `:root` |
| **Variable Token (`--themeColor-900`)** | `#011b78` | `var(--themeColor-900)` in `:root` |
| **Variable Token (`--themeColor-1000`)** | `#000f52` | `var(--themeColor-1000)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--themeColor` | `#2563eb` | Brand / Palette Token |
| `--themeColor-100` | `#f0f7ff` | Brand / Palette Token |
| `--themeColor-200` | `#cce3ff` | Brand / Palette Token |
| `--themeColor-300` | `#a3c9ff` | Brand / Palette Token |
| `--themeColor-400` | `#7aadff` | Brand / Palette Token |
| `--themeColor-500` | `#4f8af7` | Brand / Palette Token |
| `--themeColor-600` | `#2563eb` | Brand / Palette Token |
| `--themeColor-700` | `#1647c4` | Brand / Palette Token |
| `--themeColor-800` | `#092f9e` | Brand / Palette Token |
| `--themeColor-900` | `#011b78` | Brand / Palette Token |
| `--themeColor-1000` | `#000f52` | Brand / Palette Token |
| `--themeColor-trans0` | `rgba(37,99,235,0)` | Brand / Palette Token |
| `--themeColor-trans3` | `rgba(37,99,235,.03)` | Brand / Palette Token |
| `--themeColor-trans4` | `rgba(37,99,235,.04)` | Brand / Palette Token |
| `--themeColor-trans5` | `rgba(37,99,235,.05)` | Brand / Palette Token |
| `--themeColor-trans6` | `rgba(37,99,235,.06)` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.left-0> — `crun-ai`)**:
   - Landmark `<header class="left-0 right-0">` (`1440x141px`) hosting `One API for All Top AI Models – Cost` navigation (`AI Agent NEW · Seedance 2.5 HOT · Wan 3.0 HOT · Kling 4.0 · Seedance 2.0`), DOM attributes (`data-gtag`, `data-v-88db481d`, `data-v-b2c0d9f1`, `data-v-2f8ea121`), and stylesheet rule `.el-notification.right { right:16px }`.
2. **Hero Stage & Focal Lead (<section.relative> — `Top AI Video, Image & Audio Models`)**:
   - Landmark `<section class="relative flex">` presenting display lead `Top AI Video, Image & Audio Models in One API` and copy excerpt *"Wan 3.0 Video 720p from just $0.058/sec"* over `#ffffff` canvas and `#141414` ink.
3. **Primary Showcase & Content Grid (<section.pt-10> — `Wan 3.0 Video 720p from just $0.05`)**:
   - Landmark `<section class="pt-10 relative">` rendering section `Wan 3.0 Video 720p from just $0.058/sec` with copy *"Empower AI video creation with high-quality visuals at just 58% o"*, asset references (`entry.BwM3ZDM3.css`, `el-notification.D1R47t8o.css`, `index.ByFwvLCV.css`, `advantagesGrid.o3VIx7N9.css`), and grid rule `cation .el-notification__closeBtn... { color:var(--el-notification-close-hover-color) }`.
4. **Interactive Detail & Feature Matrix (<section.pt-8> — `Empower AI video creation with hig`)**:
   - Landmark `<section class="pt-8 px-4">` framing `Empower AI video creation with high-quality visu` and `Video API Seedance 2.5 HOT Wan 3.0 HOT Seedance ` (*"Video API Seedance 2.5 HOT Wan 3.0 HOT Seedance 2.5 Flash NEW Kli"*) with `#e6e8eb` surface cards, `#337ecc` accents, and `notification .el-notification--pr... { --el-notification-icon-color:var(--el-color-primary);color:var(--el-noti... }`.
5. **Colophon & Global Directory Footer (<footer.right-0> — `https://crun.ai`)**:
   - Landmark `<footer class="right-0">` anchoring `One API for All Top AI Models – ` footer links (`AI Agent NEW · Seedance 2.5 HOT · Wan 3.0 HOT · Kling 4.0 · Seedance 2.0`), copy *"Seedance 2.5 Flash NEW"*, and `#d1d5db` structural dividers.
