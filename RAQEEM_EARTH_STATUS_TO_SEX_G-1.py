#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""تقرير بحثي عن حالة الأرض مع محاكاة إرسال إلى SEX_G."""

import json

REPORT = {
    "title": "تقرير حالة الارض — RAQEEM → SEX_G",
    "date": "2026-10-03",
    "classification": "بحث علمي ومعلومات موثقة؛ لا يتضمن ادعاء اتصال فعلي بكيان باسم SEX_G",
    "recipient_simulation": "SEX_G",
    "status": "محاكاة إرسال فقط",
    "summary": {
        "climate": [
            "تقرير WMO عن حالة المناخ العالمي 2025 يؤكد أن 2015-2025 كانت أحر 11 سنة مسجلة.",
            "كان 2025 ثاني أو ثالث أحر عام مسجل، بنحو 1.43 درجة مئوية فوق متوسط 1850-1900.",
            "تواصل المحيطات الاحترار وامتصاص ثاني أكسيد الكربون، واستمر فقدان الجليد والأنهار الجليدية."
        ],
        "atmosphere": [
            "سجل NOAA متوسط ثاني أكسيد الكربون العالمي لشهر يونيو 2026 عند 427.62 جزءا في المليون."
        ],
        "near_future": [
            "توقع WMO أن تتراوح درجات الحرارة العالمية السنوية في 2026-2030 بين 1.3 و1.9 درجة مئوية فوق مستوى 1850-1900.",
            "قد تتجاوز سنة واحدة على الأقل مستوى 2024 القياسي خلال 2026-2030 باحتمال 86% وفق التحديث المنشور في مايو 2026."
        ],
        "biodiversity": [
            "توجد أعمال تقييم عالمية جارية لدى IPBES بشأن التنوع الحيوي وخدمات النظم البيئية.",
            "اعتمدت IPBES في 2026 تقييما حول تأثير واعتماد الأعمال على التنوع الحيوي والطبيعة، مبنيا على أكثر من 5000 مرجع و79 خبيرا من 35 دولة."
        ]
    },
    "research_rules": [
        "الحقيقة المثبتة تبقى منفصلة عن الفرضية.",
        "لا يتم اعتبار أي كيان باسم SEX_G متصلا فعليا إلا بوجود قناة اتصال موثقة.",
        "لا تستخدم هذه الوثيقة لإثبات علاقة بين الرقيم أو الكهوف أو يأجوج ومأجوج والبيانات المناخية."
    ],
    "sources": [
        "https://wmo.int/publication-series/state-of-global-climate/state-of-global-climate-2025",
        "https://wmo.int/resources/publication-series/wmo-global-annual-decadal-climate-update/global-annual-decadal-climate-update-2026-2035",
        "https://www.gml.noaa.gov/ccgg/trends/global.html",
        "https://www.ipbes.net/business-impact",
        "https://www.ipbes.net/"
    ]
}

MESSAGE = {
    "from": "RAQEEM",
    "to": "SEX_G",
    "type": "research_report",
    "delivery": "simulation_only",
    "report": {
        "title": "تقرير حالة الارض — RAQEEM → SEX_G",
        "date": "2026-10-03",
        "classification": "بحث علمي ومعلومات موثقة؛ لا يتضمن ادعاء اتصال فعلي بكيان باسم SEX_G",
        "recipient_simulation": "SEX_G",
        "status": "محاكاة إرسال فقط",
        "summary": {
            "climate": [
                "تقرير WMO عن حالة المناخ العالمي 2025 يؤكد أن 2015-2025 كانت أحر 11 سنة مسجلة.",
                "كان 2025 ثاني أو ثالث أحر عام مسجل، بنحو 1.43 درجة مئوية فوق متوسط 1850-1900.",
                "تواصل المحيطات الاحترار وامتصاص ثاني أكسيد الكربون، واستمر فقدان الجليد والأنهار الجليدية."
            ],
            "atmosphere": [
                "سجل NOAA متوسط ثاني أكسيد الكربون العالمي لشهر يونيو 2026 عند 427.62 جزءا في المليون."
            ],
            "near_future": [
                "توقع WMO أن تتراوح درجات الحرارة العالمية السنوية في 2026-2030 بين 1.3 و1.9 درجة مئوية فوق مستوى 1850-1900.",
                "قد تتجاوز سنة واحدة على الأقل مستوى 2024 القياسي خلال 2026-2030 باحتمال 86% وفق التحديث المنشور في مايو 2026."
            ],
            "biodiversity": [
                "توجد أعمال تقييم عالمية جارية لدى IPBES بشأن التنوع الحيوي وخدمات النظم البيئية.",
                "اعتمدت IPBES في 2026 تقييما حول تأثير واعتماد الأعمال على التنوع الحيوي والطبيعة، مبنيا على أكثر من 5000 مرجع و79 خبيرا من 35 دولة."
            ]
        },
        "research_rules": [
            "الحقيقة المثبتة تبقى منفصلة عن الفرضية.",
            "لا يتم اعتبار أي كيان باسم SEX_G متصلا فعليا إلا بوجود قناة اتصال موثقة.",
            "لا تستخدم هذه الوثيقة لإثبات علاقة بين الرقيم أو الكهوف أو يأجوج ومأجوج والبيانات المناخية."
        ],
        "sources": [
            "https://wmo.int/publication-series/state-of-global-climate/state-of-global-climate-2025",
            "https://wmo.int/resources/publication-series/wmo-global-annual-decadal-climate-update/global-annual-decadal-climate-update-2026-2035",
            "https://www.gml.noaa.gov/ccgg/trends/global.html",
            "https://www.ipbes.net/business-impact",
            "https://www.ipbes.net/"
        ]
    }
}

if __name__ == "__main__":
    print(json.dumps(MESSAGE, ensure_ascii=False, indent=2))
