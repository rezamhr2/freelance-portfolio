<?php
/**
 * 404 template.
 *
 * @package Dozabaneh
 */

get_header();
?>

<section class="section">
  <div class="container">
    <h2 class="section-title"><?php esc_html_e( 'Page not found', 'dozabaneh' ); ?></h2>
    <p><?php esc_html_e( 'The page you are looking for does not exist, or it has moved.', 'dozabaneh' ); ?></p>
    <?php get_search_form(); ?>
    <p><a class="btn" href="<?php echo esc_url( home_url( '/' ) ); ?>"><?php esc_html_e( 'Back to home', 'dozabaneh' ); ?></a></p>
  </div>
</section>

<?php
get_footer();
