---
title: "APIs & Protocols: dreams-paulvl-eu"
date: 2026-11-14
target: "[[overview|dreams-paulvl-eu]]"
---

# Discovered APIs & Protocols: dreams-paulvl-eu

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `POST` | `/api/send` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `POST` /api/send
```json
{
  "type": "object",
  "properties": {
    "cache": {
      "type": "string"
    },
    "sessionId": {
      "type": "string"
    },
    "visitId": {
      "type": "string"
    }
  }
}
```

