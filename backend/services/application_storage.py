import json
from pathlib import Path
from datetime import datetime


DATA_DIR = Path(__file__).resolve().parents[2] / "data"
APPLICATIONS_FILE = DATA_DIR / "applications.json"


def load_applications():
    """Lädt alle Bewerbungen aus der JSON-Datei."""
    if not APPLICATIONS_FILE.exists():
        return []

    with open(APPLICATIONS_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_applications(applications):
    """Speichert alle Bewerbungen lokal."""
    DATA_DIR.mkdir(exist_ok=True)

    with open(APPLICATIONS_FILE, "w", encoding="utf-8") as file:
        json.dump(applications, file, ensure_ascii=False, indent=4)


def add_application(company, job_title, location, link, status, notes):
    """Fügt eine neue Bewerbung hinzu."""
    applications = load_applications()

    new_application = {
        "id": len(applications) + 1,
        "company": company,
        "job_title": job_title,
        "location": location,
        "link": link,
        "status": status,
        "notes": notes,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    applications.append(new_application)
    save_applications(applications)

    return new_application