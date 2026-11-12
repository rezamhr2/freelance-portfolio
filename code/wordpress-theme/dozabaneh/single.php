<?php
/**
 * Single post template: Jalali date + categories + tags + comments.
 *
 * @package Dozabaneh
 */

get_header();
?>

<section class="section">
  <div class="container layout">
    <article class="post">
      <?php
      while ( have_posts() ) :
        the_post();
        ?>
        <h1 class="entry-title"><?php the_title(); ?></h1>
        <p class="entry-meta">
          <time datetime="<?php echo esc_attr( get_the_date( 'c' ) ); ?>"><?php dozabaneh_the_jalali_date(); ?></time>
          <?php
          /* Translators: %s = author name. */
          printf( ' · ' . esc_html__( 'by %s', 'dozabaneh' ), esc_html( get_the_author() ) );
          ?>
        </p>
        <?php
        if ( has_post_thumbnail() ) :
          the_post_thumbnail( 'large' );
        endif;
        the_content();
        wp_link_pages();
        ?>
        <p class="entry-meta">
          <?php the_category( ', ' ); ?>
          <?php the_tags( ' · ', ', ' ); ?>
        </p>
        <?php
        if ( comments_open() || get_comments_number() ) :
          comments_template();
        endif;
      endwhile;
      ?>
    </article>
    <?php get_sidebar(); ?>
  </div>
</section>

<?php
get_footer();
