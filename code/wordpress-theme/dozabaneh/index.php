<?php
/**
 * Blog index: post loop with Jalali dates + sidebar.
 *
 * @package Dozabaneh
 */

get_header();
?>

<section class="section">
  <div class="container layout">
    <div>
      <h2 class="section-title"><?php esc_html_e( 'News', 'dozabaneh' ); ?></h2>
      <?php if ( have_posts() ) : ?>
        <?php
        while ( have_posts() ) :
          the_post();
          get_template_part( 'template-parts/content', get_post_format() );
        endwhile;
        ?>
        <nav class="pagination" aria-label="<?php esc_attr_e( 'Posts navigation', 'dozabaneh' ); ?>">
          <?php the_posts_pagination(); ?>
        </nav>
      <?php else : ?>
        <p><?php esc_html_e( 'Nothing here yet.', 'dozabaneh' ); ?></p>
      <?php endif; ?>
    </div>
    <?php get_sidebar(); ?>
  </div>
</section>

<?php
get_footer();
