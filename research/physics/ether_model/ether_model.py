import json
import math
from pathlib import Path
from datetime import datetime, timezone

BASE = Path(__file__).resolve().parent
REPORT = BASE / "simulation_report.json"


def simulate_wave():
    samples = []
    for i in range(21):
        x = i / 20
        samples.append({
            "x": round(x, 3),
            "amplitude": round(math.sin(2 * math.pi * x), 6)
        })
    return samples


def main():
    report = {
        "project": "The Lunar Illuminator - Munir",
        "module": "ether_model",
        "status": "فرضية غير مثبتة",
        "mode": "محاكاة تعليمية لموجة رياضية",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "quran_text_modified": False,
        "added_tafsir": False,
        "direct_mind_connection_claimed": False,
        "wave_samples": simulate_wave(),
        "conclusion": "المحاكاة الرياضية لا تثبت وجود الأثير المادي."
    }

    REPORT.write_text(
        json.dumps(report, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )
    print("نجاح: تم إنشاء تقرير المحاكاة.")
    print("الحالة: فرضية غير مثبتة.")
    print(f"التقرير: {REPORT}")


if __name__ == "__main__":
    main()
