---
title: "APIs & Protocols: www-oceans-faith_moralcatch"
date: 2026-11-14
target: "[[overview|www-oceans-faith_moralcatch]]"
---

# Discovered APIs & Protocols: www-oceans-faith_moralcatch

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `POST` | `/api/census/render-batch` | `200` | REST endpoint |
| `GET` | `/api/popup-overlay/render` | `200` | REST endpoint |
| `POST` | `/api/census/overlay` | `200` | REST endpoint |
| `GET` | `/content/v2/namespaces/website/libraries/67c9e6cb13cc63773a42081f/assets/066f1bbd-73ed-4946-ba50-8ae777ed1476/moral-catch-w-opening.mp4` | `200` | REST endpoint |
| `GET` | `/content/v2/namespaces/website/libraries/67c9e6cb13cc63773a42081f/assets/ba25d242-4d3e-4a07-a39d-8505555c5083/moral-catch-w-saint-louis.mp4` | `200` | REST endpoint |
| `GET` | `/content/v2/namespaces/website/libraries/67c9e6cb13cc63773a42081f/assets/489bfa2b-5438-4532-b4ae-474edeb7ab95/moral-catch-w-catch.mp4` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `POST` /api/census/render-batch
```json
{
  "type": "object",
  "properties": {
    "success": {
      "type": "boolean"
    }
  }
}
```
### `GET` /api/popup-overlay/render
```json
{
  "type": "object",
  "properties": {
    "shouldDisplayOnPage": {
      "type": "boolean"
    },
    "renderedHtml": {
      "type": "string"
    }
  }
}
```
### `POST` /api/census/overlay
```json
{
  "type": "object",
  "properties": {
    "success": {
      "type": "boolean"
    }
  }
}
```

