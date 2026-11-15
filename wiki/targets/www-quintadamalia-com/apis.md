---
title: "APIs & Protocols: www-quintadamalia-com"
date: 2026-11-14
target: "www-quintadamalia-com"
---

# Discovered APIs & Protocols: www-quintadamalia-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/wp-json/contact-form-7/v1/contact-forms/709/feedback/schema` | `200` | REST endpoint |
| `GET` | `/wp-json/contact-form-7/v1/contact-forms/846/feedback/schema` | `200` | REST endpoint |
| `GET` | `/wp-json/contact-form-7/v1/contact-forms/709/refill` | `200` | REST endpoint |
| `GET` | `/wp-json/contact-form-7/v1/contact-forms/846/refill` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /wp-json/contact-form-7/v1/contact-forms/709/feedback/schema
```json
{
  "type": "object",
  "properties": {
    "version": {
      "type": "string"
    },
    "locale": {
      "type": "string"
    },
    "rules": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "rule": {
            "type": "any"
          },
          "field": {
            "type": "any"
          },
          "error": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `GET` /wp-json/contact-form-7/v1/contact-forms/846/feedback/schema
```json
{
  "type": "object",
  "properties": {
    "version": {
      "type": "string"
    },
    "locale": {
      "type": "string"
    },
    "rules": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "rule": {
            "type": "any"
          },
          "field": {
            "type": "any"
          },
          "error": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `GET` /wp-json/contact-form-7/v1/contact-forms/709/refill
```json
{
  "type": "array",
  "items": "any"
}
```
### `GET` /wp-json/contact-form-7/v1/contact-forms/846/refill
```json
{
  "type": "array",
  "items": "any"
}
```

