---
title: "UI & Design System: matchball-today"
date: 2026-11-14
target: "[[overview|matchball-today]]"
---

# UI Architecture & Design Tokens: matchball-today

## 🎨 Design Tokens (CSS Variables)

| Token Name | Inferred Value |
|---|---|
| `--cabecera` | `calc(56px + var(--aviso-cookies,0px))}header.cabecera{paddin` |
| `--tinta` | `#121212` |
| `--papel` | `#fff` |
| `--superficie` | `#fff` |
| `--boton-gris` | `#efefea` |
| `--boton-gris-encima` | `#e4e4de` |
| `--gris` | `#5c5c57` |
| `--linea` | `#e2e2dc` |
| `--apagado` | `#deded8` |
| `--noche` | `#07090d` |
| `--fallo` | `#b3261e` |
| `--estudio` | `linear-gradient(180deg, #fff 0%, #f7f7f4 55%, #e9e9e4 100%)` |
| `--ancho` | `600px` |
| `--margen` | `16px` |
| `--cabecera` | `56px}*,:before,:after{box-sizing:border-box}html,body{backgr` |
| `--alto-juego` | `288px}.pantalla .tarjeta-flotante.controles{height:var(--alt` |
| `--panel` | `clamp(360px, 29vw, 440px)` |
| `--lado` | `clamp(48px, 5vw, 96px)}.cabecera{padding:0 24px}.portada{pad` |
| `--panel` | `clamp(280px, 40vw, 360px)` |
| `--panel-margen` | `max(12px, env(safe-area-inset-right))}.pastilla-meta{max-wid` |

---

## 🧱 Layout Primitives & Component Tree

| Primitive | ID | Classes / Selectors |
|---|---|---|
| `<main>` | `-` | `portada` |
