---
title: "APIs & Protocols: crun-ai"
date: 2026-11-14
target: "crun-ai"
---

# Discovered APIs & Protocols: crun-ai

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/static/builds/meta/a4b17e47-d709-4c5d-979d-b017a331455a.json` | `200` | REST endpoint |
| `GET` | `/_i18n/e626a8c9/en/messages.json` | `200` | REST endpoint |
| `POST` | `/cdn-cgi/rum` | `204` | REST endpoint |
| `GET` | `/api/v1/common/last-announcement-date` | `200` | REST endpoint |
| `GET` | `/settings/website/e9d40bba-2fba-46de-bc0b-a9a50c9c8c0c/prelude/` | `200` | REST endpoint |
| `GET` | `/settings/website/e9d40bba-2fba-46de-bc0b-a9a50c9c8c0c/` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /static/builds/meta/a4b17e47-d709-4c5d-979d-b017a331455a.json
```json
{
  "type": "object",
  "properties": {
    "id": {
      "type": "string"
    },
    "timestamp": {
      "type": "number"
    },
    "matcher": {
      "type": "object",
      "properties": {
        "static": {
          "type": "object",
          "properties": {}
        },
        "wildcard": {
          "type": "object",
          "properties": {}
        },
        "dynamic": {
          "type": "object",
          "properties": {}
        }
      }
    },
    "prerendered": {
      "type": "array",
      "items": "any"
    }
  }
}
```
### `GET` /_i18n/e626a8c9/en/messages.json
```json
{
  "type": "object",
  "properties": {
    "en": {
      "type": "object",
      "properties": {
        "Models_Market": {
          "type": "string"
        },
        "AI_Tools": {
          "type": "string"
        },
        "AI_Effects": {
          "type": "string"
        },
        "Infinite_Canvas": {
          "type": "string"
        },
        "User_Guide": {
          "type": "string"
        },
        "purchase": {
          "type": "string"
        },
        "Pricing": {
          "type": "string"
        },
        "pricing_title": {
          "type": "string"
        },
        "pricing_unite": {
          "type": "string"
        },
        "API_Keys": {
          "type": "string"
        },
        "Billing": {
          "type": "string"
        },
        "API_Usage": {
          "type": "string"
        },
        "Logs": {
          "type": "string"
        },
        "Affiliate": {
          "type": "string"
        },
        "Please": {
          "type": "string"
        },
        "Document": {
          "type": "string"
        },
        "Settings": {
          "type": "string"
        },
        "Languages": {
          "type": "string"
        },
        "Example": {
          "type": "string"
        },
        "input_placeholder": {
          "type": "string"
        }
      }
    }
  }
}
```
### `GET` /api/v1/common/last-announcement-date
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
        "last_updated": {
          "type": "number"
        },
        "title": {
          "type": "string"
        },
        "title_zh": {
          "type": "string"
        },
        "change_type": {
          "type": "string"
        }
      }
    }
  }
}
```
### `GET` /settings/website/e9d40bba-2fba-46de-bc0b-a9a50c9c8c0c/prelude/
```json
{
  "type": "object",
  "properties": {
    "socket": {
      "type": "boolean"
    },
    "token": {
      "type": "string"
    },
    "buster": {
      "type": "number"
    },
    "endpoints": {
      "type": "object",
      "properties": {
        "socket": {
          "type": "object",
          "properties": {
            "client": {
              "type": "any"
            },
            "stream": {
              "type": "any"
            }
          }
        },
        "rescue": {
          "type": "object",
          "properties": {
            "socket": {
              "type": "any"
            }
          }
        }
      }
    }
  }
}
```
### `GET` /settings/website/e9d40bba-2fba-46de-bc0b-a9a50c9c8c0c/
```json
{
  "type": "object",
  "properties": {
    "website": {
      "type": "string"
    },
    "domain": {
      "type": "string"
    },
    "mailer": {
      "type": "string"
    },
    "settings": {
      "type": "object",
      "properties": {
        "logo": {
          "type": "string"
        },
        "audit_log": {
          "type": "boolean"
        },
        "rating": {
          "type": "boolean"
        },
        "transcript": {
          "type": "boolean"
        },
        "enrich": {
          "type": "boolean"
        },
        "junk_filter": {
          "type": "boolean"
        },
        "tile": {
          "type": "string"
        },
        "wait_game": {
          "type": "boolean"
        },
        "website_logo": {
          "type": "boolean"
        },
        "last_operator_face": {
          "type": "boolean"
        },
        "ongoing_operator_face": {
          "type": "boolean"
        },
        "activity_metrics": {
          "type": "boolean"
        },
        "operator_privacy": {
          "type": "boolean"
        },
        "availability_tooltip": {
          "type": "boolean"
        },
        "hide_vacation": {
          "type": "boolean"
        },
        "hide_on_away": {
          "type": "boolean"
        },
        "hide_on_mobile": {
          "type": "boolean"
        },
        "position_reverse": {
          "type": "boolean"
        },
        "email_visitors": {
          "type": "boolean"
        },
        "phone_visitors": {
          "type": "boolean"
        }
      }
    },
    "operators": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "user_id": {
            "type": "any"
          },
          "avatar": {
            "type": "any"
          },
          "nickname": {
            "type": "any"
          },
          "timestamp": {
            "type": "any"
          }
        }
      }
    },
    "plugins": {
      "type": "object",
      "properties": {}
    },
    "online": {
      "type": "boolean"
    },
    "trial": {
      "type": "boolean"
    },
    "overlay": {
      "type": "null"
    },
    "channels": {
      "type": "object",
      "properties": {
        "email": {
          "type": "string"
        }
      }
    }
  }
}
```

