=== Dozabaneh ===
Contributors: rezamhr2
Tags: bilingual, rtl-language-support, custom-menu, featured-images, custom-logo, threaded-comments, translation-ready, blog, e-commerce
Requires at least: 6.0
Tested up to: 6.7
Requires PHP: 7.4
Stable tag: 1.0.0
License: GPLv2 or later
License URI: http://www.gnu.org/licenses/gpl-2.0.html

A clean bilingual business theme for WordPress — Persian and English, correct RTL, Jalali dates, custom post types for services and portfolio, and basic WooCommerce support.

== Description ==

Dozabaneh (دوزبانه = "bilingual") is a business theme built for sites that speak two languages. It ships with:

* Full RTL support through logical CSS properties — one stylesheet, both directions.
* Jalali dates everywhere posts are dated (a tested Gregorian-to-Jalali converter in `inc/jalali.php`, verified against known anchors: 2026-03-21 = 1405-01-01, 2026-11-12 = 1405-08-21), including the Jalali year in the footer copyright.
* Custom post types: Services and Portfolio, shown on the front page.
* Customizer settings for contact details (top bar) and hero text (front page).
* Basic WooCommerce support (`add_theme_support( 'woocommerce' )` + a `woocommerce.php` wrapper).
* A front page with hero, services, portfolio, latest news, stats and a call-to-action band; blog index, single post, page, archive, search and 404 templates; one widget area; threaded comments.

A static preview of the theme's design is in the portfolio pack at `web/wordpress/` (Persian) and `web/wordpress-intl/` (English).

== Installation ==

1. Copy the `dozabaneh` folder into `wp-content/themes/`.
2. In WordPress admin, go to Appearance → Themes and activate Dozabaneh.
3. Set a static front page (Settings → Reading) or leave the blog as the home page.
4. Add Services and Portfolio items; set contact details and hero text in Appearance → Customize.
5. Optional: install WooCommerce — the theme wraps shop pages in its own layout automatically.

== Changelog ==

= 1.0.0 =
* First release.
