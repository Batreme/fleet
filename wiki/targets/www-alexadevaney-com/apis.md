---
title: "APIs & Protocols: www-alexadevaney-com"
date: 2026-11-14
target: "[[overview|www-alexadevaney-com]]"
---

# Discovered APIs & Protocols: www-alexadevaney-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/api/locations` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /api/locations
```json
{
  "type": "object",
  "properties": {
    "cities": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "any"
          },
          "name": {
            "type": "any"
          },
          "state": {
            "type": "any"
          }
        }
      }
    },
    "neighborhoods": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "label": {
            "type": "any"
          },
          "value": {
            "type": "any"
          }
        }
      }
    }
  }
}
```

