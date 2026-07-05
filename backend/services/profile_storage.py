import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[2] / "data"
PROFILE_FILE = DATA_DIR / "user_profile.json"


def save_profile(profile_data):
    DATA_DIR.mkdir(exist_ok=True)

    with open(PROFILE_FILE, "w", encoding="utf-8") as file:
        json.dump(profile_data, file, ensure_ascii=False, indent=4)


def load_profile():
    if not PROFILE_FILE.exists():
        return None

    with open(PROFILE_FILE, "r", encoding="utf-8") as file:
        return json.load(file)