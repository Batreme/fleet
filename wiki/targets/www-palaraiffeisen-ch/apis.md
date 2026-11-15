---
title: "APIs & Protocols: www-palaraiffeisen-ch"
date: 2026-11-14
target: "www-palaraiffeisen-ch"
---

# Discovered APIs & Protocols: www-palaraiffeisen-ch

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/_payload.json` | `200` | REST endpoint |
| `GET` | `/_i18n/9a2562b1/it/messages.json` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /_payload.json
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
### `GET` /_i18n/9a2562b1/it/messages.json
```json
{
  "type": "object",
  "properties": {
    "it": {
      "type": "object",
      "properties": {
        "aria": {
          "type": "object",
          "properties": {
            "pagination": {
              "type": "any"
            },
            "previous_page": {
              "type": "any"
            },
            "next_page": {
              "type": "any"
            },
            "go_to_page": {
              "type": "any"
            },
            "language_switcher": {
              "type": "any"
            },
            "logo_home": {
              "type": "any"
            }
          }
        },
        "breadcrumb": {
          "type": "object",
          "properties": {
            "items": {
              "type": "any"
            }
          }
        },
        "media": {
          "type": "object",
          "properties": {
            "banner_fullscreen": {
              "type": "any"
            }
          }
        },
        "error": {
          "type": "object",
          "properties": {
            "title": {
              "type": "any"
            },
            "subtitle": {
              "type": "any"
            },
            "cta": {
              "type": "any"
            }
          }
        },
        "seo": {
          "type": "object",
          "properties": {
            "home": {
              "type": "any"
            },
            "il-palazzetto": {
              "type": "any"
            },
            "organizza-un-evento": {
              "type": "any"
            },
            "societa-residenti": {
              "type": "any"
            },
            "news": {
              "type": "any"
            },
            "impressum": {
              "type": "any"
            },
            "privacy-policies": {
              "type": "any"
            }
          }
        }
      }
    }
  }
}
```

