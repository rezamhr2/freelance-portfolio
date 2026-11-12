# bot.py — نمونه کار: ربات فروش اشتراک تلگرام با کتابخانهٔ پایتون‌تلگرام‌بات نسخه ۲۰ به بالا (ناهمگام)
# «سپهر — اشتراک اینترنت پرسرعت»؛ طرح‌ها و قیمت‌ها نمایشی‌اند و پولی جابه‌جا نمی‌شود.
#
# امکانات: منوی اصلی ثابت با دکمه‌های پایین صفحه، مرور طرح‌های اشتراک با جدول
# قیمت درون‌چتی، خرید راهنمایی‌شده (انتخاب طرح ← خلاصه ← کد تخفیف ← روش پرداخت)،
# تحویل فوری کانفیگ و لینک اشتراک، «اشتراک‌های من» با انقضا،
# تمدید اشتراک، پشتیبانی با تیکت، پیام‌رسانی خودکار تغییر وضعیت به مشتری،
# و پنل مدیر.
# منطق اشتراک در subs.py و plans.py است؛ این فایل فقط آن را به دستورها و
# دکمه‌ها وصل می‌کند.
#
# دو حالت اجرا:
#   1) پولینگ (توسعه/تست محلی):  BOT_MODE=polling python bot.py
#   2) وب‌هوک (استقرار روی سرور): BOT_MODE=webhook WEBHOOK_URL=https://example.com python bot.py
#      حالت وب‌هوک به سرور با HTTPS عمومی نیاز دارد؛ توکن ربات و هاست را کارفرما تامین می‌کند.
#
# اجرا با نگهبان (برای گیت‌هاب اکشنز): python run_bot.py
#   نگهبان ربات را با وقفه‌ی نماییِ روبه‌افزایش دوباره بالا می‌آورد و پیش از
#   پایان اجرای زمان‌بندی‌شده، آن را تمیز متوقف می‌کند.
#
# نصب وابستگی‌ها: pip install -r requirements.txt
# نمایش آفلاین کل جریان (بدون توکن): python3 demo.py

import logging
import os
import time

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

from plans import PLANS, format_plan, format_plans, format_toman
from subs import (
    BRAND_NAME,
    DEMO_CARD_NUMBER,
    HOME_MENU,
    PAYMENT_METHODS,
    SubscriptionBook,
    SupportTickets,
    discount_for,
    format_admin_list,
    format_delivery,
    format_my_subscriptions,
    format_purchase_summary,
    format_receipt,
    format_status_push,
    format_subscription,
    format_tickets,
    format_welcome,
    is_active,
    is_admin,
    record_mock_payment,
    record_renewal_payment,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# روش پرداخت -> کلید دکمه‌ی شیشه‌ای
PAYMENT_CALLBACK = {
    "gateway": "درگاه آنلاین",
    "card": "کارت‌به‌کارت",
}

_FA = str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")


def _fa(number: int) -> str:
    """عدد را با ارقام فارسی برمی‌گرداند."""
    return str(number).translate(_FA)


# ---------- ابزارهای کوچک ----------

def get_sub_book(context: ContextTypes.DEFAULT_TYPE) -> SubscriptionBook:
    """دفتر اشتراک‌ها بین همه‌ی کاربران مشترک است (در نسخه‌ی واقعی پایگاه داده است)."""
    book = context.bot_data.get("sub_book")
    if book is None:
        book = SubscriptionBook()
        context.bot_data["sub_book"] = book
    return book


def get_tickets(context: ContextTypes.DEFAULT_TYPE) -> SupportTickets:
    """تیکت‌های پشتیبانی بین همه‌ی کاربران مشترک است."""
    tickets = context.bot_data.get("tickets")
    if tickets is None:
        tickets = SupportTickets()
        context.bot_data["tickets"] = tickets
    return tickets


def admin_id(context: ContextTypes.DEFAULT_TYPE) -> int:
    return int(context.bot_data.get("admin_id", 0) or 0)


def clear_flow_states(context: ContextTypes.DEFAULT_TYPE) -> None:
    """وقتی یک جریان تازه شروع می‌شود، حالت انتظار جریان قبلی را پاک می‌کند
    تا پیام بعدی کاربر به جریان اشتباه نرود."""
    for key in (
        "purchase",
        "awaiting_support",
        "awaiting_reply",
        "awaiting_discount",
        "awaiting_receipt",
    ):
        context.user_data.pop(key, None)


def active_count_for(context: ContextTypes.DEFAULT_TYPE, user_id: int) -> int:
    """تعداد اشتراک‌های فعال یک مشتری (برای پیام خوش‌آمد)."""
    book = get_sub_book(context)
    return sum(1 for sub in book.list_for_user(user_id) if is_active(sub))


# ---------- صفحه‌کلیدها ----------

def home_keyboard() -> ReplyKeyboardMarkup:
    """منوی اصلی ثابت پایین صفحه."""
    return ReplyKeyboardMarkup(HOME_MENU, resize_keyboard=True)


def plans_keyboard() -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton(
                f"{plan['name']} — {plan['price_toman']:,} تومان",
                callback_data=f"plan:{code}",
            )
        ]
        for code, plan in PLANS.items()
    ]
    buttons.append(
        [InlineKeyboardButton("📲 اشتراک‌های من", callback_data="mysubs")]
    )
    return InlineKeyboardMarkup(buttons)


def plan_keyboard(code: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("🚀 خرید این طرح", callback_data=f"buy:{code}")],
            [InlineKeyboardButton("⬅️ بازگشت به طرح‌ها", callback_data="plans")],
        ]
    )


def purchase_keyboard() -> InlineKeyboardMarkup:
    """خلاصه‌ی خرید: کد تخفیف، بعد دو روش پرداخت."""
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("🎁 کد تخفیف", callback_data="discount")],
            [
                InlineKeyboardButton(
                    PAYMENT_CALLBACK["gateway"], callback_data="paym:gateway"
                )
            ],
            [
                InlineKeyboardButton(
                    PAYMENT_CALLBACK["card"], callback_data="paym:card"
                )
            ],
            [InlineKeyboardButton("⬅️ بازگشت به طرح‌ها", callback_data="plans")],
        ]
    )


def mysubs_keyboard(subs: list[dict]) -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton(
                f"📲 {sub['code']} — {sub['plan_name']}",
                callback_data=f"sub:{sub['code']}",
            )
        ]
        for sub in subs
    ]
    buttons.append(
        [InlineKeyboardButton("🚀 خرید اشتراک تازه", callback_data="plans")]
    )
    return InlineKeyboardMarkup(buttons)


def sub_keyboard(code: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("♻️ تمدید این اشتراک", callback_data=f"renew:{code}")],
            [InlineKeyboardButton("⬅️ بازگشت به اشتراک‌های من", callback_data="mysubs")],
        ]
    )


def admin_keyboard(book: SubscriptionBook) -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton(
                f"{sub['code']} — {sub['plan_name']}",
                callback_data=f"admin:{sub['code']}",
            )
        ]
        for sub in book.list_all()
    ]
    return InlineKeyboardMarkup(buttons)


def admin_sub_keyboard(code: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "⏭ تمدید ۱ ماه", callback_data=f"extend:{code}"
                )
            ],
            [InlineKeyboardButton("❌ لغو اشتراک", callback_data=f"cancel:{code}")],
            [InlineKeyboardButton("⬅️ بازگشت به فهرست", callback_data="adminlist")],
        ]
    )


def tickets_keyboard(tickets: list[dict]) -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton(
                f"✉️ پاسخ #{ticket['id']} — {ticket['user_name']}",
                callback_data=f"reply:{ticket['id']}",
            )
        ]
        for ticket in tickets
    ]
    return InlineKeyboardMarkup(buttons)


# ---------- جایگزینی پیام (متن یا عکس) ----------

async def _replace_message(query, context, text: str, markup) -> None:
    """پیام دکمه‌خورده را با متن تازه جایگزین می‌کند؛ اگر پیام عکس باشد،
    زیرنویس آن عوض می‌شود و اگر هیچ‌کدام نشد، پیام تازه فرستاده می‌شود."""
    try:
        await query.edit_message_text(text, reply_markup=markup)
        return
    except Exception:
        pass
    try:
        await query.edit_message_caption(caption=text, reply_markup=markup)
        return
    except Exception:
        pass
    try:
        await query.message.delete()
    except Exception:
        pass
    await context.bot.send_message(
        chat_id=query.message.chat_id, text=text, reply_markup=markup
    )


async def _send_fresh_text(query, context, text: str, markup) -> None:
    """پیام دکمه‌خورده را پاک می‌کند و متن تازه را به‌صورت پیام جدید می‌فرستد
    (برای وقتی که پیام قبلی عکس است و متن تازه ربطی به آن ندارد)."""
    try:
        await query.message.delete()
    except Exception:
        pass
    await context.bot.send_message(
        chat_id=query.message.chat_id, text=text, reply_markup=markup
    )


# ---------- دستورها ----------

STARTED_AT = time.time()


def _format_uptime(seconds: float) -> str:
    """مدت روشن بودن ربات، به فارسی: «۲ ساعت و ۵ دقیقه»."""
    total = int(seconds)
    hours, rem = divmod(total, 3600)
    minutes, secs = divmod(rem, 60)
    if hours:
        return f"{hours} ساعت و {minutes} دقیقه"
    if minutes:
        return f"{minutes} دقیقه و {secs} ثانیه"
    return f"{secs} ثانیه"


async def status_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """پاسخ دستور /status — وضعیت ربات و مدت روشن بودن آن."""
    uptime = _format_uptime(time.time() - STARTED_AT)
    await update.message.reply_text(
        "وضعیت ربات: ✅ روشن است\n"
        f"مدت روشن بودن: {uptime}\n\n"
        "ربات هر ۶ ساعت برای چند دقیقه استراحت کوتاه دارد؛ "
        "اگر جواب نداد، چند دقیقه دیگر برگشته است."
    )


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """پاسخ دستور /start — خوش‌آمد با خط‌های اعتماد و وضعیت واقعی مشتری."""
    user = update.effective_user
    name = user.first_name if user else "کاربر"
    user_id = user.id if user else 0
    welcome = format_welcome(name, active_count_for(context, user_id))
    # خوش‌آمد متنی است؛ لوگو روی عکس پروفایل ربات است، نه در پیام.
    await update.message.reply_text(welcome, reply_markup=home_keyboard())
    await update.message.reply_text(format_plans(), reply_markup=plans_keyboard())


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """پاسخ دستور /help"""
    await update.message.reply_text(
        "راهنما:\n"
        "/start — شروع و خوش‌آمد\n"
        "/plans — دیدن طرح‌های اشتراک و قیمت‌ها\n"
        "/buy — خرید اشتراک تازه\n"
        "/mysubs — اشتراک‌های من (انقضا)\n"
        "/renew — تمدید اشتراک\n"
        "/support — پیام به پشتیبانی\n"
        "/discount — وارد کردن کد تخفیف\n"
        "/admin — پنل مدیر (فقط مدیر)\n"
        "/status — وضعیت ربات\n\n"
        "جریان خرید: طرح را انتخاب کنید ← خلاصه را ببینید ← "
        "کد تخفیف را بزنید (اگر دارید) ← روش پرداخت را انتخاب کنید ← "
        "کانفیگ و لینک اشتراک را فوری بگیرید.\n\n"
        "ربات هر ۶ ساعت برای چند دقیقه استراحت کوتاه دارد؛ "
        "اگر جواب نداد، چند دقیقه دیگر برگشته است.\n\n"
        "از دکمه‌های پایین صفحه هم می‌توانید شروع کنید."
    )


async def plans_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """پاسخ دستور /plans — فهرست طرح‌ها با دکمه."""
    await update.message.reply_text(format_plans(), reply_markup=plans_keyboard())


async def buy_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """پاسخ دستور /buy — همان فهرست طرح‌ها؛ خرید از انتخاب طرح شروع می‌شود."""
    await plans_command(update, context)


async def mysubs_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """پاسخ دستور /mysubs — اشتراک‌های همین مشتری."""
    user = update.effective_user
    book = get_sub_book(context)
    subs = book.list_for_user(user.id if user else 0)
    markup = mysubs_keyboard(subs) if subs else plans_keyboard()
    await update.message.reply_text(format_my_subscriptions(subs), reply_markup=markup)


async def renew_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """پاسخ دستور /renew — اشتراک‌های مشتری را نشان می‌دهد تا یکی را برای
    تمدید انتخاب کند."""
    user = update.effective_user
    book = get_sub_book(context)
    subs = book.list_for_user(user.id if user else 0)
    if not subs:
        await update.message.reply_text(
            "📲 هنوز اشتراکی نخریده‌اید.\nبرای دیدن طرح‌ها: /plans",
            reply_markup=plans_keyboard(),
        )
        return
    await update.message.reply_text(
        "♻️ کدام اشتراک را تمدید می‌کنید؟ مدت طرح به همان اشتراک اضافه می‌شود.",
        reply_markup=mysubs_keyboard(subs),
    )


async def support_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """پاسخ دستور /support — شروع تیکت پشتیبانی."""
    clear_flow_states(context)
    context.user_data["awaiting_support"] = True
    await update.message.reply_text("🎧 پیام خود را بنویسید؛ پشتیبانی پاسخ می‌دهد.")


async def discount_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """پاسخ دستور /discount — کد تخفیف روی خرید در جریان اعمال می‌شود."""
    purchase = context.user_data.get("purchase")
    if not purchase:
        await update.message.reply_text(
            "🎁 کد تخفیف روی خرید اعمال می‌شود؛ اول یک طرح انتخاب کنید.",
            reply_markup=plans_keyboard(),
        )
        return
    clear_flow_states(context)
    context.user_data["purchase"] = purchase
    context.user_data["awaiting_discount"] = True
    await update.message.reply_text("🎁 کد تخفیف را بفرستید؛ مثال: سپهر۱۰")


async def admin_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """پاسخ دستور /admin — فقط مدیر."""
    user = update.effective_user
    if not is_admin(user.id if user else 0, admin_id(context)):
        await update.message.reply_text("❌ این بخش فقط برای مدیر است.")
        return
    book = get_sub_book(context)
    await update.message.reply_text(
        format_admin_list(book.list_all()),
        reply_markup=admin_keyboard(book),
    )
    open_tickets = get_tickets(context).list_open()
    if open_tickets:
        await update.message.reply_text(
            format_tickets(open_tickets),
            reply_markup=tickets_keyboard(open_tickets),
        )


async def text_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """متن آزاد: اول جریان‌های در انتظار، بعد دکمه‌های منوی اصلی."""
    text = (update.message.text or "").strip()

    # ۱) تیکت پشتیبانی
    if context.user_data.pop("awaiting_support", False):
        user = update.effective_user
        name = user.first_name if user else "کاربر"
        user_id = user.id if user else 0
        ticket = get_tickets(context).create_ticket(user_id, name, text)
        admin = admin_id(context)
        if admin:
            try:
                await context.bot.send_message(
                    admin,
                    f"🎧 پیام پشتیبانی از {name}:\n{text}\n"
                    "برای پاسخ، دکمه‌ی «پاسخ» را بزنید.",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "✉️ پاسخ",
                                    callback_data=f"reply:{ticket['id']}",
                                )
                            ]
                        ]
                    ),
                )
            except Exception as exc:  # مدیر ربات را مسدود کرده باشد
                logger.warning("forward support ticket to admin failed: %s", exc)
        await update.message.reply_text(
            "✅ پیام شما به پشتیبانی رسید. پاسخ را همین‌جا می‌گیرید."
        )
        return

    # ۲) پاسخ مدیر به تیکت
    reply_ticket_id = context.user_data.pop("awaiting_reply", None)
    if reply_ticket_id is not None:
        tickets = get_tickets(context)
        ticket = tickets.answer_ticket(reply_ticket_id, text)
        if ticket is None:
            await update.message.reply_text("❌ این تیکت پیدا نشد.")
            return
        try:
            await context.bot.send_message(
                ticket["user_id"], f"🎧 پاسخ پشتیبانی:\n{text}"
            )
            await update.message.reply_text(
                f"✅ پاسخ برای {ticket['user_name']} فرستاده شد."
            )
        except Exception as exc:
            logger.warning("support reply to customer failed: %s", exc)
            await update.message.reply_text(
                "❌ پیام به مشتری نرسید (شاید ربات را مسدود کرده باشد)؛ "
                "تیکت پاسخ‌داده‌شده ثبت شد."
            )
        return

    # ۳) کد تخفیف روی خرید در جریان
    if context.user_data.pop("awaiting_discount", False):
        purchase = context.user_data.get("purchase")
        if not purchase:
            await update.message.reply_text(
                "🎁 کد تخفیف روی خرید اعمال می‌شود؛ اول یک طرح انتخاب کنید.",
                reply_markup=plans_keyboard(),
            )
            return
        plan = PLANS[purchase["plan"]]
        found = discount_for(text, plan["price_toman"])
        if found is None:
            await update.message.reply_text(
                "❌ این کد تخفیف معتبر نیست.\n\n"
                + format_purchase_summary(purchase["plan"], purchase.get("discount_code")),
                reply_markup=purchase_keyboard(),
            )
            return
        key, percent, amount = found
        purchase["discount_code"] = key
        await update.message.reply_text(
            f"✅ کد تخفیف «{key}» اعمال شد؛ {_fa(percent)}٪ تخفیف "
            f"({format_toman(amount)}).\n\n"
            + format_purchase_summary(purchase["plan"], key),
            reply_markup=purchase_keyboard(),
        )
        return

    # ۴) دکمه‌های منوی اصلی (زدن دکمه، خرید نیمه‌کاره را رها می‌کند)
    context.user_data.pop("purchase", None)
    if text == "🚀 خرید اشتراک":
        await plans_command(update, context)
    elif text == "📲 اشتراک‌های من":
        await mysubs_command(update, context)
    elif text == "♻️ تمدید اشتراک":
        await renew_command(update, context)
    elif text == "🎁 کد تخفیف":
        await discount_command(update, context)
    elif text == "🎧 پشتیبانی":
        await support_command(update, context)
    elif text == "❓ راهنما":
        await help_command(update, context)
    else:
        await update.message.reply_text(
            "متوجه نشدم. برای راهنما /help را بفرستید."
        )


async def photo_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """عکس رسید کارت‌به‌کارت: وقتی ربات منتظر رسید است، شناسه‌ی عکس را
    روی اشتراک ثبت می‌کند و مدیر را خبر می‌کند."""
    code = context.user_data.get("awaiting_receipt")
    if not code:
        return
    book = get_sub_book(context)
    sub = book.get(code)
    if sub is None:
        context.user_data.pop("awaiting_receipt", None)
        return
    photo = update.message.photo[-1]  # بزرگ‌ترین اندازه
    sub["receipt_photo"] = photo.file_id
    context.user_data.pop("awaiting_receipt", None)
    await update.message.reply_text(
        f"✅ عکس رسید برای اشتراک {code} رسید؛ پشتیبانی آن را بررسی می‌کند."
    )
    admin = admin_id(context)
    if admin:
        try:
            await context.bot.send_message(
                admin, f"🧾 رسید پرداخت کارت‌به‌کارت برای اشتراک {code} رسید."
            )
        except Exception as exc:
            logger.warning("receipt notice to admin failed: %s", exc)


# ---------- جریان مشترک خرید و تمدید ----------

async def _finish_purchase(
    query, context, plan_code: str, discount_code: str | None, method: str,
    renew_code: str | None = None,
) -> None:
    """خرید تازه یا تمدید را کامل می‌کند: اشتراک، پرداخت نمایشی،
    تحویل فوری کانفیگ و لینک، و رسید."""
    book = get_sub_book(context)
    user = query.from_user
    name = user.first_name if user else "کاربر"
    user_id = user.id if user else 0
    try:
        if renew_code:
            sub = book.renew_subscription(
                renew_code, plan_code=plan_code, discount_code=discount_code
            )
            record_renewal_payment(sub, method)
            payment = sub.get("last_payment")
        else:
            sub = book.create_subscription(
                user_id, name, plan_code, discount_code=discount_code
            )
            record_mock_payment(sub, method)
            payment = sub.get("payment")
    except ValueError as exc:
        await _replace_message(query, context, f"❌ {exc}", plans_keyboard())
        return
    context.user_data.pop("purchase", None)
    await _replace_message(query, context, format_delivery(sub), None)
    await context.bot.send_message(
        chat_id=query.message.chat_id, text=format_receipt(sub)
    )
    if method == "کارت‌به‌کارت":
        await context.bot.send_message(
            chat_id=query.message.chat_id,
            text=(
                f"💳 برای پرداخت کارت‌به‌کارت، مبلغ {format_toman(sub['price'] if not renew_code else payment['amount'])} "
                f"را به این شماره کارت بفرستید:\n{DEMO_CARD_NUMBER} "
                "(شماره‌ی نمایشی)\nبعد عکس رسید را همین‌جا بفرستید."
            ),
        )
        context.user_data["awaiting_receipt"] = sub["code"]


# ---------- دکمه‌ها (کال‌بک) ----------

async def on_button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """همه‌ی دکمه‌های شیشه‌ای اینجا مدیریت می‌شوند."""
    query = update.callback_query
    await query.answer()
    data = query.data or ""
    action, _, value = data.partition(":")

    if action == "plans":
        await _replace_message(query, context, format_plans(), plans_keyboard())
        return

    if action == "plan":
        await _replace_message(
            query, context, format_plan(value), plan_keyboard(value)
        )
        return

    if action == "buy":
        if value not in PLANS:
            await _replace_message(
                query, context, format_plan(value), plans_keyboard()
            )
            return
        clear_flow_states(context)
        context.user_data["purchase"] = {"plan": value, "discount_code": None}
        await _replace_message(
            query, context, format_purchase_summary(value), purchase_keyboard()
        )
        return

    if action == "discount":
        purchase = context.user_data.get("purchase")
        if not purchase:
            await _replace_message(
                query,
                context,
                "🎁 کد تخفیف روی خرید اعمال می‌شود؛ اول یک طرح انتخاب کنید.",
                plans_keyboard(),
            )
            return
        context.user_data["awaiting_discount"] = True
        await context.bot.send_message(
            chat_id=query.message.chat_id,
            text="🎁 کد تخفیف را بفرستید؛ مثال: سپهر۱۰",
        )
        return

    if action == "paym":
        purchase = context.user_data.get("purchase")
        if not purchase:
            return
        method = PAYMENT_CALLBACK.get(value)
        if method is None:
            return
        await _finish_purchase(
            query,
            context,
            purchase["plan"],
            purchase.get("discount_code"),
            method,
            renew_code=purchase.get("renew"),
        )
        return

    if action == "mysubs":
        user = query.from_user
        book = get_sub_book(context)
        subs = book.list_for_user(user.id if user else 0)
        markup = mysubs_keyboard(subs) if subs else plans_keyboard()
        await _replace_message(
            query, context, format_my_subscriptions(subs), markup
        )
        return

    if action == "sub":
        book = get_sub_book(context)
        sub = book.get(value)
        await _replace_message(
            query, context, format_subscription(sub, value), sub_keyboard(value)
        )
        return

    if action == "renew":
        book = get_sub_book(context)
        sub = book.get(value)
        if sub is None:
            await _replace_message(
                query, context, format_subscription(None, value), plans_keyboard()
            )
            return
        clear_flow_states(context)
        context.user_data["purchase"] = {
            "plan": sub["plan_code"],
            "discount_code": None,
            "renew": sub["code"],
        }
        await _replace_message(
            query,
            context,
            f"♻️ تمدید اشتراک {sub['code']} ({sub['plan_name']}):\n\n"
            + format_purchase_summary(sub["plan_code"]),
            purchase_keyboard(),
        )
        return

    if action == "reply":
        user = update.effective_user
        if not is_admin(user.id if user else 0, admin_id(context)):
            await _replace_message(
                query, context, "❌ این بخش فقط برای مدیر است.", None
            )
            return
        ticket = get_tickets(context).get(int(value))
        if ticket is None:
            await _replace_message(query, context, "❌ این تیکت پیدا نشد.", None)
            return
        clear_flow_states(context)
        context.user_data["awaiting_reply"] = ticket["id"]
        await _replace_message(
            query,
            context,
            f"✉️ پاسخ خود را برای {ticket['user_name']} بنویسید:\n"
            f"«{ticket['text']}»",
            None,
        )
        return

    if action == "admin":
        user = update.effective_user
        if not is_admin(user.id if user else 0, admin_id(context)):
            await _replace_message(
                query, context, "❌ این بخش فقط برای مدیر است.", None
            )
            return
        book = get_sub_book(context)
        sub = book.get(value)
        if sub is None:
            await _replace_message(
                query, context, format_subscription(None, value), None
            )
            return
        await _replace_message(
            query,
            context,
            f"{format_subscription(sub)}\n\n"
            f"مشتری: {sub['user_name']}\n"
            f"روش پرداخت: {sub['payment']['method'] if sub.get('payment') else 'پرداخت نشده ⏳'}",
            admin_sub_keyboard(value),
        )
        return

    if action == "extend":
        user = update.effective_user
        if not is_admin(user.id if user else 0, admin_id(context)):
            await _replace_message(
                query, context, "❌ این بخش فقط برای مدیر است.", None
            )
            return
        book = get_sub_book(context)
        sub = book.get(value)
        if sub is None:
            await _replace_message(
                query, context, format_subscription(None, value), None
            )
            return
        result = book.extend_subscription(value, 1)
        if sub["cancelled"] is False and "تمدید شد" in result:
            # تمدید را به مشتری خبر می‌دهد؛ اگر نرسید، جریان مدیر خراب نمی‌شود.
            try:
                await context.bot.send_message(
                    sub["user_id"],
                    format_status_push(sub, "♻️ اشتراک شما ۱ ماه تمدید شد."),
                )
            except Exception as exc:
                logger.warning("status push to customer %s failed: %s", sub["user_id"], exc)
        await _replace_message(
            query,
            context,
            f"{result}\n\n{format_admin_list(book.list_all())}",
            admin_keyboard(book),
        )
        return

    if action == "cancel":
        user = update.effective_user
        if not is_admin(user.id if user else 0, admin_id(context)):
            await _replace_message(
                query, context, "❌ این بخش فقط برای مدیر است.", None
            )
            return
        book = get_sub_book(context)
        sub = book.get(value)
        if sub is None:
            await _replace_message(
                query, context, format_subscription(None, value), None
            )
            return
        result = book.cancel_subscription(value)
        if "لغو شد" in result:
            try:
                await context.bot.send_message(
                    sub["user_id"],
                    format_status_push(sub, "❌ اشتراک شما لغو شد."),
                )
            except Exception as exc:
                logger.warning("status push to customer %s failed: %s", sub["user_id"], exc)
        await _replace_message(
            query,
            context,
            f"{result}\n\n{format_admin_list(book.list_all())}",
            admin_keyboard(book),
        )
        return

    if action == "adminlist":
        user = update.effective_user
        if not is_admin(user.id if user else 0, admin_id(context)):
            await _replace_message(
                query, context, "❌ این بخش فقط برای مدیر است.", None
            )
            return
        book = get_sub_book(context)
        await _replace_message(
            query,
            context,
            format_admin_list(book.list_all()),
            admin_keyboard(book),
        )
        return


# ---------- ساخت و اجرا ----------

def build_application(token: str, admin_user_id: int = 0) -> Application:
    """ساخت اپلیکیشن ربات و ثبت هندلرها."""
    app = Application.builder().token(token).build()
    app.bot_data["admin_id"] = admin_user_id
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("plans", plans_command))
    app.add_handler(CommandHandler("buy", buy_command))
    app.add_handler(CommandHandler("mysubs", mysubs_command))
    app.add_handler(CommandHandler("renew", renew_command))
    app.add_handler(CommandHandler("support", support_command))
    app.add_handler(CommandHandler("discount", discount_command))
    app.add_handler(CommandHandler("admin", admin_command))
    app.add_handler(CommandHandler("status", status_command))
    app.add_handler(CallbackQueryHandler(on_button))
    app.add_handler(MessageHandler(filters.PHOTO, photo_message))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_message))
    return app


def main() -> None:
    token = os.environ.get("BOT_TOKEN", "").strip()
    if not token:
        raise SystemExit(
            "BOT_TOKEN تنظیم نشده است. فایل .env.example را ببینید و "
            "توکن را در متغیر محیطی BOT_TOKEN قرار دهید."
        )

    try:
        admin_user_id = int(os.environ.get("ADMIN_USER_ID", "0") or "0")
    except ValueError:
        raise SystemExit("ADMIN_USER_ID باید عدد باشد (شناسه‌ی عددی مدیر در تلگرام).")

    mode = os.environ.get("BOT_MODE", "polling").strip().lower()
    app = build_application(token, admin_user_id)

    if mode == "webhook":
        webhook_url = os.environ.get("WEBHOOK_URL", "").strip()
        if not webhook_url:
            raise SystemExit(
                "در حالت وب‌هوک باید WEBHOOK_URL تنظیم شود؛ "
                "مثال: https://example.com"
            )
        port = int(os.environ.get("PORT", "8443"))
        logger.info("Starting in webhook mode on port %s: %s", port, webhook_url)
        app.run_webhook(
            listen="0.0.0.0",
            port=port,
            url_path=token,
            webhook_url=f"{webhook_url.rstrip('/')}/{token}",
        )
    elif mode == "polling":
        logger.info("Starting in polling mode...")
        app.run_polling()
    else:
        raise SystemExit(f"BOT_MODE نامعتبر: {mode!r} (مقادیر مجاز: polling یا webhook)")


if __name__ == "__main__":
    main()
