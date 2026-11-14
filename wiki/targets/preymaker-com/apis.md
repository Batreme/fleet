---
title: "APIs & Protocols: preymaker-com"
date: 2026-11-14
target: "[[overview|preymaker-com]]"
---

# Discovered APIs & Protocols: preymaker-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/api/data` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /api/data
```json
{
  "type": "object",
  "properties": {
    "capabilities": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "title": {
            "type": "any"
          }
        }
      }
    },
    "footer": {
      "type": "object",
      "properties": {
        "footerEmail": {
          "type": "string"
        },
        "footerMedia": {
          "type": "object",
          "properties": {
            "_type": {
              "type": "any"
            },
            "mediaType": {
              "type": "any"
            },
            "responsiveImage": {
              "type": "any"
            },
            "responsiveVideo": {
              "type": "any"
            }
          }
        },
        "footerText": {
          "type": "string"
        }
      }
    },
    "industries": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "title": {
            "type": "any"
          }
        }
      }
    },
    "pagesThemes": {
      "type": "object",
      "properties": {
        "articlePages": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "capabilities": {
          "type": "string"
        },
        "capabilityPages": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "caseStudyOverview": {
          "type": "string"
        },
        "contact": {
          "type": "string"
        },
        "home": {
          "type": "string"
        },
        "legalPages": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "news": {
          "type": "string"
        },
        "peopleAndPartners": {
          "type": "string"
        },
        "technology": {
          "type": "string"
        },
        "workOverview": {
          "type": "string"
        },
        "workPages": {
          "type": "array",
          "items": {
            "type": "any"
          }
        }
      }
    },
    "partnersList": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "category": {
            "type": "any"
          },
          "partners": {
            "type": "any"
          }
        }
      }
    },
    "workTypes": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "title": {
            "type": "any"
          }
        }
      }
    }
  }
}
```

