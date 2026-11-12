<?php
/**
 * Single page template.
 *
 * @package Dozabaneh
 */

get_header();
?>

<section class="section">
  <div class="container layout">
    <div class="page-content">
      <?php
      while ( have_posts() ) :
        the_post();
        ?>
        <h1 class="entry-title"><?php the_title(); ?></h1>
        <?php
        if ( has_post_thumbnail() ) :
          the_post_thumbnail( 'large' );
        endif;
        the_content();
        wp_link_pages();
        if ( comments_open() || get_comments_number() ) :
          comments_template();
        endif;
      endwhile;
      ?>
    </div>
    <?php get_sidebar(); ?>
  </div>
</section>

<?php
get_footer();
