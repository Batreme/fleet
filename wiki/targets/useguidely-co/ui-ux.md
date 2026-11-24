---
title: "UI & UX Architecture: useguidely-co"
date: 2026-11-24
captured_at: 2026-11-24
status: analyzed
capture: live
capture_tier: tier1_fast
http_status: 200
---

# UI & UX Architecture: useguidely-co

## Overview & Design Identity
- **Target**: `useguidely-co` (**guidely - the hospitality of the future**)
- **Production URL**: [https://useguidely.co/](https://useguidely.co/)
- **Capture Provenance**: `capture: live` (`tier1_fast`, HTTP `200`, Desktop `1280×4140px`, Mobile `390×2616px`)
- **Visual Archetype**: Light-Substrate Editorial & Modular Grid System (`#ffffff` canvas, `#14110d` ink, `#9b7b4d` accent)
- **Summary**: A smart guest app that answers questions any hour, recommends what is good right now, plans the day and takes room orders, all from one l...
- **Total Clean CSS Variables Extracted**: `14` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `Geist`
- **Body Font Stack**: `Inter`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 87.84px`, `line-height: 74.664px`, `font-weight: 700`, `letter-spacing: -3.9528px`); CSS variables `--font-display: Georgia,"Times New Roman",serif`
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 60px`, `line-height: 55.2px`, `font-weight: 600`, `letter-spacing: -2.1px`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); CSS variables `--font-body: system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif`
- **Metadata & Labels**: live computed `nav/a` (`font-size: 14px`, `line-height: 20px`, `font-weight: 400`); CSS variables `--font-mono: ui-monospace,SFMono-Regular,Menlo,monospace`

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#ffffff` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#14110d` | live computed `h2` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#f4d5c2` | `.flood-cover { background: #f4d5c2 }` |
| **Interactive Accent / Highlight** | `#9b7b4d` | `var(--accent)` in `:root` |
| **Secondary / Muted Copy** | `#6f6f6f` | `var(--muted)` in `:root` |
| **Structural Hairline Border** | `#ebebeb` | `var(--line)` in `:root` (`rgba(0,0,0,.08)`) |
| **Variable Token (`--brand`)** | `#1f1d1a` | `var(--brand)` in `:root` |
| **Variable Token (`--ink`)** | `#222222` | `var(--ink)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--brand` | `#1f1d1a` | Brand / Palette Token |
| `--accent` | `#9b7b4d` | Brand / Palette Token |
| `--surface` | `#fff` | Canvas / Surface Token |
| `--ink` | `#222` | Typography Ink Token |
| `--muted` | `#6f6f6f` | Color / Atmospheric Token |
| `--line` | `rgba(0,0,0,.08)` | Color / Atmospheric Token |
| `--font-display` | `Georgia,"Times New Roman",serif` | Typography / Scale Token |
| `--vintage-filter` | `sepia(0.24) saturate(1.1) contrast(1.04) brightness(1.02)` | Design System Custom Token |
| `--hop` | `center 42%` | Dimension / Scale Token |
| `--font-name` | `system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif` | Typography / Scale Token |
| `--font-body` | `system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif` | Typography / Scale Token |
| `--font-mono` | `ui-monospace,SFMono-Regular,Menlo,monospace` | Typography / Scale Token |
| `--hero-ready` | `0` | Design System Custom Token |
| `--reveal-delay` | `0ms` | Motion / Easing Token |
| `--useguidely-co-bg` | `#ffffff` | Canvas Substrate (from live computed `body` `background-color` (`computed_styles.json`)) |
| `--useguidely-co-ink` | `#14110d` | Primary Typography Ink (computed-derived) |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.max-w-6xl> — `useguidely-co`)**:
   - Landmark `<header class="max-w-6xl py-5">` (`1152x80px`) hosting `guidely - the hospitality of the fut` navigation (`Home · About · Hotels & lodges · Features · Pricing`), DOM attributes (`data-precedence="next"`, `data-foldout-prefetch`, `data-spark="true"`, `data-reveal="stagger"`), and stylesheet rule `before { box-sizing:border-box;border:0 solid e5e7eb }`.
2. **Hero Stage & Focal Lead (<section.hero-sec> — `The smart app for your guests.`)**:
   - Landmark `<section class="hero-sec pt-3">` presenting display lead `The smart app for your guests.` and copy excerpt *"Check-in, Wi-Fi, house details, local recommendations, guest ques"* over `#ffffff` canvas and `#14110d` ink.
3. **Primary Showcase & Content Grid (<section.mt-12> — `Check-in, Wi-Fi, house details, lo`)**:
   - Landmark `<section class="mt-12">` rendering section `Check-in, Wi-Fi, house details, local recommenda` with copy *"Smart picks for right now"*, asset references (`logo.png`, `hero-cover-19.jpg`, `001c094435c96c6a.css`, `webpack-61e7ac9f112b97ad.js`), and grid rule `body { margin:0;line-height:inherit }`.
4. **Interactive Detail & Feature Matrix (<section.mx-auto> — `Smart picks for right now`)**:
   - Landmark `<section class="mx-auto px-6">` framing `Smart picks for right now` and `Experiences & activities` (*"Experiences & activities"*) with `#f4d5c2` surface cards, `#9b7b4d` accents, and `strong { font-weight:bolder }`.
5. **Colophon & Global Directory Footer (<footer.mt-16> — `https://useguidely.co/`)**:
   - Landmark `<footer class="mt-16">` anchoring `guidely - the hospitality of the` footer links (`Home · About · Hotels & lodges · Features · Pricing`), copy *"Room service ordering"*, and `#ebebeb` structural dividers.
