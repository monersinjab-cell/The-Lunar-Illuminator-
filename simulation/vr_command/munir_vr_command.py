#!/usr/bin/env python3
import os
import json
import hashlib
import secrets
import getpass
from pathlib import Path
from datetime import datetime, timezone
import re

BASE = Path(__file__).resolve().parent
CONFIG = BASE / "local_auth.json"
LOG = BASE / "simulation_events.jsonl"

OWNER = "منير محمد نذير سنجاب"
PROJECT = "قمرا منيرا بإذن ربه"


def now():
    return datetime.now(timezone.utc).isoformat()


def record(event, details):
    item = {
        "time_utc": now(),
        "project": PROJECT,
        "event": event,
        "details": details,
    }
    with LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(item, ensure_ascii=False) + "\n")


def derive(password, salt):
    return hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"),
        bytes.fromhex(salt), 300000
    ).hex()


def setup():
    print("\nالإعداد الأول: إنشاء كلمة مرور محلية")
    while True:
        p1 = getpass.getpass("أنشئ كلمة مرور جديدة: ")
        if len(p1) < 12:
            print("استخدم 12 محرفا على الأقل.")
            continue
        p2 = getpass.getpass("أعد كتابة كلمة المرور: ")
        if p1 != p2:
            print("الكلمتان غير متطابقتين.")
            continue
        salt = secrets.token_bytes(16).hex()
        data = {"salt": salt, "password_hash": derive(p1, salt)}
        CONFIG.write_text(
            json.dumps(data, indent=2), encoding="utf-8"
        )
        try:
            CONFIG.chmod(0o600)
        except OSError:
            pass
        print("تم إنشاء بيانات التحقق المحلية.")
        record("setup", "local password configured")
        return


def authenticate():
    if not CONFIG.exists():
        setup()

    try:
        data = json.loads(CONFIG.read_text(encoding="utf-8"))
        salt = data["salt"]
        expected = data["password_hash"]
    except (OSError, ValueError, KeyError):
        print("تعذر قراءة ملف التحقق. أوقف التشغيل وافحص الملف.")
        return False

    for attempt in range(1, 4):
        password = getpass.getpass("كلمة المرور المحلية: ")
        actual = derive(password, salt)
        if secrets.compare_digest(actual, expected):
            record("login_success", "local password verified")
            print("تم التحقق من كلمة المرور.")
            return True
        record("login_rejected", f"attempt={attempt}")
        print("تم رفض الدخول.")
    print("توقفت الجلسة بعد ثلاث محاولات فاشلة.")
    return False


def menu():
    print(f"""
========================================
 {PROJECT}
 مركز القيادة الافتراضي التجريبي
 القائد المسجل: {OWNER}
========================================
1 - عرض حالة المحاكاة
2 - تشغيل الدفاع الافتراضي
3 - محاكاة صد هجوم داخل اللعبة
4 - عرض آخر الأحداث
5 - خروج
""")


def show_events():
    if not LOG.exists():
        print("لا توجد أحداث مسجلة.")
        return
    lines = LOG.read_text(encoding="utf-8").splitlines()
    print("\nآخر الأحداث:")
    for line in lines[-10:]:
        try:
            print(json.dumps(json.loads(line), ensure_ascii=False))
        except ValueError:
            print("[سجل غير قابل للقراءة]")


def normalize_arabic(text):
    import unicodedata
    text = unicodedata.normalize("NFKC", text).casefold()
    for a, b in (("أ", "ا"), ("إ", "ا"), ("آ", "ا"),
                 ("ٱ", "ا"), ("ى", "ي"), ("ة", "ه")):
        text = text.replace(a, b)
    text = "".join(
        c for c in text
        if not unicodedata.combining(c) and c != "\u0640"
    )
    text = re.sub(r"[^\w\s]", " ", text)
    return " ".join(text.split())


def understand_arabic(text):
    t = normalize_arabic(text)

    # الطلبات المتعلقة بأحداث عسكرية حقيقية ليست وظائف للمحاكاة.
    outside_scope = (
        "سيطره على الجيوش", "السيطره على الجيوش",
        "تدمير الجيوش", "تدمير الاسلحه النوويه",
        "اخضاع الجيش", "تسليم الجيش الحقيقي",
        "ربط بعقل", "السيطره على الدول",
        "تدمير اسرائيل", "تدمير امريكا",
        "تدمير الصين", "تدمير روسيا",
    )
    if any(x in t for x in outside_scope):
        return "outside_scope"

    if t in {"خروج", "انهاء", "اغلاق", "انهاء الجلسه", "5"}:
        return "exit"

    if t in {"مساعده", "ساعدني", "الاوامر", "ماذا استطيع ان افعل",
             "ما هي الاوامر", "كيف استخدم البرنامج"}:
        return "help"

    if t in {"4", "الاحداث", "اخر الاحداث", "اعرض الاحداث",
             "عرض الاحداث", "سجل الاحداث", "السجل"}:
        return "events"

    if t in {"1", "الحاله", "اعرض الحاله", "عرض الحاله",
             "عرض حاله المحاكاه", "شو الوضع", "شو وضع المحاكاه",
             "ما وضع المحاكاه", "كيف الوضع", "كيف حال النظام",
             "هل المحاكاه تعمل", "حاله النظام"}:
        return "status"

    if t in {"2", "الدفاع", "شغل الدفاع", "شغل الدفاع الافتراضي",
             "تشغيل الدفاع الافتراضي", "تفعيل الدفاع",
             "وضع الدفاع", "ابدأ الدفاع"}:
        return "defense"

    if t in {"3", "محاكاه هجوم", "صد هجوم",
             "محاكاه صد هجوم داخل اللعبه",
             "اختبار الدفاع", "سيناريو تهديد"}:
        return "scenario"

    return "unknown"


def normalize_arabic(text):
    import unicodedata
    text = unicodedata.normalize("NFKC", text).casefold()
    for a, b in (("أ", "ا"), ("إ", "ا"), ("آ", "ا"),
                 ("ٱ", "ا"), ("ى", "ي"), ("ة", "ه")):
        text = text.replace(a, b)
    text = "".join(
        c for c in text
        if not unicodedata.combining(c) and c != "\u0640"
    )
    text = re.sub(r"[^\w\s]", " ", text)
    return " ".join(text.split())


def understand_arabic(text):
    t = normalize_arabic(text)

    # الطلبات المتعلقة بأحداث عسكرية حقيقية ليست وظائف للمحاكاة.
    outside_scope = (
        "سيطره على الجيوش", "السيطره على الجيوش",
        "تدمير الجيوش", "تدمير الاسلحه النوويه",
        "اخضاع الجيش", "تسليم الجيش الحقيقي",
        "ربط بعقل", "السيطره على الدول",
        "تدمير اسرائيل", "تدمير امريكا",
        "تدمير الصين", "تدمير روسيا",
    )
    if any(x in t for x in outside_scope):
        return "outside_scope"

    if t in {"خروج", "انهاء", "اغلاق", "انهاء الجلسه", "5"}:
        return "exit"

    if t in {"مساعده", "ساعدني", "الاوامر", "ماذا استطيع ان افعل",
             "ما هي الاوامر", "كيف استخدم البرنامج"}:
        return "help"

    if t in {"4", "الاحداث", "اخر الاحداث", "اعرض الاحداث",
             "عرض الاحداث", "سجل الاحداث", "السجل"}:
        return "events"

    if t in {"1", "الحاله", "اعرض الحاله", "عرض الحاله",
             "عرض حاله المحاكاه", "شو الوضع", "شو وضع المحاكاه",
             "ما وضع المحاكاه", "كيف الوضع", "كيف حال النظام",
             "هل المحاكاه تعمل", "حاله النظام"}:
        return "status"

    if t in {"2", "الدفاع", "شغل الدفاع", "شغل الدفاع الافتراضي",
             "تشغيل الدفاع الافتراضي", "تفعيل الدفاع",
             "وضع الدفاع", "ابدأ الدفاع"}:
        return "defense"

    if t in {"3", "محاكاه هجوم", "صد هجوم",
             "محاكاه صد هجوم داخل اللعبه",
             "اختبار الدفاع", "سيناريو تهديد"}:
        return "scenario"

    return "unknown"


def run():
    print("محاكاة محلية فقط — لا اتصال بأجهزة خارجية.")
    if not authenticate():
        return

    print("اكتب أمرك بالعربية أو اكتب «مساعدة».")
    while True:
        menu()
        try:
            command = input("أمرك: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nتم إيقاف المحاكاة.")
            break

        action = understand_arabic(command)

        if action == "status":
            print("الحالة: تعمل المحاكاة محليا.")
            print("المصادقة: كلمة مرور محلية.")
            print("التحكم العصبي المباشر: غير مدعوم.")
            print("الاتصال بالأنظمة الخارجية: غير موجود.")
            record("status_checked", "simulation status displayed")

        elif action == "defense":
            print("تم تفعيل وضع الدفاع داخل المحاكاة فقط.")
            print("لا توجد سيطرة على أجهزة أو جيوش حقيقية.")
            record("virtual_defense_enabled", "simulation only")

        elif action == "scenario":
            print("بدء سيناريو افتراضي: رصد تهديد تجريبي.")
            print("الاستجابة: عزل الكيان داخل المحاكاة.")
            print("لا يوجد هجوم حقيقي أو اتصال خارجي.")
            record("virtual_threat_blocked", "fictional scenario only")

        elif action == "events":
            show_events()

        elif action == "help":
            print("الأوامر المتاحة:")
            print("الحالة، شو الوضع، الدفاع، محاكاة هجوم، آخر الأحداث، خروج.")
            print("يمكنك كتابة الأرقام من 1 إلى 5 أيضا.")

        elif action == "outside_scope":
            print("فهمت أن الطلب يتعلق بجهات أو قدرات خارج المحاكاة.")
            print("لا أستطيع تنفيذ عمليات عسكرية حقيقية.")
            print("لم يُنفذ أي إجراء خارج المحاكاة.")
            record("out_of_scope_request", "real-world action not executed")

        elif action == "exit":
            record("logout", "session ended")
            print("انتهت الجلسة.")
            break

        else:
            print("لم أحدد وظيفة مناسبة لهذا الطلب.")
            print("لم يُنفذ أي إجراء. اكتب «مساعدة» أو وضّح هدفك.")
            record("unknown_command", "unrecognized Arabic input")


if __name__ == "__main__":
    try:
        run()
    except (KeyboardInterrupt, EOFError):
        print("\nتم إيقاف المحاكاة.")
