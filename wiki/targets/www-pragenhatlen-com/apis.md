---
title: "APIs & Protocols: www-pragenhatlen-com"
date: 2026-11-14
target: "[[overview|www-pragenhatlen-com]]"
---

# Discovered APIs & Protocols: www-pragenhatlen-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/test/register` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /test/register
```json
{
  "type": "object",
  "properties": {
    "uniqueId": {
      "type": "string"
    },
    "zoneList": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  }
}
```

