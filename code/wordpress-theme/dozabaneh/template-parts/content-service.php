<?php
/**
 * Service card (front page services grid + service archive).
 *
 * @package Dozabaneh
 */
?>

<div class="card">
  <?php if ( has_post_thumbnail() ) : ?>
    <a href="<?php the_permalink(); ?>"><?php the_post_thumbnail( 'medium' ); ?></a>
  <?php endif; ?>
  <h3><a href="<?php the_permalink(); ?>"><?php the_title(); ?></a></h3>
  <p><?php the_excerpt(); ?></p>
</div>
