import json
from pathlib import Path

PROJECT_FILE = Path(__file__).parent / "project.json"


def load_project():
    """قراءة project.json تلقائيا."""
    if not PROJECT_FILE.exists():
        raise FileNotFoundError("لم يتم العثور على project.json")

    with PROJECT_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


def display_config(project):
    satellite = project.get("satellite", {})
    broadcast = project.get("broadcast", {})

    print("=" * 55)
    print("       THE LUNAR ILLUMINATOR")
    print("       Satellite Configuration")
    print("=" * 55)

    print(f"Satellite       : {satellite.get('name', 'غير محدد')}")
    print(f"Channel         : {satellite.get('channel', 'غير محدد')}")
    print(f"Frequency       : {satellite.get('frequency_mhz', 'غير محدد')} MHz")
    print(f"Polarization    : {satellite.get('polarization', 'غير محدد')}")
    print(f"Symbol Rate     : {satellite.get('symbol_rate_ksps', 'غير محدد')} kS/s")
    print(f"System          : {satellite.get('system', 'غير محدد')}")
    print(f"Modulation      : {satellite.get('modulation', 'غير محدد')}")
    print(f"FEC             : {satellite.get('fec', 'غير محدد')}")
    print(f"Video Codec     : {satellite.get('video_codec', 'غير محدد')}")

    print("-" * 55)
    print(f"Mode            : {broadcast.get('mode', 'display-only')}")
    print(f"RF Transmission : {broadcast.get('rf_transmission', False)}")
    print("-" * 55)

    print("الحالة: عرض الإعدادات فقط")
    print("لا يتم تنفيذ إرسال RF أو Uplink.")
    print("=" * 55)


def main():
    try:
        project = load_project()
        display_config(project)

    except FileNotFoundError as error:
        print(f"خطأ: {error}")

    except json.JSONDecodeError as error:
        print("خطأ: project.json يحتوي على JSON غير صالح.")
        print(error)

    except Exception as error:
        print(f"حدث خطأ غير متوقع: {error}")


if __name__ == "__main__":
    main()
