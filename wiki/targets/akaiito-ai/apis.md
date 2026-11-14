---
title: "APIs & Protocols: akaiito-ai"
date: 2026-11-14
target: "[[overview|akaiito-ai]]"
---

# Discovered APIs & Protocols: akaiito-ai

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/api/geo` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /api/geo
```json
{
  "type": "object",
  "properties": {
    "city": {
      "type": "string"
    },
    "region": {
      "type": "string"
    },
    "country": {
      "type": "string"
    },
    "tz": {
      "type": "string"
    }
  }
}
```

