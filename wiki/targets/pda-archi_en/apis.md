---
title: "APIs & Protocols: pda-archi_en"
date: 2026-11-14
target: "pda-archi_en"
---

# Discovered APIs & Protocols: pda-archi_en

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/_nuxt/builds/meta/a20c0d03-8d8b-4e9f-a527-e24301594e97.json` | `200` | REST endpoint |
| `GET` | `/_i18n/0ff7b472/en/messages.json` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /_nuxt/builds/meta/a20c0d03-8d8b-4e9f-a527-e24301594e97.json
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
          "properties": {
            "/sitemap.xml": {
              "type": "any"
            }
          }
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
### `GET` /_i18n/0ff7b472/en/messages.json
```json
{
  "type": "object",
  "properties": {
    "en": {
      "type": "object",
      "properties": {
        "header": {
          "type": "object",
          "properties": {
            "contact": {
              "type": "any"
            }
          }
        },
        "footer": {
          "type": "object",
          "properties": {
            "contact": {
              "type": "any"
            },
            "navigation": {
              "type": "any"
            },
            "socials": {
              "type": "any"
            },
            "newsletter": {
              "type": "any"
            }
          }
        },
        "modal": {
          "type": "object",
          "properties": {
            "contact": {
              "type": "any"
            },
            "address": {
              "type": "any"
            },
            "agency": {
              "type": "any"
            },
            "phone": {
              "type": "any"
            }
          }
        },
        "newsletter": {
          "type": "object",
          "properties": {
            "placeholder": {
              "type": "any"
            },
            "submit": {
              "type": "any"
            },
            "success": {
              "type": "any"
            },
            "alreadySubscribed": {
              "type": "any"
            },
            "error": {
              "type": "any"
            }
          }
        },
        "project": {
          "type": "object",
          "properties": {
            "status": {
              "type": "any"
            },
            "statusDelivered": {
              "type": "any"
            },
            "statusInProgress": {
              "type": "any"
            },
            "statusContest": {
              "type": "any"
            },
            "statusRnD": {
              "type": "any"
            },
            "related": {
              "type": "any"
            }
          }
        },
        "projects": {
          "type": "object",
          "properties": {
            "categories": {
              "type": "any"
            },
            "types": {
              "type": "any"
            },
            "grid": {
              "type": "any"
            },
            "list": {
              "type": "any"
            },
            "filters": {
              "type": "any"
            },
            "all": {
              "type": "any"
            }
          }
        },
        "a11y": {
          "type": "object",
          "properties": {
            "skipToContent": {
              "type": "any"
            },
            "home": {
              "type": "any"
            },
            "openMenu": {
              "type": "any"
            },
            "closeMenu": {
              "type": "any"
            },
            "prevTestimonial": {
              "type": "any"
            },
            "nextTestimonial": {
              "type": "any"
            },
            "openProject": {
              "type": "any"
            },
            "closeProject": {
              "type": "any"
            }
          }
        },
        "article": {
          "type": "object",
          "properties": {
            "read": {
              "type": "any"
            },
            "related": {
              "type": "any"
            },
            "back": {
              "type": "any"
            }
          }
        },
        "studio": {
          "type": "object",
          "properties": {
            "clients": {
              "type": "any"
            },
            "recognitions": {
              "type": "any"
            }
          }
        },
        "blog": {
          "type": "object",
          "properties": {
            "allCategory": {
              "type": "any"
            },
            "seeMore": {
              "type": "any"
            },
            "all": {
              "type": "any"
            },
            "recommendedRead": {
              "type": "any"
            }
          }
        },
        "actions": {
          "type": "object",
          "properties": {
            "discover": {
              "type": "any"
            },
            "readMore": {
              "type": "any"
            },
            "back": {
              "type": "any"
            },
            "seeAll": {
              "type": "any"
            },
            "contact": {
              "type": "any"
            },
            "prev": {
              "type": "any"
            },
            "next": {
              "type": "any"
            }
          }
        },
        "errors": {
          "type": "object",
          "properties": {
            "notFound": {
              "type": "any"
            },
            "notFoundMessage": {
              "type": "any"
            },
            "button": {
              "type": "any"
            }
          }
        },
        "meta": {
          "type": "object",
          "properties": {
            "siteLocale": {
              "type": "any"
            }
          }
        }
      }
    }
  }
}
```

