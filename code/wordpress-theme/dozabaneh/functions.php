<?php
/**
 * Dozabaneh theme functions.
 *
 * A clean bilingual business theme: Persian + English, correct RTL,
 * Jalali dates, custom post types for services and portfolio,
 * and basic WooCommerce support.
 *
 * @package Dozabaneh
 */

if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

require get_template_directory() . '/inc/jalali.php';

/**
 * Theme setup: title tag, thumbnails, menus, logo, HTML5, WooCommerce.
 */
function dozabaneh_setup() {
    add_theme_support( 'title-tag' );
    add_theme_support( 'post-thumbnails' );
    add_theme_support( 'custom-logo' );
    add_theme_support( 'automatic-feed-links' );
    add_theme_support( 'customize-selective-refresh-widgets' );
    add_theme_support(
        'html5',
        array( 'search-form', 'comment-form', 'comment-list', 'gallery', 'caption', 'style', 'script' )
    );
    // Basic WooCommerce support: the theme wraps shop pages in its own layout (see woocommerce.php).
    add_theme_support( 'woocommerce' );

    register_nav_menus(
        array(
            'primary' => __( 'Primary menu', 'dozabaneh' ),
            'footer'  => __( 'Footer menu', 'dozabaneh' ),
        )
    );

    load_theme_textdomain( 'dozabaneh', get_template_directory() . '/languages' );
}
add_action( 'after_setup_theme', 'dozabaneh_setup' );

/**
 * Enqueue the stylesheet and the Vazirmatn font (Persian + Latin).
 */
function dozabaneh_scripts() {
    wp_enqueue_style( 'dozabaneh-vazirmatn', 'https://fonts.googleapis.com/css2?family=Vazirmatn:wght@100..900&display=swap', array(), null );
    wp_enqueue_style( 'dozabaneh-style', get_stylesheet_uri(), array( 'dozabaneh-vazirmatn' ), wp_get_theme()->get( 'Version' ) );
}
add_action( 'wp_enqueue_scripts', 'dozabaneh_scripts' );

/**
 * Content width, for embeds.
 */
function dozabaneh_content_width() {
    $GLOBALS['content_width'] = 1080;
}
add_action( 'after_setup_theme', 'dozabaneh_content_width', 0 );

/**
 * Register the Services and Portfolio custom post types.
 */
function dozabaneh_register_post_types() {
    register_post_type(
        'service',
        array(
            'labels'       => array(
                'name'          => __( 'Services', 'dozabaneh' ),
                'singular_name' => __( 'Service', 'dozabaneh' ),
            ),
            'public'       => true,
            'has_archive'  => true,
            'menu_icon'    => 'dashicons-hammer',
            'supports'     => array( 'title', 'editor', 'thumbnail', 'excerpt' ),
            'show_in_rest' => true,
        )
    );
    register_post_type(
        'portfolio',
        array(
            'labels'       => array(
                'name'          => __( 'Portfolio', 'dozabaneh' ),
                'singular_name' => __( 'Portfolio item', 'dozabaneh' ),
            ),
            'public'       => true,
            'has_archive'  => true,
            'menu_icon'    => 'dashicons-portfolio',
            'supports'     => array( 'title', 'editor', 'thumbnail', 'excerpt' ),
            'show_in_rest' => true,
        )
    );
}
add_action( 'init', 'dozabaneh_register_post_types' );

/**
 * One widget area, shown in the sidebar.
 */
function dozabaneh_widgets_init() {
    register_sidebar(
        array(
            'name'          => __( 'Sidebar', 'dozabaneh' ),
            'id'            => 'sidebar-1',
            'before_widget' => '<section class="widget %2$s">',
            'after_widget'  => '</section>',
            'before_title'  => '<h3 class="widget-title">',
            'after_title'   => '</h3>',
        )
    );
}
add_action( 'widgets_init', 'dozabaneh_widgets_init' );

/**
 * Customizer: contact details (top bar) and hero text (front page).
 */
function dozabaneh_customize_register( $wp_customize ) {
    $wp_customize->add_section(
        'dozabaneh_contact',
        array(
            'title'    => __( 'Contact details', 'dozabaneh' ),
            'priority' => 30,
        )
    );
    foreach ( array( 'phone', 'email' ) as $field ) {
        $wp_customize->add_setting(
            'dozabaneh_' . $field,
            array(
                'default'           => '',
                'sanitize_callback' => 'sanitize_text_field',
            )
        );
        $wp_customize->add_control(
            'dozabaneh_' . $field,
            array(
                'label'   => ( 'phone' === $field ) ? __( 'Phone', 'dozabaneh' ) : __( 'Email', 'dozabaneh' ),
                'section' => 'dozabaneh_contact',
                'type'    => 'text',
            )
        );
    }

    $wp_customize->add_section(
        'dozabaneh_hero',
        array(
            'title'    => __( 'Hero (front page)', 'dozabaneh' ),
            'priority' => 31,
        )
    );
    foreach ( array( 'hero_title', 'hero_text' ) as $field ) {
        $wp_customize->add_setting(
            'dozabaneh_' . $field,
            array(
                'default'           => '',
                'sanitize_callback' => 'sanitize_text_field',
            )
        );
        $wp_customize->add_control(
            'dozabaneh_' . $field,
            array(
                'label'   => ( 'hero_title' === $field ) ? __( 'Hero title', 'dozabaneh' ) : __( 'Hero text', 'dozabaneh' ),
                'section' => 'dozabaneh_hero',
                'type'    => ( 'hero_title' === $field ) ? 'text' : 'textarea',
            )
        );
    }
}
add_action( 'customize_register', 'dozabaneh_customize_register' );

/**
 * Shorter excerpts, ending with an ellipsis.
 */
function dozabaneh_excerpt_length() {
    return 24;
}
add_filter( 'excerpt_length', 'dozabaneh_excerpt_length' );

function dozabaneh_excerpt_more() {
    return ' …';
}
add_filter( 'excerpt_more', 'dozabaneh_excerpt_more' );
