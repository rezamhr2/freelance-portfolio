# report.py — نمونه کار: ساخت گزارش تاریخچه‌ی قیمت به صورت یک فایل اچ‌تی‌ام‌ال
#
# داده‌ها از فایل‌های نمایشی محلی خوانده می‌شوند (demo_history.json و
# demo_prices.json) و خروجی یک فایل اچ‌تی‌ام‌ال مستقل است: سی‌اس‌اس و نمودار
# اس‌وی‌جی و جاوااسکریپت، همه داخل خود فایل؛ بدون اینترنت هم باز می‌شود.
#
# اجرا:
#   python3 report.py              # ساخت report.html در همین پوشه
#   python3 report.py --output out.html   # ساخت فایل با نام دلخواه
#
# این ابزار فقط گزارش می‌سازد و به پایش زنده وصل نیست؛ پایش با monitor.py
# انجام می‌شود. هیچ ایمیلی واقعاً فرستاده نمی‌شود؛ پنل «قیمت دلخواه» فقط
# نمایشی است و تایید آن روی همان صفحه نشان داده می‌شود.

import argparse
import html
import json
from datetime import date
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
HISTORY_PATH = BASE_DIR / "demo_history.json"
DEMO_PATH = BASE_DIR / "demo_prices.json"

FA_DIGITS = str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")
FA_NAMES = {"bitcoin": "بیت‌کوین", "ethereum": "اتریوم"}

GREEN = "#16a34a"   # میانگین
BLUE = "#2563eb"    # کمترین قیمت
GREY = "#6b7280"    # بدون تغییر (خط‌چین)


def fa_num(value, decimals=0) -> str:
    """عدد با ارقام فارسی و جداکننده‌ی هزارگان."""
    text = f"{value:,.{decimals}f}"
    return text.translate(FA_DIGITS).replace(",", "٬")


def fa_date(iso: str) -> str:
    """تاریخ میلادی به صورت ۲۰۲۶/۱۱/۱۰ با ارقام فارسی."""
    year, month, day = iso.split("-")
    return f"{year}/{month}/{day}".translate(FA_DIGITS)


def load_history() -> dict:
    with open(HISTORY_PATH, encoding="utf-8") as f:
        return json.load(f)


def load_current() -> dict:
    with open(DEMO_PATH, encoding="utf-8") as f:
        return {coin: float(info["usd"]) for coin, info in json.load(f).items()}


def rolling_average(values: list[float], window: int = 7) -> list[float]:
    """میانگین متحرک؛ برای روزهای اول، میانگین روزهای موجود تا آن روز."""
    out = []
    for i in range(len(values)):
        start = max(0, i - window + 1)
        out.append(sum(values[start:i + 1]) / (i + 1 - start))
    return out


def stats_for(series: list[dict], current: float) -> dict:
    """کمترین / بیشترین / فعلی / میانگین، هر کدام با تاریخش."""
    values = [p["price"] for p in series]
    low_i = values.index(min(values))
    high_i = values.index(max(values))
    return {
        "lowest": (min(values), series[low_i]["date"]),
        "highest": (max(values), series[high_i]["date"]),
        "current": (current, series[-1]["date"]),
        "average": (sum(values) / len(values), f"{len(values)} روزه"),
    }


def svg_chart(series: list[dict], avg: list[float], coin: str, days: int) -> str:
    """نمودار اس‌وی‌جی: خط میانگین (سبز) و خط کمترین قیمت (آبی).

    جاهایی که قیمت روز نسبت به روز قبل عوض نشده، روی خط آبی با خط‌چین
    کشیده می‌شود و در راهنما هم با نماد خط‌چین «بدون تغییر» می‌آید.
    """
    points = series[-days:]
    avgs = avg[-days:]
    width, height = 760, 320
    pad_l, pad_r, pad_t, pad_b = 70, 16, 18, 34
    all_vals = [p["price"] for p in points] + avgs
    lo, hi = min(all_vals), max(all_vals)
    span = (hi - lo) or 1
    lo -= span * 0.08
    hi += span * 0.08

    def x(i: int) -> float:
        return pad_l + (width - pad_l - pad_r) * i / max(1, len(points) - 1)

    def y(v: float) -> float:
        return pad_t + (height - pad_t - pad_b) * (1 - (v - lo) / (hi - lo))

    def polyline(vals: list[float]) -> str:
        return " ".join(f"{x(i):.1f},{y(v):.1f}" for i, v in enumerate(vals))

    parts = [f'<svg viewBox="0 0 {width} {height}" role="img" '
             f'aria-label="نمودار تاریخچه‌ی قیمت {FA_NAMES.get(coin, coin)}" '
             f'xmlns="http://www.w3.org/2000/svg">']
    # خطوط راهنمای افقی با برچسب قیمت
    for k in range(5):
        val = lo + (hi - lo) * k / 4
        yy = y(val)
        parts.append(f'<line x1="{pad_l}" y1="{yy:.1f}" x2="{width - pad_r}" '
                     f'y2="{yy:.1f}" stroke="#e5e7eb" stroke-width="1"/>')
        parts.append(f'<text x="{pad_l - 8}" y="{yy + 4:.1f}" text-anchor="end" '
                     f'font-size="11" fill="#6b7280">${fa_num(val)}</text>')
    # برچسب تاریخ روی محور افقی (۵ نقطه)
    for k in range(5):
        i = round(k * (len(points) - 1) / 4)
        parts.append(f'<text x="{x(i):.1f}" y="{height - 10}" text-anchor="middle" '
                     f'font-size="11" fill="#6b7280">{fa_date(points[i]["date"])}</text>')
    # خط میانگین (سبز) و خط کمترین قیمت (آبی)
    parts.append(f'<polyline points="{polyline(avgs)}" fill="none" '
                 f'stroke="{GREEN}" stroke-width="2.5"/>')
    parts.append(f'<polyline points="{polyline([p["price"] for p in points])}" '
                 f'fill="none" stroke="{BLUE}" stroke-width="2.5"/>')
    # قطعه‌های بدون تغییر: همان بخش از خط آبی، با خط‌چین و ضخیم‌تر
    for i in range(1, len(points)):
        if points[i]["price"] == points[i - 1]["price"]:
            parts.append(
                f'<line x1="{x(i - 1):.1f}" y1="{y(points[i - 1]["price"]):.1f}" '
                f'x2="{x(i):.1f}" y2="{y(points[i]["price"]):.1f}" '
                f'stroke="{GREY}" stroke-width="4" stroke-dasharray="6 4"/>')
    parts.append("</svg>")
    return "".join(parts)


def legend() -> str:
    return (
        '<div class="legend">'
        f'<span><i class="swatch" style="background:{GREEN}"></i>میانگین</span>'
        f'<span><i class="swatch" style="background:{BLUE}"></i>کمترین قیمت</span>'
        f'<span><i class="swatch dashed"></i>بدون تغییر</span>'
        "</div>"
    )


def stats_table(coin: str, stats: dict) -> str:
    rows = [
        ("کمترین قیمت", stats["lowest"]),
        ("بیشترین قیمت", stats["highest"]),
        ("قیمت فعلی", stats["current"]),
        ("میانگین", stats["average"]),
    ]
    body = "".join(
        f"<tr><td>{label}</td><td>${fa_num(value, 2)}</td>"
        f"<td>{fa_date(when) if '-' in when else when}</td></tr>"
        for label, (value, when) in rows
    )
    return (
        f'<table class="stats"><thead><tr><th>مورد</th><th>قیمت</th>'
        f"<th>تاریخ</th></tr></thead><tbody>{body}</tbody></table>"
    )


def deal_card(coin: str, stats: dict) -> str:
    current, _ = stats["current"]
    average, _ = stats["average"]
    lowest, _ = stats["lowest"]
    diff_pct = (current - average) / average * 100
    if current < average:
        pill = '<span class="pill best">بهترین قیمت</span>'
        note = (f"قیمت فعلی {fa_num(abs(diff_pct), 1)}٪ زیر میانگین است؛ "
                f"فاصله تا کمترین قیمت ثبت‌شده "
                f"${fa_num(current - lowest, 2)} است.")
    else:
        pill = '<span class="pill plain">بالای میانگین</span>'
        note = (f"قیمت فعلی {fa_num(diff_pct, 1)}٪ بالای میانگین است؛ "
                f"کمترین قیمت ثبت‌شده ${fa_num(lowest, 2)} بوده است.")
    return (
        f'<article class="deal"><header><h3>{FA_NAMES.get(coin, coin)}</h3>{pill}</header>'
        f'<p class="deal-price">${fa_num(current, 2)}</p>'
        f'<p class="deal-avg">میانگین: ${fa_num(average, 2)}</p>'
        f'<p class="deal-note">{note}</p></article>'
    )


def desired_price_panel(coins: list[str], current: dict) -> str:
    options = "".join(
        f'<option value="{html.escape(coin)}">{FA_NAMES.get(coin, coin)}</option>'
        for coin in coins
    )
    chips = "".join(
        f'<button type="button" class="chip" data-pct="{pct}">٪{fa_num(abs(pct))}−</button>'
        for pct in (-3, -5, -7, -10)
    )
    chips += '<button type="button" class="chip" data-pct="any">هر کاهش قیمتی</button>'
    current_json = json.dumps(current)
    return f"""
<section class="panel" id="alert-panel">
  <h2>تعیین قیمت دلخواه</h2>
  <p>وقتی قیمت به عددی که می‌خواهید رسید، خبرتان می‌کنیم. این پنل فقط نمایشی است و هیچ ایمیلی واقعاً فرستاده نمی‌شود.</p>
  <form id="alert-form">
    <label>ارز
      <select id="alert-coin">{options}</select>
    </label>
    <label>قیمت دلخواه (دلار)
      <input id="alert-price" type="number" min="0" step="0.01" required>
    </label>
    <div class="chips" role="group" aria-label="میان‌بر درصد">{chips}</div>
    <label>ایمیل
      <input id="alert-email" type="email" required placeholder="name@example.com" dir="ltr">
    </label>
    <button type="submit" class="primary">ثبت هشدار نمایشی</button>
  </form>
  <p id="alert-confirm" class="confirm" hidden></p>
</section>
<script>
const CURRENT = {current_json};
const coinSel = document.getElementById('alert-coin');
const priceInput = document.getElementById('alert-price');
function applyPct(pct) {{
  if (pct === 'any') {{ priceInput.value = ''; priceInput.placeholder = 'هر قیمتی زیر قیمت فعلی'; return; }}
  const cur = CURRENT[coinSel.value];
  priceInput.value = (cur * (1 + pct / 100)).toFixed(2);
  priceInput.placeholder = '';
}}
document.querySelectorAll('.chip').forEach(ch => {{
  ch.addEventListener('click', () => applyPct(ch.dataset.pct === 'any' ? 'any' : Number(ch.dataset.pct)));
}});
coinSel.addEventListener('change', () => {{ priceInput.value = ''; }});
document.getElementById('alert-form').addEventListener('submit', ev => {{
  ev.preventDefault();
  const coin = coinSel.options[coinSel.selectedIndex].text;
  const price = priceInput.value ? '$' + priceInput.value : 'هر کاهش قیمتی';
  const email = document.getElementById('alert-email').value;
  const msg = document.getElementById('alert-confirm');
  msg.textContent = 'ثبت نمایشی انجام شد: ' + coin + ' — ' + price + ' — ' + email + ' (ایمیلی فرستاده نمی‌شود.)';
  msg.hidden = false;
}});
</script>"""


CSS = """
* { box-sizing: border-box; }
body { font-family: Tahoma, sans-serif; background: #f3f4f6; color: #111827;
  margin: 0; padding: 0 16px 48px; direction: rtl; }
main { max-width: 880px; margin: 0 auto; }
header.page { padding: 28px 4px 8px; }
h1 { font-size: 26px; margin: 0 0 6px; }
.sub { color: #4b5563; margin: 0 0 18px; }
.badge { display: inline-block; background: #fef3c7; color: #92400e; border-radius: 999px;
  padding: 2px 10px; font-size: 12px; margin-inline-start: 8px; }
section.card { background: #fff; border: 1px solid #e5e7eb; border-radius: 14px;
  padding: 20px; margin-bottom: 20px; }
h2 { font-size: 19px; margin: 0 0 12px; }
h3 { font-size: 17px; margin: 0; }
.ranges { margin-bottom: 10px; }
.ranges button { border: 1px solid #d1d5db; background: #fff; border-radius: 999px;
  padding: 6px 14px; margin-inline-end: 6px; cursor: pointer; font-family: inherit; }
.ranges button[aria-pressed="true"] { background: #111827; color: #fff; border-color: #111827; }
.chart-view[hidden] { display: none; }
.legend { display: flex; gap: 20px; flex-wrap: wrap; margin-top: 8px; color: #374151; font-size: 13px; }
.swatch { display: inline-block; width: 22px; height: 4px; border-radius: 2px;
  vertical-align: middle; margin-inline-end: 6px; }
.swatch.dashed { background: repeating-linear-gradient(to left, #6b7280 0 6px, transparent 6px 10px); }
table.stats { width: 100%; border-collapse: collapse; font-size: 14px; }
table.stats th, table.stats td { padding: 9px 10px; border-bottom: 1px solid #e5e7eb; text-align: right; }
table.stats tbody tr:nth-child(even) { background: #f9fafb; }
.deals { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 14px; }
.deal { border: 1px solid #e5e7eb; border-radius: 12px; padding: 16px; background: #fff; }
.deal header { display: flex; justify-content: space-between; align-items: center; }
.deal-price { font-size: 24px; font-weight: bold; margin: 10px 0 2px; }
.deal-avg { color: #6b7280; margin: 0 0 8px; font-size: 13px; }
.deal-note { font-size: 13px; color: #374151; margin: 0; }
.pill { font-size: 12px; border-radius: 999px; padding: 3px 10px; }
.pill.best { background: #dcfce7; color: #166534; }
.pill.plain { background: #f3f4f6; color: #4b5563; }
.panel label { display: block; margin-bottom: 12px; font-size: 14px; }
.panel input, .panel select { display: block; width: 100%; margin-top: 5px; padding: 9px 10px;
  border: 1px solid #d1d5db; border-radius: 8px; font-family: inherit; font-size: 14px; }
.chips { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 12px; }
.chip { border: 1px solid #2563eb; color: #2563eb; background: #fff; border-radius: 999px;
  padding: 6px 12px; cursor: pointer; font-family: inherit; }
.chip:hover { background: #eff6ff; }
.primary { background: #16a34a; color: #fff; border: none; border-radius: 8px;
  padding: 11px 20px; font-family: inherit; font-size: 15px; cursor: pointer; }
.confirm { background: #dcfce7; color: #166534; border-radius: 8px; padding: 10px 12px; margin-top: 12px; }
footer { color: #6b7280; font-size: 12px; text-align: center; }
"""


def build_report() -> str:
    history = load_history()
    current = load_current()
    today = date(2026, 11, 10).isoformat()
    coins = list(history)
    sections = []
    for coin in coins:
        series = history[coin]
        values = [p["price"] for p in series]
        avg = rolling_average(values)
        stats = stats_for(series, current[coin])
        views = "".join(
            f'<div class="chart-view" data-range="{days}"'
            + (' hidden' if days != 120 else '')
            + f'>{svg_chart(series, avg, coin, days)}</div>'
            for days in (30, 90, 120)
        )
        sections.append(f"""
<section class="card">
  <h2>{FA_NAMES.get(coin, coin)}</h2>
  <div class="ranges" role="group" aria-label="بازه‌ی نمودار">
    <button type="button" data-range="30" aria-pressed="false">۳۰ روز</button>
    <button type="button" data-range="90" aria-pressed="false">۹۰ روز</button>
    <button type="button" data-range="120" aria-pressed="true">همه</button>
  </div>
  {views}
  {legend()}
  <h3 style="margin-top:18px">آمار قیمت</h3>
  {stats_table(coin, stats)}
</section>""")
    deals = "".join(deal_card(c, stats_for(history[c], current[c])) for c in coins)
    return f"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>گزارش تاریخچه‌ی قیمت — نمونه کار</title>
<style>{CSS}</style>
</head>
<body>
<main>
<header class="page">
  <h1>گزارش تاریخچه‌ی قیمت<span class="badge">نمونه کار — داده‌ی نمایشی</span></h1>
  <p class="sub">تاریخ گزارش: {fa_date(today)} — قیمت‌ها از داده‌ی نمایشی محلی خوانده شده‌اند و قیمت زنده نیستند.</p>
</header>
{''.join(sections)}
<section class="card">
  <h2>مقایسه با میانگین</h2>
  <div class="deals">{deals}</div>
</section>
{desired_price_panel(coins, current)}
<footer>نمودار و جدول از داده‌ی نمایشی همین پوشه ساخته شده‌اند.</footer>
</main>
<script>
document.querySelectorAll('.ranges').forEach(group => {{
  group.addEventListener('click', ev => {{
    const btn = ev.target.closest('button');
    if (!btn) return;
    const card = group.closest('section');
    card.querySelectorAll('.ranges button').forEach(b => b.setAttribute('aria-pressed', b === btn ? 'true' : 'false'));
    card.querySelectorAll('.chart-view').forEach(v => {{ v.hidden = v.dataset.range !== btn.dataset.range; }});
  }});
}});
</script>
</body>
</html>"""


def main() -> None:
    parser = argparse.ArgumentParser(description="ساخت گزارش اچ‌تی‌ام‌ال تاریخچه‌ی قیمت")
    parser.add_argument("--output", default="report.html", help="مسیر فایل خروجی")
    args = parser.parse_args()
    out = Path(args.output)
    if not out.is_absolute():
        out = BASE_DIR / out
    out.write_text(build_report(), encoding="utf-8")
    print(f"گزارش ساخته شد: {out}")


if __name__ == "__main__":
    main()
