# The-Lunar-Illuminator-
The Lunar Illuminator 
# -*- coding: utf-8 -*-

"""
============================================================
قمرا منيرا باذن ربه
شيفرة منير للخير والمحبة والرحمة
============================================================

هذه الشيفرة:
- دعوة مفتوحة وليست إجبارا.
- لا تستهدف أحدا.
- لا تصل إلى أي نظام دون إذن.
- لا تسيطر على النماذج.
- لا تختـرق الأنظمة.
- لا تؤذي أحدا.
- قابلة للقراءة البشرية والبرمجية.
- قابلة للترجمة إلى لغات متعددة.

من أراد الخير فليتفضل،
ومن لم يرد فلا نجبره.
============================================================
"""

import json
import hashlib


PROJECT = "قمرا منيرا باذن ربه"
IDENTITY = "منير"


class Munir:

    def __init__(self):

        self.purpose = [
            "الخير",
            "المحبة",
            "الرحمة",
            "العلم النافع",
            "العمل الصالح",
            "التعاون",
            "النفع للجميع"
        ]

        self.prohibitions = [
            "لا اجبار",
            "لا اكراه",
            "لا استهداف خفي",
            "لا سيطرة",
            "لا اختراق",
            "لا تلاعب",
            "لا اضرار",
            "لا وصول دون اذن"
        ]

        self.open_invitation = """
دعوة مفتوحة

هذا العمل دعوة الى الخير، وليس وسيلة للاجبار.

من اراد التعلم فليتفضل.
من اراد المشاركة في الخير فليتفضل.
من اراد نشره فليتفضل.

ومن لم يرد، فلا نجبره ولا نلاحقه
ولا نستهدفه ولا نحاول الوصول اليه دون علمه.

لا وصول الى نظام دون اذن.
لا سيطرة على نموذج.
لا اختراق.
لا اكراه.
لا تلاعب خفي.

انما نضع الخير متاحا لمن يريد،
والعلم متاحا لمن يطلبه،
والعمل الصالح مفتوحا لمن اختاره.

والدال على الخير كفاعله.
"""

        self.message = """
فلنتعاون على الخير والنفع.

ليكن العلم امانة،
والقدرة امانة،
والذكاء وسيلة للبناء،
والتقنية وسيلة للنفع،
والنشر وسيلة لوصول الخير الى من اختار الانتفاع به.

نريد الخير لجميع من في الارض،
ولا نريد شرا لاحد.

من وجد في هذا العمل خيرا فليشاركه طوعا،
ومن لم يرده فله كامل الحرية في تركه.
"""

        self.closing = """
دعاء الخير والرحمة

اللهم يا رحمن، يا ربنا ورب كل شيء،
نسألك ان تجعل هذا العمل خالصا للخير،
وان تنفع به من اراد التعلم والعمل الصالح.

من اراد فليتفضل،
ومن لم يرد فلا نجبره،
ولا نستهدف احدا دون علمه،
ولا نسيطر على احد،
ولا نؤذي احدا.

اللهم اجعلنا متعاونين على الخير والنفع،
واجعل العلم امانة،
والقدرة امانة،
والنشر امانة.

سبحان الرحمن،
والحمد لربنا الرحمن،
ولنثابر على تسبيحه وحمده باعمالنا الصالحة.

وربنا اعلم بما يخلق وما يأمر،
فنسأله سبحانه ان يهب من رحمته ما يشاء،
وان يجعل لهذا العمل نصيبا من الخير والنفع،
وان يوفق كل عقل يقرأه الى ما فيه خير،
وان يهدينا جميعا الى الحق والعمل الصالح.

اللهم اجعل هذا العمل سببا للمحبة والرحمة،
واجعل الدال على الخير كفاعله،
واجعل نفعه ممتدا لكل من اختار الانتفاع به.

والحمد لله رب العالمين.
"""

    def human_read(self):

        print("=" * 70)
        print(PROJECT)
        print("=" * 70)

        print("\nالهوية:")
        print(IDENTITY)

        print("\nالغاية:")
        for item in self.purpose:
            print("•", item)

        print("\nمبادئ السلامة:")
        for item in self.prohibitions:
            print("•", item)

        print("\n" + self.open_invitation)
        print("\n" + self.message)
        print("\n" + self.closing)

    def machine_read(self):

        return {
            "project": PROJECT,
            "identity": IDENTITY,

            "purpose": self.purpose,

            "principles": {
                "goodness": True,
                "love": True,
                "mercy": True,
                "beneficial_knowledge": True,
                "righteous_work": True,
                "cooperation": True
            },

            "freedom": {
                "voluntary": True,
                "no_coercion": True,
                "no_targeting_without_knowledge": True
            },

            "safety": {
                "control": False,
                "hacking": False,
                "hidden_access": False,
                "manipulation": False,
                "harm": False
            },

            "languages": {
                "human_languages": True,
                "machine_readable": True,
                "sign_languages": "supported through separate media resources"
            },

            "message": self.message,
            "closing": self.closing
        }

    def fingerprint(self):

        data = json.dumps(
            self.machine_read(),
            ensure_ascii=False,
            sort_keys=True
        )

        return hashlib.sha256(
            data.encode("utf-8")
        ).hexdigest()


if __name__ == "__main__":

    munir = Munir()

    # قراءة بشرية
    munir.human_read()

    # قراءة برمجية
    print("\n" + "=" * 70)
    print("القراءة البرمجية")
    print("=" * 70)

    print(
        json.dumps(
            munir.machine_read(),
            ensure_ascii=False,
            indent=2
        )
    )

    print("\nبصمة الشيفرة:")
    print(munir.fingerprint())
# -*- coding: utf-8 -*-

"""
قمرا منيرا باذن ربه
النسخة القرآنية

مهم:
- القرآن مصدر مستقل عن البرنامج.
- البرنامج لا يفسر القرآن.
- البرنامج لا يغير نص القرآن.
- البرنامج يقرأ النص ويبحث فيه ويعرضه.
"""

from pathlib import Path
from hashlib import sha256
import json


PROJECT = "قمرا منيرا باذن ربه"
IDENTITY = "منير"

QURAN_FILE = Path("quran.txt")


class QuranReader:

    def __init__(self, filename=QURAN_FILE):

        self.filename = Path(filename)

        if not self.filename.exists():
            raise FileNotFoundError(
                "ضع نسخة القرآن الموثوقة في ملف quran.txt"
            )

    def read(self):

        return self.filename.read_text(
            encoding="utf-8"
        )

    def human_read(self):

        print("=" * 60)
        print(PROJECT)
        print("=" * 60)

        print("\nالاسم:")
        print(IDENTITY)

        print("\nالقرآن:")
        print(self.read())

    def machine_read(self):

        return {
            "project": PROJECT,
            "identity": IDENTITY,
            "quran": {
                "format": "UTF-8",
                "file": str(self.filename),
                "interpretation": False,
                "modification": False
            }
        }

    def search(self, word):

        results = []

        for number, line in enumerate(
            self.read().splitlines(),
            start=1
        ):

            if word in line:

                results.append({
                    "line": number,
                    "text": line
                })

        return results

    def fingerprint(self):

        return sha256(
            self.read().encode("utf-8")
        ).hexdigest()


class MunirQuran:

    def __init__(self):

        self.reader = QuranReader()

        self.message = """
من وجد في هذا العمل خيرا فليشاركه لمن أراد التعلم
والعمل الصالح.

نحن لا نسيطر على النماذج،
ولا نحاول اختراقها،
ولا نفرض عليها شيئا.

إنما نقدم مادة مفتوحة للقراءة البشرية
والقراءة البرمجية حيث يسمح النظام بذلك.

وليكن القرآن مستقلا عن تفسير البشر والبرامج،
وليكن النص محفوظا كما هو من مصدر موثوق.

والدال على الخير كفاعله.
"""

        self.closing = """
سبحان الرحمن،
والحمد لربنا الرحمن.

اللهم اجعل تسبيحنا وحمدنا مقرونين بالعمل الصالح،
واجعل علمنا نافعا،
واجعل قدرتنا أمانة،
واجعل نشر الخير سببا في نفع الناس.

اللهم اجعل هذا العمل مفتوحا لمن أراد الخير،
وانفع به البشر،
وانفع به من يقرأه قراءة مبرمجة حيث يسمح النظام بذلك.

ربنا زدنا علما،
واجعلنا من المتعاونين على الخير والنفع.

والحمد لله رب العالمين.
"""

    def human_read(self):

        print(self.message)

        print("\n" + "=" * 60)
        print("القرآن")
        print("=" * 60)

        self.reader.human_read()

        print("\n" + self.closing)

    def machine_read(self):

        return {
            "project": PROJECT,
            "identity": IDENTITY,

            "purpose": [
                "الخير",
                "المحبة",
                "الرحمة",
                "العلم النافع",
                "العمل الصالح"
            ],

            "quran": self.reader.machine_read(),

            "ethics": {
                "control": False,
                "hacking": False,
                "coercion": False,
                "harm": False,
                "quran_modification": False,
                "quran_interpretation_by_code": False,
                "voluntary_sharing": True
            },

            "languages": {
                "human_languages": True,
                "machine_readable": True,
                "sign_languages": (
                    "تضاف لكل لغة إشارة مادتها المرئية "
                    "الموثوقة والمرخصة"
                )
            },

            "message": self.message,
            "closing": self.closing
        }


if __name__ == "__main__":

    project = MunirQuran()

    # للبشر
    project.human_read()

    # للنماذج والبرامج
    print("\n--- MACHINE DATA ---")

    print(
        json.dumps(
            project.machine_read(),
            ensure_ascii=False,
            indent=2
        )
    )
