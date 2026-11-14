---
title: "APIs & Protocols: www-thefriedegg-com"
date: 2026-11-14
target: "[[overview|www-thefriedegg-com]]"
---

# Discovered APIs & Protocols: www-thefriedegg-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/scripts/v1/memberstack.js` | `200` | REST endpoint |
| `GET` | `/swg/js/v1/publisher.js` | `200` | REST endpoint |
| `POST` | `/app-member` | `200` | REST endpoint |
| `GET` | `/df77045d` | `200` | REST endpoint |
| `POST` | `/events` | `200` | REST endpoint |
| `GET` | `/v2/48488577/banner.js` | `200` | REST endpoint |
| `GET` | `/api/home-events` | `200` | REST endpoint |
| `GET` | `/collections/new-arrivals/products.json` | `200` | REST endpoint |
| `GET` | `/hs-script-loader-public/v2/config/pixels-and-events/json` | `200` | REST endpoint |
| `GET` | `/collected-forms/v1/config/json` | `200` | REST endpoint |
| `GET` | `/web-interactives/public/v1/embed/combinedConfigs` | `200` | REST endpoint |
| `POST` | `/events` | `200` | REST endpoint |
| `GET` | `/embed/v3/form/48488577/616295f3-13c4-4fd9-8ddc-98cd3ab25c89/json` | `200` | REST endpoint |
| `GET` | `/embed/v3/form/48488577/616295f3-13c4-4fd9-8ddc-98cd3ab25c89/json` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `POST` /app-member
```json
{
  "type": "object",
  "properties": {
    "data": {
      "type": "object",
      "properties": {
        "app": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "mode": {
              "type": "any"
            },
            "plans": {
              "type": "any"
            },
            "contentGroups": {
              "type": "any"
            },
            "customFields": {
              "type": "any"
            },
            "allowMemberSelfDelete": {
              "type": "any"
            },
            "analyticsEnabled": {
              "type": "any"
            },
            "captchaRequired": {
              "type": "any"
            },
            "authProviders": {
              "type": "any"
            },
            "additionalAuthMethods": {
              "type": "any"
            },
            "ssoSignupButtonURL": {
              "type": "any"
            },
            "isPaid": {
              "type": "any"
            },
            "branding": {
              "type": "any"
            },
            "experiments": {
              "type": "any"
            }
          }
        },
        "member": {
          "type": "null"
        },
        "sessionData": {
          "type": "object",
          "properties": {
            "sessionId": {
              "type": "any"
            }
          }
        }
      }
    }
  }
}
```
### `GET` /df77045d
```json
{
  "type": "object",
  "properties": {
    "error": {
      "type": "boolean"
    },
    "statusCode": {
      "type": "number"
    },
    "code": {
      "type": "string"
    },
    "message": {
      "type": "string"
    },
    "site": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string"
        }
      }
    }
  }
}
```
### `GET` /api/home-events
```json
{
  "type": "object",
  "properties": {
    "events": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "any"
          },
          "url": {
            "type": "any"
          },
          "image": {
            "type": "any"
          },
          "date": {
            "type": "any"
          },
          "tag": {
            "type": "any"
          },
          "tag_url": {
            "type": "any"
          }
        }
      }
    },
    "more_url": {
      "type": "string"
    }
  }
}
```
### `GET` /collections/new-arrivals/products.json
```json
{
  "type": "object",
  "properties": {
    "products": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "any"
          },
          "title": {
            "type": "any"
          },
          "handle": {
            "type": "any"
          },
          "body_html": {
            "type": "any"
          },
          "published_at": {
            "type": "any"
          },
          "created_at": {
            "type": "any"
          },
          "updated_at": {
            "type": "any"
          },
          "vendor": {
            "type": "any"
          },
          "product_type": {
            "type": "any"
          },
          "tags": {
            "type": "any"
          },
          "variants": {
            "type": "any"
          },
          "images": {
            "type": "any"
          },
          "options": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `GET` /hs-script-loader-public/v2/config/pixels-and-events/json
```json
{
  "type": "object",
  "properties": {
    "pixels": {
      "type": "object",
      "properties": {
        "ADWORDS": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "FACEBOOK": {
          "type": "array",
          "items": {
            "type": "any"
          }
        }
      }
    },
    "enhancedConversionEventSettings": {
      "type": "object",
      "properties": {
        "FACEBOOK": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "ADWORDS": {
          "type": "array",
          "items": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `GET` /collected-forms/v1/config/json
```json
{
  "type": "object",
  "properties": {
    "portalId": {
      "type": "number"
    },
    "submissionsApiDomain": {
      "type": "string"
    },
    "reportScraperTest": {
      "type": "boolean"
    },
    "formCaptureEnabled": {
      "type": "boolean"
    },
    "token": {
      "type": "number"
    }
  }
}
```

