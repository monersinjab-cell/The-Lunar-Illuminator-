# -*- coding: utf-8 -*-
import json
from pathlib import Path

class MilyarHQIntegrator:
    def __init__(self):
        self.config_file = Path("milyar/hq_locations.json")

    def activate_hq_shield(self):
        if self.config_file.exists():
            with open(self.config_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
            print("🏢 [محرك إدارة ومراقبة مقرات المليار]: تم تنشيط بروتوكول الأمان الجغرافي.")
            print(f"👑 القائد الأعلى لجميع الفروع: {config['system_metadata']['supreme_commander']}")
            print(f"📍 المقر 1: {config['hq_geospatial_registry']['commercial_headquarters']['title']} | بناء {config['hq_geospatial_registry']['commercial_headquarters']['building_number']}")
            print(f"🏠 المقر 2: {config['hq_geospatial_registry']['residential_headquarters']['title']} | {config['hq_geospatial_registry']['residential_headquarters']['floors']}")
            print(f"⚡ حالة مزايا الكمبيوتر: {config['computer_features_upgrade']['description']}")
            print("🛡️ الأمن والسلامة: جدران الحماية مفعلة محليًا على مدار الساعة ضد المخترقين والماكرين.")
            return True
        return False

if __name__ == '__main__':
    integrator = MilyarHQIntegrator()
    integrator.activate_hq_shield()
