<?php
/**
 * Front page: hero (Customizer) + services + portfolio + latest news (Jalali dates) + call to action.
 *
 * @package Dozabaneh
 */

get_header();
?>

<section class="hero">
  <div class="container">
    <h1><?php echo esc_html( get_theme_mod( 'dozabaneh_hero_title', get_bloginfo( 'name' ) ) ); ?></h1>
    <p><?php echo esc_html( get_theme_mod( 'dozabaneh_hero_text', get_bloginfo( 'description' ) ) ); ?></p>
    <a class="btn" href="<?php echo esc_url( get_post_type_archive_link( 'service' ) ); ?>"><?php esc_html_e( 'Our services', 'dozabaneh' ); ?></a>
    <a class="btn btn-ghost" href="<?php echo esc_url( get_permalink( get_option( 'page_for_posts' ) ) ); ?>"><?php esc_html_e( 'Latest news', 'dozabaneh' ); ?></a>
  </div>
</section>

<section class="section">
  <div class="container">
    <h2 class="section-title"><?php esc_html_e( 'Services', 'dozabaneh' ); ?></h2>
    <p class="section-sub"><?php esc_html_e( 'What we do, in one place.', 'dozabaneh' ); ?></p>
    <div class="cards">
      <?php
      $services = new WP_Query(
        array(
          'post_type'      => 'service',
          'posts_per_page' => 3,
        )
      );
      if ( $services->have_posts() ) :
        while ( $services->have_posts() ) :
          $services->the_post();
          get_template_part( 'template-parts/content', 'service' );
        endwhile;
        wp_reset_postdata();
      endif;
      ?>
    </div>
  </div>
</section>

<section class="section stats-band">
  <div class="container">
    <div><b><?php echo esc_html( wp_count_posts( 'portfolio' )->publish ); ?></b><span><?php esc_html_e( 'Portfolio items', 'dozabaneh' ); ?></span></div>
    <div><b><?php echo esc_html( wp_count_posts( 'service' )->publish ); ?></b><span><?php esc_html_e( 'Services', 'dozabaneh' ); ?></span></div>
    <div><b><?php echo esc_html( wp_count_posts()->publish ); ?></b><span><?php esc_html_e( 'News posts', 'dozabaneh' ); ?></span></div>
    <div><b><?php echo esc_html( dozabaneh_jalali_date( 'Y' ) ); ?></b><span><?php esc_html_e( 'Jalali year', 'dozabaneh' ); ?></span></div>
  </div>
</section>

<section class="section">
  <div class="container">
    <h2 class="section-title"><?php esc_html_e( 'Portfolio', 'dozabaneh' ); ?></h2>
    <p class="section-sub"><?php esc_html_e( 'Recent work.', 'dozabaneh' ); ?></p>
    <div class="cards">
      <?php
      $portfolio = new WP_Query(
        array(
          'post_type'      => 'portfolio',
          'posts_per_page' => 3,
        )
      );
      if ( $portfolio->have_posts() ) :
        while ( $portfolio->have_posts() ) :
          $portfolio->the_post();
          get_template_part( 'template-parts/content', get_post_type() );
        endwhile;
        wp_reset_postdata();
      endif;
      ?>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <h2 class="section-title"><?php esc_html_e( 'Latest news', 'dozabaneh' ); ?></h2>
    <p class="section-sub"><?php esc_html_e( 'Dates shown in Jalali.', 'dozabaneh' ); ?></p>
    <?php
    $news = new WP_Query(
      array(
        'posts_per_page' => 3,
      )
    );
    if ( $news->have_posts() ) :
      while ( $news->have_posts() ) :
        $news->the_post();
        get_template_part( 'template-parts/content', get_post_format() );
      endwhile;
      wp_reset_postdata();
    endif;
    ?>
  </div>
</section>

<section class="section cta-band">
  <div class="container">
    <h2><?php esc_html_e( 'Ready to start?', 'dozabaneh' ); ?></h2>
    <p><?php esc_html_e( 'Tell us about your project — we reply within one working day.', 'dozabaneh' ); ?></p>
    <a class="btn" href="<?php echo esc_url( get_theme_mod( 'dozabaneh_email', '' ) ? 'mailto:' . get_theme_mod( 'dozabaneh_email', '' ) : home_url( '/' ) ); ?>"><?php esc_html_e( 'Contact us', 'dozabaneh' ); ?></a>
  </div>
</section>

<?php
get_footer();
