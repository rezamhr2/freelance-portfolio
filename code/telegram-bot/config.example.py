# نمونه‌ی تنظیمات (جایگزین ساده‌ی .env برای کسانی که فایل env نمی‌خواهند)
# استفاده: این فایل را به نام config.py کپی کنید و توکن واقعی را جایگذاری کنید.
# فایل config.py واقعی را هرگز برای کسی ارسال نکنید.

BOT_TOKEN = "PASTE_YOUR_BOT_TOKEN_HERE"  # توکن ربات از بات‌فادر
BOT_MODE = "polling"  # polling یا webhook
WEBHOOK_URL = "https://example.com"  # فقط در حالت webhook لازم است
PORT = 8443  # فقط در حالت webhook
ADMIN_USER_ID = 0  # شناسه‌ی عددی مدیر در تلگرام؛ صفر یعنی پنل مدیر خاموش است
