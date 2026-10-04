# -*- coding: utf-8 -*-
"""The Lunar Illuminator - Large RF/Satellite simulation.
SIMULATION ONLY: no RF hardware, no uplink, no real transmission.
"""

import json, math, random
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent
CONFIG = ROOT / "config.json"
STATUS = ROOT / "RF_STATUS.json"

def load():
    return json.loads(CONFIG.read_text(encoding="utf-8"))

def db(x):
    return 10 * math.log10(max(x, 1e-12))

def run():
    cfg = load()
    random.seed(cfg["simulation"]["seed"])
    now = datetime.now(timezone.utc).isoformat()
    records = []

    for sat in cfg["satellites"]:
        for ch in cfg["channels"]:
            noise = random.uniform(-1.0, 1.0)
            snr = ch["nominal_snr_db"] + noise
            loss = random.uniform(0.1, 3.0)
            quality = max(0.0, min(100.0, 50 + snr * 3 - loss * 2))
            records.append({
                "timestamp": now,
                "satellite": sat["id"],
                "band": ch["band"],
                "frequency_mhz": ch["frequency_mhz"],
                "modulation": ch["modulation"],
                "simulated_snr_db": round(snr, 3),
                "simulated_path_loss_db": round(loss, 3),
                "simulated_quality_percent": round(quality, 2),
                "packet_error_rate": round(max(0.0, 0.02 - snr / 1000), 6),
                "transmission": False,
                "uplink": False,
                "simulation_only": True,
            })

    out = {
        "project": cfg["project"],
        "status": "SIMULATION_ONLY",
        "generated_at": now,
        "rf_transmission": False,
        "satellite_uplink": False,
        "channel_count": len(cfg["channels"]),
        "satellite_count": len(cfg["satellites"]),
        "record_count": len(records),
        "records": records,
    }
    STATUS.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Created {STATUS}")
    print(f"Satellites: {len(cfg['satellites'])}")
    print(f"Channels:   {len(cfg['channels'])}")
    print(f"Records:    {len(records)}")
    print("REAL RF TRANSMISSION: DISABLED")

if __name__ == "__main__":
    run()
