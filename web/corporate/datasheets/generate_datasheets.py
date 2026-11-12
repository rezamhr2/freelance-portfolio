#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""سازنده برگه‌های مشخصات فنی و کاتالوگ کامل — نمونه کار آریا صنعت توان.
اجرا: python3 generate_datasheets.py  (خروجی در همین پوشه)
مدل‌ها واقعی‌اند و مشخصات از برگه فنی سازنده گرفته شده است.
"""
import os
import re
import arabic_reshaper
from bidi.algorithm import get_display
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer,
                                Table, TableStyle, HRFlowable)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_RIGHT, TA_CENTER

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_R = "/usr/share/fonts/truetype/noto/NotoNaskhArabic-Regular.ttf"
FONT_B = "/usr/share/fonts/truetype/noto/NotoNaskhArabic-Bold.ttf"
FONT_L = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_LB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
pdfmetrics.registerFont(TTFont("Naskh", FONT_R))
pdfmetrics.registerFont(TTFont("NaskhB", FONT_B))
pdfmetrics.registerFont(TTFont("DejaVu", FONT_L))
pdfmetrics.registerFont(TTFont("DejaVuB", FONT_LB))

NAVY = HexColor("#0f3b5e")
AMBER = HexColor("#f59e0b")
LIGHT = HexColor("#eaf2fa")
GREY = HexColor("#475569")
LINE = HexColor("#cbd5e1")


_AR = re.compile(r'[\u0600-\u06FF\uFB50-\uFEFF\u200C\u200D]')
_LATIN_RUN = re.compile(r'[A-Za-z0-9]+(?:[ /.\-]+[A-Za-z0-9]+)*')


def fa(text, latin_font="DejaVu"):
    """شکل‌دهی و راست‌به‌چپ‌سازی متن فارسی برای نمایش در پی‌دی‌اف.
    قلم نسخ لاتین را چاپ نمی‌کند، پس تکه‌های لاتین را با قلم دژاوو می‌پوشانیم.
    تکه لاتین را در نشانه‌های جهت چپ‌به‌راست می‌گذاریم تا ترتیب عدد و حرف
    (مثل 376 FC) در متن راست‌به‌چپ به‌هم نریزد."""
    s = _LATIN_RUN.sub(lambda m: "\u202a" + m.group(0) + "\u202c", str(text))
    vis = get_display(arabic_reshaper.reshape(s))
    out, buf = [], []

    def flush():
        if buf:
            out.append('<font name="%s">%s</font>' % (latin_font, "".join(buf)))
            buf.clear()

    for ch in vis:
        if _AR.match(ch) or ch == " ":
            flush()
            out.append(ch)
        else:
            buf.append(ch)
    flush()
    return "".join(out)


S_TITLE = ParagraphStyle("t", fontName="NaskhB", fontSize=18, leading=26,
                         alignment=TA_RIGHT, textColor=NAVY)
S_H2 = ParagraphStyle("h2", fontName="NaskhB", fontSize=13, leading=20,
                      alignment=TA_RIGHT, textColor=NAVY)
S_BODY = ParagraphStyle("b", fontName="Naskh", fontSize=11, leading=19,
                        alignment=TA_RIGHT, textColor=HexColor("#1f2937"))
S_CELL = ParagraphStyle("c", fontName="Naskh", fontSize=10.5, leading=17,
                        alignment=TA_RIGHT)
S_CELL_B = ParagraphStyle("cb", fontName="NaskhB", fontSize=10.5, leading=17,
                          alignment=TA_RIGHT, textColor=NAVY)
S_FOOT = ParagraphStyle("f", fontName="Naskh", fontSize=9, leading=14,
                        alignment=TA_CENTER, textColor=GREY)
S_COVER = ParagraphStyle("cv", fontName="NaskhB", fontSize=26, leading=38,
                         alignment=TA_CENTER, textColor=NAVY)


def P(text, style=S_BODY):
    latin = "DejaVuB" if style.fontName == "NaskhB" else "DejaVu"
    return Paragraph(fa(text, latin), style)


def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Naskh", 9)
    canvas.setFillColor(GREY)
    canvas.drawCentredString(A4[0] / 2, 14 * mm,
                             get_display(arabic_reshaper.reshape(
                                 "آریا صنعت توان — برگه مشخصات فنی — نمونه کار")))
    canvas.setStrokeColor(AMBER)
    canvas.setLineWidth(2)
    canvas.line(15 * mm, A4[1] - 14 * mm, A4[0] - 15 * mm, A4[1] - 14 * mm)
    canvas.restoreState()


PRODUCTS = [
    {"id": "AT-2500", "cat": "ترانسفورماتور", "brand": "زیمنس",
     "name": "ترانسفورماتور خشک رزینی جیافول ۲۵۰۰",
     "desc": "ترانسفورماتور خشک رزینی بدون روغن، مناسب نصب در فضای بسته و ساختمان‌ها.",
     "specs": [("ولتاژ نامی", "۲۰ / ۰٫۴ کیلوولت"), ("توان نامی", "۲۵۰۰ کیلوولت‌آمپر"),
               ("نوع ترانسفورماتور", "خشک رزینی"), ("کلاس حرارتی", "F"),
               ("گروه برداری", "Dyn11"), ("گارانتی", "۲۴ ماه")]},
    {"id": "AT-1600", "cat": "ترانسفورماتور", "brand": "ای‌بی‌بی",
     "name": "ترانسفورماتور توزیع روغنی ۱۶۰۰",
     "desc": "ترانسفورماتور توزیع روغنی سه‌فاز با خنک‌کاری طبیعی، مناسب شبکه‌های توزیع شهری و صنعتی.",
     "specs": [("ولتاژ نامی", "۲۲ / ۰٫۴ کیلوولت"), ("توان نامی", "۱۶۰۰ کیلوولت‌آمپر"),
               ("نوع خنک‌کاری", "روغنی با گردش طبیعی"), ("تلفات بی‌باری", "۲۴۰۰ وات"),
               ("تلفات بارداری", "۱۷۷۰۰ وات در ۷۵ درجه"), ("گارانتی", "۲۴ ماه")]},
    {"id": "AT-33", "cat": "ترانسفورماتور", "brand": "ای‌بی‌بی",
     "name": "ترانسفورماتور ولتاژ تک‌فاز تی‌جی‌سی ۷",
     "desc": "ترانسفورماتور ولتاژ تک‌فاز با عایق رزینی، برای اندازه‌گیری و حفاظت در پست‌های فشار متوسط.",
     "specs": [("ولتاژ نامی", "۳۳/√۳ کیلوولت"), ("ولتاژ ثانویه", "۱۱۰/√۳ ولت"),
               ("بار نامی", "۱۰۰ ولت‌آمپر"), ("کلاس دقت", "۰٫۵"),
               ("وزن تقریبی", "۵۰ کیلوگرم"), ("گارانتی", "۱۸ ماه")]},
    {"id": "TT-5000", "cat": "تجهیزات آزمون", "brand": "مگر",
     "name": "دستگاه آزمون عایقی MIT515",
     "desc": "آزمون مقاومت عایقی با ولتاژ آزمون تا ۵ کیلوولت، برای نگهداری تجهیزات فشار قوی.",
     "specs": [("ولتاژ آزمون", "۲۵۰ تا ۵۰۰۰ ولت"), ("بازه مقاومت", "۱۰ کیلواهم تا ۱۰ ترااهم"),
               ("دقت اندازه‌گیری", "±۵٪ تا ۱ ترااهم"), ("رده حفاظتی", "CAT IV 600 ولت"),
               ("وزن تقریبی", "۴٫۵ کیلوگرم"), ("گارانتی", "۱۲ ماه")]},
    {"id": "TT-100", "cat": "تجهیزات آزمون", "brand": "مگر",
     "name": "اهم‌متر ترانسفورماتور MTO210",
     "desc": "اندازه‌گیری مقاومت مستقیم سیم‌پیچ ترانسفورماتور و موتور با جریان آزمون تا ۱۰ آمپر.",
     "specs": [("جریان آزمون", "تا ۱۰ آمپر مستقیم"), ("بازه اندازه‌گیری", "۱۰ میکرواهم تا ۲۰۰۰ اهم"),
               ("دقت اندازه‌گیری", "±۰٫۲۵٪"), ("تغذیه", "۸۵ تا ۲۶۴ ولت"),
               ("وزن تقریبی", "۱۳٫۱ کیلوگرم"), ("گارانتی", "۱۲ ماه")]},
    {"id": "TT-REL", "cat": "تجهیزات آزمون", "brand": "اومیکرون",
     "name": "مجموعه آزمون رله CMC 356",
     "desc": "مجموعه آزمون رله حفاظتی با شش خروجی جریان و چهار خروجی ولتاژ، برای آزمون همه نسل‌های رله.",
     "specs": [("خروجی جریان", "۶×۳۲ آمپر / ۳×۶۴ آمپر / ۱×۱۲۸ آمپر"), ("خروجی ولتاژ", "۴×۳۰۰ ولت"),
               ("دقت اندازه‌گیری", "خطا کمتر از ۰٫۰۸٪"), ("تغذیه مستقیم", "۰ تا ۲۶۴ ولت"),
               ("بازه فرکانس", "۱۰ تا ۱۰۰۰ هرتز"), ("گارانتی", "۱۸ ماه")]},
    {"id": "CB-20", "cat": "کابل و سیم", "brand": "پریسمیان",
     "name": "کابل قدرت N2XS2Y",
     "desc": "کابل قدرت سه‌رشته با عایق پلی‌اتیلن شبکه‌ای برای شبکه‌های فشار متوسط.",
     "specs": [("ولتاژ نامی", "۱۲ / ۲۰ کیلوولت"), ("سطح مقطع", "۳×۱۸۵ میلی‌متر مربع"),
               ("جنس هادی", "مس"), ("نوع عایق", "پلی‌اتیلن شبکه‌ای"),
               ("مقاومت هادی", "۰٫۰۹۹۱ اهم بر کیلومتر"), ("گارانتی", "۱۲ ماه")]},
    {"id": "CB-C", "cat": "کابل و سیم", "brand": "لپ",
     "name": "کابل کنترل اولفلکس کلاسیک ۱۱۰",
     "desc": "کابل کنترل ۱۲ رشته با رشته‌های شماره‌دار، برای مدارهای فرمان ماشین‌ها و تابلوها.",
     "specs": [("ولتاژ نامی", "۳۰۰ / ۵۰۰ ولت"), ("تعداد رشته", "۱۲×۱٫۵ میلی‌متر مربع"),
               ("ولتاژ آزمون", "۴ کیلوولت"), ("قطر خارجی", "۱۲ میلی‌متر"),
               ("دمای کار", "منفی ۴۰ تا ۸۰ درجه سانتی‌گراد"), ("گارانتی", "۱۲ ماه")]},
    {"id": "CB-I", "cat": "کابل و سیم", "brand": "لپ",
     "name": "کابل کنترل شیلددار اولفلکس کلاسیک ۱۱۰",
     "desc": "کابل کنترل شیلددار با بافت مسی قلع‌اندود، برای مدارهای فرمان در محیط‌های پرنویز.",
     "specs": [("ولتاژ نامی", "۳۰۰ / ۵۰۰ ولت"), ("تعداد رشته", "۱۲×۱٫۵ میلی‌متر مربع"),
               ("شیلد", "بافت مسی قلع‌اندود"), ("ولتاژ آزمون", "۴ کیلوولت"),
               ("جنس روکش", "پی‌وی‌سی"), ("گارانتی", "۱۲ ماه")]},
    {"id": "SW-24", "cat": "کلید و حفاظت", "brand": "زیمنس",
     "name": "کلید خلأ 3AH5",
     "desc": "کلید خلأ فشار متوسط با مکانیزم فنری، مناسب تابلوهای فشار متوسط و پست‌های توزیع.",
     "specs": [("ولتاژ نامی", "۲۴ کیلوولت"), ("جریان نامی", "۱۲۵۰ آمپر"),
               ("قدرت قطع", "۲۵ کیلوآمپر"), ("ولتاژ ضربه", "۱۲۵ کیلوولت"),
               ("مکانیزم", "فنری دستی"), ("گارانتی", "۲۴ ماه")]},
    {"id": "SW-R", "cat": "کلید و حفاظت", "brand": "ای‌بی‌بی",
     "name": "رله حفاظتی فیدر REF615",
     "desc": "رله حفاظتی دیجیتال فیدر با حفاظت اضافه‌جریان، خطای زمین و ثبت رویداد.",
     "specs": [("ورودی جریان", "۱ / ۵ آمپر"), ("ولتاژ تغذیه", "۸۰ تا ۲۵۰ ولت مستقیم"),
               ("دقت اندازه‌گیری", "±۰٫۵٪"), ("توابع حفاظتی", "اضافه‌جریان، خطای زمین، عدم تعادل"),
               ("وزن تقریبی", "۳٫۵ کیلوگرم"), ("گارانتی", "۲۴ ماه")]},
    {"id": "SW-33", "cat": "کلید و حفاظت", "brand": "زیمنس",
     "name": "سکسیونر 3DC",
     "desc": "سکسیونر سه‌پل با عایق رزینی، برای قطع و وصل خطوط فشار متوسط و حفاظت پرسنل.",
     "specs": [("ولتاژ نامی", "۳۶ کیلوولت"), ("جریان نامی", "۶۳۰ آمپر"),
               ("جریان کوتاه‌مدت", "۲۰ کیلوآمپر"), ("ولتاژ ضربه", "۱۷۰ کیلوولت"),
               ("نصب", "داخلی با عایق رزینی"), ("گارانتی", "۱۸ ماه")]},
    {"id": "MT-87", "cat": "ابزار اندازه‌گیری", "brand": "فلوک",
     "name": "مولتی‌متر صنعتی 87V",
     "desc": "مولتی‌متر دیجیتال صنعتی با اندازه‌گیری ولتاژ، جریان، مقاومت و ظرفیت.",
     "specs": [("ولتاژ", "تا ۱۰۰۰ ولت"), ("جریان", "تا ۱۰ آمپر"),
               ("دقت ولتاژ مستقیم", "±(۰٫۰۵٪ + ۱)"), ("رده حفاظتی", "CAT III 1000 ولت، CAT IV 600 ولت"),
               ("وزن تقریبی", "۳۵۵ گرم"), ("گارانتی", "۱۲ ماه")]},
    {"id": "MT-C", "cat": "ابزار اندازه‌گیری", "brand": "فلوک",
     "name": "کلمپ‌متر 376 FC",
     "desc": "کلمپ‌متر با پروب انعطاف‌پذیر همراه، برای اندازه‌گیری جریان‌های بالا بدون قطع مدار.",
     "specs": [("ولتاژ", "تا ۱۰۰۰ ولت"), ("جریان با دهانه", "تا ۱۰۰۰ آمپر"),
               ("جریان با پروب انعطاف‌پذیر", "تا ۲۵۰۰ آمپر"), ("دقت جریان دهانه", "۲٪ ±۵ رقم"),
               ("رده حفاظتی", "CAT III 1000 ولت، CAT IV 600 ولت"), ("گارانتی", "۱۲ ماه")]},
    {"id": "MT-Q", "cat": "ابزار اندازه‌گیری", "brand": "فلوک",
     "name": "تحلیل‌گر کیفیت توان 1775",
     "desc": "تحلیل‌گر کیفیت توان سه‌فاز با ثبت هارمونیک، افت ولتاژ و گذرای سریع.",
     "specs": [("ولتاژ ورودی", "تا ۱۰۰۰ ولت"), ("ورودی", "۴ ولتاژ + ۴ جریان"),
               ("دقت اندازه‌گیری", "کلاس ای"), ("هارمونیک", "تا مرتبه ۵۰ و تا ۳۰ کیلوهرتز"),
               ("گذرا", "تا ۸ کیلوولت با نمونه‌برداری ۱ مگاهرتز"), ("گارانتی", "۱۸ ماه")]},
]


def build_datasheet(p):
    path = os.path.join(HERE, p["id"] + ".pdf")
    doc = SimpleDocTemplate(path, pagesize=A4, rightMargin=18 * mm,
                            leftMargin=18 * mm, topMargin=22 * mm,
                            bottomMargin=20 * mm,
                            title="برگه مشخصات فنی " + p["id"])
    story = []
    story.append(P("آریا صنعت توان", ParagraphStyle(
        "co", fontName="NaskhB", fontSize=12, leading=18,
        alignment=TA_RIGHT, textColor=AMBER)))
    story.append(P(p["name"], S_TITLE))
    story.append(Paragraph(fa(p["id"]), ParagraphStyle(
        "mdl", fontName="DejaVuB", fontSize=12, leading=16,
        alignment=TA_RIGHT, textColor=GREY)))
    story.append(Spacer(1, 4 * mm))
    story.append(HRFlowable(width="100%", thickness=1, color=LINE))
    story.append(Spacer(1, 5 * mm))
    story.append(P("دسته: " + p["cat"], S_BODY))
    story.append(P("سازنده: " + p["brand"], S_BODY))
    story.append(P(p["desc"], S_BODY))
    story.append(Spacer(1, 5 * mm))
    story.append(P("مشخصات فنی", S_H2))
    story.append(Spacer(1, 2 * mm))
    rows = [[Paragraph(fa("مشخصه"), S_CELL_B), Paragraph(fa("مقدار"), S_CELL_B)]]
    for k, v in p["specs"]:
        rows.append([Paragraph(fa(k), S_CELL), Paragraph(fa(v), S_CELL)])
    t = Table(rows, colWidths=[55 * mm, 119 * mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), LIGHT),
        ("GRID", (0, 0), (-1, -1), 0.5, LINE),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
    ]))
    story.append(t)
    story.append(Spacer(1, 6 * mm))
    story.append(P("شرایط فروش و پشتیبانی", S_H2))
    story.append(P("قیمت این محصول به‌صورت عمده و بر اساس حجم سفارش اعلام می‌شود. "
                   "برای استعلام قیمت و زمان تحویل، از صفحه تماس درخواست خود را ثبت کنید.",
                   S_BODY))
    story.append(P("همه محصولات با برگه آزمون کارخانه و ضمانت‌نامه معتبر تحویل داده می‌شوند.",
                   S_BODY))
    doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
    return path


def build_catalogue():
    path = os.path.join(HERE, "catalogue.pdf")
    doc = SimpleDocTemplate(path, pagesize=A4, rightMargin=18 * mm,
                            leftMargin=18 * mm, topMargin=22 * mm,
                            bottomMargin=20 * mm, title="کاتالوگ محصولات آریا صنعت توان")
    story = []
    story.append(Spacer(1, 30 * mm))
    story.append(P("کاتالوگ محصولات", S_COVER))
    story.append(Spacer(1, 4 * mm))
    story.append(P("آریا صنعت توان", ParagraphStyle(
        "co2", fontName="NaskhB", fontSize=16, leading=24,
        alignment=TA_CENTER, textColor=AMBER)))
    story.append(Spacer(1, 6 * mm))
    story.append(P("توزیع‌کننده تجهیزات برق صنعتی — ترانسفورماتور، تجهیزات آزمون، "
                   "کابل و سیم، کلید و حفاظت، ابزار اندازه‌گیری", ParagraphStyle(
                       "sub", fontName="Naskh", fontSize=11, leading=19,
                       alignment=TA_CENTER, textColor=GREY)))
    story.append(Spacer(1, 10 * mm))
    story.append(P("این کاتالوگ شامل ۱۵ محصول در ۵ دسته است. برگه مشخصات فنی هر محصول "
                   "به‌صورت جداگانه نیز در وب‌سایت قابل دانلود است.", S_BODY))
    story.append(Spacer(1, 8 * mm))
    rows = [[Paragraph(fa(h), S_CELL_B) for h in
             ("ردیف", "مدل", "نام محصول", "سازنده")]]
    for i, p in enumerate(PRODUCTS, 1):
        rows.append([Paragraph(fa(str(i)), S_CELL),
                     Paragraph(fa(p["id"]), S_CELL),
                     Paragraph(fa(p["name"]), S_CELL),
                     Paragraph(fa(p["brand"]), S_CELL)])
    t = Table(rows, colWidths=[14 * mm, 24 * mm, 96 * mm, 40 * mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), LIGHT),
        ("GRID", (0, 0), (-1, -1), 0.5, LINE),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
    ]))
    story.append(t)
    story.append(Spacer(1, 8 * mm))
    for p in PRODUCTS:
        story.append(P(p["name"] + " — " + p["id"], S_H2))
        story.append(P(p["desc"], S_BODY))
        story.append(P("دسته: " + p["cat"] + " | سازنده: " + p["brand"] + " | گارانتی: " +
                       dict(p["specs"])["گارانتی"], S_BODY))
        story.append(Spacer(1, 3 * mm))
    doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
    return path


if __name__ == "__main__":
    for p in PRODUCTS:
        print("built", build_datasheet(p))
    print("built", build_catalogue())
    print("done:", len(PRODUCTS), "datasheets + catalogue")
