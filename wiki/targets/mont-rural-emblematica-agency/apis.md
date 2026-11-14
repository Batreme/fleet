---
title: "APIs & Protocols: mont-rural-emblematica-agency"
date: 2026-11-14
target: "[[overview|mont-rural-emblematica-agency]]"
---

# Discovered APIs & Protocols: mont-rural-emblematica-agency

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `POST` | `/api/discounts/v1/getactive/` | `200` | REST endpoint |
| `POST` | `/event/` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `POST` /api/discounts/v1/getactive/
```json
{
  "type": "object",
  "properties": {
    "error": {
      "type": "string"
    }
  }
}
```
### `POST` /event/
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

