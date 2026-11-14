---
title: "APIs & Protocols: earthwallet-com"
date: 2026-11-14
target: "[[overview|earthwallet-com]]"
---

# Discovered APIs & Protocols: earthwallet-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/assets/rockies.json` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /assets/rockies.json
```json
{
  "type": "object",
  "properties": {
    "latitude": {
      "type": "number"
    },
    "longitude": {
      "type": "number"
    },
    "spanKm": {
      "type": "number"
    },
    "resolution": {
      "type": "number"
    },
    "min": {
      "type": "number"
    },
    "max": {
      "type": "number"
    },
    "centerElevation": {
      "type": "number"
    }
  }
}
```

