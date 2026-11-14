---
title: "UI & Design System: giga-ai"
date: 2026-11-14
target: "[[overview|giga-ai]]"
---

# UI Architecture & Design Tokens: giga-ai

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--font-sans-source` | `"inter"}
@font-face{unicode-range:U+100-130,U+132-151,U+154-` |
| `--font-sans-ext-source` | `"interExt", "interExt Fallback"}
@font-face{font-family:geis` |
| `--font-mono-source` | `"geistMono", "geistMono Fallback"}
@font-face{font-family:ge` |
| `--font-geist-source` | `"geistSans", "geistSans Fallback"}
@font-face{font-family:ge` |
| `--font-pixel-line-source` | `"geistPixelLine", "geistPixelLine Fallback"}
@font-face{font` |
| `--sans` | `"Geist", system-ui, sans-serif` |
| `--mono` | `"Geist Mono", ui-monospace, monospace` |
| `--display` | `inter, interExt, "InterVariable", system-ui, sans-serif` |
| `--text` | `inter, interExt, "InterVariable", system-ui, sans-serif` |
| `--key-radius` | `8px` |
| `--key-face` | `linear-gradient(123.37deg, #3b3b3e 13.97%, #2a2a2d 87.5%)` |
| `--key-edge` | `#ffffff1f` |
| `--key-lit` | `inset 1px 1px 0 #ffffff14` |
| `--key-ink` | `#e8edefe0` |
| `--key-shadow` | `4px 6px 5px #00000080, 2px 4px 2.5px #0009` |
| `--key-shadow-down` | `1px 2px 2px #00000080, 1px 1px 1px #0009` |
| `--key-hover` | `brightness(1.12)` |
| `--key-ring` | `1.5px solid #e8edef99` |
| `--key-release` | `.15s cubic-bezier(.16,.84,.32,1)` |
| `--key-mono` | `400 11px/14px "Geist Mono", geistMono, monospace` |
| `--okey-face` | `linear-gradient(155.7deg, #f7732b 13.97%, #dd520c 87.5%)` |
| `--okey-edge` | `#ffd2b8b3` |
| `--okey-lit` | `inset 1px 1px 0 #ffffff40` |
| `--okey-ink` | `#fffffff2` |
| `--okey-cast` | `8px 12px 18px #00000059, 4px 6px 8px #00000073, 2px 4px 6px ` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `-` | `ft-nav` |
| `<nav>` | `-` | `ft-legal` |
| `<header>` | `bar` | `docked` |
| `<aside>` | `gigaNote` | `` |
| `<main>` | `main` | `` |
| `<footer>` | `footer` | `` |
