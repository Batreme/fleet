---
title: "UI & Design System: dark-moon-org"
date: 2026-11-14
target: "[[overview|dark-moon-org]]"
---

# UI Architecture & Design Tokens: dark-moon-org

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--ed-bg` | `#000` |
| `--ed-pale` | `#0b0d13` |
| `--ed-fg` | `#dceaf4` |
| `--ed-soft` | `#b9c7d6` |
| `--ed-mute` | `#8e9baa` |
| `--ed-line` | `rgba(220,234,244,0.16)` |
| `--ed-acc` | `#87bfff` |
| `--ed-title` | `var(--font-display),"Space Mono",monospace` |
| `--ed-head` | `var(--font-google-sans),var(--font-title),sans-serif` |
| `--ed-text` | `var(--font-poppins),sans-serif` |
| `--ed-ease` | `cubic-bezier(0.19,1,0.22,1)` |
| `--ed-line` | `rgba(220,234,244,0.22)` |
| `--ed-mute` | `#adc4e6}#m-platform.ed.ed-blue .kgrid .ic{color:#87bfff}.mla` |
| `--ed-fg` | `#0a2472` |
| `--ed-soft` | `#2a3f7a` |
| `--ed-mute` | `#3b4f86` |
| `--ed-line` | `rgba(10,36,114,0.18)` |
| `--ed-acc` | `#3b26cc` |
| `--ed-bg` | `#dceaf4}#m-agents.ed.ed-alice .chip{border-color:#0a2472` |
| `--font-title` | `var(--font-display)` |
| `--font-sans` | `"Space Mono",monospace}#m-remediation.ed{background:linear-g` |
| `--ed-line` | `rgba(10,36,114,0.2)}.mlab[data-art=b] #m-platform.ed>.wrap>.` |
| `--cq` | `0}.mlab[data-art=c] #m-platform.ed>.wrap>.chips{margin-top:1` |
| `--ink` | `#080a11` |
| `--deep` | `#0b1020` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `hidden items-center gap-0.5 lg:flex ml-1 xl:ml-5` |
| `<nav>` | `-` | `ml-3 hidden items-center` |
| `<nav>` | `-` | `w-full px-[calc(var(--dm-gutter)+var(--dm-inset))] flex-1 overflow-y-auto pb-10 pt-6` |
| `<nav>` | `-` | `rl__nav` |
| `<header>` | `-` | `fixed inset-x-0 top-0 z-50` |
| `<aside>` | `-` | `dm-sidebar rl` |
| `<main>` | `-` | `` |
| `<main>` | `-` | `dm-content` |
| `<footer>` | `-` | `relative bg-white text-black` |
| `<dialog>` | `-` | `sheet` |
| `<dialog>` | `-` | `sheet` |
| `<dialog>` | `-` | `sheet` |
| `<dialog>` | `-` | `sheet` |
| `<dialog>` | `-` | `sheet` |
| `<dialog>` | `-` | `sheet` |
