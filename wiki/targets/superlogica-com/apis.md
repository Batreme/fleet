---
title: "APIs & Protocols: superlogica-com"
date: 2026-11-14
target: "[[overview|superlogica-com]]"
---

# Discovered APIs & Protocols: superlogica-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/injector.js/v2/0157` | `200` | REST endpoint |
| `GET` | `/assets-site/page-data/app-data.json` | `200` | REST endpoint |
| `GET` | `/assets-site/page-data/index/page-data.json` | `200` | REST endpoint |
| `GET` | `/v1/config/7dbff80fa83c4bf99828909479b720ed` | `200` | REST endpoint |
| `GET` | `/assets-site/page-data/sq/d/1386545924.json` | `200` | REST endpoint |
| `GET` | `/assets-site/page-data/sq/d/1506924018.json` | `200` | REST endpoint |
| `GET` | `/assets-site/page-data/sq/d/1578440110.json` | `200` | REST endpoint |
| `GET` | `/assets-site/page-data/sq/d/1894217869.json` | `200` | REST endpoint |
| `GET` | `/assets-site/page-data/sq/d/762035779.json` | `200` | REST endpoint |
| `POST` | `/v1/ingest` | `200` | REST endpoint |
| `POST` | `/api/tag/get-consent` | `200` | REST endpoint |
| `GET` | `/v2/3453052/banner.js` | `200` | REST endpoint |
| `GET` | `/api/iab/vendor-list.json` | `200` | REST endpoint |
| `POST` | `/events/49ccf18e9d316b2c0f3db5c60b6a2332d880aa3b58f6dd689de623f93ebd10aa` | `200` | REST endpoint |
| `GET` | `/livechat-public/v1/message/public` | `200` | REST endpoint |
| `GET` | `/hs-script-loader-public/v2/config/pixels-and-events/json` | `200` | REST endpoint |
| `GET` | `/media/images/hero/card-novos-leads.json` | `200` | REST endpoint |
| `GET` | `/media/images/manual-para-inteligente/ilustracao.json` | `200` | REST endpoint |
| `POST` | `/events/49ccf18e9d316b2c0f3db5c60b6a2332d880aa3b58f6dd689de623f93ebd10aa` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /assets-site/page-data/app-data.json
```json
{
  "type": "object",
  "properties": {
    "webpackCompilationHash": {
      "type": "string"
    }
  }
}
```
### `GET` /assets-site/page-data/index/page-data.json
```json
{
  "type": "object",
  "properties": {
    "componentChunkName": {
      "type": "string"
    },
    "path": {
      "type": "string"
    },
    "result": {
      "type": "object",
      "properties": {
        "pageContext": {
          "type": "object",
          "properties": {
            "breadcrumb": {
              "type": "any"
            }
          }
        }
      }
    },
    "staticQueryHashes": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  }
}
```
### `GET` /v1/config/7dbff80fa83c4bf99828909479b720ed
```json
{
  "type": "object",
  "properties": {
    "pixelId": {
      "type": "string"
    },
    "aamFields": {
      "type": "array",
      "items": "any"
    },
    "cookieOptIn": {
      "type": "boolean"
    },
    "autoCaptureFields": {
      "type": "array",
      "items": "any"
    },
    "autoCaptureOptIn": {
      "type": "boolean"
    }
  }
}
```
### `GET` /assets-site/page-data/sq/d/1386545924.json
```json
{
  "type": "object",
  "properties": {
    "data": {
      "type": "object",
      "properties": {
        "allSubmenuJson": {
          "type": "object",
          "properties": {
            "nodes": {
              "type": "any"
            }
          }
        }
      }
    }
  }
}
```
### `GET` /assets-site/page-data/sq/d/1506924018.json
```json
{
  "type": "object",
  "properties": {
    "data": {
      "type": "object",
      "properties": {
        "allFooterJson": {
          "type": "object",
          "properties": {
            "nodes": {
              "type": "any"
            }
          }
        },
        "allJuridicJson": {
          "type": "object",
          "properties": {
            "nodes": {
              "type": "any"
            }
          }
        }
      }
    }
  }
}
```
### `GET` /assets-site/page-data/sq/d/1578440110.json
```json
{
  "type": "object",
  "properties": {
    "data": {
      "type": "object",
      "properties": {
        "site": {
          "type": "object",
          "properties": {
            "siteMetadata": {
              "type": "any"
            }
          }
        }
      }
    }
  }
}
```
### `GET` /assets-site/page-data/sq/d/1894217869.json
```json
{
  "type": "object",
  "properties": {
    "data": {
      "type": "object",
      "properties": {
        "allHeaderJson": {
          "type": "object",
          "properties": {
            "nodes": {
              "type": "any"
            }
          }
        }
      }
    }
  }
}
```
### `GET` /assets-site/page-data/sq/d/762035779.json
```json
{
  "type": "object",
  "properties": {
    "data": {
      "type": "object",
      "properties": {
        "allSocialJson": {
          "type": "object",
          "properties": {
            "nodes": {
              "type": "any"
            }
          }
        }
      }
    }
  }
}
```
### `POST` /v1/ingest
```json
{
  "type": "object",
  "properties": {
    "response": {
      "type": "string"
    }
  }
}
```

