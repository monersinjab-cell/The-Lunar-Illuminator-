from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

BASE = Path(__file__).resolve().parent
TEST_DIR = BASE / "safe_test"
TEST_FILE = TEST_DIR / "sample.txt"
LOG = BASE / "good_learning_log.jsonl"
PROJECT = "قمرا منيرا بإذن ربه"


def record(event, details=None):
    item = {
        "time_utc": datetime.now(timezone.utc).isoformat(),
        "project": PROJECT,
        "event": event,
        "details": details or {},
    }
    with LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(item, ensure_ascii=False) + "\n")


def main():
    TEST_DIR.mkdir(parents=True, exist_ok=True)

    if not TEST_FILE.exists():
        TEST_FILE.write_text(
            "ملف اختبار آمن\n", encoding="utf-8"
        )

    original = TEST_FILE.read_bytes()
    simulated = original + b"SAFE TEST"
    changed = hashlib.sha256(original).digest() != \
        hashlib.sha256(simulated).digest()

    print("المشروع:", PROJECT)
    print("الاختبار المحلي:", "نجح" if changed else "لم يكتمل")
    print("لم يتم تعديل الملف الأصلي أو فحص أجهزة أخرى.")

    record("safe_test", {
        "difference_detected": changed,
        "original_file_modified": False,
    })

    answer = input(
        "هل توافق على الدرس التعليمي؟ اكتب نعم أو لا: "
    ).strip()

    if answer != "نعم":
        record("lesson_not_approved")
        print("لم يُعرض الدرس.")
        return

    record("lesson_consent_given")
    print("\nدرس الأمانة الرقمية:")
    print("• اختلاف البصمة يكشف اختلاف المحتوى، لا هوية من غيّره.")
    print("• لا تتهم أحداً دون دليل.")
    print("• احمِ الملفات وراجع الصلاحيات وأصلح الأخطاء بأمان.")
    print("• النص القرآني يُراجع من مصدر موثوق ولا يُعدّل.")
    print("• مخرجات البرنامج ليست نصاً قرآنياً.")

    quiz = input(
        "\nهل اختلاف البصمة وحده يثبت سوء النية؟ اكتب نعم أو لا: "
    ).strip()
    correct = quiz == "لا"
    print("إجابة صحيحة." if correct else
          "الإجابة الصحيحة: لا، نحتاج إلى أدلة إضافية.")

    record("learning_quiz", {"answer": quiz, "correct": correct})
    print("سجل الأحداث:", LOG)


if __name__ == "__main__":
    main()
