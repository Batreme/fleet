---
title: "APIs & Protocols: andreas-vision"
date: 2026-11-14
target: "[[overview|andreas-vision]]"
---

# Discovered APIs & Protocols: andreas-vision

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/api/where` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /api/where
```json
{
  "type": "object",
  "properties": {
    "city": {
      "type": "string"
    },
    "country": {
      "type": "string"
    },
    "at": {
      "type": "string"
    }
  }
}
```

