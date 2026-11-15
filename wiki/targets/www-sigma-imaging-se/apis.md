---
title: "APIs & Protocols: www-sigma-imaging-se"
date: 2026-11-14
target: "www-sigma-imaging-se"
---

# Discovered APIs & Protocols: www-sigma-imaging-se

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/core/v2/klevu.js` | `200` | REST endpoint |
| `GET` | `/klevu-js-v1/klevu-js-api/klevu-173997154273517723.json` | `200` | REST endpoint |
| `GET` | `/klevu-js-v1/klevu-js-api/klevu-173997154273517723-banner.json` | `200` | REST endpoint |
| `GET` | `/klevu-js-v1/klevu-js-api/klevu-173997154273517723-maps.json` | `200` | REST endpoint |
| `GET` | `/v2/analytics.js` | `200` | REST endpoint |
| `GET` | `/rest/default/V1/klevu/customerData` | `200` | REST endpoint |
| `GET` | `/theme/default/v2/quick-search-theme.js` | `200` | REST endpoint |
| `GET` | `/amcookie/cookie/cookies` | `200` | REST endpoint |
| `POST` | `/geo_ip/action/process/` | `200` | REST endpoint |
| `POST` | `/public/1.0/klevu-173997154273517723/session` | `200` | REST endpoint |
| `POST` | `/` | `200` | REST endpoint |
| `POST` | `/` | `-1` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /klevu-js-v1/klevu-js-api/klevu-173997154273517723.json
```json
{
  "type": "object",
  "properties": {
    "klevu_showBannerAds": {
      "type": "boolean"
    },
    "klevu_multiSelectFilters": {
      "type": "boolean"
    },
    "klevu_abTestActive": {
      "type": "boolean"
    },
    "klevu_userAnalyticsDomain": {
      "type": "string"
    },
    "klevu_uc_userOptions": {
      "type": "object",
      "properties": {
        "addToCartButton": {
          "type": "string"
        },
        "showRolloverImage": {
          "type": "boolean"
        },
        "showProductSwatches": {
          "type": "boolean"
        },
        "enablePersonalisationInCatNav": {
          "type": "boolean"
        },
        "showRatingsCountOnCategoryPage": {
          "type": "boolean"
        },
        "noResultsOptions": {
          "type": "object",
          "properties": {
            "messages": {
              "type": "any"
            },
            "banners": {
              "type": "any"
            }
          }
        },
        "noImageUrl": {
          "type": "string"
        },
        "showRatingsOnCategoryPage": {
          "type": "boolean"
        },
        "enablePersonalisationInSearch": {
          "type": "boolean"
        },
        "isFullImageUrlProvided": {
          "type": "boolean"
        },
        "priceInterval": {
          "type": "string"
        },
        "showRatingsCountOnSearchResultsLandingPage": {
          "type": "boolean"
        },
        "showRecentlyViewedItems": {
          "type": "boolean"
        },
        "showTrendingProducts": {
          "type": "boolean"
        },
        "showRatingsOnQuickSearches": {
          "type": "boolean"
        },
        "showRatingsCountOnQuickSearches": {
          "type": "boolean"
        },
        "showRatingsOnSearchResultsLandingPage": {
          "type": "boolean"
        },
        "showFiltersInMobile": {
          "type": "boolean"
        }
      }
    },
    "klevu_cmsAnalyticsDomain": {
      "type": "string"
    },
    "klevu_showOutOfStock": {
      "type": "boolean"
    },
    "klevu_webStoreLanguage": {
      "type": "string"
    },
    "klevu_logoFreeSearch": {
      "type": "boolean"
    },
    "klevu_layoutView": {
      "type": "string"
    },
    "klevu_showPopuralTerms": {
      "type": "boolean"
    },
    "klevu_showProductCode": {
      "type": "boolean"
    },
    "klevu_showPopularSearches": {
      "type": "boolean"
    },
    "klevu_cmsApiKey": {
      "type": "string"
    },
    "klevu_categorySearchEnabled": {
      "type": "boolean"
    },
    "klevu_showPriceSlider": {
      "type": "boolean"
    },
    "klevu_addToCartEnabled": {
      "type": "boolean"
    },
    "klevu_cmsEnabled": {
      "type": "boolean"
    },
    "klevu_filtersOnLeft": {
      "type": "boolean"
    },
    "klevu_showPrices": {
      "type": "boolean"
    }
  }
}
```
### `GET` /klevu-js-v1/klevu-js-api/klevu-173997154273517723-banner.json
```json
{
  "type": "object",
  "properties": {
    "klevu_banner": {
      "type": "array",
      "items": "any"
    }
  }
}
```
### `GET` /klevu-js-v1/klevu-js-api/klevu-173997154273517723-maps.json
```json
{
  "type": "object",
  "properties": {
    "klevu_autoCorrectMap": {
      "type": "array",
      "items": "any"
    },
    "klevu_keywordUrlMap": {
      "type": "array",
      "items": "any"
    }
  }
}
```
### `GET` /rest/default/V1/klevu/customerData
```json
{
  "type": "object",
  "properties": {
    "session_id": {
      "type": "string"
    },
    "shopper_ip": {
      "type": "string"
    },
    "revalidate_after": {
      "type": "number"
    }
  }
}
```
### `GET` /amcookie/cookie/cookies
```json
{
  "type": "object",
  "properties": {
    "groupData": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "groupId": {
            "type": "any"
          },
          "isEssential": {
            "type": "any"
          },
          "name": {
            "type": "any"
          },
          "description": {
            "type": "any"
          },
          "checked": {
            "type": "any"
          },
          "cookies": {
            "type": "any"
          }
        }
      }
    },
    "lastUpdate": {
      "type": "number"
    },
    "cookiePolicy": {
      "type": "string"
    }
  }
}
```
### `POST` /geo_ip/action/process/
```json
{
  "type": "object",
  "properties": {
    "success": {
      "type": "boolean"
    },
    "data": {
      "type": "array",
      "items": "any"
    }
  }
}
```
### `POST` /public/1.0/klevu-173997154273517723/session
```json
{
  "type": "object",
  "properties": {
    "apikey": {
      "type": "string"
    },
    "sessionId": {
      "type": "string"
    },
    "segmentInfo": {
      "type": "object",
      "properties": {
        "segments": {
          "type": "array",
          "items": "any"
        },
        "ttl": {
          "type": "number"
        }
      }
    }
  }
}
```

