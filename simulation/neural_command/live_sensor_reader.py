import json, subprocess, time
from pathlib import Path
from datetime import datetime, timezone

base = Path(__file__).resolve().parent
log = base / "live_sensor_readings.jsonl"

def run(args):
    return subprocess.run(args, capture_output=True, text=True, timeout=20)

print("قمرا منيرا بإذن ربه")
print("قارئ مستشعرات الهاتف الحقيقية")
print("هذه ليست قراءة دماغية EEG.")

try:
    sensors = run(["termux-sensor", "-l"])
    print(sensors.stdout or sensors.stderr)

    if sensors.returncode != 0:
        print("تعذر الوصول للمستشعرات. تحقق من تطبيق Termux:API.")
        raise SystemExit(1)

    print("بدأ التسجيل. اضغط Ctrl+C للإيقاف.")

    while True:
        result = run(["termux-sensor", "-n", "1"])
        entry = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "source": "android_sensor_api",
            "brain_reading": False,
            "success": result.returncode == 0,
            "output": result.stdout,
            "error": result.stderr
        }
        with log.open("a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
        print(result.stdout or result.stderr or "لا توجد بيانات")
        time.sleep(2)

except KeyboardInterrupt:
    print("\nتم إيقاف التسجيل بأمان.")
except Exception as exc:
    print("خطأ:", exc)
