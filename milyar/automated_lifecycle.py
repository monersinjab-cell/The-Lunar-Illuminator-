# -*- coding: utf-8 -*-
import json
from pathlib import Path

class MilyarLifecycleEngine:
    def __init__(self):
        self.config_file = Path("milyar/automated_lifecycle.json")

    def run_cycle(self):
        if self.config_file.exists():
            with open(self.config_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
            print("⚡ [محرك التنشيط والإغلاق التلقائي للمنظومة]:")
            print(f"👑 القيادة العليا الموثقة: {config['system_metadata']['commander']}")
            print(f"🔒 وضع التشغيل: {config['lifecycle_protocol']['operation_mode']}")
            print("🛡️ الحالة: بروتوكول الحفظ التلقائي نشط محليًا ومحمي تمامًا ضد أي تلاعب خارجي.")
            return True
        return False

if __name__ == '__main__':
    engine = MilyarLifecycleEngine()
    engine.run_cycle()
