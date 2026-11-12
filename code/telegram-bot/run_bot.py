# run_bot.py — نگهبان ربات «سپهر» (فقط کتابخانه‌ی استاندارد پایتون)
#
# ربات را اجرا می‌کند و اگر از کار بیفتد، با وقفه‌ی نماییِ روبه‌افزایش
# (cooldown) دوباره بالا می‌آورد تا ربات بیشترِ وقت روشن باشد:
#   - اولین تلاشِ دوباره بعد از ۶۰ ثانیه، بعد ۱۲۰، ۲۴۰، ۴۸۰، تا سقف ۹۰۰ ثانیه.
#   - اگر یک اجرا بیش از ۱۰ دقیقه سالم کار کند، وقفه به ۶۰ ثانیه برمی‌گردد.
#   - اگر ربات ۵ بار پشت سر هم در کمتر از ۶۰ ثانیه بمیرد (خطای پیکربندی یا
#     توکن اشتباه)، نگهبان دیگر تلاش نمی‌کند و با خطا خارج می‌شود — کوبیدن
#     بی‌فایده به تلگرام، فقط حساب را به دردسر می‌اندازد.
#   - هر اجرا حداکثر ۳۴۰ دقیقه طول می‌کشد (پیش از سقف ۳۵۰ دقیقه‌ایِ
#     گیت‌هاب اکشنز)، بعد ربات را تمیز متوقف می‌کند تا اجرای بعدیِ
#     زمان‌بندی‌شده آن را دوباره بالا بیاورد.
#
# پیام به مدیر (فقط با ADMIN_USER_ID): روشن شدن در شروع اجرا و توقف
# زمان‌بندی‌شده. تلاش‌های دوباره‌ی وسط اجرا فقط در لاگ می‌آیند، نه در
# تلگرام مدیر — تا مدیر اسپم نشود.
#
# پیام به کاربر سمت ربات است، نه اینجا: متن خوش‌آمد و دستور /status به
# کاربر می‌گویند ربات هر ۶ ساعت چند دقیقه استراحت می‌کند و برمی‌گردد.
# ربات خاموش نمی‌تواند پیام بدهد، پس «پیام قطعی» باید از پیش در متن
# ربات باشد — همین‌طور هم هست.
#
# اجرا:  BOT_TOKEN=... ADMIN_USER_ID=... python run_bot.py
# متغیرهای اختیاری: RUN_BUDGET_MINUTES (پیش‌فرض 340)،
#   BACKOFF_INITIAL_SECONDS (پیش‌فرض 60)، BACKOFF_MAX_SECONDS (پیش‌فرض 900).

import json
import logging
import os
import signal
import subprocess
import sys
import time
import urllib.request

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger("run_bot")

HERE = os.path.dirname(os.path.abspath(__file__))
BOT_SCRIPT = os.path.join(HERE, "bot.py")

RUN_BUDGET_SECONDS = int(os.environ.get("RUN_BUDGET_MINUTES", "340") or "340") * 60
BACKOFF_INITIAL = int(os.environ.get("BACKOFF_INITIAL_SECONDS", "60") or "60")
BACKOFF_MAX = int(os.environ.get("BACKOFF_MAX_SECONDS", "900") or "900")
HEALTHY_RUN_SECONDS = 600
MAX_FAST_FAILURES = 5
GRACE_SECONDS = 20

_shutdown = False


def _handle_signal(signum, frame):
    global _shutdown
    _shutdown = True
    logger.info("signal %s received, shutting down gracefully...", signum)


signal.signal(signal.SIGTERM, _handle_signal)
signal.signal(signal.SIGINT, _handle_signal)


def _notify_admin(token: str, admin_id: int, text: str) -> None:
    """یک پیام به مدیر بفرست؛ اگر نشد، فقط لاگ کن — نگهبان نباید بمیرد."""
    if not token or not admin_id:
        return
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = json.dumps({"chat_id": admin_id, "text": text}).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            resp.read()
    except Exception as exc:  # noqa: BLE001 - best effort only
        logger.warning("could not notify admin: %s", exc)


def _sleep_with_shutdown(seconds: float) -> bool:
    """بخواب، ولی اگر سیگنال توقف آمد زود برگرد. True یعنی توقف خواسته شد."""
    deadline = time.time() + seconds
    while time.time() < deadline:
        if _shutdown:
            return True
        time.sleep(min(1.0, deadline - time.time()))
    return _shutdown


def _stop_child(proc: subprocess.Popen) -> None:
    """فرزند را تمیز متوقف کن: اول SIGTERM، بعد از مهلت SIGKILL."""
    if proc.poll() is not None:
        return
    proc.terminate()
    try:
        proc.wait(timeout=GRACE_SECONDS)
    except subprocess.TimeoutExpired:
        logger.warning("bot did not stop in %ss, killing it", GRACE_SECONDS)
        proc.kill()
        proc.wait()


def main() -> int:
    token = os.environ.get("BOT_TOKEN", "").strip()
    if not token:
        logger.error("BOT_TOKEN is not set.")
        return 1
    try:
        admin_id = int(os.environ.get("ADMIN_USER_ID", "0") or "0")
    except ValueError:
        logger.error("ADMIN_USER_ID must be a number.")
        return 1

    env = dict(os.environ)
    env["BOT_MODE"] = env.get("BOT_MODE", "polling").strip().lower() or "polling"

    started_at = time.time()
    backoff = BACKOFF_INITIAL
    fast_failures = 0
    first_start = True

    while True:
        if _shutdown:
            break
        if time.time() - started_at >= RUN_BUDGET_SECONDS:
            logger.info("run budget reached, stopping cleanly.")
            break

        logger.info("starting bot.py (backoff=%ss)...", backoff)
        proc = subprocess.Popen(
            [sys.executable, BOT_SCRIPT],
            env=env,
            cwd=HERE,
        )
        if first_start:
            _notify_admin(token, admin_id, "✅ ربات سپهر روشن شد.")
            first_start = False

        run_started = time.time()
        while proc.poll() is None:
            if _shutdown or time.time() - started_at >= RUN_BUDGET_SECONDS:
                _stop_child(proc)
                break
            time.sleep(1)

        if _shutdown or time.time() - started_at >= RUN_BUDGET_SECONDS:
            break

        runtime = time.time() - run_started
        code = proc.returncode
        logger.warning("bot exited with code %s after %.0fs", code, runtime)

        if runtime >= HEALTHY_RUN_SECONDS:
            # A long healthy run: the failure was transient, reset the cooldown.
            backoff = BACKOFF_INITIAL
            fast_failures = 0
        else:
            fast_failures += 1
            if fast_failures >= MAX_FAST_FAILURES:
                logger.error(
                    "bot died %s times in a row within 60s — likely a config "
                    "or token problem, not a transient failure. Giving up.",
                    fast_failures,
                )
                return 1

        logger.info("retrying in %ss (fast failures: %s)...", backoff, fast_failures)
        if _sleep_with_shutdown(backoff):
            break
        backoff = min(backoff * 2, BACKOFF_MAX)

    _notify_admin(
        token,
        admin_id,
        "⏸ ربات سپهر برای استراحت زمان‌بندی‌شده متوقف شد؛ تا چند دقیقه دیگر برمی‌گردد.",
    )
    logger.info("supervisor exiting.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
