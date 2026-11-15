---
title: "APIs & Protocols: arcteryx-com_us-en-explore-system0"
date: 2026-11-14
target: "arcteryx-com_us-en-explore-system0"
---

# Discovered APIs & Protocols: arcteryx-com_us-en-explore-system0

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/consent/001f551c-85d9-46c2-b1d6-b0a70f84d759/001f551c-85d9-46c2-b1d6-b0a70f84d759.json` | `200` | REST endpoint |
| `GET` | `/cookieconsentpub/v1/geo/location` | `200` | REST endpoint |
| `GET` | `/consent/001f551c-85d9-46c2-b1d6-b0a70f84d759/019dfaaf-4154-7197-8852-4a6b5d5bfc59/en.json` | `200` | REST endpoint |
| `GET` | `/vendorlist/iab2V2Data.json` | `200` | REST endpoint |
| `GET` | `/scripttemplates/202605.1.0/assets/otFloatingRoundedCorner.json` | `200` | REST endpoint |
| `GET` | `/scripttemplates/202605.1.0/assets/v2/otPcTab.json` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /consent/001f551c-85d9-46c2-b1d6-b0a70f84d759/001f551c-85d9-46c2-b1d6-b0a70f84d759.json
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
### `GET` /consent/001f551c-85d9-46c2-b1d6-b0a70f84d759/019dfaaf-4154-7197-8852-4a6b5d5bfc59/en.json
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
### `GET` /vendorlist/iab2V2Data.json
```json
{
  "type": "object",
  "properties": {
    "standardTexts": {
      "type": "object",
      "properties": {
        "features": {
          "type": "string"
        }
      }
    },
    "features": {
      "type": "object",
      "properties": {
        "1": {
          "type": "object",
          "properties": {
            "illustrations": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "description": {
              "type": "any"
            },
            "id": {
              "type": "any"
            }
          }
        },
        "2": {
          "type": "object",
          "properties": {
            "illustrations": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "description": {
              "type": "any"
            },
            "id": {
              "type": "any"
            }
          }
        },
        "3": {
          "type": "object",
          "properties": {
            "illustrations": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "description": {
              "type": "any"
            },
            "id": {
              "type": "any"
            }
          }
        }
      }
    },
    "lastUpdated": {
      "type": "string"
    },
    "specialFeatures": {
      "type": "object",
      "properties": {
        "1": {
          "type": "object",
          "properties": {
            "illustrations": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "description": {
              "type": "any"
            },
            "id": {
              "type": "any"
            }
          }
        },
        "2": {
          "type": "object",
          "properties": {
            "illustrations": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "description": {
              "type": "any"
            },
            "id": {
              "type": "any"
            }
          }
        }
      }
    },
    "gvlSpecificationVersion": {
      "type": "number"
    },
    "specialPurposes": {
      "type": "object",
      "properties": {
        "1": {
          "type": "object",
          "properties": {
            "illustrations": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "description": {
              "type": "any"
            },
            "id": {
              "type": "any"
            }
          }
        },
        "2": {
          "type": "object",
          "properties": {
            "illustrations": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "description": {
              "type": "any"
            },
            "id": {
              "type": "any"
            }
          }
        },
        "3": {
          "type": "object",
          "properties": {
            "illustrations": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "description": {
              "type": "any"
            },
            "id": {
              "type": "any"
            }
          }
        }
      }
    },
    "vendorListVersion": {
      "type": "number"
    },
    "purposes": {
      "type": "object",
      "properties": {
        "11": {
          "type": "object",
          "properties": {
            "illustrations": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "description": {
              "type": "any"
            },
            "id": {
              "type": "any"
            }
          }
        },
        "1": {
          "type": "object",
          "properties": {
            "illustrations": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "description": {
              "type": "any"
            },
            "id": {
              "type": "any"
            }
          }
        },
        "2": {
          "type": "object",
          "properties": {
            "illustrations": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "description": {
              "type": "any"
            },
            "id": {
              "type": "any"
            }
          }
        },
        "3": {
          "type": "object",
          "properties": {
            "illustrations": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "description": {
              "type": "any"
            },
            "id": {
              "type": "any"
            }
          }
        },
        "4": {
          "type": "object",
          "properties": {
            "illustrations": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "description": {
              "type": "any"
            },
            "id": {
              "type": "any"
            }
          }
        },
        "5": {
          "type": "object",
          "properties": {
            "illustrations": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "description": {
              "type": "any"
            },
            "id": {
              "type": "any"
            }
          }
        },
        "6": {
          "type": "object",
          "properties": {
            "illustrations": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "description": {
              "type": "any"
            },
            "id": {
              "type": "any"
            }
          }
        },
        "7": {
          "type": "object",
          "properties": {
            "illustrations": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "description": {
              "type": "any"
            },
            "id": {
              "type": "any"
            }
          }
        },
        "8": {
          "type": "object",
          "properties": {
            "illustrations": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "description": {
              "type": "any"
            },
            "id": {
              "type": "any"
            }
          }
        },
        "9": {
          "type": "object",
          "properties": {
            "illustrations": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "description": {
              "type": "any"
            },
            "id": {
              "type": "any"
            }
          }
        },
        "10": {
          "type": "object",
          "properties": {
            "illustrations": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "description": {
              "type": "any"
            },
            "id": {
              "type": "any"
            }
          }
        }
      }
    },
    "stacks": {
      "type": "object",
      "properties": {
        "22": {
          "type": "object",
          "properties": {
            "specialFeatures": {
              "type": "any"
            },
            "purposes": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "description": {
              "type": "any"
            },
            "id": {
              "type": "any"
            }
          }
        },
        "44": {
          "type": "object",
          "properties": {
            "specialFeatures": {
              "type": "any"
            },
            "purposes": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "description": {
              "type": "any"
            },
            "id": {
              "type": "any"
            }
          }
        },
        "23": {
          "type": "object",
          "properties": {
            "specialFeatures": {
              "type": "any"
            },
            "purposes": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "description": {
              "type": "any"
            },
            "id": {
              "type": "any"
            }
          }
        },
        "45": {
          "type": "object",
          "properties": {
            "specialFeatures": {
              "type": "any"
            },
            "purposes": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "description": {
              "type": "any"
            },
            "id": {
              "type": "any"
            }
          }
        },
        "24": {
          "type": "object",
          "properties": {
            "specialFeatures": {
              "type": "any"
            },
            "purposes": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "description": {
              "type": "any"
            },
            "id": {
              "type": "any"
            }
          }
        },
        "25": {
          "type": "object",
          "properties": {
            "specialFeatures": {
              "type": "any"
            },
            "purposes": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "description": {
              "type": "any"
            },
            "id": {
              "type": "any"
            }
          }
        },
        "26": {
          "type": "object",
          "properties": {
            "specialFeatures": {
              "type": "any"
            },
            "purposes": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "description": {
              "type": "any"
            },
            "id": {
              "type": "any"
            }
          }
        },
        "27": {
          "type": "object",
          "properties": {
            "specialFeatures": {
              "type": "any"
            },
            "purposes": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "description": {
              "type": "any"
            },
            "id": {
              "type": "any"
            }
          }
        },
        "28": {
          "type": "object",
          "properties": {
            "specialFeatures": {
              "type": "any"
            },
            "purposes": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "description": {
              "type": "any"
            },
            "id": {
              "type": "any"
            }
          }
        },
        "29": {
          "type": "object",
          "properties": {
            "specialFeatures": {
              "type": "any"
            },
            "purposes": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "description": {
              "type": "any"
            },
            "id": {
              "type": "any"
            }
          }
        },
        "30": {
          "type": "object",
          "properties": {
            "specialFeatures": {
              "type": "any"
            },
            "purposes": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "description": {
              "type": "any"
            },
            "id": {
              "type": "any"
            }
          }
        },
        "31": {
          "type": "object",
          "properties": {
            "specialFeatures": {
              "type": "any"
            },
            "purposes": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "description": {
              "type": "any"
            },
            "id": {
              "type": "any"
            }
          }
        },
        "10": {
          "type": "object",
          "properties": {
            "specialFeatures": {
              "type": "any"
            },
            "purposes": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "description": {
              "type": "any"
            },
            "id": {
              "type": "any"
            }
          }
        },
        "32": {
          "type": "object",
          "properties": {
            "specialFeatures": {
              "type": "any"
            },
            "purposes": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "description": {
              "type": "any"
            },
            "id": {
              "type": "any"
            }
          }
        },
        "11": {
          "type": "object",
          "properties": {
            "specialFeatures": {
              "type": "any"
            },
            "purposes": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "description": {
              "type": "any"
            },
            "id": {
              "type": "any"
            }
          }
        },
        "33": {
          "type": "object",
          "properties": {
            "specialFeatures": {
              "type": "any"
            },
            "purposes": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "description": {
              "type": "any"
            },
            "id": {
              "type": "any"
            }
          }
        },
        "12": {
          "type": "object",
          "properties": {
            "specialFeatures": {
              "type": "any"
            },
            "purposes": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "description": {
              "type": "any"
            },
            "id": {
              "type": "any"
            }
          }
        },
        "34": {
          "type": "object",
          "properties": {
            "specialFeatures": {
              "type": "any"
            },
            "purposes": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "description": {
              "type": "any"
            },
            "id": {
              "type": "any"
            }
          }
        },
        "13": {
          "type": "object",
          "properties": {
            "specialFeatures": {
              "type": "any"
            },
            "purposes": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "description": {
              "type": "any"
            },
            "id": {
              "type": "any"
            }
          }
        },
        "35": {
          "type": "object",
          "properties": {
            "specialFeatures": {
              "type": "any"
            },
            "purposes": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "description": {
              "type": "any"
            },
            "id": {
              "type": "any"
            }
          }
        }
      }
    },
    "tcfPolicyVersion": {
      "type": "number"
    },
    "vendors": {
      "type": "object",
      "properties": {
        "1462": {
          "type": "object",
          "properties": {
            "iab2V2GVLVersion": {
              "type": "any"
            },
            "features": {
              "type": "any"
            },
            "specialFeatures": {
              "type": "any"
            },
            "urls": {
              "type": "any"
            },
            "dataRetention": {
              "type": "any"
            },
            "usesNonCookieAccess": {
              "type": "any"
            },
            "legIntPurposes": {
              "type": "any"
            },
            "specialPurposes": {
              "type": "any"
            },
            "purposes": {
              "type": "any"
            },
            "deviceStorageDisclosureUrl": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "id": {
              "type": "any"
            },
            "flexiblePurposes": {
              "type": "any"
            },
            "dataDeclaration": {
              "type": "any"
            }
          }
        },
        "1461": {
          "type": "object",
          "properties": {
            "iab2V2GVLVersion": {
              "type": "any"
            },
            "features": {
              "type": "any"
            },
            "specialFeatures": {
              "type": "any"
            },
            "urls": {
              "type": "any"
            },
            "dataRetention": {
              "type": "any"
            },
            "usesNonCookieAccess": {
              "type": "any"
            },
            "legIntPurposes": {
              "type": "any"
            },
            "specialPurposes": {
              "type": "any"
            },
            "purposes": {
              "type": "any"
            },
            "deviceStorageDisclosureUrl": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "cookieMaxAgeSeconds": {
              "type": "any"
            },
            "id": {
              "type": "any"
            },
            "flexiblePurposes": {
              "type": "any"
            },
            "dataDeclaration": {
              "type": "any"
            }
          }
        },
        "1460": {
          "type": "object",
          "properties": {
            "iab2V2GVLVersion": {
              "type": "any"
            },
            "features": {
              "type": "any"
            },
            "specialFeatures": {
              "type": "any"
            },
            "urls": {
              "type": "any"
            },
            "dataRetention": {
              "type": "any"
            },
            "usesNonCookieAccess": {
              "type": "any"
            },
            "legIntPurposes": {
              "type": "any"
            },
            "specialPurposes": {
              "type": "any"
            },
            "purposes": {
              "type": "any"
            },
            "deviceStorageDisclosureUrl": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "cookieMaxAgeSeconds": {
              "type": "any"
            },
            "id": {
              "type": "any"
            },
            "flexiblePurposes": {
              "type": "any"
            },
            "dataDeclaration": {
              "type": "any"
            }
          }
        },
        "1217": {
          "type": "object",
          "properties": {
            "iab2V2GVLVersion": {
              "type": "any"
            },
            "features": {
              "type": "any"
            },
            "specialFeatures": {
              "type": "any"
            },
            "urls": {
              "type": "any"
            },
            "dataRetention": {
              "type": "any"
            },
            "usesNonCookieAccess": {
              "type": "any"
            },
            "legIntPurposes": {
              "type": "any"
            },
            "specialPurposes": {
              "type": "any"
            },
            "purposes": {
              "type": "any"
            },
            "deviceStorageDisclosureUrl": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "id": {
              "type": "any"
            },
            "flexiblePurposes": {
              "type": "any"
            },
            "dataDeclaration": {
              "type": "any"
            }
          }
        },
        "1216": {
          "type": "object",
          "properties": {
            "iab2V2GVLVersion": {
              "type": "any"
            },
            "features": {
              "type": "any"
            },
            "specialFeatures": {
              "type": "any"
            },
            "urls": {
              "type": "any"
            },
            "dataRetention": {
              "type": "any"
            },
            "usesNonCookieAccess": {
              "type": "any"
            },
            "legIntPurposes": {
              "type": "any"
            },
            "specialPurposes": {
              "type": "any"
            },
            "purposes": {
              "type": "any"
            },
            "deviceStorageDisclosureUrl": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "id": {
              "type": "any"
            },
            "flexiblePurposes": {
              "type": "any"
            },
            "dataDeclaration": {
              "type": "any"
            }
          }
        },
        "1458": {
          "type": "object",
          "properties": {
            "iab2V2GVLVersion": {
              "type": "any"
            },
            "features": {
              "type": "any"
            },
            "specialFeatures": {
              "type": "any"
            },
            "urls": {
              "type": "any"
            },
            "dataRetention": {
              "type": "any"
            },
            "usesNonCookieAccess": {
              "type": "any"
            },
            "legIntPurposes": {
              "type": "any"
            },
            "specialPurposes": {
              "type": "any"
            },
            "purposes": {
              "type": "any"
            },
            "deviceStorageDisclosureUrl": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "id": {
              "type": "any"
            },
            "flexiblePurposes": {
              "type": "any"
            },
            "dataDeclaration": {
              "type": "any"
            }
          }
        },
        "1457": {
          "type": "object",
          "properties": {
            "iab2V2GVLVersion": {
              "type": "any"
            },
            "features": {
              "type": "any"
            },
            "specialFeatures": {
              "type": "any"
            },
            "urls": {
              "type": "any"
            },
            "dataRetention": {
              "type": "any"
            },
            "usesNonCookieAccess": {
              "type": "any"
            },
            "legIntPurposes": {
              "type": "any"
            },
            "specialPurposes": {
              "type": "any"
            },
            "purposes": {
              "type": "any"
            },
            "deviceStorageDisclosureUrl": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "id": {
              "type": "any"
            },
            "flexiblePurposes": {
              "type": "any"
            },
            "dataDeclaration": {
              "type": "any"
            }
          }
        },
        "1214": {
          "type": "object",
          "properties": {
            "iab2V2GVLVersion": {
              "type": "any"
            },
            "features": {
              "type": "any"
            },
            "specialFeatures": {
              "type": "any"
            },
            "urls": {
              "type": "any"
            },
            "dataRetention": {
              "type": "any"
            },
            "usesNonCookieAccess": {
              "type": "any"
            },
            "legIntPurposes": {
              "type": "any"
            },
            "specialPurposes": {
              "type": "any"
            },
            "purposes": {
              "type": "any"
            },
            "deviceStorageDisclosureUrl": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "cookieMaxAgeSeconds": {
              "type": "any"
            },
            "id": {
              "type": "any"
            },
            "flexiblePurposes": {
              "type": "any"
            },
            "dataDeclaration": {
              "type": "any"
            }
          }
        },
        "1456": {
          "type": "object",
          "properties": {
            "iab2V2GVLVersion": {
              "type": "any"
            },
            "features": {
              "type": "any"
            },
            "specialFeatures": {
              "type": "any"
            },
            "urls": {
              "type": "any"
            },
            "dataRetention": {
              "type": "any"
            },
            "usesNonCookieAccess": {
              "type": "any"
            },
            "legIntPurposes": {
              "type": "any"
            },
            "specialPurposes": {
              "type": "any"
            },
            "purposes": {
              "type": "any"
            },
            "deviceStorageDisclosureUrl": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "id": {
              "type": "any"
            },
            "flexiblePurposes": {
              "type": "any"
            },
            "dataDeclaration": {
              "type": "any"
            }
          }
        },
        "1213": {
          "type": "object",
          "properties": {
            "iab2V2GVLVersion": {
              "type": "any"
            },
            "features": {
              "type": "any"
            },
            "specialFeatures": {
              "type": "any"
            },
            "urls": {
              "type": "any"
            },
            "dataRetention": {
              "type": "any"
            },
            "usesNonCookieAccess": {
              "type": "any"
            },
            "legIntPurposes": {
              "type": "any"
            },
            "specialPurposes": {
              "type": "any"
            },
            "purposes": {
              "type": "any"
            },
            "deviceStorageDisclosureUrl": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "id": {
              "type": "any"
            },
            "flexiblePurposes": {
              "type": "any"
            },
            "dataDeclaration": {
              "type": "any"
            }
          }
        },
        "1455": {
          "type": "object",
          "properties": {
            "iab2V2GVLVersion": {
              "type": "any"
            },
            "features": {
              "type": "any"
            },
            "specialFeatures": {
              "type": "any"
            },
            "urls": {
              "type": "any"
            },
            "dataRetention": {
              "type": "any"
            },
            "usesNonCookieAccess": {
              "type": "any"
            },
            "legIntPurposes": {
              "type": "any"
            },
            "specialPurposes": {
              "type": "any"
            },
            "purposes": {
              "type": "any"
            },
            "deviceStorageDisclosureUrl": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "cookieMaxAgeSeconds": {
              "type": "any"
            },
            "id": {
              "type": "any"
            },
            "flexiblePurposes": {
              "type": "any"
            },
            "dataDeclaration": {
              "type": "any"
            }
          }
        },
        "1212": {
          "type": "object",
          "properties": {
            "iab2V2GVLVersion": {
              "type": "any"
            },
            "features": {
              "type": "any"
            },
            "specialFeatures": {
              "type": "any"
            },
            "urls": {
              "type": "any"
            },
            "dataRetention": {
              "type": "any"
            },
            "usesNonCookieAccess": {
              "type": "any"
            },
            "legIntPurposes": {
              "type": "any"
            },
            "specialPurposes": {
              "type": "any"
            },
            "purposes": {
              "type": "any"
            },
            "deviceStorageDisclosureUrl": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "cookieMaxAgeSeconds": {
              "type": "any"
            },
            "id": {
              "type": "any"
            },
            "flexiblePurposes": {
              "type": "any"
            },
            "dataDeclaration": {
              "type": "any"
            }
          }
        },
        "1454": {
          "type": "object",
          "properties": {
            "iab2V2GVLVersion": {
              "type": "any"
            },
            "features": {
              "type": "any"
            },
            "specialFeatures": {
              "type": "any"
            },
            "urls": {
              "type": "any"
            },
            "dataRetention": {
              "type": "any"
            },
            "usesNonCookieAccess": {
              "type": "any"
            },
            "legIntPurposes": {
              "type": "any"
            },
            "specialPurposes": {
              "type": "any"
            },
            "purposes": {
              "type": "any"
            },
            "deviceStorageDisclosureUrl": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "cookieMaxAgeSeconds": {
              "type": "any"
            },
            "id": {
              "type": "any"
            },
            "flexiblePurposes": {
              "type": "any"
            },
            "dataDeclaration": {
              "type": "any"
            }
          }
        },
        "1453": {
          "type": "object",
          "properties": {
            "iab2V2GVLVersion": {
              "type": "any"
            },
            "features": {
              "type": "any"
            },
            "specialFeatures": {
              "type": "any"
            },
            "urls": {
              "type": "any"
            },
            "dataRetention": {
              "type": "any"
            },
            "usesNonCookieAccess": {
              "type": "any"
            },
            "legIntPurposes": {
              "type": "any"
            },
            "specialPurposes": {
              "type": "any"
            },
            "purposes": {
              "type": "any"
            },
            "deviceStorageDisclosureUrl": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "cookieMaxAgeSeconds": {
              "type": "any"
            },
            "id": {
              "type": "any"
            },
            "flexiblePurposes": {
              "type": "any"
            },
            "dataDeclaration": {
              "type": "any"
            }
          }
        },
        "1452": {
          "type": "object",
          "properties": {
            "iab2V2GVLVersion": {
              "type": "any"
            },
            "features": {
              "type": "any"
            },
            "specialFeatures": {
              "type": "any"
            },
            "urls": {
              "type": "any"
            },
            "dataRetention": {
              "type": "any"
            },
            "usesNonCookieAccess": {
              "type": "any"
            },
            "legIntPurposes": {
              "type": "any"
            },
            "specialPurposes": {
              "type": "any"
            },
            "purposes": {
              "type": "any"
            },
            "deviceStorageDisclosureUrl": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "id": {
              "type": "any"
            },
            "flexiblePurposes": {
              "type": "any"
            },
            "dataDeclaration": {
              "type": "any"
            }
          }
        },
        "1219": {
          "type": "object",
          "properties": {
            "iab2V2GVLVersion": {
              "type": "any"
            },
            "features": {
              "type": "any"
            },
            "specialFeatures": {
              "type": "any"
            },
            "urls": {
              "type": "any"
            },
            "dataRetention": {
              "type": "any"
            },
            "usesNonCookieAccess": {
              "type": "any"
            },
            "legIntPurposes": {
              "type": "any"
            },
            "specialPurposes": {
              "type": "any"
            },
            "purposes": {
              "type": "any"
            },
            "deviceStorageDisclosureUrl": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "id": {
              "type": "any"
            },
            "flexiblePurposes": {
              "type": "any"
            },
            "dataDeclaration": {
              "type": "any"
            }
          }
        },
        "1473": {
          "type": "object",
          "properties": {
            "iab2V2GVLVersion": {
              "type": "any"
            },
            "features": {
              "type": "any"
            },
            "specialFeatures": {
              "type": "any"
            },
            "urls": {
              "type": "any"
            },
            "dataRetention": {
              "type": "any"
            },
            "usesNonCookieAccess": {
              "type": "any"
            },
            "legIntPurposes": {
              "type": "any"
            },
            "specialPurposes": {
              "type": "any"
            },
            "purposes": {
              "type": "any"
            },
            "deviceStorageDisclosureUrl": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "cookieMaxAgeSeconds": {
              "type": "any"
            },
            "id": {
              "type": "any"
            },
            "flexiblePurposes": {
              "type": "any"
            },
            "dataDeclaration": {
              "type": "any"
            }
          }
        },
        "1230": {
          "type": "object",
          "properties": {
            "iab2V2GVLVersion": {
              "type": "any"
            },
            "features": {
              "type": "any"
            },
            "specialFeatures": {
              "type": "any"
            },
            "urls": {
              "type": "any"
            },
            "dataRetention": {
              "type": "any"
            },
            "usesNonCookieAccess": {
              "type": "any"
            },
            "legIntPurposes": {
              "type": "any"
            },
            "specialPurposes": {
              "type": "any"
            },
            "purposes": {
              "type": "any"
            },
            "deviceStorageDisclosureUrl": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "id": {
              "type": "any"
            },
            "flexiblePurposes": {
              "type": "any"
            },
            "dataDeclaration": {
              "type": "any"
            }
          }
        },
        "1472": {
          "type": "object",
          "properties": {
            "iab2V2GVLVersion": {
              "type": "any"
            },
            "features": {
              "type": "any"
            },
            "specialFeatures": {
              "type": "any"
            },
            "urls": {
              "type": "any"
            },
            "dataRetention": {
              "type": "any"
            },
            "usesNonCookieAccess": {
              "type": "any"
            },
            "legIntPurposes": {
              "type": "any"
            },
            "specialPurposes": {
              "type": "any"
            },
            "purposes": {
              "type": "any"
            },
            "deviceStorageDisclosureUrl": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "id": {
              "type": "any"
            },
            "flexiblePurposes": {
              "type": "any"
            },
            "dataDeclaration": {
              "type": "any"
            }
          }
        },
        "1471": {
          "type": "object",
          "properties": {
            "iab2V2GVLVersion": {
              "type": "any"
            },
            "features": {
              "type": "any"
            },
            "specialFeatures": {
              "type": "any"
            },
            "urls": {
              "type": "any"
            },
            "dataRetention": {
              "type": "any"
            },
            "usesNonCookieAccess": {
              "type": "any"
            },
            "legIntPurposes": {
              "type": "any"
            },
            "specialPurposes": {
              "type": "any"
            },
            "purposes": {
              "type": "any"
            },
            "deviceStorageDisclosureUrl": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "cookieMaxAgeSeconds": {
              "type": "any"
            },
            "id": {
              "type": "any"
            },
            "flexiblePurposes": {
              "type": "any"
            },
            "dataDeclaration": {
              "type": "any"
            }
          }
        }
      }
    },
    "dataCategories": {
      "type": "object",
      "properties": {
        "11": {
          "type": "object",
          "properties": {
            "name": {
              "type": "any"
            },
            "description": {
              "type": "any"
            },
            "id": {
              "type": "any"
            }
          }
        },
        "1": {
          "type": "object",
          "properties": {
            "name": {
              "type": "any"
            },
            "description": {
              "type": "any"
            },
            "id": {
              "type": "any"
            }
          }
        },
        "2": {
          "type": "object",
          "properties": {
            "name": {
              "type": "any"
            },
            "description": {
              "type": "any"
            },
            "id": {
              "type": "any"
            }
          }
        },
        "3": {
          "type": "object",
          "properties": {
            "name": {
              "type": "any"
            },
            "description": {
              "type": "any"
            },
            "id": {
              "type": "any"
            }
          }
        },
        "4": {
          "type": "object",
          "properties": {
            "name": {
              "type": "any"
            },
            "description": {
              "type": "any"
            },
            "id": {
              "type": "any"
            }
          }
        },
        "5": {
          "type": "object",
          "properties": {
            "name": {
              "type": "any"
            },
            "description": {
              "type": "any"
            },
            "id": {
              "type": "any"
            }
          }
        },
        "6": {
          "type": "object",
          "properties": {
            "name": {
              "type": "any"
            },
            "description": {
              "type": "any"
            },
            "id": {
              "type": "any"
            }
          }
        },
        "7": {
          "type": "object",
          "properties": {
            "name": {
              "type": "any"
            },
            "description": {
              "type": "any"
            },
            "id": {
              "type": "any"
            }
          }
        },
        "8": {
          "type": "object",
          "properties": {
            "name": {
              "type": "any"
            },
            "description": {
              "type": "any"
            },
            "id": {
              "type": "any"
            }
          }
        },
        "9": {
          "type": "object",
          "properties": {
            "name": {
              "type": "any"
            },
            "description": {
              "type": "any"
            },
            "id": {
              "type": "any"
            }
          }
        },
        "10": {
          "type": "object",
          "properties": {
            "name": {
              "type": "any"
            },
            "description": {
              "type": "any"
            },
            "id": {
              "type": "any"
            }
          }
        }
      }
    }
  }
}
```
### `GET` /scripttemplates/202605.1.0/assets/otFloatingRoundedCorner.json
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
### `GET` /scripttemplates/202605.1.0/assets/v2/otPcTab.json
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

