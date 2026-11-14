---
title: "APIs & Protocols: bespokegroup-io"
date: 2026-11-14
target: "[[overview|bespokegroup-io]]"
---

# Discovered APIs & Protocols: bespokegroup-io

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `POST` | `/` | `200` | REST endpoint |
| `GET` | `/api/v2/client/ws` | `101` | REST endpoint |

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

