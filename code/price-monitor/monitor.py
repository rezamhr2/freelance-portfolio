# monitor.py — نمونه کار: پایش قیمت بازار و هشدار عبور از آستانه
#
# منبع پیش‌فرض: ای‌پی‌آی عمومی کوین‌گکو (بدون کلید، بدون ثبت‌نام).
# هیچ سایتی اسکرپ نمی‌شود؛ فقط یک ای‌پی‌آی عمومی خوانده می‌شود.
# حالت نمایشی (--demo) قیمت‌ها را از فایل محلی demo_prices.json می‌خواند و
# بدون اینترنت هم کار می‌کند.
#
# اجرا:
#   python3 monitor.py              # یک بار بررسی با API واقعی
#   python3 monitor.py --demo       # بررسی با داده‌ی نمایشی محلی
#   python3 monitor.py --loop 60    # بررسی هر ۶۰ ثانیه (Ctrl+C برای توقف)
#
# برای اتصال به منبع دیگر، فقط تابع fetch_prices و فایل config.json را عوض کنید
# (راهنما در README.md).

import argparse
import json
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
CONFIG_PATH = BASE_DIR / "config.json"
DEMO_PATH = BASE_DIR / "demo_prices.json"

COINGECKO_URL = (
    "https://api.coingecko.com/api/v3/simple/price"
    "?ids={ids}&vs_currencies=usd"
)


def load_config(path: Path = CONFIG_PATH) -> dict:
    """خواندن تنظیمات (ارزها و آستانه‌ها) از config.json"""
    with open(path, encoding="utf-8") as f:
        config = json.load(f)
    if not config.get("coins"):
        raise ValueError("config.json باید حداقل یک ارز در coins داشته باشد.")
    return config


def fetch_prices_live(coin_ids: list[str]) -> dict[str, float]:
    """گرفتن قیمت لحظه‌ای از ای‌پی‌آی عمومی کوین‌گکو (دلار)."""
    url = COINGECKO_URL.format(ids=",".join(coin_ids))
    request = urllib.request.Request(url, headers={"User-Agent": "price-monitor-demo/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            data = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        print(f"خطای سرور از کوین‌گکو: {exc.code} {exc.reason}", file=sys.stderr)
        raise SystemExit(1)
    except urllib.error.URLError as exc:
        print(f"خطای اتصال به کوین‌گکو: {exc.reason}", file=sys.stderr)
        raise SystemExit(1)
    prices = {}
    for coin_id in coin_ids:
        entry = data.get(coin_id)
        if entry and "usd" in entry:
            prices[coin_id] = float(entry["usd"])
    return prices


def fetch_prices_demo() -> dict[str, float]:
    """خواندن قیمت‌های نمایشی از فایل محلی (بدون اینترنت)."""
    with open(DEMO_PATH, encoding="utf-8") as f:
        data = json.load(f)
    return {coin: float(info["usd"]) for coin, info in data.items()}


def check_thresholds(prices: dict[str, float], config: dict) -> list[str]:
    """مقایسه‌ی قیمت‌ها با آستانه‌ها و ساخت پیام هشدار."""
    alerts = []
    thresholds = config.get("thresholds_usd", {})
    for coin_id, price in prices.items():
        limit = thresholds.get(coin_id)
        if limit is None:
            continue
        if price >= float(limit):
            alerts.append(
                f"🚨 هشدار: قیمت {coin_id} برابر ${price:,.2f} است "
                f"و از آستانه‌ی ${float(limit):,.2f} عبور کرده است."
            )
        else:
            print(f"ℹ️ {coin_id}: ${price:,.2f} — زیر آستانه‌ی ${float(limit):,.2f}")
    return alerts


def run_once(demo: bool = False) -> int:
    """یک دور بررسی؛ اگر هشدار بود ۱ برمی‌گرداند، وگرنه ۰."""
    config = load_config()
    coin_ids = list(config["coins"])
    prices = fetch_prices_demo() if demo else fetch_prices_live(coin_ids)
    if not prices:
        print("هیچ قیمتی دریافت نشد.", file=sys.stderr)
        return 2
    print("قیمت‌های دریافتی:")
    for coin_id, price in prices.items():
        print(f"  {coin_id}: ${price:,.2f}")
    alerts = check_thresholds(prices, config)
    for alert in alerts:
        print(alert)
    if alerts:
        print(f"تعداد هشدارها: {len(alerts)}")
        return 1
    print("هیچ هشداری نیست.")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(description="پایش قیمت و هشدار عبور از آستانه")
    parser.add_argument("--demo", action="store_true", help="استفاده از داده‌ی نمایشی محلی")
    parser.add_argument("--loop", type=int, default=0, metavar="SECONDS",
                        help="تکرار بررسی هر N ثانیه (۰ یعنی فقط یک بار)")
    args = parser.parse_args()

    if args.loop and args.loop > 0:
        print(f"پایش دوره‌ای هر {args.loop} ثانیه شروع شد (توقف با Ctrl+C).")
        try:
            while True:
                run_once(demo=args.demo)
                print("---")
                time.sleep(args.loop)
        except KeyboardInterrupt:
            print("پایش متوقف شد.")
            return
    else:
        sys.exit(run_once(demo=args.demo))


if __name__ == "__main__":
    main()
