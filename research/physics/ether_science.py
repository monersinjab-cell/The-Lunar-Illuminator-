#!/usr/bin/env python3
import json
import math
import sys
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent
LOG = ROOT / "ether_measurements.jsonl"
C = 299792458

def status():
    print("مشروع: قمرا منيرا بإذن ربه")
    print("الوحدة: الأثير والحقول الفيزيائية")
    print("حالة الأثير المادي التاريخي: غير مثبت تجريبيا")
    print("المجالات المدروسة: الضوء، الراديو، الحقول الكهرومغناطيسية")
    print("المنهج: قياس، توثيق، تكرار، تحقق")
    print("لا تعتبر الحسابات أو الفرضيات دليلا على اكتشاف الأثير.")

def wavelength(frequency_hz):
    if not math.isfinite(frequency_hz) or frequency_hz <= 0:
        raise ValueError("يجب إدخال تردد موجب وصحيح.")
    print(f"التردد: {frequency_hz:g} Hz")
    print(f"الطول الموجي في الفراغ: {C / frequency_hz:.9g} متر")
    print("النتيجة حساب فيزيائي ولا تثبت وجود الأثير.")

def record(kind, value, unit, notes=""):
    entry = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "topic": "ether_and_measurable_physics",
        "measurement": kind,
        "value": value,
        "unit": unit,
        "notes": notes,
        "status": "قياس مسجل؛ ليس إثباتا للأثير"
    }
    with LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    print("تم تسجيل القياس في:", LOG)

if __name__ == "__main__":
    try:
        if len(sys.argv) == 2 and sys.argv[1] == "status":
            status()
        elif len(sys.argv) == 3 and sys.argv[1] == "wavelength":
            wavelength(float(sys.argv[2]))
        elif len(sys.argv) >= 5 and sys.argv[1] == "record":
            record(sys.argv[2], float(sys.argv[3]), sys.argv[4],
                   " ".join(sys.argv[5:]))
        else:
            print("الاستخدام:")
            print("python research/physics/ether_science.py status")
            print("python research/physics/ether_science.py wavelength 1408000000")
            print("python research/physics/ether_science.py record frequency 1408 MHz")
    except (ValueError, OSError) as exc:
        print("خطأ:", exc)
        sys.exit(1)
