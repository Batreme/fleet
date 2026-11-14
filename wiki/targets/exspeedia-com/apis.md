---
title: "APIs & Protocols: exspeedia-com"
date: 2026-11-14
target: "[[overview|exspeedia-com]]"
---

# Discovered APIs & Protocols: exspeedia-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/consent/019d9c05-c22b-757a-b891-7504a134d1dd/019d9c05-c22b-757a-b891-7504a134d1dd.json` | `200` | REST endpoint |
| `GET` | `/cookieconsentpub/v1/geo/location` | `200` | REST endpoint |
| `GET` | `/api/world` | `200` | REST endpoint |
| `GET` | `/api/tours` | `200` | REST endpoint |
| `GET` | `/api/achievements` | `200` | REST endpoint |
| `GET` | `/api/expedia/domains` | `200` | REST endpoint |
| `GET` | `/api/intro-clips` | `200` | REST endpoint |
| `GET` | `/video/upload/w_256,q_auto:eco/v1/exspeedia/intro/01KW9K4JYKKW3PV052N7MMRD67.mp4` | `206` | REST endpoint |
| `GET` | `/video/upload/w_256,q_auto:eco/v1/exspeedia/intro/01KW9K4JYKKW3PV052N7MMRD67.mp4` | `206` | REST endpoint |
| `GET` | `/video/upload/w_256,q_auto:eco/v1/exspeedia/intro/01KW9K4JYKKW3PV052N7MMRD67.mp4` | `206` | REST endpoint |
| `GET` | `/video/upload/w_256,q_auto:eco/v1/exspeedia/intro/01KW9K4JYKKW3PV052N7MMRD67.mp4` | `206` | REST endpoint |
| `GET` | `/video/upload/w_256,q_auto:eco/v1/exspeedia/intro/01KW9K4JYKKW3PV052N7MMRD67.mp4` | `206` | REST endpoint |
| `GET` | `/video/upload/w_256,q_auto:eco/v1/exspeedia/intro/01KW9K4JYKKW3PV052N7MMRD67.mp4` | `206` | REST endpoint |
| `GET` | `/video/upload/w_256,q_auto:eco/v1/exspeedia/intro/01KW9K4JYKKW3PV052N7MMRD67.mp4` | `206` | REST endpoint |
| `GET` | `/video/upload/w_256,q_auto:eco/v1/exspeedia/intro/01KW9K4JYKKW3PV052N7MMRD67.mp4` | `206` | REST endpoint |
| `GET` | `/video/upload/w_256,q_auto:eco/v1/exspeedia/intro/01KW9K597VSH2004YKZV4YRYX5.mp4` | `206` | REST endpoint |
| `GET` | `/video/upload/w_256,q_auto:eco/v1/exspeedia/intro/01KW9K523EG3YEBV907ZFXW7QH.mp4` | `206` | REST endpoint |
| `GET` | `/video/upload/w_256,q_auto:eco/v1/exspeedia/intro/01KW9K5T95KF5ACPFS71S8EWW8.mp4` | `206` | REST endpoint |
| `GET` | `/video/upload/w_256,q_auto:eco/v1/exspeedia/intro/01KW9K5M04S5NXZYS3GBNHX08W.mp4` | `206` | REST endpoint |
| `GET` | `/video/upload/w_256,q_auto:eco/v1/exspeedia/intro/01KW9K5EV1ADMR6JGFEJ2DKP8B.mp4` | `206` | REST endpoint |
| `GET` | `/video/upload/w_256,q_auto:eco/v1/exspeedia/intro/01KW9K4VA0XC7K9AXZMG8WCKJW.mp4` | `206` | REST endpoint |
| `GET` | `/threejs/data/world-043026.json` | `200` | REST endpoint |
| `GET` | `/consent/019d9c05-c22b-757a-b891-7504a134d1dd/018f3b33-511c-7d68-b6ae-9358fec5b9e3/en.json` | `200` | REST endpoint |
| `GET` | `/scripttemplates/202603.1.0/assets/otFlat.json` | `200` | REST endpoint |
| `GET` | `/scripttemplates/202603.1.0/assets/v2/otPcPanel.json` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /consent/019d9c05-c22b-757a-b891-7504a134d1dd/019d9c05-c22b-757a-b891-7504a134d1dd.json
```json
{
  "type": "object",
  "properties": {
    "CookieSPAEnabled": {
      "type": "boolean"
    },
    "CookieSameSiteNoneEnabled": {
      "type": "boolean"
    },
    "CookieV2CSPEnabled": {
      "type": "boolean"
    },
    "MultiVariantTestingEnabled": {
      "type": "boolean"
    },
    "UseV2": {
      "type": "boolean"
    },
    "MobileSDK": {
      "type": "boolean"
    },
    "SkipGeolocation": {
      "type": "boolean"
    },
    "ScriptType": {
      "type": "string"
    },
    "Version": {
      "type": "string"
    },
    "OptanonDataJSON": {
      "type": "string"
    },
    "GeolocationUrl": {
      "type": "string"
    },
    "BulkDomainCheckUrl": {
      "type": "string"
    },
    "RuleSet": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "Id": {
            "type": "any"
          },
          "Name": {
            "type": "any"
          },
          "Countries": {
            "type": "any"
          },
          "States": {
            "type": "any"
          },
          "LanguageSwitcherPlaceholder": {
            "type": "any"
          },
          "BannerPushesDown": {
            "type": "any"
          },
          "Default": {
            "type": "any"
          },
          "Global": {
            "type": "any"
          },
          "Type": {
            "type": "any"
          },
          "UseGoogleVendors": {
            "type": "any"
          },
          "VariantEnabled": {
            "type": "any"
          },
          "TestEndTime": {
            "type": "any"
          },
          "Variants": {
            "type": "any"
          },
          "TemplateName": {
            "type": "any"
          },
          "Conditions": {
            "type": "any"
          },
          "GCEnable": {
            "type": "any"
          },
          "IsGPPEnabled": {
            "type": "any"
          },
          "EnableJWTAuthForKnownUsers": {
            "type": "any"
          }
        }
      }
    },
    "IabData": {
      "type": "object",
      "properties": {
        "cookieVersion": {
          "type": "string"
        },
        "createdTime": {
          "type": "string"
        },
        "updatedTime": {
          "type": "string"
        },
        "cmpId": {
          "type": "string"
        },
        "cmpVersion": {
          "type": "string"
        },
        "consentScreen": {
          "type": "string"
        },
        "consentLanguage": {
          "type": "null"
        },
        "vendorListVersion": {
          "type": "number"
        },
        "maxVendorId": {
          "type": "number"
        },
        "encodingType": {
          "type": "string"
        },
        "globalVendorListUrl": {
          "type": "string"
        }
      }
    },
    "IabV2Data": {
      "type": "object",
      "properties": {
        "cookieVersion": {
          "type": "string"
        },
        "createdTime": {
          "type": "string"
        },
        "updatedTime": {
          "type": "string"
        },
        "cmpId": {
          "type": "string"
        },
        "cmpVersion": {
          "type": "string"
        },
        "consentScreen": {
          "type": "string"
        },
        "consentLanguage": {
          "type": "null"
        },
        "vendorListVersion": {
          "type": "number"
        },
        "maxVendorId": {
          "type": "number"
        },
        "encodingType": {
          "type": "string"
        },
        "globalVendorListUrl": {
          "type": "string"
        }
      }
    },
    "Iab2V2Data": {
      "type": "object",
      "properties": {
        "cookieVersion": {
          "type": "string"
        },
        "createdTime": {
          "type": "string"
        },
        "updatedTime": {
          "type": "string"
        },
        "cmpId": {
          "type": "string"
        },
        "cmpVersion": {
          "type": "string"
        },
        "consentScreen": {
          "type": "string"
        },
        "consentLanguage": {
          "type": "null"
        },
        "vendorListVersion": {
          "type": "number"
        },
        "maxVendorId": {
          "type": "number"
        },
        "encodingType": {
          "type": "string"
        },
        "globalVendorListUrl": {
          "type": "string"
        }
      }
    },
    "GoogleData": {
      "type": "object",
      "properties": {
        "vendorListVersion": {
          "type": "number"
        },
        "googleVendorListUrl": {
          "type": "string"
        }
      }
    },
    "ScriptDynamicLoadEnabled": {
      "type": "boolean"
    },
    "TenantFeatures": {
      "type": "object",
      "properties": {
        "CookieV2BannerFocus": {
          "type": "boolean"
        },
        "CookieV2RejectAll": {
          "type": "boolean"
        },
        "CookieV2TargetedTemplates": {
          "type": "boolean"
        },
        "CookieV2GPC": {
          "type": "boolean"
        },
        "CookieV2GeolocationJsonApi": {
          "type": "boolean"
        },
        "WebButtonCustomisations": {
          "type": "boolean"
        },
        "CookieV2TCF21": {
          "type": "boolean"
        },
        "CookieV2SkipCategory": {
          "type": "boolean"
        },
        "CookieV2BannerLogo": {
          "type": "boolean"
        },
        "ConsentStoreConsentStrings": {
          "type": "boolean"
        },
        "features.cmp-amazon-consent-Signal": {
          "type": "boolean"
        },
        "CookiesV2TCF2.3Adoption": {
          "type": "boolean"
        },
        "CookieV2AssignTemplateRule": {
          "type": "boolean"
        },
        "MobileAuthenticatedConsents": {
          "type": "boolean"
        },
        "CookieV2MicrosoftUET": {
          "type": "boolean"
        },
        "CookieV2GCMDMA": {
          "type": "boolean"
        },
        "CookieV2RemoveSettingsIcon": {
          "type": "boolean"
        },
        "CookieV2NewConsentReceiptAPI": {
          "type": "boolean"
        },
        "CookieV2GeneralVendors": {
          "type": "boolean"
        },
        "CookieV2GPP": {
          "type": "boolean"
        }
      }
    },
    "IsSuppressBanner": {
      "type": "boolean"
    }
  }
}
```
### `GET` /cookieconsentpub/v1/geo/location
```json
{
  "type": "object",
  "properties": {
    "country": {
      "type": "string"
    },
    "state": {
      "type": "string"
    },
    "stateName": {
      "type": "string"
    },
    "continent": {
      "type": "string"
    }
  }
}
```
### `GET` /api/world
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "name": {
        "type": "string"
      },
      "code": {
        "type": "string"
      },
      "countries": {
        "type": "array",
        "items": {
          "type": "any"
        }
      }
    }
  }
}
```
### `GET` /api/tours
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "name": {
        "type": "string"
      },
      "slug": {
        "type": "string"
      },
      "stops": {
        "type": "array",
        "items": {
          "type": "any"
        }
      }
    }
  }
}
```
### `GET` /api/achievements
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "id": {
        "type": "string"
      },
      "name": {
        "type": "string"
      },
      "slug": {
        "type": "string"
      },
      "icon": {
        "type": "string"
      },
      "levels": {
        "type": "array",
        "items": {
          "type": "any"
        }
      }
    }
  }
}
```
### `GET` /api/expedia/domains
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "url": {
        "type": "string"
      },
      "country": {
        "type": "object",
        "properties": {
          "id": {
            "type": "any"
          },
          "code_a2": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `GET` /api/intro-clips
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "video": {
        "type": "string"
      },
      "thumb": {
        "type": "string"
      },
      "poster": {
        "type": "string"
      }
    }
  }
}
```

