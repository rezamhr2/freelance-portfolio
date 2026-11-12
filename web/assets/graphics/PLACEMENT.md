# Placement plan — graphics for the sample webpages

**Status 2026-11-10 (batch B):** the 39 generic SVGs (21 unDraw illustrations + 18
Heroicons/Lucide icons) were **retired** under Marshall's maximum-effort
taste filter — see SOURCES.md, "Retired 2026-11-10". The live asset set is
real photography only: **22 new photos + 18 store product photos**
(40 JPGs, ~6.3 MB). **Everything is wired into the HTML/CSS** — every photo
listed below is placed on its page (heroes, section anchors, category circles,
product cards, configurator), verified by the batch-B Playwright run
(19 pages + 2 stores, 390/768/1280, zero broken images) and the final
verification in `~/workspace/goals/freelance-resume-and-portfolio-samples/hidden_files/overnight/after/`.

## General notes (apply everywhere)

- **Real photos, not clip-art.** Every placement below follows the research
  in DESIGN-DIRECTION.md: Stripe/Linear "real product UI/photo as hero",
  Apple "real product photography only, full-bleed", Notion warm neutrals +
  one highlighted element, Balad need-based sections, Aparat intent-named
  rails, Vercel proof-first.
- **No icons any more.** Chips and headers carry themselves typographically
  (Vercel/Notion discipline: type + hairlines, not glyphs). Do NOT swap in
  another generic icon set — that repeats the mistake.
- **Empty-cart is a typographic/CSS state**, not an illustration
  (Digikala-style honest empty state: "سبد خرید شما خالی است" + a button).
- **Photos carry no baked-in text**, so Persian RTL pages stay clean.
  Two exceptions, both flagged in SOURCES.md: `contactless-pos.jpg`
  (newspaper print, illegible at card size) and `vegetable-market.jpg`
  (already cropped right ~15% to remove the "$2.00" chalkboard; a small
  "marquee" tent logo remains top-centre).
- **Hero photos: one per page, large-format.** Secondary photos are section
  anchors, never stretched full-bleed at small sizes; keep aspect ratio.

## corporate/ — آریا صنعت توان (Persian, industrial distributor)

1. `switchgear.jpg` — **hero**, beside "تجهیزات برق صنعتی را سریع‌تر،
   شفاف‌تر و با…". Real switchgear cabinet row with gauges and breakers —
   the distributor's actual world. Stripe/Linear "real product as hero" +
   Vercel proof-first. The photo's own blue-grey tones set the page accent.
2. `factory-interior.jpg` — **"داستان ما" / about section**. 1936 B&W
   factory hall, worker at a control panel beside heavy machinery.
   Bulgari "craft quantified" pattern: the past as proof of longevity.
   Keep the B&W treatment (do not colourise). **Kept per Marshall
   2026-11-10** — the heritage tone stays.
3. `pylon.jpg` — **DROPPED per Marshall 2026-11-10.** Was the abstract
   divider / "چشم‌انداز ما" section background (dramatic B&W Ada Bridge
   pylon against a black sky). The `.dark-band` section is now a flat dark
   navy band with no photo. The file is retained in
   `corporate/pylon.jpg` but is not referenced by any page.

## corporate-intl/ — Corelia (English, fintech)

1. `financial-district.jpg` — **hero**, beside "Financial infrastructure"
   and the live settlement preview. Cabot Square, Canary Wharf at dusk —
   where the money actually lives. Stripe "trust as hard numbers" pattern:
   the photo earns the "Proof before pitch" section below it.
2. `modern-architecture.jpg` — **"Built for every stage" / "In their own
   words" band**. Brutalist Australian Embassy, Paris — hard concrete
   geometry, blue sky. Linear "one surface, rest flat": a single
   architectural photo as the page's only image beyond the hero.
3. `contactless-pos.jpg` — **fee calculator / "Transparent pricing"
   section**. Hand tapping a blank card on a POS terminal beside coffee =
   money changing hands in real life. Vercel proof-first: show the
   transaction, don't describe it. Note: faint newspaper print under the
   terminal is illegible at card size.

## store/ — آریا استور (Persian, online store)

1. `shopping-bags-paper.jpg` — **hero**, beside "جشنوارهٔ بزرگ تخفیف
   آریا استور". Woman in a camel coat holding plain paper shopping bags —
   no text, no brands. The festival banner's subject; Snappfood
   "discount rail" energy without a stock-photo handshake.
2. `delivery-doorstep.jpg` — **"ارسال سریع به سراسر کشور"** (shipping
   section). Real doorstep parcel handoff. Torob "trust as a mechanism"
   pattern: show the delivery happening instead of promising it in text.
3. **Empty cart: typographic/CSS state** (no photo) — see General notes.

### Product photos — store/products/ (one per product, filename = `<id>-<slug>.jpg`)

- Product cards use the photo as the card image; the hero keeps
  `shopping-bags-paper.jpg`. Where a photo is a substitute (ids 2, 7, 12,
  13) the card still shows the real product category — no fake "exact"
  claim is made in the UI; the substitution is recorded in SOURCES.md.
- `06-samsung-galaxy-watch-7.jpg` is a tight crop of one watch — it works
  as a card image as-is; do not re-crop.
- Both product photos are **present since batch 2 (2026-11-10)** — the
  "missing" note below is stale and superseded. Id 5 Sony XM5 is the real
  photo (`05-sony-wh-1000xm5.jpg`, exact model, used unmodified); id 9
  De'Longhi Dedica is a labelled substitute (`09-delonghi-dedica-ec685.jpg`,
  a real De'Longhi Caffè Treviso pump machine — same brand, same machine
  type, not the Dedica EC685; see SOURCES.md).

## store-intl/ — Northlight (English, minimal store)

1. `phone-blank-screen.jpg` — **hero / configurator side art**, beside
   "Buy iPhone 18 Pro". Minimalist hand holding a phone with a blank
   white screen on grey. Apple pattern: real product photography only,
   one product per tile, near-zero density. The blank screen is the
   point: the configurator is the content.

### Product photos — store-intl/products/

- Product cards + configurator: `iphone-18-pro.jpg` is the hero/configurator
  image for the iPhone 18 Pro; `iphone-18-pro-max.jpg` for the Pro Max
  option in the configurator. The other five photos are the product-grid
  card images.
- The iPhone 18 Pro/Max and MacBook Air M5 photos are the previous
  generation (17 Pro/Max, M4) — the page's copy already treats these as
  future products, so the photos read as the closest real thing; note the
  substitution in SOURCES.md, don't claim them as 18-series shots.
- `ipad-air-m3.jpg` shows the back of the iPad (clean, no serial) — fine
  for a card; the front view is not used.

## diet/ — سبزینه (Persian, diet calculator)

1. `salad-bowl-pexels.jpg` — **hero**, next to "محاسبه‌گر کالری و شاخص
   تودهٔ بدنی". Top-view mixed-leaf salad bowl on white marble with large
   negative space. Notion warm neutrals + one highlighted element: the
   negative space is where the calculator sits.
2. `ghormeh-sabzi.jpg` — **"نمونه برنامه یک روز" / "دستورهای غذایی"**
   section. Real vegan ghormeh sabzi with rice and tomato-cucumber
   salad. Aparat intent-named rails: this is the dish the audience
   actually eats, not a stock "healthy bowl". Strongest Iranian-specific
   asset in the set.
3. `vegetable-market.jpg` — **"سبزینه را بشناسید" / about section**
   (optional third). Farmers-market stall piled with oranges. Balad
   need-based sections: food as a place, not a concept. Already cropped
   right ~15% (chalkboard removed); small "marquee" tent logo remains
   top-centre.

## diet-intl/ — Platewise (English, calorie app)

1. `buddha-bowl.jpg` — **hero**, beside "Know what you eat." Vibrant
   buddha bowl (avocado, tempeh, edamame, radish, rice). Apple
   one-product-per-tile: the bowl IS the hero.
2. `gym-dumbbells.jpg` — **"Everything you need, in your pocket"** /
   activity feature rows. Close-up of a hand gripping a dumbbell, rack
   behind. Exercise is half the app's story. Raycast "one accent used
   once per page" discipline: one human moment, not a gym montage.

## map/ — نقشه‌یار (Persian, Tehran places map)

1. `azadi-tower.jpg` — **hero**, above the map and filters. Dramatic
   low-angle Azadi Tower against deep blue sky, one pedestrian for
   scale. Balad "city guide by human need" + Linear "product screenshot
   IS the hero": the landmark is the page's identity, not decoration.
   Best single image for this page.
2. `milad-tower.jpg` — **"دیدنی" / places-to-see rail**. Night view
   *from* Milad Tower over Tehran's lights and highways — the city at
   night as the reward for exploring. (The tower itself is not in frame.)
3. `tehran-skyline.jpg` — **"نتایج" / results panel header** (optional).
   North Tehran under the snowcapped Alborz — the city the map covers,
   in one frame. Small Persian billboards visible — fine for RTL.
4. `golestan-palace.jpg` — **historical/cultural places chip or detail
   panel texture**. Close-up of Golestan Palace tilework (blue/yellow
   Persian floral tiles). Bulgari macro-detail pattern: craft in
   close-up. Replaces the old landmark icon's job with something real.
5. `tehran-bazaar.jpg` — **optional 5th**, "خوردنی" / market rail.
   Tehran bazaar street: tiled mosque, motorbikes, shoppers, stalls.
   Smallest file; use only if the rail needs a fifth image.

## map-intl/ — Wayfinder (English, places map)

1. `city-skyline.jpg` — **hero**, above the map. Château Frontenac,
   Quebec City at dusk with a cruise ship — a recognisable destination,
   not a generic skyline. Arc "Spaces" pattern: one place, one mood, one
   flooded image. The hero is a destination, not a map pin.
2. **No second image.** A distinctive traveller/city-walk photo was
   hunted and not found to the bar (see SOURCES.md gaps). One strong
   hero suffices — do not force a second.

## index/ — portfolio index

1. `workspace-minimal.jpg` — **DROPPED per Marshall 2026-11-10.** Was the
   cover beside "نمونه‌کارها — رضا محمدرضایی" (top-view white desk: laptop,
   coffee, pencil, sticky notes). The index hero is now type-led with no
   photo. The file is retained in `index/workspace-minimal.jpg` but is
   not referenced by any page.

## resume/ — resume page

1. `workspace-notebook.jpg` — **header**, beside the name / "درباره من".
   Wooden desk: laptop, blank notebook, pen, coffee — warm, no text.
   The work, not a portrait. Notion warm neutrals.

## What was deliberately skipped / dropped

- **All 39 SVGs retired 2026-11-10** (see SOURCES.md "Retired
  2026-11-10"). No replacement icon set: swapping Heroicons for another
  generic stroke set would repeat the mistake.
- **Decorative background patterns** (e.g. Hero Patterns): not sourced;
  the photography carries the pages. Revisit only if Marshall wants
  textured backgrounds.
- **Wayfinder second image**: not found to the bar — one strong hero
  suffices.
- **Corporate modern hero**: not found to the bar (fenced Japanese
  substation, hedge-hidden green box rejected) — switchgear + archival
  hall cover the page.
- **Distinctive SVG**: none sourced anywhere. Everything distinctive
  found was photography. A vector set would need to be custom-drawn.
