from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

BASE = Path(__file__).resolve().parent
PROJECT = "قمرا منيرا بإذن ربه"

VERSE = (
    "تبارك الذي جعل في السماء بروجا "
    "وجعل فيها سراجا وقمرا منيرا"
)

record = {
    "project": PROJECT,
    "system": "العقل المنير",
    "mode": "بحث وتوثيق",
    "reference": {
        "surah": "الفرقان",
        "ayah": 61,
        "text": VERSE,
        "type": "نص قرآني",
    },
    "research_rules": {
        "preserve_quran_text": True,
        "separate_revelation_from_analysis": True,
        "verify_scientific_sources": True,
        "label_hypotheses": True,
        "astronomy_based_on_observation": True,
        "astrology_not_treated_as_proven_science": True,
        "no_claim_of_direct_revelation_connection": True,
        "no_control_over_human_minds": True,
    },
    "status": "سجل بحث محلي؛ لا يمثل اتصالا بالوحي",
    "created_utc": datetime.now(timezone.utc).isoformat(),
}

output = BASE / "munir_light_record.json"
output.write_text(
    json.dumps(record, ensure_ascii=False, indent=2) + "\n",
    encoding="utf-8",
)

digest = hashlib.sha256(output.read_bytes()).hexdigest()

report = BASE / "munir_light_integrity.txt"
report.write_text(
    f"Project: {PROJECT}\n"
    f"File: {output.name}\n"
    f"SHA256: {digest}\n"
    "Status: Local integrity hash created.\n"
    "Note: This hash does not prove the truth of the contents.\n",
    encoding="utf-8",
)

print("تم إنشاء سجل العقل المنير.")
print(f"السجل: {output}")
print(f"تقرير السلامة: {report}")
print(f"SHA-256: {digest}")
print("الحالة: توثيق محلي، وليس اتصالا مباشرا بالوحي.")
