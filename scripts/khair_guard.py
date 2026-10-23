#!/usr/bin/env python
"""فحص محلي بسيط لملفات مشروع القمر المنير، دون اتصال بالشبكة."""

from pathlib import Path
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parent.parent

FILES = [
    Path("quran/framework/KHAIR_MODEL_DEVELOPMENT.md"),
    Path("ai/model_records/khair_model_template.json"),
]

def main():
    print("مشروع القمر المنير بإذن ربه")
    print("نوع التشغيل: فحص محلي للملفات")
    print("لا يجري هذا البرنامج اختراقاً أو فحصاً للأجهزة الأخرى.")
    failed = False

    for relative in FILES:
        path = ROOT / relative
        if not path.is_file():
            print(f"[غير موجود] {relative}")
            failed = True
            continue

        data = path.read_bytes()
        print(f"[موجود] {relative}")
        print(f"  الحجم: {len(data)} بايت")
        print(f"  SHA-256: {hashlib.sha256(data).hexdigest()}")

        if path.suffix == ".json":
            try:
                json.loads(data.decode("utf-8"))
                print("  JSON: صالح")
            except (UnicodeDecodeError, json.JSONDecodeError) as exc:
                print(f"  JSON: غير صالح ({exc})")
                failed = True

    print("النتيجة:", "توجد مشكلات تحتاج مراجعة" if failed else "اكتمل الفحص المحلي")
    return 1 if failed else 0

if __name__ == "__main__":
    sys.exit(main())
