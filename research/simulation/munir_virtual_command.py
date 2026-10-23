import json
from datetime import datetime, timezone
from pathlib import Path

BASE = Path(__file__).resolve().parent
LOG = BASE / "virtual_command_log.json"

SYSTEMS = {
    "1": "منظومة الدفاع الافتراضية",
    "2": "منظومة الطيران الافتراضية",
    "3": "منظومة الرصد الفضائي",
    "4": "منظومة الاتصالات الافتراضية",
    "5": "منظومة التدريب العسكري الخيالي",
    "6": "مركز القيادة الافتراضي",
}

def load_log():
    if LOG.exists():
        try:
            data = json.loads(LOG.read_text(encoding="utf-8"))
            if isinstance(data, list):
                return data
        except (ValueError, OSError):
            pass
    return []

events = load_log()
states = {key: False for key in SYSTEMS}

def record(action, system, result):
    events.append({
        "time": datetime.now(timezone.utc).isoformat(),
        "action": action,
        "system": system,
        "result": result,
        "mode": "FICTIONAL_SIMULATION_ONLY"
    })
    LOG.write_text(
        json.dumps(events, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

def menu():
    print("\n" + "=" * 42)
    print(" منير | مركز القيادة الافتراضي")
    print(" محاكاة خيالية للتدريب فقط")
    print("=" * 42)
    for key, name in SYSTEMS.items():
        status = "نشطة افتراضياً" if states[key] else "متوقفة افتراضياً"
        print(f"{key}. {name} — {status}")
    print("7. عرض سجل الأحداث")
    print("8. إيقاف جميع الوحدات الافتراضية")
    print("0. خروج")
    print("تنبيه: لا يوجد اتصال بأي سلاح أو جهاز حقيقي.")

while True:
    menu()
    choice = input("\nاختر رقماً: ").strip()

    if choice == "0":
        print("انتهت المحاكاة.")
        break

    elif choice in SYSTEMS:
        name = SYSTEMS[choice]
        states[choice] = not states[choice]
        status = "تشغيل افتراضي" if states[choice] else "إيقاف افتراضي"
        record(status, name, "محاكاة محلية فقط")
        print(f"{name}: {status}")

    elif choice == "7":
        print(json.dumps(events[-20:], ensure_ascii=False, indent=2))

    elif choice == "8":
        for key, name in SYSTEMS.items():
            states[key] = False
            record("إيقاف افتراضي شامل", name, "محاكاة محلية فقط")
        print("تم إيقاف جميع الوحدات الافتراضية.")

    else:
        print("اختيار غير صحيح. حاول مرة أخرى.")
