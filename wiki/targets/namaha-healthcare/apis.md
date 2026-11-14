---
title: "APIs & Protocols: namaha-healthcare"
date: 2026-11-14
target: "[[overview|namaha-healthcare]]"
---

# Discovered APIs & Protocols: namaha-healthcare

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/v1/components/verify` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /v1/components/verify
```json
{
  "type": "object",
  "properties": {
    "valid": {
      "type": "boolean"
    }
  }
}
```

