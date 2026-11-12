# subs.py — منطق خالص اشتراک: طرح، خرید، تمدید، تحویل کانفیگ، رسید،
# اشتراک‌های من، تیکت پشتیبانی و پنل مدیر
# این ماژول هیچ وابستگی به تلگرام ندارد؛ demo.py همه‌ی جریان را بدون توکن
# و بدون اتصال اجرا می‌کند. bot.py فقط همین توابع را به دکمه‌ها و دستورها وصل می‌کند.
# همه‌ی داده‌ها در حافظه نگه داشته می‌شوند؛ در نسخه‌ی واقعی، اشتراک‌ها
# در پایگاه داده ذخیره می‌شوند.
#
# نکتهٔ نمایشی: کانفیگ و لینک اشتراک روی دامنهٔ نمایشی demo.sepehr.example
# ساخته می‌شوند؛ این دامنه واقعی نیست و به هیچ سروری وصل نمی‌شود.

import calendar
from datetime import datetime

from plans import PLANS, format_toman, get_plan

BRAND_NAME = "سپهر — اشتراک اینترنت پرسرعت"

# منوی اصلی ربات: دکمه‌های ثابت پایین صفحه (در subs.py است تا demo.py
# بدون تلگرام هم بتواند چیدمان آن را بررسی کند).
HOME_MENU = [
    ["🚀 خرید اشتراک", "📲 اشتراک‌های من"],
    ["♻️ تمدید اشتراک", "🎁 کد تخفیف"],
    ["🎧 پشتیبانی", "❓ راهنما"],
]

# کدهای تخفیف (درصد). این کدها در نمونه کار واقعاً کار می‌کنند و
# تخفیف واقعی می‌دهند؛ در نسخهٔ واقعی همین جدول را مدیر پر می‌کند.
DISCOUNT_CODES = {"سپهر۱۰": 10}

# روش‌های پرداخت. «درگاه آنلاین» در نسخه‌ی واقعی به درگاه وصل می‌شود؛
# «کارت‌به‌کارت» شماره‌ی کارت نمایشی را نشان می‌دهد و عکس رسید را می‌گیرد.
PAYMENT_METHODS = ["درگاه آنلاین", "کارت‌به‌کارت"]
# شماره‌ی کارت نمایشی برای پرداخت کارت‌به‌کارت — شماره‌ی واقعی نیست و
# در نسخهٔ واقعی جای آن شماره‌ی واقعی فروشنده گذاشته می‌شود.
DEMO_CARD_NUMBER = "۶۰۳۷ ۹۹۱۱ ۰۰۰۰ ۰۰۰۰"

# دامنهٔ نمایشی تحویل کانفیگ و لینک اشتراک — دامنهٔ example. واقعی نیست.
DEMO_DOMAIN = "demo.sepehr.example"

_FA_DIGITS = str.maketrans("۰۱۲۳۴۵۶۷۸۹٠١٢٣٤٥٦٧٨٩", "01234567890123456789")


def _normalize_code(code: str) -> str:
    """ارقام فارسی/عربی کد تخفیف را به لاتین تبدیل می‌کند تا «سپهر10» هم
    مثل «سپهر۱۰» پذیرفته شود."""
    return code.strip().translate(_FA_DIGITS)


def _fa_digits(number: int) -> str:
    """عدد را با ارقام فارسی برمی‌گرداند (برای پیام‌های نمایشی)."""
    return str(number).translate(str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹"))


def _add_months(moment: datetime, months: int) -> datetime:
    """چند ماه به یک تاریخ اضافه می‌کند؛ روز آخر ماه کوتاه را درست می‌کند
    (مثلاً ۳۱ ژانویه + ۱ ماه می‌شود ۲۸ فوریه)."""
    month = moment.month - 1 + months
    year = moment.year + month // 12
    month = month % 12 + 1
    day = min(moment.day, calendar.monthrange(year, month)[1])
    return moment.replace(year=year, month=month, day=day)


def _fmt_date(moment: datetime) -> str:
    """تاریخ را به شکل کوتاه برمی‌گرداند: 2026-12-10."""
    return moment.strftime("%Y-%m-%d")


def _fmt_when(moment: datetime) -> str:
    """تاریخ و ساعت را برمی‌گرداند: 2026-11-10 21:30."""
    return moment.strftime("%Y-%m-%d %H:%M")


def discount_for(code: str, price: int) -> tuple[str, int, int] | None:
    """کد تخفیف را بررسی می‌کند؛ معتبر باشد (کلید جدول، درصد، مبلغ تخفیف)
    می‌دهد و نامعتبر باشد None. ارقام فارسی و لاتین هر دو پذیرفته می‌شوند."""
    normalized = _normalize_code(code)
    for key, percent in DISCOUNT_CODES.items():
        if _normalize_code(key) == normalized:
            return key, percent, price * percent // 100
    return None


def apply_discount_text(code: str, price: int) -> tuple[str, int] | str:
    """متن پاسخ به کد تخفیف؛ معتبر باشد (پیام تایید، مبلغ تخفیف) و
    نامعتبر باشد پیام خطا می‌دهد."""
    found = discount_for(code, price)
    if found is None:
        return "❌ این کد تخفیف معتبر نیست."
    key, percent, amount = found
    return (
        f"✅ کد تخفیف «{key}» اعمال شد؛ {_fa_digits(percent)}٪ تخفیف "
        f"({format_toman(amount)})."
    ), amount


def subscription_link(sub: dict) -> str:
    """لینک اشتراک نمایشی روی دامنهٔ نمایشی."""
    return f"https://{DEMO_DOMAIN}/s/{sub['code']}"


def demo_config_text(sub: dict) -> str:
    """متن کانفیگ نمایشی برای تحویل فوری؛ آدرس آن واقعی نیست."""
    return (
        "⚙️ کانفیگ نمایشی:\n"
        f"آدرس: {DEMO_DOMAIN}\n"
        "پورت: 443\n"
        f"شناسه: {sub['code']}\n"
        f"طرح: {sub['plan_name']}"
    )


def subscription_status(sub: dict) -> str:
    """وضعیت اشتراک از روی لغو و انقضا حساب می‌شود، نه از فیلد ذخیره‌شده."""
    if sub["cancelled"]:
        return "لغو شده"
    if datetime.now() > sub["expires_at"]:
        return "منقضی‌شده"
    return "فعال"


def is_active(sub: dict) -> bool:
    """اشتراک فعال یعنی لغو نشده و منقضی نشده باشد."""
    return subscription_status(sub) == "فعال"

class SubscriptionBook:
    """دفتر اشتراک‌ها: خرید، تمدید، لغو، پیگیری با کد، پنل مدیر."""

    def __init__(self) -> None:
        self.subs: dict[str, dict] = {}
        self._counter = 1000

    def _next_code(self) -> str:
        self._counter += 1
        return f"SP-{self._counter}"

    def create_subscription(
        self,
        user_id: int,
        user_name: str,
        plan_code: str,
        discount_code: str | None = None,
    ) -> dict:
        """از یک طرح، یک اشتراک تازه می‌سازد و کد اشتراک برمی‌گرداند.
        انقضا از لحظهٔ خرید حساب می‌شود."""
        plan = get_plan(plan_code)
        if plan is None:
            raise ValueError(f"طرح «{plan_code}» پیدا نشد.")
        now = datetime.now()
        price = plan["price_toman"]
        amount_off = 0
        stored_code = None
        if discount_code:
            found = discount_for(discount_code, price)
            if found is not None:
                stored_code, _percent, amount_off = found
        sub = {
            "code": self._next_code(),
            "user_id": user_id,
            "user_name": user_name,
            "plan_code": plan_code.strip().lower(),
            "plan_name": plan["name"],
            "months": plan["months"],
            "price": price - amount_off,
            "discount_code": stored_code,
            "discount_amount": amount_off,
            "payment": None,  # بعد از پرداخت نمایشی پر می‌شود
            "receipt_photo": None,  # شناسه‌ی عکس رسید کارت‌به‌کارت
            "cancelled": False,
            "renewals": 0,
            "created_at": now,
            "expires_at": _add_months(now, plan["months"]),
        }
        self.subs[sub["code"]] = sub
        return sub

    def get(self, code: str) -> dict | None:
        """اشتراک را با کد پیدا می‌کند؛ کد نامعتبر None می‌دهد."""
        return self.subs.get((code or "").strip().upper())

    def list_for_user(self, user_id: int) -> list[dict]:
        """اشتراک‌های یک مشتری، از تازه‌ترین به قدیمی‌ترین."""
        mine = [s for s in self.subs.values() if s["user_id"] == user_id]
        return list(reversed(mine))

    def list_all(self) -> list[dict]:
        """همه‌ی اشتراک‌ها به ترتیب ثبت."""
        return list(self.subs.values())

    def renew_subscription(
        self,
        code: str,
        plan_code: str | None = None,
        discount_code: str | None = None,
    ) -> dict:
        """تمدید اشتراک: مدت طرح به اشتراک موجود اضافه می‌شود.
        اگر اشتراک منقضی شده باشد، مدت تازه از همین لحظه حساب می‌شود؛
        اگر هنوز فعال باشد، به انقضای فعلی اضافه می‌شود.
        طرح تمدید به‌طور پیش‌فرض همان طرح اشتراک است."""
        sub = self.get(code)
        if sub is None:
            raise ValueError(f"اشتراکی با کد «{(code or '').strip().upper()}» پیدا نشد.")
        if sub["cancelled"]:
            raise ValueError(f"اشتراک {sub['code']} لغو شده است؛ تمدید نمی‌شود.")
        plan = get_plan(plan_code) if plan_code else get_plan(sub["plan_code"])
        if plan is None:
            raise ValueError(f"طرح «{plan_code}» پیدا نشد.")
        price = plan["price_toman"]
        amount_off = 0
        stored_code = None
        if discount_code:
            found = discount_for(discount_code, price)
            if found is not None:
                stored_code, _percent, amount_off = found
        base = max(datetime.now(), sub["expires_at"])
        sub["expires_at"] = _add_months(base, plan["months"])
        sub["renewals"] += 1
        sub["last_renewal_price"] = price - amount_off
        sub["last_renewal_discount"] = stored_code
        return sub

    def extend_subscription(self, code: str, months: int = 1) -> str:
        """تمدید دستی مدیر: چند ماه به انقضای اشتراک اضافه می‌کند."""
        sub = self.get(code)
        if sub is None:
            return f"❌ اشتراکی با کد «{(code or '').strip().upper()}» پیدا نشد."
        if sub["cancelled"]:
            return f"❌ اشتراک {sub['code']} لغو شده است؛ تمدید نمی‌شود."
        base = max(datetime.now(), sub["expires_at"])
        sub["expires_at"] = _add_months(base, months)
        return (
            f"✅ اشتراک {sub['code']} {months} ماه تمدید شد؛ "
            f"انقضای تازه: {_fmt_date(sub['expires_at'])}."
        )

    def cancel_subscription(self, code: str) -> str:
        """لغو اشتراک از طرف مدیر؛ اشتراک لغوشده دیگر تمدید نمی‌شود."""
        sub = self.get(code)
        if sub is None:
            return f"❌ اشتراکی با کد «{(code or '').strip().upper()}» پیدا نشد."
        if sub["cancelled"]:
            return f"ℹ️ اشتراک {sub['code']} قبلاً لغو شده بود."
        sub["cancelled"] = True
        return f"✅ اشتراک {sub['code']} لغو شد."

def record_mock_payment(sub: dict, method: str, amount: int | None = None) -> dict:
    """پرداخت نمایشی را روی اشتراک ثبت می‌کند و رسید برمی‌گرداند.
    در نسخهٔ واقعی اینجا درگاه پرداخت صدا زده می‌شود؛
    در نمونه کار، پرداخت فقط شبیه‌سازی می‌شود و پولی جابه‌جا نمی‌شود.
    کارت‌به‌کارت هم همین‌جا ثبت می‌شود و عکس رسید جداگانه روی اشتراک
    می‌نشیند؛ در نسخهٔ واقعی، تایید رسید پیش از فعال‌سازی است."""
    if method not in PAYMENT_METHODS:
        raise ValueError(f"روش پرداخت «{method}» معتبر نیست.")
    if sub.get("payment") is not None and sub.get("renewals", 0) == 0:
        return sub["payment"]
    payment = {
        "payment_id": f"PAY-{sub['code']}",
        "method": method,
        "amount": sub["price"] if amount is None else amount,
        "paid": True,
        "paid_at": datetime.now(),
    }
    sub["payment"] = payment
    return payment


def record_renewal_payment(sub: dict, method: str) -> dict:
    """پرداخت نمایشی تمدید را ثبت می‌کند و رسید برمی‌گرداند."""
    if method not in PAYMENT_METHODS:
        raise ValueError(f"روش پرداخت «{method}» معتبر نیست.")
    payment = {
        "payment_id": f"PAY-{sub['code']}-R{sub['renewals']}",
        "method": method,
        "amount": sub.get("last_renewal_price", sub["price"]),
        "paid": True,
        "paid_at": datetime.now(),
    }
    sub["last_payment"] = payment
    sub["payment"] = payment
    return payment


def format_purchase_summary(plan_code: str, discount_code: str | None = None) -> str:
    """خلاصه‌ی پیش از خرید: طرح، قیمت، تخفیف و مبلغ نهایی — همان چیزی که
    مشتری پیش از پرداخت می‌بیند."""
    plan = get_plan(plan_code)
    if plan is None:
        return f"❌ طرح «{plan_code}» پیدا نشد."
    price = plan["price_toman"]
    amount_off = 0
    stored_code = None
    if discount_code:
        found = discount_for(discount_code, price)
        if found is not None:
            stored_code, _percent, amount_off = found
    lines = ["🧾 خلاصه‌ی خرید:", ""]
    lines.append(f"طرح: {plan['name']}")
    lines.append(f"مدت: {plan['months']} ماه")
    lines.append(f"قیمت: {format_toman(price)}")
    if stored_code is not None:
        lines.append(f"تخفیف ({stored_code}): −{format_toman(amount_off)}")
    lines.append(f"مبلغ نهایی: {format_toman(price - amount_off)}")
    return "\n".join(lines)


def format_subscription(sub: dict | None, code: str = "") -> str:
    """جزئیات یک اشتراک: طرح، وضعیت، انقضا و لینک."""
    if sub is None:
        return (
            f"❌ اشتراکی با کد «{(code or '').strip().upper()}» پیدا نشد.\n"
            "کد را درست وارد کنید؛ مثال: SP-1001"
        )
    lines = [
        f"📲 اشتراک {sub['code']}",
        f"طرح: {sub['plan_name']}",
        f"وضعیت: {subscription_status(sub)}",
        f"انقضا: {_fmt_date(sub['expires_at'])}",
        f"مبلغ پرداختی: {format_toman(sub['price'])}",
        "",
        f"🔗 لینک اشتراک:\n{subscription_link(sub)}",
    ]
    return "\n".join(lines)


def format_delivery(sub: dict) -> str:
    """پیام تحویل فوری بعد از پرداخت: فعال‌سازی، لینک اشتراک و کانفیگ."""
    return (
        "🎉 اشتراک شما فعال شد!\n"
        f"کد اشتراک: {sub['code']}\n"
        f"طرح: {sub['plan_name']}\n"
        f"انقضا: {_fmt_date(sub['expires_at'])}\n"
        f"🔗 لینک اشتراک:\n{subscription_link(sub)}\n\n"
        f"{demo_config_text(sub)}\n\n"
        "این کانفیگ نمایشی است؛ آدرس بالا واقعی نیست و اتصالی برقرار نمی‌کند."
    )


def format_receipt(sub: dict) -> str:
    """رسید پرداخت؛ فقط وقتی پرداخت ثبت شده باشد رسید کامل می‌دهد."""
    payment = sub.get("payment")
    if payment is None:
        return (
            f"❌ اشتراک {sub['code']} هنوز پرداخت نشده است.\n"
            "برای پرداخت، دکمه‌ی «پرداخت» را بزنید."
        )
    lines = [
        "🧾 رسید پرداخت",
        f"{BRAND_NAME}",
        "",
        f"اشتراک: {sub['code']}",
        f"مشتری: {sub['user_name']}",
        f"طرح: {sub['plan_name']}",
        f"شناسه‌ی پرداخت: {payment['payment_id']}",
        f"روش پرداخت: {payment['method']}",
        f"زمان پرداخت: {_fmt_when(payment['paid_at'])}",
        "",
        f"مبلغ پرداختی: {format_toman(payment['amount'])}",
        f"انقضا: {_fmt_date(sub['expires_at'])}",
        f"وضعیت اشتراک: {subscription_status(sub)}",
        "",
        "از خرید شما سپاسگزاریم! 🙏",
    ]
    return "\n".join(lines)


def format_my_subscriptions(subs: list[dict]) -> str:
    """فهرست اشتراک‌های یک مشتری، از تازه‌ترین به قدیمی‌ترین."""
    if not subs:
        return "📲 هنوز اشتراکی نخریده‌اید.\nبرای دیدن طرح‌ها: /plans"
    lines = ["📲 اشتراک‌های شما:", ""]
    for sub in subs:
        lines.append(
            f"• {sub['code']} — {sub['plan_name']} — "
            f"{subscription_status(sub)} — انقضا {_fmt_date(sub['expires_at'])}"
        )
    lines.append("")
    lines.append("برای جزئیات و تمدید هر اشتراک، روی آن بزنید.")
    return "\n".join(lines)


def format_admin_list(subs: list[dict]) -> str:
    """فهرست اشتراک‌ها برای پنل مدیر."""
    if not subs:
        return "📋 هنوز اشتراکی ثبت نشده است."
    lines = ["📋 پنل مدیر — همه‌ی اشتراک‌ها:", ""]
    for sub in subs:
        paid = (
            "پرداخت شده ✅"
            if sub.get("payment") is not None and sub["payment"].get("paid")
            else "پرداخت نشده ⏳"
        )
        lines.append(
            f"• {sub['code']} — {sub['user_name']} — {sub['plan_name']} — "
            f"{format_toman(sub['price'])} — {subscription_status(sub)} — {paid}"
        )
    lines.append("")
    lines.append("برای تمدید یا لغو یک اشتراک، روی آن بزنید.")
    return "\n".join(lines)


def format_status_push(sub: dict, note: str) -> str:
    """متن پیامی که با هر تغییر وضعیت اشتراک برای مشتری فرستاده می‌شود؛
    خروجی همین متن است و ارسال آن با bot.py است."""
    return f"{note}\n\n" + format_subscription(sub)


def format_welcome(name: str, active_count: int) -> str:
    """متن خوش‌آمد /start با خط‌های اعتماد و وضعیت واقعی مشتری."""
    return (
        f"سلام {name}! 👋\n"
        f"به {BRAND_NAME} خوش آمدید.\n\n"
        "⚡ تحویل فوری کانفیگ بعد از پرداخت\n"
        "🎧 پشتیبانی ۲۴ ساعته در تلگرام\n"
        "♻️ تمدید آسان، بدون توقف سرویس\n\n"
        f"📲 اشتراک‌های فعال شما: {active_count}\n\n"
        "🕐 ربات هر ۶ ساعت چند دقیقه استراحت می‌کند؛ "
        "اگر جواب نداد، به‌زودی برمی‌گردد.\n\n"
        "از دکمه‌های پایین شروع کنید 👇"
    )


class SupportTickets:
    """تیکت‌های پشتیبانی: پیام مشتری، پاسخ مدیر، وضعیت باز/پاسخ‌داده‌شده."""

    def __init__(self) -> None:
        self.tickets: list[dict] = []
        self._counter = 0

    def create_ticket(self, user_id: int, user_name: str, text: str) -> dict:
        self._counter += 1
        ticket = {
            "id": self._counter,
            "user_id": user_id,
            "user_name": user_name,
            "text": text,
            "created_at": _fmt_when(datetime.now()),
            "answered": False,
            "answer": None,
        }
        self.tickets.append(ticket)
        return ticket

    def get(self, ticket_id: int) -> dict | None:
        for ticket in self.tickets:
            if ticket["id"] == ticket_id:
                return ticket
        return None

    def list_open(self) -> list[dict]:
        return [t for t in self.tickets if not t["answered"]]

    def answer_ticket(self, ticket_id: int, answer: str) -> dict | None:
        ticket = self.get(ticket_id)
        if ticket is None:
            return None
        ticket["answered"] = True
        ticket["answer"] = answer
        return ticket


def format_tickets(tickets: list[dict]) -> str:
    """فهرست تیکت‌های باز برای پنل مدیر."""
    if not tickets:
        return "🎧 تیکت باز ندارید."
    lines = ["🎧 تیکت‌های باز پشتیبانی:", ""]
    for ticket in tickets:
        lines.append(
            f"• #{ticket['id']} — {ticket['user_name']} "
            f"({ticket['created_at']}): {ticket['text']}"
        )
    lines.append("")
    lines.append("برای پاسخ، روی تیکت بزنید.")
    return "\n".join(lines)


def is_admin(user_id: int, admin_id: int) -> bool:
    """مدیر فقط وقتی مشخص است که شناسه‌ی مدیر تنظیم شده باشد و برابر باشد."""
    return admin_id != 0 and user_id == admin_id
