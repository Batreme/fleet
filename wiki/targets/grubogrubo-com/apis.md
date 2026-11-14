---
title: "APIs & Protocols: grubogrubo-com"
date: 2026-11-14
target: "[[overview|grubogrubo-com]]"
---

# Discovered APIs & Protocols: grubogrubo-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/geometry.json` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /geometry.json
```json
{
  "type": "array",
  "items": {
    "type": "array",
    "items": {
      "type": "number"
    }
  }
}
```

