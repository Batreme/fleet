---
title: "APIs & Protocols: www-raomuhammadhamza-tech"
date: 2026-11-14
target: "www-raomuhammadhamza-tech"
---

# Discovered APIs & Protocols: www-raomuhammadhamza-tech

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `POST` | `/api/presence` | `200` | REST endpoint |
| `GET` | `/api/now-playing` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `POST` /api/presence
```json
{
  "type": "object",
  "properties": {
    "state": {
      "type": "string"
    },
    "live": {
      "type": "number"
    },
    "total": {
      "type": "number"
    }
  }
}
```
### `GET` /api/now-playing
```json
{
  "type": "object",
  "properties": {
    "state": {
      "type": "string"
    },
    "title": {
      "type": "string"
    },
    "artist": {
      "type": "string"
    },
    "album": {
      "type": "string"
    },
    "art": {
      "type": "string"
    },
    "url": {
      "type": "string"
    },
    "preview": {
      "type": "string"
    },
    "at": {
      "type": "string"
    }
  }
}
```

