import json
from pathlib import Path
from quran_guard import protected_ask

ROOT = Path(__file__).resolve().parent.parent
PROTOCOL = ROOT / "milyar/quran_development_protocol.json"

def ask_research(question):
    data = json.loads(PROTOCOL.read_text(encoding="utf-8"))
    rules = data["rules"]
    instruction = (
        "أنت مساعد بحث ضمن مشروع قمرا منيرا بإذن ربه. "
        "النص القرآني مرجع مستقل لا تعدله ولا تنشئ آيات. "
        "لا تنسب أي جواب منك إلى القرآن أو الوحي، ولا تقدم تفسيرًا على أنه حقيقة إلهية. "
        "ميّز بين المعلومة الموثقة والفرضية والاستنتاج، واطلب مصدرًا عند الحاجة. "
        "إن لم تكن متأكدًا فصرّح بذلك. "
        "أجب بالعربية بإيجاز عن السؤال البحثي التالي:\n"
        + str(question)
    )
    return {
        "label": "مخرجات نموذج ذكاء اصطناعي — تحتاج إلى مراجعة",
        "quran_text_modified": False,
        "answer": protected_ask(instruction, 96)["answer"]
    }

if __name__ == "__main__":
    try:
        result = ask_research("كيف نميز المعلومة الموثقة عن الفرضية في مشروع بحثي؟")
        print(result["label"])
        print(result["answer"])
        print("سلامة النص القرآني: لم يُطلب من النموذج إعادة كتابته.")
    except Exception as e:
        print("تعذر إكمال الاختبار:", e)
