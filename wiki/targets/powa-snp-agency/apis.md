---
title: "APIs & Protocols: powa-snp-agency"
date: 2026-11-14
target: "powa-snp-agency"
---

# Discovered APIs & Protocols: powa-snp-agency

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/_next/data/s9v-j03RuUBrH7ohF6iH8/index.json` | `200` | REST endpoint |
| `GET` | `/_next/data/s9v-j03RuUBrH7ohF6iH8/donate-&-create.json` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /_next/data/s9v-j03RuUBrH7ohF6iH8/index.json
```json
{
  "type": "object",
  "properties": {
    "pageProps": {
      "type": "object",
      "properties": {
        "seo": {
          "type": "object",
          "properties": {
            "title": {
              "type": "any"
            },
            "keywords": {
              "type": "any"
            },
            "description": {
              "type": "any"
            },
            "image": {
              "type": "any"
            }
          }
        },
        "cms": {
          "type": "object",
          "properties": {
            "homePage": {
              "type": "any"
            },
            "gallery": {
              "type": "any"
            },
            "donate": {
              "type": "any"
            },
            "preloader": {
              "type": "any"
            }
          }
        }
      }
    },
    "__N_SSG": {
      "type": "boolean"
    }
  }
}
```
### `GET` /_next/data/s9v-j03RuUBrH7ohF6iH8/donate-&-create.json
```json
{
  "type": "object",
  "properties": {
    "pageProps": {
      "type": "object",
      "properties": {
        "seo": {
          "type": "object",
          "properties": {
            "title": {
              "type": "any"
            },
            "keywords": {
              "type": "any"
            },
            "description": {
              "type": "any"
            },
            "image": {
              "type": "any"
            }
          }
        },
        "cms": {
          "type": "object",
          "properties": {
            "createScreen": {
              "type": "any"
            },
            "preloader": {
              "type": "any"
            },
            "donate": {
              "type": "any"
            }
          }
        }
      }
    },
    "__N_SSG": {
      "type": "boolean"
    }
  }
}
```

