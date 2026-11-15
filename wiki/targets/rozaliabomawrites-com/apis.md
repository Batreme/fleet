---
title: "APIs & Protocols: rozaliabomawrites-com"
date: 2026-11-14
target: "rozaliabomawrites-com"
---

# Discovered APIs & Protocols: rozaliabomawrites-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `POST` | `/rest/v1/rpc/get_sticker_settings` | `200` | REST endpoint |
| `GET` | `/rest/v1/posts` | `200` | REST endpoint |
| `GET` | `/rest/v1/tracks` | `200` | REST endpoint |
| `POST` | `/__l5e/trackevents` | `202` | REST endpoint |
| `POST` | `/__l5e/trackevents` | `202` | REST endpoint |
| `GET` | `/pagead/id` | `200` | REST endpoint |
| `POST` | `/__l5e/trackevents` | `202` | REST endpoint |
| `POST` | `/youtubei/v1/log_event` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `POST` /rest/v1/rpc/get_sticker_settings
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "sticker_key": {
        "type": "string"
      },
      "enabled": {
        "type": "boolean"
      }
    }
  }
}
```
### `GET` /rest/v1/posts
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "id": {
        "type": "string"
      },
      "title": {
        "type": "string"
      },
      "body": {
        "type": "string"
      },
      "image_url": {
        "type": "string"
      },
      "external_link": {
        "type": "null"
      },
      "created_at": {
        "type": "string"
      },
      "tags": {
        "type": "array",
        "items": {
          "type": "any"
        }
      }
    }
  }
}
```
### `GET` /rest/v1/tracks
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "id": {
        "type": "string"
      },
      "title": {
        "type": "string"
      },
      "artist": {
        "type": "string"
      },
      "yt_id": {
        "type": "string"
      }
    }
  }
}
```
### `POST` /__l5e/trackevents
```json
{
  "type": "object",
  "properties": {
    "accepted": {
      "type": "boolean"
    }
  }
}
```
### `POST` /__l5e/trackevents
```json
{
  "type": "object",
  "properties": {
    "accepted": {
      "type": "boolean"
    }
  }
}
```
### `POST` /__l5e/trackevents
```json
{
  "type": "object",
  "properties": {
    "accepted": {
      "type": "boolean"
    }
  }
}
```
### `POST` /youtubei/v1/log_event
```json
{
  "type": "object",
  "properties": {
    "responseContext": {
      "type": "object",
      "properties": {}
    }
  }
}
```

