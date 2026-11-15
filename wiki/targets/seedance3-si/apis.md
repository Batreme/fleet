---
title: "APIs & Protocols: seedance3-si"
date: 2026-11-14
target: "seedance3-si"
---

# Discovered APIs & Protocols: seedance3-si

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/api/get-user-credits` | `200` | REST endpoint |
| `GET` | `/api/auth/session` | `200` | REST endpoint |
| `GET` | `/api/auth/session` | `200` | REST endpoint |
| `GET` | `/v3/m-outer-0edadf75b42c6ef7240c043f3272f3f9.html` | `200` | REST endpoint |
| `GET` | `/v3/fingerprinted/js/m-outer-df5ee3b49f88025f22168cdfc5823764.js` | `200` | REST endpoint |
| `POST` | `/6` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /api/get-user-credits
```json
{
  "type": "object",
  "properties": {
    "code": {
      "type": "number"
    },
    "message": {
      "type": "string"
    },
    "data": {
      "type": "object",
      "properties": {
        "credits": {
          "type": "number"
        },
        "isLoggedIn": {
          "type": "boolean"
        },
        "userType": {
          "type": "string"
        },
        "isVip": {
          "type": "boolean"
        },
        "is_recharged": {
          "type": "null"
        },
        "hasActiveSubscription": {
          "type": "boolean"
        },
        "vipExpiresAt": {
          "type": "null"
        },
        "isPremiumYearly": {
          "type": "boolean"
        },
        "isYearlyMember": {
          "type": "boolean"
        }
      }
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
### `GET` /api/auth/session
```json
{
  "type": "null"
}
```
### `POST` /6
```json
{
  "type": "object",
  "properties": {
    "muid": {
      "type": "string"
    },
    "guid": {
      "type": "string"
    },
    "sid": {
      "type": "string"
    }
  }
}
```

