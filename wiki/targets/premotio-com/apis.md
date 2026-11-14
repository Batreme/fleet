---
title: "APIs & Protocols: premotio-com"
date: 2026-11-14
target: "[[overview|premotio-com]]"
---

# Discovered APIs & Protocols: premotio-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/_payload.json` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /_payload.json
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "data": {
        "type": "number"
      },
      "prerenderedAt": {
        "type": "number"
      }
    }
  }
}
```

