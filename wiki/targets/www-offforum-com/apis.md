---
title: "APIs & Protocols: www-offforum-com"
date: 2026-11-14
target: "www-offforum-com"
---

# Discovered APIs & Protocols: www-offforum-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/_payload.json` | `200` | REST endpoint |
| `GET` | `/_i18n/7163566c/en/messages.json` | `200` | REST endpoint |
| `GET` | `/_nuxt/builds/meta/f81898ee-7d1f-4ef5-8e16-a51221c4185a.json` | `200` | REST endpoint |
| `GET` | `/privacy-policy/_payload.json` | `200` | REST endpoint |
| `GET` | `/_payload.json` | `200` | REST endpoint |
| `GET` | `/about/_payload.json` | `200` | REST endpoint |
| `GET` | `/v1/chunk/B8inz76cuUHs02xbmmH36N7vweZtYO9zwCYs8iYYROAo1uCBr02NRwMBoYqV2eNY96AQmAGL01UCe1nE02qgMzvpqsEBdkknBfxT7GTc00J6LeTA/0.ts` | `200` | REST endpoint |
| `GET` | `/v1/chunk/2cfus2FJoswScqyV1BH01N9iJvibvfJmvPWPgFfsSLfh5vUvMmtsVn2Y1vTElcWozRhg2yZqck7HJEugPg79NCkV3KFdU4MFM/1.ts` | `-1` | REST endpoint |
| `GET` | `/v1/chunk/EamTyGwF1J02jFw28XvTo5O9oRfuylkBc902a02HMsFi1VBZWFt7V3A6A6en5YrDH1Sr83p01DUMzAYtiz00v6vwxpG8qzieNqhD9S56y02n008Ca00/1.ts` | `200` | REST endpoint |
| `GET` | `/v1/chunk/V01bxG2E3wcGMMjw02sVY3AogQFvsOZPrngRZpZJdXdBC02C3QZ6eks01HOiEZ1os00g1Z02kxfGQi68PSfG15b00h00tg/2.ts` | `200` | REST endpoint |

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
### `GET` /_i18n/7163566c/en/messages.json
```json
{
  "type": "object",
  "properties": {
    "en": {
      "type": "object",
      "properties": {
        "404": {
          "type": "object",
          "properties": {
            "back_home": {
              "type": "any"
            }
          }
        },
        "home": {
          "type": "object",
          "properties": {
            "comingNext": {
              "type": "any"
            },
            "live": {
              "type": "any"
            },
            "discoverSingle": {
              "type": "any"
            },
            "discoverMultiple": {
              "type": "any"
            }
          }
        },
        "sat": {
          "type": "string"
        },
        "event": {
          "type": "object",
          "properties": {
            "workshop": {
              "type": "any"
            },
            "date": {
              "type": "any"
            }
          }
        },
        "consent": {
          "type": "object",
          "properties": {
            "boxTitle": {
              "type": "any"
            },
            "introTitle": {
              "type": "any"
            },
            "intro": {
              "type": "any"
            },
            "linkLabel": {
              "type": "any"
            },
            "link": {
              "type": "any"
            },
            "customize": {
              "type": "any"
            },
            "acceptNecessary": {
              "type": "any"
            },
            "accept": {
              "type": "any"
            },
            "title": {
              "type": "any"
            },
            "alwaysOn": {
              "type": "any"
            },
            "acceptSelection": {
              "type": "any"
            },
            "prev": {
              "type": "any"
            },
            "cookies": {
              "type": "any"
            }
          }
        }
      }
    }
  }
}
```
### `GET` /_nuxt/builds/meta/f81898ee-7d1f-4ef5-8e16-a51221c4185a.json
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
### `GET` /privacy-policy/_payload.json
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
### `GET` /about/_payload.json
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

