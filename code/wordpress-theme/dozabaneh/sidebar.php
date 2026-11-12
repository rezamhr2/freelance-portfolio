<?php
/**
 * Sidebar: the one widget area, with a search form as fallback.
 *
 * @package Dozabaneh
 */

if ( ! is_active_sidebar( 'sidebar-1' ) ) {
    ?>
    <aside class="widget-area">
      <section class="widget">
        <h3 class="widget-title"><?php esc_html_e( 'Search', 'dozabaneh' ); ?></h3>
        <?php get_search_form(); ?>
      </section>
    </aside>
    <?php
    return;
}
?>
<aside class="widget-area">
  <?php dynamic_sidebar( 'sidebar-1' ); ?>
</aside>
