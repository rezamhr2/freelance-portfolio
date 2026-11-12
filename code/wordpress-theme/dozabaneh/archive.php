<?php
/**
 * Archive template: category, tag, date, and custom post type archives.
 *
 * @package Dozabaneh
 */

get_header();
?>

<section class="section">
  <div class="container layout">
    <div>
      <h2 class="section-title"><?php the_archive_title(); ?></h2>
      <?php the_archive_description( '<p class="section-sub">', '</p>' ); ?>
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
        <p><?php esc_html_e( 'Nothing here yet.', 'dozabaneh' ); ?></p>
      <?php endif; ?>
    </div>
    <?php get_sidebar(); ?>
  </div>
</section>

<?php
get_footer();
