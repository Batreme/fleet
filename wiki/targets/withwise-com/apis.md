---
title: "APIs & Protocols: withwise-com"
date: 2026-11-14
target: "[[overview|withwise-com]]"
---

# Discovered APIs & Protocols: withwise-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `POST` | `/api/v1/log` | `200` | REST endpoint |
| `POST` | `/wp-admin/admin-ajax.php` | `200` | REST endpoint |
| `GET` | `/client_data/b047423cf8a7ccfdd76d3e1d8ba6349f/wzr_eoL0.json` | `200` | REST endpoint |
| `GET` | `/v2/145539501/banner.js` | `200` | REST endpoint |
| `GET` | `/client_data/b047423cf8a7ccfdd76d3e1d8ba6349f/config/fnp1sZDG.json` | `200` | REST endpoint |
| `GET` | `/client_data/b047423cf8a7ccfdd76d3e1d8ba6349f/translations/vsLwSRzQ.json` | `200` | REST endpoint |
| `GET` | `/hs-script-loader-public/v2/config/pixels-and-events/json` | `200` | REST endpoint |
| `GET` | `/collected-forms/v1/config/json` | `200` | REST endpoint |
| `GET` | `/client_data/b047423cf8a7ccfdd76d3e1d8ba6349f/audit-table/hoqP7uFb.json` | `200` | REST endpoint |
| `GET` | `/web-interactives/public/v1/embed/combinedConfigs` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `POST` /wp-admin/admin-ajax.php
```json
{
  "type": "object",
  "properties": {
    "success": {
      "type": "boolean"
    },
    "data": {
      "type": "object",
      "properties": {
        "nonce": {
          "type": "string"
        }
      }
    }
  }
}
```
### `GET` /client_data/b047423cf8a7ccfdd76d3e1d8ba6349f/wzr_eoL0.json
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "targetBanner": {
        "type": "number"
      },
      "condition": {
        "type": "string"
      }
    }
  }
}
```
### `GET` /client_data/b047423cf8a7ccfdd76d3e1d8ba6349f/config/fnp1sZDG.json
```json
{
  "type": "object",
  "properties": {
    "reloadOnAccept": {
      "type": "boolean"
    },
    "dataShortCodes": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "key": {
            "type": "any"
          },
          "content": {
            "type": "any"
          },
          "uiTag": {
            "type": "any"
          },
          "type": {
            "type": "any"
          },
          "customTag": {
            "type": "any"
          },
          "attributes": {
            "type": "any"
          },
          "processedHTML": {
            "type": "any"
          }
        }
      }
    },
    "iabDataShortCodes": {
      "type": "array",
      "items": "any"
    },
    "activeLaw": {
      "type": "string"
    },
    "showAuditTable": {
      "type": "boolean"
    },
    "showToggler": {
      "type": "boolean"
    },
    "googleACMEnabled": {
      "type": "boolean"
    },
    "readMore": {
      "type": "object",
      "properties": {
        "status": {
          "type": "boolean"
        },
        "styles": {
          "type": "object",
          "properties": {
            "color": {
              "type": "any"
            },
            "border-color": {
              "type": "any"
            },
            "background-color": {
              "type": "any"
            }
          }
        },
        "type": {
          "type": "string"
        }
      }
    },
    "togglerSwitch": {
      "type": "object",
      "properties": {
        "status": {
          "type": "boolean"
        },
        "styles": {
          "type": "object",
          "properties": {
            "activeColor": {
              "type": "any"
            },
            "inactiveColor": {
              "type": "any"
            }
          }
        }
      }
    },
    "togglerIABSwitch": {
      "type": "object",
      "properties": {
        "status": {
          "type": "boolean"
        },
        "styles": {
          "type": "object",
          "properties": {
            "activeColor": {
              "type": "any"
            },
            "inactiveColor": {
              "type": "any"
            }
          }
        }
      }
    },
    "ccpaSwitch": {
      "type": "object",
      "properties": {
        "status": {
          "type": "boolean"
        },
        "styles": {
          "type": "object",
          "properties": {
            "activeColor": {
              "type": "any"
            },
            "inactiveColor": {
              "type": "any"
            }
          }
        }
      }
    },
    "placeHolder": {
      "type": "object",
      "properties": {
        "status": {
          "type": "boolean"
        },
        "styles": {
          "type": "object",
          "properties": {
            "border-color": {
              "type": "any"
            },
            "background-color": {
              "type": "any"
            },
            "color": {
              "type": "any"
            }
          }
        }
      }
    },
    "togglerIABTab": {
      "type": "object",
      "properties": {
        "status": {
          "type": "boolean"
        },
        "styles": {
          "type": "object",
          "properties": {
            "activeColor": {
              "type": "any"
            },
            "inactiveColor": {
              "type": "any"
            }
          }
        }
      }
    },
    "html": {
      "type": "string"
    },
    "css": {
      "type": "string"
    },
    "defaultLanguage": {
      "type": "string"
    },
    "bannerType": {
      "type": "string"
    },
    "respectGPC": {
      "type": "boolean"
    },
    "iabEnabled": {
      "type": "boolean"
    },
    "scriptExpiry": {
      "type": "string"
    }
  }
}
```
### `GET` /client_data/b047423cf8a7ccfdd76d3e1d8ba6349f/translations/vsLwSRzQ.json
```json
{
  "type": "object",
  "properties": {
    "cky_notice_title": {
      "type": "string"
    },
    "cky_notice_description": {
      "type": "string"
    },
    "cky_notice_close_label": {
      "type": "string"
    },
    "cky_readmore_text": {
      "type": "string"
    },
    "cky_readmore_privacyLink": {
      "type": "string"
    },
    "cky_revisit_title": {
      "type": "string"
    },
    "cky_video_placeholder_title": {
      "type": "string"
    },
    "cky_accept_text": {
      "type": "string"
    },
    "cky_reject_text": {
      "type": "string"
    },
    "cky_settings_text": {
      "type": "string"
    },
    "cky_preference_title": {
      "type": "string"
    },
    "cky_preference_description": {
      "type": "string"
    },
    "cky_preference_always_enabled": {
      "type": "string"
    },
    "cky_preference_save_text": {
      "type": "string"
    },
    "cky_preference_accept_text": {
      "type": "string"
    },
    "cky_preference_reject_text": {
      "type": "string"
    },
    "cky_preview_save_text": {
      "type": "string"
    },
    "cky_enable_category_label": {
      "type": "string"
    },
    "cky_disable_category_label": {
      "type": "string"
    },
    "cky_preference_close_label": {
      "type": "string"
    }
  }
}
```
### `GET` /hs-script-loader-public/v2/config/pixels-and-events/json
```json
{
  "type": "object",
  "properties": {
    "pixels": {
      "type": "object",
      "properties": {
        "ADWORDS": {
          "type": "array",
          "items": {
            "type": "any"
          }
        }
      }
    },
    "enhancedConversionEventSettings": {
      "type": "object",
      "properties": {}
    }
  }
}
```
### `GET` /collected-forms/v1/config/json
```json
{
  "type": "object",
  "properties": {
    "portalId": {
      "type": "number"
    },
    "submissionsApiDomain": {
      "type": "string"
    },
    "reportScraperTest": {
      "type": "boolean"
    },
    "formCaptureEnabled": {
      "type": "boolean"
    },
    "token": {
      "type": "number"
    }
  }
}
```
### `GET` /client_data/b047423cf8a7ccfdd76d3e1d8ba6349f/audit-table/hoqP7uFb.json
```json
{
  "type": "object",
  "properties": {
    "cookies": {
      "type": "object",
      "properties": {
        "__cf_bm": {
          "type": "object",
          "properties": {
            "cookie_id": {
              "type": "any"
            },
            "duration": {
              "type": "any"
            },
            "description": {
              "type": "any"
            }
          }
        },
        "AWSALBCORS": {
          "type": "object",
          "properties": {
            "cookie_id": {
              "type": "any"
            },
            "duration": {
              "type": "any"
            },
            "description": {
              "type": "any"
            }
          }
        },
        "VISITOR_PRIVACY_METADATA": {
          "type": "object",
          "properties": {
            "cookie_id": {
              "type": "any"
            },
            "duration": {
              "type": "any"
            },
            "description": {
              "type": "any"
            }
          }
        },
        "cookietest": {
          "type": "object",
          "properties": {
            "cookie_id": {
              "type": "any"
            },
            "duration": {
              "type": "any"
            },
            "description": {
              "type": "any"
            }
          }
        },
        "cookieyes-*": {
          "type": "object",
          "properties": {
            "cookie_id": {
              "type": "any"
            },
            "duration": {
              "type": "any"
            },
            "description": {
              "type": "any"
            }
          }
        },
        "VISITOR_INFO1_LIVE": {
          "type": "object",
          "properties": {
            "cookie_id": {
              "type": "any"
            },
            "duration": {
              "type": "any"
            },
            "description": {
              "type": "any"
            }
          }
        },
        "ytidb::LAST_RESULT_ENTRY_KEY": {
          "type": "object",
          "properties": {
            "cookie_id": {
              "type": "any"
            },
            "duration": {
              "type": "any"
            },
            "description": {
              "type": "any"
            }
          }
        },
        "YSC": {
          "type": "object",
          "properties": {
            "cookie_id": {
              "type": "any"
            },
            "duration": {
              "type": "any"
            },
            "description": {
              "type": "any"
            }
          }
        },
        "AWSALB": {
          "type": "object",
          "properties": {
            "cookie_id": {
              "type": "any"
            },
            "duration": {
              "type": "any"
            },
            "description": {
              "type": "any"
            }
          }
        },
        "__Secure-YNID": {
          "type": "object",
          "properties": {
            "cookie_id": {
              "type": "any"
            },
            "duration": {
              "type": "any"
            },
            "description": {
              "type": "any"
            }
          }
        },
        "__Secure-ROLLOUT_TOKEN": {
          "type": "object",
          "properties": {
            "cookie_id": {
              "type": "any"
            },
            "duration": {
              "type": "any"
            },
            "description": {
              "type": "any"
            }
          }
        },
        "__Secure-YEC": {
          "type": "object",
          "properties": {
            "cookie_id": {
              "type": "any"
            },
            "duration": {
              "type": "any"
            },
            "description": {
              "type": "any"
            }
          }
        },
        "__Secure-BUCKET": {
          "type": "object",
          "properties": {
            "cookie_id": {
              "type": "any"
            },
            "duration": {
              "type": "any"
            },
            "description": {
              "type": "any"
            }
          }
        }
      }
    },
    "cky_audit_table_empty_text": {
      "type": "string"
    },
    "cky_audit_table_header_id": {
      "type": "string"
    },
    "cky_audit_table_header_duration": {
      "type": "string"
    },
    "cky_audit_table_header_description": {
      "type": "string"
    },
    "cky_preference_necessary_title": {
      "type": "string"
    },
    "cky_preference_necessary_description": {
      "type": "string"
    },
    "cky_preference_functional_title": {
      "type": "string"
    },
    "cky_preference_functional_description": {
      "type": "string"
    },
    "cky_preference_analytics_title": {
      "type": "string"
    },
    "cky_preference_analytics_description": {
      "type": "string"
    },
    "cky_preference_performance_title": {
      "type": "string"
    },
    "cky_preference_performance_description": {
      "type": "string"
    },
    "cky_preference_advertisement_title": {
      "type": "string"
    },
    "cky_preference_advertisement_description": {
      "type": "string"
    },
    "cky_preference_other_title": {
      "type": "string"
    },
    "cky_preference_other_description": {
      "type": "string"
    }
  }
}
```
### `GET` /web-interactives/public/v1/embed/combinedConfigs
```json
{
  "type": "object",
  "properties": {
    "sortedAudienceConfigs": {
      "type": "array",
      "items": "any"
    },
    "requestedConfigs": {
      "type": "array",
      "items": "any"
    },
    "gates": {
      "type": "array",
      "items": "any"
    }
  }
}
```

