# UI & UX Architecture: crun-ai

## Overview & Design Identity
- **Target**: `crun-ai` (**One API for All Top AI Models – Cost-Effective AI API · Crun**)
- **Production URL**: [https://crun.ai](https://crun.ai)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#409eff` canvas, `#18222b` ink, `#213d5b` accent)
- **Summary**: One API to access all top AI models—video, image, audio, and text. Fast integration, 30–70% cost savings, high-performance, and developer...
- **Total Clean CSS Variables Extracted**: `811` (curated ground-truth set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Poppins`
- **Body Font Stack**: `Crisp Noto Sans Regular`
- **Monospace / Technical Font Stack**: not declared in static CSS (uses primary stack / `ui-monospace`)
- **Hero Display (`H1`)**: CSS variables `--text-4xl: 2.25rem`, `--text-4xl--line-height: 1.11111`, `--text-5xl: 3rem`; rule `h1` (`font-size: 2em!important`)
- **Section Heading (`H2`)**: CSS variables `--text-2xl: 1.5rem`, `--text-2xl--line-height: 1.33333`, `--text-3xl: 1.875rem`; rule `h2` (`font-size: 1.5em!important`)
- **Body Copy**: CSS variables `--text-base: 1rem`, `--text-base--line-height: 1.5`, `--el-font-size-base: 14px`
- **Metadata & Labels**: CSS variables `--text-xs: .75rem`, `--text-xs--line-height: 1.33333`, `--text-sm: .875rem`

---

## Semantic Color System (Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted CSS Source / Selector |
|---|---|---|
| **Primary Canvas Substrate** | `#409eff` | `var(--el-color-primary)` in `:root` |
| **Primary Typography Ink** | `#3375b9` | `var(--el-color-primary-light-3)` in `:root` |
| **Elevated Surface / Card Substrate** | `#2a598a` | `var(--el-color-primary-light-5)` in `:root` |
| **Interactive Accent / Highlight** | `#213d5b` | `var(--el-color-primary-light-7)` in `:root` |
| **Secondary / Muted Copy** | `#1d3043` | `var(--el-color-primary-light-8)` in `:root` |
| **Structural Hairline Border** | `#18222b` | `var(--el-color-primary-light-9)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--el-notification-width` | `330px` | Layout / Spatial Grid Token |
| `--el-notification-padding` | `14px 26px 14px 13px` | Layout / Spatial Grid Token |
| `--el-notification-radius` | `8px` | Elevation / Border Token |
| `--el-notification-shadow` | `var(--el-box-shadow-light)` | Elevation / Border Token |
| `--el-notification-border-color` | `var(--el-border-color-lighter)` | Brand / Palette Token |
| `--el-notification-icon-size` | `24px` | Layout / Spatial Grid Token |
| `--el-notification-close-font-size` | `var(--el-message-close-size,16px)` | Typography / Scale Token |
| `--el-notification-group-margin-left` | `13px` | Layout / Spatial Grid Token |
| `--el-notification-group-margin-right` | `8px` | Layout / Spatial Grid Token |
| `--el-notification-content-font-size` | `var(--el-font-size-base)` | Typography / Scale Token |
| `--el-notification-content-color` | `var(--el-text-color-regular)` | Brand / Palette Token |
| `--el-notification-title-font-size` | `16px` | Typography / Scale Token |
| `--el-notification-title-color` | `var(--el-text-color-primary)` | Brand / Palette Token |
| `--el-notification-close-color` | `var(--el-text-color-secondary)` | Brand / Palette Token |
| `--el-notification-close-hover-color` | `var(--el-text-color-regular)` | Brand / Palette Token |
| `--el-notification-icon-color` | `var(--el-color-primary)` | Brand / Palette Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.fixed> — `crun-ai`)**:
   - Landmark `<header class="fixed left-0">` hosting `One API for All Top AI Models – Cost` navigation (`AI Agent NEW · Seedance 2.5 HOT · Kling 4.0 NEW · Seedance 2.0 · Seedance 2.0 Mini`), DOM attributes (`data-gtag`, `data-v-c988fe2b`, `data-v-b2c0d9f1`, `data-v-2f8ea121`), and stylesheet rule `.el-notification.right { right:16px }`.
2. **Hero Stage & Focal Lead (<section.relative> — `Top AI Video, Image & Audio Models`)**:
   - Landmark `<section class="relative flex">` presenting display lead `Top AI Video, Image & Audio Models in One API` and copy excerpt *"Seedance 2.0 Mini video from $0.008/sec. Built for AI comic serie"* over `#409eff` canvas and `#18222b` ink.
3. **Primary Showcase & Content Grid (<section.pt-10> — `Popular AI API Models`)**:
   - Landmark `<section class="pt-10 relative">` rendering section `Popular AI API Models` with copy *"Seedance 2.0 Mini video from $0.008/sec."*, asset references (`entry.C15VBcyN.css`, `el-notification.D1R47t8o.css`, `index.ByFwvLCV.css`, `advantagesGrid.o3VIx7N9.css`), and grid rule `cation .el-notification__closeBtn... { color:var(--el-notification-close-hover-color) }`.
4. **Interactive Detail & Feature Matrix (<section.px-4> — `Nano Banana 2.1`)**:
   - Landmark `<section class="px-4 pt-8">` framing `Nano Banana 2.1` and `Seedance 2.5` (*"Built for AI comic series and short videos, with cost-effective g"*) with `#2a598a` surface cards, `#213d5b` accents, and `notification .el-notification--pr... { --el-notification-icon-color:var(--el-color-primary);color:var(--el-noti... }`.
5. **Colophon & Global Directory Footer (<footer.right-0> — `https://crun.ai`)**:
   - Landmark `<footer class="right-0">` anchoring `One API for All Top AI Models – ` footer links (`AI Agent NEW · Seedance 2.5 HOT · Kling 4.0 NEW · Seedance 2.0 · Seedance 2.0 Mini`), copy *"Video API Seedance 2.5 HOT Kling 4.0 NEW Seedance 2.0 Seedan"*, and `#18222b` structural dividers.
