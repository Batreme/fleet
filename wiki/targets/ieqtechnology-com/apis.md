---
title: "APIs & Protocols: ieqtechnology-com"
date: 2026-11-14
target: "ieqtechnology-com"
---

# Discovered APIs & Protocols: ieqtechnology-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/captcha/v1/221126bfaff10f69f5e2c60a7ff42e4b9f16aed7/static/hcaptcha.html` | `200` | REST endpoint |
| `GET` | `/captcha/v1/221126bfaff10f69f5e2c60a7ff42e4b9f16aed7/static/hcaptcha.html` | `200` | REST endpoint |
| `POST` | `/checksiteconfig` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `POST` /checksiteconfig
```json
{
  "type": "object",
  "properties": {
    "features": {
      "type": "object",
      "properties": {
        "enc_get_req": {
          "type": "boolean"
        }
      }
    },
    "c": {
      "type": "object",
      "properties": {
        "type": {
          "type": "string"
        },
        "req": {
          "type": "string"
        },
        "sig": {
          "type": "string"
        },
        "kid": {
          "type": "string"
        }
      }
    },
    "pass": {
      "type": "boolean"
    }
  }
}
```

