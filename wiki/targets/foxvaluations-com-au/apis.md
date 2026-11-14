---
title: "APIs & Protocols: foxvaluations-com-au"
date: 2026-11-14
target: "[[overview|foxvaluations-com-au]]"
---

# Discovered APIs & Protocols: foxvaluations-com-au

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

