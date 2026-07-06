from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = PROJECT_ROOT / "data"

PROFILE_FILE = DATA_DIR / "user_profile.json"
APPLICATIONS_FILE = DATA_DIR / "applications.json"

APP_NAME = "DecisionOS"
VERSION = "0.1.0"