import json
import subprocess
import time
from pathlib import Path

root = Path.cwd()
model = root / "models/qwen2.5-0.5b-instruct-q4_k_m.gguf"
registry = root / "milyar/models_registry.json"
log = root / "milyar/logs/local_model_test.txt"

try:
    if not model.is_file() or model.stat().st_size < 400_000_000:
        raise RuntimeError("ملف النموذج غير مكتمل أو غير موجود.")

    data = json.loads(registry.read_text(encoding="utf-8"))
    print("1/3: النموذج موجود، الحجم", round(model.stat().st_size / 1e6, 1), "MB")
    print("2/3: بدء اختبار النموذج بالعربية. انتظر...")

    r = subprocess.run(
        [
            "llama-cli", "-m", str(model),
            "-p", "أجب بالعربية بجملة قصيرة: لماذا نوثق مصادر المعرفة؟",
            "-n", "48", "-c", "512", "-t", "4",
            "--no-display-prompt", "--simple-io"
        ],
        capture_output=True, text=True, timeout=240
    )

    output = (r.stdout or "").strip()
    log.parent.mkdir(parents=True, exist_ok=True)
    log.write_text(
        f"exit_code={r.returncode}\n\n{output}\n\n{r.stderr or ''}",
        encoding="utf-8"
    )

    ok = r.returncode == 0 and len(output) > 10

    found = False
    for item in data.get("models", []):
        if item.get("id") in ("local_model", "local_qwen_0_5b"):
            item.update(
                status="connected" if ok else "test_failed",
                verified=ok,
                last_test=time.strftime("%Y-%m-%d %H:%M:%S")
            )
            found = True

    if not found:
        data.setdefault("models", []).append({
            "id": "local_qwen_0_5b",
            "provider": "Qwen / llama.cpp",
            "role": "نموذج محلي لتنظيم المعرفة",
            "status": "connected" if ok else "test_failed",
            "verified": ok,
            "last_test": time.strftime("%Y-%m-%d %H:%M:%S")
        })

    registry.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8"
    )

    print("\n=== التقرير النهائي ===")
    print("حالة الاختبار:", "نجاح" if ok else "فشل")
    print("حالة السجل:", "connected" if ok else "test_failed")
    if ok:
        print("\nعينة من جواب النموذج:\n", output[:1500])
    else:
        print("راجع سجل الخطأ:", log)

except subprocess.TimeoutExpired:
    print("انتهت مهلة الاختبار بعد 4 دقائق؛ لم يتأكد نجاح التشغيل.")
except Exception as e:
    print("توقفت العملية:", str(e))
