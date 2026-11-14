---
title: "APIs & Protocols: jimo-ai_product-ai"
date: 2026-11-14
target: "[[overview|jimo-ai_product-ai]]"
---

# Discovered APIs & Protocols: jimo-ai_product-ai

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/api/v2/client/ws` | `101` | REST endpoint |
| `POST` | `/` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `POST` /
```json
{
  "type": "object",
  "properties": {
    "content_uuid": {
      "type": "string"
    },
    "success": {
      "type": "boolean"
    }
  }
}
```

