#!/usr/bin/env python3
import hashlib
import json
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
source_dir = root / "quran" / "source"
report_path = source_dir / "SOURCE_VERIFICATION.json"
original_path = source_dir / "tanzil_download_original.txt"
processed_path = source_dir / "tanzil_quran_uthmani.txt"

def fail(message):
    print("FAIL:", message)
    sys.exit(1)

for path in (report_path, original_path, processed_path):
    if not path.is_file():
        fail(f"Missing required file: {path.relative_to(root)}")

try:
    report = json.loads(report_path.read_text(encoding="utf-8"))
except Exception as exc:
    fail(f"Invalid verification JSON: {exc}")

def sha256(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

expected_original = report.get("original_download_sha256")
expected_processed = report.get("processed_file_sha256")
actual_original = sha256(original_path)
actual_processed = sha256(processed_path)

if not expected_original or actual_original != expected_original:
    fail("Original Tanzil download hash does not match the recorded hash")
if not expected_processed or actual_processed != expected_processed:
    fail("Processed Quran text hash does not match the recorded hash")

records = []
try:
    for line_number, raw in enumerate(
        processed_path.read_text(encoding="utf-8").splitlines(), 1
    ):
        parts = raw.split("|", 2)
        if len(parts) != 3:
            fail(f"Malformed record at line {line_number}")
        surah_text, ayah_text, text = parts
        if not surah_text.isdigit() or not ayah_text.isdigit() or not text.strip():
            fail(f"Invalid record at line {line_number}")
        surah, ayah = int(surah_text), int(ayah_text)
        if not 1 <= surah <= 114 or ayah < 1:
            fail(f"Out-of-range identifier at line {line_number}")
        records.append((surah, ayah, text))

except Exception as exc:
    fail(f"Unable to read processed Quran text: {exc}")

if len(records) != 6236:
    fail(f"Expected 6236 records, found {len(records)}")
if len({(s, a) for s, a, _ in records}) != len(records):
    fail("Duplicate surah/ayah identifiers found")
if {s for s, _, _ in records} != set(range(1, 115)):
    fail("Expected all 114 surahs")
if [ (s, a) for s, a, _ in records ] != sorted((s, a) for s, a, _ in records):
    fail("Records are not ordered by surah and ayah")

print("PASS: recorded source hashes match")
print("PASS: 6236 records, 114 surahs, unique ordered identifiers")
print("LIMIT: structural integrity only; not independent verse-by-verse verification")
