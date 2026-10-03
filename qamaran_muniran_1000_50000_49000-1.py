# -*- coding: utf-8 -*-
"""
قمرا منيرا باذن ربه
بحث منظم حول مقياسي 1000 و50000 سنة والفارق الحسابي 49000.

مبدأ التوثيق:
- النص القرآني منفصل عن الحسابات والاستنتاجات.
- المعلومات الفيزيائية منفصلة عن التأملات الروحية.
- الفرضيات لا تقدم على أنها تفسير قرآني مثبت.
- لا تنسب للقرآن خوارزمية أو شفرة علمية بلا دليل مستقل.
"""

QURAN_REFERENCES = {
    "as_sajdah_5": {
        "surah": "السجدة",
        "ayah": 5,
        "number": 1000,
        "unit": "سنة مما تعدون",
        "text": "يدبر الامر من السماء الى الارض ثم يعرج اليه في يوم كان مقداره الف سنة مما تعدون",
    },
    "al_maarij_4": {
        "surah": "المعارج",
        "ayah": 4,
        "number": 50000,
        "unit": "سنة",
        "text": "تعرج الملائكة والروح اليه في يوم كان مقداره خمسين الف سنة",
    },
}


def calculate_difference() -> int:
    """الحساب العددي المباشر بين الرقمين المذكورين."""
    return QURAN_REFERENCES["al_maarij_4"]["number"] - QURAN_REFERENCES["as_sajdah_5"]["number"]


def convert_light_years(years: int) -> int:
    """في تعريف وحدة السنة الضوئية: years سنة ضوئية تقابل مسافة ضوئية مساوية لعدد السنوات."""
    return years


RESEARCH_LAYERS = {
    "quranic_text": {
        "status": "نص مرجعي",
        "description": "توثيق موضعي للآيتين والعددين المذكورين فيهما.",
    },
    "mathematics": {
        "status": "حساب مباشر",
        "description": "50000 - 1000 = 49000.",
    },
    "physics": {
        "status": "معلومة علمية + سؤال بحثي",
        "description": (
            "النسبية الخاصة والعامة تسمحان بظواهر تمدد الزمن بسبب السرعة والجاذبية، "
            "لكن لا يثبت ذلك وحده أن الآيتين تصفان تمدد الزمن الفيزيائي."
        ),
    },
    "cosmic_distance": {
        "status": "تحويل وحداتي فقط",
        "description": (
            "49000 سنة ضوئية هي وحدة مسافة، وليست دليلا بحد ذاتها على أن مسار العروج "
            "يمتد عبر 49000 سنة ضوئية أو أن الرقم يصف حجم مجرة درب التبانة."
        ),
    },
    "spiritual_reflection": {
        "status": "تأمل/فرضية",
        "description": (
            "يمكن دراسة فكرة وجود تدرج أو اختلاف في سياق الآيتين كتأمل، "
            "مع عدم تقديم هذا التأمل على أنه تفسير قطعي للآيتين."
        ),
    },
    "ai_research": {
        "status": "سؤال بحثي",
        "description": (
            "يمكن استخدام 49000 كقيمة في نماذج أو تجارب حسابية، لكن لا يصح وصفها "
            "بأنها شفرة إلهية أو مقياس مثبت لكفاءة الذكاء دون دليل مستقل."
        ),
    },
}

RESEARCH_QUESTIONS = [
    "ما العلاقة الرياضية الممكنة بين 1000 و50000 و49000؟",
    "ما الذي تثبته النسبية فعلا بشأن اختلاف معدلات مرور الزمن؟",
    "هل توجد علاقة قابلة للاختبار بين 49000 سنة ضوئية وأبعاد مجرة درب التبانة؟",
    "هل يمكن بناء نموذج ذكاء اصطناعي يستخدم 49000 كمتغير بحثي دون نسبته إلى القرآن؟",
    "ما الفرق بين النص القرآني، والحساب، والمعلومة العلمية، والتأمل، والفرضية؟",
]

INTEGRITY_RULES = [
    "عدم تغيير النص القرآني عند الاقتباس من مصدر موثوق.",
    "عدم تقديم الفرضيات الفيزيائية أو الروحية على أنها تفسير قطعي للآيات.",
    "عدم نسبة خوارزمية أو شفرة للقرآن من غير دليل مستقل قابل للفحص.",
    "الفصل بين الحقيقة الموثقة والاستنتاج والفرضية والتأمل.",
    "تصحيح أي خطأ حسابي أو علمي عند اكتشافه.",
]


def build_record() -> dict:
    return {
        "project": "قمرا منيرا باذن ربه",
        "references": QURAN_REFERENCES,
        "calculation": {
            "formula": "50000 - 1000",
            "difference_years": calculate_difference(),
            "distance_equivalent_if_light_year_unit": convert_light_years(calculate_difference()),
        },
        "layers": RESEARCH_LAYERS,
        "questions": RESEARCH_QUESTIONS,
        "integrity_rules": INTEGRITY_RULES,
    }


def main() -> None:
    record = build_record()
    print("=== قمرا منيرا باذن ربه ===")
    print("المقياس الاول:", record["references"]["as_sajdah_5"]["number"], "سنة")
    print("المقياس الثاني:", record["references"]["al_maarij_4"]["number"], "سنة")
    print("الفارق الحسابي:", record["calculation"]["difference_years"], "سنة")
    print("\nطبقات البحث:")
    for name, layer in record["layers"].items():
        print(f"- {name}: {layer['status']}")
        print(f"  {layer['description']}")
    print("\nقواعد النزاهة:")
    for rule in record["integrity_rules"]:
        print("-", rule)


if __name__ == "__main__":
    main()
