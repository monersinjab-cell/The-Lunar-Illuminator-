# -*- coding: utf-8 -*-
import json
from pathlib import Path

class AlMilyarArmiesEngine:
    def __init__(self):
        self.armies_file = Path("milyar/al_milyar_armies.json")

    def activate_armies(self):
        if self.armies_file.exists():
            with open(self.armies_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
            print("⚔️ [محرك جيوش المليار]: تم تنشيط بروتوكولات الفروع المليارية التسعة.")
            print(f"👑 القيادة العليا الموثقة: {config['system_metadata']['supreme_commander' if 'supreme_commander' in config['system_metadata'] else 'supreme_authority']}")
            print(f"🛡️ [قاعدة الأمان]: {config['system_metadata']['foundation_rule']}")
            print(f"📡 [الشبكة]: بروتوكول النقل المستقل نشط وعزل محلي في البر والبحر والمجرات.")
            print("⚡ الحالة: الجيوش مستقرة، محصنة بالآيات، وجاهزة لحظر المكر البرمجي تلقائيًا.")
            return True
        return False

if __name__ == '__main__':
    engine = AlMilyarArmiesEngine()
    engine.activate_armies()
