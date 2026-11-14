---
title: "APIs & Protocols: bybang-co"
date: 2026-11-14
target: "[[overview|bybang-co]]"
---

# Discovered APIs & Protocols: bybang-co

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/api/content` | `200` | REST endpoint |
| `GET` | `/api/session` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /api/content
```json
{
  "type": "object",
  "properties": {
    "content": {
      "type": "object",
      "properties": {
        "siteSettings": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "navContactLabel": {
              "type": "any"
            },
            "navProjectsLabel": {
              "type": "any"
            },
            "navAboutLabel": {
              "type": "any"
            },
            "contactEmail": {
              "type": "any"
            },
            "ctaLabel": {
              "type": "any"
            },
            "clockLabel": {
              "type": "any"
            }
          }
        },
        "homeIntro": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "body": {
              "type": "any"
            },
            "featuredImages": {
              "type": "any"
            }
          }
        },
        "aboutPage": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "title": {
              "type": "any"
            },
            "body": {
              "type": "any"
            },
            "leadImage": {
              "type": "any"
            },
            "secondaryImages": {
              "type": "any"
            },
            "teamMembers": {
              "type": "any"
            },
            "galleryItems": {
              "type": "any"
            }
          }
        },
        "projects": {
          "type": "array",
          "items": {
            "type": "any"
          }
        }
      }
    },
    "mode": {
      "type": "string"
    },
    "stage": {
      "type": "string"
    }
  }
}
```
### `GET` /api/session
```json
{
  "type": "object",
  "properties": {
    "available": {
      "type": "boolean"
    },
    "authenticated": {
      "type": "boolean"
    }
  }
}
```

