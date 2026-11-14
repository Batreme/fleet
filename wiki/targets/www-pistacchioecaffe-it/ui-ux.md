---
title: "UI & Design System: www-pistacchioecaffe-it"
date: 2026-11-14
target: "[[overview|www-pistacchioecaffe-it]]"
---

# UI Architecture & Design Tokens: www-pistacchioecaffe-it

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--top-left` | `before,.hint--top-right:before,.hint--top:before{border-top-` |
| `--top` | `before{margin-bottom:-11px` |
| `--top` | `after{-webkit-transform:translateX(-50%)` |
| `--top` | `hover:before{-webkit-transform:translateY(-8px)` |
| `--top` | `hover:after{-webkit-transform:translateX(-50%) translateY(-8` |
| `--bottom` | `after,.hint--bottom:before{top:100%` |
| `--bottom` | `before{margin-top:-11px` |
| `--bottom` | `after{-webkit-transform:translateX(-50%)` |
| `--bottom` | `hover:before{-webkit-transform:translateY(8px)` |
| `--bottom` | `hover:after{-webkit-transform:translateX(-50%) translateY(8p` |
| `--right` | `before{border-right-color:#383838` |
| `--right` | `after{margin-bottom:-14px}.hint--right:after,.hint--right:be` |
| `--right` | `hover:after,.hint--right:hover:before{-webkit-transform:tran` |
| `--left` | `before{border-left-color:#383838` |
| `--left` | `after{margin-bottom:-14px}.hint--left:after,.hint--left:befo` |
| `--left` | `hover:after,.hint--left:hover:before{-webkit-transform:trans` |
| `--top-left` | `after,.hint--top-left:before{bottom:100%` |
| `--top-left` | `before{margin-bottom:-11px` |
| `--top-left` | `after{-webkit-transform:translateX(-100%)` |
| `--top-left` | `hover:before{-webkit-transform:translateY(-8px)` |
| `--top-left` | `hover:after{-webkit-transform:translateX(-100%) translateY(-` |
| `--top-right` | `after,.hint--top-right:before{bottom:100%` |
| `--top-right` | `before{margin-bottom:-11px` |
| `--top-right` | `after{-webkit-transform:translateX(0)` |
| `--top-right` | `hover:after,.hint--top-right:hover:before{-webkit-transform:` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<nav>` | `site-navigation` | `main-navigation` |
| `<header>` | `masthead` | `site-header` |
| `<main>` | `primary` | `site-main` |
| `<footer>` | `colophon` | `site-footer contenitore-flex` |
