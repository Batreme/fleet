---
title: "APIs & Protocols: supermodels-phototypelabs-com"
date: 2026-11-14
target: "supermodels-phototypelabs-com"
---

# Discovered APIs & Protocols: supermodels-phototypelabs-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/api/posts` | `200` | REST endpoint |
| `GET` | `/api/landingConfig` | `200` | REST endpoint |
| `GET` | `/v1alpha/projects/-/apps/1:271024040881:web:ee3d1ca433a180f71feb90/webConfig` | `200` | REST endpoint |
| `POST` | `/v1/projects/supermodels-15e8f/installations` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /api/posts
```json
{
  "type": "object",
  "properties": {
    "posts": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "slug": {
            "type": "any"
          },
          "title": {
            "type": "any"
          },
          "excerpt": {
            "type": "any"
          },
          "featuredImage": {
            "type": "any"
          },
          "featuredImageAlt": {
            "type": "any"
          },
          "publishedAt": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `GET` /api/landingConfig
```json
{
  "type": "object",
  "properties": {
    "version": {
      "type": "number"
    },
    "navigation": {
      "type": "object",
      "properties": {
        "catalog": {
          "type": "string"
        },
        "providers": {
          "type": "string"
        },
        "experience": {
          "type": "string"
        },
        "manifesto": {
          "type": "string"
        },
        "work": {
          "type": "string"
        },
        "pricing": {
          "type": "string"
        },
        "faq": {
          "type": "string"
        },
        "signIn": {
          "type": "string"
        }
      }
    },
    "collection": {
      "type": "object",
      "properties": {
        "eyebrow": {
          "type": "string"
        },
        "headline": {
          "type": "string"
        },
        "counter": {
          "type": "string"
        },
        "focusLabel": {
          "type": "string"
        },
        "focusModelKey": {
          "type": "string"
        },
        "focusAction": {
          "type": "string"
        },
        "note": {
          "type": "string"
        },
        "allModelsAction": {
          "type": "string"
        },
        "featuredModels": {
          "type": "array",
          "items": {
            "type": "any"
          }
        }
      }
    },
    "providers": {
      "type": "object",
      "properties": {
        "eyebrow": {
          "type": "string"
        },
        "headline": {
          "type": "string"
        },
        "description": {
          "type": "string"
        },
        "note": {
          "type": "string"
        }
      }
    },
    "manifesto": {
      "type": "object",
      "properties": {
        "eyebrow": {
          "type": "string"
        },
        "headline": {
          "type": "string"
        },
        "description": {
          "type": "string"
        },
        "leftNote": {
          "type": "string"
        },
        "rightNote": {
          "type": "string"
        }
      }
    },
    "pricing": {
      "type": "object",
      "properties": {
        "eyebrow": {
          "type": "string"
        },
        "headline": {
          "type": "string"
        },
        "description": {
          "type": "string"
        },
        "estimateNote": {
          "type": "string"
        }
      }
    },
    "closing": {
      "type": "object",
      "properties": {
        "eyebrow": {
          "type": "string"
        },
        "headline": {
          "type": "string"
        },
        "description": {
          "type": "string"
        },
        "action": {
          "type": "string"
        },
        "actionLink": {
          "type": "string"
        },
        "sideNote": {
          "type": "string"
        },
        "imageUrl": {
          "type": "string"
        }
      }
    },
    "sectionStyles": {
      "type": "object",
      "properties": {
        "page": {
          "type": "object",
          "properties": {
            "backgroundColor": {
              "type": "any"
            },
            "backgroundImageUrl": {
              "type": "any"
            }
          }
        },
        "hero": {
          "type": "object",
          "properties": {
            "backgroundColor": {
              "type": "any"
            },
            "backgroundImageUrl": {
              "type": "any"
            }
          }
        },
        "collection": {
          "type": "object",
          "properties": {
            "backgroundImageUrl": {
              "type": "any"
            },
            "backgroundColor": {
              "type": "any"
            }
          }
        },
        "catalog": {
          "type": "object",
          "properties": {
            "backgroundColor": {
              "type": "any"
            },
            "backgroundImageUrl": {
              "type": "any"
            }
          }
        },
        "providers": {
          "type": "object",
          "properties": {
            "backgroundImageUrl": {
              "type": "any"
            },
            "backgroundColor": {
              "type": "any"
            }
          }
        },
        "manifesto": {
          "type": "object",
          "properties": {
            "backgroundImageUrl": {
              "type": "any"
            },
            "backgroundColor": {
              "type": "any"
            }
          }
        },
        "workspace": {
          "type": "object",
          "properties": {
            "backgroundColor": {
              "type": "any"
            },
            "backgroundImageUrl": {
              "type": "any"
            }
          }
        },
        "principles": {
          "type": "object",
          "properties": {
            "backgroundColor": {
              "type": "any"
            },
            "backgroundImageUrl": {
              "type": "any"
            }
          }
        },
        "work": {
          "type": "object",
          "properties": {
            "backgroundColor": {
              "type": "any"
            },
            "backgroundImageUrl": {
              "type": "any"
            }
          }
        },
        "pricing": {
          "type": "object",
          "properties": {
            "backgroundColor": {
              "type": "any"
            },
            "backgroundImageUrl": {
              "type": "any"
            }
          }
        },
        "faq": {
          "type": "object",
          "properties": {
            "backgroundColor": {
              "type": "any"
            },
            "backgroundImageUrl": {
              "type": "any"
            }
          }
        },
        "closing": {
          "type": "object",
          "properties": {
            "backgroundColor": {
              "type": "any"
            },
            "backgroundImageUrl": {
              "type": "any"
            }
          }
        }
      }
    },
    "categoryAvailability": {
      "type": "object",
      "properties": {
        "image:Fastest Models": {
          "type": "object",
          "properties": {
            "enabled": {
              "type": "any"
            }
          }
        },
        "image:Best Models": {
          "type": "object",
          "properties": {
            "enabled": {
              "type": "any"
            }
          }
        },
        "image:Image editing": {
          "type": "object",
          "properties": {
            "enabled": {
              "type": "any"
            }
          }
        },
        "image:Upscale image": {
          "type": "object",
          "properties": {
            "enabled": {
              "type": "any"
            }
          }
        },
        "video:Best Models": {
          "type": "object",
          "properties": {
            "enabled": {
              "type": "any"
            }
          }
        },
        "video:Fastest Models": {
          "type": "object",
          "properties": {
            "enabled": {
              "type": "any"
            }
          }
        },
        "video:Video upscalers": {
          "type": "object",
          "properties": {
            "enabled": {
              "type": "any"
            }
          }
        },
        "video:Avatar video": {
          "type": "object",
          "properties": {
            "enabled": {
              "type": "any"
            }
          }
        },
        "voice:Studio narration": {
          "type": "object",
          "properties": {
            "enabled": {
              "type": "any"
            }
          }
        },
        "voice:Expressive direction": {
          "type": "object",
          "properties": {
            "enabled": {
              "type": "any"
            }
          }
        },
        "music:Full songs": {
          "type": "object",
          "properties": {
            "enabled": {
              "type": "any"
            }
          }
        },
        "music:Music clips": {
          "type": "object",
          "properties": {
            "enabled": {
              "type": "any"
            }
          }
        },
        "text:Frontier models": {
          "type": "object",
          "properties": {
            "enabled": {
              "type": "any"
            }
          }
        },
        "text:Fast models": {
          "type": "object",
          "properties": {
            "enabled": {
              "type": "any"
            }
          }
        }
      }
    },
    "copyRevision": {
      "type": "number"
    },
    "footer": {
      "type": "object",
      "properties": {
        "tagline": {
          "type": "string"
        },
        "privacy": {
          "type": "string"
        },
        "signature": {
          "type": "string"
        },
        "signatureUrl": {
          "type": "string"
        }
      }
    },
    "work": {
      "type": "object",
      "properties": {
        "eyebrow": {
          "type": "string"
        },
        "headline": {
          "type": "string"
        },
        "description": {
          "type": "string"
        },
        "valueProps": {
          "type": "array",
          "items": "any"
        },
        "examples": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "steps": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "teamsEyebrow": {
          "type": "string"
        },
        "teamsHeadline": {
          "type": "string"
        },
        "teamsDescription": {
          "type": "string"
        },
        "teamsAction": {
          "type": "string"
        },
        "teamsActionLink": {
          "type": "string"
        }
      }
    },
    "principles": {
      "type": "object",
      "properties": {
        "eyebrow": {
          "type": "string"
        },
        "headline": {
          "type": "string"
        },
        "items": {
          "type": "array",
          "items": {
            "type": "any"
          }
        }
      }
    },
    "workspace": {
      "type": "object",
      "properties": {
        "eyebrow": {
          "type": "string"
        },
        "headline": {
          "type": "string"
        },
        "description": {
          "type": "string"
        },
        "tabs": {
          "type": "array",
          "items": {
            "type": "any"
          }
        }
      }
    },
    "serverUpdatedAt": {
      "type": "object",
      "properties": {
        "_seconds": {
          "type": "number"
        },
        "_nanoseconds": {
          "type": "number"
        }
      }
    },
    "catalog": {
      "type": "object",
      "properties": {
        "eyebrow": {
          "type": "string"
        },
        "headline": {
          "type": "string"
        },
        "description": {
          "type": "string"
        }
      }
    },
    "faq": {
      "type": "object",
      "properties": {
        "eyebrow": {
          "type": "string"
        },
        "headline": {
          "type": "string"
        },
        "items": {
          "type": "array",
          "items": {
            "type": "any"
          }
        }
      }
    },
    "hero": {
      "type": "object",
      "properties": {
        "brand": {
          "type": "string"
        },
        "brandFontFamily": {
          "type": "string"
        },
        "brandFontWeight": {
          "type": "number"
        },
        "brandLetterSpacing": {
          "type": "number"
        },
        "brandBlockColor": {
          "type": "string"
        },
        "brandTextColor": {
          "type": "string"
        },
        "eyebrow": {
          "type": "string"
        },
        "headlineWeight": {
          "type": "number"
        },
        "headlineColor": {
          "type": "string"
        },
        "action": {
          "type": "string"
        },
        "actionLink": {
          "type": "string"
        },
        "imageUrl": {
          "type": "string"
        },
        "imageAlt": {
          "type": "string"
        },
        "images": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "rightNote": {
          "type": "string"
        },
        "leftNote": {
          "type": "string"
        },
        "scrollLabel": {
          "type": "string"
        },
        "description": {
          "type": "string"
        },
        "headline": {
          "type": "string"
        }
      }
    },
    "modelAvailability": {
      "type": "object",
      "properties": {
        "replicate/openai/gpt-image-2.5-flare": {
          "type": "object",
          "properties": {
            "enabled": {
              "type": "any"
            },
            "isNew": {
              "type": "any"
            }
          }
        },
        "replicate/openai/gpt-image-2.5-sunburst": {
          "type": "object",
          "properties": {
            "enabled": {
              "type": "any"
            },
            "isNew": {
              "type": "any"
            }
          }
        },
        "replicate/google/nano-banana-2.1": {
          "type": "object",
          "properties": {
            "enabled": {
              "type": "any"
            },
            "isNew": {
              "type": "any"
            }
          }
        },
        "replicate/black-forest-labs/flux-3-image": {
          "type": "object",
          "properties": {
            "enabled": {
              "type": "any"
            },
            "isNew": {
              "type": "any"
            }
          }
        },
        "replicate/alibaba/qwen-image-3": {
          "type": "object",
          "properties": {
            "enabled": {
              "type": "any"
            },
            "isNew": {
              "type": "any"
            }
          }
        },
        "replicate/alibaba/qwen-image-3-pro": {
          "type": "object",
          "properties": {
            "enabled": {
              "type": "any"
            },
            "isNew": {
              "type": "any"
            }
          }
        },
        "replicate/qwen/qwen-image-layered": {
          "type": "object",
          "properties": {
            "enabled": {
              "type": "any"
            },
            "isNew": {
              "type": "any"
            }
          }
        },
        "replicate/qwen/qwen-edit-multiangle": {
          "type": "object",
          "properties": {
            "enabled": {
              "type": "any"
            },
            "isNew": {
              "type": "any"
            }
          }
        },
        "replicate/prunaai/p-image": {
          "type": "object",
          "properties": {
            "enabled": {
              "type": "any"
            },
            "isNew": {
              "type": "any"
            }
          }
        },
        "replicate/prunaai/p-image-edit": {
          "type": "object",
          "properties": {
            "enabled": {
              "type": "any"
            },
            "isNew": {
              "type": "any"
            }
          }
        },
        "replicate/krea/krea-3": {
          "type": "object",
          "properties": {
            "enabled": {
              "type": "any"
            },
            "isNew": {
              "type": "any"
            }
          }
        },
        "replicate/krea/krea-2-medium": {
          "type": "object",
          "properties": {
            "enabled": {
              "type": "any"
            },
            "isNew": {
              "type": "any"
            }
          }
        },
        "replicate/krea/krea-2-medium-turbo": {
          "type": "object",
          "properties": {
            "enabled": {
              "type": "any"
            },
            "isNew": {
              "type": "any"
            }
          }
        },
        "replicate/krea/krea-2-large": {
          "type": "object",
          "properties": {
            "enabled": {
              "type": "any"
            },
            "isNew": {
              "type": "any"
            }
          }
        },
        "replicate/openai/gpt-image-2": {
          "type": "object",
          "properties": {
            "enabled": {
              "type": "any"
            },
            "isNew": {
              "type": "any"
            }
          }
        },
        "replicate/google/nano-banana-pro": {
          "type": "object",
          "properties": {
            "enabled": {
              "type": "any"
            },
            "isNew": {
              "type": "any"
            }
          }
        },
        "replicate/google/nano-banana-2": {
          "type": "object",
          "properties": {
            "enabled": {
              "type": "any"
            },
            "isNew": {
              "type": "any"
            }
          }
        },
        "replicate/google/nano-banana-2-lite": {
          "type": "object",
          "properties": {
            "enabled": {
              "type": "any"
            },
            "isNew": {
              "type": "any"
            }
          }
        },
        "replicate/black-forest-labs/flux-2-max": {
          "type": "object",
          "properties": {
            "enabled": {
              "type": "any"
            },
            "isNew": {
              "type": "any"
            }
          }
        },
        "replicate/black-forest-labs/flux-2-pro": {
          "type": "object",
          "properties": {
            "enabled": {
              "type": "any"
            },
            "isNew": {
              "type": "any"
            }
          }
        }
      }
    },
    "updatedAt": {
      "type": "string"
    }
  }
}
```
### `GET` /v1alpha/projects/-/apps/1:271024040881:web:ee3d1ca433a180f71feb90/webConfig
```json
{
  "type": "object",
  "properties": {
    "projectId": {
      "type": "string"
    },
    "appId": {
      "type": "string"
    },
    "storageBucket": {
      "type": "string"
    },
    "authDomain": {
      "type": "string"
    },
    "messagingSenderId": {
      "type": "string"
    },
    "measurementId": {
      "type": "string"
    }
  }
}
```
### `POST` /v1/projects/supermodels-15e8f/installations
```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "fid": {
      "type": "string"
    },
    "refreshToken": {
      "type": "string"
    },
    "authToken": {
      "type": "object",
      "properties": {
        "token": {
          "type": "string"
        },
        "expiresIn": {
          "type": "string"
        }
      }
    }
  }
}
```

