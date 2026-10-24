import json
from pathlib import Path
from datetime import datetime, timezone

root = Path.cwd()
out = root / "milyar" / "quran_work"
out.mkdir(parents=True, exist_ok=True)

candidates = [
    root / "quran" / "quran.txt",
    root / "quran.txt",
    root / "quran" / "quran-uthmani.txt",
]
source = next((p for p in candidates if p.is_file() and p.stat().st_size > 0), None)

surahs = []
for n in range(1, 115):
    surahs.append({
        "surah_number": n,
        "scope": "جميع آيات السورة",
        "status": (
            "source_found_needs_integrity_verification"
            if source else "blocked_missing_verified_quran_text"
        ),
        "verse_tasks_created": False,
        "note": (
            "يجب التحقق من النص وعدد الآيات قبل إنشاء مهام لكل آية."
            if source else
            "لم يُعثر على ملف نص قرآني معتمد؛ لم تُنشأ آيات من عندنا."
        )
    })

manifest = {
    "project": "قمرا منيرا بإذن ربه",
    "module": "AL MILYAR",
    "mode": "تنظيم بحث مدني آلي",
    "created_utc": datetime.now(timezone.utc).isoformat(),
    "surah_count": 114,
    "verified_quran_source": str(source.relative_to(root)) if source else None,
    "source_integrity_verified": False,
    "completed_surahs": 0,
    "surahs": surahs,
    "rules": [
        "عدم اختلاق نص قرآني أو آيات",
        "عدم تعديل النص القرآني الأصلي",
        "فصل النص عن البحث والتأمل والاستنتاج",
        "عدم ادعاء نتائج لم تُختبر",
        "العمل المدني السلمي واحترام الخصوصية"
    ]
}

(out / "manifest.json").write_text(
    json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
    encoding="utf-8"
)

(out / "START_HERE.md").write_text(
    "# تشغيل منظومة المليار\n\n"
    "تم إنشاء قائمة عمل للسور الـ114.\n\n"
    "- لا يُعتبر أي نص قرآني موثّقًا قبل فحص مصدره وسلامته.\n"
    "- لا تُنشأ سجلات آيات مفترضة.\n"
    "- هذه الأداة تنظّم العمل ولا تعمل في الخلفية بعد إغلاق Termux.\n"
    "- لم يتم رفع الملفات إلى GitHub.\n",
    encoding="utf-8"
)

print("=" * 48)
print("تم تشغيل تهيئة منظومة المليار")
print("السور المدرجة في قائمة العمل:", len(surahs))
print("ملف قائمة العمل:", out / "manifest.json")
if source:
    print("عُثر على ملف نصي:", source.relative_to(root))
    print("الحالة: يلزم التحقق من المصدر وسلامة النص.")
else:
    print("الحالة: متوقف بأمان؛ لم يُعثر على ملف القرآن في المسارات المعروفة.")
    print("لم يتم اختلاق آيات أو الادعاء بإنجاز دراسة الآيات.")
print("تم إنشاء الملفات دون حذف ملفات سابقة أو رفعها.")
print("=" * 48)
