---
title: "APIs & Protocols: ringpopcandy-com"
date: 2026-11-14
target: "[[overview|ringpopcandy-com]]"
---

# Discovered APIs & Protocols: ringpopcandy-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/cdn/shopifycloud/storefront/assets/storefront/storefronts.moderate.specrules-eb468f32.json` | `200` | REST endpoint |
| `GET` | `/consent/01a019ee-727f-79aa-945b-b1819f8381ac/01a019ee-727f-79aa-945b-b1819f8381ac.json` | `200` | REST endpoint |
| `GET` | `/scripttemplates/202607.1.0/sri-hashes.json` | `200` | REST endpoint |
| `GET` | `/shopifycloud/shop-js/modules/v2/loader.init-shop-cart-sync.en.esm.js` | `200` | REST endpoint |
| `GET` | `/shopifycloud/shop-js/modules/v2/client.init-shop-cart-sync_B_uppJgi.en.esm.js` | `200` | REST endpoint |
| `GET` | `/shopifycloud/shop-js/modules/v2/chunk.document_DMcRsBXN.esm.js` | `200` | REST endpoint |
| `GET` | `/shopifycloud/shop-js/modules/v2/chunk.window_CAbVMZox.esm.js` | `200` | REST endpoint |
| `GET` | `/shopifycloud/shop-js/modules/v2/chunk.init_C-ooJD99.esm.js` | `200` | REST endpoint |
| `GET` | `/shopifycloud/shop-js/modules/v2/chunk.register_CWAkTP1C.esm.js` | `200` | REST endpoint |
| `GET` | `/shopifycloud/shop-js/modules/v2/chunk.networkErrorMessages_Du380vAr.esm.js` | `200` | REST endpoint |
| `GET` | `/shopifycloud/shop-js/modules/v2/client.shop-cart-sync_BkYDJPZz.en.esm.js` | `200` | REST endpoint |
| `GET` | `/shopifycloud/shop-js/modules/v2/chunk.defineInitFunction_DyjeAYT_.esm.js` | `200` | REST endpoint |
| `GET` | `/shopifycloud/shop-js/modules/v2/chunk.casing_U_9x-Om3.esm.js` | `200` | REST endpoint |
| `GET` | `/shopifycloud/shop-js/modules/v2/chunk.v4_C3N_0s0v.esm.js` | `200` | REST endpoint |
| `GET` | `/shopifycloud/shop-js/modules/v2/chunk.utils_Cjeq_SSZ.esm.js` | `200` | REST endpoint |
| `GET` | `/shopifycloud/shop-js/modules/v2/chunk.useUserRecognitionSignal_D_xRcsqT.esm.js` | `200` | REST endpoint |
| `GET` | `/shopifycloud/shop-js/modules/v2/chunk.storage_n5jjEbMM.esm.js` | `200` | REST endpoint |
| `GET` | `/shopifycloud/shop-js/modules/v2/chunk.hooks_hUU__FPJ.esm.js` | `200` | REST endpoint |
| `GET` | `/shopifycloud/shop-js/modules/v2/chunk.authorize_DINGMyE5.esm.js` | `200` | REST endpoint |
| `GET` | `/shopifycloud/shop-js/modules/v2/chunk.useEventListener_DWE4XdI5.esm.js` | `200` | REST endpoint |
| `GET` | `/shopifycloud/shop-js/modules/v2/chunk.validators_BbO3UEjF.esm.js` | `200` | REST endpoint |
| `POST` | `/v1/metrics` | `200` | REST endpoint |
| `POST` | `/api/collect` | `204` | REST endpoint |
| `GET` | `/consent/01a019ee-727f-79aa-945b-b1819f8381ac/0195407d-bddb-7eca-87f0-fd0591f8b1f8/en.json` | `200` | REST endpoint |
| `GET` | `/collections/all/products.json` | `200` | REST endpoint |
| `POST` | `/v1/metrics` | `200` | REST endpoint |
| `POST` | `/v1/metrics` | `200` | REST endpoint |
| `GET` | `/scripttemplates/202607.1.0/assets/otFlat.json` | `200` | REST endpoint |
| `GET` | `/scripttemplates/202607.1.0/assets/v2/otPcTab.json` | `200` | REST endpoint |
| `GET` | `/collections/all/products.json` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /cdn/shopifycloud/storefront/assets/storefront/storefronts.moderate.specrules-eb468f32.json
```json
{
  "type": "object",
  "properties": {
    "tag": {
      "type": "string"
    },
    "prefetch": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "where": {
            "type": "any"
          },
          "eagerness": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `GET` /consent/01a019ee-727f-79aa-945b-b1819f8381ac/01a019ee-727f-79aa-945b-b1819f8381ac.json
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
        "CookieV2GPC": {
          "type": "boolean"
        },
        "CookieV2GeolocationJsonApi": {
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
        "CookieV2AssignTemplateRule": {
          "type": "boolean"
        },
        "CookiesV2TCF2.3Adoption": {
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
### `GET` /scripttemplates/202607.1.0/sri-hashes.json
```json
{
  "type": "object",
  "properties": {
    "hbbtv.js": {
      "type": "string"
    },
    "otBannerSdk.js": {
      "type": "string"
    },
    "otConfirmDialog.js": {
      "type": "string"
    },
    "otGPP.js": {
      "type": "string"
    },
    "otSDKBlock.js": {
      "type": "string"
    },
    "otSDKStub.js": {
      "type": "string"
    },
    "otStub.js": {
      "type": "string"
    },
    "otTCF.js": {
      "type": "string"
    },
    "trackingTechnologies.js": {
      "type": "string"
    }
  }
}
```

