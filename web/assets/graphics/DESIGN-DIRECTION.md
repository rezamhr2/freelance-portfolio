# Design direction — freelance portfolio sample webpages

**Status 2026-11-10:** direction only — no HTML/CSS edited. Nothing in this
document is wired into the pages until Marshall reviews it.

**Why this document exists:** Marshall's verdict on the sample pages was
that they look too generic — they don't showcase intuition or creativity,
Iranian or international — and that cool websites use animations and
transitions, which he didn't see anywhere in our work. The price-monitor
report is "pretty much a white page with writing", and the code reports and
sheets previews need the same treatment as the web pages.

**What changed first:** the 39 generic SVGs (21 unDraw illustrations + 18
Heroicons/Lucide icons) were retired under the taste filter below and
replaced by 22 real photographs (see SOURCES.md "Replacement photos
(Track 3)" and PLACEMENT.md). The 18 store product photos survive — real
photos already pass the bar. This document is the direction for wiring
those assets in, plus the design and motion changes each page needs.

## Research base (studied live, 2026-11-10)

Full research reports: `/tmp/iranian-research.md` (33 KB),
`/tmp/international-research.md` (44 KB), `/tmp/motion-research.md`
(60 KB, 30+ cited sources), `/tmp/report-direction.md` (35 KB, the four
report/sheets sections merged below as §§R0–R4), `/tmp/asset-audit.md`
(19 KB, the SVG audit + replacement hunt).

### Iranian exemplars — what they actually do

- **Digikala** (homepage unfetchable from the sandbox; studied via the
  noxfolio analysis, DeepWiki and the DigikalaJet case study): full-width
  promo carousels → 4 promo cards → category tiles → named horizontal
  product rails. Product card = image + truncated title + seller/stock +
  bold price + struck old price + red % pill. One flat red accent. Every
  rail has skeleton-loading + retry states.
- **Snapp** (snapp.ir): one-sentence hero + enumerating sub-line, no
  screenshot. Super-app grid of ~25 named tiles ending «+10، مشاهده همه».
  Flat green accent. Driver-recruitment benefit cards with checkable
  claims + «register in under 10 minutes».
- **Snappfood**: two-level category chips first (verticals with «کالابرگ»
  tags, then cuisine chips). Restaurant card = name (neighbourhood) /
  status / ★rating (abbreviated count) / from-price / discount %.
  Closed/pre-order status shown on the card, never hidden. «تخفیف شکار کن»
  discount rail with live countdown + capped amount (تا 500 هزار تومان).
- **Torob** (product page fetched): prices always «از X تومان»; seller
  count as trust («در ۵۹ فروشگاه»); variant matrix with per-variant
  «ناموجود» + honest empty state «این محصول فعلا فروشنده‌ای ندارد» +
  similar products; price-history + last-change date («۶ روز پیش») +
  instalment line + shop trust (years, recent orders).
- **Balad** (fully fetched): map page as a city guide by human need —
  خوردنی / موندنی / دیدنی, ranked top-20 lists + «مشاهده موارد بیشتر»;
  place rows = name + type + rating + reviewer count, no-data state
  written out («نظر و امتیازی وجود ندارد»); Iran-specific intelligence as
  copy (traffic/pollution zones red/blue, speed-camera alerts, house
  numbers, Persian voice assistant with regional accents); ~30-city
  switcher + plain-language about section.
- **Cafe Bazaar**: stack of trust/feature blocks, one illustration + one
  bold claim + one sentence each; trust as a named mechanism («بازار امن
  با آنتی‌ویروس», «میزبان نسخه رسمی همراه بانک‌ها»); 20-category taxonomy
  + «انتخاب بازار» editorial badge; app cards = icon + name + category +
  one trust metric.
- **Aparat** (fully fetched): NO hero — opens straight into content rails
  (منتخب پخش زنده، ویژه‌های آپارات، آپارات موزیک، پیشنهاد آپارات،
  جذاب‌ترین‌ها، داغ‌ترین‌ها); video card = duration badge + title +
  channel + abbreviated views + relative age; rails named by intent;
  fixed 18-category set.
- **Divar** (ad page fetched; homepage unfetchable): ad page = spec table
  first, then yes/no facts, tiered price table, description last;
  «زنگ خطرهای قبل از معامله» safety banner inline near the top; listing
  card = thumbnail + title + price + one spec line + district + relative
  age + paid-promotion tags; 236-node category tree with
  category-specific filters.
- **Cross-site patterns:** Persian digits + thousand separators on all
  prices, «از» for from-prices, «تومان» always attached; one flat accent
  per brand for price/discount/CTA/active only; rating always "number
  (abbreviated count)", no-data written out; status lives on the card;
  discovery via named horizontal rails, grids only for search results;
  trust stated as a mechanism in one line; every section has
  loading/error/empty states. (Colour hex, typography scale, spacing and
  micro-interactions could NOT be verified from text fetches.)

### International exemplars — what they actually do

- **Stripe** (stripe.com): one expressive surface (animated WebGL gradient
  mesh, blue→pink→orange, −12° skew) only in the upper-third hero, rest
  white + navy ink `#0a2540`, pale-grey sections, diagonal `skewY(-6deg)`
  seams; light display type Söhne weight 300, hero 56–64px, lh 1.03–1.07,
  tracking −0.02em; trust as hard numbers (135+ currencies · $1.9T in
  2025 · 99.999% uptime · 200M+ subscriptions) + per-case "Products used"
  lines + named testimonials; "Choose an integration path" 3-door band.
- **Linear** (linear.app): product screenshot IS the hero, 64px Inter
  Variable weight 510, bg `#08090a`, full-width real product UI; hairlines
  + grey ladder `#08090a → #0f1011 → #161718`, borders 6–10% white, 1px
  glowing border + radial glow; keyboard-first (⌘K palette, inline
  shortcuts, muted status pills, ENG-2076 IDs); three numbered claims
  "Fig 0.1/0.2/0.3".
- **Apple** (apple.com): one product per tile, one viewport per tile, name
  40px/600 + one-line tagline + two tiny blue pill CTAs (`#0066cc`),
  alternating light/dark tiles, near-zero density; type scale 56/40/28/17,
  tracking −0.28px hero, spacing 4/8/12/17/24/32/48/80; progressive
  disclosure tease → scroll story → specs → configurator (Finish→Storage
  →Accessories, live price, sticky sub-nav with Buy + price); real product
  photography only, full-bleed, 1x/2x/3x.
- **Vercel** (vercel.com): disciplined monochrome `#fafafa` / `#171717`,
  hairlines, colour only in prismatic glow behind the single black ▲
  triangle reused as logo/prompt/bullet; Geist weight 450, −0.06em
  tracking; mono uppercase micro-eyebrows 11–13px, 0.071em; proof-first
  sections (named customer + scale number, then 4 features); terminal/code
  as hero imagery; 48px pill CTAs.
- **Arc** (arc.net — SUNSETTING 22 Dec 2026, live page is only a
  farewell/migration notice; historic patterns only): 240px sidebar-first
  "Spaces" each with own 2-colour gradient, 13px tab titles; serif
  marketing (Marlin/Argent CF) + sans-only product; scalloped cream
  section dividers + one flooded violet (`#3139fb`) band; theme-colour
  gradients as mood per space.
- **Raycast** (raycast.com — fetch returned only YouTube titles; patterns
  from published breakdowns): command palette scaled up as hero;
  near-black ladder `#07080a→#0d0d0d→#101111→#121212`, hairlines `#242728`,
  one white CTA pill, red diagonal stripe (`#FF6363`) used once per page
  max; physical keycaps (gradient `#121212→#0d0d0d`, 4px radius, layered
  shadow, Inter ss03 `g`); honest pricing — Free permanently first, Pro
  $8/mo annual / $10 monthly, AI add-on $8.
- **Notion** (notion.com): warm neutrals (`#f6f5f4`, warm near-black,
  whisper borders `1px rgba(0,0,0,0.1)`), NotionInter 64px / −2.125px
  tracking; B&W line illustrations + one highlighted word (yellow pill);
  hero mockup is a *populated* workspace (Kanban: To-do/In progress/In
  review/Complete); trust band mixes scale + names + independent proof
  (100M users · 50% of YC · 62% of Fortune 100 · 1.4M community · G2 #1
  ×3 years); use-case verb cards ("Triage product feedback"...) with tiny
  illustrations; single purple pill CTA `#5645d4` for the one primary
  action.
- **Awwwards winners:** Bitwip (SOTD 5 Nov 2026, bitwip.fr — "TECH MEETS
  CREATIVITY"; metrics second "200+ projects · 12+ years"; edge-to-edge
  showreel, live office clocks per territory, platformer 404; territory
  sections + logo grid + named testimonial); Scout Motors (E-commerce of
  the Year 2026 — one sentence + same "Reserve Now" CTA repeated at every
  section break; price + caveat beside the CTA; heritage 1961 before
  product; numbered 01–12 gallery with place/year captions); Lando Norris
  (Site of the Year 2026, landonorris.com — one typeface used big,
  hand-broken uppercase headlines "ON / TRACK", bolded words inside a
  personal message, hover-swap helmet cards, everything numbered, hero 0,
  projects 01, "Next.2"); Bulgari "Emerald Strata" (SOTD 2026 — 3 chapters
  with labelled interactions "drag to explore", macro + workshop + sketch
  photos on warm beige, craft quantified "26.05 carats · ~1 year ·
  1000+ hours"); bonus Penelope Care (lifestyle hero + 3-word heading +
  one button; shop cut 4 ways; prices on homepage; shipping in top
  banner).
- **Top-10 cross-cutting moves:** (1) one expressive surface, rest flat;
  (2) one accent + one type scale (56/40/28/17), light weights 300–510 +
  negative tracking; (3) real product UI/photo as hero; (4) trust =
  numbers + names + independent proof; (5) mono uppercase micro-eyebrows;
  (6) hairlines + surface ladder, not shadows; (7) one CTA repeated, price
  beside it; (8) label interactions + number items 01–13 with captions;
  (9) sidebar-first "Spaces" app layout; (10) warm neutrals + one
  highlighted word + one peeking illustration. Do NOT copy: Arc as a live
  brand; Stripe's rainbow on the industrial page (borrow structure,
  recolour); Lando/Bulgari maximalism on distributor homepages; Penelope
  Care's disabled pinch-zoom.

## Taste filter (applies to everything from now on)

- **NON-GENERIC ONLY.** No generic stock icons, no clip-art-style
  illustrations, no flat pastel blobs everyone uses. The 39 SVGs failed
  this bar and were retired (see SOURCES.md).
- **Every asset justified by the research.** Each placement in
  PLACEMENT.md names the exemplar/pattern it serves. Fewer, better assets
  beat volume: 22 photos + 18 product photos is the whole set.
- **Real photography or real product UI as hero** (Stripe/Linear/Apple),
  never a flat illustration pretending to be a product.
- **One expressive surface per page, rest flat** (Stripe/Arc). One accent
  colour per page, used for price/discount/CTA/active only
  (Digikala/Snapp/Torob).
- **Trust as a mechanism or a number** (Torob seller counts, Stripe hard
  numbers, Cafe Bazaar named mechanisms) — never a generic shield icon.

## Shared design tokens

Use these on every page so the eight samples read as one portfolio:

- **Type:** one scale per page — display 56px (hero, English) / 40px
  (Persian hero, Vazirmatn 700), section 28px/600, sub-section 18px/600,
  body 14–16px, label/micro-eyebrow 11–13px uppercase (Persian:
  letterspaced, not all-caps — all-caps does not exist in Persian script),
  tracking −0.02em to −0.06em on display sizes, light weights (300–510)
  where the font allows. Numbers always `font-variant-numeric:
  tabular-nums`; Persian prices always with thousand separators + «تومان».
- **Colour:** one flat accent per page (price/discount/CTA/active only);
  surfaces as a ladder (hairlines + 2–3 greys), not shadows; colour =
  meaning only (green = favourable/OK, red = problem, amber = warning).
- **Spacing:** an 8px rhythm (4/8/12/16/24/32/48/80); section gaps 48–80px,
  card padding 20–24px, card radius 12–14px.
- **Sections:** every section gets a numbered/labelled eyebrow (e.g.
  «۰۱ · خدمات») so a scanning reader can tell where summary ends and
  evidence begins (Observable "one named view per section").

## Shared motion system (applies to every page)

Governing principle (Kowalski, Linear/ex-Vercel): **motion must earn its
place** — explain hierarchy, confirm an action, guide attention, maintain
continuity, or add polish; otherwise delete it. "Animation should be felt,
not seen." Frequency rule: actions done 100+ times/day get no animation;
hovers minimal/fast; modals/toasts standard; rare moments (success) may
delight.

- **Durations:** micro/press 100–160 ms · hover/tooltip 150–200 ms ·
  menus/tabs/cards 200–300 ms · modal/drawer 300–500 ms · section reveals
  400–800 ms · count-up 600–900 ms (headline result only) · ambient loops
  8–20 s only. Functional UI under a 300 ms default ceiling; never
  >700 ms functional, never >1500 ms anything. Enter longer than exit
  (modal 300 ms in / 200 ms out).
- **Easings:** workhorse `--ease-out: cubic-bezier(0.23, 1, 0.32, 1)` ·
  Stripe soft `cubic-bezier(0.215, 0.61, 0.355, 1)` · Material standard
  `cubic-bezier(0.4, 0, 0.2, 1)`, enter `cubic-bezier(0, 0, 0.2, 1)`,
  exit `cubic-bezier(0.4, 0, 1, 1)` · sheet `cubic-bezier(0.32, 0.72, 0, 1)`
  · expressive hero `cubic-bezier(0.16, 1, 0.3, 1)`. Ease-out for
  entering, ease-in only for exits, never `linear` for UI, no
  bounce/elastic on product chrome (overshoot reserved for one
  celebration, e.g. order placed).
- **Page-load reveals:** animate `transform` + `opacity` only; fade + rise
  12–24 px (16 px house value), 500–600 ms; choreography hero visual →
  headline → CTA, stagger **60 ms** per item (30–80 ms range), **capped
  at 6 items**; never block interaction during a stagger.
- **Hover:** button `translateY(-1px)` + shadow 150–200 ms, `:active
  scale(0.97)` 100 ms; card lift −2 to −4 px + shadow 250–300 ms (Linear
  variant: 1 px accent glow fading in, 150 ms); arrow links +3–4 px,
  150 ms; product image `scale(1.04)` inside `overflow:hidden`, 300 ms;
  gate lifts behind `@media (hover: hover)`.
- **State changes:** cart badge pulse (scale 1→1.25→1, 300 ms) + button
  morphing to "✓ Added" (150 ms); tab switch = opacity crossfade 200 ms
  + sliding indicator 250 ms; accordion/modal = fade + scale 0.95→1,
  300 ms in / 200 ms out, content a beat after container; configurator =
  colour crossfade 300 ms + 2% settle (no sideways slide), price counts
  old→new value 400 ms; calculator = count-up 700 ms ease-out via
  `requestAnimationFrame` from the *previous* value (not zero), only on
  Calculate press, never per keystroke, `tabular-nums`, final frame
  exactly the target; map = pin tap scale 250 ms, `flyTo` 600–800 ms but
  cancelled on user input, pins fade in/out (never slide).
- **Scroll reveals:** triggered one-shot only, no scrubbed/pinned scenes;
  one shared `IntersectionObserver`, threshold 0.15 (0.2 for large
  sections), `rootMargin: 0px 0px -10% 0px`, `unobserve()` after firing,
  once-only; no-JS fallback reveals everything; do NOT import AOS
  (~20 lines vanilla); CSS scroll-driven animations are Chromium-only in
  2026 — don't use them.
- **Never:** layout properties, parallax/scroll-jacking, >500 ms
  functional durations, animating everything, bounce on routine UI,
  `ease`/`linear` defaults, autoplay that fights the user, scroll
  listeners with `getBoundingClientRect()` per frame, one observer per
  element, hidden content without JS, flashing >3/sec (WCAG 2.3.1).
- **`prefers-reduced-motion` (exact):** CSS safety-net reset
  (`animation/transition-duration: 0.01ms!important;
  animation-iteration-count: 1!important; scroll-behavior: auto!important`)
  PLUS a JS guard — `matchMedia('(prefers-reduced-motion: reduce)')` with
  a `change` listener gating all JS motion (reveals, count-ups, flyTo,
  loops). "Reduce ≠ none": drop translations/spins/zooms, keep ≤200 ms
  fades and colour changes; hover feedback becomes a border/outline
  instead of a lift. Disable: reveals, parallax, fly-to-cart, count-ups
  (show final value), ambient loops, stagger delays. Test in DevTools
  emulation + once on a real device.
- **RTL note:** drawer/modal slides mirror to `inline-end` in RTL;
  reveals rise vertically (direction-neutral); arrow nudges follow the
  reading direction (left in RTL, right in LTR).
- **Current state (verified 2026-11-10):** sample pages have almost no
  motion — only a few bare `transform .2s` / `.25s ease` transitions;
  Persian corporate pages have **zero** transitions. Everything below
  starts from that baseline.
- **Caveats:** Arc-specific durations could not be sourced; Stripe/Linear
  numbers are consensus values from scraped snapshots and research
  playbooks, not their production stylesheets; RTL mirroring notes are
  recommendations, not sourced guidance.

---

## corporate/ — آریا صنعت توان (Persian, industrial distributor)

Page structure (verified): hero «تجهیزات برق صنعتی را سریع‌تر، شفاف‌تر و
با…», services «همه خدمات، در یک جا» / «چرا آریا صنعت توان؟», trust badges
(نشان‌های اعتماد محلی), about page sections «داستان ما»، «ماموریت ما»،
«چشم‌انداز ما»، «مشخصات شرکت»، «ارزش‌های ما»، «تیم ما». Currently **zero**
transitions anywhere on the Persian corporate pages.

1. **Hero becomes a real place, not a gradient.** `switchgear.jpg` as a
   large-format hero image beside the opening heading (Linear "product
   screenshot IS the hero", Vercel proof-first). The photo's own
   blue-grey tones set the page accent — no purple anywhere. Type: hero
   40px/700 Vazirmatn, one-line tagline, one CTA. Motion: load fade+rise
   16px, 600 ms, hero visual → headline → CTA, stagger 60 ms.
2. **Trust as numbers, not badges.** Replace the generic trust-badge row
   with a Stripe-style trust band: named brands (Siemens, ABB, Megger,
   Omicron, Prysmian, Fluke) as a text row + hard numbers (years in
   business, models stocked, orders fulfilled) — Torob's "seller count as
   trust" pattern. Numbers count up 700 ms on scroll into view.
3. **One dark expressive band.** `pylon.jpg` as a full-width dark section
   background behind «چشم‌انداز ما» (Arc "one flooded band", Stripe "one
   expressive surface, rest flat"). Abstract use only — never caption it
   as electrical equipment. Motion: section reveal once-only, 500 ms
   fade+rise; no parallax.
4. **Heritage as proof, if Marshall likes it.** `factory-interior.jpg`
   (1936 B&W hall) in «داستان ما» — Bulgari "craft quantified": the past
   as proof of longevity, kept B&W. If he doesn't like the heritage tone,
   drop it and let `switchgear.jpg` carry the page alone.
5. **Motion baseline fix.** Add the shared motion system: solid card lift
   only (no card scale) on service cards, datasheet rows background-fade
   only, nav underline slides between pages, page change is a 200 ms
   opacity fade (Linear pattern). This page currently has zero
   transitions — even the baseline matters most here.

## corporate-intl/ — Corelia (English, fintech)

Page structure (verified, 54,962 B): "Financial infrastructure", "Proof
before pitch", "Flexible solutions for every business model", "Built for
every stage", "In their own words", "An API your engineers will actually
enjoy", "Transparent pricing, no surprises", "Answers before you ask",
"Talk to a human about your volume", "Ready to get started?"

1. **Hero: real financial district + live preview.** `financial-district.jpg`
   (Cabot Square at dusk) beside "Financial infrastructure" and the live
   settlement preview (Stripe: one expressive surface in the upper-third
   hero, rest white + navy ink `#0a2540`; Linear: real product UI IS the
   hero). Hero 56px/300 Söhne-style light display type, tracking −0.02em.
   Motion: Stripe-style hero 600 ms, no bounce/slide — fade + 16px rise,
   visual → headline → CTA, stagger 60 ms.
2. **"Proof before pitch" becomes a numbers band.** Stripe trust-as-numbers
   (135+ currencies · $1.9T · 99.999% uptime) translated to Corelia's
   scale: settlement volume, currencies, uptime, named customers — then
   the "In their own words" testimonials with per-case "Products used"
   lines (Stripe pattern). Numbers count up 700 ms on scroll into view.
3. **One architectural photo, one flooded band.** `modern-architecture.jpg`
   (brutalist Australian Embassy, Paris) as the single image in "Built for
   every stage"; `contactless-pos.jpg` (POS terminal + coffee) in the fee
   calculator / "Transparent pricing" section — Vercel proof-first: show
   the transaction, don't describe it. No other images on the page.
4. **Pricing toggle + CTA discipline.** "Transparent pricing" gets a
   toggle with a sliding pill (250 ms) + price count 400 ms on switch;
   the one CTA ("Ready to get started?") repeats at every section break
   with price beside it (Scout Motors pattern). Arrow links nudge +4 px /
   150 ms. **No logo marquee** — flagged as the common fintech tell.
5. **Type + hairlines.** Light display type (300–450), mono uppercase
   micro-eyebrows 11–13px / 0.071em above each section ("SETTLEMENT",
   "PRICING", "API"), hairlines + surface ladder instead of shadows
   (Linear/Vercel). Motion: pricing toggle pill slide 250 ms, price count
   400 ms, arrow nudge +4 px/150 ms.

---

## store/ — آریا استور (Persian, online store)

Page structure (verified, 83,802 B): «جشنوارهٔ بزرگ تخفیف آریا استور»,
«خرید اقساطی، بدون پیش‌پرداخت سنگین», «ارسال سریع به سراسر کشور», «⚡
پیشنهادهای شگفت‌انگیز امروز», «خرید بر اساس بودجه», «پرسش‌های پرتکرار
خریداران», «سبد خرید شما». 13 real products with real photos
(`store/products/`).

1. **Festival hero with a real subject.** `shopping-bags-paper.jpg`
   (woman with plain paper bags, no brands) beside «جشنوارهٔ بزرگ تخفیف»
   — Snappfood "discount rail" energy, Digikala promo-card structure
   (promo carousel → promo cards → category tiles → named product rails).
   The hero is the festival's subject, not a gradient. Motion: load
   reveal 600 ms, image → headline → CTA, stagger 60 ms.
2. **Product cards, Digikala-style.** Card = real product photo +
   truncated title + seller/stock + bold price + struck old price + red %
   pill (Digikala card pattern, verified). Prices always Persian digits +
   thousand separators + «تومان»; «از» for from-prices. Product image
   `scale(1.04)` inside `overflow:hidden` on hover, 300 ms; card lift
   −2 to −4 px + shadow, 250–300 ms, gated behind `@media (hover: hover)`.
3. **Named rails, not one long grid.** «پیشنهادهای شگفت‌انگیز امروز» as a
   horizontal rail with a live countdown + capped discount amount
   (Snappfood «تخفیف شکار کن» pattern); «خرید بر اساس بودجه» as named
   budget rails; grids only for search results (Aparat intent-named
   rails). Status lives on the card (Torob: «ناموجود» shown, never
   hidden); honest empty state «این محصول فعلا فروشنده‌ای ندارد» +
   similar products when a variant is out.
4. **Delivery as proof.** `delivery-doorstep.jpg` (real doorstep parcel
   handoff) in «ارسال سریع به سراسر کشور» — Torob "trust as a mechanism":
   show the delivery happening. Shipping promise stated once, in one
   place (the UX audit found three conflicting promises: 1–2 vs 1–3 vs
   1–4 days — pick one). Empty cart is a typographic/CSS state, not an
   illustration.
5. **Cart micro-interactions.** Add-to-cart: badge pulse (scale 1→1.25→1,
   300 ms) + button morphing to «✓ اضافه شد» (150 ms); cart drawer opens
   as a sheet (300 ms, sheet curve `cubic-bezier(0.32, 0.72, 0, 1)`),
   mirrored to `inline-end` in RTL. Filter chips: 150 ms exit / 250 ms
   staggered entrance. Grid reveal: stagger 60 ms, capped at 6 items.

## store-intl/ — Northlight (English, minimal store)

Page structure (verified, 45,489 B): "Search northlight.com", iPhone 18
Pro, MacBook Air, Apple Watch Series 11, "The latest.", "Ways to save.",
"Buy iPhone 18 Pro", "Which iPhone 18 Pro is right for you?",
"Questions? We have answers.", "Your Bag". 7 real product photos
(`store-intl/products/`).

1. **Apple discipline, applied literally.** One product per tile, one
   viewport per tile; name 40px/600 + one-line tagline + two tiny blue
   pill CTAs (`#0066cc`); alternating light/dark tiles; near-zero density
   (Apple). `phone-blank-screen.jpg` (minimalist blank-screen phone) as
   configurator side art beside "Buy iPhone 18 Pro" — the blank screen is
   the point: the configurator is the content. Motion: hero phone fade +
   scale 0.98→1, 700 ms.
2. **Configurator as progressive disclosure.** Finish → Storage →
   Accessories, live price, sticky sub-nav with Buy + price (Apple
   pattern). Colour choice = crossfade 300 ms + 2% settle (no sideways
   slide); storage change = price counts old→new value, 400 ms, plus a
   "Δ +$200" hint; Buy button draws a checkmark on success — the one
   earned celebration on the page. Spec accordion via
   `grid-template-rows`, 300 ms in / 200 ms out.
3. **"Ways to save." as honest proof.** Raycast honest pricing first
   (Free permanently first, then Pro): show the real saving per option
   with the price beside the CTA, one CTA repeated (Scout Motors). No
   invented discounts — the 7 real product photos carry the grid; the
   iPhone 18 Pro/Max and MacBook Air M5 photos are the previous generation
   (17 Pro/Max, M4) and are noted as such in SOURCES.md, never claimed
   as 18-series shots.
4. **Type + hairlines, nothing else.** Geist-style 450 weight, −0.06em
   tracking on display sizes; mono uppercase micro-eyebrows 11–13px /
   0.071em; monochrome `#fafafa` / `#171717`, hairlines, colour only as
   meaning (Vercel). No decorative images beyond the phone + product
   photos; no icons.

## diet/ — سبزینه (Persian, diet calculator)

Page structure (verified, 55,826 B): «محاسبه‌گر کالری و شاخص تودهٔ بدنی»,
«مشخصات شما», «نتیجه شما», «هدف روزانه و پیش‌بینی تغییر وزن»,
«درشت‌مغذی‌های روزانه», «نمونه برنامه یک روز (مقادیر به گرم)», «قدم‌های
بعدی شما», «سبزینه را بشناسید», «برنامه‌های غذایی», «دستورهای غذایی»,
«تجربه کاربران سبزینه», «پرسش‌های پرتکرار», «سبزینه را همیشه همراه داشته
باشید».

1. **Hero with room for the calculator.** `salad-bowl-pexels.jpg`
   (top-view salad bowl on white marble, large negative space) beside the
   calculator — Notion warm neutrals + one highlighted element: the
   negative space is where «مشخصات شما» sits. Warm neutrals (`#f6f5f4`,
   warm near-black, whisper borders) instead of clinical white.
2. **Real Iranian food, not stock "healthy".** `ghormeh-sabzi.jpg` (real
   vegan ghormeh sabzi with rice and salad) in «نمونه برنامه یک روز» /
   «دستورهای غذایی» — Aparat intent-named rails: this is the dish the
   audience actually eats. `vegetable-market.jpg` (farmers-market oranges,
   already cropped) in «سبزینه را بشناسید» — Balad need-based sections:
   food as a place, not a concept.
3. **Results as a hero number, not a wall of text.** «نتیجه شما» (BMR +
   daily target) becomes one big number (32px/700, `tabular-nums`) with
   the projection beside it; macro bars animate via `transform: scaleX`
   (not `width`), 500 ms; stepper press 100 ms. Count-up 700 ms
   ease-out via `requestAnimationFrame` from the *previous* value (not
   zero), **only on Calculate press, never per keystroke**, final frame
   exactly the target.
4. **Testimonials as a named rail.** «تجربه کاربران سبزینه» as a named
   horizontal rail with one trust metric per card (Cafe Bazaar app-card
   pattern: icon + name + category + one trust metric — here, typographic,
   no icon). No-data states written out (Balad pattern).
5. **Motion restraint.** Calculator count-up on Calculate only; macro
   bars `scaleX`; no count on typing; section reveals once-only, 500 ms.
   The calculator is used repeatedly — it must never feel like a
   performance.

## diet-intl/ — Platewise (English, calorie app)

Page structure (verified, 49,943 B): "Know what you eat.", "Loved by
people getting healthier", "Everything you need, in your pocket", "Syncs
with the devices you already own", "Free BMR calculator", "Frequently
asked questions", "Your first healthy week starts today".

1. **The bowl IS the hero.** `buddha-bowl.jpg` (vibrant buddha bowl:
   avocado, tempeh, edamame, radish, rice) beside "Know what you eat." —
   Apple one-product-per-tile. One highlighted element on warm neutrals
   (Notion). Hero 56px/−2.125px tracking.
2. **Activity as one human moment.** `gym-dumbbells.jpg` (hand gripping a
   dumbbell) in "Everything you need, in your pocket" — exercise is half
   the app's story. Raycast "one accent used once per page" discipline:
   one human moment, not a gym montage.
3. **Use-case verb cards.** "Triage product feedback"-style verb cards
   (Notion): "Log a meal", "Scan a barcode", "Hit your protein" — each
   with a tiny caption, no icons. "Syncs with the devices you already
   own" as a populated-mockup band (Notion: hero mockup is a *populated*
   workspace — here, a populated day-log, not an empty app shell).
4. **Calculator + week plan as the conversion path.** "Free BMR
   calculator" with the same count-up rules as Sabzineh (700 ms, on
   Calculate only, from previous value); "Your first healthy week starts
   today" as a 7-day numbered path (Lando Norris "everything numbered")
   with one CTA repeated. FAQ as an accordion (fade + scale 0.95→1,
   300 ms in / 200 ms out, content a beat after container).

---

## map/ — نقشه‌یار (Persian, Tehran places map)

Page structure (verified, 57,055 B): «نقشه‌یار» + «نتایج» — mostly
JS-driven (place names rendered by JS). The page is a map with a results
panel; the direction below is about the frame around the map, not the map
tiles (Esri tiles already verified).

1. **Landmark as identity.** `azadi-tower.jpg` (low-angle Azadi Tower,
   deep blue sky) as the hero above the map and filters — Balad "city
   guide by human need" + Linear "product screenshot IS the hero": the
   landmark is the page's identity, not decoration. This is the best
   single image in the whole set.
2. **Need-based sections, not a bare list.** Balad pattern: organise the
   results panel by human need — خوردنی / موندنی / دیدنی — with ranked
   lists + «مشاهده موارد بیشتر». `milad-tower.jpg` (night view *from*
   Milad Tower) anchors «دیدنی»; `tehran-bazaar.jpg` (bazaar street)
   anchors «خوردنی»; `tehran-skyline.jpg` (north Tehran under the Alborz)
   heads the «نتایج» panel. Place rows = name + type + rating +
   reviewer count; no-data state written out («نظر و امتیازی وجود ندارد»).
3. **Iran-specific intelligence as copy.** Balad pattern: traffic/pollution
   zones, speed-camera alerts, house numbers, Persian voice assistant —
   as one-line copy in the relevant section, not as a feature list. This
   is the one thing no international map sample can show, and it is the
   page's distinctive value.
4. **`golestan-palace.jpg` as texture.** Tilework close-up as the header
   texture for historical/cultural places (Bulgari macro-detail pattern)
   — it replaces the old landmark icon's job with something real.
5. **Motion.** Pin tap scale 250 ms; `flyTo` 600–800 ms, cancelled on
   user input; pins fade in/out (never slide); filter change = fade
   in/out, pins never slide; list↔map cross-highlight, pin 1.15, 150 ms.
   No scroll-jacking on the map; the map is the interaction, not the
   animation.

## map-intl/ — Wayfinder (English, places map)

Page structure (verified, 78,215 B): place names rendered by JS; 4 travel
modes; "Search in this area" affordance; place details panel.

1. **One destination, one mood.** `city-skyline.jpg` (Château Frontenac
   at dusk with a cruise ship) as the hero above the map — Arc "Spaces"
   pattern: one place, one mood, one flooded image. The hero is a
   destination, not a map pin. No second image: a distinctive
   traveller/city-walk photo was hunted and not found to the bar; one
   strong hero suffices.
2. **Sidebar-first "Spaces" layout.** Arc pattern: a 240px sidebar of
   named place collections ("Spaces"), each with its own 2-colour mood,
   13px titles — the map is the content area, the sidebar is the
   navigation. This is the one layout move that makes Wayfinder feel
   like an app, not a demo.
3. **Place details as a destination card.** When a place is picked, the
   details panel shows name + type + rating (abbreviated count) + status
   (open/closed/pre-order — shown on the card, never hidden, Snappfood
   pattern) + one photo when available. Routing: 4 travel modes with a
   navigation arrow mark — typographic, no icon set.
4. **Numbered, labelled exploration.** Lando Norris "everything
   numbered": curated routes as numbered items 01–13 with place/year
   captions (Scout Motors numbered gallery); interactions labelled
   ("drag to explore", Bulgari pattern).
5. **Motion.** Same as Naghshehyar: pin tap 250 ms, interruptible `flyTo`
   600–800 ms, pins fade in/out, list↔map cross-highlight 150 ms.
   Sidebar sections reveal once-only, 500 ms.

## index/ — portfolio index

Page structure (verified): «نمونه‌کارها — رضا محمدرضایی», «رزومه», «نمونه کارها».

1. **One cover image, type carries the rest.** `workspace-minimal.jpg`
   (white-desk flat-lay) at the top beside «نمونه‌کارها — رضا محمدرضایی» —
   **flagged as the weakest keeper in the set** (a familiar flat-lay). If
   Marshall dislikes it, drop it and let the type carry the page
   (Vercel monochrome discipline). One image only, never a gallery.
2. **Front-door load reveal.** Hero visual → headline → project list,
   fade + 16px rise, 500–600 ms, stagger 60 ms capped at 6 items.
   Project cards: lift −2 to −4 px + arrow nudge +3–4 px, 150–250 ms.
3. **The portfolio as a numbered index.** Lando Norris "everything
   numbered": each sample as a numbered row (01–08) with a one-line
   description and a mono micro-eyebrow for its type (STORE / FINTECH /
   CALCULATOR / MAP). No thumbnails of the sample pages — the samples
   are the content; the index is the table of contents.
4. **Trust band, Notion-style.** Scale + names + independent proof in one
   band (100M users · 50% of YC pattern, translated: real counts from the
   portfolio — 8 samples, 13 real products, 2 languages, 4 reports).

## resume/ — resume page

Page structure (verified): «رزومه — رضا محمدرضایی», «درباره من», «خدمات», «نمونه‌کار
واقعی», «نمونه کارها», «تحصیلات و گواهی», «شرایط کاری», «روش کار»,
«English version».

1. **Warm header, no portrait.** `workspace-notebook.jpg` (wooden desk,
   laptop, blank notebook, coffee, no text) beside the name / «درباره من»
   — Notion warm neutrals. The work, not a portrait.
2. **A CV is read, not performed.** Resume sections reveal once-only
   **with no stagger** (motion research: a CV is read, not performed).
   Skill bars animate via `transform: scaleX`, 500 ms, on scroll into
   view. All motion off in `@media print` — the printed resume must be
   clean and static.
3. **Services as verb cards.** «خدمات» as Notion-style use-case verb
   cards ("Translate EN↔FA", "Build a store sample", "Audit a UX") with
   one-line outcomes each. «نمونه‌کار واقعی» links to the live samples
   with one-line proof each (13 real products, Esri maps, real reports).
4. **«شرایط کاری» and «روش کار» as honest, checkable claims.**
   Snapp/Cafe Bazaar pattern: benefit cards with checkable claims
   ("register in under 10 minutes" style) — e.g. response time, revision
   policy, delivery format — each verifiable, none vague.

---

# Reports & sheets pages — design direction

Marshall's verdict on these four: *"too plain — pretty much a white page
with writing."* They need the same professional treatment as the web
pages. Everything below is grounded in what the files actually contain
(tables, numbers, sections verified by reading each file). Nothing here
invents new data. Sources studied: Stripe/Linear/Vercel dashboard
patterns (2026 round-ups), the dashboard-design skill (Stripe/Linear/
Vercel standard), Setproduct data-table guide, Observable data apps,
Tableau visual best practice, sklearn `plot_tree` visualisation, HTML
report patterns (ops/report skill).

Scope: `code/price-monitor/report.html`,
`code/pandas-decision-tree/report.html`,
`sheets/price-inventory-preview.html`, `sheets/apps-script-sample.html`.
All four share the same shell today — Vazirmatn, `#f3f4f6` page
background, white cards (`border #e5e7eb`, `radius 14px`, `padding
20px`), `max-width: 880px`, `h1 26px`, amber نمونه کار badge — so §R0
fixes the shared shell once, and §§R1–R4 give each page its own highest-
impact changes.

## §R0 — Shared shell (apply to all four pages before any per-page work)

1. **Widen and re-tokenise.** `max-width: 880px` → `1120px` (reports are
   wide artefacts; 880px forces the 9-column products table and the
   8-column price-history table into horizontal scroll). Page background
   `#f3f4f6` → `#FAFAFA`; card border `#E5E5E5`; text `#171717` /
   secondary `#525252` / tertiary `#A3A3A3`; keep the existing blue
   `#2563EB` as the single primary accent and green `#16A34A` / red
   `#DC2626` strictly for semantic up/down states (Stripe/Vercel rule:
   colour = meaning). Define these once as CSS variables; every page
   reuses them, so the four pages finally read as one portfolio.
2. **One type scale, tabular numbers everywhere.** Page title 28px/700,
   section `h2` 18px/600, card label 12px/500 uppercase (Persian:
   letterspaced, not all-caps), body 14px/400 with `line-height 1.9`
   kept for Persian readability, caption/footnote 12px. All money,
   percentages, counts and dates get `font-variant-numeric: tabular-nums`
   and `direction: ltr; unicode-bidi: embed` on the numeric span so
   digits align in columns — today the Persian-digit prices in the stats
   tables do not line up. **RTL note:** the Setproduct/Stripe
   "right-align numbers" rule is written for LTR; in these RTL pages the
   equivalent is: numeric columns align to the *number edge* (left in RTL
   layout) with a consistent gutter, text columns to the reading edge.
   Pick one and apply it identically in all four tables.
3. **A real page header, not a bare `h1` + badge.** Every page gets the
   same header block: eyebrow (e.g. `گزارش قیمت · بیت‌کوین و اتریوم`),
   title, one-line sub, and a meta row (date / source / scope) in 12px
   tertiary text with a hairline divider underneath (Stripe "context
   beside the value" pattern — the date `۲۰۲۶/۱۱/۱۰` currently floats as
   a grey sub-line and reads as an afterthought). Keep the amber نمونه کار
   badge, but move it into the meta row as a small pill instead of glued
   to the title.
4. **Section rhythm.** `margin-bottom: 20px` on cards is fine; add a
   numbered section eyebrow (`۰۱ · داشبورد`, `۰۲ · محصولات`…) in 12px/600
   blue-grey above each `h2`, and `24px` gaps between major sections vs
   `16px` inside a card (Observable "one named view per section" in
   static form).
5. **Motion (shared).** Page load: cards `fadeUp` — `opacity 0 → 1`,
   `translateY(8px) → 0`, `320ms`, `cubic-bezier(0.22, 1, 0.36, 1)`,
   staggered `60ms` per card, max 5 cards staggered (later cards animate
   together, no conga line). KPI/hero numbers: count-up `700ms`, same
   easing, only for the 1–2 hero numbers per page. All hover/focus state
   changes: `150ms ease-out`. **Always** wrap in `@media
   (prefers-reduced-motion: reduce) { * { animation: none !important;
   transition: none !important; } }` and set final values as the default
   state so content is never hidden if JS/CSS animation fails.

## §R1 — `code/price-monitor/report.html` — Price-history report (Bitcoin & Ethereum)

What the file actually contains: RTL Persian. Two asset cards (Bitcoin,
Ethereum), each with 30/90/120-day range buttons (۱۲۰ = همه, currently
active), three inline-SVG chart views (one per range), a legend (میانگین
green `#16a34a`, کمترین قیمت blue `#2563eb`, بدون تغییر dashed grey),
and a 4-row stats table (کمترین / بیشترین / قیمت فعلی / میانگین).
Bitcoin: min $86,272.28 (۲۰۲۶/۰۷/۱۴), max $103,160.79 (۲۰۲۶/۱۱/۰۴),
current $102,500 (۲۰۲۶/۱۱/۱۰), 120-day average $96,242.49. Ethereum: min
$3,527.68 (۲۰۲۶/۱۰/۰۹), max $4,565.80 (۲۰۲۶/۰۸/۱۳), current $3,850,
average $4,034.50. Then a "مقایسه با میانگین" section with two deal
cards: Bitcoin $102,500, +6.5% above average (pill بالای میانگین,
currently grey/plain); Ethereum $3,850, −4.6% below average (pill بهترین
قیمت, green), $322.32 above its recorded low. Then an alert panel: coin
select, target-price input, % shortcut chips (−3/−5/−7/−10% and هر کاهش
قیمتی), email field, green ثبت هشدار button, green confirmation box on
submit. Current problems: the stats that matter (current price, % vs
average) are buried in a plain 3-column table and in small deal cards at
the bottom; the two SVG lines have no area fill, no end-dot, no hover
value, no min/max markers; the range switch swaps whole SVGs with no
transition; up/down has no colour (both deal pills are neutral/green
regardless of direction).

1. **KPI strip on top of each asset card (highest impact).** Replace the
   4-row stats table as the *first* thing in each card with a 4-across
   KPI row (Stripe pattern: KPI row first, chart second, table as
   evidence): **قیمت فعلی** (32px/700, tabular-nums, hero number), **٪
   نسبت به میانگین** (+6.5% BTC / −4.6% ETH, coloured — see change 2),
   **کمترین** and **بیشترین** (16px/600 with 12px date caption
   underneath, e.g. `۲۰۲۶/۰۷/۱۴`). The existing stats table stays, but
   moves *below* the chart as the evidence table with a sticky header.
2. **One colour system for direction, used identically in both assets.**
   Green `#16A34A` = price is *favourable* (below average / near the
   low); amber `#D97706` = above average but within range; red `#DC2626`
   = at/near the recorded high. Apply it to: the % vs average figure,
   the deal pill (Bitcoin's بالای میانگین pill stops being grey `.plain`
   and becomes amber; Ethereum's بهترین قیمت stays green), and the
   chart's end-dot. Never use green/red for the two chart *series*
   themselves — the series keep their existing identity colours (average
   green line, lowest-price blue line) and direction colour lives only
   in the KPI/pill layer, so colour never means two things at once
   (Vercel/Stripe discipline).
3. **Make the chart a chart, not two polylines.** Keep the hand-built SVG
   (no chart library needed): add a soft area fill under the average
   line (`fill #16A34A`, `opacity 0.07` — flat fill, never a gradient),
   a 5px end-dot on the current price with a white stroke, min/max
   markers (small dots + 12px labels at $86,272.28 / $103,160.79 for BTC
   and $3,527.68 / $4,565.80 for ETH), and a hover crosshair that shows
   date + both series values in a small tooltip (the existing
   `role="img"` + `aria-label` stays; add a visually-hidden table toggle
   "مشاهده به‌صورت جدول" for screen readers). Move the legend *inside*
   the chart card header as inline swatches next to the range buttons
   instead of a loose row underneath, and restyle the range buttons as a
   segmented control (single pill container, active segment dark
   `#111827` — the current per-button pill borders read as loose tags).
4. **Promote the comparison section into a verdict strip.** The two deal
   cards become a 2-column "verdict" row directly under the two asset
   cards: each card gets a left accent stripe (amber for BTC, green for
   ETH — the ops-report KPI-tile pattern), the big price stays 24px/700,
   and the note line becomes a structured second line: `میانگین
   $96,242.49 · فاصله تا کمترین $16,227.72` (BTC) / `میانگین $4,034.50 ·
   فاصله تا کمترین $322.32` (ETH). The $322.32 figure already exists in
   the ETH note — surface it in the same position on both cards so the
   two are comparable at a glance.
5. **Alert panel becomes a proper form card.** Give it the same
   white-card treatment as the asset cards (it currently has no card
   background at all), a 2-column layout on desktop (coin + target price
   side by side; email full-width below), the % chips as a segmented row
   with the active chip filled blue, and the confirmation message as a
   green callout with a check dot. The submit button keeps green
   `#16A34A` — it is the page's one primary action.
6. **Motion.** Range switch: outgoing chart fades `opacity 1 → 0, 120ms
   ease-out`, incoming chart fades in `180ms cubic-bezier(0.22,1,0.36,1)`
   with the average polyline drawing in via `stroke-dashoffset` over
   `500ms` (only on range change, not on first paint — first paint draws
   instantly, then the end-dot pops `scale 0 → 1, 200ms, 150ms delay`).
   KPI current-price numbers count up `700ms` on load. Deal-card accent
   stripe grows `width 0 → 3px, 300ms` on scroll into view
   (IntersectionObserver, once). Range-button state change `150ms
   ease-out`. `prefers-reduced-motion`: all of the above become instant
   swaps.

## §R2 — `code/pandas-decision-tree/report.html` — Decision-tree report (subscription prediction)

What the file actually contains: RTL Persian. Sections: what the model
does (target `subscribed`, 1 = buys / 0 = doesn't buy; 3 features `age`,
`monthly_visits`, `avg_order_toman` in a 2-column definition table); data
(`customers.csv`, 40 rows × 4 columns); split & training (75% train =
30 rows, 25% test = 10 rows, `random_state=42`, `stratify=y`,
`DecisionTreeClassifier(max_depth=3)`); main rule as a blue callout (avg
order **above 165,000 تومان → buys**, below → doesn't buy); accuracy as
a bare `۹۰٪` (24px) with note "9 of 10 test rows correct, measured on
test not train"; 3 sample predictions table (age 30 / 15 visits /
300,000 تومان → buys; 45 / 3 / 80,000 → doesn't buy; 25 / 20 / 400,000
→ buys) with green/red pills; run section (`pip install -r
requirements.txt`, `python3 train_tree.py`, dark `<pre>` block) and file
links (`train_tree.py`, `customers.csv`, `README.md`). Current problems:
there is *no tree diagram at all* — the report about a decision tree
shows the rule as a sentence; the 90% accuracy is a lone number with no
visual weight; the train/test split is prose, not a visual; the three
sample customers are a plain table with no link back to the rule.

> ⚠️ **Do-not-invent guardrail:** the file documents only the root split
> (avg order ≤/> 165,000 تومان). It does **not** give the depth-2/3
> splits, Gini values, or leaf sample counts. The diagram in change 1
> must therefore show exactly what is known — root + two leaves — and
> label deeper levels as "not shown in this report". If the implementer
> can export the real tree (`sklearn.tree.plot_tree`, `filled=True`), the
> full depth-3 tree replaces it; do not fabricate branch thresholds to
> fill the diagram.

1. **A visual tree diagram replaces the blue rule box (highest impact).**
   Build the tree as pure HTML/CSS (no image, no library): root node
   card — `میانگین سفارش ≤ ۱۶۵٬۰۰۰ تومان؟` — with two connector lines
   (SVG or CSS borders, elbow connectors, `drawIn` animation) branching
   to two leaf cards: **نمی‌خرد** (red-tinted, `#FEE2E2` bg / `#991B1B`
   text, the existing `.pill.nobuy` colours) and **می‌خرد**
   (green-tinted, `#DCFCE7` / `#166534`, existing `.pill.buy` colours).
   Each leaf shows the rule in one line (`≤ ۱۶۵٬۰۰۰ → ۰` / `>
   ۱۶۵٬۰۰۰ → ۱`) and, underneath, which sample customers land there (2
   buy / 1 no-buy from the samples table). This is the
   `plot_tree(filled=True, rounded=True)` pattern translated to HTML:
   colour by predicted class, darker = purer, human-readable
   feature/class names, rounded nodes. Put the existing rule sentence
   *under* the diagram as its caption, not as the diagram itself.
2. **Accuracy becomes a hero metric, not a 24px line.** A dedicated
   accuracy card: giant `۹۰٪` at 48px/700 with a 9/10 segmented bar
   underneath (10 segments, 9 filled green, 1 empty — a part-to-whole
   bar, never a pie chart), caption `۹ از ۱۰ ردیف تست درست پیش‌بینی شد ·
   سنجیده‌شده روی دادهٔ تست، نه آموزش`. Beside it (2-column row on
   desktop), a train/test split visual: a single horizontal stacked bar,
   75% blue (`آموزش · ۳۰ ردیف`) / 25% grey (`تست · ۱۰ ردیف`), with
   `random_state=42` and `stratify=y` as 12px captions underneath.
3. **Feature table becomes three feature chips + a data card.** The 4-row
   definition table (`age` / `monthly_visits` / `avg_order_toman` /
   `subscribed`) becomes: a row of three feature cards (monospace code
   name on top, Persian meaning below, e.g. `avg_order_toman` → میانگین
   مبلغ سفارش), plus a compact data card — `customers.csv · ۴۰ ردیف × ۴
   ستون` with a 4-column mini-grid showing the column names. The target
   `subscribed` gets its own treatment (a two-state pill `۱ = می‌خرد / ۰
   = نمی‌خرد`) so the output is visually distinct from the inputs.
4. **Sample predictions become "trace the tree" rows.** Keep the 3-row
   table but add a first column showing the path: `میانگین ۳۰۰٬۰۰۰ >
   ۱۶۵٬۰۰۰ ← شاخهٔ راست` for the two buyers and the mirrored left-branch
   path for the 45-year-old non-buyer — each row's pill then reads as the
   *outcome of following the diagram*, not an isolated label. Add a thin
   progress-style bar under each avg-order value showing where it sits
   relative to the 165,000 threshold (marker line at the threshold, dot
   at the customer's value: 80,000 left of it, 300,000/400,000 right of
   it). This is the Observable "derived metric" idea: the same threshold
   number appears in the tree, in the rule, and in every sample row, so
   the report feels like one connected argument.
5. **Run section becomes a terminal card.** Keep the dark `#111827`
   `<pre>` but give it a terminal chrome: a header bar with three dots +
   `train_tree.py` filename + a copy button, and syntax-colour the two
   commands (command in white, flags/paths in muted blue-grey —
   hand-coloured spans, no highlighter library). The three file links
   become a row of file chips with a small document glyph and the file
   type (`‎.py` / `‎.csv` / `‎.md`) as a suffix, instead of bare blue
   pill links.
6. **Motion.** Tree diagram: connectors draw in (`stroke-dashoffset`,
   `450ms`, `cubic-bezier(0.22,1,0.36,1)`), nodes `fadeScale` in
   root-first then leaves, staggered `120ms`. Accuracy number counts up
   0 → 90% over `800ms`; the 9/10 segments fill left-to-right, each
   `60ms` apart, bar fill `500ms ease-out`. Threshold dots in the sample
   rows slide from the threshold line to their value on scroll into view,
   `450ms`. Copy button: check feedback `200ms`.
   `prefers-reduced-motion`: tree appears fully drawn, numbers render at
   final values, no count-up.

## §R3 — `sheets/price-inventory-preview.html` — Price & inventory spreadsheet preview (Aria Mobile shop)

What the file actually contains: RTL Persian, shop «آریا موبایل». Action
row (green download button for `price-inventory-sample.xlsx`, secondary
README link) + a blue note ("formulas live in the file; dashboard numbers
are formula-computed"). Dashboard section: a 12-row, 2-column table — 15
products, 1,520 units, total value 206,405,000 تومان, 3 low-stock, 3
near-minimum, 9 sufficient, avg sell 347,800 تومان, avg buy 234,200
تومان, max sell 1,650,000 تومان, min sell 45,000 تومان, 8 recorded price
changes, 6 competitor-compared products. Products table: 15 rows × 9
columns (code, name, category, buy price, sell price, stock, min stock,
status pill, stock value) with a totals footer (1,520 units /
206,405,000 تومان). Status pills today: موجود green (9), نزدیک به حداقل
amber (3: A004 tablet glass 45/30, B002 leather iPhone case 35/20, D001
TWS earbuds 28/15), کمبود موجودی red (3: C002 USB-C cable 12/30, C003 car
charger 8/20, F001 smartwatch 5/10). Footnote explains the status formula
(≤ min = low; ≤ 2× min = near; else OK). Price-history table: 8 rows,
۱۴۰۵/۰۸/۰۲–۱۴۰۵/۰۸/۱۶, changes +5,000 to +100,000 تومان, two cuts
(−20,000 B002, −70,000 E001 powerbank), % from −6.7% to +11.1%, with a
reason per row. Competitor table: 6 products, 2 cheapest (A002 iPhone 15
glass, E001 powerbank, gap 0), 4 near-cheapest (gaps +3,000 / +6,000 /
+10,000 / +20,000 تومان). Current problems: the "dashboard" is a 12-row
label/value table — the numbers a shop owner cares about (total value,
low stock) are rows 3 and 4 of 12; the products table has no stock
visualisation (a 5 vs a 320 both read as plain numbers); price changes
have no direction colour; the page does not read as a spreadsheet at all,
despite being a preview *of* a spreadsheet.

1. **Dashboard table → KPI card grid (highest impact).** Convert the
   12-row table into a 4 + 4 KPI layout: Row 1 (the money row):
   **ارزش کل موجودی ۲۰۶٬۴۰۵٬۰۰۰ تومان** (hero, 32px/700), **۱٬۵۲۰
   واحد**, **۱۵ قلم**, **میانگین قیمت فروش ۳۴۷٬۸۰۰ تومان**. Row 2 (the
   health row): **۳ کمبود موجودی** (red accent), **۳ نزدیک به حداقل**
   (amber), **۹ موجودی کافی** (green), **۸ تغییر قیمت ثبت‌شده**. The
   remaining dashboard facts (avg buy 234,200, max sell 1,650,000, min
   sell 45,000, 6 competitor-compared) become small supporting lines
   under the relevant KPI cards (e.g. under avg sell: `خرید ۲۳۴٬۲۰۰ ·
   گران‌ترین ۱٬۶۵۰٬۰۰۰ · ارزان‌ترین ۴۵٬۰۰۰`), not their own rows. Stripe
   rule: cap KPIs at 4 per row, one primary metric per view — the total
   value is the primary, top-right in RTL (top-left in LTR terms). Add a
   thin stock-health stacked bar under the health row: 9 green / 3 amber
   / 3 red segments with a 3-up legend — the 9/3/3 split is instantly
   visible instead of three separate rows.
2. **Make the products table read as a real spreadsheet.** This is the one
   page where the spreadsheet metaphor should be *visible*: give the
   table a sheet chrome — a tab bar above it (`محصولات` active tab,
   `تاریخچهٔ تغییر قیمت` and `مقایسه با رقبا` as inactive tabs that scroll
   to those sections), a frozen first column (code) on horizontal scroll,
   sticky `<thead>` (`position: sticky; top: 0`, header bg `#F9FAFB`,
   12px/600 labels), row hover `#F9FAFB`, and a sticky totals footer (the
   existing `۱٬۵۲۰ / ۲۰۶٬۴۰۵٬۰۰۰` footer row stays pinned at the bottom
   of the scroll area). Add a toolbar above the table: a status filter
   (همه / کمبود / نزدیک به حداقل / موجود — clicking filters rows, with
   the active filter shown as a removable chip + result count `۱۵ قلم ←
   ۳ قلم`) and a search field filtering by name/code. Numbers aligned to
   the number edge with `tabular-nums`; product codes in monospace.
3. **Stock becomes a visual, not just a number.** In the موجودی column,
   add a mini stock bar under each number: bar length = stock relative
   to 2× min (the "near" threshold), coloured green / amber / red by the
   same status rule, so C002 (12 vs min 30) and F001 (5 vs min 10) read
   as nearly-empty bars before you read the digits. The وضعیت pill gets
   a dot prefix (●) in the same colour — status is never colour-alone
   (accessibility rule from the table guide). The three low-stock rows
   get a 3px red edge accent (RTL: right-edge) on the row itself, so
   scanning the table, the eye lands on C002, C003, F001 first.
4. **Price history: direction colour + a summary line.** The تغییر columns
   get semantic colour: increases in blue `#2563EB` with `+`, decreases
   in red `#DC2626` with `−`, and a small ▲/▼ glyph (not emoji) — the two
   cuts (B002 −20,000 / −5.9%, E001 −70,000 / −6.7%) must be instantly
   distinguishable from the six rises (+5,000 to +100,000, up to +11.1%
   on C002). Above the table, one summary line: `۸ تغییر · ۶ افزایش · ۲
   کاهش · بزرگ‌ترین افزایش ‎+۱۰۰٬۰۰۰ تومان (ساعت هوشمند)`. The دلیل
   column stays as text — it is the human context, and truncating it
   would lose the reason (supplier rise / FX / festival discount /
   competitor check).
5. **Competitor table: make "cheapest" the visual anchor.** In the
   ارزان‌ترین column, bold the winning price; in the اختلاف column, `۰`
   renders as a green `ارزان‌ترین` pill (A002, E001) and positive gaps as
   amber `+۳٬۰۰۰` … `+۲۰٬۰۰۰` text with a thin bar proportional to the
   gap (max 20,000 = full width). Add a one-line verdict above the
   table: `۲ از ۶ کالا ارزان‌ترین‌اند؛ بقیه تا ۲۰٬۰۰۰ تومان بالاترند`.
   Keep the existing footnote about generic competitor names (رقیب ۱ /
   رقیب ۲) — it is a trust note, not clutter.
6. **Motion.** KPI numbers count up `700ms` on load (total value counts
   in chunks, not digit-by-digit — animate the formatted number). Stock
   bars grow `width 0 → target, 500ms, cubic-bezier(0.22,1,0.36,1)`,
   staggered `40ms` per row. Filter change: non-matching rows fade/scale
   out `180ms ease-out`, matching rows flash a `#EFF6FF` background for
   `400ms` then settle. Tab switch scrolls smoothly
   (`scroll-behavior: smooth`, `400ms`) to the section. Sticky header
   appears with no animation (it must not shimmer on scroll).
   `prefers-reduced-motion`: bars render full-width instantly, no
   count-up, filter changes are instant.

## §R4 — `sheets/apps-script-sample.html` — Apps Script automation sample

What the file actually contains: RTL Persian. Intro: two automations for
a Google Sheets price/inventory workbook — (1) every sale-price edit logs
old price + new price + date to the «تاریخچهٔ تغییر قیمت» sheet; (2)
daily, items at/below minimum stock are gathered into a Gmail *draft*
(never auto-sent) for review before sending. Explicitly not connected to
any real sheet; sheet names, column numbers and recipient email live in
one CONFIG block to be swapped for the real file. "Section by section":
CONFIG table (8 keys: `SHEET_PRODUCTS`, `SHEET_PRICE_LOG`, `PRICE_COL` 5,
`STOCK_COL` 6, `MIN_STOCK_COL` 7, `FIRST_DATA_ROW` 3 — row 1 title, row 2
headers — `REPORT_EMAIL`, `TIMEZONE` Asia/Tehran); `onOpen` custom menu
«مدیریت فروشگاه» with 2 items (manual price-change log, build low-stock
draft); `onEdit` auto-log with 6 guards (products sheet only; price
column only; data rows ≥ 3 only; single-row edits only; old price must
exist; new ≠ old); `logSelectedPriceChange` manual path (asks user for
old price); `sendLowStockReport` daily draft (table of code/name/stock/
min, no draft if nothing is low). Then the full code in a dark `<pre>`
block (verbatim `.gs` file), a 4-step install list (Extensions → Apps
Script → paste → set CONFIG → daily time trigger for
`sendLowStockReport`; `onEdit` needs no trigger), 4 honest notes
(draft-only, never auto-sent; Gregorian dates — Jalali needs a separate
library; formula/import price changes are not auto-logged, use manual;
not connected to a real sheet), and links (`apps-script-sample.gs`,
`price-inventory-preview.html`, `README.md`). Current problems: it reads
as a wall of prose + one very long code block; the two automations have
no visual identity (a reader cannot tell in 5 seconds what runs when);
the 6 `onEdit` guards are a bullet list that looks like fine print; the
code block is unlabelled dark text with no navigation.

1. **A flow diagram on top: what runs when (highest impact).** Before any
   prose, a 3-step horizontal flow (pure HTML/CSS, arrows between cards):
   **① ویرایش قیمت در شیت** → **② `onEdit` بررسی می‌کند** → **③ ردیف در
   تاریخچه ثبت می‌شود**, and a second parallel flow **① هر روز (تریگر
   زمانی)** → **② `sendLowStockReport` کالاهای کم را پیدا می‌کند** → **③
   پیش‌نویس در جیمیل ساخته می‌شود (ارسال نمی‌شود)**. Each step is a small
   card with the function name in monospace; the Gmail step gets an amber
   "پیش‌نویس، نه ارسال" tag — the single most important trust fact on the
   page, currently buried in paragraph 2. This is the Observable pipeline
   pattern (trigger → transform → output) and it answers the only
   question a prospective client asks first: *when does this run and what
   does it touch?*
2. **CONFIG table becomes a settings card with a "change only this"
   frame.** Restyle the 8-row table as a bordered settings panel with a
   header `فقط این بخش را عوض کنید` and group the rows: برگه‌ها
   (`SHEET_PRODUCTS`, `SHEET_PRICE_LOG`), ستون‌ها (`PRICE_COL 5`,
   `STOCK_COL 6`, `MIN_STOCK_COL 7`, `FIRST_DATA_ROW 3`), گزارش
   (`REPORT_EMAIL`, `TIMEZONE`). Column numbers get a visual anchor: a
   mini sheet-grid sketch (7 columns × 3 rows, the price/stock/min
   columns highlighted, row 3 marked "اولین ردیف داده") so `PRICE_COL: 5`
   is not an abstract number. Code names stay monospace LTR; Persian
   meanings stay 14px.
3. **The 6 `onEdit` guards become a guard checklist, not bullets.** Six
   rows, each with a ✓/✗-style check glyph (not emoji), the guard in bold
   + one-line explanation: e.g. `فقط برگهٔ محصولات — ویرایش برگه‌های دیگر
   نادیده گرفته می‌شود`. Style it as a "safety" card with a green left
   accent — this is the feature the page is *selling* (it will not spam
   the log), so it deserves a card, not a `<ul>`. The manual path
   (`logSelectedPriceChange`) gets a small "when auto doesn't run"
   callout beside it: `قیمت با فرمول یا ایمپورت عوض شد ← ثبت دستی از منو`.
4. **Code block becomes a navigable code viewer.** Keep the verbatim code
   (it must stay identical to the `.gs` file), but wrap the dark `<pre>`
   in a viewer: header bar with filename `apps-script-sample.gs`, a copy
   button, and anchor links (`CONFIG` · `onOpen` · `onEdit` ·
   `logSelectedPriceChange` · `sendLowStockReport`) that jump-scroll
   within the block; add hand-coloured syntax spans for the five function
   names and the CONFIG keys only (minimal highlighting — full token
   colouring by hand is brittle; function names in blue `#60A5FA`,
   strings in green `#86EFAC`, comments already muted). Add line numbers
   in a muted gutter column (CSS counter, not in the copied text — copy
   must return the raw code). The install steps become a numbered
   timeline (①–④ with a vertical connector line) instead of a plain
   `<ol>`, and the 4 honest notes become a single "نکته‌های صادقانه"
   callout card with amber left accent — they are a selling point
   (honesty), not footnotes.
5. **Cross-links become a footer action row.** The three links (`.gs`
   file, inventory preview, README) become a row of action chips at the
   bottom of the page with the primary one (download `.gs`) filled blue.
   The existing footer line ("کد کامل این صفحه با فایل اسکریپت یکسان است")
   stays as the caption under that row — it is the verifiability claim.
6. **Motion.** Flow cards enter staggered `fadeUp 320ms`, `80ms` apart,
   arrows draw in after (`scaleX 0 → 1, 300ms, 200ms delay`). Guard
   checklist rows check in one by one on scroll into view (`opacity +
   translateX(4px) → 0, 250ms`, staggered `70ms` — subtle, like ticking
   items off). Code-viewer anchor jump: smooth scroll `300ms`. Copy
   button: `Copied ✓` feedback `200ms`, revert after `1,500ms`. Timeline
   steps: the connector line grows `height 0 → 100%, 500ms` on scroll
   into view. `prefers-reduced-motion`: flow appears complete, checklist
   fully checked, no smooth scroll (`scroll-behavior: auto`).

## Cross-page consistency checklist (for the implementer)

- [ ] All four report pages share the §R0 tokens (background, borders,
  text greys, blue `#2563EB`, green `#16A34A`, red `#DC2626`, amber
  `#D97706`); no page invents a new accent colour.
- [ ] Every number uses `tabular-nums`; every money figure keeps the same
  format (thousands separators, currency/unit suffix in the same position)
  as the source file.
- [ ] Status language is identical everywhere: موجود / نزدیک به حداقل /
  کمبود موجودی (inventory) and the price-report direction colours mean
  the same thing on both asset cards.
- [ ] No external assets: Vazirmatn is already self-hosted in
  `web/assets/fonts/`; all charts/diagrams are hand-built SVG + HTML/CSS;
  all motion is CSS + ~20 lines of vanilla JS (count-up,
  IntersectionObserver, filter).
- [ ] `prefers-reduced-motion` respected on every page; content is fully
  legible with animations disabled or JS off (final values are the
  default state).
- [ ] Mobile: KPI grids collapse 4 → 2 → 1; tables keep `.table-wrap`
  horizontal scroll with sticky header; the 9-column products table never
  forces page-level horizontal scroll.

---

## What was deliberately not done

- **No HTML/CSS was edited.** This is direction only; wiring starts after
  Marshall reviews it.
- **No new icon set.** Swapping Heroicons for another generic stroke set
  would repeat the mistake the SVGs were retired for.
- **No decorative background patterns.** The photography carries the
  pages; patterns were not sourced (licensing/extraction friction).
- **No logo marquee on Corelia** — flagged as the common fintech tell.
- **No fly-to-cart animation** on the store pages — documented in the
  motion research as not recommended for these static pages.
- **No count-up on typing** in either calculator — count-up only on
  Calculate press, from the previous value.
- **No parallax, no scroll-jacking, no scrubbed/pinned scenes** anywhere.
- **No fabricated data:** the decision-tree diagram shows root + two
  leaves only (the file documents nothing deeper); the report numbers are
  the files' own numbers.
- **Arc as a live brand** was not copied (it sunsets 22 Dec 2026); only
  its historic "Spaces" layout pattern is borrowed for Wayfinder.
- **Stripe's rainbow gradient** was not copied onto the industrial page
  (borrow structure, recolour); **Lando/Bulgari maximalism** was not
  applied to distributor homepages; **Penelope Care's disabled
  pinch-zoom** was not copied.

## Gaps (said plainly)

- **Wayfinder second image:** not found to the bar. One strong hero
  suffices.
- **Corporate modern hero:** no good modern substation/transformer photo
  found. Switchgear + archival hall cover the page; a fresh Pexels
  search ("industrial electrician") could run in a later round.
- **Distinctive SVG:** none sourced anywhere. A vector set would need to
  be custom-drawn.
- **Product-photo gaps (Track 2, unchanged):** Sony XM5 (id 5) and
  De'Longhi Dedica (id 9) — retry the Flickr URLs from a different IP;
  the Sony file must be used unmodified if obtained (CC BY-ND).
- **Colour hex, typography scale, spacing and micro-interactions for the
  Iranian exemplars** could not be verified from text fetches (Digikala
  homepage unfetchable; Divar homepage unfetchable) — the Iranian
  patterns above are structural, not token-level.
- **Stripe/Linear numbers** are consensus values from scraped snapshots
  and research playbooks, not their production stylesheets; **Arc
  durations** could not be sourced; **RTL mirroring notes** are
  recommendations, not sourced guidance.
- **Motion research caveat:** the per-page motion specs in this document
  are grounded in the motion-research report's consensus values; test in
  DevTools emulation + once on a real device before calling them done.

## Open questions for Marshall

**Decided 2026-11-10 ~22:02:** (1) KEEP the 1936 B&W factory hall;
(2) DROP the pylon; (3) DROP the index cover image — type carries the
index; (4) vegetable-market photo ACCEPTABLE (small tent logo remains);
(5) Canary Wharf hero for Corelia; (6) no SVG restorations;
(7) stores first (done).

1. **Heritage tone on corporate?** ~~Keep the 1936 B&W factory hall in
   «داستان ما», or drop it and let `switchgear.jpg` carry the page alone?~~
   **Decided: KEEP.**
2. **Pylon as abstract art?** ~~Is the B&W bridge pylon acceptable as a
   dark section background on the corporate page (never captioned as
   electrical), or should it be dropped?~~ **Decided: DROP.**
3. **Index cover image?** ~~`workspace-minimal.jpg` is the weakest keeper
   (a familiar flat-lay) — keep it, or drop it and let the type carry the
   index page?~~ **Decided: DROP — type carries the index.**
4. **Vegetable-market crop:** the "$2.00" chalkboard is cropped out; a
   small "marquee" tent logo remains top-centre. ~~Acceptable, or drop the
   third diet image?~~ **Decided: ACCEPTABLE.**
5. **Corelia hero:** ~~Canary Wharf at dusk as the fintech hero — or would
   he rather the settlement preview carry the hero alone with no photo?~~
   **Decided: Canary Wharf hero.**
6. **Retired SVGs:** the 39 SVGs are moved to
   `hidden_files/retired-graphics-2026-11-10/` (recoverable, not
   deleted). ~~Any he wants restored?~~ **Decided: no restorations.**
7. **Wiring order:** ~~which page first when the direction is approved —
   the two stores (product photos already live), or corporate/Corelia?~~
   **Decided: stores first (done).**
