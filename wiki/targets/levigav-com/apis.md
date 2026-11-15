---
title: "APIs & Protocols: levigav-com"
date: 2026-11-14
target: "levigav-com"
---

# Discovered APIs & Protocols: levigav-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/api/verse` | `200` | REST endpoint |
| `GET` | `/api/aim` | `200` | REST endpoint |
| `GET` | `/api/hearts` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /api/verse
```json
{
  "type": "object",
  "properties": {
    "day": {
      "type": "string"
    },
    "likes": {
      "type": "number"
    },
    "liked": {
      "type": "boolean"
    }
  }
}
```
### `GET` /api/aim
```json
{
  "type": "object",
  "properties": {
    "top": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "any"
          },
          "rating": {
            "type": "any"
          },
          "avg": {
            "type": "any"
          },
          "hits": {
            "type": "any"
          },
          "acc": {
            "type": "any"
          },
          "combo": {
            "type": "any"
          },
          "map": {
            "type": "any"
          },
          "at": {
            "type": "any"
          }
        }
      }
    },
    "total": {
      "type": "number"
    }
  }
}
```
### `GET` /api/hearts
```json
{
  "type": "object",
  "properties": {
    "hearts": {
      "type": "number"
    }
  }
}
```

