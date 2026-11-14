---
title: "APIs & Protocols: clipdance-ai"
date: 2026-11-14
target: "[[overview|clipdance-ai]]"
---

# Discovered APIs & Protocols: clipdance-ai

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/api/auth/get-session` | `200` | REST endpoint |
| `GET` | `/pixel-config/v1/5WVMdMpzG6jAb6C87jzL8A.json` | `200` | REST endpoint |
| `POST` | `/v1/sdk/events` | `202` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /api/auth/get-session
```json
{
  "type": "null"
}
```
### `GET` /pixel-config/v1/5WVMdMpzG6jAb6C87jzL8A.json
```json
{
  "type": "object",
  "properties": {
    "automatic_advanced_matching_enabled": {
      "type": "boolean"
    }
  }
}
```

