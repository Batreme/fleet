---
title: "APIs & Protocols: sinedogma-com-tr"
date: 2026-11-14
target: "sinedogma-com-tr"
---

# Discovered APIs & Protocols: sinedogma-com-tr

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/.netlify/functions/content` | `200` | REST endpoint |
| `GET` | `/pagead/id` | `200` | REST endpoint |
| `POST` | `/$rpc/google.internal.waa.v1.Waa/GenerateIT` | `200` | REST endpoint |
| `GET` | `/api/geo` | `200` | REST endpoint |
| `POST` | `/youtubei/v1/log_event` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /.netlify/functions/content
```json
{
  "type": "object",
  "properties": {
    "schemaVersion": {
      "type": "number"
    },
    "settings": {
      "type": "object",
      "properties": {
        "siteName": {
          "type": "string"
        },
        "baseUrl": {
          "type": "string"
        },
        "defaultSeoDescription": {
          "type": "string"
        },
        "wordsPerMinute": {
          "type": "number"
        },
        "excerptTargetWords": {
          "type": "number"
        },
        "excerptSoftMaxWords": {
          "type": "number"
        },
        "defaultOgImage": {
          "type": "string"
        },
        "fxDisplayCurrency": {
          "type": "string"
        }
      }
    },
    "exchangeRates": {
      "type": "object",
      "properties": {
        "USD": {
          "type": "number"
        },
        "EUR": {
          "type": "number"
        },
        "GBP": {
          "type": "number"
        },
        "updatedAt": {
          "type": "string"
        }
      }
    },
    "issues": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "key": {
            "type": "any"
          },
          "label": {
            "type": "any"
          },
          "year": {
            "type": "any"
          },
          "order": {
            "type": "any"
          }
        }
      }
    },
    "articleCategories": {
      "type": "array",
      "items": "any"
    },
    "newsPublications": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "value": {
            "type": "any"
          },
          "label": {
            "type": "any"
          }
        }
      }
    },
    "productStatuses": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "salesPointTypes": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "publishingStatuses": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "siteTexts": {
      "type": "object",
      "properties": {}
    },
    "externalCode": {
      "type": "object",
      "properties": {}
    },
    "emptyCategoryRules": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "any"
          },
          "categoryType": {
            "type": "any"
          },
          "issueKey": {
            "type": "any"
          },
          "categoryValue": {
            "type": "any"
          },
          "message": {
            "type": "any"
          }
        }
      }
    },
    "sectionExceptions": {
      "type": "array",
      "items": "any"
    },
    "navigation": {
      "type": "array",
      "items": "any"
    },
    "announcement": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string"
        },
        "active": {
          "type": "boolean"
        },
        "text": {
          "type": "string"
        },
        "linkLabel": {
          "type": "string"
        },
        "linkUrl": {
          "type": "string"
        },
        "startDate": {
          "type": "string"
        },
        "endDate": {
          "type": "string"
        }
      }
    },
    "nationalLibraryLink": {
      "type": "string"
    },
    "articles": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "title": {
            "type": "any"
          },
          "categoryType": {
            "type": "any"
          },
          "issueKey": {
            "type": "any"
          },
          "categoryLabel": {
            "type": "any"
          },
          "keywords": {
            "type": "any"
          },
          "order": {
            "type": "any"
          },
          "seoTitle": {
            "type": "any"
          },
          "seoDescription": {
            "type": "any"
          },
          "indexable": {
            "type": "any"
          },
          "status": {
            "type": "any"
          },
          "archived": {
            "type": "any"
          },
          "categoryValue": {
            "type": "any"
          },
          "contentType": {
            "type": "any"
          },
          "id": {
            "type": "any"
          },
          "createdAt": {
            "type": "any"
          },
          "updatedAt": {
            "type": "any"
          },
          "slug": {
            "type": "any"
          },
          "slugLocked": {
            "type": "any"
          },
          "slugHistory": {
            "type": "any"
          },
          "publishDate": {
            "type": "any"
          }
        }
      }
    },
    "magazines": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "title": {
            "type": "any"
          },
          "issueKey": {
            "type": "any"
          },
          "newIssueLabel": {
            "type": "any"
          },
          "newIssueYear": {
            "type": "any"
          },
          "coverUrl": {
            "type": "any"
          },
          "altText": {
            "type": "any"
          },
          "visualLabel": {
            "type": "any"
          },
          "productStatus": {
            "type": "any"
          },
          "infoTitle": {
            "type": "any"
          },
          "order": {
            "type": "any"
          },
          "status": {
            "type": "any"
          },
          "archived": {
            "type": "any"
          },
          "indexable": {
            "type": "any"
          },
          "buyLinks": {
            "type": "any"
          },
          "contentType": {
            "type": "any"
          },
          "id": {
            "type": "any"
          },
          "createdAt": {
            "type": "any"
          },
          "updatedAt": {
            "type": "any"
          },
          "slug": {
            "type": "any"
          },
          "slugLocked": {
            "type": "any"
          }
        }
      }
    },
    "books": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "title": {
            "type": "any"
          },
          "author": {
            "type": "any"
          },
          "translator": {
            "type": "any"
          },
          "isbn": {
            "type": "any"
          },
          "price": {
            "type": "any"
          },
          "priceCurrency": {
            "type": "any"
          },
          "dimensions": {
            "type": "any"
          },
          "pageCount": {
            "type": "any"
          },
          "publicationYear": {
            "type": "any"
          },
          "edition": {
            "type": "any"
          },
          "printRun": {
            "type": "any"
          },
          "bindingType": {
            "type": "any"
          },
          "paperType": {
            "type": "any"
          },
          "insideCoverPrint": {
            "type": "any"
          },
          "insideCoverPrintUrl": {
            "type": "any"
          },
          "insideCoverPrintUrl2": {
            "type": "any"
          },
          "coverUrl": {
            "type": "any"
          },
          "coverWidth": {
            "type": "any"
          },
          "coverHeight": {
            "type": "any"
          },
          "altText": {
            "type": "any"
          }
        }
      }
    },
    "news": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "title": {
            "type": "any"
          },
          "publication": {
            "type": "any"
          },
          "keywords": {
            "type": "any"
          },
          "order": {
            "type": "any"
          },
          "publishDate": {
            "type": "any"
          },
          "unpublishDate": {
            "type": "any"
          },
          "seoTitle": {
            "type": "any"
          },
          "seoDescription": {
            "type": "any"
          },
          "canonicalPath": {
            "type": "any"
          },
          "indexable": {
            "type": "any"
          },
          "status": {
            "type": "any"
          },
          "archived": {
            "type": "any"
          },
          "pinned": {
            "type": "any"
          },
          "personLinks": {
            "type": "any"
          },
          "productLinks": {
            "type": "any"
          },
          "contentType": {
            "type": "any"
          },
          "id": {
            "type": "any"
          },
          "createdAt": {
            "type": "any"
          },
          "updatedAt": {
            "type": "any"
          },
          "slugHistory": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `GET` /api/geo
```json
{
  "type": "object",
  "properties": {
    "country": {
      "type": "string"
    }
  }
}
```
### `POST` /youtubei/v1/log_event
```json
{
  "type": "object",
  "properties": {
    "responseContext": {
      "type": "object",
      "properties": {}
    }
  }
}
```

