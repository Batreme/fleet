---
title: "APIs & Protocols: www-sharplink-com"
date: 2026-11-14
target: "[[overview|www-sharplink-com]]"
---

# Discovered APIs & Protocols: www-sharplink-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/_nuxt/builds/meta/b53cb66d-1ab0-4274-a16d-80387405d916.json` | `200` | REST endpoint |
| `GET` | `/api/dashboard/sbet-prices` | `200` | REST endpoint |
| `GET` | `/api/dashboard/sbet-last-trade` | `200` | REST endpoint |
| `GET` | `/api/dashboard/eth-prices-coingecko` | `200` | REST endpoint |
| `GET` | `/api/dashboard/eth-coingecko` | `200` | REST endpoint |
| `GET` | `/api/dashboard/impact3-data` | `200` | REST endpoint |
| `GET` | `/api/dashboard/polygon` | `500` | REST endpoint |
| `GET` | `/f/290008427472090/x/c203c1fda0/shrp_stack.json` | `200` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /_nuxt/builds/meta/b53cb66d-1ab0-4274-a16d-80387405d916.json
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
            "/home": {
              "type": "any"
            },
            "/eth-dashboard": {
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
      "items": "any"
    }
  }
}
```
### `GET` /api/dashboard/sbet-prices
```json
{
  "type": "object",
  "properties": {
    "history": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "date": {
            "type": "any"
          },
          "value": {
            "type": "any"
          }
        }
      }
    },
    "lastPrice": {
      "type": "number"
    },
    "change": {
      "type": "number"
    },
    "changePercent": {
      "type": "string"
    },
    "avgVolume30Day": {
      "type": "number"
    },
    "lastTradeDate": {
      "type": "string"
    }
  }
}
```
### `GET` /api/dashboard/sbet-last-trade
```json
{
  "type": "object",
  "properties": {
    "timestamp": {
      "type": "string"
    },
    "source": {
      "type": "string"
    },
    "price": {
      "type": "number"
    }
  }
}
```
### `GET` /api/dashboard/eth-prices-coingecko
```json
{
  "type": "object",
  "properties": {
    "history": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "date": {
            "type": "any"
          },
          "value": {
            "type": "any"
          }
        }
      }
    },
    "lastPrice": {
      "type": "number"
    },
    "change": {
      "type": "number"
    },
    "changePercent": {
      "type": "string"
    }
  }
}
```
### `GET` /api/dashboard/eth-coingecko
```json
{
  "type": "object",
  "properties": {
    "price": {
      "type": "number"
    },
    "formattedPrice": {
      "type": "string"
    },
    "rawPrice": {
      "type": "number"
    },
    "change24h": {
      "type": "number"
    },
    "changePercent": {
      "type": "string"
    },
    "timestamp": {
      "type": "string"
    },
    "coin": {
      "type": "string"
    }
  }
}
```
### `GET` /api/dashboard/impact3-data
```json
{
  "type": "object",
  "properties": {
    "total_eth_holdings": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "row_number": {
            "type": "any"
          },
          "Date": {
            "type": "any"
          },
          "Total ETH Holdings": {
            "type": "any"
          }
        }
      }
    },
    "eth_nav": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "row_number": {
            "type": "any"
          },
          "Date": {
            "type": "any"
          },
          "ETH NAV": {
            "type": "any"
          }
        }
      }
    },
    "eth_concentration": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "row_number": {
            "type": "any"
          },
          "Date": {
            "type": "any"
          },
          "ETH Concentration": {
            "type": "any"
          }
        }
      }
    },
    "staking_rewards": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "row_number": {
            "type": "any"
          },
          "Date": {
            "type": "any"
          },
          "Staking Rewards (ETH)": {
            "type": "any"
          }
        }
      }
    },
    "mnav_data": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "Date": {
            "type": "any"
          },
          "mNAV": {
            "type": "any"
          },
          "Enterprise Value": {
            "type": "any"
          },
          "NAV": {
            "type": "any"
          },
          "Sharplink NAV": {
            "type": "any"
          },
          "Basic-equivalent NAV per share": {
            "type": "any"
          }
        }
      }
    },
    "Sharplink NAV": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "row_number": {
            "type": "any"
          },
          "Date": {
            "type": "any"
          },
          "Sharplink NAV": {
            "type": "any"
          }
        }
      }
    },
    "Basic-equivalent NAV per share": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "row_number": {
            "type": "any"
          },
          "Date": {
            "type": "any"
          },
          "Basic-equivalent NAV per share": {
            "type": "any"
          }
        }
      }
    },
    "fdmnav": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "Date": {
            "type": "any"
          },
          "Fully Diluted mNAV": {
            "type": "any"
          },
          "Enterprise Value": {
            "type": "any"
          },
          "Market Cap": {
            "type": "any"
          }
        }
      }
    },
    "disclaimer_data": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "Disclaimer Date": {
            "type": "any"
          },
          "Disclaimer Time": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `GET` /api/dashboard/polygon
```json
{
  "type": "object",
  "properties": {
    "error": {
      "type": "boolean"
    },
    "url": {
      "type": "string"
    },
    "statusCode": {
      "type": "number"
    },
    "statusMessage": {
      "type": "string"
    },
    "message": {
      "type": "string"
    }
  }
}
```
### `GET` /f/290008427472090/x/c203c1fda0/shrp_stack.json
```json
{
  "type": "object",
  "properties": {
    "v": {
      "type": "string"
    },
    "fr": {
      "type": "number"
    },
    "ip": {
      "type": "number"
    },
    "op": {
      "type": "number"
    },
    "w": {
      "type": "number"
    },
    "h": {
      "type": "number"
    },
    "nm": {
      "type": "string"
    },
    "ddd": {
      "type": "number"
    },
    "assets": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "any"
          },
          "w": {
            "type": "any"
          },
          "h": {
            "type": "any"
          },
          "u": {
            "type": "any"
          },
          "p": {
            "type": "any"
          },
          "e": {
            "type": "any"
          }
        }
      }
    },
    "layers": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "ddd": {
            "type": "any"
          },
          "ind": {
            "type": "any"
          },
          "ty": {
            "type": "any"
          },
          "nm": {
            "type": "any"
          },
          "refId": {
            "type": "any"
          },
          "sr": {
            "type": "any"
          },
          "ks": {
            "type": "any"
          },
          "ao": {
            "type": "any"
          },
          "ip": {
            "type": "any"
          },
          "op": {
            "type": "any"
          },
          "st": {
            "type": "any"
          },
          "bm": {
            "type": "any"
          }
        }
      }
    }
  }
}
```

