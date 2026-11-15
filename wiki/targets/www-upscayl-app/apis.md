---
title: "APIs & Protocols: www-upscayl-app"
date: 2026-11-14
target: "www-upscayl-app"
---

# Discovered APIs & Protocols: www-upscayl-app

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/api/auth/session` | `200` | REST endpoint |
| `GET` | `/api/guest/session` | `404` | REST endpoint |
| `GET` | `/api/auth/session` | `200` | REST endpoint |
| `POST` | `/api/experiments/free-upscaler` | `200` | REST endpoint |
| `GET` | `/getconfig/sodar` | `200` | REST endpoint |
| `GET` | `/gsi/status` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /api/auth/session
```json
{
  "type": "null"
}
```
### `GET` /api/guest/session
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
### `GET` /api/auth/session
```json
{
  "type": "null"
}
```
### `POST` /api/experiments/free-upscaler
```json
{
  "type": "object",
  "properties": {
    "variant": {
      "type": "string"
    },
    "tracked": {
      "type": "boolean"
    }
  }
}
```
### `GET` /getconfig/sodar
```json
{
  "type": "object",
  "properties": {
    "sodar_query_id": {
      "type": "string"
    },
    "injector_basename": {
      "type": "string"
    },
    "bg_hash_basename": {
      "type": "string"
    },
    "bg_binary": {
      "type": "string"
    },
    "rc_enable": {
      "type": "string"
    },
    "bg_snapshot_delay_ms": {
      "type": "string"
    },
    "is_gen_204": {
      "type": "string"
    }
  }
}
```

