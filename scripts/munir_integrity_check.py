import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FILES = [
    "security/munir_integrity_protocol.json",
    "research/simulation/earth_armies_virtual_world.json",
]

errors = []
report = {
    "project": "The Lunar Illuminator",
    "check": "local_integrity_check",
    "files": {},
}

for name in FILES:
    path = ROOT / name
    if not path.is_file():
        errors.append(f"MISSING: {name}")
        continue

    raw = path.read_bytes()
    try:
        json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        errors.append(f"INVALID JSON: {name}: {exc}")
        continue

    report["files"][name] = {
        "sha256": hashlib.sha256(raw).hexdigest(),
        "json_valid": True,
    }
    print(f"OK: {name}")

protocol_path = ROOT / FILES[0]
world_path = ROOT / FILES[1]

if protocol_path.is_file() and world_path.is_file():
    try:
        protocol = json.loads(protocol_path.read_text(encoding="utf-8"))
        world = json.loads(world_path.read_text(encoding="utf-8"))
        rules = protocol.get("quran_reference", {})

        if rules.get("preserve_text") is not True:
            errors.append("Quran text preservation rule missing")
        if rules.get("model_output_is_not_quran") is not True:
            errors.append("AI/Quran distinction rule missing")

        for key in ("real_world_connections", "command_execution", "weapon_control"):
            if world.get(key) is not False:
                errors.append(f"Simulation boundary invalid: {key}")
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        errors.append(f"Validation error: {exc}")

report["status"] = "FAIL" if errors else "PASS"
report["errors"] = errors
out = ROOT / "security/integrity_report.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\\n", encoding="utf-8")

print("\\nSTATUS:", report["status"])
print("REPORT:", out.relative_to(ROOT))
for error in errors:
    print("ERROR:", error)

sys.exit(1 if errors else 0)
