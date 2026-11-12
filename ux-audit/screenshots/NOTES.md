# tehranjanebi.com — screenshot + measurement notes

Captured 2026-11-10 (Tue ~20:15–20:20 Tehran) in the
sandbox. Read-only: no sign-in, no purchase, no personal data. Cart reached
at /cart without logging in; checkout steps past the cart were NOT tested
(they need items in the cart and a login).

Method note: the sandbox reaches the internet through an egress proxy, so the
load times below are indicative, not absolute — a direct connection will
differ. The first capture attempt timed out on the homepage (cold proxy);
the numbers below are from the clean second run. Overflow was measured
after full render: `document.documentElement.scrollWidth` vs `innerWidth`.

## Files (23)

Viewport (top of page) + full-page shots for every page, desktop 1280px and
mobile 390px, plus the search-suggestion attempt and the raw numbers:

- desktop-home.png / desktop-home-full.png
- desktop-category-glass.png / desktop-category-glass-full.png
- desktop-product-glass.png / desktop-product-glass-full.png
- desktop-search-glass.png / desktop-search-glass-full.png
- desktop-search-glass-dropdown.png (typed "گلس", waited 1.5s)
- desktop-cart.png / desktop-cart-full.png
- mobile-home.png / mobile-home-full.png
- mobile-category-glass.png / mobile-category-glass-full.png
- mobile-product-glass.png / mobile-product-glass-full.png
- mobile-search-glass.png / mobile-search-glass-full.png
- mobile-search-glass-dropdown.png
- mobile-cart.png / mobile-cart-full.png
- measurements.json (all numbers, console errors, failed requests)

Pages: home https://tehranjanebi.com/ · category
/product-category/Phone-screen-protector/ (محافظ صفحه گلس, from the homepage
nav) · product /product/wotaer-stenciled-mobile-glass/ (first product in the
category) · search /search?string=گلس (typed in the search box, Enter) ·
cart /cart (direct URL, no login needed).

## Load times (loadEvent, seconds)

| Page | Desktop 1280 | Mobile 390 |
|---|---|---|
| Home | 4.5 | 3.5 |
| Category (glass) | 1.8 | 1.9 |
| Product (WOTAER glass) | 4.2 | 4.0 |
| Search "گلس" | 2.0 | 1.8 |
| Cart | 1.5 | 1.3 |

Slowest single resources: product-gallery JPGs 1.7–2.4 s each; a Yektanet
analytics request took 8.6 s on desktop search. The homepage carries
175 images (desktop) / 119 (mobile). The page never reaches network idle:
third-party requests (Enamad/Samandehi badges, Yektanet, Goftino) stay
pending after load.

## Horizontal overflow at 390px

NONE. scrollWidth == innerWidth on every page at both widths (1280 and 390).
No horizontal scrolling anywhere.

## Console errors / failed requests

- 1 console error per viewport: `Failed to load resource:
  net::ERR_EMPTY_RESPONSE` (the Enamad seal).
- Failed requests, same on every page (desktop 33, mobile 10 — same
  resources, retried across pages):
  - 3 images from panel.tehranjanebi.com — **HTTP 404** (verified with curl):
    `2601669797549.png`, `6451669797819 - Copy.png`, `24071669797581.png`.
    Served as `text/html` + `nosniff`, so the browser ORB-blocks them.
  - Samandehi badge `logo.samandehi.ir/logo.aspx` — **HTTP 403**.
  - Enamad seal `trustseal.enamad.ir/logo.aspx` — **empty response**
    (ERR_EMPTY_RESPONSE / ERR_ABORTED).
  - Yektanet analytics `collect` calls — ERR_ABORTED (aborted on navigation,
    benign).

## Per-page visual observations

- **Home (desktop):** clean RTL header (hours Sat–Thu 9–19, gift/support
  links, orange login button, search, categories button, account/cart
  icons); red hero banner with rotating carousel (adapters, then flash/RAM);
  brand logo carousel (Tajis, ProOne, Pioneer, Oxygen, Earldom, Apple);
  category tiles, then product carousels (latest, discounted, bestsellers,
  cases, high-volume, shop equipment, RAM/flash, chargers); about text with
  "show more"; footer with two phone numbers, link columns, social icons.
- **Home (mobile):** single column, hamburger + account + cart icons,
  full-width search, two black pill buttons, hero scales down readably,
  brand carousel shows 2 at a time with names, category tiles below.
  Bottom sticky bar (Telegram/Instagram/WhatsApp) + orange chat button
  overlap page content slightly.
- **Category glass (both):** breadcrumb, title "خرید عمده محافظ صفحه
  نمایش (۲۸)", brand chips (Mietubl, بدون برند, Blva, Xiaomi), sub-category
  chips, sort dropdown, right sidebar with category list and counts.
  Product cards show a photo, title, "دوماه گارانتی تهران جانبی" badge and
  an orange "مشاهده قیمت همکار پس از ورود" button — **no prices are visible
  anywhere without logging in**. Count mismatch: title says 28 products,
  sidebar says محافظ صفحه گلس (۴۱).
- **Product WOTAER (both):** gallery (main photo + 3 thumbnails), feature
  list (easy install, stencil, anti-static, 9H hardness, HD), "wholesale
  only for colleagues" note, quantity-tier table whose price column reads
  "پس از ورود", variant table (model / code / stock / colour dropdown /
  quantity stepper / add-to-cart per row — iPhone 13–17 variants), long SEO
  description, similar-products carousel. No price and no working
  add-to-cart path is visible without login.
- **Search "گلس" (both):** results page works (`/search?string=گلس`),
  same card grid as the category page, title is just "محصولات" — no
  visible result count and no echo of the search term outside the search
  box. **No suggestion dropdown appeared within 1.5 s of typing** in the
  search box (dropdown screenshots show the plain homepage/hero).
- **Cart (both):** opens without login. Empty-cart state: dashed box
  "خرید خالی است!", totals all ۰ تومان, discount-code box, blue
  "ثبت سفارش" button, and the wholesale minimum-order rules text
  (minimum 6 million Toman + minimum 10 items; orders below are not
  reviewed; invoice confirmation via WhatsApp/SMS). **The Goftino support
  chat widget auto-opened and covered ~40% of the desktop cart page and
  most of the mobile cart width**, hiding the cart summary — it was not
  clicked, it opened by itself.
- **Home full page (desktop):** the 10 category tiles are **plain grey
  gradients with no photo** — they read as empty boxes. The footer shows
  a **broken-image icon for "logo-samandehi"** (the Samandehi badge does
  not render) and **no Enamad seal is visible anywhere in the footer**.
- **Product full page (desktop):** variant table is dense but usable;
  model names mix Persian digits with Latin ("iPhone ۱۳/۱۴ Pro/۱۴",
  "iPhone ۱۵/۱۶") inconsistently. Footer again shows the broken
  Samandehi logo.
- **Mobile product/search:** gallery and cards scale cleanly, single
  column, readable; the floating orange filter button (search) and the
  chat button overlap content edges but do not block reading.

## What this does NOT cover

- No login, so wholesale prices, the real add-to-cart flow, checkout,
  payment and order tracking were not exercised.
- Timings are sandbox-proxied; treat them as relative (home and product
  pages are the heaviest) rather than absolute.
- The Enamad/Samandehi failures were seen through the sandbox egress
  proxy; the 404s and the 403 are server-side responses, but badge
  behaviour from a real Iranian connection may differ — worth one
  re-check from Marshall's side.
