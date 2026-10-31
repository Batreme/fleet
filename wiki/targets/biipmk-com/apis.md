---
title: "APIs & Protocols: biipmk-com"
date: 2026-10-31
target: "[[overview|biipmk-com]]"
---

# Discovered APIs & Protocols: biipmk-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `POST` | `/anonymous` | `200` | REST endpoint |
| `GET` | `/auth/web/access-token` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /auth/web/access-token
```json
{
  "type": "object",
  "properties": {
    "message": {
      "type": "string"
    }
  }
}
```

