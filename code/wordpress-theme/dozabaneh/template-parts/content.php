<?php
/**
 * Default post card (blog loop, archives, search).
 *
 * @package Dozabaneh
 */
?>

<article id="post-<?php the_ID(); ?>" <?php post_class( 'post' ); ?>>
  <?php if ( has_post_thumbnail() ) : ?>
    <a href="<?php the_permalink(); ?>"><?php the_post_thumbnail( 'medium' ); ?></a>
  <?php endif; ?>
  <h3 class="entry-title"><a href="<?php the_permalink(); ?>"><?php the_title(); ?></a></h3>
  <p class="entry-meta">
    <time datetime="<?php echo esc_attr( get_the_date( 'c' ) ); ?>"><?php dozabaneh_the_jalali_date(); ?></time>
  </p>
  <div class="entry-summary">
    <?php the_excerpt(); ?>
  </div>
  <p><a href="<?php the_permalink(); ?>"><?php esc_html_e( 'Read more', 'dozabaneh' ); ?> ←</a></p>
</article>
