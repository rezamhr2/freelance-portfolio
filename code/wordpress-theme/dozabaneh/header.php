<?php
/**
 * Theme header: top bar (contact details from the Customizer) + site header + primary menu.
 *
 * @package Dozabaneh
 */
?>
<!DOCTYPE html>
<html <?php language_attributes(); ?>>
<head>
<meta charset="<?php bloginfo( 'charset' ); ?>">
<meta name="viewport" content="width=device-width, initial-scale=1">
<?php wp_head(); ?>
</head>
<body <?php body_class(); ?>>
<?php wp_body_open(); ?>

<div class="topbar">
  <div class="container">
    <span><?php echo esc_html( get_theme_mod( 'dozabaneh_phone', '' ) ); ?></span>
    <span><a href="mailto:<?php echo esc_attr( get_theme_mod( 'dozabaneh_email', '' ) ); ?>"><?php echo esc_html( get_theme_mod( 'dozabaneh_email', '' ) ); ?></a></span>
  </div>
</div>

<header class="site-header">
  <div class="container">
    <div class="site-branding">
      <?php if ( has_custom_logo() ) : ?>
        <?php the_custom_logo(); ?>
      <?php endif; ?>
      <h1 class="site-title"><a href="<?php echo esc_url( home_url( '/' ) ); ?>"><?php bloginfo( 'name' ); ?></a></h1>
      <p class="site-description"><?php bloginfo( 'description' ); ?></p>
    </div>
    <nav class="main-nav" aria-label="<?php esc_attr_e( 'Primary menu', 'dozabaneh' ); ?>">
      <?php
      wp_nav_menu(
        array(
          'theme_location' => 'primary',
          'fallback_cb'    => 'wp_page_menu',
        )
      );
      ?>
    </nav>
  </div>
</header>

<main id="main">
