---
title: "APIs & Protocols: www-terakawaoffice-com_en"
date: 2026-11-14
target: "www-terakawaoffice-com_en"
---

# Discovered APIs & Protocols: www-terakawaoffice-com_en

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/cdn-cgi/speculation` | `200` | REST endpoint |
| `GET` | `/fx/rates.php` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /cdn-cgi/speculation
```json
{
  "type": "object",
  "properties": {
    "tag": {
      "type": "string"
    },
    "prefetch": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "eagerness": {
            "type": "any"
          },
          "source": {
            "type": "any"
          },
          "where": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `GET` /fx/rates.php
```json
{
  "type": "object",
  "properties": {
    "ok": {
      "type": "boolean"
    },
    "source": {
      "type": "string"
    },
    "published": {
      "type": "string"
    },
    "fetched_at": {
      "type": "string"
    },
    "rates": {
      "type": "object",
      "properties": {
        "AED": {
          "type": "number"
        },
        "AUD": {
          "type": "number"
        },
        "BRL": {
          "type": "number"
        },
        "CAD": {
          "type": "number"
        },
        "CHF": {
          "type": "number"
        },
        "CNY": {
          "type": "number"
        },
        "CZK": {
          "type": "number"
        },
        "DKK": {
          "type": "number"
        },
        "EUR": {
          "type": "number"
        },
        "GBP": {
          "type": "number"
        },
        "HKD": {
          "type": "number"
        },
        "HUF": {
          "type": "number"
        },
        "IDR": {
          "type": "number"
        },
        "ILS": {
          "type": "number"
        },
        "INR": {
          "type": "number"
        },
        "ISK": {
          "type": "number"
        },
        "KRW": {
          "type": "number"
        },
        "MXN": {
          "type": "number"
        },
        "MYR": {
          "type": "number"
        },
        "NOK": {
          "type": "number"
        }
      }
    },
    "stale": {
      "type": "boolean"
    }
  }
}
```

