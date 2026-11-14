---
title: "APIs & Protocols: davidcata-com_en-musica"
date: 2026-11-14
target: "[[overview|davidcata-com_en-musica]]"
---

# Discovered APIs & Protocols: davidcata-com_en-musica

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

