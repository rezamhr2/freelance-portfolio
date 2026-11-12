<?php
/**
 * Theme footer: footer menu + copyright with the current Jalali year.
 *
 * @package Dozabaneh
 */
?>
</main>

<footer class="site-footer">
  <div class="container">
    <nav class="footer-nav" aria-label="<?php esc_attr_e( 'Footer menu', 'dozabaneh' ); ?>">
      <?php
      wp_nav_menu(
        array(
          'theme_location' => 'footer',
          'fallback_cb'    => false,
        )
      );
      ?>
    </nav>
    <p class="site-info">
      <?php
      /* Translators: %1$s = site name, %2$s = current Jalali year. */
      printf( esc_html__( '© %2$s %1$s — All rights reserved.', 'dozabaneh' ), esc_html( get_bloginfo( 'name' ) ), esc_html( dozabaneh_jalali_date( 'Y' ) ) );
      ?>
    </p>
  </div>
</footer>

<?php wp_footer(); ?>
</body>
</html>
