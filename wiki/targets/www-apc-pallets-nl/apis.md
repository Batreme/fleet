---
title: "APIs & Protocols: www-apc-pallets-nl"
date: 2026-11-14
target: "[[overview|www-apc-pallets-nl]]"
---

# Discovered APIs & Protocols: www-apc-pallets-nl

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/config/LI-6A4688394E530/` | `200` | REST endpoint |
| `GET` | `/v1/identify/LI-6A4688394E530` | `200` | REST endpoint |
| `POST` | `/com.snowplowanalytics.snowplow/tp2` | `200` | REST endpoint |
| `POST` | `/com.snowplowanalytics.snowplow/tp2` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /config/LI-6A4688394E530/
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "key": {
        "type": "string"
      },
      "config": {
        "type": "array",
        "items": "any"
      }
    }
  }
}
```
### `GET` /v1/identify/LI-6A4688394E530
```json
{
  "type": "array",
  "items": "any"
}
```

