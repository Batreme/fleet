---
title: "APIs & Protocols: ethiack-com"
date: 2026-11-14
target: "ethiack-com"
---

# Discovered APIs & Protocols: ethiack-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/_payload.json` | `200` | REST endpoint |
| `GET` | `/_nuxt/builds/meta/5c026f32-1717-41d0-b7fd-e280cb0f1a13.json` | `200` | REST endpoint |
| `POST` | `/api/send` | `200` | REST endpoint |
| `GET` | `/embed/v3/form/25953430/6c578f32-7938-47ca-bc93-06584a2ef720/json` | `200` | REST endpoint |
| `GET` | `/embed/v3/form/25953430/6c578f32-7938-47ca-bc93-06584a2ef720/json` | `200` | REST endpoint |
| `GET` | `/consentconfig/2a530695-716e-4fb0-91a1-bcd5c3d1b666/settings.json` | `200` | REST endpoint |
| `GET` | `/config` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /_payload.json
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
### `GET` /_nuxt/builds/meta/5c026f32-1717-41d0-b7fd-e280cb0f1a13.json
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
    "matcher": {
      "type": "object",
      "properties": {
        "static": {
          "type": "object",
          "properties": {
            "/blog": {
              "type": "any"
            },
            "/blog/dont-fear-the-ai-reaper-using-llms-to-hack-better-and-faster": {
              "type": "any"
            },
            "/blog/bug-bounty-vs-pentesting-for-saas-which-one-should-you-choose": {
              "type": "any"
            },
            "/blog/bypassing-wafs-for-fun-and-js-injection-with-parameter-pollution": {
              "type": "any"
            },
            "/blog/catch-them-early-integrate-automated-pentesting-in-your-cicd-pipeline": {
              "type": "any"
            },
            "/blog/cleaning-the-portal-ux-improvements-to-the-way-you-use-ethiack": {
              "type": "any"
            },
            "/blog/como-cumprir-com-a-nis2-guia-para-pmes-portuguesas": {
              "type": "any"
            },
            "/blog/como-fazer-um-invent\u00e1rio-de-ativos-para-ciberseguran\u00e7a": {
              "type": "any"
            },
            "/blog/continuous-security-assurance-for-compliancewise-adapting-to-an-ever-evolving-landscape": {
              "type": "any"
            },
            "/blog/digital-exposure-analysis-of-the-500-largest-portuguese-companies": {
              "type": "any"
            },
            "/blog/dont-stop-the-party-how-baladapp-is-keeping-their-users-safe-with-autonomous-ethical-hacking": {
              "type": "any"
            },
            "/blog/ethiack-214-test-internal-assets-cicd-sso-new-reports-and-more": {
              "type": "any"
            },
            "/blog/ethiack-beacon-easily-test-your-internal-assets": {
              "type": "any"
            },
            "/blog/ethiack-distinguished-as-a-leader-in-innovation-in-portugal": {
              "type": "any"
            },
            "/blog/ethiack-featured-in-the-portugal-fintech-report-2023": {
              "type": "any"
            },
            "/blog/ethiack-raises-a-4-million-funding-round-to-develop-ai-powered-hackbots": {
              "type": "any"
            },
            "/blog/ethiacks-journey-with-google-for-startups-in-the-growth-academy-ai-for-cybersecurity": {
              "type": "any"
            },
            "/blog/everything-financial-institutions-need-to-know-about-the-nis2-directive": {
              "type": "any"
            },
            "/blog/extended-capabilities-for-ethiacks-api-whats-changing": {
              "type": "any"
            },
            "/blog/find-the-needle-in-the-haystack-with-advanced-filters-for-attack-surface-management": {
              "type": "any"
            }
          }
        },
        "wildcard": {
          "type": "object",
          "properties": {}
        },
        "dynamic": {
          "type": "object",
          "properties": {}
        }
      }
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
### `POST` /api/send
```json
{
  "type": "object",
  "properties": {
    "cache": {
      "type": "string"
    },
    "sessionId": {
      "type": "string"
    },
    "visitId": {
      "type": "string"
    }
  }
}
```
### `GET` /embed/v3/form/25953430/6c578f32-7938-47ca-bc93-06584a2ef720/json
```json
{
  "type": "object",
  "properties": {
    "form": {
      "type": "object",
      "properties": {
        "portalId": {
          "type": "number"
        },
        "guid": {
          "type": "string"
        },
        "cssClass": {
          "type": "string"
        },
        "inlineMessage": {
          "type": "string"
        },
        "redirectUrl": {
          "type": "string"
        },
        "submitText": {
          "type": "string"
        },
        "formFieldGroups": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "metaData": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "captchaEnabled": {
          "type": "boolean"
        },
        "formTypeNumber": {
          "type": "number"
        },
        "thankYouMessageJson": {
          "type": "string"
        },
        "themeColor": {
          "type": "string"
        },
        "themeName": {
          "type": "string"
        },
        "style": {
          "type": "string"
        },
        "variantId": {
          "type": "null"
        },
        "isPublished": {
          "type": "boolean"
        },
        "embedVersion": {
          "type": "null"
        },
        "captchaVersion": {
          "type": "string"
        }
      }
    },
    "properties": {
      "type": "object",
      "properties": {}
    },
    "knownSmartFields": {
      "type": "array",
      "items": "any"
    },
    "gates": {
      "type": "object",
      "properties": {
        "ServiceHub:Feedback:TrellisSmileys": {
          "type": "boolean"
        },
        "LeadCaptureFe::Legacy::FormV2ReCaptchaV3Fix": {
          "type": "boolean"
        }
      }
    },
    "scopes": {
      "type": "object",
      "properties": {
        "noBranding": {
          "type": "boolean"
        },
        "renderShell": {
          "type": "boolean"
        },
        "rawHtmlAccess": {
          "type": "boolean"
        },
        "customStyleAccess": {
          "type": "boolean"
        }
      }
    },
    "time": {
      "type": "number"
    },
    "themeCss": {
      "type": "string"
    },
    "globalStyle": {
      "type": "string"
    },
    "countryCode": {
      "type": "string"
    },
    "portalSetting": {
      "type": "object",
      "properties": {
        "enableLiveValidation": {
          "type": "boolean"
        }
      }
    },
    "errorCode": {
      "type": "null"
    }
  }
}
```
### `GET` /embed/v3/form/25953430/6c578f32-7938-47ca-bc93-06584a2ef720/json
```json
{
  "type": "object",
  "properties": {
    "form": {
      "type": "object",
      "properties": {
        "portalId": {
          "type": "number"
        },
        "guid": {
          "type": "string"
        },
        "cssClass": {
          "type": "string"
        },
        "inlineMessage": {
          "type": "string"
        },
        "redirectUrl": {
          "type": "string"
        },
        "submitText": {
          "type": "string"
        },
        "formFieldGroups": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "metaData": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "captchaEnabled": {
          "type": "boolean"
        },
        "formTypeNumber": {
          "type": "number"
        },
        "thankYouMessageJson": {
          "type": "string"
        },
        "themeColor": {
          "type": "string"
        },
        "themeName": {
          "type": "string"
        },
        "style": {
          "type": "string"
        },
        "variantId": {
          "type": "null"
        },
        "isPublished": {
          "type": "boolean"
        },
        "embedVersion": {
          "type": "null"
        },
        "captchaVersion": {
          "type": "string"
        }
      }
    },
    "properties": {
      "type": "object",
      "properties": {}
    },
    "knownSmartFields": {
      "type": "array",
      "items": "any"
    },
    "gates": {
      "type": "object",
      "properties": {
        "ServiceHub:Feedback:TrellisSmileys": {
          "type": "boolean"
        },
        "LeadCaptureFe::Legacy::FormV2ReCaptchaV3Fix": {
          "type": "boolean"
        }
      }
    },
    "scopes": {
      "type": "object",
      "properties": {
        "noBranding": {
          "type": "boolean"
        },
        "renderShell": {
          "type": "boolean"
        },
        "rawHtmlAccess": {
          "type": "boolean"
        },
        "customStyleAccess": {
          "type": "boolean"
        }
      }
    },
    "time": {
      "type": "number"
    },
    "themeCss": {
      "type": "string"
    },
    "globalStyle": {
      "type": "string"
    },
    "countryCode": {
      "type": "string"
    },
    "portalSetting": {
      "type": "object",
      "properties": {
        "enableLiveValidation": {
          "type": "boolean"
        }
      }
    },
    "errorCode": {
      "type": "null"
    }
  }
}
```
### `GET` /consentconfig/2a530695-716e-4fb0-91a1-bcd5c3d1b666/settings.json
```json
{
  "type": "object",
  "properties": {
    "widget": {
      "type": "object",
      "properties": {
        "enabled": {
          "type": "boolean"
        },
        "position": {
          "type": "object",
          "properties": {
            "position": {
              "type": "any"
            },
            "distanceVerticalPx": {
              "type": "any"
            },
            "distanceHorizontalPx": {
              "type": "any"
            }
          }
        },
        "theme": {
          "type": "object",
          "properties": {
            "closed": {
              "type": "any"
            },
            "opened": {
              "type": "any"
            }
          }
        },
        "content": {
          "type": "object",
          "properties": {
            "cultures": {
              "type": "any"
            },
            "default": {
              "type": "any"
            },
            "autodetectLanguage": {
              "type": "any"
            }
          }
        }
      }
    },
    "twipla": {
      "type": "null"
    }
  }
}
```

