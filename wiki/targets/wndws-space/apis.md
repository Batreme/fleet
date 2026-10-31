---
title: "APIs & Protocols: wndws-space"
date: 2026-10-31
target: "[[overview|wndws-space]]"
---

# Discovered APIs & Protocols: wndws-space

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/api/windows` | `200` | REST endpoint |
| `GET` | `/_nuxt/builds/meta/07ecdace-b27c-471e-8120-907eb85e8299.json` | `200` | REST endpoint |
| `GET` | `/prelude/_payload.json` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /api/windows
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "id": {
        "type": "string"
      },
      "createdTime": {
        "type": "string"
      },
      "fields": {
        "type": "object",
        "properties": {
          "Submitted At": {
            "type": "any"
          },
          "Photo URL": {
            "type": "any"
          },
          "Name": {
            "type": "any"
          },
          "Photo": {
            "type": "any"
          },
          "Location": {
            "type": "any"
          },
          "Status": {
            "type": "any"
          },
          "Story": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `GET` /_nuxt/builds/meta/07ecdace-b27c-471e-8120-907eb85e8299.json
```json
{
  "type": "object",
  "properties": {
    "id": {
      "type": "string"
    },
    "timestamp": {
      "type": "number"
    },
    "prerendered": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  }
}
```
### `GET` /prelude/_payload.json
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "data": {
        "type": "number"
      },
      "prerenderedAt": {
        "type": "number"
      }
    }
  }
}
```

