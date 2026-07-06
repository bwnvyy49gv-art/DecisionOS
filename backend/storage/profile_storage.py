import json

from backend.config.settings import PROFILE_FILE
from backend.models.user_profile import UserProfile


def save_profile(profile):
    PROFILE_FILE.parent.mkdir(exist_ok=True)

    if isinstance(profile, UserProfile):
        profile_data = profile.to_dict()
    else:
        profile_data = profile

    with open(PROFILE_FILE, "w", encoding="utf-8") as file:
        json.dump(profile_data, file, ensure_ascii=False, indent=4)


def load_profile():
    if not PROFILE_FILE.exists():
        return None

    with open(PROFILE_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

    return UserProfile.from_dict(data)