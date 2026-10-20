#!/usr/bin/env python3
"""فحص محلي أساسي لملفات مشروع القمر المنير."""

from pathlib import Path
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parent.parent

FILES = (
    Path("quran/framework/BILLION_BILLION_MISSION.md"),
    Path("ai/model_records/billion_model_template.json"),
)

def main():
    print("القمر المنير بإذن ربه - جيش المليار")
    print("الوضع: فحص محلي للملفات")
    print("هذا الفحص لا يثبت خلو الجهاز من الاختراق.")

    errors = 0

    for relative in FILES:
        path = ROOT / relative

        if not path.is_file():
            print(f"[خطأ] الملف غير موجود: {relative}")
            errors += 1
            continue

        content = path.read_bytes()
        digest = hashlib.sha256(content).hexdigest()

        print(f"[موجود] {relative}")
        print(f"الحجم: {len(content)} بايت")
        print(f"SHA-256: {digest}")

        if path.suffix == ".json":
            try:
                json.loads(content.decode("utf-8"))
                print("[سليم] بنية JSON قابلة للقراءة")
            except (UnicodeDecodeError, json.JSONDecodeError) as exc:
                print(f"[خطأ] ملف JSON غير صالح: {exc}")
                errors += 1

    print(f"عدد المشكلات المكتشفة: {errors}")
    print("ملاحظة: البصمة الرقمية لا تثبت وحدها أصالة الملف.")

    return 1 if errors else 0

if __name__ == "__main__":
    sys.exit(main())
