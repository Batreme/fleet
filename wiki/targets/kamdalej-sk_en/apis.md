---
title: "APIs & Protocols: kamdalej-sk_en"
date: 2026-11-14
target: "[[overview|kamdalej-sk_en]]"
---

# Discovered APIs & Protocols: kamdalej-sk_en

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/consent/019c98a8-e583-7fb5-a62e-f9ff4028352b/019c98a8-e583-7fb5-a62e-f9ff4028352b.json` | `200` | REST endpoint |
| `GET` | `/cookieconsentpub/v1/geo/location` | `200` | REST endpoint |
| `GET` | `/backend/api/global-init` | `200` | REST endpoint |
| `GET` | `/backend/api/links` | `200` | REST endpoint |
| `GET` | `/backend/api/page-init` | `200` | REST endpoint |
| `GET` | `/consent/019c98a8-e583-7fb5-a62e-f9ff4028352b/0199297b-f4f7-7204-bde5-f87a8ac2909a/en-gb.json` | `200` | REST endpoint |
| `GET` | `/scripttemplates/202603.1.0/assets/otCenterRounded.json` | `200` | REST endpoint |
| `GET` | `/scripttemplates/202603.1.0/assets/v2/otPcTab.json` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /consent/019c98a8-e583-7fb5-a62e-f9ff4028352b/019c98a8-e583-7fb5-a62e-f9ff4028352b.json
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
        "CookieV2CSP": {
          "type": "boolean"
        },
        "CookiesSameSiteNone": {
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
### `GET` /backend/api/global-init
```json
{
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "message": {
      "type": "string"
    },
    "data": {
      "type": "object",
      "properties": {
        "translations": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "menus": {
          "type": "object",
          "properties": {
            "head": {
              "type": "any"
            },
            "footer": {
              "type": "any"
            }
          }
        }
      }
    }
  }
}
```
### `GET` /backend/api/links
```json
{
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "message": {
      "type": "string"
    },
    "data": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "any"
          },
          "labelEn": {
            "type": "any"
          },
          "labelUk": {
            "type": "any"
          },
          "labelSk": {
            "type": "any"
          },
          "linkEn": {
            "type": "any"
          },
          "linkSk": {
            "type": "any"
          },
          "linkUk": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `GET` /backend/api/page-init
```json
{
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "message": {
      "type": "string"
    },
    "data": {
      "type": "object",
      "properties": {
        "page": {
          "type": "object",
          "properties": {
            "id": {
              "type": "any"
            },
            "titleEn": {
              "type": "any"
            },
            "titleUk": {
              "type": "any"
            },
            "titleSk": {
              "type": "any"
            },
            "slugEn": {
              "type": "any"
            },
            "slugUk": {
              "type": "any"
            },
            "slugSk": {
              "type": "any"
            },
            "heroEn": {
              "type": "any"
            },
            "heroUk": {
              "type": "any"
            },
            "heroSk": {
              "type": "any"
            },
            "heroContentEn": {
              "type": "any"
            },
            "heroContentUk": {
              "type": "any"
            },
            "heroContentSk": {
              "type": "any"
            },
            "image": {
              "type": "any"
            },
            "imageMobile": {
              "type": "any"
            },
            "partnerBannersHeadlineEn": {
              "type": "any"
            },
            "partnerBannersHeadlineUk": {
              "type": "any"
            },
            "partnerBannersHeadlineSk": {
              "type": "any"
            },
            "partnerBannersDescriptionEn": {
              "type": "any"
            },
            "partnerBannersDescriptionUk": {
              "type": "any"
            }
          }
        },
        "seo": {
          "type": "object",
          "properties": {
            "title": {
              "type": "any"
            },
            "description": {
              "type": "any"
            },
            "image": {
              "type": "any"
            },
            "url": {
              "type": "any"
            }
          }
        }
      }
    }
  }
}
```
### `GET` /consent/019c98a8-e583-7fb5-a62e-f9ff4028352b/0199297b-f4f7-7204-bde5-f87a8ac2909a/en-gb.json
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
### `GET` /scripttemplates/202603.1.0/assets/otCenterRounded.json
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
### `GET` /scripttemplates/202603.1.0/assets/v2/otPcTab.json
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

