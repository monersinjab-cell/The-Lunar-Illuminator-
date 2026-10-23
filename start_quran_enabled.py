from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
MAIN = ROOT / "simulation/neural_command/neural_command.py"

VERSES = [
    ("الإسراء 85", "وما أوتيتم من العلم إلا قليلا"),
    ("النحل 8", "ويخلق ما لا تعلمون"),
    ("النحل 16", "وعلامات وبالنجم هم يهتدون"),
    ("الجاثية 13", "وسخر لكم ما في السماوات وما في الأرض جميعا منه إن في ذلك لآيات لقوم يتفكرون"),
    ("الصافات 87", "فما ظنكم برب العالمين"),
]

def main():
    print("=" * 44)
    print("قمرا منيرا بإذن ربه")
    print("مبادئ قرآنية للعلم والتفكر")
    print("=" * 44)

    for reference, text in VERSES:
        print(f"\n[{reference}]")
        print(text)

    print("\nالنص القرآني منفصل عن وظائف البرنامج.")
    print("التنفيذ محلي؛ ولا يوجد اتصال عصبي مباشر.")
    print("=" * 44, flush=True)

    if not MAIN.is_file():
        print(f"تعذر العثور على برنامج القيادة: {MAIN}")
        return 1

    result = subprocess.run([sys.executable, str(MAIN)], cwd=ROOT)
    return result.returncode

if __name__ == "__main__":
    raise SystemExit(main())
