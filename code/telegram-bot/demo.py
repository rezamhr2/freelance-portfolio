# demo.py — نمایش آفلاین کل جریان ربات فروش اشتراک، بدون نیاز به تلگرام
# اجرا: python3 demo.py
# این اسکریپت فقط منطق خالص plans.py و subs.py را اجرا می‌کند؛
# هیچ اتصالی به تلگرام برقرار نمی‌شود و توکن لازم نیست.
# خروجی دقیقاً همان پیام‌هایی است که مشتری و مدیر در تلگرام می‌بینند،
# پس کارفرما بدون نصب چیزی می‌فهمد ربات چه کار می‌کند.

import os

from plans import PLANS, format_plan, format_plans
from subs import (
    BRAND_NAME,
    DEMO_DOMAIN,
    HOME_MENU,
    SubscriptionBook,
    SupportTickets,
    _add_months,
    apply_discount_text,
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
    record_mock_payment,
    record_renewal_payment,
    subscription_status,
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def say(who: str, text: str) -> None:
    """یک پیام را مثل گفت‌وگوی تلگرام چاپ می‌کند."""
    print(f"─── {who} ───")
    print(text)
    print()


def main() -> None:
    book = SubscriptionBook()
    tickets = SupportTickets()
    customer_id = 123456789
    customer_name = "مشتری نمونه"

    print(f"🛍 نمایش ربات «{BRAND_NAME}» — نمونه کار")
    print("همه‌ی مرحله‌ها آفلاین اجرا می‌شوند؛ توکن و اتصال لازم نیست.")
    print()

    # ۱) شروع: خوش‌آمد با خط‌های اعتماد و وضعیت واقعی مشتری
    say("مشتری", "/start")
    # خوش‌آمد متنی است؛ لوگو روی عکس پروفایل ربات است، نه در پیام.
    welcome0 = format_welcome(customer_name, 0)
    say("ربات", welcome0)
    say("ربات", "دکمه‌های پایین صفحه: " + " | ".join(
        button for row in HOME_MENU for button in row
    ))

    # ۲) مرور طرح‌ها با جدول قیمت درون‌چتی
    say("مشتری", "«🚀 خرید اشتراک» را می‌زند.")
    say("ربات", format_plans())

    # ۳) دیدن جزئیات یک طرح
    say("مشتری", "روی «۱ ماهه» می‌زند.")
    plan_text = format_plan("m1")
    say("ربات", plan_text)

    # ۴) کد تخفیف: اول اشتباه، بعد درست (با ارقام لاتین هم)
    say("مشتری", "کد تخفیف «اشتباه» را می‌فرستد.")
    say("ربات", apply_discount_text("اشتباه", 200000))
    say("مشتری", "کد تخفیف «سپهر۱۰» را می‌فرستد.")
    discount_msg, discount_amount = apply_discount_text("سپهر۱۰", 200000)
    say("ربات", discount_msg)

    # ۵) خلاصه‌ی خرید و ثبت اشتراک اول (۱ ماهه، با تخفیف)
    say("مشتری", "«🚀 خرید این طرح» را می‌زند.")
    say("ربات", format_purchase_summary("m1", "سپهر۱۰"))
    say("مشتری", "روش پرداخت «درگاه آنلاین» را انتخاب می‌کند.")
    sub1 = book.create_subscription(
        customer_id, customer_name, "m1", discount_code="سپهر۱۰"
    )
    record_mock_payment(sub1, "درگاه آنلاین")
    say("ربات", format_delivery(sub1))
    say("ربات", format_receipt(sub1))
    code1 = sub1["code"]

    # ۶) اشتراک دوم برای همان مشتری (۱۲ ماهه، کارت‌به‌کارت)
    say("مشتری", "یک اشتراک دوم می‌خرد (۱۲ ماهه، کارت‌به‌کارت).")
    sub2 = book.create_subscription(customer_id, customer_name, "m12")
    record_mock_payment(sub2, "کارت‌به‌کارت")
    say("ربات", format_delivery(sub2))
    say(
        "ربات",
        "💳 برای پرداخت کارت‌به‌کارت، مبلغ را به شماره‌ی کارت نمایشی بفرستید "
        "و عکس رسید را همین‌جا بفرستید.",
    )
    code2 = sub2["code"]

    # ۷) «اشتراک‌های من»
    say("مشتری", "«📲 اشتراک‌های من» را می‌زند.")
    say("ربات", format_my_subscriptions(book.list_for_user(customer_id)))

    # ۸) تمدید اشتراک اول با همان طرح
    say("مشتری", "«♻️ تمدید این اشتراک» را برای اشتراک اول می‌زند.")
    old_expiry = sub1["expires_at"]
    book.renew_subscription(code1)
    renewal_payment = record_renewal_payment(sub1, "درگاه آنلاین")
    say("ربات", f"✅ اشتراک {code1} تمدید شد.")
    say("ربات", format_receipt(sub1))

    # ۹) پنل مدیر: فهرست اشتراک‌ها، تمدید دستی و لغو
    say("مدیر", "/admin")
    say("ربات", format_admin_list(book.list_all()))
    say("مدیر", f"اشتراک {code2} را ۱ ماه تمدید می‌کند.")
    old_expiry2 = sub2["expires_at"]
    say("ربات", book.extend_subscription(code2, 1))
    say("ربات", "📩 پیامی که مشتری می‌گیرد:")
    say("ربات", format_status_push(sub2, "♻️ اشتراک شما ۱ ماه تمدید شد."))
    say("مدیر", f"اشتراک {code2} را لغو می‌کند.")
    say("ربات", book.cancel_subscription(code2))
    say("ربات", "📩 پیامی که مشتری می‌گیرد:")
    say("ربات", format_status_push(sub2, "❌ اشتراک شما لغو شد."))

    # ۱۰) پیگیری با کد اشتباه
    say("مشتری", "کد اشتباه SP-9999 را می‌فرستد.")
    say("ربات", format_subscription(book.get("SP-9999"), "SP-9999"))

    # ۱۱) پشتیبانی: تیکت مشتری و پاسخ مدیر
    say("مشتری", "«🎧 پشتیبانی» را می‌زند و پیام می‌فرستد.")
    ticket = tickets.create_ticket(
        customer_id, customer_name, "سلام، کانفیگ من وصل نمی‌شود."
    )
    say("ربات", "✅ پیام شما به پشتیبانی رسید. پاسخ را همین‌جا می‌گیرید.")
    say("مدیر", "/admin — تیکت‌های باز:")
    say("ربات", format_tickets(tickets.list_open()))
    say("مدیر", "به تیکت پاسخ می‌دهد.")
    tickets.answer_ticket(ticket["id"], "سلام! کانفیگ تازه برای شما فرستاده شد.")
    say("ربات", "🎧 پاسخ پشتیبانی:\nسلام! کانفیگ تازه برای شما فرستاده شد.")

    # ۱۲) خوش‌آمد دوباره: حالا یک اشتراک فعال دارد
    say("مشتری", "دوباره /start می‌زند.")
    welcome1 = format_welcome(
        customer_name,
        sum(1 for s in book.list_for_user(customer_id) if is_active(s)),
    )
    say("ربات", welcome1)

    # بررسی‌های خودکار
    menu_labels = [b for row in HOME_MENU for b in row]
    assert len(menu_labels) == 6, "منوی اصلی باید شش دکمه داشته باشد"
    for label in ("🚀 خرید اشتراک", "📲 اشتراک‌های من", "♻️ تمدید اشتراک",
                  "🎁 کد تخفیف", "🎧 پشتیبانی", "❓ راهنما"):
        assert label in menu_labels, f"دکمه‌ی «{label}» باید در منوی اصلی باشد"
    assert PLANS["m1"]["price_toman"] == 200000, "قیمت ۱ ماهه باید ۲۰۰٬۰۰۰ باشد"
    assert PLANS["m2"]["price_toman"] == 360000, "قیمت ۲ ماهه باید ۳۶۰٬۰۰۰ باشد"
    assert PLANS["m3"]["price_toman"] == 510000, "قیمت ۳ ماهه باید ۵۱۰٬۰۰۰ باشد"
    assert PLANS["m6"]["price_toman"] == 960000, "قیمت ۶ ماهه باید ۹۶۰٬۰۰۰ باشد"
    assert PLANS["m12"]["price_toman"] == 1800000, "قیمت ۱۲ ماهه باید ۱٬۸۰۰٬۰۰۰ باشد"
    plans_text = format_plans()
    assert "200,000 تومان" in plans_text, "جدول قیمت باید ارزان‌ترین طرح را نشان بدهد"
    assert "1,800,000 تومان" in plans_text, "جدول قیمت باید گران‌ترین طرح را نشان بدهد"
    assert "۱۲ ماهه" in plans_text, "جدول قیمت باید طرح ۱۲ ماهه را داشته باشد"
    assert plan_text == (
        "📋 ۱ ماهه\n"
        "مدت: 1 ماه\n"
        "کاربر: نامحدود\n"
        "قیمت: 200,000 تومان\n"
        "یک ماه، کاربر نامحدود"
    ), "متن جزئیات طرح نباید عوض شده باشد"
    assert "پیدا نشد" in format_plan("bad"), "طرح نامعتبر باید پیام خطا بدهد"
    assert "معتبر نیست" in apply_discount_text("اشتباه", 200000), "کد نامعتبر باید خطا بدهد"
    assert discount_for("سپهر10", 200000) == ("سپهر۱۰", 10, 20000), (
        "کد با ارقام لاتین هم باید پذیرفته شود"
    )
    assert "۱۰٪ تخفیف" in discount_msg, "پیام تخفیف باید درصد را بگوید"
    assert discount_amount == 20000, "تخفیف ۱۰٪ روی ۲۰۰٬۰۰۰ باید ۲۰٬۰۰۰ باشد"
    summary = format_purchase_summary("m1", "سپهر۱۰")
    assert "۱ ماهه" in summary, "خلاصه باید نام طرح را نشان بدهد"
    assert "200,000 تومان" in summary, "خلاصه باید قیمت طرح را نشان بدهد"
    assert "−20,000 تومان" in summary, "خلاصه باید مبلغ تخفیف را نشان بدهد"
    assert "180,000 تومان" in summary, "خلاصه باید مبلغ نهایی را نشان بدهد"
    assert code1 == "SP-1001", "اولین کد اشتراک باید SP-1001 باشد"
    assert sub1["price"] == 180000, "قیمت اشتراک اول بعد از تخفیف باید ۱۸۰٬۰۰۰ باشد"
    assert sub1["discount_code"] == "سپهر۱۰", "کد تخفیف باید روی اشتراک بماند"
    assert sub1["discount_amount"] == 20000, "مبلغ تخفیف باید روی اشتراک بماند"
    assert subscription_status(sub1) == "فعال", "اشتراک تازه باید فعال باشد"
    assert sub1["expires_at"] > sub1["created_at"], "انقضا باید بعد از ثبت باشد"
    assert sub1["expires_at"] == _add_months(old_expiry, 1), (
        "تمدید باید دقیقاً یک ماه به انقضا اضافه کند"
    )
    assert sub1["payment"] is not None, "رسید باید بعد از پرداخت ثبت شده باشد"
    assert sub1["payment"]["method"] == "درگاه آنلاین", "روش پرداخت تمدید باید ثبت شده باشد"
    assert sub1["payment"]["amount"] == 200000, "مبلغ تمدید باید قیمت طرح باشد"
    assert renewal_payment["payment_id"] == "PAY-SP-1001-R1", (
        "شناسه‌ی پرداخت تمدید باید درست باشد"
    )
    assert "200,000" in format_receipt(sub1), "رسید تمدید باید مبلغ درست را نشان بدهد"
    delivery1 = format_delivery(sub1)
    assert code1 in delivery1, "پیام تحویل باید کد اشتراک را بگوید"
    assert DEMO_DOMAIN in delivery1, "پیام تحویل باید دامنهٔ نمایشی را بگوید"
    assert f"https://{DEMO_DOMAIN}/s/{code1}" in delivery1, (
        "پیام تحویل باید لینک اشتراک را بگوید"
    )
    assert "کانفیگ نمایشی" in delivery1, "پیام تحویل باید کانفیگ را بگوید"
    assert code2 == "SP-1002", "دومین کد اشتراک باید SP-1002 باشد"
    assert sub2["price"] == 1800000, "قیمت اشتراک دوم باید ۱٬۸۰۰٬۰۰۰ باشد"
    assert sub2["payment"]["method"] == "کارت‌به‌کارت", "روش پرداخت دوم باید ثبت شده باشد"
    mine = book.list_for_user(customer_id)
    assert [s["code"] for s in mine] == ["SP-1002", "SP-1001"], (
        "اشتراک‌های من باید هر دو اشتراک را از تازه‌ترین نشان بدهد"
    )
    assert book.list_for_user(999) == [], "مشتری دیگر نباید اشتراکی ببیند"
    mine_text = format_my_subscriptions(mine)
    assert "SP-1001" in mine_text and "SP-1002" in mine_text, (
        "فهرست اشتراک‌های من باید کدها را نشان بدهد"
    )
    assert "هنوز اشتراکی" in format_my_subscriptions([]), (
        "مشتری بدون اشتراک باید پیام راهنما بگیرد"
    )
    assert sub1["renewals"] == 1, "تمدید باید یک بار شمرده شود"
    assert sub2["expires_at"] > old_expiry2, "تمدید دستی مدیر باید انقضا را جلو ببرد"
    push_extend = format_status_push(sub2, "♻️ اشتراک شما ۱ ماه تمدید شد.")
    assert "تمدید" in push_extend and code2 in push_extend, (
        "پیام تمدید باید مرحله و کد را بگوید"
    )
    assert subscription_status(sub2) == "لغو شده", "اشتراک لغوشده باید لغو شده باشد"
    push_cancel = format_status_push(sub2, "❌ اشتراک شما لغو شد.")
    assert "لغو" in push_cancel and code2 in push_cancel, (
        "پیام لغو باید مرحله و کد را بگوید"
    )
    try:
        book.renew_subscription(code2)
        raise AssertionError("تمدید اشتراک لغوشده باید خطا بدهد")
    except ValueError:
        pass
    assert book.get("SP-9999") is None, "کد نامعتبر نباید اشتراکی بدهد"
    assert "پیدا نشد" in format_subscription(None, "SP-9999"), (
        "کد نامعتبر باید پیام خطا بدهد"
    )
    assert "پیدا نشد" in book.extend_subscription("SP-9999"), (
        "تمدید کد نامعتبر باید خطا بدهد"
    )
    assert "پیدا نشد" in book.cancel_subscription("SP-9999"), (
        "لغو کد نامعتبر باید خطا بدهد"
    )
    assert ticket["id"] == 1, "اولین تیکت باید شماره‌ی ۱ بگیرد"
    assert tickets.list_open() == [], "بعد از پاسخ، تیکت باز نباید بماند"
    assert tickets.get(1)["answered"] is True, "تیکت باید پاسخ‌داده‌شده ثبت شود"
    assert "تحویل فوری" in welcome0, "خوش‌آمد باید خط تحویل فوری را داشته باشد"
    assert "پشتیبانی ۲۴ ساعته" in welcome0, "خوش‌آمد باید خط پشتیبانی را داشته باشد"
    assert "اشتراک‌های فعال شما: 0" in welcome0, "خوش‌آمد اول باید صفر اشتراک فعال نشان بدهد"
    assert "اشتراک‌های فعال شما: 1" in welcome1, "خوش‌آمد باید تعداد واقعی اشتراک فعال را نشان بدهد"
    admin_list = format_admin_list(book.list_all())
    assert "SP-1001" in admin_list and "SP-1002" in admin_list, (
        "پنل مدیر باید هر دو اشتراک را نشان بدهد"
    )
    # نگهبان واژه‌ها: هیچ کلمهٔ ممنوعه‌ای در کد ربات و پیام‌هایش نباشد
    sources = ""
    for fname in ("bot.py", "plans.py", "subs.py"):
        with open(os.path.join(BASE_DIR, fname), encoding="utf-8") as fh:
            sources += fh.read()
    banned = "vp" + "n"
    assert banned not in sources.lower(), "کلمهٔ ممنوعه نباید در کد ربات باشد"
    shown = (
        welcome0 + welcome1 + plans_text + plan_text + discount_msg
        + format_delivery(sub1) + format_delivery(sub2)
        + format_receipt(sub1) + mine_text + admin_list
    )
    banned2 = "فیلتر" + "شکن"
    assert banned2 not in shown, "کلمهٔ ممنوعه نباید در پیام‌های ربات باشد"
    # نگهبان حجم: طرح‌ها فقط زمانی‌اند
    gig = "گی" + "گ"
    assert gig not in sources, "حجم نباید در کد ربات باشد"
    assert ("g" + "b") not in sources.lower(), "حجم نباید در کد ربات باشد"
    assert gig not in shown, "حجم نباید در پیام‌های ربات باشد"
    print("✅ همه‌ی بررسی‌ها موفق بود — جریان کامل از خرید اشتراک تا تمدید و پشتیبانی کار می‌کند.")


if __name__ == "__main__":
    main()
