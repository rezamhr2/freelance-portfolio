# Graphic sources — freelance portfolio sample webpages

All files under `web/assets/graphics/` were searched for and downloaded on
2026-11-10. Every asset is free for commercial reuse; no Google Images, no
hotlinks, no AI-generated images, no watermarks, no fake brands.

**Current set (2026-11-10, after the taste-filter curation + batch-2 finishing touches):** 28 real
photographs (JPEG, max 1200px) + 20 real product photos (JPEG, max 1200px,
quality 85) = 48 files, ~7 MB. The original 39 SVG files (21 unDraw
illustrations + 18 Heroicons/Lucide icons, 252.5 KB) were **retired
2026-11-10** — see "Retired 2026-11-10" below; they are not deleted, they
live in
`~/workspace/goals/freelance-resume-and-portfolio-samples/hidden_files/retired-graphics-2026-11-10/`
with a README explaining how to restore any of them. The per-file SVG
tables further down this file are kept as the audit trail of what was
retired.

Track 2: the 20 product photos were each visually checked to be the listed
product or the closest same-brand same-category substitute, with the
substitution noted below (2.56 MB + batch-2 additions). Track 3: the 28 replacement photos were
each visually checked the same way (see "Replacement photos (Track 3)").

## Rework note 2026-11-10 — store pages (Aria + Northlight)

No new photos were added in this rework; every image below was already in
the set. What changed is how the existing files are used:

- **Aria hero:** the three carousel slides now use `shopping-bags-paper.jpg`,
  `05-sony-wh-1000xm5.jpg` and `delivery-hero.jpg` as full-bleed CSS
  backgrounds (files unmodified). The Sony XM5 file is still the exact
  Flickr bytes, CC BY-ND 4.0, never resized, cropped or re-encoded.
- **Northlight heroes:** `iphone-18-pro.jpg`, `macbook-air-m5.jpg` and
  `apple-watch-series-11.jpg` are now split-panel backgrounds (photo half +
  white panel half), files unmodified. The iPhone 18 Pro hero is a real
  18 Pro photo since 2026-11-11; the MacBook Air (M4) substitution is
  unchanged and still noted in the page footer.
- **Substitute labelling:** the Aria product modal now shows a short honest
  photo note on the five substitute/representative photos (ids 2, 7, 9, 12,
  13); the De'Longhi note reads "عکس: اسپرسوساز دلونگی کافه ترویزو، مدل
  مشابه همین دستگاه". No photo claim in the UI was changed otherwise.

## Retired 2026-11-10 — the 39 SVGs (0 KEEP / 21 REPLACE / 18 DROP)

Marshall's verdict: the pages look too generic. An audit of the 39 SVGs
(full audit: `/tmp/asset-audit.md`) judged **0 KEEP**: every unDraw
illustration is the same flat style seen on thousands of sites (same
proportions, same default #6C63FF purple, same faceless figures);
recolouring the accent does not make it distinctive. Every Heroicons/Lucide
icon is an interchangeable stroke glyph. The 21 illustrations were replaced
by the 22 real photographs in "Replacement photos (Track 3)"; the 18 icons
were dropped with no replacement — chips and headers now carry themselves
typographically (do not swap in another generic icon set).

The SVGs were moved (not deleted) to
`hidden_files/retired-graphics-2026-11-10/` — to restore one, copy it back
into its page folder under `web/assets/graphics/<page>/` and re-add its
SOURCES.md / PLACEMENT.md entries. The v4 (delivered) and v5 (built,
unsent) zips still contain the SVGs; only the live folder was curated.

## Replacement photos (Track 3, 2026-11-10)

22 real photographs, all PIL-verified as JPEG image bytes and visually
inspected, max 1200px wide, quality 82 (except `vegetable-market.jpg`,
re-encoded at quality 85 after cropping). Licence for each verified on its
source page / API record (Openverse API licence field, Wikimedia Commons
`extmetadata.LicenseShortName`, or the Pexels photo page stating "License,
Free"). **Attribution:** CC BY / CC BY-SA files need a credit line at
wiring time (photographer + licence, as listed). CC0, Public domain and
Pexels files need no credit (a credit is still welcome).

### corporate/ — آریا صنعت توان (3)
| file | what it is | source | author | licence |
|---|---|---|---|---|
| `switchgear.jpg` (1200×900, 146 KB) | Real switchgear cabinet row with gauges and breakers — exactly the distributor's world | https://commons.wikimedia.org/wiki/File%3AElectrical_switchgear.JPG | P199 | Public domain |
| `factory-interior.jpg` (1200×847, 162 KB) | 1936 B&W factory hall: worker at a control panel beside heavy machinery — archival, atmospheric | https://commons.wikimedia.org/wiki/File%3AA_factory_hall%2C_machinery_and_a_worker_of_Toppila_Oy_1936_%28JOKAKAL3B-3879%29.tif | Finnish Heritage Agency (JOKA archive) | CC BY 4.0 |
| `pylon.jpg` (1200×900, 145 KB) | Dramatic B&W upward shot of a cable-stayed bridge pylon against black sky — **DROPPED per Marshall 2026-11-10; file retained but not referenced by any page** | https://commons.wikimedia.org/wiki/File%3AAda_Bridge_pylon_%28Sava_river%2C_Belgrade%29.jpg | Petar Milošević | CC BY-SA 4.0 |

**Flag — `factory-interior.jpg`:** B&W archival; **kept per Marshall
2026-11-10** — the heritage tone stays.

### corporate-intl/ — Corelia (3)
| file | what it is | source | author | licence |
|---|---|---|---|---|
| `financial-district.jpg` (1200×645, 210 KB) | Cabot Square, Canary Wharf at dusk — real financial district, fountain, towers | https://commons.wikimedia.org/wiki/File%3ACabot_Square%2C_Canary_Wharf_-_June_2008.jpg | Diliff | CC BY-SA 3.0 |
| `modern-architecture.jpg` (829×1023, 168 KB) | Brutalist Australian Embassy, Paris (Seidler/Breuer/Nervi) — hard concrete geometry, blue sky | https://www.flickr.com/photos/94852245@N00/7006799497 | seier+seier | CC BY 2.0 |
| `contactless-pos.jpg` (1200×801, 113 KB) | Hand tapping a blank white card on a POS terminal beside a coffee cup | https://www.pexels.com/photo/close-up-shot-of-a-point-of-sale-machine-11344562/ | Towfiqu barbhuiya | Pexels licence (free to use) |

**Note — `contactless-pos.jpg`:** faint newspaper print on the table,
illegible at display size.

### store/ — آریا استور (2 + 1 hero + 5 category circles, batch 2)
| file | what it is | source | author | licence |
|---|---|---|---|---|
| `shopping-bags-paper.jpg` (1200×800, 83 KB) | Woman in a camel coat holding plain paper shopping bags, no text, no brands | https://www.pexels.com/photo/woman-in-coat-standing-with-paper-bags-in-hands-6567651/ | Tim Douglas | Pexels licence (free to use) |
| `delivery-doorstep.jpg` (1200×800, 131 KB) | Courier handing a plain cardboard parcel to a woman at her doorstep | https://www.pexels.com/photo/man-delivering-a-package-13456097/ | Mizuno K | Pexels licence (free to use) |
| `delivery-hero.jpg` (1200×801, 91 KB) | Courier in a red shirt and cap carrying a long cardboard box out of a white van stacked with parcels — hero slide 3 (fast delivery), clearly distinct from `delivery-doorstep.jpg` | https://www.pexels.com/photo/a-man-in-red-shirt-carrying-a-cardboard-box-beside-the-van-7843960/ | Kampus Production | Pexels licence (free to use) |

### store/categories/ — آریا استور category circles (5, batch 2)
Digikala-style photo circles; all Pexels licence (free to use, no attribution needed), each verified at 168px (2× the 84px circle size) to read clearly as its category.
| file | what it is | source | author | licence |
|---|---|---|---|---|
| `all.jpg` (600×600) | Fully stocked supermarket aisle, jars and shelves — centre-cropped to cut out Hebrew store signage in the original | https://www.pexels.com/photo/fully-stocked-supermarket-interior-5951182/ | Aqsawii | Pexels licence (free to use) |
| `digital.jpg` (1200×800) | Tablet, smartwatch and smartphone flat lay (red/teal) | https://www.pexels.com/photo/tablet-smartphone-and-smartwatch-24738079/ | Imthiyaz Syed | Pexels licence (free to use) |
| `home.jpg` (1200×800) | Woman cooking in a colourful kitchen | https://www.pexels.com/photo/a-woman-cooking-in-the-kitchen-8279649/ | Los Muertos Crew | Pexels licence (free to use) |
| `beauty.jpg` (1200×901) | Two unlabeled serum dropper bottles, Gua Sha stone and olive sprig on black fabric | https://www.pexels.com/photo/white-and-black-unlabeled-serum-bottles-8102135/ | Polina | Pexels licence (free to use) |
| `food.jpg` (1200×1800) | Vibrant market stall: tomatoes, green beans, aubergines, grapes, bananas, carrots — handwritten price numbers only, no brands | https://www.pexels.com/photo/vegetable-and-fruits-displayed-on-market-stall-14650543/ | Feyza Tuğba | Pexels licence (free to use) |

### store-intl/ — Northlight (1)
| file | what it is | source | author | licence |
|---|---|---|---|---|
| `phone-blank-screen.jpg` (1200×1800, 126 KB) | Minimalist hand holding a phone with a blank white screen on grey | https://www.pexels.com/photo/photo-of-person-holding-smartphone-4631067/ | cottonbro studio | Pexels licence (free to use) |

### diet/ — سبزینه (3)
| file | what it is | source | author | licence |
|---|---|---|---|---|
| `ghormeh-sabzi.jpg` (1200×880, 179 KB) | Real vegan ghormeh sabzi with rice and tomato-cucumber salad — authentic Persian food, no text. Strongest Iranian-specific asset in the set | https://commons.wikimedia.org/wiki/File%3AAilin14VeganGhormehSabzi.JPG | AilinParsa | CC0 |
| `salad-bowl-pexels.jpg` (1200×1800, 103 KB) | Top-view mixed-leaf salad bowl on white marble, large negative space | https://www.pexels.com/photo/top-view-of-bowl-with-mix-of-salads-placed-on-table-4198041/ | Kaboompics | Pexels licence (free to use) |
| `vegetable-market.jpg` (1020×900 after crop, 331 KB) | Farmers-market stall piled with oranges, vendor behind | https://commons.wikimedia.org/wiki/File%3AFruit_and_vegetable_stall_at_Southside_Farmers_Market_November_2025.jpg | Nick-D | CC BY-SA 4.0 |

**Note — `vegetable-market.jpg`:** cropped right ~15% at the file level
(1200×900 → 1020×900) to remove the small "$2.00" chalkboard. A small
"marquee" tent logo remains visible top-centre.

### diet-intl/ — Platewise (2)
| file | what it is | source | author | licence |
|---|---|---|---|---|
| `buddha-bowl.jpg` (1200×900, 271 KB) | Vibrant buddha bowl: avocado, tempeh, edamame, radish, rice | https://commons.wikimedia.org/wiki/File%3ABuddhaBowlLot.jpg | PizzaMan | CC BY-SA 4.0 |
| `gym-dumbbells.jpg` (1200×1797, 153 KB) | Close-up of a hand gripping a dumbbell, rack behind | https://commons.wikimedia.org/wiki/File%3AClose-up_Hand_holding_dumbbell_in_gym.jpg | Nenad Stojkovic | CC BY 2.0 |

### map/ — نقشه‌یار (5 — recommend 3 + texture)
| file | what it is | source | author | licence |
|---|---|---|---|---|
| `azadi-tower.jpg` (1200×1806, 309 KB) | Dramatic low-angle Azadi Tower against deep blue sky, one pedestrian for scale. Best single image for this page | https://commons.wikimedia.org/wiki/File%3A2018-09-26_Iran%2C_Tehran%2C_Azadi_Tower_%281%29.jpg | Laurens R. Krol | CC BY 4.0 |
| `milad-tower.jpg` (1200×900, 293 KB) | Night view *from* Milad Tower over Tehran's lights and highways (the tower itself is not in frame) | https://commons.wikimedia.org/wiki/File%3AMilad_tower2023.jpg | Toyota 1999 | CC BY-SA 4.0 |
| `tehran-skyline.jpg` (1200×947, 302 KB) | North Tehran under the snowcapped Alborz. Small Persian billboards visible — fine for RTL | https://commons.wikimedia.org/wiki/File%3ANorth_of_Tehran_Skyline_view.jpg | Ninara (Helsinki) | CC BY-SA 3.0 |
| `golestan-palace.jpg` (1024×683, 222 KB) | Close-up of Golestan Palace tilework — blue/yellow Persian floral tiles | https://www.flickr.com/photos/78722206@N00/5104795061 | Fulvio Spada | CC BY-SA 2.0 |
| `tehran-bazaar.jpg` (850×563, 119 KB) | Tehran bazaar street: tiled mosque, motorbikes, shoppers, stalls. Optional 5th; smallest file | https://commons.wikimedia.org/wiki/File%3A2011_Musavi_street_Tehran_6413045335.jpg | kamshots | CC BY 2.0 |

### map-intl/ — Wayfinder (1)
| file | what it is | source | author | licence |
|---|---|---|---|---|
| `city-skyline.jpg` (1200×568, 159 KB) | Château Frontenac, Quebec City at dusk with a cruise ship — a recognisable destination, not a generic skyline | https://commons.wikimedia.org/wiki/File%3ACh%C3%A2teau_Frontenac_city_at_night.jpg | Wilfredor | CC BY-SA 4.0 |

### index/ (1)
| file | what it is | source | author | licence |
|---|---|---|---|---|
| `workspace-minimal.jpg` (1200×800, 61 KB) | Top-view white desk: laptop, coffee, pencil, sticky notes. **DROPPED per Marshall 2026-11-10 — the index hero is now type-led with no photo; file retained but not referenced by any page** | https://www.pexels.com/photo/macbook-air-beside-white-ceramic-mug-442575/ | JESHOOTS.com | Pexels licence (free to use) |

### resume/ (1)
| file | what it is | source | author | licence |
|---|---|---|---|---|
| `workspace-notebook.jpg` (1200×800, 107 KB) | Wooden desk: laptop, blank notebook, pen, coffee — warm, no text | https://www.pexels.com/photo/workplace-with-laptop-and-notepad-placed-near-coffee-cup-5668471/ | Sora Shimazaki | Pexels licence (free to use) |

### Gaps (said plainly)
- **Wayfinder second image:** no distinctive traveller/city-walk photo found
  to the bar (Commons returned a man reading on a bus; Openverse 504'd).
  One strong hero suffices — do not force a second.
- **Corporate modern hero:** no good modern substation/transformer photo
  found (fenced Japanese substation, hedge-hidden green box rejected).
  Switchgear + archival hall cover the page.
- **Distinctive SVG:** none sourced anywhere. Everything distinctive found
  was photography. A vector set would need to be custom-drawn.
- **Product-photo gaps (Track 2):** both gaps from the 2026-11-10 audit are now closed (batch 2, 2026-11-10) — see the `05` and `09` rows in the table above. The Sony XM5 file came from the Flickr retry URL (the 429 had cleared); no exact Dedica photo exists under a free licence in Commons/Openverse/Pexels (searched 2026-11-10), so id 9 uses the clearly-labelled De'Longhi substitute.

## Licences (verified on the source pages, 2026-11-10)

### unDraw illustrations — free, no attribution required
- **Source:** unDraw (https://undraw.co), downloaded via the `undraw-js`
  npm package v1.0.6 (https://www.npmjs.com/package/undraw-js,
  tarball https://registry.npmjs.org/undraw-js/-/undraw-js-1.0.6.tgz),
  which bundles the unDraw illustration library as SVG files.
- **Author:** Katerina Limpitsouni.
- **Licence:** unDraw licence (https://undraw.co/license, read 2026-11-10):
  "All images, assets and vectors published on unDraw can be used for free.
  You can use them for noncommercial and commercial purposes. You do not
  need to ask permission from or provide credit to the creator or unDraw."
  The licence bars: building a similar/competing illustration service,
  redistributing the assets as standalone packs, and AI/ML training.
  None of those apply here — the SVGs are used as illustrations inside
  sample webpages. Modification (e.g. recolouring the default #6C63FF
  accent to a page's palette) is allowed.
- **Note:** unDraw publishes no public direct-download CDN links; the npm
  package is the published distribution channel for the same files.

### Heroicons — MIT
- **Source:** https://heroicons.com — downloaded from the GitHub repo
  `tailwindlabs/heroicons` (master, `src/24/outline/*.svg`).
- **Author:** Tailwind Labs, Inc.
- **Licence:** MIT (LICENSE file read 2026-11-10 at
  https://raw.githubusercontent.com/tailwindlabs/heroicons/master/LICENSE).
  Copyright notice must be kept in copies — see `NOTICES.md` in this folder
  (to be added at wiring time) or the SOURCES note below.

### Lucide icons — ISC
- **Source:** https://lucide.dev — downloaded from the GitHub repo
  `lucide-icons/lucide` (main, `icons/*.svg`).
- **Author:** Lucide Icons and Contributors.
- **Licence:** ISC (LICENSE file read 2026-11-10 at
  https://raw.githubusercontent.com/lucide-icons/lucide/main/LICENSE).
  Copyright notice must be kept in copies.

## Per-file list — RETIRED SVGs (audit trail only)

The tables below record the 39 SVG files retired 2026-11-10 (see "Retired
2026-11-10" above). They are **not** in `web/assets/graphics/` any more.
For the live assets see "Replacement photos (Track 3)" above and the
product-photo sections further down.

### corporate/ — آریا صنعت توان (industrial distributor)
| file | what it is | source | licence |
|---|---|---|---|
| `factory.svg` | Flat illustration: factory building with chimneys | unDraw, "Factory" (undraw-js 1.0.6) | unDraw (free, no attribution) |
| `circuit-board.svg` | Flat illustration: circuit board / electronics | unDraw, "Circuit board" (undraw-js 1.0.6) | unDraw (free, no attribution) |
| `icon-cog.svg` | Cog / settings outline icon, 24×24 | Heroicons `cog-6-tooth`, https://raw.githubusercontent.com/tailwindlabs/heroicons/master/src/24/outline/cog-6-tooth.svg | MIT |
| `icon-shield-check.svg` | Shield with check outline icon, 24×24 | Heroicons `shield-check`, https://raw.githubusercontent.com/tailwindlabs/heroicons/master/src/24/outline/shield-check.svg | MIT |

### corporate-intl/ — Corelia (fintech)
| file | what it is | source | licence |
|---|---|---|---|
| `finance.svg` | Flat illustration: person with finance charts | unDraw, "Finance" (undraw-js 1.0.6) | unDraw (free, no attribution) |
| `online-payments.svg` | Flat illustration: online card payment | unDraw, "Online payments" (undraw-js 1.0.6) | unDraw (free, no attribution) |
| `icon-banknotes.svg` | Banknotes outline icon, 24×24 | Heroicons `banknotes`, https://raw.githubusercontent.com/tailwindlabs/heroicons/master/src/24/outline/banknotes.svg | MIT |
| `icon-chart-bar.svg` | Bar chart outline icon, 24×24 | Heroicons `chart-bar`, https://raw.githubusercontent.com/tailwindlabs/heroicons/master/src/24/outline/chart-bar.svg | MIT |

### store/ — آریا استور (Iranian online store)
| file | what it is | source | licence |
|---|---|---|---|
| `online-shopping.svg` | Flat illustration: person shopping online | unDraw, "Online shopping" (undraw-js 1.0.6) | unDraw (free, no attribution) |
| `add-to-cart.svg` | Flat illustration: adding a product to cart | unDraw, "Add to cart" (undraw-js 1.0.6) | unDraw (free, no attribution) |
| `delivery-truck.svg` | Flat illustration: delivery truck | unDraw, "Delivery truck" (undraw-js 1.0.6) | unDraw (free, no attribution) |
| `empty-cart.svg` | Flat illustration: empty shopping cart | unDraw, "Empty cart" (undraw-js 1.0.6) | unDraw (free, no attribution) |
| `icon-shopping-bag.svg` | Shopping bag outline icon, 24×24 | Heroicons `shopping-bag`, https://raw.githubusercontent.com/tailwindlabs/heroicons/master/src/24/outline/shopping-bag.svg | MIT |
| `icon-truck.svg` | Delivery truck outline icon, 24×24 | Heroicons `truck`, https://raw.githubusercontent.com/tailwindlabs/heroicons/master/src/24/outline/truck.svg | MIT |

### store-intl/ — Northlight (minimal English store)
| file | what it is | source | licence |
|---|---|---|---|
| `mobile-devices.svg` | Flat illustration: phones / devices | unDraw, "Mobile devices" (undraw-js 1.0.6) | unDraw (free, no attribution) |
| `shopping-app.svg` | Flat illustration: shopping on a phone app | unDraw, "Shopping app" (undraw-js 1.0.6) | unDraw (free, no attribution) |
| `icon-phone.svg` | Phone outline icon, 24×24 | Heroicons `device-phone-mobile`, https://raw.githubusercontent.com/tailwindlabs/heroicons/master/src/24/outline/device-phone-mobile.svg | MIT |
| `icon-tag.svg` | Price tag outline icon, 24×24 | Heroicons `tag`, https://raw.githubusercontent.com/tailwindlabs/heroicons/master/src/24/outline/tag.svg | MIT |

### diet/ — سبزینه (Persian diet calculator)
| file | what it is | source | licence |
|---|---|---|---|
| `healthy-options.svg` | Flat illustration: healthy food choices | unDraw, "Healthy options" (undraw-js 1.0.6) | unDraw (free, no attribution) |
| `cooking.svg` | Flat illustration: person cooking | unDraw, "Cooking" (undraw-js 1.0.6) | unDraw (free, no attribution) |
| `icon-leaf.svg` | Leaf outline icon, 24×24 | Lucide `leaf`, https://raw.githubusercontent.com/lucide-icons/lucide/main/icons/leaf.svg | ISC |
| `icon-apple.svg` | Apple outline icon, 24×24 | Lucide `apple`, https://raw.githubusercontent.com/lucide-icons/lucide/main/icons/apple.svg | ISC |

### diet-intl/ — Platewise (English calorie app)
| file | what it is | source | licence |
|---|---|---|---|
| `healthy-habit.svg` | Flat illustration: healthy daily habit | unDraw, "Healthy habit" (undraw-js 1.0.6) | unDraw (free, no attribution) |
| `workout.svg` | Flat illustration: person working out | unDraw, "Workout" (undraw-js 1.0.6) | unDraw (free, no attribution) |
| `icon-dumbbell.svg` | Dumbbell outline icon, 24×24 | Lucide `dumbbell`, https://raw.githubusercontent.com/lucide-icons/lucide/main/icons/dumbbell.svg | ISC |
| `icon-flame.svg` | Flame outline icon, 24×24 | Lucide `flame`, https://raw.githubusercontent.com/lucide-icons/lucide/main/icons/flame.svg | ISC |

### map/ — نقشه‌یار (Tehran places map)
| file | what it is | source | licence |
|---|---|---|---|
| `map.svg` | Flat illustration: map with pins | unDraw, "Map" (undraw-js 1.0.6) | unDraw (free, no attribution) |
| `current-location.svg` | Flat illustration: current location / GPS | unDraw, "Current location" (undraw-js 1.0.6) | unDraw (free, no attribution) |
| `location-search.svg` | Flat illustration: searching a location | unDraw, "Location search" (undraw-js 1.0.6) | unDraw (free, no attribution) |
| `icon-map-pin.svg` | Map pin outline icon, 24×24 | Heroicons `map-pin`, https://raw.githubusercontent.com/tailwindlabs/heroicons/master/src/24/outline/map-pin.svg | MIT |
| `icon-landmark.svg` | Landmark / classical building outline icon, 24×24 | Lucide `landmark`, https://raw.githubusercontent.com/lucide-icons/lucide/main/icons/landmark.svg | ISC |

### map-intl/ — Wayfinder (English places map)
| file | what it is | source | licence |
|---|---|---|---|
| `adventure-map.svg` | Flat illustration: adventure / travel map | unDraw, "Adventure map" (undraw-js 1.0.6) | unDraw (free, no attribution) |
| `destination.svg` | Flat illustration: arriving at a destination | unDraw, "Destination" (undraw-js 1.0.6) | unDraw (free, no attribution) |
| `icon-navigation.svg` | Navigation arrow outline icon, 24×24 | Lucide `navigation`, https://raw.githubusercontent.com/lucide-icons/lucide/main/icons/navigation.svg | ISC |
| `icon-globe.svg` | Globe outline icon, 24×24 | Heroicons `globe-alt`, https://raw.githubusercontent.com/tailwindlabs/heroicons/master/src/24/outline/globe-alt.svg | MIT |

### index/ — portfolio index
| file | what it is | source | licence |
|---|---|---|---|
| `portfolio-website.svg` | Flat illustration: portfolio website | unDraw, "Portfolio website" (undraw-js 1.0.6) | unDraw (free, no attribution) |
| `icon-briefcase.svg` | Briefcase outline icon, 24×24 | Heroicons `briefcase`, https://raw.githubusercontent.com/tailwindlabs/heroicons/master/src/24/outline/briefcase.svg | MIT |

### resume/ — resume page
| file | what it is | source | licence |
|---|---|---|---|
| `online-resume.svg` | Flat illustration: online CV / resume | unDraw, "Online resume" (undraw-js 1.0.6) | unDraw (free, no attribution) |
| `icon-academic-cap.svg` | Graduation cap outline icon, 24×24 | Heroicons `academic-cap`, https://raw.githubusercontent.com/tailwindlabs/heroicons/master/src/24/outline/academic-cap.svg | MIT |

## Product photos (Track 2, 2026-11-10)

Real product photos for the two store pages. Every photo was visually
checked (the actual product in frame, not a box, not a lookalike). All
are JPEG, resized to max 1200px at quality 85 (progressive). Licence
notes:
- **CC0** (public domain dedication) — free, no conditions.
- **CC BY / CC BY-SA** — free for commercial use with attribution; the
  attribution below satisfies it. CC BY-SA files may be cropped/resized;
  the one crop made here (Galaxy Watch 7, store id 6) is noted.
- **Pexels licence** — free to use, no attribution required.
- No BY-ND files were used (the only free Sony XM5 copies are BY-ND and
  could not be downloaded — see gaps).

### store/products/ — آریا استور (filenames carry the page's product id)
| file | product (page id) | what the photo actually shows | source | licence |
|---|---|---|---|---|
| `01-galaxy-a55-5g.jpg` | 1 · Samsung Galaxy A55 5G | Exact model, on a store display stand | Wikimedia Commons, "Samsung Galaxy A55 5G 2024.jpg", Captainmorlypogi1959 — https://commons.wikimedia.org/wiki/File:Samsung_Galaxy_A55_5G_2024.jpg | CC BY-SA 4.0 |
| `02-redmi-note-13-pro-5g.jpg` | 2 · Xiaomi Redmi Note 13 Pro 5G | **Substitute:** Redmi Note 14 Pro+ 5G (successor, same line) on a store display; no free photo of the 13 Pro exists on Commons/Openverse | Wikimedia Commons, "Redmi Note 14 ProPlus.jpg", Maksdroider — https://commons.wikimedia.org/wiki/File:Redmi_Note_14_ProPlus.jpg | CC BY-SA 4.0 |
| `03-iphone-16.jpg` | 3 · Apple iPhone 16 | Exact model (Ultramarine), held in hand showing the About screen — the serial number is legible only at full size, not at card size | Wikimedia Commons, "About iPhone 16 Ultramarine.jpg" — https://commons.wikimedia.org/wiki/File:About_iPhone_16_Ultramarine.jpg | CC BY-SA 4.0 |
| `04-asus-vivobook-15.jpg` | 4 · Asus Vivobook 15 | Exact model, on a desk (screen off, home-desk background) | Wikimedia Commons, "Asus Vivobook 15.jpg", LeopardWin — https://commons.wikimedia.org/wiki/File:Asus_Vivobook_15.jpg | CC0 |
| `05-sony-wh-1000xm5.jpg` | 5 · Sony WH-1000XM5 | Exact model (silver/white), on a wooden table, NC/AMB button visible | Flickr, TheBetterDay — https://live.staticflickr.com/65535/52435973857_a66d368130_b.jpg | CC BY-ND 4.0 — **file used unmodified (exact bytes, no resize/crop/re-encode)**; displayed with the standard card treatment. Credit in the page footer. |
| `06-samsung-galaxy-watch-7.jpg` | 6 · Samsung Galaxy Watch 7 | Exact model, 40mm Cream — **cropped** to the left watch from a two-watch store-display shot (crop removes the Japanese price placards; CC BY-SA allows derivatives) | Wikimedia Commons, "Galaxy Watch 7.jpg", Kyu3a — https://commons.wikimedia.org/wiki/File:Galaxy_Watch_7.jpg | CC BY-SA 4.0 |
| `07-xiaomi-s10-robot-vacuum.jpg` | 7 · Xiaomi S10 robot vacuum | **Substitute:** Xiaomi Mi Robot Vacuum (same brand, same category; no free photo of the exact S10) — white round vacuum with lidar turret at its dock | Wikimedia Commons, "XiaomiMiRobotVacuumCleanerRobot.jpg", Raysonho — https://commons.wikimedia.org/wiki/File:XiaomiMiRobotVacuumCleanerRobot.jpg | CC0 |
| `08-philips-hd9200-air-fryer.jpg` | 8 · Philips HD9200 air fryer | Philips air fryer of the HD9200 generation (white body, purple dial, PHILIPS branding); exact-model match not confirmed from the photo alone | Wikimedia Commons, "Airfryer Convert.jpg", Maurina Rara — https://commons.wikimedia.org/wiki/File:Airfryer_Convert.jpg | CC BY 2.0 |
| `09-delonghi-dedica-ec685.jpg` | 9 · De'Longhi Dedica EC685 | **Substitute:** a real De'Longhi home pump espresso machine with portafilter and steam wand (Caffè Treviso model, 2009 photo, "DeLonghi / CAFFÈ TREVISO" on the fascia) — same brand, same machine type; **not the Dedica EC685**. No exact Dedica photo exists under a free licence (Commons `intitle:Dedica`/`intitle:EC685` and Pexels searched 2026-11-10; Openverse 504'd). Tightly cropped to the machine (BY-SA allows derivatives). Credit in the page footer. | Wikimedia Commons, "Espresso machine (4196276883) (2).jpg", Sander van der Wel — https://commons.wikimedia.org/wiki/File:Espresso_machine_(4196276883)_(2).jpg | CC BY-SA 2.0 |
| `10-braun-series-7.jpg` | 10 · Braun Series 7 | Exact model (799c-7), studio shot on white | Wikimedia Commons, "Braun Series 7 799c-7 electric shaver.jpg", Florian Fuchs — https://commons.wikimedia.org/wiki/File:Braun_Series_7_799c-7_electric_shaver.jpg | CC BY 3.0 |
| `11-oralb-pro-3-3000.jpg` | 11 · Oral-B Pro 3 3000 | Exact model, with charging base, on grey | Wikimedia Commons, "2024 Szczoteczka do zębów Oral-B Pro 3 3000 (2).jpg", Jacek Halicki — https://commons.wikimedia.org/wiki/File:2024_Szczoteczka_do_z%C4%99b%C3%B3w_Oral-B_Pro_3_3000_(2).jpg | CC BY-SA 4.0 |
| `12-lavazza-qualita-rossa.jpg` | 12 · Lavazza Qualità Rossa | **Substitute:** roasted coffee beans in an open silver bag (no free photo of the Lavazza bag itself; the only exact-product shots are dubious CC0 Amazon listings — not used) | Pexels, "Brown Coffee Beans in Silver Package", Justus Menke — https://www.pexels.com/photo/brown-coffee-beans-in-silver-package-5214207/ | Pexels (free to use) |
| `13-saharkhiz-saffron.jpg` | 13 · Saharkhiz saffron (sargol) | Loose red saffron threads (sargol grade look) with a spoon — representative photo, not the Saharkhiz pack | Wikimedia Commons, "Saffron Red Thread ( World's Most Expensive Speices).jpg", Umarsami — https://commons.wikimedia.org/wiki/File:Saffron_Red_Thread_(_World%27s_Most_Expensive_Speices).jpg | CC BY-SA 4.0 |

**Gaps in store/products/ — both closed in batch 2 (2026-11-10):**
- **id 5 · Sony WH-1000XM5 — CLOSED.** The Flickr retry URL worked (429 cleared): https://live.staticflickr.com/65535/52435973857_a66d368130_b.jpg — CC BY-ND 4.0 by TheBetterDay; file used unmodified, see the `05` row above.
- **id 9 · De'Longhi Dedica EC685 — CLOSED with a labelled substitute.** No exact Dedica photo exists under a free licence (Commons + Pexels searched; Openverse 504'd). The file used is a real De'Longhi pump machine (Caffè Treviso) — same brand, same machine type — see the `09` row above. The Flickr "delonghi en90f" (a Nespresso capsule machine, different machine type) was **not** used; two Pexels espresso-machine photos were checked and rejected (Bezzera and Nespresso, both with legible wrong branding).

### store-intl/products/ — Northlight
| file | product | what the photo actually shows | source | licence |
|---|---|---|---|---|
| `iphone-18-pro.jpg` | iPhone 18 Pro | Exact model: Silver iPhone 18 Pro, back + side profile (also the hero) | Apple official product image, via ayshei.com listing "apple-iphone-18-pro-silver-hk-version-1-sim-esim-256gb" | Apple Inc. — demo use only, non-commercial |
| `iphone-18-pro-max.jpg` | iPhone 18 Pro Max (compare) | Exact model: Burgundy iPhone 18 Pro Max, back view on white | Wikimedia Commons, "IPhone 18 Pro Max rear.jpg", Chino Futaba (茅野ふたば) — https://commons.wikimedia.org/wiki/File:IPhone_18_Pro_Max_rear.jpg | CC BY-SA 4.0 |
| `macbook-air-m5.jpg` | MacBook Air 13-inch (M5) | **Substitute:** MacBook Air 13-inch (M4, Silver) — the M5 does not exist yet | Wikimedia Commons, "MacBook Air (13-inch, M4, Silver).jpg", AzureSaturn — https://commons.wikimedia.org/wiki/File:MacBook_Air_(13-inch,_M4,_Silver).jpg | CC0 |
| `ipad-air-m3.jpg` | iPad Air 11-inch (M3) | Exact model, back view (the front About-screen shot was rejected: visible serial number / MAC addresses) | Wikimedia Commons, "IPad Air 11-inch (M3) backside.jpg" — https://commons.wikimedia.org/wiki/File:IPad_Air_11-inch_(M3)_backside.jpg | CC BY-SA 4.0 |
| `apple-watch-series-11.jpg` | Apple Watch Series 11 | **Substitute:** Apple Watch Series 10 (two watches, white + black bands) — one generation back, near-identical design | Wikimedia Commons, "Apple Watch Series 10.JPG", KK IN HK — https://commons.wikimedia.org/wiki/File:Apple_Watch_Series_10.JPG | Public domain |
| `airpods-pro-3.jpg` | AirPods Pro 3 | Exact model, earbuds + closed case on white (the pairing-screen shot was rejected: an email address printed on the case) | Wikimedia Commons, "AirPods Pro 3 with case.jpg", Auggie G — https://commons.wikimedia.org/wiki/File:AirPods_Pro_3_with_case.jpg | CC BY 3.0 |
| `homepod-mini.jpg` | HomePod mini | Exact model (orange), on a wooden table | Wikimedia Commons, "HomePod mini (Orange).jpg", AzureSaturn — https://commons.wikimedia.org/wiki/File:HomePod_mini_(Orange).jpg | CC0 |

### store-intl/finishes/ — Northlight configurator finishes
| file | finish | what the photo actually shows | source | licence |
|---|---|---|---|---|
| `finish-black.jpg` (900×1350, 125 KB) | Black | Exact model: Black iPhone 18 Pro, back view, studio render on a plain off-white background | Apple official product image, via ayshei.com listing "Apple iPhone 18 Pro Black 256 GB \| International Version \| eSim Only" | Apple Inc. — demo use only, non-commercial |
| `finish-silver.jpg` (900×1350, 83 KB) | Silver | Exact model: Silver iPhone 18 Pro, back + side profile (same Apple image as the hero/product photo, different crop) | Apple official product image, via ayshei.com (see `iphone-18-pro.jpg` above) | Apple Inc. — demo use only, non-commercial |
| `finish-glacier.jpg` (900×1350, 160 KB) | Glacier | Exact model: Glacier iPhone 18 Pro, back view — isolated from Apple's back+front hero, the front phone cropped out | Apple official product image, via PB Tech listing "Apple-iPhone-18-Pro-512GB-Glacier" | Apple Inc. — demo use only, non-commercial |
| `finish-burgundy.jpg` (900×1350, 171 KB) | Burgundy | Exact model: Burgundy iPhone 18 Pro, camera close-up on a black background — a detail shot, not a full back view; no full back view of a Burgundy 18 Pro was available at usable resolution | Apple official product image, via jabko.ua listing "apple-iphone-18-pro-256gb-burgundy" | Apple Inc. — demo use only, non-commercial |

**Attribution for the CC BY-SA photos:** the store page footer credits Chino Futaba (Burgundy Pro Max); the Apple official images are credited in the footer as Apple's product images.

**Attribution for the CC BY / CC BY-SA photos:** when the pages are
wired, add a small photo-credits line (footer or an "Image credits"
note) naming the photographers above; the CC0 and Pexels photos need no
credit. The store page's products have numeric ids 1–13 and no image
field yet — the filenames above carry the id, so wiring is
`products/<id>-<slug>.jpg` per product.

## Attribution notes for wiring time
- unDraw: no attribution required (but a credit line is welcome).
- Heroicons (MIT) and Lucide (ISC): keep the copyright notice in copies —
  add a short notice in the site footer or in a `NOTICES.md` next to the
  assets when the graphics are wired in: "Icons: Heroicons (MIT, © Tailwind
  Labs) and Lucide (ISC, © Lucide Contributors)."
