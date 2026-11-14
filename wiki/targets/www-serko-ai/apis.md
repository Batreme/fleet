---
title: "APIs & Protocols: www-serko-ai"
date: 2026-11-14
target: "[[overview|www-serko-ai]]"
---

# Discovered APIs & Protocols: www-serko-ai

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `POST` | `/context-v2/117114932` | `200` | REST endpoint |
| `POST` | `/prediction/117114932` | `200` | REST endpoint |
| `POST` | `/logger` | `200` | REST endpoint |
| `POST` | `/logger` | `200` | REST endpoint |
| `POST` | `/logger` | `200` | REST endpoint |
| `GET` | `/5rRIWCamhz/b70022a0-3e04-47a6-92c3-b19114951a0a/en.json` | `200` | REST endpoint |
| `POST` | `/clientlogger` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `POST` /context-v2/117114932
```json
{
  "type": "object",
  "properties": {
    "requestId": {
      "type": "string"
    },
    "clientIp": {
      "type": "string"
    },
    "userAgentDigest": {
      "type": "string"
    },
    "userAgent": {
      "type": "object",
      "properties": {
        "deviceClass": {
          "type": "string"
        },
        "deviceName": {
          "type": "string"
        },
        "deviceBrand": {
          "type": "string"
        },
        "osClass": {
          "type": "string"
        },
        "osName": {
          "type": "string"
        },
        "osVersion": {
          "type": "string"
        },
        "agentClass": {
          "type": "string"
        },
        "agentName": {
          "type": "string"
        },
        "agentVersionMajor": {
          "type": "string"
        }
      }
    },
    "location": {
      "type": "object",
      "properties": {
        "countryIso": {
          "type": "string"
        },
        "countryName": {
          "type": "string"
        }
      }
    },
    "integrationData": {
      "type": "object",
      "properties": {
        "firmographic": {
          "type": "object",
          "properties": {
            "domain": {
              "type": "any"
            }
          }
        }
      }
    }
  }
}
```
### `POST` /prediction/117114932
```json
{
  "type": "object",
  "properties": {
    "policy": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string"
        },
        "timestamp": {
          "type": "number"
        },
        "experiences": {
          "type": "object",
          "properties": {}
        }
      }
    }
  }
}
```
### `POST` /logger
```json
{
  "type": "object",
  "properties": {}
}
```
### `POST` /logger
```json
{
  "type": "object",
  "properties": {}
}
```
### `POST` /logger
```json
{
  "type": "object",
  "properties": {}
}
```
### `GET` /5rRIWCamhz/b70022a0-3e04-47a6-92c3-b19114951a0a/en.json
```json
{
  "type": "object",
  "properties": {
    "buttons": {
      "type": "object",
      "properties": {
        "accept": {
          "type": "string"
        },
        "acceptAll": {
          "type": "string"
        },
        "deny": {
          "type": "string"
        },
        "denyNonEssential": {
          "type": "string"
        },
        "rejectNonEssential": {
          "type": "string"
        },
        "dialog": {
          "type": "object",
          "properties": {
            "denyAll": {
              "type": "any"
            },
            "openDrawer": {
              "type": "any"
            }
          }
        },
        "denyAll": {
          "type": "string"
        },
        "managePreferences": {
          "type": "string"
        },
        "save": {
          "type": "string"
        },
        "storagePolicy": {
          "type": "string"
        }
      }
    },
    "categories": {
      "type": "object",
      "properties": {
        "ESSENTIAL": {
          "type": "object",
          "properties": {
            "label": {
              "type": "any"
            },
            "description": {
              "type": "any"
            }
          }
        },
        "MARKETING": {
          "type": "object",
          "properties": {
            "label": {
              "type": "any"
            },
            "description": {
              "type": "any"
            }
          }
        },
        "PERSONALIZATION": {
          "type": "object",
          "properties": {
            "label": {
              "type": "any"
            },
            "description": {
              "type": "any"
            }
          }
        },
        "ANALYTICS": {
          "type": "object",
          "properties": {
            "label": {
              "type": "any"
            },
            "description": {
              "type": "any"
            }
          }
        },
        "STORAGE": {
          "type": "object",
          "properties": {
            "label": {
              "type": "any"
            },
            "description": {
              "type": "any"
            }
          }
        },
        "OPT_OUT": {
          "type": "object",
          "properties": {
            "label": {
              "type": "any"
            },
            "description": {
              "type": "any"
            }
          }
        }
      }
    },
    "dialog": {
      "type": "object",
      "properties": {
        "close": {
          "type": "string"
        },
        "label": {
          "type": "string"
        }
      }
    },
    "messaging": {
      "type": "object",
      "properties": {
        "analyticsOnByDefault": {
          "type": "string"
        },
        "poweredBy": {
          "type": "string"
        },
        "default": {
          "type": "string"
        },
        "categories": {
          "type": "string"
        },
        "cookieQuestion": {
          "type": "string"
        },
        "timer": {
          "type": "string"
        },
        "privacyPolicy": {
          "type": "string"
        },
        "cookiePolicy": {
          "type": "string"
        },
        "privacyNotice": {
          "type": "string"
        },
        "cookieNotice": {
          "type": "string"
        },
        "moreDetails": {
          "type": "string"
        },
        "widgetAltText": {
          "type": "string"
        },
        "usageWhat": {
          "type": "string"
        },
        "usageHow": {
          "type": "string"
        },
        "usageList": {
          "type": "string"
        },
        "viewCookies": {
          "type": "string"
        },
        "viewDisclosures": {
          "type": "string"
        },
        "closeButton": {
          "type": "string"
        },
        "subjectRightsRequest": {
          "type": "string"
        },
        "doNotSellOrShare": {
          "type": "string"
        }
      }
    },
    "optOut": {
      "type": "object",
      "properties": {
        "honored": {
          "type": "string"
        },
        "active": {
          "type": "string"
        },
        "signalHonored": {
          "type": "string"
        },
        "signalActive": {
          "type": "string"
        }
      }
    },
    "disclosure": {
      "type": "object",
      "properties": {
        "day": {
          "type": "string"
        },
        "label": {
          "type": "string"
        },
        "none": {
          "type": "string"
        },
        "noProvider": {
          "type": "string"
        },
        "cookie": {
          "type": "object",
          "properties": {
            "purpose": {
              "type": "any"
            },
            "expiry": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "classification": {
              "type": "any"
            },
            "provider": {
              "type": "any"
            }
          }
        },
        "dayPlural": {
          "type": "string"
        },
        "script": {
          "type": "object",
          "properties": {
            "purpose": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "classification": {
              "type": "any"
            },
            "provider": {
              "type": "any"
            }
          }
        },
        "titles": {
          "type": "object",
          "properties": {
            "classification": {
              "type": "any"
            },
            "expiry": {
              "type": "any"
            },
            "name": {
              "type": "any"
            },
            "provider": {
              "type": "any"
            },
            "purpose": {
              "type": "any"
            },
            "type": {
              "type": "any"
            }
          }
        },
        "types": {
          "type": "object",
          "properties": {
            "localStorage": {
              "type": "any"
            },
            "trackingPixel": {
              "type": "any"
            }
          }
        }
      }
    },
    "drawer": {
      "type": "object",
      "properties": {
        "header": {
          "type": "string"
        },
        "close": {
          "type": "string"
        },
        "copy": {
          "type": "string"
        },
        "copied": {
          "type": "string"
        },
        "description": {
          "type": "string"
        },
        "alwaysOn": {
          "type": "string"
        },
        "copyAriaLabel": {
          "type": "string"
        }
      }
    },
    "doNotSell": {
      "type": "object",
      "properties": {
        "header": {
          "type": "string"
        },
        "description": {
          "type": "string"
        },
        "link": {
          "type": "string"
        }
      }
    },
    "aria": {
      "type": "object",
      "properties": {
        "newWindow": {
          "type": "string"
        },
        "external": {
          "type": "string"
        },
        "externalNewWindow": {
          "type": "string"
        }
      }
    }
  }
}
```
### `POST` /clientlogger
```json
{
  "type": "object",
  "properties": {}
}
```

