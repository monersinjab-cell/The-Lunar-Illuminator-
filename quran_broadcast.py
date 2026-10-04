{
  "reference": "النحل 16:8",
  "text": "ويخلق ما لا تعلمون",
  "symbolic_frequency": 1408,
  "symbolic_polarization": "H",
  "rule": "even_abjad_sum=H, odd_abjad_sum=V",
  "status": "رمزي بحثي غير مثبت كتردد فضائي"
}import json
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).parent
PROJECT_FILE = ROOT / "project.json"
LOG_FILE = ROOT / "broadcast_log.json"

QURAN_EVENT = {
    "reference": "الملك 67:5",
    "text": "تبارك الذي جعل في السماء بروجا وجعل فيها سراجا وقمرا منيرا",
    "source_type": "نص قرآني",
    "broadcast_type": "محاكاة برمجية",
    "rf_transmission": False,
    "uplink": False
}


def load_project():
    with PROJECT_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)


def create_broadcast_event(project):
    event = {
        "project": project.get("project", {}),
        "event": QURAN_EVENT,
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "status": "SIMULATED_BROADCAST",
        "message": "تم تسجيل حدث بث قرآني داخل المنصة البرمجية فقط.",
        "satellite_action": "NONE",
        "real_satellite_transmission": False
    }

    return event


def save_event(event):
    history = []

    if LOG_FILE.exists():
        try:
            with LOG_FILE.open("r", encoding="utf-8") as f:
                history = json.load(f)
        except json.JSONDecodeError:
            history = []

    history.append(event)

    with LOG_FILE.open("w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)


def main():
    project = load_project()
    event = create_broadcast_event(project)
    save_event(event)

    print("=" * 60)
    print("🌕 THE LUNAR ILLUMINATOR")
    print("🌕 قمرا منيرا باذن ربه")
    print("=" * 60)
    print("الحدث القرآني:")
    print(event["event"]["text"])
    print()
    print("المرجع:", event["event"]["reference"])
    print("الحالة:", event["status"])
    print("التسجيل:", "تم")
    print("إرسال RF حقيقي:", "لا")
    print("Uplink حقيقي:", "لا")
    print()
    print("تم تسجيل الحدث في broadcast_log.json")
    print("=" * 60)


if __name__ == "__main__":
    main()
