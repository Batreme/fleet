---
title: "APIs & Protocols: www-routedurhum-com"
date: 2026-11-14
target: "[[overview|www-routedurhum-com]]"
---

# Discovered APIs & Protocols: www-routedurhum-com

## 📡 Endpoint Catalog

| Method | Path | Status | Protocol / Operation |
|---|---|---|---|
| `GET` | `/rdr-elements/dose.json` | `200` | REST endpoint |
| `GET` | `/_functions/accueilApercu` | `200` | REST endpoint |
| `POST` | `/api/v1/bulklog` | `204` | REST endpoint |
| `GET` | `/_functions/dernieresInfos` | `200` | REST endpoint |
| `GET` | `/_functions/classement` | `200` | REST endpoint |
| `GET` | `/pages/pages/thunderbolt` | `200` | REST endpoint |
| `GET` | `/pages/pages/thunderbolt` | `200` | REST endpoint |
| `GET` | `/pages/pages/thunderbolt` | `200` | REST endpoint |
| `GET` | `/media/3e0895_82d10f21a48544de926bff1637d18875~mv2.avif/v1/fill/w_240,h_300,al_c,q_74,enc_avif,quality_auto/img.avif` | `200` | REST endpoint |
| `GET` | `/media/547c0f_b65d06d6f43e4d4b9d74635fbaf1c267~mv2.avif/v1/fill/w_240,h_300,al_c,q_74,enc_avif,quality_auto/img.avif` | `200` | REST endpoint |
| `GET` | `/media/547c0f_0ec7bede97ca4fce963691b88f05cf7f~mv2.avif/v1/fill/w_240,h_300,al_c,q_74,enc_avif,quality_auto/img.avif` | `200` | REST endpoint |
| `GET` | `/media/547c0f_12a0d916e9f041a29cb03fa50e3c3918~mv2.avif/v1/fill/w_240,h_300,al_c,q_74,enc_avif,quality_auto/img.avif` | `200` | REST endpoint |
| `GET` | `/media/547c0f_f3c314a0d40f4b9387c88f609ff9fdc0~mv2.avif/v1/fill/w_240,h_300,al_c,q_74,enc_avif,quality_auto/img.avif` | `200` | REST endpoint |
| `GET` | `/media/547c0f_f37ba0120dd540a3b780feeab92eeee7~mv2.avif/v1/fill/w_240,h_300,al_c,q_74,enc_avif,quality_auto/img.avif` | `200` | REST endpoint |
| `GET` | `/rdr-elements/statique/abord.json` | `200` | REST endpoint |
| `POST` | `/api/v1/bulklog` | `204` | REST endpoint |
| `POST` | `/api/v1/bulklog` | `204` | REST endpoint |
| `GET` | `/pages/pages/thunderbolt` | `200` | REST endpoint |
| `GET` | `/rdr-elements/statique/entete-pied-fr.json` | `200` | REST endpoint |
| `POST` | `/api/v1/bulklog` | `204` | REST endpoint |
| `GET` | `/rdr-elements/statique/accueil-attrs-fr.json` | `200` | REST endpoint |
| `POST` | `/api/v1/bulklog` | `204` | REST endpoint |
| `GET` | `/_api/v1/access-tokens` | `200` | REST endpoint |
| `GET` | `/media/547c0f_a192c1ad17974cfe97268940dd6cbedb~mv2.avif/v1/fill/w_240,h_300,al_c,q_74,enc_avif,quality_auto/img.avif` | `200` | REST endpoint |
| `GET` | `/media/547c0f_b3617d428e8f45aaa42555c8fc87f670~mv2.avif/v1/fill/w_240,h_300,al_c,q_74,enc_avif,quality_auto/img.avif` | `200` | REST endpoint |
| `GET` | `/media/547c0f_10a907dd3b0d46379c426d3ae00ae34b~mv2.avif/v1/fill/w_240,h_300,al_c,q_74,enc_avif,quality_auto/img.avif` | `200` | REST endpoint |
| `GET` | `/media/547c0f_90080eeff06f478395d99e7ef36482dc~mv2.avif/v1/fill/w_240,h_300,al_c,q_74,enc_avif,quality_auto/img.avif` | `200` | REST endpoint |
| `GET` | `/media/547c0f_f4bba3e2571b4ccabbbb17a721d2fb31~mv2.avif/v1/fill/w_240,h_300,al_c,q_74,enc_avif,quality_auto/img.avif` | `200` | REST endpoint |
| `GET` | `/media/547c0f_a796bcb980d2403b97fc1d2c89182641~mv2.avif/v1/fill/w_240,h_300,al_c,q_74,enc_avif,quality_auto/img.avif` | `200` | REST endpoint |
| `POST` | `/api/v1/bulklog` | `204` | REST endpoint |

---

## 📦 Inferred Payload Schemas

### `GET` /rdr-elements/dose.json
```json
{
  "type": "object",
  "properties": {
    "taux": {
      "type": "number"
    },
    "statique": {
      "type": "boolean"
    }
  }
}
```
### `GET` /_functions/accueilApercu
```json
{
  "type": "object",
  "properties": {
    "badges": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "cle": {
            "type": "any"
          },
          "image": {
            "type": "any"
          },
          "fr": {
            "type": "any"
          },
          "en": {
            "type": "any"
          }
        }
      }
    },
    "medias": {
      "type": "object",
      "properties": {
        "video": {
          "type": "string"
        },
        "videoAffiche": {
          "type": "string"
        },
        "filigrane": {
          "type": "string"
        },
        "topo": {
          "type": "string"
        },
        "topoFaq": {
          "type": "string"
        },
        "espacePhoto": {
          "type": "string"
        },
        "tymalFond": {
          "type": "string"
        },
        "tymalVideo": {
          "type": "string"
        },
        "tymalDrapeau": {
          "type": "string"
        },
        "youtube": {
          "type": "string"
        },
        "logoIntro": {
          "type": "string"
        }
      }
    },
    "classes": {
      "type": "object",
      "properties": {
        "Ultim": {
          "type": "object",
          "properties": {
            "c": {
              "type": "any"
            },
            "n": {
              "type": "any"
            },
            "icone": {
              "type": "any"
            }
          }
        },
        "Ocean Fifty": {
          "type": "object",
          "properties": {
            "c": {
              "type": "any"
            },
            "n": {
              "type": "any"
            },
            "icone": {
              "type": "any"
            }
          }
        },
        "Class40": {
          "type": "object",
          "properties": {
            "c": {
              "type": "any"
            },
            "n": {
              "type": "any"
            },
            "icone": {
              "type": "any"
            }
          }
        },
        "IMOCA": {
          "type": "object",
          "properties": {
            "c": {
              "type": "any"
            },
            "n": {
              "type": "any"
            },
            "icone": {
              "type": "any"
            }
          }
        },
        "Vintage Mono": {
          "type": "object",
          "properties": {
            "c": {
              "type": "any"
            },
            "n": {
              "type": "any"
            },
            "icone": {
              "type": "any"
            }
          }
        },
        "Vintage Multi": {
          "type": "object",
          "properties": {
            "c": {
              "type": "any"
            },
            "n": {
              "type": "any"
            },
            "icone": {
              "type": "any"
            }
          }
        }
      }
    },
    "phases": {
      "type": "object",
      "properties": {
        "avant": {
          "type": "object",
          "properties": {
            "photo": {
              "type": "any"
            },
            "titre": {
              "type": "any"
            },
            "faits": {
              "type": "any"
            },
            "ctas": {
              "type": "any"
            },
            "affiche": {
              "type": "any"
            },
            "depart": {
              "type": "any"
            }
          }
        },
        "village": {
          "type": "object",
          "properties": {
            "debut": {
              "type": "any"
            },
            "photo": {
              "type": "any"
            },
            "titre": {
              "type": "any"
            },
            "faits": {
              "type": "any"
            },
            "ctas": {
              "type": "any"
            },
            "affiche": {
              "type": "any"
            },
            "depart": {
              "type": "any"
            },
            "tymal": {
              "type": "any"
            }
          }
        },
        "depart": {
          "type": "object",
          "properties": {
            "debut": {
              "type": "any"
            },
            "photo": {
              "type": "any"
            },
            "titre": {
              "type": "any"
            },
            "faits": {
              "type": "any"
            },
            "ctas": {
              "type": "any"
            },
            "affiche": {
              "type": "any"
            },
            "depart": {
              "type": "any"
            },
            "tymal": {
              "type": "any"
            },
            "trio": {
              "type": "any"
            }
          }
        },
        "course": {
          "type": "object",
          "properties": {
            "debut": {
              "type": "any"
            },
            "photo": {
              "type": "any"
            },
            "titre": {
              "type": "any"
            },
            "faits": {
              "type": "any"
            },
            "ctas": {
              "type": "any"
            },
            "affiche": {
              "type": "any"
            },
            "depart": {
              "type": "any"
            },
            "tymal": {
              "type": "any"
            },
            "course": {
              "type": "any"
            },
            "faq": {
              "type": "any"
            }
          }
        }
      }
    },
    "actus": {
      "type": "array",
      "items": "any"
    },
    "skippers": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "prenom": {
            "type": "any"
          },
          "nom": {
            "type": "any"
          },
          "bateau": {
            "type": "any"
          },
          "photoVignette": {
            "type": "any"
          },
          "drapeau": {
            "type": "any"
          },
          "classes": {
            "type": "any"
          }
        }
      }
    },
    "faq": {
      "type": "object",
      "properties": {
        "kicker": {
          "type": "string"
        },
        "titre": {
          "type": "string"
        },
        "toutes": {
          "type": "object",
          "properties": {
            "texte": {
              "type": "any"
            },
            "url": {
              "type": "any"
            }
          }
        },
        "questions": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "exemple": {
          "type": "string"
        }
      }
    },
    "calendrier": {
      "type": "object",
      "properties": {
        "moments": {
          "type": "object",
          "properties": {
            "ouverture-village": {
              "type": "any"
            },
            "veille-depart": {
              "type": "any"
            },
            "passage-course": {
              "type": "any"
            },
            "depart": {
              "type": "any"
            }
          }
        },
        "apercu": {
          "type": "string"
        }
      }
    }
  }
}
```
### `GET` /_functions/dernieresInfos
```json
{
  "type": "object",
  "properties": {
    "maj": {
      "type": "string"
    },
    "relire": {
      "type": "number"
    },
    "infos": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "any"
          },
          "niveau": {
            "type": "any"
          },
          "pages": {
            "type": "any"
          },
          "texte": {
            "type": "any"
          },
          "lien": {
            "type": "any"
          },
          "libelleLien": {
            "type": "any"
          },
          "debut": {
            "type": "any"
          },
          "fin": {
            "type": "any"
          }
        }
      }
    },
    "recap": {
      "type": "object",
      "properties": {
        "titre": {
          "type": "string"
        },
        "texte": {
          "type": "string"
        },
        "youtube": {
          "type": "string"
        }
      }
    },
    "recaps": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "titre": {
            "type": "any"
          },
          "texte": {
            "type": "any"
          },
          "youtube": {
            "type": "any"
          },
          "date": {
            "type": "any"
          }
        }
      }
    }
  }
}
```
### `GET` /_functions/classement
```json
{
  "type": "object",
  "properties": {
    "phase": {
      "type": "string"
    },
    "depart": {
      "type": "string"
    },
    "maj": {
      "type": "string"
    },
    "distance": {
      "type": "number"
    },
    "classes": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "any"
          },
          "cle": {
            "type": "any"
          },
          "nom": {
            "type": "any"
          },
          "couleur": {
            "type": "any"
          },
          "icone": {
            "type": "any"
          },
          "partants": {
            "type": "any"
          },
          "lignes": {
            "type": "any"
          }
        }
      }
    },
    "identifies": {
      "type": "number"
    },
    "partants": {
      "type": "number"
    },
    "intervalleMin": {
      "type": "number"
    },
    "prochain": {
      "type": "string"
    },
    "medias": {
      "type": "object",
      "properties": {
        "motif": {
          "type": "string"
        },
        "filigrane": {
          "type": "string"
        }
      }
    },
    "sources": {
      "type": "object",
      "properties": {
        "xml": {
          "type": "string"
        }
      }
    }
  }
}
```
### `GET` /pages/pages/thunderbolt
```json
{
  "type": "object",
  "properties": {
    "stateRefs": {
      "type": "object",
      "properties": {}
    },
    "structure": {
      "type": "object",
      "properties": {
        "components": {
          "type": "object",
          "properties": {
            "masterPage": {
              "type": "any"
            },
            "BACKGROUND_GROUP": {
              "type": "any"
            },
            "SCROLL_TO_TOP": {
              "type": "any"
            },
            "SCROLL_TO_BOTTOM": {
              "type": "any"
            },
            "SKIP_TO_CONTENT_BTN": {
              "type": "any"
            },
            "SITE_HEADER": {
              "type": "any"
            },
            "PAGES_CONTAINER": {
              "type": "any"
            },
            "SITE_PAGES": {
              "type": "any"
            },
            "SITE_FOOTER": {
              "type": "any"
            }
          }
        },
        "features": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "siteFeaturesConfigs": {
          "type": "object",
          "properties": {
            "mpaNavigation": {
              "type": "any"
            },
            "pages": {
              "type": "any"
            },
            "reporter": {
              "type": "any"
            },
            "passwordProtectedPage": {
              "type": "any"
            },
            "environmentService": {
              "type": "any"
            },
            "siteLocaleService": {
              "type": "any"
            },
            "translations": {
              "type": "any"
            },
            "pageAnchors": {
              "type": "any"
            },
            "lightbox": {
              "type": "any"
            },
            "stickyToComponent": {
              "type": "any"
            },
            "componentsLoader": {
              "type": "any"
            },
            "ooi": {
              "type": "any"
            },
            "siteMembers": {
              "type": "any"
            },
            "captcha": {
              "type": "any"
            },
            "protectedPages": {
              "type": "any"
            },
            "windowScroll": {
              "type": "any"
            },
            "ooiTpaSharedConfig": {
              "type": "any"
            },
            "tpa": {
              "type": "any"
            },
            "seo": {
              "type": "any"
            },
            "router": {
              "type": "any"
            }
          }
        }
      }
    },
    "props": {
      "type": "object",
      "properties": {
        "scrollRestoration": {
          "type": "object",
          "properties": {
            "shouldRestoreScrollPosition": {
              "type": "any"
            }
          }
        },
        "accessibilityBrowserZoom": {
          "type": "object",
          "properties": {
            "isBuilder": {
              "type": "any"
            },
            "isStudio": {
              "type": "any"
            }
          }
        },
        "animations": {
          "type": "object",
          "properties": {
            "repeaterTemplateToParentMap": {
              "type": "any"
            },
            "isPreview": {
              "type": "any"
            }
          }
        },
        "siteMembers": {
          "type": "object",
          "properties": {
            "componentIds": {
              "type": "any"
            }
          }
        },
        "scrollToAnchor": {
          "type": "object",
          "properties": {
            "anchorDataIdToCompIdMap": {
              "type": "any"
            },
            "nicknameToCompIdMap": {
              "type": "any"
            },
            "compsToUpdate": {
              "type": "any"
            },
            "isAnchorsLinksOnPageWithoutTopAndBottom": {
              "type": "any"
            },
            "isBuilderComponentModel": {
              "type": "any"
            },
            "anchorNameToCompIdMap": {
              "type": "any"
            },
            "isResponsive": {
              "type": "any"
            }
          }
        },
        "windowScroll": {
          "type": "object",
          "properties": {
            "headerContainerComponentId": {
              "type": "any"
            }
          }
        },
        "tpa": {
          "type": "object",
          "properties": {
            "widgets": {
              "type": "any"
            },
            "tpaGalleriesImageItems": {
              "type": "any"
            },
            "pageId": {
              "type": "any"
            },
            "hasWixTpaOnPage": {
              "type": "any"
            },
            "tpaInnerRouteConfig": {
              "type": "any"
            },
            "appPublicData": {
              "type": "any"
            },
            "isFixedHeader": {
              "type": "any"
            },
            "siteScale": {
              "type": "any"
            }
          }
        },
        "domSelectors": {
          "type": "object",
          "properties": {
            "allComponentIds": {
              "type": "any"
            }
          }
        },
        "components": {
          "type": "object",
          "properties": {
            "componentsUnderFoldMap": {
              "type": "any"
            }
          }
        },
        "siteWixCodeSdk": {
          "type": "object",
          "properties": {
            "pagesData": {
              "type": "any"
            },
            "nonPopupsPagesData": {
              "type": "any"
            },
            "lightboxes": {
              "type": "any"
            }
          }
        },
        "windowWixCodeSdk": {
          "type": "object",
          "properties": {
            "popupNameToPageId": {
              "type": "any"
            },
            "popupPageIdToName": {
              "type": "any"
            },
            "popupTpaPageIdToPageId": {
              "type": "any"
            },
            "pageId": {
              "type": "any"
            },
            "templateIdToCompIdMap": {
              "type": "any"
            },
            "appDefIdToCompIdsMap": {
              "type": "any"
            }
          }
        },
        "seoWixCodeSdk": {
          "type": "object",
          "properties": {
            "pageId": {
              "type": "any"
            },
            "description": {
              "type": "any"
            },
            "ogImage": {
              "type": "any"
            },
            "ogImageHeight": {
              "type": "any"
            },
            "ogImageWidth": {
              "type": "any"
            },
            "pageName": {
              "type": "any"
            },
            "title": {
              "type": "any"
            },
            "advancedSeoData": {
              "type": "any"
            },
            "currentPageUrl": {
              "type": "any"
            },
            "translationsData": {
              "type": "any"
            },
            "tpaPageId": {
              "type": "any"
            },
            "managingAppDefId": {
              "type": "any"
            }
          }
        },
        "motion": {
          "type": "object",
          "properties": {
            "animationDataByCompId": {
              "type": "any"
            },
            "scrubAnimationBreakpoints": {
              "type": "any"
            },
            "repeaterTemplateToParentMap": {
              "type": "any"
            },
            "isResponsive": {
              "type": "any"
            }
          }
        },
        "triggersAndReactions": {
          "type": "object",
          "properties": {
            "compsToTriggers": {
              "type": "any"
            },
            "compIdsWithAccessibleTrigger": {
              "type": "any"
            },
            "isTouchDevice": {
              "type": "any"
            },
            "repeaterDescendantToRepeaterMapper": {
              "type": "any"
            },
            "compsToEffects": {
              "type": "any"
            },
            "compEffectsToVariantId": {
              "type": "any"
            },
            "variantIdToEffect": {
              "type": "any"
            },
            "viewportTriggerCompsToParams": {
              "type": "any"
            },
            "presetVariantsToReactionVariants": {
              "type": "any"
            },
            "effectTriggerToReaction": {
              "type": "any"
            },
            "scrubReactionWithBpRanges": {
              "type": "any"
            },
            "scrubBpRanges": {
              "type": "any"
            },
            "dynamicCompToDescendants": {
              "type": "any"
            },
            "isMotionEnabled": {
              "type": "any"
            },
            "breakpointsRanges": {
              "type": "any"
            }
          }
        },
        "reporter": {
          "type": "object",
          "properties": {
            "skipPageView": {
              "type": "any"
            }
          }
        },
        "__componentsConfig__": {
          "type": "object",
          "properties": {}
        },
        "render": {
          "type": "object",
          "properties": {
            "compProps": {
              "type": "any"
            }
          }
        }
      }
    },
    "nicknameToCompIdMaps": {
      "type": "object",
      "properties": {}
    }
  }
}
```
### `GET` /pages/pages/thunderbolt
```json
{
  "type": "object",
  "properties": {
    "stateRefs": {
      "type": "object",
      "properties": {
        "comp-muf9fz41_r_comp-mucghtyv": {
          "type": "object",
          "properties": {
            "experiments": {
              "type": "any"
            }
          }
        },
        "comp-muf9fz41_r_comp-mucgk8e9": {
          "type": "object",
          "properties": {
            "experiments": {
              "type": "any"
            }
          }
        },
        "comp-muf9fz41_r_comp-muip2bp0": {
          "type": "object",
          "properties": {
            "experiments": {
              "type": "any"
            }
          }
        },
        "comp-muf996vx": {
          "type": "object",
          "properties": {
            "experiments": {
              "type": "any"
            }
          }
        },
        "comp-muf99srn": {
          "type": "object",
          "properties": {
            "experiments": {
              "type": "any"
            }
          }
        },
        "comp-mmxzg4ms_r_comp-mtk4ubef": {
          "type": "object",
          "properties": {
            "experiments": {
              "type": "any"
            }
          }
        },
        "comp-mmxzg4ms_r_comp-mnucd699": {
          "type": "object",
          "properties": {
            "experiments": {
              "type": "any"
            }
          }
        },
        "comp-mmv1vptc_r_comp-kd5px9hr": {
          "type": "object",
          "properties": {
            "isOpen": {
              "type": "any"
            },
            "isVisible": {
              "type": "any"
            },
            "toggle": {
              "type": "any"
            },
            "open": {
              "type": "any"
            },
            "close": {
              "type": "any"
            },
            "animate": {
              "type": "any"
            },
            "experiments": {
              "type": "any"
            }
          }
        },
        "comp-mmv1vptc_r_comp-kd5px9kk": {
          "type": "object",
          "properties": {
            "reportBi": {
              "type": "any"
            },
            "currentUrl": {
              "type": "any"
            }
          }
        },
        "comp-mmv1vptc_r_comp-kkmqi5tc": {
          "type": "object",
          "properties": {
            "reportBi": {
              "type": "any"
            },
            "toggle": {
              "type": "any"
            }
          }
        },
        "comp-mne9qeno_r_comp-mne9q97u": {
          "type": "object",
          "properties": {
            "isOpen": {
              "type": "any"
            },
            "isVisible": {
              "type": "any"
            },
            "toggle": {
              "type": "any"
            },
            "open": {
              "type": "any"
            },
            "close": {
              "type": "any"
            },
            "animate": {
              "type": "any"
            },
            "experiments": {
              "type": "any"
            }
          }
        },
        "comp-mne9qeno_r_comp-mne9q99b": {
          "type": "object",
          "properties": {
            "reportBi": {
              "type": "any"
            },
            "currentUrl": {
              "type": "any"
            }
          }
        },
        "comp-mne9qeno_r_comp-mne9q9ak": {
          "type": "object",
          "properties": {
            "reportBi": {
              "type": "any"
            },
            "toggle": {
              "type": "any"
            }
          }
        },
        "comp-mne9xs5l_r_comp-mne9xnff": {
          "type": "object",
          "properties": {
            "isOpen": {
              "type": "any"
            },
            "isVisible": {
              "type": "any"
            },
            "toggle": {
              "type": "any"
            },
            "open": {
              "type": "any"
            },
            "close": {
              "type": "any"
            },
            "animate": {
              "type": "any"
            },
            "experiments": {
              "type": "any"
            }
          }
        },
        "comp-mne9xs5l_r_comp-mne9xngt": {
          "type": "object",
          "properties": {
            "reportBi": {
              "type": "any"
            },
            "currentUrl": {
              "type": "any"
            }
          }
        },
        "comp-mne9xs5l_r_comp-mne9xni0": {
          "type": "object",
          "properties": {
            "reportBi": {
              "type": "any"
            },
            "toggle": {
              "type": "any"
            }
          }
        },
        "comp-mnea0doe_r_comp-mnea094e": {
          "type": "object",
          "properties": {
            "isOpen": {
              "type": "any"
            },
            "isVisible": {
              "type": "any"
            },
            "toggle": {
              "type": "any"
            },
            "open": {
              "type": "any"
            },
            "close": {
              "type": "any"
            },
            "animate": {
              "type": "any"
            },
            "experiments": {
              "type": "any"
            }
          }
        },
        "comp-mnea0doe_r_comp-mnea095o": {
          "type": "object",
          "properties": {
            "reportBi": {
              "type": "any"
            },
            "currentUrl": {
              "type": "any"
            }
          }
        },
        "comp-mnea0doe_r_comp-mnea09ta": {
          "type": "object",
          "properties": {
            "reportBi": {
              "type": "any"
            },
            "toggle": {
              "type": "any"
            }
          }
        },
        "comp-mnea7rxy_r_comp-mnea7ny4": {
          "type": "object",
          "properties": {
            "isOpen": {
              "type": "any"
            },
            "isVisible": {
              "type": "any"
            },
            "toggle": {
              "type": "any"
            },
            "open": {
              "type": "any"
            },
            "close": {
              "type": "any"
            },
            "animate": {
              "type": "any"
            },
            "experiments": {
              "type": "any"
            }
          }
        }
      }
    },
    "structure": {
      "type": "object",
      "properties": {
        "components": {
          "type": "object",
          "properties": {
            "bhup2": {
              "type": "any"
            },
            "Containerbhup2": {
              "type": "any"
            },
            "comp-muf9fz41": {
              "type": "any"
            },
            "comp-muf9fz41_r_comp-mucghtyv": {
              "type": "any"
            },
            "comp-muf9fz41_r_comp-mucghtyv_relative": {
              "type": "any"
            },
            "comp-muf9fz41_r_comp-mucgk8e9": {
              "type": "any"
            },
            "comp-muf9fz41_r_comp-muip2bp0": {
              "type": "any"
            },
            "PAGE_SECTIONSbhup2": {
              "type": "any"
            },
            "comp-muf996vx": {
              "type": "any"
            },
            "comp-muf996vx_relative": {
              "type": "any"
            },
            "comp-muf99srn": {
              "type": "any"
            },
            "comp-mmxzg4ms": {
              "type": "any"
            },
            "comp-mmxzg4ms_r_comp-mm3m1ky0": {
              "type": "any"
            },
            "comp-mmxzg4ms_r_comp-mm3m1ky0_relative": {
              "type": "any"
            },
            "comp-mmxzg4ms_r_comp-mtk4ubef": {
              "type": "any"
            },
            "comp-mmxzg4ms_r_comp-mmxd3qve": {
              "type": "any"
            },
            "comp-mmxzg4ms_r_comp-mmxd3qve_relative": {
              "type": "any"
            },
            "comp-mmxzg4ms_r_comp-msdmqeck": {
              "type": "any"
            },
            "comp-mmxzg4ms_r_comp-mnucd699": {
              "type": "any"
            },
            "comp-mmv1vptc-pinned-layer": {
              "type": "any"
            }
          }
        },
        "features": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "siteFeaturesConfigs": {
          "type": "object",
          "properties": {}
        }
      }
    },
    "props": {
      "type": "object",
      "properties": {
        "scrollRestoration": {
          "type": "object",
          "properties": {
            "shouldRestoreScrollPosition": {
              "type": "any"
            }
          }
        },
        "accessibilityBrowserZoom": {
          "type": "object",
          "properties": {
            "isBuilder": {
              "type": "any"
            },
            "isStudio": {
              "type": "any"
            }
          }
        },
        "animations": {
          "type": "object",
          "properties": {
            "repeaterTemplateToParentMap": {
              "type": "any"
            },
            "isPreview": {
              "type": "any"
            }
          }
        },
        "pageAnchors": {
          "type": "object",
          "properties": {
            "anchors": {
              "type": "any"
            },
            "pageAnchorsObservers": {
              "type": "any"
            },
            "activeAnchorObservers": {
              "type": "any"
            },
            "headerComponentId": {
              "type": "any"
            },
            "isBuilderComponentModel": {
              "type": "any"
            }
          }
        },
        "menuContainer": {
          "type": "object",
          "properties": {
            "menuContainerConfig": {
              "type": "any"
            },
            "menuTogglesConfig": {
              "type": "any"
            }
          }
        },
        "imagePlaceholder": {
          "type": "object",
          "properties": {
            "staticMediaUrl": {
              "type": "any"
            },
            "isSEOBot": {
              "type": "any"
            },
            "userDomainMediaBaseUrl": {
              "type": "any"
            },
            "userDomainMediaPrefixes": {
              "type": "any"
            }
          }
        },
        "siteMembers": {
          "type": "object",
          "properties": {
            "componentIds": {
              "type": "any"
            }
          }
        },
        "scrollToAnchor": {
          "type": "object",
          "properties": {
            "anchorDataIdToCompIdMap": {
              "type": "any"
            },
            "nicknameToCompIdMap": {
              "type": "any"
            },
            "compsToUpdate": {
              "type": "any"
            },
            "isAnchorsLinksOnPageWithoutTopAndBottom": {
              "type": "any"
            },
            "isBuilderComponentModel": {
              "type": "any"
            },
            "anchorNameToCompIdMap": {
              "type": "any"
            },
            "isResponsive": {
              "type": "any"
            }
          }
        },
        "windowScroll": {
          "type": "object",
          "properties": {
            "headerContainerComponentId": {
              "type": "any"
            }
          }
        },
        "tpa": {
          "type": "object",
          "properties": {
            "widgets": {
              "type": "any"
            },
            "tpaGalleriesImageItems": {
              "type": "any"
            },
            "pageId": {
              "type": "any"
            },
            "hasWixTpaOnPage": {
              "type": "any"
            },
            "tpaInnerRouteConfig": {
              "type": "any"
            },
            "appPublicData": {
              "type": "any"
            },
            "isFixedHeader": {
              "type": "any"
            },
            "siteScale": {
              "type": "any"
            }
          }
        },
        "svgLoader": {
          "type": "object",
          "properties": {
            "compIdToSvgDataMap": {
              "type": "any"
            },
            "colorsMap": {
              "type": "any"
            },
            "mediaRootUrl": {
              "type": "any"
            },
            "compIdToVectorArtPropsPaths": {
              "type": "any"
            }
          }
        },
        "wixCustomElementComponent": {
          "type": "object",
          "properties": {
            "customElements": {
              "type": "any"
            },
            "isInSeo": {
              "type": "any"
            }
          }
        },
        "seo": {
          "type": "object",
          "properties": {
            "pageId": {
              "type": "any"
            },
            "description": {
              "type": "any"
            },
            "indexPage": {
              "type": "any"
            },
            "ogImage": {
              "type": "any"
            },
            "ogImageHeight": {
              "type": "any"
            },
            "ogImageWidth": {
              "type": "any"
            },
            "pageName": {
              "type": "any"
            },
            "title": {
              "type": "any"
            },
            "advancedSeoData": {
              "type": "any"
            },
            "currentPageUrl": {
              "type": "any"
            },
            "translationsData": {
              "type": "any"
            },
            "tpaPageId": {
              "type": "any"
            },
            "managingAppDefId": {
              "type": "any"
            }
          }
        },
        "menusCurrentPage": {
          "type": "object",
          "properties": {}
        },
        "domSelectors": {
          "type": "object",
          "properties": {
            "allComponentIds": {
              "type": "any"
            }
          }
        },
        "components": {
          "type": "object",
          "properties": {
            "componentsUnderFoldMap": {
              "type": "any"
            }
          }
        },
        "siteWixCodeSdk": {
          "type": "object",
          "properties": {
            "pagesData": {
              "type": "any"
            },
            "nonPopupsPagesData": {
              "type": "any"
            },
            "lightboxes": {
              "type": "any"
            }
          }
        },
        "windowWixCodeSdk": {
          "type": "object",
          "properties": {
            "isPopup": {
              "type": "any"
            },
            "popupNameToPageId": {
              "type": "any"
            },
            "popupPageIdToName": {
              "type": "any"
            },
            "popupTpaPageIdToPageId": {
              "type": "any"
            },
            "pageId": {
              "type": "any"
            },
            "templateIdToCompIdMap": {
              "type": "any"
            },
            "appDefIdToCompIdsMap": {
              "type": "any"
            }
          }
        },
        "seoWixCodeSdk": {
          "type": "object",
          "properties": {
            "pageId": {
              "type": "any"
            },
            "description": {
              "type": "any"
            },
            "indexPage": {
              "type": "any"
            },
            "ogImage": {
              "type": "any"
            },
            "ogImageHeight": {
              "type": "any"
            },
            "ogImageWidth": {
              "type": "any"
            },
            "pageName": {
              "type": "any"
            },
            "title": {
              "type": "any"
            },
            "advancedSeoData": {
              "type": "any"
            },
            "currentPageUrl": {
              "type": "any"
            },
            "translationsData": {
              "type": "any"
            },
            "tpaPageId": {
              "type": "any"
            },
            "managingAppDefId": {
              "type": "any"
            }
          }
        },
        "motion": {
          "type": "object",
          "properties": {
            "animationDataByCompId": {
              "type": "any"
            },
            "scrubAnimationBreakpoints": {
              "type": "any"
            },
            "repeaterTemplateToParentMap": {
              "type": "any"
            },
            "isResponsive": {
              "type": "any"
            }
          }
        }
      }
    },
    "nicknameToCompIdMaps": {
      "type": "object",
      "properties": {}
    }
  }
}
```
### `GET` /pages/pages/thunderbolt
```json
{
  "type": "object",
  "properties": {
    "sdkData": {
      "type": "object",
      "properties": {
        "bhup2": {
          "type": "object",
          "properties": {
            "currentPageSEODescription": {
              "type": "any"
            },
            "currentPageSEOKeywords": {
              "type": "any"
            },
            "currentUrlPageTitle": {
              "type": "any"
            },
            "visibleInMenu": {
              "type": "any"
            }
          }
        },
        "comp-muf996vx": {
          "type": "object",
          "properties": {
            "initialSdkStyles": {
              "type": "any"
            }
          }
        },
        "comp-mmxzg4ms_r_comp-mmxd3qve": {
          "type": "object",
          "properties": {
            "initialSdkStyles": {
              "type": "any"
            }
          }
        },
        "comp-mmv1vptc_r_comp-kd5px9kk": {
          "type": "object",
          "properties": {
            "pageList": {
              "type": "any"
            }
          }
        },
        "comp-mmv1vptc_r_comp-kkmqi5tc": {
          "type": "object",
          "properties": {
            "isResponsive": {
              "type": "any"
            },
            "svgId": {
              "type": "any"
            },
            "altText": {
              "type": "any"
            },
            "compId": {
              "type": "any"
            },
            "strokeWidth": {
              "type": "any"
            },
            "properties": {
              "type": "any"
            },
            "layout": {
              "type": "any"
            },
            "shadow": {
              "type": "any"
            },
            "colorsMap": {
              "type": "any"
            },
            "overrideColors": {
              "type": "any"
            },
            "mediaSvgUrl": {
              "type": "any"
            }
          }
        },
        "comp-mne9qeno_r_comp-mne9q99b": {
          "type": "object",
          "properties": {
            "pageList": {
              "type": "any"
            }
          }
        },
        "comp-mne9qeno_r_comp-mne9q9ak": {
          "type": "object",
          "properties": {
            "isResponsive": {
              "type": "any"
            },
            "svgId": {
              "type": "any"
            },
            "altText": {
              "type": "any"
            },
            "compId": {
              "type": "any"
            },
            "strokeWidth": {
              "type": "any"
            },
            "properties": {
              "type": "any"
            },
            "layout": {
              "type": "any"
            },
            "shadow": {
              "type": "any"
            },
            "colorsMap": {
              "type": "any"
            },
            "overrideColors": {
              "type": "any"
            },
            "mediaSvgUrl": {
              "type": "any"
            }
          }
        },
        "comp-mne9xs5l_r_comp-mne9xngt": {
          "type": "object",
          "properties": {
            "pageList": {
              "type": "any"
            }
          }
        },
        "comp-mne9xs5l_r_comp-mne9xni0": {
          "type": "object",
          "properties": {
            "isResponsive": {
              "type": "any"
            },
            "svgId": {
              "type": "any"
            },
            "altText": {
              "type": "any"
            },
            "compId": {
              "type": "any"
            },
            "strokeWidth": {
              "type": "any"
            },
            "properties": {
              "type": "any"
            },
            "layout": {
              "type": "any"
            },
            "shadow": {
              "type": "any"
            },
            "colorsMap": {
              "type": "any"
            },
            "overrideColors": {
              "type": "any"
            },
            "mediaSvgUrl": {
              "type": "any"
            }
          }
        },
        "comp-mnea0doe_r_comp-mnea095o": {
          "type": "object",
          "properties": {
            "pageList": {
              "type": "any"
            }
          }
        },
        "comp-mnea0doe_r_comp-mnea09ta": {
          "type": "object",
          "properties": {
            "isResponsive": {
              "type": "any"
            },
            "svgId": {
              "type": "any"
            },
            "altText": {
              "type": "any"
            },
            "compId": {
              "type": "any"
            },
            "strokeWidth": {
              "type": "any"
            },
            "properties": {
              "type": "any"
            },
            "layout": {
              "type": "any"
            },
            "shadow": {
              "type": "any"
            },
            "colorsMap": {
              "type": "any"
            },
            "overrideColors": {
              "type": "any"
            },
            "mediaSvgUrl": {
              "type": "any"
            }
          }
        },
        "comp-mnea7rxy_r_comp-mnea7nzl": {
          "type": "object",
          "properties": {
            "pageList": {
              "type": "any"
            }
          }
        },
        "comp-mnea7rxy_r_comp-mnea7o10": {
          "type": "object",
          "properties": {
            "isResponsive": {
              "type": "any"
            },
            "svgId": {
              "type": "any"
            },
            "altText": {
              "type": "any"
            },
            "compId": {
              "type": "any"
            },
            "strokeWidth": {
              "type": "any"
            },
            "properties": {
              "type": "any"
            },
            "layout": {
              "type": "any"
            },
            "shadow": {
              "type": "any"
            },
            "colorsMap": {
              "type": "any"
            },
            "overrideColors": {
              "type": "any"
            },
            "mediaSvgUrl": {
              "type": "any"
            }
          }
        },
        "comp-mnea9mae_r_comp-mnea9gd8": {
          "type": "object",
          "properties": {
            "pageList": {
              "type": "any"
            }
          }
        },
        "comp-mnea9mae_r_comp-mnea9gen": {
          "type": "object",
          "properties": {
            "isResponsive": {
              "type": "any"
            },
            "svgId": {
              "type": "any"
            },
            "altText": {
              "type": "any"
            },
            "compId": {
              "type": "any"
            },
            "strokeWidth": {
              "type": "any"
            },
            "properties": {
              "type": "any"
            },
            "layout": {
              "type": "any"
            },
            "shadow": {
              "type": "any"
            },
            "colorsMap": {
              "type": "any"
            },
            "overrideColors": {
              "type": "any"
            },
            "mediaSvgUrl": {
              "type": "any"
            }
          }
        },
        "comp-mneamxrz_r_comp-mneamsa1": {
          "type": "object",
          "properties": {
            "pageList": {
              "type": "any"
            }
          }
        },
        "comp-mneamxrz_r_comp-mneamsbl": {
          "type": "object",
          "properties": {
            "isResponsive": {
              "type": "any"
            },
            "svgId": {
              "type": "any"
            },
            "altText": {
              "type": "any"
            },
            "compId": {
              "type": "any"
            },
            "strokeWidth": {
              "type": "any"
            },
            "properties": {
              "type": "any"
            },
            "layout": {
              "type": "any"
            },
            "shadow": {
              "type": "any"
            },
            "colorsMap": {
              "type": "any"
            },
            "overrideColors": {
              "type": "any"
            },
            "mediaSvgUrl": {
              "type": "any"
            }
          }
        },
        "comp-mnebabc8_r_comp-mneba622": {
          "type": "object",
          "properties": {
            "pageList": {
              "type": "any"
            }
          }
        },
        "comp-mnebabc8_r_comp-mneba63i": {
          "type": "object",
          "properties": {
            "isResponsive": {
              "type": "any"
            },
            "svgId": {
              "type": "any"
            },
            "altText": {
              "type": "any"
            },
            "compId": {
              "type": "any"
            },
            "strokeWidth": {
              "type": "any"
            },
            "properties": {
              "type": "any"
            },
            "layout": {
              "type": "any"
            },
            "shadow": {
              "type": "any"
            },
            "colorsMap": {
              "type": "any"
            },
            "overrideColors": {
              "type": "any"
            },
            "mediaSvgUrl": {
              "type": "any"
            }
          }
        }
      }
    },
    "isBuilderDocument": {
      "type": "boolean"
    },
    "responsiveCompsInClassic": {
      "type": "object",
      "properties": {}
    },
    "onLoadProperties": {
      "type": "object",
      "properties": {}
    },
    "containersChildrenIds": {
      "type": "object",
      "properties": {
        "bhup2": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "comp-muf9fz41": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "comp-muf9fz41_r_comp-mucghtyv": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "comp-muf996vx": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "comp-mmxzg4ms": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "comp-mmxzg4ms_r_comp-mm3m1ky0": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "comp-mmxzg4ms_r_comp-mmxd3qve": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "comp-mmv1vptc": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "comp-mmv1vptc_r_comp-kd5px9hr": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "comp-mne9qeno": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "comp-mne9qeno_r_comp-mne9q97u": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "comp-mne9xs5l": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "comp-mne9xs5l_r_comp-mne9xnff": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "comp-mnea0doe": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "comp-mnea0doe_r_comp-mnea094e": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "comp-mnea7rxy": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "comp-mnea7rxy_r_comp-mnea7ny4": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "comp-mnea9mae": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "comp-mnea9mae_r_comp-mnea9gbm": {
          "type": "array",
          "items": {
            "type": "any"
          }
        },
        "comp-mneamxrz": {
          "type": "array",
          "items": {
            "type": "any"
          }
        }
      }
    },
    "compIdToRepeaterId": {
      "type": "object",
      "properties": {}
    },
    "staticEvents": {
      "type": "array",
      "items": "any"
    },
    "ghosts": {
      "type": "object",
      "properties": {
        "structure": {
          "type": "object",
          "properties": {}
        },
        "props": {
          "type": "object",
          "properties": {}
        },
        "parentComponentsUpdates": {
          "type": "object",
          "properties": {}
        }
      }
    },
    "slots": {
      "type": "object",
      "properties": {}
    },
    "applications": {
      "type": "object",
      "properties": {
        "675bbcef-18d8-41f5-800e-131ec9e08762": {
          "type": "object",
          "properties": {
            "wixCode": {
              "type": "any"
            }
          }
        }
      }
    },
    "connections": {
      "type": "object",
      "properties": {
        "wixCode": {
          "type": "object",
          "properties": {
            "page1": {
              "type": "any"
            },
            "section107": {
              "type": "any"
            },
            "entete": {
              "type": "any"
            },
            "fenetreNewsletter": {
              "type": "any"
            },
            "section108": {
              "type": "any"
            },
            "accueilapercu": {
              "type": "any"
            },
            "footer": {
              "type": "any"
            },
            "rdrNotify": {
              "type": "any"
            },
            "Newsletter": {
              "type": "any"
            },
            "newsletter-barre": {
              "type": "any"
            },
            "piedHaut": {
              "type": "any"
            },
            "menuContainer1": {
              "type": "any"
            },
            "expandableMenu1": {
              "type": "any"
            },
            "vectorImage1": {
              "type": "any"
            },
            "menuContainer2": {
              "type": "any"
            },
            "expandableMenu2": {
              "type": "any"
            },
            "vectorImage3": {
              "type": "any"
            },
            "menuContainer3": {
              "type": "any"
            },
            "expandableMenu3": {
              "type": "any"
            },
            "vectorImage116": {
              "type": "any"
            }
          }
        }
      }
    },
    "compIdConnections": {
      "type": "object",
      "properties": {
        "bhup2": {
          "type": "object",
          "properties": {
            "wixCode": {
              "type": "any"
            }
          }
        },
        "comp-muf9fz41_r_comp-mucghtyv": {
          "type": "object",
          "properties": {
            "wixCode": {
              "type": "any"
            }
          }
        },
        "comp-muf9fz41_r_comp-mucgk8e9": {
          "type": "object",
          "properties": {
            "wixCode": {
              "type": "any"
            }
          }
        },
        "comp-muf9fz41_r_comp-muip2bp0": {
          "type": "object",
          "properties": {
            "wixCode": {
              "type": "any"
            }
          }
        },
        "comp-muf996vx": {
          "type": "object",
          "properties": {
            "wixCode": {
              "type": "any"
            }
          }
        },
        "comp-muf99srn": {
          "type": "object",
          "properties": {
            "wixCode": {
              "type": "any"
            }
          }
        },
        "comp-mmxzg4ms_r_comp-mm3m1ky0": {
          "type": "object",
          "properties": {
            "wixCode": {
              "type": "any"
            }
          }
        },
        "comp-mmxzg4ms_r_comp-mtk4ubef": {
          "type": "object",
          "properties": {
            "wixCode": {
              "type": "any"
            }
          }
        },
        "comp-mmxzg4ms_r_comp-mmxd3qve": {
          "type": "object",
          "properties": {
            "wixCode": {
              "type": "any"
            }
          }
        },
        "comp-mmxzg4ms_r_comp-msdmqeck": {
          "type": "object",
          "properties": {
            "wixCode": {
              "type": "any"
            }
          }
        },
        "comp-mmxzg4ms_r_comp-mnucd699": {
          "type": "object",
          "properties": {
            "wixCode": {
              "type": "any"
            }
          }
        },
        "comp-mmv1vptc_r_comp-kd5px9hr": {
          "type": "object",
          "properties": {
            "wixCode": {
              "type": "any"
            }
          }
        },
        "comp-mmv1vptc_r_comp-kd5px9kk": {
          "type": "object",
          "properties": {
            "wixCode": {
              "type": "any"
            }
          }
        },
        "comp-mmv1vptc_r_comp-kkmqi5tc": {
          "type": "object",
          "properties": {
            "wixCode": {
              "type": "any"
            }
          }
        },
        "comp-mne9qeno_r_comp-mne9q97u": {
          "type": "object",
          "properties": {
            "wixCode": {
              "type": "any"
            }
          }
        },
        "comp-mne9qeno_r_comp-mne9q99b": {
          "type": "object",
          "properties": {
            "wixCode": {
              "type": "any"
            }
          }
        },
        "comp-mne9qeno_r_comp-mne9q9ak": {
          "type": "object",
          "properties": {
            "wixCode": {
              "type": "any"
            }
          }
        },
        "comp-mne9xs5l_r_comp-mne9xnff": {
          "type": "object",
          "properties": {
            "wixCode": {
              "type": "any"
            }
          }
        },
        "comp-mne9xs5l_r_comp-mne9xngt": {
          "type": "object",
          "properties": {
            "wixCode": {
              "type": "any"
            }
          }
        },
        "comp-mne9xs5l_r_comp-mne9xni0": {
          "type": "object",
          "properties": {
            "wixCode": {
              "type": "any"
            }
          }
        }
      }
    },
    "orderedControllers": {
      "type": "array",
      "items": "any"
    },
    "controllerConfigs": {
      "type": "object",
      "properties": {
        "675bbcef-18d8-41f5-800e-131ec9e08762": {
          "type": "object",
          "properties": {
            "wixCode": {
              "type": "any"
            }
          }
        }
      }
    },
    "applicationsPublicData": {
      "type": "object",
      "properties": {
        "14cc59bc-f0b7-15b8-e1c7-89ce41d0e0c9": {
          "type": "object",
          "properties": {
            "APP": {
              "type": "any"
            }
          }
        },
        "3c3f3569-205d-4802-9c2d-8e13aaf0d695": {
          "type": "object",
          "properties": {
            "APP": {
              "type": "any"
            }
          }
        }
      }
    },
    "hasTPAComponentOnPage": {
      "type": "boolean"
    },
    "hasBlocksWidgetOnPage": {
      "type": "boolean"
    },
    "allControllersOnPageAreGhosts": {
      "type": "boolean"
    },
    "sosp": {
      "type": "object",
      "properties": {
        "pagesToShowSosp": {
          "type": "object",
          "properties": {}
        },
        "controllersInSosp": {
          "type": "object",
          "properties": {}
        }
      }
    }
  }
}
```

