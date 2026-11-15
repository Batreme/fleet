---
title: "APIs & Protocols: www-mynobs-co"
date: 2026-11-14
target: "www-mynobs-co"
---

# Discovered APIs & Protocols: www-mynobs-co

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/api/auth/me` | `200` | REST endpoint |
| `GET` | `/api/sentry-config` | `200` | REST endpoint |
| `GET` | `/api/announcement` | `200` | REST endpoint |
| `POST` | `/api/4512081515118592/envelope/` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /api/auth/me
```json
{
  "type": "object",
  "properties": {
    "ok": {
      "type": "boolean"
    },
    "user": {
      "type": "null"
    }
  }
}
```
### `GET` /api/sentry-config
```json
{
  "type": "object",
  "properties": {
    "ok": {
      "type": "boolean"
    },
    "dsn": {
      "type": "string"
    },
    "environment": {
      "type": "string"
    },
    "release": {
      "type": "string"
    }
  }
}
```
### `GET` /api/announcement
```json
{
  "type": "object",
  "properties": {
    "ok": {
      "type": "boolean"
    },
    "announcement": {
      "type": "object",
      "properties": {
        "text": {
          "type": "string"
        },
        "active": {
          "type": "boolean"
        },
        "revision": {
          "type": "string"
        }
      }
    }
  }
}
```
### `POST` /api/4512081515118592/envelope/
```json
{
  "type": "object",
  "properties": {}
}
```

