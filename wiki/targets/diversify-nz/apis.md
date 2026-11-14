---
title: "APIs & Protocols: diversify-nz"
date: 2026-11-14
target: "[[overview|diversify-nz]]"
---

# Discovered APIs & Protocols: diversify-nz

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/r/v1/sites/491220/categories` | `200` | REST endpoint |
| `GET` | `/r/v1/sites/491220/products` | `200` | REST endpoint |
| `POST` | `/r/v1/list_products` | `200` | REST endpoint |
| `GET` | `/r/v1/sites/491220/portfolio/categories` | `200` | REST endpoint |
| `GET` | `/r/v1/sites/491220/portfolio/setting` | `200` | REST endpoint |
| `GET` | `/r/v1/sites/491220/portfolio/products` | `200` | REST endpoint |
| `GET` | `/r/v1/sites/491220/blog/tags` | `200` | REST endpoint |
| `GET` | `/r/v1/sites/491220/blog` | `200` | REST endpoint |
| `GET` | `/r/v1/sites/491220/ecommerce` | `200` | REST endpoint |
| `POST` | `/3.0/projects/5317e03605cd66236a000002/events/strikingly_pageviews` | `201` | REST endpoint |
| `GET` | `/r/v1/sites/491220/popups/active` | `200` | REST endpoint |
| `GET` | `/r/v1/sites/491220/portfolio/setting` | `200` | REST endpoint |
| `GET` | `/r/v1/sites/491220/ecommerce` | `200` | REST endpoint |
| `GET` | `/r/v1/sites/491220/membership/tiers` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /r/v1/sites/491220/categories
```json
{
  "type": "object",
  "properties": {
    "data": {
      "type": "array",
      "items": "any"
    }
  }
}
```
### `GET` /r/v1/sites/491220/products
```json
{
  "type": "object",
  "properties": {
    "status": {
      "type": "number"
    },
    "meta": {
      "type": "object",
      "properties": {
        "devMessage": {
          "type": "null"
        },
        "errorKey": {
          "type": "null"
        },
        "userMessage": {
          "type": "object",
          "properties": {
            "i18n": {
              "type": "any"
            },
            "plain": {
              "type": "any"
            }
          }
        }
      }
    },
    "data": {
      "type": "object",
      "properties": {
        "paginationMeta": {
          "type": "object",
          "properties": {
            "currentPage": {
              "type": "any"
            },
            "previousPage": {
              "type": "any"
            },
            "nextPage": {
              "type": "any"
            },
            "perPage": {
              "type": "any"
            },
            "totalPages": {
              "type": "any"
            },
            "totalCount": {
              "type": "any"
            }
          }
        },
        "allProductsCount": {
          "type": "number"
        },
        "showDummyData": {
          "type": "null"
        },
        "products": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "filterOptions": {
          "type": "object",
          "properties": {
            "prices": {
              "type": "any"
            },
            "filteredPriceRange": {
              "type": "any"
            },
            "productOptions": {
              "type": "any"
            },
            "dimensions": {
              "type": "any"
            }
          }
        }
      }
    }
  }
}
```
### `POST` /r/v1/list_products
```json
{
  "type": "object",
  "properties": {
    "status": {
      "type": "number"
    },
    "meta": {
      "type": "object",
      "properties": {
        "devMessage": {
          "type": "null"
        },
        "errorKey": {
          "type": "null"
        },
        "userMessage": {
          "type": "object",
          "properties": {
            "i18n": {
              "type": "any"
            },
            "plain": {
              "type": "any"
            }
          }
        }
      }
    },
    "data": {
      "type": "object",
      "properties": {
        "products": {
          "type": "array",
          "items": "any"
        }
      }
    }
  }
}
```
### `GET` /r/v1/sites/491220/portfolio/categories
```json
{
  "type": "object",
  "properties": {
    "data": {
      "type": "array",
      "items": "any"
    }
  }
}
```
### `GET` /r/v1/sites/491220/portfolio/setting
```json
{
  "type": "object",
  "properties": {
    "status": {
      "type": "number"
    },
    "meta": {
      "type": "object",
      "properties": {
        "devMessage": {
          "type": "null"
        },
        "errorKey": {
          "type": "null"
        },
        "userMessage": {
          "type": "object",
          "properties": {
            "i18n": {
              "type": "any"
            },
            "plain": {
              "type": "any"
            }
          }
        }
      }
    },
    "data": {
      "type": "object",
      "properties": {
        "categoryOrder": {
          "type": "object",
          "properties": {}
        },
        "productOrder": {
          "type": "object",
          "properties": {}
        },
        "productLayout": {
          "type": "null"
        },
        "regionOptionsOrder": {
          "type": "array",
          "items": "any"
        },
        "currencyCode": {
          "type": "string"
        },
        "contactRequired": {
          "type": "boolean"
        },
        "visitorForm": {
          "type": "object",
          "properties": {
            "customForm": {
              "type": "any"
            },
            "enableSpamVerification": {
              "type": "any"
            }
          }
        },
        "restrictedDetails": {
          "type": "null"
        },
        "customButtonType": {
          "type": "string"
        },
        "customUrlType": {
          "type": "null"
        },
        "customButtonSetting": {
          "type": "object",
          "properties": {
            "individualButtonMigrated": {
              "type": "any"
            }
          }
        }
      }
    }
  }
}
```
### `GET` /r/v1/sites/491220/portfolio/products
```json
{
  "type": "object",
  "properties": {
    "status": {
      "type": "number"
    },
    "meta": {
      "type": "object",
      "properties": {
        "devMessage": {
          "type": "null"
        },
        "errorKey": {
          "type": "null"
        },
        "userMessage": {
          "type": "object",
          "properties": {
            "i18n": {
              "type": "any"
            },
            "plain": {
              "type": "any"
            }
          }
        }
      }
    },
    "data": {
      "type": "object",
      "properties": {
        "paginationMeta": {
          "type": "object",
          "properties": {
            "currentPage": {
              "type": "any"
            },
            "previousPage": {
              "type": "any"
            },
            "nextPage": {
              "type": "any"
            },
            "perPage": {
              "type": "any"
            },
            "totalPages": {
              "type": "any"
            },
            "totalCount": {
              "type": "any"
            }
          }
        },
        "showDummyData": {
          "type": "null"
        },
        "dummyTemplateType": {
          "type": "null"
        },
        "dummyCategoryId": {
          "type": "null"
        },
        "allProductsCount": {
          "type": "number"
        },
        "products": {
          "type": "array",
          "items": "any"
        }
      }
    }
  }
}
```
### `GET` /r/v1/sites/491220/blog/tags
```json
{
  "type": "object",
  "properties": {
    "status": {
      "type": "number"
    },
    "meta": {
      "type": "object",
      "properties": {
        "devMessage": {
          "type": "null"
        },
        "errorKey": {
          "type": "null"
        },
        "userMessage": {
          "type": "object",
          "properties": {
            "i18n": {
              "type": "any"
            },
            "plain": {
              "type": "any"
            }
          }
        }
      }
    },
    "data": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "any"
          },
          "count": {
            "type": "any"
          },
          "id": {
            "type": "any"
          },
          "url": {
            "type": "any"
          },
          "pageTitle": {
            "type": "any"
          },
          "description": {
            "type": "any"
          },
          "slug": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `GET` /r/v1/sites/491220/blog
```json
{
  "type": "object",
  "properties": {
    "status": {
      "type": "number"
    },
    "meta": {
      "type": "object",
      "properties": {
        "devMessage": {
          "type": "null"
        },
        "errorKey": {
          "type": "null"
        },
        "userMessage": {
          "type": "object",
          "properties": {
            "i18n": {
              "type": "any"
            },
            "plain": {
              "type": "any"
            }
          }
        }
      }
    },
    "data": {
      "type": "object",
      "properties": {
        "blog": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "role": {
              "type": "any"
            },
            "isPro": {
              "type": "any"
            },
            "customDomain": {
              "type": "any"
            },
            "subscribersCount": {
              "type": "any"
            },
            "blogSettings": {
              "type": "any"
            },
            "showDummyData": {
              "type": "any"
            },
            "blogPosts": {
              "type": "any"
            },
            "wechatMpAccountId": {
              "type": "any"
            },
            "pagination": {
              "type": "any"
            }
          }
        }
      }
    }
  }
}
```
### `GET` /r/v1/sites/491220/ecommerce
```json
{
  "type": "object",
  "properties": {
    "status": {
      "type": "number"
    },
    "meta": {
      "type": "object",
      "properties": {
        "devMessage": {
          "type": "null"
        },
        "errorKey": {
          "type": "null"
        },
        "userMessage": {
          "type": "object",
          "properties": {
            "i18n": {
              "type": "any"
            },
            "plain": {
              "type": "any"
            }
          }
        }
      }
    },
    "data": {
      "type": "object",
      "properties": {
        "paymentGateways": {
          "type": "object",
          "properties": {
            "stripe": {
              "type": "any"
            },
            "offline": {
              "type": "any"
            },
            "paypal": {
              "type": "any"
            },
            "midtrans": {
              "type": "any"
            },
            "alipay": {
              "type": "any"
            },
            "pingppWxPub": {
              "type": "any"
            },
            "pingppWxPubQr": {
              "type": "any"
            },
            "pingppAlipayQr": {
              "type": "any"
            },
            "pingppAlipayWap": {
              "type": "any"
            },
            "wechatpay": {
              "type": "any"
            },
            "square": {
              "type": "any"
            }
          }
        },
        "connectedToPaynow": {
          "type": "boolean"
        },
        "shortcuts": {
          "type": "array",
          "items": "any"
        },
        "shortcutsOrder": {
          "type": "object",
          "properties": {}
        },
        "hasCoupon": {
          "type": "boolean"
        },
        "customerSupportEmail": {
          "type": "string"
        },
        "notificationEmail": {
          "type": "string"
        },
        "shippingGuideline": {
          "type": "string"
        },
        "currencyCode": {
          "type": "string"
        },
        "currencyData": {
          "type": "object",
          "properties": {
            "code": {
              "type": "any"
            },
            "symbol": {
              "type": "any"
            },
            "decimal": {
              "type": "any"
            },
            "thousand": {
              "type": "any"
            },
            "precision": {
              "type": "any"
            },
            "name": {
              "type": "any"
            }
          }
        },
        "estimatedDelivery": {
          "type": "null"
        },
        "orderBy": {
          "type": "null"
        },
        "orderList": {
          "type": "object",
          "properties": {
            "43597": {
              "type": "any"
            }
          }
        },
        "categoryOrder": {
          "type": "object",
          "properties": {}
        },
        "shippingRegions": {
          "type": "object",
          "properties": {
            "default": {
              "type": "any"
            },
            "nz": {
              "type": "any"
            },
            "au": {
              "type": "any"
            }
          }
        },
        "taxes": {
          "type": "number"
        },
        "registration": {
          "type": "string"
        },
        "registrationMessage": {
          "type": "null"
        },
        "banner": {
          "type": "array",
          "items": "any"
        },
        "flashSalePosition": {
          "type": "boolean"
        }
      }
    }
  }
}
```
### `POST` /3.0/projects/5317e03605cd66236a000002/events/strikingly_pageviews
```json
{
  "type": "object",
  "properties": {
    "created": {
      "type": "boolean"
    }
  }
}
```

