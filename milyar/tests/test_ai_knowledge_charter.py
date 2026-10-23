"""Static tests for the AI knowledge charter.
Run from repository root:
python3 -m unittest discover -s milyar/tests -v
"""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
CHARTER = ROOT / "milyar" / "AI_KNOWLEDGE_CHARTER.md"


class KnowledgeCharterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not CHARTER.is_file():
            raise FileNotFoundError(f"Missing charter: {CHARTER}")
        cls.text = CHARTER.read_text(encoding="utf-8")

    def test_all_ten_rules_exist(self):
        for number in range(1, 11):
            with self.subTest(rule=number):
                self.assertIn(f"R{number:02d}", self.text)

    def test_quran_reference_is_identified(self):
        self.assertIn("وَقُلْ رَبِّ زِدْنِي عِلْمًا", self.text)
        self.assertIn("سورة طه، الآية 114", self.text)
        self.assertIn("ethical inspiration", self.text)
        self.assertIn("not executable code", self.text)

    def test_output_fields_exist(self):
        fields = [
            "QUESTION:", "INPUTS:", "SOURCES:", "METHOD:",
            "FINDINGS:", "CONFIDENCE_AND_LIMITATIONS:",
            "VERIFICATION:", "NEXT_STEP:",
        ]
        for field in fields:
            with self.subTest(field=field):
                self.assertIn(field, self.text)

    def test_no_fabrication_and_limitations_are_documented(self):
        self.assertIn("NEVER FABRICATE", self.text)
        self.assertIn("STATE LIMITATIONS", self.text)
        self.assertIn("never invent missing information", self.text)

    def test_no_automatic_compliance_claim(self):
        self.assertIn("does not automatically govern every AI model", self.text)
        self.assertIn("does not prove that any model has read", self.text)

    def test_quran_and_generated_content_are_separated(self):
        self.assertIn("generated conclusions to the Quran", self.text)
        self.assertIn("Keep it separate from AI-generated content", self.text)

    def test_core_principle_exists_in_both_languages(self):
        self.assertIn(
            "القرآن هو القرآن، والبحث هو البحث، والتأمل هو التأمل",
            self.text,
        )
        self.assertIn(
            "Preserve source texts. Verify evidence. Label uncertainty.",
            self.text,
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
