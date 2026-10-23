from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parent
REQUESTS = ROOT / "support_requests.jsonl"
PROJECT = "قمرا منيرا بإذن ربه"
NETWORK = "شبكة المؤازرة والخير"

def utc_now():
    return datetime.now(timezone.utc).isoformat()

def log_request(category, description):
    record = {
        "time_utc": utc_now(),
        "project": PROJECT,
        "network": NETWORK,
        "category": category,
        "description": description,
        "status": "بانتظار مراجعة بشرية",
        "authorization": "لم يتم التحقق من أي جهة",
        "external_connection": False
    }

    with REQUESTS.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")

    digest = hashlib.sha256(
        json.dumps(record, ensure_ascii=False, sort_keys=True)
        .encode("utf-8")
    ).hexdigest()

    print("تم تسجيل الطلب محليا.")
    print("الحالة: بانتظار المراجعة البشرية.")
    print("بصمة السجل SHA-256:", digest)
    print("لم يتم إرسال أي أمر أو اتصال خارجي.")

def main():
    print("شبكة المؤازرة والخير")
    print("1 - إسعاف ومساعدة مدنية")
    print("2 - إغاثة وإدارة موارد")
    print("3 - توثيق معلومات والتحقق منها")
    print("4 - أمن سيبراني دفاعي مصرح به")

    choice = input("اختر نوع الطلب: ").strip()
    categories = {
        "1": "إسعاف ومساعدة مدنية",
        "2": "إغاثة وإدارة موارد",
        "3": "توثيق معلومات",
        "4": "أمن سيبراني دفاعي"
    }

    if choice not in categories:
        print("اختيار غير صالح.")
        return

    description = input("اكتب وصفا مختصرا للطلب: ").strip()
    if not description:
        print("لم يسجل طلب فارغ.")
        return

    log_request(categories[choice], description)

if __name__ == "__main__":
    main()
