<?php
/**
 * Comments template.
 *
 * @package Dozabaneh
 */

if ( post_password_required() ) {
    return;
}
?>

<div class="comments-area">
  <?php if ( have_comments() ) : ?>
    <h3>
      <?php
      printf(
        /* Translators: %s = number of comments. */
        esc_html( _nx( '%s comment', '%s comments', get_comments_number(), 'comments title', 'dozabaneh' ) ),
        esc_html( number_format_i18n( get_comments_number() ) )
      );
      ?>
    </h3>
    <ol class="comment-list">
      <?php
      wp_list_comments(
        array(
          'style'       => 'ol',
          'short_ping'  => true,
          'avatar_size' => 48,
        )
      );
      ?>
    </ol>
    <?php the_comments_pagination(); ?>
  <?php endif; ?>

  <?php if ( ! comments_open() && get_comments_number() ) : ?>
    <p><?php esc_html_e( 'Comments are closed.', 'dozabaneh' ); ?></p>
  <?php endif; ?>

  <?php comment_form(); ?>
</div>
