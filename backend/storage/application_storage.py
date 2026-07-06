import json

from backend.config.settings import APPLICATIONS_FILE
from backend.models.application import Application


def load_applications():
    if not APPLICATIONS_FILE.exists():
        return []

    with open(APPLICATIONS_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

    return [Application.from_dict(item) for item in data]


def save_applications(applications):
    APPLICATIONS_FILE.parent.mkdir(exist_ok=True)

    data = [
        application.to_dict() if isinstance(application, Application) else application
        for application in applications
    ]

    with open(APPLICATIONS_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def add_application(company, job_title, location, link, status, notes):
    applications = load_applications()

    next_id = len(applications) + 1

    new_application = Application.create_new(
        application_id=next_id,
        company=company,
        job_title=job_title,
        location=location,
        link=link,
        status=status,
        notes=notes
    )

    applications.append(new_application)
    save_applications(applications)

    return new_application