import json
from pathlib import Path

FILE = Path(__file__).with_name("models_registry.json")

def main():
    data = json.loads(FILE.read_text(encoding="utf-8"))
    print("منظومة:", data["project"])
    print("السجل:", data["system"])
    print("-" * 40)

    for model in data["models"]:
        print(f'{model["provider"]}: {model["role"]}')
        print(f'الحالة: {model["status"]}')
        print(f'تم التحقق من الاتصال: {model["verified"]}')
        print()

    print("فحص السجل: ناجح")
    print("تنبيه: السجل لا يعني أن النماذج متصلة فعليا.")

if __name__ == "__main__":
    main()
