---
title: "APIs & Protocols: studyhall-design"
date: 2026-11-14
target: "[[overview|studyhall-design]]"
---

# Discovered APIs & Protocols: studyhall-design

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `POST` | `/api/workforce-weather` | `200` | REST endpoint |
| `GET` | `/api/sonos/now-playing` | `200` | REST endpoint |
| `GET` | `/v1/chunk/jjXTjwxtVHA702932UO4SozYLUUQmJy5yoS01roCU3EIN0002u3F3q46sUTHRDGg9y361jV02y1hmPp3jIJmEsRpW1g/18446744073709551615.m4s` | `206` | REST endpoint |
| `GET` | `/v1/chunk/jjXTjwxtVHA702932UO4SozYLUUQmJy5yoS01roCU3EIN0002u3F3q46sUTHRDGg9y361jV02y1hmPp3jIJmEsRpW1g/0.m4s` | `206` | REST endpoint |
| `GET` | `/v1/chunk/LuTtrMh79AZQgHzdmN1d17PO74rdzI01PyiIJuVwIPKb67WOQ4pWulUUe9WzEhEt7HN53Vwh00AtiQa9wvzdE5IdZ2mSViudAUYxmYA3m545U/18446744073709551615.m4s` | `206` | REST endpoint |
| `GET` | `/v1/chunk/LuTtrMh79AZQgHzdmN1d17PO74rdzI01PyiIJuVwIPKb67WOQ4pWulUUe9WzEhEt7HN53Vwh00AtiQa9wvzdE5IdZ2mSViudAUYxmYA3m545U/0.m4s` | `206` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `POST` /api/workforce-weather
```json
{
  "type": "object",
  "properties": {
    "fetchedAt": {
      "type": "string"
    },
    "locations": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "city": {
            "type": "any"
          },
          "timezone": {
            "type": "any"
          },
          "timezoneLabel": {
            "type": "any"
          },
          "query": {
            "type": "any"
          },
          "temperature": {
            "type": "any"
          },
          "unit": {
            "type": "any"
          },
          "condition": {
            "type": "any"
          },
          "conditionId": {
            "type": "any"
          },
          "description": {
            "type": "any"
          },
          "clockIcon": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `GET` /api/sonos/now-playing
```json
{
  "type": "object",
  "properties": {
    "playing": {
      "type": "boolean"
    },
    "title": {
      "type": "null"
    },
    "artist": {
      "type": "null"
    },
    "imageUrl": {
      "type": "null"
    },
    "groupName": {
      "type": "null"
    },
    "fetchedAt": {
      "type": "string"
    }
  }
}
```

