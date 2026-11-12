/**
 * نمونه کار — اسکریپت نمونه برای گوگل شیت مدیریت قیمت و موجودی
 * ============================================================
 *
 * برای استفاده در فایل واقعی کارفرما:
 *  ۱. در گوگل شیت، از منوی اکستنشنز گزینهٔ اپس اسکریپت را باز کنید.
 *  ۲. این کد را جایگذاری کنید و مقدارهای بخش «تنظیمات» را با
 *     نام برگه‌ها و ایمیل خودتان جایگزین کنید.
 *  ۳. با هر ویرایش شیت، ثبت خودکار تغییر قیمت اجرا می‌شود؛
 *     برای گزارش روزانه، از بخش تریگرها یک تریگر زمانی روزانه
 *     برای تابع sendLowStockReport بسازید.
 *
 * این اسکریپت هیچ ایمیلی به‌صورت خودکار «ارسال» نمی‌کند؛
 * گزارش کمبود موجودی فقط به‌صورت «پیش‌نویس» در جیمیل ساخته می‌شود
 * تا کاربر پیش از ارسال آن را ببیند و تأیید کند.
 */

// ------------------------------------------------------------------ تنظیمات
// این مقدارها را با مشخصات فایل واقعی جایگزین کنید.
const CONFIG = {
  SHEET_PRODUCTS: 'محصولات',              // نام برگهٔ محصولات
  SHEET_PRICE_LOG: 'تاریخچه تغییر قیمت',  // نام برگهٔ تاریخچهٔ تغییر قیمت
  PRICE_COL: 5,        // ستون قیمت فروش در برگهٔ محصولات (ستون E)
  STOCK_COL: 6,        // ستون موجودی (ستون F)
  MIN_STOCK_COL: 7,    // ستون حداقل موجودی (ستون G)
  FIRST_DATA_ROW: 3,   // اولین ردیف داده (ردیف ۱ عنوان و ردیف ۲ سرستون است)
  REPORT_EMAIL: 'example@email.com', // ← ایمیل گیرندهٔ گزارش را اینجا بنویسید
  TIMEZONE: 'Asia/Tehran'
};

// ------------------------------------------------- منوی اختصاصی در گوگل شیت
// با باز شدن فایل، یک منوی «مدیریت فروشگاه» به شیت اضافه می‌شود.
function onOpen() {
  SpreadsheetApp.getUi()
    .createMenu('مدیریت فروشگاه')
    .addItem('ثبت دستی تغییر قیمت انتخاب‌شده', 'logSelectedPriceChange')
    .addItem('ساخت پیش‌نویس گزارش کمبود موجودی', 'sendLowStockReport')
    .addToUi();
}

// ------------------------------------------- ثبت خودکار تغییر قیمت (onEdit)
// هر بار که قیمت فروش یک کالا در برگهٔ «محصولات» تغییر کند،
// یک ردیف تازه با قیمت قبلی، قیمت جدید و تاریخ به برگهٔ
// «تاریخچه تغییر قیمت» اضافه می‌شود.
function onEdit(e) {
  if (!e || !e.range) return; // اگر بدون رویداد ویرایش اجرا شد، کاری نکن.

  const sheet = e.range.getSheet();
  if (sheet.getName() !== CONFIG.SHEET_PRODUCTS) return;

  // فقط تغییر در ستون قیمت فروش، و فقط در ردیف‌های داده.
  if (e.range.getColumn() !== CONFIG.PRICE_COL) return;
  if (e.range.getRow() < CONFIG.FIRST_DATA_ROW) return;
  if (e.range.getNumRows() !== 1) return; // تغییر گروهی را ثبت نمی‌کنیم.

  const row = e.range.getRow();
  const newPrice = e.range.getValue();
  const oldPrice = e.oldValue;

  // اگر قیمت قبلی در دسترس نیست (مثلاً سلول خالی بوده)، ثبت نمی‌کنیم.
  if (oldPrice === undefined || oldPrice === null || oldPrice === '') return;
  if (Number(newPrice) === Number(oldPrice)) return; // بدون تغییر واقعی.

  const productCode = sheet.getRange(row, 1).getValue();
  const productName = sheet.getRange(row, 2).getValue();
  const today = Utilities.formatDate(new Date(), CONFIG.TIMEZONE, 'yyyy-MM-dd');

  const logSheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(CONFIG.SHEET_PRICE_LOG);
  if (!logSheet) return;

  // ستون‌ها: تاریخ | کد کالا | نام محصول | قیمت قبلی | قیمت جدید | تغییر | تغییر ٪ | دلیل
  // ستون‌های تغییر (تومان و درصد) در شیت با فرمول محاسبه می‌شوند، پس خالی می‌مانند.
  // «دلیل» را کاربر بعداً دستی می‌نویسد؛ تاریخ به میلادی ثبت می‌شود
  // چون تبدیل به تاریخ جلالی در اپس اسکریپت به کتابخانهٔ جداگانه نیاز دارد.
  logSheet.appendRow([
    today,
    productCode,
    productName,
    Number(oldPrice),
    Number(newPrice),
    '',
    '',
    'ثبت خودکار — دلیل را وارد کنید'
  ]);
}

// ------------------------------- ثبت دستی تغییر قیمت ردیف انتخاب‌شده
// اگر onEdit در دسترس نبود (مثلاً قیمت با فرمول یا با ایمپورت تغییر کرده)،
// کاربر می‌تواند ردیف کالا را انتخاب کند و از منو این گزینه را بزند؛
// در این حالت قیمت قبلی را از کاربر می‌پرسد.
function logSelectedPriceChange() {
  const ui = SpreadsheetApp.getUi();
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(CONFIG.SHEET_PRODUCTS);
  if (!sheet) return; // برگهٔ محصولات پیدا نشد.
  const cell = sheet.getActiveCell();
  const row = cell.getRow();
  if (row < CONFIG.FIRST_DATA_ROW) {
    ui.alert('لطفاً یک ردیف کالا (ردیف ۳ به بعد) را انتخاب کنید.');
    return;
  }
  const answer = ui.prompt('قیمت قبلی (تومان)', 'قیمت قبلی این کالا را وارد کنید:', ui.ButtonSet.OK_CANCEL);
  if (answer.getSelectedButton() !== ui.Button.OK) return;
  const oldPrice = Number(answer.getResponseText());
  if (!oldPrice) {
    ui.alert('قیمت قبلی معتبر نیست.');
    return;
  }
  const newPrice = sheet.getRange(row, CONFIG.PRICE_COL).getValue();
  const today = Utilities.formatDate(new Date(), CONFIG.TIMEZONE, 'yyyy-MM-dd');
  const logSheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(CONFIG.SHEET_PRICE_LOG);
  logSheet.appendRow([
    today,
    sheet.getRange(row, 1).getValue(),
    sheet.getRange(row, 2).getValue(),
    oldPrice,
    newPrice,
    '',
    '',
    'ثبت دستی — دلیل را وارد کنید'
  ]);
  ui.alert('تغییر قیمت در برگهٔ «تاریخچه تغییر قیمت» ثبت شد.');
}

// -------------------------------------- پیش‌نویس گزارش روزانهٔ کمبود موجودی
// کالاهایی را که موجودی‌شان به حداقل یا کمتر از آن رسیده پیدا می‌کند
// و یک پیش‌نویس ایمیل در جیمیل می‌سازد (ارسال نمی‌کند).
// برای اجرای روزانه: در اپس اسکریپت از بخش تریگرها یک تریگر زمانی
// (زمان‌محور، روزانه) برای همین تابع بسازید.
function sendLowStockReport() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const sheet = ss.getSheetByName(CONFIG.SHEET_PRODUCTS);
  if (!sheet) return;

  const lastRow = sheet.getLastRow();
  if (lastRow < CONFIG.FIRST_DATA_ROW) return; // هنوز کالایی ثبت نشده است.
  const data = sheet.getRange(CONFIG.FIRST_DATA_ROW, 1, lastRow - CONFIG.FIRST_DATA_ROW + 1, 7).getValues();

  const lowItems = [];
  for (const row of data) {
    const code = row[0];
    const name = row[1];
    const stock = Number(row[5]);
    const minStock = Number(row[6]);
    if (!name) continue;
    if (stock <= minStock) {
      lowItems.push({ code: code, name: name, stock: stock, minStock: minStock });
    }
  }

  if (lowItems.length === 0) return; // چیزی برای گزارش نیست.

  const today = Utilities.formatDate(new Date(), CONFIG.TIMEZONE, 'yyyy-MM-dd');
  let body = '<p>سلام،</p>';
  body += '<p>کالاهای زیر به حداقل موجودی رسیده‌اند و نیاز به سفارش دارند:</p>';
  body += '<table border="1" cellpadding="6" cellspacing="0" dir="rtl" style="border-collapse: collapse;">';
  body += '<tr><th>کد کالا</th><th>نام محصول</th><th>موجودی</th><th>حداقل موجودی</th></tr>';
  for (const item of lowItems) {
    body += '<tr><td>' + item.code + '</td><td>' + item.name + '</td><td>' +
      item.stock + '</td><td>' + item.minStock + '</td></tr>';
  }
  body += '</table>';
  body += '<p>این گزارش به‌صورت خودکار از گوگل شیت مدیریت قیمت و موجودی ساخته شده است.</p>';

  // فقط پیش‌نویس ساخته می‌شود؛ ارسال با تأیید دستی کاربر انجام می‌شود.
  GmailApp.createDraft(
    CONFIG.REPORT_EMAIL,
    'گزارش کمبود موجودی — ' + today + ' (' + lowItems.length + ' کالا)',
    '',
    { htmlBody: body }
  );
}
