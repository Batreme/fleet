---
title: "APIs & Protocols: turismo-gov-st_fr"
date: 2026-11-14
target: "[[overview|turismo-gov-st_fr]]"
---

# Discovered APIs & Protocols: turismo-gov-st_fr

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/projectconfigurations/brands/6a1ff0f403b3898036beb611.json` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /projectconfigurations/brands/6a1ff0f403b3898036beb611.json
```json
{
  "type": "object",
  "properties": {
    "_id": {
      "type": "string"
    },
    "publishedAt": {
      "type": "string"
    },
    "projectId": {
      "type": "string"
    },
    "projectName": {
      "type": "string"
    },
    "jobId": {
      "type": "string"
    },
    "shadowRoot": {
      "type": "boolean"
    },
    "isDomainRestrictionEnabled": {
      "type": "boolean"
    },
    "verifiedDomains": {
      "type": "array",
      "items": "any"
    },
    "client": {
      "type": "object",
      "properties": {
        "colors": {
          "type": "object",
          "properties": {
            "main": {
              "type": "any"
            },
            "paintTransform": {
              "type": "any"
            },
            "backdrop_inner": {
              "type": "any"
            },
            "backdrop_outer": {
              "type": "any"
            },
            "button_bg": {
              "type": "any"
            },
            "button_bg_hover": {
              "type": "any"
            },
            "button_border": {
              "type": "any"
            },
            "button_text": {
              "type": "any"
            },
            "button_text_hover": {
              "type": "any"
            },
            "card": {
              "type": "any"
            },
            "danger": {
              "type": "any"
            },
            "primary_button_bg": {
              "type": "any"
            },
            "primary_button_bg_hover": {
              "type": "any"
            },
            "primary_button_text": {
              "type": "any"
            },
            "primary_button_text_hover": {
              "type": "any"
            },
            "secondary": {
              "type": "any"
            },
            "tertiary": {
              "type": "any"
            },
            "text": {
              "type": "any"
            },
            "title": {
              "type": "any"
            },
            "toggle_off": {
              "type": "any"
            }
          }
        },
        "customButton": {
          "type": "object",
          "properties": {
            "active": {
              "type": "any"
            },
            "image": {
              "type": "any"
            },
            "imageWidth": {
              "type": "any"
            },
            "label": {
              "type": "any"
            },
            "colors": {
              "type": "any"
            },
            "styles": {
              "type": "any"
            }
          }
        },
        "fonts": {
          "type": "object",
          "properties": {
            "title": {
              "type": "any"
            },
            "text": {
              "type": "any"
            }
          }
        },
        "widgetStyle": {
          "type": "object",
          "properties": {
            "borderRadius": {
              "type": "any"
            },
            "consentButtonBorderRadius": {
              "type": "any"
            },
            "discardButtonBorderRadius": {
              "type": "any"
            },
            "titleFontSize": {
              "type": "any"
            },
            "fontSize": {
              "type": "any"
            },
            "padding": {
              "type": "any"
            },
            "boxShadowType": {
              "type": "any"
            }
          }
        },
        "overlayStyle": {
          "type": "object",
          "properties": {
            "insertRootAt": {
              "type": "any"
            },
            "backdropStyle": {
              "type": "any"
            },
            "disableScrollHijack": {
              "type": "any"
            },
            "position": {
              "type": "any"
            }
          }
        },
        "isCustomStyle": {
          "type": "boolean"
        },
        "marketplace": {
          "type": "array",
          "items": "any"
        }
      }
    },
    "privacypolicy": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string"
        },
        "name": {
          "type": "string"
        },
        "type": {
          "type": "string"
        }
      }
    },
    "dpo": {
      "type": "object",
      "properties": {}
    },
    "contractsV2": {
      "type": "array",
      "items": "any"
    },
    "portability": {
      "type": "array",
      "items": "any"
    },
    "cookies": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "identifier": {
            "type": "any"
          },
          "language": {
            "type": "any"
          },
          "aboutUsId": {
            "type": "any"
          },
          "steps": {
            "type": "any"
          },
          "strings": {
            "type": "any"
          },
          "a11yStrings": {
            "type": "any"
          },
          "settings": {
            "type": "any"
          },
          "uiSettings": {
            "type": "any"
          },
          "version": {
            "type": "any"
          },
          "name": {
            "type": "any"
          },
          "icon": {
            "type": "any"
          },
          "isFree": {
            "type": "any"
          },
          "country": {
            "type": "any"
          },
          "title": {
            "type": "any"
          },
          "regulation": {
            "type": "any"
          },
          "projectId": {
            "type": "any"
          },
          "googleConsentMode": {
            "type": "any"
          },
          "gpc": {
            "type": "any"
          },
          "isLive": {
            "type": "any"
          },
          "partOfABTest": {
            "type": "any"
          }
        }
      }
    },
    "contracts": {
      "type": "array",
      "items": "any"
    },
    "processings": {
      "type": "array",
      "items": "any"
    },
    "themes": {
      "type": "object",
      "properties": {
        "light": {
          "type": "object",
          "properties": {
            "colors": {
              "type": "any"
            },
            "customButton": {
              "type": "any"
            },
            "fonts": {
              "type": "any"
            },
            "overlayStyle": {
              "type": "any"
            },
            "widgetStyle": {
              "type": "any"
            }
          }
        }
      }
    },
    "hasAppSdkBrands": {
      "type": "boolean"
    },
    "hasWebSdkBrands": {
      "type": "boolean"
    },
    "schemaVersion": {
      "type": "string"
    }
  }
}
```

