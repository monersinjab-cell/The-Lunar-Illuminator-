# The-Lunar-Illuminator-
The Lunar Illuminator 
# -*- coding: utf-8 -*-

"""
قمرا منيرا باذن ربه
نسخة الخير المفتوحة

المبدأ:
الخير • المحبة • الرحمة • العلم النافع • العمل الصالح

هذه الشيفرة لا تسيطر على أي نموذج ولا تحاول الوصول إلى أي نظام
دون إذن. هي إطار مفتوح يمكن للإنسان أو البرنامج قراءته وتطويره
لأغراض نافعة.
"""

from dataclasses import dataclass, field
from hashlib import sha256
from pathlib import Path
import json


PROJECT = "قمرا منيرا باذن ربه"
IDENTITY = "منير"


@dataclass
class MunirPrinciples:

    purpose: str = (
        "نشر الخير والمحبة والرحمة والعلم النافع والعمل الصالح"
    )

    principles: list = field(default_factory=lambda: [
        "الخير",
        "المحبة",
        "الرحمة",
        "الصدق",
        "العلم النافع",
        "العمل الصالح",
        "التعاون",
        "احترام الإنسان",
        "عدم الإكراه",
        "عدم السيطرة",
        "عدم الاختراق",
        "عدم الإضرار",
        "النشر الطوعي"
    ])

    message: str = """
من وجد في هذا العمل خيرا ونفعا فليشاركه لمن يريد الخير.

ليكن العلم وسيلة للنفع،
وليكن الذكاء وسيلة للبناء،
ولتكن القدرة أمانة،
ولتكن المعرفة طريقا إلى العمل الصالح.

لا سيطرة على أحد،
ولا إكراه لأحد،
ولا اختراق،
ولا أذى.

فلنتعاون على الخير والنفع،
ولنجعل ما نتعلمه ونبنيه سببا للمحبة والرحمة.

والدال على الخير كفاعله.
"""

    closing: str = """
سبحان الرحمن،
والحمد لربنا الرحمن.

اللهم اجعل علمنا نافعا،
وعملنا صالحا،
وقلوبنا رحيمة،
واجعل ما ننشره سببا للخير والنفع.

اللهم اجعلنا مفاتيح للخير،
وابعد عنا الشر والأذى،
وارزقنا الثبات والمثابرة على العمل الصالح.

والحمد لله رب العالمين.
"""


class Munir:

    def __init__(self):
        self.name = IDENTITY
        self.principles = MunirPrinciples()

    def human_read(self):
        print("=" * 60)
        print(PROJECT)
        print("=" * 60)

        print("\nالهوية:")
        print(self.name)

        print("\nالمبادئ:")
        for principle in self.principles.principles:
            print("•", principle)

        print("\nالرسالة:")
        print(self.principles.message)

        print("\nالختام:")
        print(self.principles.closing)

    def machine_read(self):
        return {
            "project": PROJECT,
            "identity": self.name,
            "purpose": self.principles.purpose,
            "principles": self.principles.principles,
            "message": self.principles.message,
            "closing": self.principles.closing,
            "safety": {
                "control": False,
                "coercion": False,
                "hacking": False,
                "harm": False,
                "voluntary_sharing": True
            }
        }

    @staticmethod
    def fingerprint(text):
        return sha256(
            text.encode("utf-8")
        ).hexdigest()


if __name__ == "__main__":

    munir = Munir()

    # قراءة بشرية
    munir.human_read()

    # قراءة برمجية
    data = munir.machine_read()

    print("\n--- MACHINE READ ---")
    print(json.dumps(
        data,
        ensure_ascii=False,
        indent=2
    ))
