---
title: "APIs & Protocols: www-lapl-org"
date: 2026-11-14
target: "www-lapl-org"
---

# Discovered APIs & Protocols: www-lapl-org

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

