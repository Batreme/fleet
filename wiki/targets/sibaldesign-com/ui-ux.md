---
title: "UI & Design System: sibaldesign-com"
date: 2026-11-14
target: "[[overview|sibaldesign-com]]"
---

# UI Architecture & Design Tokens: sibaldesign-com

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--ink-000` | `#04060b` |
| `--ink-100` | `#080c15` |
| `--ink-200` | `#0d1320` |
| `--ink-300` | `#131b2b` |
| `--panel` | `rgba(20,27,42,.66)` |
| `--panel-hi` | `rgba(30,40,60,.72)` |
| `--line` | `#232e45` |
| `--line-hi` | `#33415f` |
| `--dim` | `#7f90b4` |
| `--mid` | `#a3b4d4` |
| `--fg` | `#c3d0e8` |
| `--white` | `#eaf1ff` |
| `--accent` | `#5fe0ff` |
| `--flash` | `#7ce9ff` |
| `--accent-lo` | `rgba(95,224,255,.14)` |
| `--mono` | `"JetBrains Mono",ui-monospace,SFMono-Regular,Menlo,monospace` |
| `--sans` | `"Chakra Petch",system-ui,-apple-system,sans-serif` |
| `--gut` | `clamp(16px,3.2vw,44px)` |
| `--max` | `1200px` |
| `--ease` | `cubic-bezier(.16,1,.3,1)` |
| `--ease-io` | `cubic-bezier(.65,0,.35,1)}*,*:before,*:after{box-sizing:bord` |
| `--back` | `clamp(40px,8.6vw,150px)` |
| `--lines` | `1` |
| `--cycle` | `.26s` |
| `--cols` | `6` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `nav__links` |
| `<nav>` | `drawer` | `drawer` |
| `<header>` | `-` | `nav` |
| `<main>` | `top` | `` |
| `<footer>` | `-` | `foot` |
