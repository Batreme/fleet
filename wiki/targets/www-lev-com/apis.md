---
title: "APIs & Protocols: www-lev-com"
date: 2026-11-14
target: "www-lev-com"
---

# Discovered APIs & Protocols: www-lev-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `POST` | `/api/website-visit-session-link` | `200` | REST endpoint |
| `GET` | `/array/phc_qIESQidXk7O2n5GV3apj5zoJblRhD9tkJrQSYvRDcHT/config` | `200` | REST endpoint |
| `POST` | `/api/csp-report` | `204` | REST endpoint |
| `POST` | `/events` | `200` | REST endpoint |
| `POST` | `/flags/` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `POST` /api/website-visit-session-link
```json
{
  "type": "object",
  "properties": {
    "ok": {
      "type": "boolean"
    }
  }
}
```
### `GET` /array/phc_qIESQidXk7O2n5GV3apj5zoJblRhD9tkJrQSYvRDcHT/config
```json
{
  "type": "object",
  "properties": {
    "analytics": {
      "type": "object",
      "properties": {
        "endpoint": {
          "type": "string"
        }
      }
    },
    "autocaptureExceptions": {
      "type": "boolean"
    },
    "autocapture_opt_out": {
      "type": "boolean"
    },
    "captureDeadClicks": {
      "type": "boolean"
    },
    "capturePerformance": {
      "type": "object",
      "properties": {
        "network_timing": {
          "type": "boolean"
        },
        "web_vitals": {
          "type": "boolean"
        },
        "web_vitals_allowed_metrics": {
          "type": "null"
        }
      }
    },
    "conversations": {
      "type": "object",
      "properties": {
        "collectName": {
          "type": "boolean"
        },
        "color": {
          "type": "string"
        },
        "domains": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "enabled": {
          "type": "boolean"
        },
        "greetingText": {
          "type": "string"
        },
        "identificationFormDescription": {
          "type": "string"
        },
        "identificationFormTitle": {
          "type": "string"
        },
        "placeholderText": {
          "type": "string"
        },
        "requireEmail": {
          "type": "boolean"
        },
        "token": {
          "type": "string"
        },
        "widgetEnabled": {
          "type": "boolean"
        },
        "widgetPosition": {
          "type": "string"
        }
      }
    },
    "defaultIdentifiedOnly": {
      "type": "boolean"
    },
    "elementsChainAsString": {
      "type": "boolean"
    },
    "errorTracking": {
      "type": "object",
      "properties": {
        "autocaptureExceptions": {
          "type": "boolean"
        },
        "suppressionRules": {
          "type": "array",
          "items": {
            "type": "any"
          }
        }
      }
    },
    "hasFeatureFlags": {
      "type": "boolean"
    },
    "heatmaps": {
      "type": "object",
      "properties": {
        "captureMode": {
          "type": "string"
        },
        "urlAllowlist": {
          "type": "array",
          "items": "any"
        },
        "urlAllowlistEnforced": {
          "type": "boolean"
        }
      }
    },
    "logs": {
      "type": "object",
      "properties": {
        "captureConsoleLogs": {
          "type": "boolean"
        }
      }
    },
    "productTours": {
      "type": "boolean"
    },
    "push": {
      "type": "object",
      "properties": {
        "appIds": {
          "type": "array",
          "items": "any"
        }
      }
    },
    "sdkVersion": {
      "type": "object",
      "properties": {
        "requested": {
          "type": "string"
        }
      }
    },
    "sessionRecording": {
      "type": "object",
      "properties": {
        "canvasFps": {
          "type": "number"
        },
        "canvasQuality": {
          "type": "string"
        },
        "consoleLogRecordingEnabled": {
          "type": "boolean"
        },
        "endpoint": {
          "type": "string"
        },
        "eventTriggers": {
          "type": "array",
          "items": "any"
        },
        "linkedFlag": {
          "type": "null"
        },
        "masking": {
          "type": "object",
          "properties": {
            "maskAllInputs": {
              "type": "any"
            }
          }
        },
        "minimumDurationMilliseconds": {
          "type": "null"
        },
        "networkPayloadCapture": {
          "type": "object",
          "properties": {
            "recordBody": {
              "type": "any"
            },
            "recordHeaders": {
              "type": "any"
            }
          }
        },
        "recordCanvas": {
          "type": "boolean"
        },
        "recorderVersion": {
          "type": "string"
        },
        "sampleRate": {
          "type": "null"
        },
        "scriptConfig": {
          "type": "object",
          "properties": {
            "script": {
              "type": "any"
            }
          }
        },
        "triggerMatchType": {
          "type": "null"
        },
        "urlBlocklist": {
          "type": "array",
          "items": "any"
        },
        "urlTriggers": {
          "type": "array",
          "items": "any"
        },
        "version": {
          "type": "number"
        }
      }
    },
    "siteApps": {
      "type": "array",
      "items": "any"
    },
    "supportedCompression": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "surveys": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "appearance": {
            "type": "any"
          },
          "conditions": {
            "type": "any"
          },
          "current_iteration": {
            "type": "any"
          },
          "current_iteration_start_date": {
            "type": "any"
          },
          "enable_partial_responses": {
            "type": "any"
          },
          "end_date": {
            "type": "any"
          },
          "id": {
            "type": "any"
          },
          "internal_targeting_flag_key": {
            "type": "any"
          },
          "name": {
            "type": "any"
          },
          "questions": {
            "type": "any"
          },
          "schedule": {
            "type": "any"
          },
          "start_date": {
            "type": "any"
          },
          "targeting_flag_key": {
            "type": "any"
          },
          "type": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `POST` /flags/
```json
{
  "type": "object",
  "properties": {
    "errorsWhileComputingFlags": {
      "type": "boolean"
    },
    "flags": {
      "type": "object",
      "properties": {
        "chat_banner": {
          "type": "object",
          "properties": {
            "key": {
              "type": "any"
            },
            "enabled": {
              "type": "any"
            },
            "variant": {
              "type": "any"
            },
            "reason": {
              "type": "any"
            },
            "metadata": {
              "type": "any"
            }
          }
        },
        "lead_pipelines": {
          "type": "object",
          "properties": {
            "key": {
              "type": "any"
            },
            "enabled": {
              "type": "any"
            },
            "variant": {
              "type": "any"
            },
            "reason": {
              "type": "any"
            },
            "metadata": {
              "type": "any"
            }
          }
        },
        "contact_import_enrichment": {
          "type": "object",
          "properties": {
            "key": {
              "type": "any"
            },
            "enabled": {
              "type": "any"
            },
            "variant": {
              "type": "any"
            },
            "reason": {
              "type": "any"
            },
            "metadata": {
              "type": "any"
            }
          }
        },
        "web_contact_calling": {
          "type": "object",
          "properties": {
            "key": {
              "type": "any"
            },
            "enabled": {
              "type": "any"
            },
            "variant": {
              "type": "any"
            },
            "reason": {
              "type": "any"
            },
            "metadata": {
              "type": "any"
            }
          }
        },
        "exp-ascendix-meeting-cta": {
          "type": "object",
          "properties": {
            "key": {
              "type": "any"
            },
            "enabled": {
              "type": "any"
            },
            "variant": {
              "type": "any"
            },
            "reason": {
              "type": "any"
            },
            "metadata": {
              "type": "any"
            }
          }
        },
        "credit_memo": {
          "type": "object",
          "properties": {
            "key": {
              "type": "any"
            },
            "enabled": {
              "type": "any"
            },
            "variant": {
              "type": "any"
            },
            "reason": {
              "type": "any"
            },
            "metadata": {
              "type": "any"
            }
          }
        },
        "survey-targeting-4d00b357b1": {
          "type": "object",
          "properties": {
            "key": {
              "type": "any"
            },
            "enabled": {
              "type": "any"
            },
            "variant": {
              "type": "any"
            },
            "reason": {
              "type": "any"
            },
            "metadata": {
              "type": "any"
            }
          }
        },
        "slide_bank": {
          "type": "object",
          "properties": {
            "key": {
              "type": "any"
            },
            "enabled": {
              "type": "any"
            },
            "variant": {
              "type": "any"
            },
            "reason": {
              "type": "any"
            },
            "metadata": {
              "type": "any"
            }
          }
        },
        "buy_box": {
          "type": "object",
          "properties": {
            "key": {
              "type": "any"
            },
            "enabled": {
              "type": "any"
            },
            "variant": {
              "type": "any"
            },
            "reason": {
              "type": "any"
            },
            "metadata": {
              "type": "any"
            }
          }
        },
        "standalone_campaigns": {
          "type": "object",
          "properties": {
            "key": {
              "type": "any"
            },
            "enabled": {
              "type": "any"
            },
            "variant": {
              "type": "any"
            },
            "reason": {
              "type": "any"
            },
            "metadata": {
              "type": "any"
            }
          }
        },
        "survey-targeting-447ca8ae65-custom": {
          "type": "object",
          "properties": {
            "key": {
              "type": "any"
            },
            "enabled": {
              "type": "any"
            },
            "variant": {
              "type": "any"
            },
            "reason": {
              "type": "any"
            },
            "metadata": {
              "type": "any"
            }
          }
        },
        "lev-website-lev-agent": {
          "type": "object",
          "properties": {
            "key": {
              "type": "any"
            },
            "enabled": {
              "type": "any"
            },
            "variant": {
              "type": "any"
            },
            "reason": {
              "type": "any"
            },
            "metadata": {
              "type": "any"
            }
          }
        },
        "survey-targeting-3b041e9aa5-custom": {
          "type": "object",
          "properties": {
            "key": {
              "type": "any"
            },
            "enabled": {
              "type": "any"
            },
            "variant": {
              "type": "any"
            },
            "reason": {
              "type": "any"
            },
            "metadata": {
              "type": "any"
            }
          }
        },
        "scroll-popup-test": {
          "type": "object",
          "properties": {
            "key": {
              "type": "any"
            },
            "enabled": {
              "type": "any"
            },
            "variant": {
              "type": "any"
            },
            "reason": {
              "type": "any"
            },
            "metadata": {
              "type": "any"
            }
          }
        },
        "deal_inbox": {
          "type": "object",
          "properties": {
            "key": {
              "type": "any"
            },
            "enabled": {
              "type": "any"
            },
            "variant": {
              "type": "any"
            },
            "reason": {
              "type": "any"
            },
            "metadata": {
              "type": "any"
            }
          }
        },
        "survey-targeting-aea44ca699-custom": {
          "type": "object",
          "properties": {
            "key": {
              "type": "any"
            },
            "enabled": {
              "type": "any"
            },
            "variant": {
              "type": "any"
            },
            "reason": {
              "type": "any"
            },
            "metadata": {
              "type": "any"
            }
          }
        },
        "sourcing": {
          "type": "object",
          "properties": {
            "key": {
              "type": "any"
            },
            "enabled": {
              "type": "any"
            },
            "variant": {
              "type": "any"
            },
            "reason": {
              "type": "any"
            },
            "metadata": {
              "type": "any"
            }
          }
        },
        "iab-signup-banner": {
          "type": "object",
          "properties": {
            "key": {
              "type": "any"
            },
            "enabled": {
              "type": "any"
            },
            "variant": {
              "type": "any"
            },
            "reason": {
              "type": "any"
            },
            "metadata": {
              "type": "any"
            }
          }
        },
        "credit_approval_test": {
          "type": "object",
          "properties": {
            "key": {
              "type": "any"
            },
            "enabled": {
              "type": "any"
            },
            "variant": {
              "type": "any"
            },
            "reason": {
              "type": "any"
            },
            "metadata": {
              "type": "any"
            }
          }
        },
        "beta_release_announcement": {
          "type": "object",
          "properties": {
            "key": {
              "type": "any"
            },
            "enabled": {
              "type": "any"
            },
            "variant": {
              "type": "any"
            },
            "reason": {
              "type": "any"
            },
            "metadata": {
              "type": "any"
            }
          }
        }
      }
    },
    "requestId": {
      "type": "string"
    },
    "evaluatedAt": {
      "type": "number"
    }
  }
}
```

