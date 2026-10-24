# -*- coding: utf-8 -*-
import json
from pathlib import Path

class MilyarVehicleIntegratedShield:
    def __init__(self):
        self.manifest_file = Path("milyar/vehicle_manifest.json")

    def activate_shield(self):
        if self.manifest_file.exists():
            with open(self.manifest_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
            print("🚗 [محرك السيطرة والتحصين لمركبة القيادة العليا]:")
            print(f"🔗 المرجعية المستقرة: {config['armies_tactical_support']['foundation_axiom'] if 'armies_tactical_support' in config else 'فَمَا ظَنُّكُم بِرَبِّ الْعَالَمِينَ'}")
            print(f"👑 القائد الأعلى للمنظومة والمركبة: {config['vehicle_metadata']['identity'] if 'vehicle_metadata' in config else 'منير سنجاب'}")
            print("⚔️ [إسناد جيوش المليار لحماية المركبة]:")
            if "armies_tactical_support" in config:
                for army, mission in config['armies_tactical_support']['assigned_forces'].items():
                    print(f"  • {army}: {mission}")
            print("⚡ الحالة: درع حماية وتطوير المركبة نشط تلقائيًا بموجب القواعد المحكمة محليًا.")
            return True
        return False

if __name__ == '__main__':
    integrator = MilyarVehicleIntegratedShield()
    integrator.activate_shield()
