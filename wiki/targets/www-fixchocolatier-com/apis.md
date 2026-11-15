---
title: "APIs & Protocols: www-fixchocolatier-com"
date: 2026-11-14
target: "www-fixchocolatier-com"
---

# Discovered APIs & Protocols: www-fixchocolatier-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/api/form` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /api/form
```json
{
  "type": "object",
  "properties": {
    "data": {
      "type": "object",
      "properties": {
        "id": {
          "type": "number"
        },
        "documentId": {
          "type": "string"
        },
        "name": {
          "type": "string"
        },
        "formSlug": {
          "type": "string"
        },
        "success_action": {
          "type": "string"
        },
        "success_redirect": {
          "type": "null"
        },
        "success_message": {
          "type": "string"
        },
        "limit_published": {
          "type": "boolean"
        },
        "limit_on": {
          "type": "null"
        },
        "limit_action": {
          "type": "null"
        },
        "limit_redirect": {
          "type": "null"
        },
        "limit_message": {
          "type": "null"
        },
        "allowed_submissions": {
          "type": "number"
        },
        "createdAt": {
          "type": "string"
        },
        "updatedAt": {
          "type": "string"
        },
        "publishedAt": {
          "type": "string"
        },
        "locale": {
          "type": "string"
        },
        "description": {
          "type": "null"
        },
        "limit_field": {
          "type": "null"
        },
        "token": {
          "type": "string"
        }
      }
    },
    "meta": {
      "type": "object",
      "properties": {
        "csrfToken": {
          "type": "string"
        }
      }
    }
  }
}
```

