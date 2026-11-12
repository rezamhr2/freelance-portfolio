<?php
/**
 * Search results template.
 *
 * @package Dozabaneh
 */

get_header();
?>

<section class="section">
  <div class="container layout">
    <div>
      <h2 class="section-title">
        <?php
        /* Translators: %s = search query. */
        printf( esc_html__( 'Search results for: %s', 'dozabaneh' ), '<span>' . esc_html( get_search_query() ) . '</span>' );
        ?>
      </h2>
      <?php if ( have_posts() ) : ?>
        <?php
        while ( have_posts() ) :
          the_post();
          get_template_part( 'template-parts/content', get_post_type() );
        endwhile;
        ?>
        <nav class="pagination" aria-label="<?php esc_attr_e( 'Posts navigation', 'dozabaneh' ); ?>">
          <?php the_posts_pagination(); ?>
        </nav>
      <?php else : ?>
        <p><?php esc_html_e( 'Nothing matched your search. Try different words.', 'dozabaneh' ); ?></p>
        <?php get_search_form(); ?>
      <?php endif; ?>
    </div>
    <?php get_sidebar(); ?>
  </div>
</section>

<?php
get_footer();
