# The-Lunar-Illuminator-
The Lunar Illuminator 
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
