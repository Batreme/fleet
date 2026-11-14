---
title: "APIs & Protocols: explorewashingtonpark-org"
date: 2026-11-14
target: "[[overview|explorewashingtonpark-org]]"
---

# Discovered APIs & Protocols: explorewashingtonpark-org

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `POST` | `/events` | `200` | REST endpoint |
| `GET` | `/api/ui-extensions/script-registrations` | `200` | REST endpoint |
| `GET` | `/v1/weather/now` | `200` | REST endpoint |
| `GET` | `/itineraries` | `200` | REST endpoint |
| `POST` | `/api/census/render-batch` | `200` | REST endpoint |
| `POST` | `/forms/6a637ff7bddd76910c2a98e9/events` | `200` | REST endpoint |
| `GET` | `/projects-settings/7f434dd25a731bd8674909a501ae4d6c7.json` | `200` | REST endpoint |
| `GET` | `/api/popup-overlay/render` | `200` | REST endpoint |
| `POST` | `/api/census/button-render` | `200` | REST endpoint |
| `POST` | `/api/census/button-render` | `200` | REST endpoint |
| `GET` | `/v1/widget-settings` | `200` | REST endpoint |
| `GET` | `/_s/v4/app/6af164091d5/languages/en.json` | `200` | REST endpoint |
| `GET` | `/_s/v4/app/6af164091d5/languages/en_dev.json` | `200` | REST endpoint |
| `POST` | `/v1/session/start` | `200` | REST endpoint |
| `POST` | `/api/census/overlay` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /api/ui-extensions/script-registrations
```json
{
  "type": "object",
  "properties": {
    "extensionScriptRegistrations": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "any"
          },
          "extensionCredential": {
            "type": "any"
          },
          "src": {
            "type": "any"
          },
          "integrity": {
            "type": "any"
          },
          "createdOn": {
            "type": "any"
          },
          "updatedOn": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `GET` /v1/weather/now
```json
{
  "type": "object",
  "properties": {
    "timestamp": {
      "type": "string"
    },
    "location": {
      "type": "object",
      "properties": {
        "lat": {
          "type": "number"
        },
        "lon": {
          "type": "number"
        }
      }
    },
    "temperature": {
      "type": "number"
    },
    "temperatureUnit": {
      "type": "string"
    },
    "feelsLike": {
      "type": "number"
    },
    "condition": {
      "type": "string"
    },
    "conditionText": {
      "type": "string"
    },
    "humidity": {
      "type": "number"
    },
    "windSpeed": {
      "type": "number"
    },
    "windUnit": {
      "type": "string"
    },
    "windDirection": {
      "type": "number"
    },
    "icon": {
      "type": "string"
    }
  }
}
```
### `GET` /itineraries
```json
{
  "type": "object",
  "properties": {
    "website": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string"
        },
        "captchaSettings": {
          "type": "object",
          "properties": {
            "siteKey": {
              "type": "any"
            },
            "enabledForDonations": {
              "type": "any"
            }
          }
        },
        "cloneable": {
          "type": "boolean"
        },
        "contentModifiedOn": {
          "type": "number"
        },
        "identifier": {
          "type": "string"
        },
        "imageMetadataProcessingEnabled": {
          "type": "boolean"
        },
        "isHstsEnabled": {
          "type": "boolean"
        },
        "language": {
          "type": "string"
        },
        "location": {
          "type": "object",
          "properties": {
            "mapLat": {
              "type": "any"
            },
            "mapLng": {
              "type": "any"
            },
            "addressTitle": {
              "type": "any"
            },
            "addressLine1": {
              "type": "any"
            },
            "addressLine2": {
              "type": "any"
            },
            "addressCountry": {
              "type": "any"
            }
          }
        },
        "logoImageId": {
          "type": "string"
        },
        "mobileLogoImageId": {
          "type": "string"
        },
        "primaryDomain": {
          "type": "string"
        },
        "screenshotId": {
          "type": "string"
        },
        "shareButtonOptions": {
          "type": "object",
          "properties": {
            "3": {
              "type": "any"
            },
            "8": {
              "type": "any"
            },
            "4": {
              "type": "any"
            },
            "2": {
              "type": "any"
            },
            "7": {
              "type": "any"
            },
            "6": {
              "type": "any"
            },
            "1": {
              "type": "any"
            }
          }
        },
        "showOwnerLogin": {
          "type": "boolean"
        },
        "siteDescription": {
          "type": "string"
        },
        "siteStatus": {
          "type": "object",
          "properties": {}
        },
        "siteTitle": {
          "type": "string"
        },
        "socialLogoImageId": {
          "type": "string"
        },
        "sslSetting": {
          "type": "number"
        }
      }
    },
    "websiteSettings": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string"
        },
        "websiteId": {
          "type": "string"
        },
        "subjects": {
          "type": "array",
          "items": "any"
        },
        "country": {
          "type": "string"
        },
        "state": {
          "type": "string"
        },
        "simpleLikingEnabled": {
          "type": "boolean"
        },
        "mobileInfoBarSettings": {
          "type": "object",
          "properties": {
            "isContactEmailEnabled": {
              "type": "any"
            },
            "isContactPhoneNumberEnabled": {
              "type": "any"
            },
            "isLocationEnabled": {
              "type": "any"
            },
            "isBusinessHoursEnabled": {
              "type": "any"
            }
          }
        },
        "announcementBarSettings": {
          "type": "object",
          "properties": {
            "style": {
              "type": "any"
            },
            "text": {
              "type": "any"
            }
          }
        },
        "popupOverlaySettings": {
          "type": "object",
          "properties": {
            "style": {
              "type": "any"
            },
            "showOnScroll": {
              "type": "any"
            },
            "scrollPercentage": {
              "type": "any"
            },
            "showOnTimer": {
              "type": "any"
            },
            "timerDelay": {
              "type": "any"
            },
            "showUntilSignup": {
              "type": "any"
            },
            "displayFrequency": {
              "type": "any"
            },
            "enableMobile": {
              "type": "any"
            },
            "enabledPages": {
              "type": "any"
            },
            "showOnAllPages": {
              "type": "any"
            },
            "version": {
              "type": "any"
            }
          }
        },
        "commentLikesAllowed": {
          "type": "boolean"
        },
        "commentAnonAllowed": {
          "type": "boolean"
        },
        "commentThreaded": {
          "type": "boolean"
        },
        "commentApprovalRequired": {
          "type": "boolean"
        },
        "commentAvatarsOn": {
          "type": "boolean"
        },
        "commentSortType": {
          "type": "number"
        },
        "commentFlagThreshold": {
          "type": "number"
        },
        "commentFlagsAllowed": {
          "type": "boolean"
        },
        "commentEnableByDefault": {
          "type": "boolean"
        },
        "commentDisableAfterDaysDefault": {
          "type": "number"
        },
        "disqusShortname": {
          "type": "string"
        }
      }
    },
    "collection": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string"
        },
        "websiteId": {
          "type": "string"
        },
        "backgroundSource": {
          "type": "number"
        },
        "enabled": {
          "type": "boolean"
        },
        "starred": {
          "type": "boolean"
        },
        "type": {
          "type": "number"
        },
        "ordering": {
          "type": "number"
        },
        "title": {
          "type": "string"
        },
        "navigationTitle": {
          "type": "string"
        },
        "urlId": {
          "type": "string"
        },
        "itemCount": {
          "type": "number"
        },
        "updatedOn": {
          "type": "number"
        },
        "description": {
          "type": "string"
        },
        "pageSize": {
          "type": "number"
        },
        "features": {
          "type": "object",
          "properties": {
            "relatedItems": {
              "type": "any"
            },
            "productQuickView": {
              "type": "any"
            }
          }
        },
        "eventView": {
          "type": "number"
        },
        "folder": {
          "type": "boolean"
        },
        "dropdown": {
          "type": "boolean"
        },
        "tags": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "categories": {
          "type": "array",
          "items": {
            "type": "any"
          }
        }
      }
    },
    "shoppingCart": {
      "type": "object",
      "properties": {
        "websiteId": {
          "type": "string"
        },
        "created": {
          "type": "number"
        },
        "entries": {
          "type": "array",
          "items": "any"
        },
        "shippingLocation": {
          "type": "object",
          "properties": {}
        },
        "taxLineItems": {
          "type": "array",
          "items": "any"
        },
        "coupons": {
          "type": "array",
          "items": "any"
        },
        "promoCodes": {
          "type": "array",
          "items": "any"
        },
        "appliedGiftCards": {
          "type": "array",
          "items": "any"
        },
        "cartType": {
          "type": "number"
        },
        "validCoupons": {
          "type": "array",
          "items": "any"
        },
        "invalidCoupons": {
          "type": "array",
          "items": "any"
        },
        "subtotalCents": {
          "type": "number"
        },
        "taxCents": {
          "type": "number"
        },
        "shippingCostCents": {
          "type": "number"
        },
        "discountCents": {
          "type": "number"
        },
        "giftCardRedemptionTotalCents": {
          "type": "number"
        },
        "grandTotalCents": {
          "type": "number"
        },
        "amountDueCents": {
          "type": "number"
        },
        "remainingBalanceCents": {
          "type": "number"
        },
        "totalQuantity": {
          "type": "number"
        }
      }
    },
    "shareButtons": {
      "type": "object",
      "properties": {
        "twitter": {
          "type": "boolean"
        },
        "facebook": {
          "type": "boolean"
        },
        "reddit": {
          "type": "boolean"
        },
        "tumblr": {
          "type": "boolean"
        },
        "google": {
          "type": "boolean"
        },
        "pinterest": {
          "type": "boolean"
        },
        "linkedin": {
          "type": "boolean"
        }
      }
    },
    "showCart": {
      "type": "boolean"
    },
    "localizedStrings": {
      "type": "object",
      "properties": {
        "smartling": {
          "type": "object",
          "properties": {
            "string_format": {
              "type": "any"
            }
          }
        },
        "account": {
          "type": "string"
        },
        "add": {
          "type": "string"
        },
        "addVideo": {
          "type": "string"
        },
        "all": {
          "type": "string"
        },
        "allProducts": {
          "type": "string"
        },
        "back": {
          "type": "string"
        },
        "backToAllEvents": {
          "type": "string"
        },
        "category": {
          "type": "string"
        },
        "categories": {
          "type": "string"
        },
        "categorySelectText": {
          "type": "string"
        },
        "close": {
          "type": "string"
        },
        "closeAnnouncement": {
          "type": "string"
        },
        "closeMenu": {
          "type": "string"
        },
        "completeAndContinue": {
          "type": "string"
        },
        "courseCtaStart": {
          "type": "string"
        },
        "courseCtaContinue": {
          "type": "string"
        },
        "courseCtaPreview": {
          "type": "string"
        },
        "courseCtaRetake": {
          "type": "string"
        },
        "courseUnpublishedLessons": {
          "type": "string"
        }
      }
    },
    "userAccountsContext": {
      "type": "object",
      "properties": {
        "showSignInLink": {
          "type": "boolean"
        }
      }
    },
    "template": {
      "type": "object",
      "properties": {
        "mobileStylesEnabled": {
          "type": "boolean"
        }
      }
    },
    "uiextensions": {
      "type": "object",
      "properties": {
        "product-badge": {
          "type": "string"
        },
        "product-body": {
          "type": "string"
        },
        "product-badge-mobile": {
          "type": "string"
        },
        "product-body-mobile": {
          "type": "string"
        },
        "product-collection-item": {
          "type": "string"
        },
        "scripts-enabled": {
          "type": "boolean"
        }
      }
    },
    "empty": {
      "type": "boolean"
    },
    "emptyFolder": {
      "type": "boolean"
    },
    "calendarView": {
      "type": "boolean"
    },
    "items": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "any"
          },
          "collectionId": {
            "type": "any"
          },
          "recordType": {
            "type": "any"
          },
          "addedOn": {
            "type": "any"
          },
          "updatedOn": {
            "type": "any"
          },
          "displayIndex": {
            "type": "any"
          },
          "starred": {
            "type": "any"
          },
          "passthrough": {
            "type": "any"
          },
          "tags": {
            "type": "any"
          },
          "categories": {
            "type": "any"
          },
          "workflowState": {
            "type": "any"
          },
          "publishOn": {
            "type": "any"
          },
          "authorId": {
            "type": "any"
          },
          "systemDataId": {
            "type": "any"
          },
          "systemDataVariants": {
            "type": "any"
          },
          "systemDataSourceType": {
            "type": "any"
          },
          "filename": {
            "type": "any"
          },
          "mediaFocalPoint": {
            "type": "any"
          },
          "colorData": {
            "type": "any"
          },
          "urlId": {
            "type": "any"
          }
        }
      }
    },
    "pagePreviewContext": {
      "type": "object",
      "properties": {
        "isPreviewMode": {
          "type": "boolean"
        },
        "memberAccessUrl": {
          "type": "string"
        }
      }
    }
  }
}
```
### `POST` /api/census/render-batch
```json
{
  "type": "object",
  "properties": {
    "success": {
      "type": "boolean"
    }
  }
}
```
### `POST` /forms/6a637ff7bddd76910c2a98e9/events
```json
{
  "type": "string"
}
```
### `GET` /projects-settings/7f434dd25a731bd8674909a501ae4d6c7.json
```json
{
  "type": "object",
  "properties": {
    "website": {
      "type": "string"
    },
    "uid": {
      "type": "string"
    },
    "project_slug": {
      "type": "string"
    },
    "deleted_at": {
      "type": "null"
    },
    "api_key": {
      "type": "string"
    },
    "language_from": {
      "type": "string"
    },
    "language_from_custom_flag": {
      "type": "string"
    },
    "language_from_custom_name": {
      "type": "null"
    },
    "auto_switch": {
      "type": "boolean"
    },
    "auto_switch_fallback": {
      "type": "null"
    },
    "translation_engine": {
      "type": "number"
    },
    "excluded_paths": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "type": {
            "type": "any"
          },
          "value": {
            "type": "any"
          },
          "language_button_displayed": {
            "type": "any"
          },
          "exclusion_behavior": {
            "type": "any"
          },
          "excluded_languages": {
            "type": "any"
          },
          "regex": {
            "type": "any"
          }
        }
      }
    },
    "excluded_blocks": {
      "type": "array",
      "items": "any"
    },
    "dynamics": {
      "type": "array",
      "items": "any"
    },
    "custom_settings": {
      "type": "object",
      "properties": {
        "dynamic": {
          "type": "string"
        },
        "live": {
          "type": "boolean"
        },
        "button_style": {
          "type": "object",
          "properties": {
            "with_name": {
              "type": "any"
            },
            "full_name": {
              "type": "any"
            },
            "is_dropdown": {
              "type": "any"
            },
            "with_flags": {
              "type": "any"
            },
            "custom_css": {
              "type": "any"
            },
            "flag_type": {
              "type": "any"
            }
          }
        },
        "switchers": {
          "type": "array",
          "items": "any"
        },
        "translate_search": {
          "type": "boolean"
        },
        "translate_images": {
          "type": "boolean"
        },
        "loading_bar": {
          "type": "boolean"
        },
        "hide_switcher": {
          "type": "boolean"
        },
        "wait_transition": {
          "type": "boolean"
        },
        "auto_inject_script": {
          "type": "boolean"
        },
        "ve_inject_library": {
          "type": "boolean"
        },
        "squarespace_official_integration": {
          "type": "boolean"
        },
        "squarespace_extension_connected": {
          "type": "boolean"
        }
      }
    },
    "media_enabled": {
      "type": "boolean"
    },
    "external_enabled": {
      "type": "boolean"
    },
    "page_views_enabled": {
      "type": "boolean"
    },
    "versions": {
      "type": "object",
      "properties": {
        "translation": {
          "type": "number"
        }
      }
    },
    "pending_translation_enabled": {
      "type": "boolean"
    }
  }
}
```
### `GET` /api/popup-overlay/render
```json
{
  "type": "object",
  "properties": {
    "shouldDisplayOnPage": {
      "type": "boolean"
    },
    "renderedHtml": {
      "type": "string"
    }
  }
}
```
### `POST` /api/census/button-render
```json
{
  "type": "object",
  "properties": {
    "success": {
      "type": "boolean"
    }
  }
}
```
### `POST` /api/census/button-render
```json
{
  "type": "object",
  "properties": {
    "success": {
      "type": "boolean"
    }
  }
}
```

