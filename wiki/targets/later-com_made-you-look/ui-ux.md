---
title: "UI & Design System: later-com_made-you-look"
date: 2026-11-14
target: "[[overview|later-com_made-you-look]]"
---

# UI Architecture & Design Tokens: later-com_made-you-look

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--clean-player` | `before{content:"•"` |
| `--style-transparent` | `hover{background-color:rgba(255,255,255,.2)}.ytp-ad-button-v` |
| `--style-filled` | `hover{background-color:#0556bf}.ytp-ad-button-vm--style-fill` |
| `--style-filled-white` | `hover{background-color:#d9d9d9}.ytp-ad-button-vm--style-fill` |
| `--style-filled-dark` | `hover{background-color:#65b8ff}.ytp-ad-button-vm--style-mono` |
| `--style-mono-filled` | `hover{background-color:#3f3f3f}.ytp-ad-button-vm--style-mono` |
| `--large` | `hover{background-color:rgba(0,0,0,.7)}.ytp-ad-avatar-lockup-` |
| `--large` | `hover{background-color:#65b8ff}.ytp-player-minimized .ytp-ad` |
| `--w2w-start-background-color` | `#000` |
| `--w2w-end-background-color` | `#000` |
| `--yt-slider-shape-gradient-percent` | `0` |
| `--progress-width` | `0px` |
| `--progress-left-buffer` | `0px` |
| `--progress-right-buffer` | `0px` |
| `--unified-seek-scrubber-pill-height` | `32px` |
| `--unified-seek-edge-padding` | `8px` |
| `--seek-scrubber-width-destination` | `0px` |
| `--unified-seek-morph-transition-ms` | `100ms` |
| `--scrubber-container-x` | `0px` |
| `--half-width` | `calc(var(--seek-scrubber-width-destination)*0.5)` |
| `--half-height` | `min(var(--half-width),calc(var(--unified-seek-scrubber-pill-` |
| `--unified-seek-bounce-scale` | `1.15` |
| `--unified-seek-offset-x` | `0px` |
| `--unified-seek-bounce-offset-x` | `0px}.ytp-unified-seek-active .ytp-decorated-scrubber-contain` |
| `--unified-seek-offset-x` | `calc(max(0px,
        var(--half-width) + var(--unified-seek` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<main>` | `-` | `` |
| `<dialog>` | `myl-drawer` | `_1T8tE` |
