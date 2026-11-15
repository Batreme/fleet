---
title: "APIs & Protocols: tridentstars-maserati-com_en"
date: 2026-11-14
target: "tridentstars-maserati-com_en"
---

# Discovered APIs & Protocols: tridentstars-maserati-com_en

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/en/_payload.json` | `200` | REST endpoint |
| `GET` | `/_nuxt/builds/meta/8c8596f9-a91b-4c04-9889-10ece88d014b.json` | `200` | REST endpoint |
| `GET` | `/consent/81be852f-f22f-496a-8730-4d261472c4f4/81be852f-f22f-496a-8730-4d261472c4f4.json` | `200` | REST endpoint |
| `GET` | `/cookieconsentpub/v1/geo/location` | `200` | REST endpoint |
| `GET` | `/en/_payload.json` | `200` | REST endpoint |
| `GET` | `/consent/81be852f-f22f-496a-8730-4d261472c4f4/019372ea-d9a6-7eee-b3d5-577ca9e69524/en.json` | `200` | REST endpoint |
| `GET` | `/en/_payload.json` | `200` | REST endpoint |
| `GET` | `/scripttemplates/202411.1.0/assets/otCenterRounded.json` | `200` | REST endpoint |
| `GET` | `/scripttemplates/202411.1.0/assets/v2/otPcCenter.json` | `200` | REST endpoint |
| `GET` | `/consent/81be852f-f22f-496a-8730-4d261472c4f4/81be852f-f22f-496a-8730-4d261472c4f4.json` | `200` | REST endpoint |
| `POST` | `/ee/v1/identity/acquire` | `200` | GraphQL: `AnonymousQuery` |
| `GET` | `/cookieconsentpub/v1/geo/location` | `200` | REST endpoint |
| `POST` | `/ee/irl1/v1/interact` | `200` | GraphQL: `AnonymousQuery` |
| `GET` | `/consent/81be852f-f22f-496a-8730-4d261472c4f4/019372ea-d9a6-7eee-b3d5-577ca9e69524/en.json` | `200` | REST endpoint |
| `GET` | `/scripttemplates/202411.1.0/assets/otCenterRounded.json` | `200` | REST endpoint |
| `GET` | `/scripttemplates/202411.1.0/assets/v2/otPcCenter.json` | `200` | REST endpoint |
| `POST` | `/ee/irl1/v1/interact` | `200` | GraphQL: `AnonymousQuery` |

---

## 📦 Inferred Payload Schemas

### `GET` /en/_payload.json
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "data": {
        "type": "number"
      },
      "prerenderedAt": {
        "type": "number"
      }
    }
  }
}
```
### `GET` /_nuxt/builds/meta/8c8596f9-a91b-4c04-9889-10ece88d014b.json
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
    "prerendered": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  }
}
```
### `GET` /consent/81be852f-f22f-496a-8730-4d261472c4f4/81be852f-f22f-496a-8730-4d261472c4f4.json
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
        "CookieV2BannerLogo": {
          "type": "boolean"
        },
        "ConsentStoreConsentStrings": {
          "type": "boolean"
        },
        "CookieV2AssignTemplateRule": {
          "type": "boolean"
        },
        "MobileAuthenticatedConsents": {
          "type": "boolean"
        },
        "CookieV2GCMDMA": {
          "type": "boolean"
        },
        "CookieV2RemoveSettingsIcon": {
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
### `GET` /en/_payload.json
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "data": {
        "type": "number"
      },
      "prerenderedAt": {
        "type": "number"
      }
    }
  }
}
```
### `GET` /consent/81be852f-f22f-496a-8730-4d261472c4f4/019372ea-d9a6-7eee-b3d5-577ca9e69524/en.json
```json
{
  "type": "object",
  "properties": {
    "DomainData": {
      "type": "object",
      "properties": {
        "pclifeSpanYr": {
          "type": "string"
        },
        "pclifeSpanYrs": {
          "type": "string"
        },
        "pclifeSpanSecs": {
          "type": "string"
        },
        "pclifeSpanWk": {
          "type": "string"
        },
        "pclifeSpanWks": {
          "type": "string"
        },
        "pccontinueWithoutAcceptText": {
          "type": "string"
        },
        "pccloseButtonType": {
          "type": "string"
        },
        "MainText": {
          "type": "string"
        },
        "MainInfoText": {
          "type": "string"
        },
        "AboutText": {
          "type": "string"
        },
        "AboutCookiesText": {
          "type": "string"
        },
        "ConfirmText": {
          "type": "string"
        },
        "AllowAllText": {
          "type": "string"
        },
        "CookiesUsedText": {
          "type": "string"
        },
        "CookiesDescText": {
          "type": "string"
        },
        "AboutLink": {
          "type": "string"
        },
        "ActiveText": {
          "type": "string"
        },
        "AlwaysActiveText": {
          "type": "string"
        },
        "AlwaysInactiveText": {
          "type": "string"
        },
        "PCShowAlwaysActiveToggle": {
          "type": "boolean"
        }
      }
    },
    "CommonData": {
      "type": "object",
      "properties": {
        "pcenterContinueWoAcceptLinkColor": {
          "type": "string"
        },
        "IabThirdPartyCookieUrl": {
          "type": "string"
        },
        "OptanonHideAcceptButton": {
          "type": "string"
        },
        "OptanonStyle": {
          "type": "string"
        },
        "OptanonStaticContentLocation": {
          "type": "string"
        },
        "BannerCustomCSS": {
          "type": "string"
        },
        "PCCustomCSS": {
          "type": "string"
        },
        "PcTextColor": {
          "type": "string"
        },
        "PcButtonColor": {
          "type": "string"
        },
        "PcButtonTextColor": {
          "type": "string"
        },
        "PcBackgroundColor": {
          "type": "string"
        },
        "PcMenuColor": {
          "type": "string"
        },
        "PcMenuHighLightColor": {
          "type": "string"
        },
        "PcAccordionBackgroundColor": {
          "type": "string"
        },
        "PCenterExpandToViewText": {
          "type": "string"
        },
        "PcEnableToggles": {
          "type": "boolean"
        },
        "PcLinksTextColor": {
          "type": "string"
        },
        "TextColor": {
          "type": "string"
        },
        "ButtonColor": {
          "type": "string"
        },
        "BannerMPButtonColor": {
          "type": "string"
        }
      }
    },
    "NtfyConfig": {
      "type": "object",
      "properties": {
        "ShowNtfy": {
          "type": "boolean"
        },
        "NtfyDuration": {
          "type": "number"
        },
        "ShowCS": {
          "type": "boolean"
        },
        "CSType": {
          "type": "string"
        },
        "CSTxt": {
          "type": "string"
        },
        "Sync": {
          "type": "object",
          "properties": {
            "Title": {
              "type": "any"
            },
            "TitleAlign": {
              "type": "any"
            },
            "TitleColor": {
              "type": "any"
            },
            "Desc": {
              "type": "any"
            },
            "DescAlign": {
              "type": "any"
            },
            "DescColor": {
              "type": "any"
            },
            "BgColor": {
              "type": "any"
            },
            "BdrColor": {
              "type": "any"
            },
            "IconBgColor": {
              "type": "any"
            },
            "ShowClose": {
              "type": "any"
            },
            "CloseAria": {
              "type": "any"
            },
            "ShowIcon": {
              "type": "any"
            }
          }
        },
        "Complete": {
          "type": "object",
          "properties": {
            "Title": {
              "type": "any"
            },
            "TitleAlign": {
              "type": "any"
            },
            "TitleColor": {
              "type": "any"
            },
            "Desc": {
              "type": "any"
            },
            "DescAlign": {
              "type": "any"
            },
            "DescColor": {
              "type": "any"
            },
            "BgColor": {
              "type": "any"
            },
            "BdrColor": {
              "type": "any"
            },
            "IconBgColor": {
              "type": "any"
            },
            "ShowClose": {
              "type": "any"
            },
            "CloseAria": {
              "type": "any"
            },
            "ShowIcon": {
              "type": "any"
            }
          }
        },
        "CSButton": {
          "type": "object",
          "properties": {
            "Color": {
              "type": "any"
            },
            "BgColor": {
              "type": "any"
            },
            "BdrColor": {
              "type": "any"
            },
            "Align": {
              "type": "any"
            }
          }
        },
        "CSLink": {
          "type": "object",
          "properties": {
            "Color": {
              "type": "any"
            },
            "Align": {
              "type": "any"
            }
          }
        }
      }
    },
    "OTTData": {
      "type": "null"
    },
    "MobileData": {
      "type": "null"
    }
  }
}
```
### `GET` /en/_payload.json
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "data": {
        "type": "number"
      },
      "prerenderedAt": {
        "type": "number"
      }
    }
  }
}
```
### `GET` /scripttemplates/202411.1.0/assets/otCenterRounded.json
```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "html": {
      "type": "string"
    },
    "css": {
      "type": "string"
    }
  }
}
```
### `GET` /scripttemplates/202411.1.0/assets/v2/otPcCenter.json
```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "html": {
      "type": "string"
    },
    "css": {
      "type": "string"
    }
  }
}
```
### `GET` /consent/81be852f-f22f-496a-8730-4d261472c4f4/81be852f-f22f-496a-8730-4d261472c4f4.json
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
        "CookieV2BannerLogo": {
          "type": "boolean"
        },
        "ConsentStoreConsentStrings": {
          "type": "boolean"
        },
        "CookieV2AssignTemplateRule": {
          "type": "boolean"
        },
        "MobileAuthenticatedConsents": {
          "type": "boolean"
        },
        "CookieV2GCMDMA": {
          "type": "boolean"
        },
        "CookieV2RemoveSettingsIcon": {
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

