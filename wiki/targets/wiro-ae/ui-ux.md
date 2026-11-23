---
title: "UI & UX Architecture: wiro-ae"
date: 2026-11-23
captured_at: 2026-11-23
status: analyzed
capture: live
capture_tier: tier2_webgl
http_status: 200
---

# UI & UX Architecture: wiro-ae

## Overview & Design Identity
- **Target**: `wiro-ae` (**Wiro · Operating System for All Agencies**)
- **Production URL**: [https://wiro.ae/](https://wiro.ae/)
- **Capture Provenance**: `capture: live` (`tier2_webgl`, HTTP `200`, Desktop `1440×900px`, Mobile `390×844px`)
- **Visual Archetype**: Dark-Substrate WebGL / Canvas Interactive Experience (`#000000` / `#efacd4`)
- **Summary**: Run your whole agency in one place: projects, clients, invoices, social scheduling, ads, influencers and PR. The agency operating system...
- **Total Clean CSS Variables Extracted**: `84` (curated live-grounded set below)

---

## Typography & Hierarchy
- **Display Font Stack**: `__bricolage_29b70e`
- **Body Font Stack**: `__dmSans_224c19`
- **Monospace / Technical Font Stack**: `SFMono-Regular`
- **Hero Display (`H1`)**: live computed `h1` (`font-size: 62px`, `line-height: 62px`, `font-weight: 700`); rule `h1` (`font-size: clamp(27px,4.4vw,62px)`, `line-height: 1`)
- **Section Heading (`H2`)**: live computed `h2` (`font-size: 158.4px`, `line-height: 148.896px`, `font-weight: 700`); rule `h2` (`font-size: clamp(82px,11vw,220px)`, `line-height: .94`)
- **Body Copy**: live computed `body` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`); rule `p` (`font-size: clamp(16px,1.2vw,19px)`, `line-height: 1.5`)
- **Metadata & Labels**: live computed `nav/a` (`font-size: 16px`, `line-height: 24px`, `font-weight: 400`)

---

## Semantic Color System (Live-Computed & Source-Grounded)
| Semantic Role | Ground-Truth Value | Extracted Live / CSS Source |
|---|---|---|
| **Primary Canvas Substrate** | `#000000` | live computed `body` `background-color` (`computed_styles.json`) |
| **Primary Typography Ink** | `#f6f0e4` | live computed `p` `color` (`computed_styles.json`) |
| **Elevated Surface / Card Substrate** | `#10100f` | live computed `button` `background-color` (`computed_styles.json`) |
| **Interactive Accent / Highlight** | `#efacd4` | `var(--c-inverse-accent)` in `:root` |
| **Secondary / Muted Copy** | `#b8b5ac` | `var(--c-inverse-muted)` in `:root` |
| **Structural Hairline Border** | `#222220` | `var(--c-inverse-border)` in `:root` |
| **Variable Token (`--wiro-canvas`)** | `#f6efe3` | `var(--wiro-canvas)` in `:root` |
| **Variable Token (`--wiro-surface-2`)** | `#ece5da` | `var(--wiro-surface-2)` in `:root` |
| **Variable Token (`--wiro-yellow`)** | `#f6d94e` | `var(--wiro-yellow)` in `:root` |
| **Variable Token (`--wiro-sage`)** | `#9caf63` | `var(--wiro-sage)` in `:root` |
| **Variable Token (`--wiro-blue`)** | `#a9c5e9` | `var(--wiro-blue)` in `:root` |

---

## Reverse-Engineered CSS Variables (Sanitized Ground Truth)
| Variable Name | Extracted Value | Semantic Role |
|---|---|---|
| `--font-heading` | `var(--font-bricolage),"Bricolage Grotesque",sans-serif` | Typography Ink Token |
| `--font-ui` | `var(--font-dmsans),"DM Sans",Arial,Helvetica,sans-serif` | Typography / Scale Token |
| `--solar-stroke-width` | `2.5` | Layout / Spatial Grid Token |
| `--wiro-ink` | `#10100f` | Typography Ink Token |
| `--wiro-muted` | `rgba(16,16,15,.52)` | Color / Atmospheric Token |
| `--wiro-canvas` | `#f6efe3` | Canvas / Surface Token |
| `--wiro-surface` | `#f6efe3` | Canvas / Surface Token |
| `--wiro-surface-2` | `#ece5da` | Canvas / Surface Token |
| `--wiro-border` | `rgba(16,16,15,.12)` | Elevation / Border Token |
| `--wiro-pink` | `#efacd4` | Typography Ink Token |
| `--wiro-yellow` | `#f6d94e` | Color / Atmospheric Token |
| `--wiro-sage` | `#9caf63` | Color / Atmospheric Token |
| `--wiro-blue` | `#a9c5e9` | Color / Atmospheric Token |
| `--wiro-radius-lg` | `18px` | Elevation / Border Token |
| `--wiro-radius-md` | `12px` | Elevation / Border Token |
| `--wiro-radius-sm` | `10px` | Elevation / Border Token |

---

## Structural DOM Landmarks (`dom.html`)
1. **Brand Header & Navigation Bar (<header.mkt-header> — `wiro-ae`)**:
   - Landmark `<header class="mkt-header">` (`1440x68px`) hosting `Wiro · Operating System for All Agen` navigation (`Platform · Influencer · Dubai and the UAE · Articles · For creators`), DOM attributes (`data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`, `data-precedence="next"`), and stylesheet rule `html { scroll-behavior:smooth }`.
2. **Hero Stage & Focal Lead (<section.wi> — `Organize Your Chaos`)**:
   - Landmark `<section class="wi">` presenting display lead `Organize Your Chaos` and copy excerpt *"The operating system for modern agencies."* over `#000000` canvas and `#f6f0e4` ink.
3. **Primary Showcase & Content Grid (<section.lp-hero> — `One system for every page your age`)**:
   - Landmark `<section class="lp-hero">` rendering section `One system for every page your agency runs.` with copy *"Fifteen modules, one shared record of the work. Nothing lives in "*, asset references (`intro-arrow.webp`, `intro-window-2.webp`, `logo-icon.svg`, `landscape-bg.webp`), and grid rule `.lp-page { position:relative;min-height:100vh;color:var(--lp-ink);font-family:var(-... }`.
4. **Interactive Detail & Feature Matrix (<section.lp-section> — `Projects`)**:
   - Landmark `<section class="lp-section lp-pages">` framing `Projects` and `Clients` (*"Progress 7 of 9 8 of 9"*) with `#10100f` surface cards, `#efacd4` accents, and `.lp-page strong { font-family:var(--lp-heading);font-weight:700;letter-spacing:0 }`.
5. **Colophon & Global Directory Footer (<footer.lp-footer> — `https://wiro.ae/`)**:
   - Landmark `<footer class="lp-footer lp-footer-scatter">` anchoring `Wiro · Operating System for All ` footer links (`Platform · Influencer · Dubai and the UAE · Articles · For creators`), copy *"Briefs, timelines, owners and approvals moving through one s"*, and `#222220` structural dividers.
