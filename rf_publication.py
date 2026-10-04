#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The Lunar Illuminator — RF Publication Simulation
==================================================

هذا الملف يجهز بيانات مشروع "قمرا منيرا بإذن ربه"
للعرض والنشر البرمجي والمحاكاة.

مهم:
- هذا البرنامج لا يرسل موجات RF حقيقية.
- 1408 MHz قيمة محاكاة/إعداد فقط.
- البث RF الحقيقي يحتاج إلى أجهزة راديوية مناسبة
  وتصريح/ترخيص والتزام بالأنظمة المحلية.
- النص العربي محفوظ كبيانات أدخلها المستخدم.
- لا يضيف البرنامج تفسيرا للنص القرآني.
- أي ترجمة يجب أن تبقى موسومة بأنها ترجمة وليست نصا قرآنيا.
"""

from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
import json


PROJECT = "The Lunar Illuminator"
ARABIC_TITLE = "قمرا منيرا بإذن ربه"

# قيمة محاكاة فقط
SIMULATED_FREQUENCY_MHZ = 1408.0


QURANIC_TEXT = r"""
الذين امنوا يقاتلون في سبيل الله والذين كفروا يقاتلون في سبيل الطاغوت فقاتلوا اولياء الشيطان ان كيد الشيطان كان ضعيفا

ياايها الذين امنوا مالكم اذا قيل لكم انفروا في سبيل الله اثاقلتم الى ارضيتم بالحياة الدنيا فما متاع الحياة الدنيا في الاخرة الا قليل

فقاتل في سبيل الله لا تكلف الا نفسك وحرض المؤمنين عسى الله ان يكف بأس الذين كفروا والله اشد بأسا واشد تنكيلا

اذ يوحي ربك الى الملائكة اني معكم فثبتوا الذين امنوا سالقي في قلوب الذين كفروا الرعب

ان بطش ربك لشديد

يوم نبطش البطشة الكبرى انا منتقمون

كدأب ال فرعون والذين من قبلهم كذبوا باياتنا فاخذهم الله بذنوبهم والله شديد العقاب

قل للذين كفروا ستغلبون وتحشرون الى جهنم وبئس المهاد

تبارك الذي جعل في السماء بروجا وجعل فيها سراجا وقمرا منيرا

وداعيا الى الله باذنه وسراجا منيرا

ربي زدني علما

وكفى بربك هاديا ونصيرا

وان يريدوا ان يخدعوك فان حسبك الله هو الذي ايدك بنصره وبالمؤمنين

وعلى الله قصد السبيل ومنها جائر ويخلق ما لا تعلمون
""".strip()


MESSAGE = r"""
لا للتفسير نعم للقران العظيم
نعم لامر رب العالمين
سمعنا واطعنا غفرانك ربنا واليك المصير
""".strip()


@dataclass
class RFSimulation:
    project: str
    title_ar: str
    mode: str
    status: str
    frequency_mhz: float
    frequency_type: str
    transmission: bool
    quran_text_policy: str
    translation_ready: bool
    multilingual: bool
    timestamp_utc: str
    note: str


def build_record() -> RFSimulation:
    """إنشاء سجل حالة المحاكاة."""

    return RFSimulation(
        project=PROJECT,
        title_ar=ARABIC_TITLE,
        mode="SIMULATION / CONFIGURATION",
        status="READY FOR DISPLAY",
        frequency_mhz=SIMULATED_FREQUENCY_MHZ,
        frequency_type="SIMULATED — NOT A REAL RF TRANSMISSION",
        transmission=False,
        quran_text_policy=(
            "User-supplied Quranic text is preserved as data; "
            "no added tafsir and no claim that model output is Quran."
        ),
        translation_ready=True,
        multilingual=True,
        timestamp_utc=datetime.now(timezone.utc).isoformat(),
        note=(
            "This record can be published on GitHub Pages or another "
            "web host as an RF-status simulation. "
            "It does not create RF energy."
        ),
    )


def save_json(path: str = "rf_publication.json") -> None:
    """
    إنشاء ملف JSON مرافق للمحاكاة.
    """

    record = build_record()

    payload = {
        "rf_status": asdict(record),

        "content": {
            "arabic": QURANIC_TEXT,
            "message": MESSAGE,
        },

        "language_support": [
            "ar",
            "en",
            "fr",
            "es",
            "de",
            "tr",
            "ur",
            "fa",
            "id",
            "ms",
            "hi",
            "bn",
            "zh",
            "ja",
            "ko",
            "ru",
            "pt",
            "it",
        ],

        "translation_policy": {
            "source_language": "ar",
            "translate_without_modifying_source": True,
            "mark_translations_as_translations": True,
            "do_not_present_translation_as_quran": True,
        },

        "safety": {
            "real_rf_transmission": False,
            "requires_authorized_hardware_for_real_rf": True,
            "requires_compliance_with_local_rules": True,
        },
    }

    Path(path).write_text(
        json.dumps(
            payload,
            ensure_ascii=False,
            indent=2
        ),
        encoding="utf-8"
    )


def print_status() -> None:
    """عرض حالة المشروع بشكل واضح."""

    record = build_record()

    print()
    print("🌕 THE LUNAR ILLUMINATOR")
    print("=" * 45)
    print(f"العنوان: {record.title_ar}")
    print(f"الحالة: {record.status}")
    print(f"التردد المحاكى: {record.frequency_mhz:g} MHz")
    print(f"النمط: {record.mode}")
    print(
        "بث RF حقيقي: "
        + ("نعم" if record.transmission else "لا")
    )
    print()
    print("النص العربي محفوظ كبيانات مستخدم.")
    print("لا يوجد تفسير مضاف من البرنامج.")
    print("المنظومة قابلة للترجمة إلى لغات متعددة.")
    print("الترجمة تبقى منفصلة عن النص العربي الأصلي.")
    print()


def main() -> None:
    """نقطة تشغيل البرنامج."""

    print_status()
    save_json()

    print("تم إنشاء الملف:")
    print("rf_publication.json")
    print()
    print("الحالة: SIMULATION READY")
    print("1408 MHz: SIMULATION ONLY")
    print()


if __name__ == "__main__":
    main()
