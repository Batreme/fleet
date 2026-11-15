---
title: "APIs & Protocols: www-terrenohotel-com_en"
date: 2026-11-14
target: "www-terrenohotel-com_en"
---

# Discovered APIs & Protocols: www-terrenohotel-com_en

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/HOTEL/100380929.json` | `200` | REST endpoint |
| `GET` | `/MiraiWebService/cookieBanner/100380929` | `200` | REST endpoint |
| `POST` | `/getCookie` | `204` | REST endpoint |
| `GET` | `/MiraiWebService/ip/get` | `200` | REST endpoint |
| `GET` | `/HOTEL/100380929-currencies.json` | `200` | REST endpoint |
| `GET` | `/features/specs` | `200` | REST endpoint |
| `GET` | `/api/dictionary` | `200` | REST endpoint |
| `GET` | `/lobby/api/channels/100380929/settings/public` | `200` | REST endpoint |
| `GET` | `/api/dictionary` | `200` | REST endpoint |
| `GET` | `/100380929/112026.json` | `200` | REST endpoint |
| `GET` | `/100380929/122026.json` | `200` | REST endpoint |
| `GET` | `/100380929/012027.json` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /HOTEL/100380929.json
```json
{
  "type": "object",
  "properties": {
    "maxBookingDays": {
      "type": "number"
    },
    "visibleMonths": {
      "type": "number"
    },
    "maxDate": {
      "type": "number"
    },
    "promoText": {
      "type": "object",
      "properties": {
        "de": {
          "type": "string"
        },
        "en": {
          "type": "string"
        },
        "es": {
          "type": "string"
        }
      }
    },
    "promoTextKey": {
      "type": "string"
    },
    "showPromoNav": {
      "type": "boolean"
    },
    "showPromoBooking": {
      "type": "boolean"
    },
    "bookText": {
      "type": "object",
      "properties": {
        "de": {
          "type": "string"
        },
        "en": {
          "type": "string"
        },
        "es": {
          "type": "string"
        }
      }
    },
    "bookTextKey": {
      "type": "string"
    },
    "showTotalNights": {
      "type": "boolean"
    },
    "lodgingDenomination": {
      "type": "string"
    },
    "showLanguageSwitcher": {
      "type": "boolean"
    },
    "minRoomsEngineNotification": {
      "type": "number"
    },
    "showReservationText": {
      "type": "object",
      "properties": {
        "de": {
          "type": "string"
        },
        "en": {
          "type": "string"
        },
        "es": {
          "type": "string"
        }
      }
    },
    "showReservationKey": {
      "type": "string"
    },
    "tracking": {
      "type": "object",
      "properties": {
        "analyticsTracking": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "adwordsTracking": {
          "type": "array",
          "items": "any"
        },
        "gtmTracking": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "bingTracking": {
          "type": "array",
          "items": "any"
        },
        "affiliredTracking": {
          "type": "array",
          "items": "any"
        },
        "thnTracking": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "miraiTracking": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "facebookTracking": {
          "type": "array",
          "items": "any"
        },
        "compareTracking": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "tiktokTracking": {
          "type": "array",
          "items": "any"
        },
        "gtgEnabled": {
          "type": "boolean"
        },
        "idTokenProvider": {
          "type": "number"
        }
      }
    },
    "clubConfiguration": {
      "type": "object",
      "properties": {
        "showClubDiscountFilter": {
          "type": "boolean"
        },
        "activeClubDiscountByDefault": {
          "type": "boolean"
        }
      }
    },
    "showPricesInCalendar": {
      "type": "boolean"
    },
    "languages": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "occupationDescriptionMode": {
      "type": "string"
    }
  }
}
```
### `GET` /MiraiWebService/cookieBanner/100380929
```json
{
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    }
  }
}
```
### `GET` /MiraiWebService/ip/get
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
### `GET` /HOTEL/100380929-currencies.json
```json
{
  "type": "object",
  "properties": {
    "PR": {
      "type": "string"
    },
    "HK": {
      "type": "string"
    },
    "PT": {
      "type": "string"
    },
    "HM": {
      "type": "string"
    },
    "HN": {
      "type": "string"
    },
    "PW": {
      "type": "string"
    },
    "PY": {
      "type": "string"
    },
    "HR": {
      "type": "string"
    },
    "HT": {
      "type": "string"
    },
    "HU": {
      "type": "string"
    },
    "ID": {
      "type": "string"
    },
    "YT": {
      "type": "string"
    },
    "IE": {
      "type": "string"
    },
    "AD": {
      "type": "string"
    },
    "IL": {
      "type": "string"
    },
    "AE": {
      "type": "string"
    },
    "IN": {
      "type": "string"
    },
    "IO": {
      "type": "string"
    },
    "ZA": {
      "type": "string"
    },
    "IS": {
      "type": "string"
    }
  }
}
```
### `GET` /features/specs
```json
{
  "type": "object",
  "properties": {
    "core": {
      "type": "boolean"
    },
    "finder": {
      "type": "boolean"
    },
    "hotelverse": {
      "type": "boolean"
    },
    "otaprices": {
      "type": "boolean"
    },
    "payments": {
      "type": "boolean"
    },
    "pestana": {
      "type": "boolean"
    },
    "showPriceIncrements": {
      "type": "boolean"
    },
    "metrics": {
      "type": "boolean"
    },
    "errorTracking": {
      "type": "boolean"
    },
    "cesSurvey": {
      "type": "boolean"
    },
    "modalPaynopain": {
      "type": "boolean"
    },
    "modalRedsys": {
      "type": "boolean"
    },
    "variants": {
      "type": "object",
      "properties": {
        "100171892": {
          "type": "object",
          "properties": {
            "hotelverse": {
              "type": "any"
            }
          }
        },
        "15327367": {
          "type": "object",
          "properties": {
            "hotelverse": {
              "type": "any"
            }
          }
        },
        "100152860": {
          "type": "object",
          "properties": {
            "hotelverse": {
              "type": "any"
            }
          }
        },
        "100376436": {
          "type": "object",
          "properties": {
            "hotelverse": {
              "type": "any"
            }
          }
        },
        "100377194": {
          "type": "object",
          "properties": {
            "pestana": {
              "type": "any"
            },
            "showPriceIncrements": {
              "type": "any"
            }
          }
        },
        "100377444": {
          "type": "object",
          "properties": {
            "pestana": {
              "type": "any"
            }
          }
        },
        "100378056": {
          "type": "object",
          "properties": {
            "pestana": {
              "type": "any"
            },
            "showPriceIncrements": {
              "type": "any"
            }
          }
        },
        "100378057": {
          "type": "object",
          "properties": {
            "pestana": {
              "type": "any"
            },
            "showPriceIncrements": {
              "type": "any"
            }
          }
        },
        "100378058": {
          "type": "object",
          "properties": {
            "pestana": {
              "type": "any"
            }
          }
        },
        "100378059": {
          "type": "object",
          "properties": {
            "pestana": {
              "type": "any"
            },
            "showPriceIncrements": {
              "type": "any"
            }
          }
        },
        "100378060": {
          "type": "object",
          "properties": {
            "pestana": {
              "type": "any"
            }
          }
        },
        "100378061": {
          "type": "object",
          "properties": {
            "pestana": {
              "type": "any"
            }
          }
        },
        "100378062": {
          "type": "object",
          "properties": {
            "pestana": {
              "type": "any"
            }
          }
        },
        "100378063": {
          "type": "object",
          "properties": {
            "pestana": {
              "type": "any"
            }
          }
        },
        "100378102": {
          "type": "object",
          "properties": {
            "pestana": {
              "type": "any"
            },
            "showPriceIncrements": {
              "type": "any"
            }
          }
        },
        "100378106": {
          "type": "object",
          "properties": {
            "pestana": {
              "type": "any"
            },
            "showPriceIncrements": {
              "type": "any"
            }
          }
        },
        "100378108": {
          "type": "object",
          "properties": {
            "pestana": {
              "type": "any"
            },
            "showPriceIncrements": {
              "type": "any"
            }
          }
        },
        "100378209": {
          "type": "object",
          "properties": {
            "pestana": {
              "type": "any"
            },
            "showPriceIncrements": {
              "type": "any"
            }
          }
        },
        "100378241": {
          "type": "object",
          "properties": {
            "pestana": {
              "type": "any"
            },
            "showPriceIncrements": {
              "type": "any"
            }
          }
        },
        "100378242": {
          "type": "object",
          "properties": {
            "pestana": {
              "type": "any"
            },
            "showPriceIncrements": {
              "type": "any"
            }
          }
        }
      }
    }
  }
}
```
### `GET` /api/dictionary
```json
{
  "type": "object",
  "properties": {
    "metasearch.action.upload": {
      "type": "string"
    },
    "core.action.clear": {
      "type": "string"
    },
    "dictionary.label.dashboard": {
      "type": "string"
    },
    "dictionary.label.projects": {
      "type": "string"
    },
    "dictionary.label.users": {
      "type": "string"
    },
    "dictionary.label.keys": {
      "type": "string"
    },
    "core.action.manage_booking": {
      "type": "string"
    },
    "common.label.password": {
      "type": "string"
    },
    "dictionary.confirm.delete_user": {
      "type": "string"
    },
    "intelligence.label.assistant": {
      "type": "string"
    },
    "common.action.new": {
      "type": "string"
    },
    "common.label.others_terms": {
      "type": "string"
    },
    "metasearch.label.drop_file": {
      "type": "string"
    },
    "core.action.edit_booking": {
      "type": "string"
    },
    "dictionary.label.key": {
      "type": "string"
    },
    "dictionary.label.translations": {
      "type": "string"
    },
    "dictionary.label.state": {
      "type": "string"
    },
    "dictionary.label.updated": {
      "type": "string"
    },
    "dictionary.confirm.delete_key": {
      "type": "string"
    },
    "dictionary.action.get_translated_drafts": {
      "type": "string"
    }
  }
}
```
### `GET` /lobby/api/channels/100380929/settings/public
```json
{
  "type": "object",
  "properties": {
    "channelId": {
      "type": "string"
    },
    "channel": {
      "type": "string"
    },
    "type": {
      "type": "string"
    },
    "settings": {
      "type": "object",
      "properties": {
        "ai": {
          "type": "object",
          "properties": {
            "name": {
              "type": "any"
            },
            "avatar": {
              "type": "any"
            },
            "active": {
              "type": "any"
            },
            "tone": {
              "type": "any"
            },
            "captureLead": {
              "type": "any"
            },
            "voice": {
              "type": "any"
            },
            "voiceLocale": {
              "type": "any"
            }
          }
        },
        "twilio": {
          "type": "object",
          "properties": {
            "active": {
              "type": "any"
            },
            "whatsappNumber": {
              "type": "any"
            }
          }
        },
        "web": {
          "type": "object",
          "properties": {
            "left": {
              "type": "any"
            },
            "right": {
              "type": "any"
            },
            "top": {
              "type": "any"
            },
            "bottom": {
              "type": "any"
            },
            "leftMobile": {
              "type": "any"
            },
            "rightMobile": {
              "type": "any"
            },
            "topMobile": {
              "type": "any"
            },
            "bottomMobile": {
              "type": "any"
            }
          }
        }
      }
    },
    "updatedAt": {
      "type": "null"
    }
  }
}
```
### `GET` /api/dictionary
```json
{
  "type": "object",
  "properties": {
    "metasearch.action.upload": {
      "type": "string"
    },
    "core.action.clear": {
      "type": "string"
    },
    "dictionary.label.dashboard": {
      "type": "string"
    },
    "dictionary.label.projects": {
      "type": "string"
    },
    "dictionary.label.users": {
      "type": "string"
    },
    "dictionary.label.keys": {
      "type": "string"
    },
    "core.action.manage_booking": {
      "type": "string"
    },
    "common.label.password": {
      "type": "string"
    },
    "dictionary.confirm.delete_user": {
      "type": "string"
    },
    "intelligence.label.assistant": {
      "type": "string"
    },
    "common.action.new": {
      "type": "string"
    },
    "common.label.others_terms": {
      "type": "string"
    },
    "metasearch.label.drop_file": {
      "type": "string"
    },
    "core.action.edit_booking": {
      "type": "string"
    },
    "dictionary.label.key": {
      "type": "string"
    },
    "dictionary.label.translations": {
      "type": "string"
    },
    "dictionary.label.state": {
      "type": "string"
    },
    "dictionary.label.updated": {
      "type": "string"
    },
    "dictionary.confirm.delete_key": {
      "type": "string"
    },
    "dictionary.action.get_translated_drafts": {
      "type": "string"
    }
  }
}
```
### `GET` /100380929/112026.json
```json
{
  "type": "object",
  "properties": {
    "currency": {
      "type": "string"
    },
    "prices": {
      "type": "object",
      "properties": {
        "14/11/2026": {
          "type": "number"
        },
        "15/11/2026": {
          "type": "number"
        },
        "16/11/2026": {
          "type": "number"
        },
        "17/11/2026": {
          "type": "number"
        },
        "18/11/2026": {
          "type": "number"
        },
        "19/11/2026": {
          "type": "number"
        },
        "20/11/2026": {
          "type": "number"
        },
        "21/11/2026": {
          "type": "number"
        },
        "22/11/2026": {
          "type": "number"
        },
        "23/11/2026": {
          "type": "number"
        },
        "24/11/2026": {
          "type": "number"
        },
        "25/11/2026": {
          "type": "number"
        },
        "26/11/2026": {
          "type": "number"
        },
        "27/11/2026": {
          "type": "number"
        },
        "28/11/2026": {
          "type": "number"
        },
        "29/11/2026": {
          "type": "number"
        },
        "30/11/2026": {
          "type": "number"
        }
      }
    }
  }
}
```

