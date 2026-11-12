<?php
/**
 * Jalali (Persian) calendar helpers for the Dozabaneh theme.
 *
 * Gregorian -> Jalali conversion, 33-year cycle algorithm.
 * Verified against known anchors: 2026-03-21 = 1405-01-01 (Nowruz 1405),
 * 2026-11-12 = 1405-08-21, 2025-12-22 = 1404-10-01, 2024-03-20 = 1403-01-01.
 *
 * @package Dozabaneh
 */

if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

/**
 * Convert a Gregorian date to Jalali.
 *
 * @param int $gy Gregorian year.
 * @param int $gm Gregorian month (1-12).
 * @param int $gd Gregorian day (1-31).
 * @return array [ Jalali year, month, day ].
 */
function dozabaneh_gregorian_to_jalali( $gy, $gm, $gd ) {
    $g_d_m = array( 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334 );
    $gy2   = ( $gm > 2 ) ? ( $gy + 1 ) : $gy;
    $days  = 355666 + ( 365 * $gy ) + (int) ( ( $gy2 + 3 ) / 4 ) - (int) ( ( $gy2 + 99 ) / 100 ) + (int) ( ( $gy2 + 399 ) / 400 ) + $gd + $g_d_m[ $gm - 1 ];
    $jy    = -1595 + ( 33 * (int) ( $days / 12053 ) );
    $days  = $days % 12053;
    $jy   += 4 * (int) ( $days / 1461 );
    $days  = $days % 1461;
    if ( $days > 365 ) {
        $jy  += (int) ( ( $days - 1 ) / 365 );
        $days = ( $days - 1 ) % 365;
    }
    if ( $days < 186 ) {
        $jm = 1 + (int) ( $days / 31 );
        $jd = 1 + ( $days % 31 );
    } else {
        $jm = 7 + (int) ( ( $days - 186 ) / 30 );
        $jd = 1 + ( ( $days - 186 ) % 30 );
    }
    return array( $jy, $jm, $jd );
}

/**
 * Persian month names.
 *
 * @return array Month number (1-12) => name.
 */
function dozabaneh_jalali_months() {
    return array(
        1  => 'فروردین',
        2  => 'اردیبهشت',
        3  => 'خرداد',
        4  => 'تیر',
        5  => 'مرداد',
        6  => 'شهریور',
        7  => 'مهر',
        8  => 'آبان',
        9  => 'آذر',
        10 => 'دی',
        11 => 'بهمن',
        12 => 'اسفند',
    );
}

/**
 * Format a date as Jalali, e.g. "۲۱ آبان ۱۴۰۵".
 *
 * @param string $format Use 'Y' (year), 'm' (month number), 'F' (month name), 'd' (day). Default: 'j F Y'.
 * @param int|null $timestamp Unix timestamp. Default: now.
 * @param bool $persian_digits Convert digits to Persian (۰-۹). Default: true.
 * @return string Formatted Jalali date.
 */
function dozabaneh_jalali_date( $format = 'j F Y', $timestamp = null, $persian_digits = true ) {
    if ( null === $timestamp ) {
        $timestamp = time();
    }
    list( $jy, $jm, $jd ) = dozabaneh_gregorian_to_jalali(
        (int) gmdate( 'Y', $timestamp ),
        (int) gmdate( 'n', $timestamp ),
        (int) gmdate( 'j', $timestamp )
    );
    $months = dozabaneh_jalali_months();
    $out    = str_replace(
        array( 'Y', 'm', 'F', 'j', 'd' ),
        array( $jy, str_pad( $jm, 2, '0', STR_PAD_LEFT ), $months[ $jm ], $jd, str_pad( $jd, 2, '0', STR_PAD_LEFT ) ),
        $format
    );
    if ( $persian_digits ) {
        $out = str_replace(
            array( '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' ),
            array( '۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹' ),
            $out
        );
    }
    return $out;
}

/**
 * Template tag: print the current post's date in Jalali.
 */
function dozabaneh_the_jalali_date() {
    echo esc_html( dozabaneh_jalali_date( 'j F Y', get_the_time( 'U' ) ) );
}
