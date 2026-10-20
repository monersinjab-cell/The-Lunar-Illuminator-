import json
import random
from datetime import datetime, timezone
from pathlib import Path

PROJECT = "MUNIR AI SMART VEHICLE"
VEHICLE = "Kia Optima 2013"
MODE = "SIMULATION_ONLY"
STATUS = "فرضية واختبارات افتراضية غير متصلة بالسيارة"

def simulate():
    # جميع الأرقام التالية افتراضية وليست قياسات فعلية
    speed = random.randint(0, 120)
    fuel_l_100km = round(random.uniform(6.5, 12.5), 2)
    coolant_c = random.randint(80, 105)
    rf_noise = round(random.uniform(0, 100), 1)

    alerts = []

    if coolant_c >= 105:
        alerts.append(
            "تحذير افتراضي: حرارة مرتفعة؛ "
            "تحقق من السيارة فعليا عند ظهور عرض حقيقي"
        )

    if rf_noise >= 80:
        alerts.append(
            "تداخل افتراضي مرتفع؛ لا توجد عملية إرسال أو تشويش"
        )

    if speed > 100:
        alerts.append(
            "سيناريو سرعة مرتفعة؛ التزم بالحدود القانونية"
        )

    return {
        "project": PROJECT,
        "vehicle": VEHICLE,
        "mode": MODE,
        "status": STATUS,
        "timestamp_utc": datetime.now(
            timezone.utc
        ).isoformat(),
        "simulated_data": {
            "speed_kmh": speed,
            "fuel_l_per_100km": fuel_l_100km,
            "coolant_temperature_c": coolant_c,
            "rf_noise_index_0_100": rf_noise,
            "test_frequency_mhz": 1408
        },
        "alerts": alerts,
        "safety": {
            "vehicle_control": False,
            "rf_transmission": False,
            "obd_connection": False,
            "real_vehicle_measurements": False
        },
        "note": (
            "محاكاة تعليمية فقط؛ "
            "لا تستخدم لاتخاذ قرار قيادة أو صيانة."
        )
    }

if __name__ == "__main__":
    result = simulate()
    output = Path(__file__).with_name(
        "simulation_log.json"
    )
    output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

    print("=" * 48)
    print(PROJECT)
    print(VEHICLE)
    print("الحالة:", STATUS)
    print("-" * 48)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    print("-" * 48)
    print("تم حفظ سجل المحاكاة في:", output)
