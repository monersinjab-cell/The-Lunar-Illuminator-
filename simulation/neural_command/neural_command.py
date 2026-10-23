import json
import time
from pathlib import Path
from datetime import datetime, timezone

BASE = Path(__file__).resolve().parent
LOG = BASE / "events.jsonl"
RUNNING = True

TEAMS = {
    "المراقبة": "جاهزة",
    "التحليل": "جاهزة",
    "الإنذار": "جاهزة",
    "الاستجابة": "جاهزة",
}

def record(event, details):
    item = {
        "time_utc": datetime.now(timezone.utc).isoformat(),
        "event": event,
        "details": details,
        "mode": "LOCAL_SIMULATION",
    }
    with LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(item, ensure_ascii=False) + "\n")

def status():
    print("\nالحالة: محاكاة محلية")
    print("الإشارة العصبية الحقيقية: غير متصلة")
    print("الاتصال الخارجي: معطل")
    print("البيانات: اصطناعية للاختبار")
    for name, state in TEAMS.items():
        print(f"- فريق {name}: {state}")

def simulate_signal():
    print("\nمحاكاة إشارة اصطناعية للاختبار فقط.")
    print("هذه ليست قراءة لنشاط دماغ القائد.")
    record("synthetic_signal_test", "تم إنشاء حدث اختباري")
    print("تم تسجيل الاختبار.")

def coordinate():
    print("\nتنسيق الفرق الافتراضية:")
    for name in TEAMS:
        print(f"- {name}: استلام مهمة اختبار")
    record("team_coordination", "تنسيق افتراضي غير متصل")
    print("اكتمل التنسيق التجريبي.")

def show_events():
    if not LOG.exists():
        print("لا توجد أحداث مسجلة بعد.")
        return
    lines = LOG.read_text(encoding="utf-8").splitlines()
    print("\nآخر الأحداث:")
    for line in lines[-10:]:
        try:
            print(json.dumps(json.loads(line),
                             ensure_ascii=False, indent=2))
        except json.JSONDecodeError:
            print("سجل غير صالح؛ يحتاج إلى مراجعة.")

def main():
    global RUNNING
    record("module_started", "بدء مركز القيادة الافتراضي")
    while RUNNING:
        print("""
========================================
 قمرا منيرا بإذن ربه
 منظومة القيادة العصبية الافتراضية
========================================
1 - حالة المنظومة
2 - اختبار إشارة اصطناعية
3 - تنسيق الفرق الافتراضية
4 - سجل الأحداث
5 - إيقاف آمن وخروج
""")
        choice = input("أمرك: ").strip().translate(
            str.maketrans("٠١٢٣٤٥٦٧٨٩", "0123456789")
        )
        if choice == "1":
            status()
        elif choice == "2":
            simulate_signal()
        elif choice == "3":
            coordinate()
        elif choice == "4":
            show_events()
        elif choice == "5":
            record("safe_shutdown", "طلب المشغل الإيقاف")
            RUNNING = False
            print("تم إيقاف الوحدة التجريبية.")
        else:
            print("أدخل رقمًا من 1 إلى 5.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        record("interrupted", "إيقاف بواسطة لوحة المفاتيح")
        print("\nتم إنهاء التشغيل.")
