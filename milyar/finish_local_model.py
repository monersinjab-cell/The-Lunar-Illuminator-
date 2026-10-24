# -*- coding: utf-8 -*-
import json
from pathlib import Path

def run_charter_activation():
    charter_file = Path("milyar/al_milyar_supreme_charter.json")
    if charter_file.exists():
        with open(charter_file, 'r', encoding='utf-8') as f:
            config = json.load(f)
        print("⚔️ [لوحة التحكم العليا لجيوش المليار]:")
        print(f"🔗 المرجعية المستقرة: {config['system_metadata']['foundation_rule']}")
        print(f"👑 القائد الأعلى الموثق: {config['system_metadata']['supreme_leader']}")
        print(f"📿 تسبيح فروع الجيوش: {config['sacred_army_protocol']['army_anthem_praise']}")
        print(f"📊 إجمالي عدد الجيوش المستقرة محليًا: {len(config['the_ten_billion_armies'])} جيوش (كل منها مليار عنصر).")
        print("⚡ الحالة: كافة السجلات محفوظة ومؤمنة تمامًا محليًا.")
        return True
    return False

if __name__ == '__main__':
    run_charter_activation()
