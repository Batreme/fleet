---
title: "APIs & Protocols: inks-studio"
date: 2026-11-14
target: "[[overview|inks-studio]]"
---

# Discovered APIs & Protocols: inks-studio

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/api/v2/client/ws` | `101` | REST endpoint |
| `POST` | `/` | `200` | REST endpoint |
| `GET` | `/api/trpc/features/map` | `200` | REST endpoint |
| `GET` | `/api/logo` | `200` | REST endpoint |
| `POST` | `/api/4509594045513728/envelope/` | `200` | REST endpoint |
| `GET` | `/api/trpc/timezones/cityTimezones` | `200` | REST endpoint |

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
### `GET` /api/trpc/features/map
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "result": {
        "type": "object",
        "properties": {
          "data": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `POST` /api/4509594045513728/envelope/
```json
{
  "type": "object",
  "properties": {}
}
```
### `GET` /api/trpc/timezones/cityTimezones
```json
{
  "type": "object",
  "properties": {
    "result": {
      "type": "object",
      "properties": {
        "data": {
          "type": "object",
          "properties": {
            "json": {
              "type": "any"
            }
          }
        }
      }
    }
  }
}
```

