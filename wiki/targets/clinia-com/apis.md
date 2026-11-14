---
title: "APIs & Protocols: clinia-com"
date: 2026-11-14
target: "[[overview|clinia-com]]"
---

# Discovered APIs & Protocols: clinia-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `POST` | `/api/4511949891305472/envelope/` | `200` | REST endpoint |
| `GET` | `/api/v2/status.json` | `200` | REST endpoint |
| `GET` | `/cms-js-static/ex/js/island-runtime/v1/island-runtime.mjs` | `200` | REST endpoint |
| `POST` | `/api/4511949891305472/envelope/` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `POST` /api/4511949891305472/envelope/
```json
{
  "type": "object",
  "properties": {}
}
```
### `GET` /api/v2/status.json
```json
{
  "type": "object",
  "properties": {
    "page": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string"
        },
        "name": {
          "type": "string"
        },
        "url": {
          "type": "string"
        },
        "time_zone": {
          "type": "string"
        },
        "updated_at": {
          "type": "string"
        }
      }
    },
    "status": {
      "type": "object",
      "properties": {
        "indicator": {
          "type": "string"
        },
        "description": {
          "type": "string"
        }
      }
    }
  }
}
```
### `POST` /api/4511949891305472/envelope/
```json
{
  "type": "object",
  "properties": {
    "id": {
      "type": "string"
    }
  }
}
```

