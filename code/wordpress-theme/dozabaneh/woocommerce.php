<?php
/**
 * WooCommerce wrapper: shop pages inside the theme's layout.
 * Basic WooCommerce support is declared in functions.php.
 *
 * @package Dozabaneh
 */

get_header();
?>

<section class="section">
  <div class="container">
    <?php woocommerce_content(); ?>
  </div>
</section>

<?php
get_footer();
