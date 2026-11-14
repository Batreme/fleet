---
title: "APIs & Protocols: noravale-framer-website"
date: 2026-11-14
target: "[[overview|noravale-framer-website]]"
---

# Discovered APIs & Protocols: noravale-framer-website

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

