from dataclasses import dataclass
from datetime import datetime


@dataclass
class Application:
    id: int
    company: str
    job_title: str
    location: str
    link: str
    status: str
    notes: str
    created_at: str

    def to_dict(self):
        return {
            "id": self.id,
            "company": self.company,
            "job_title": self.job_title,
            "location": self.location,
            "link": self.link,
            "status": self.status,
            "notes": self.notes,
            "created_at": self.created_at
        }

    @staticmethod
    def create_new(application_id, company, job_title, location, link, status, notes):
        return Application(
            id=application_id,
            company=company,
            job_title=job_title,
            location=location,
            link=link,
            status=status,
            notes=notes,
            created_at=datetime.now().strftime("%Y-%m-%d %H:%M")
        )

    @staticmethod
    def from_dict(data):
        return Application(
            id=data.get("id", 0),
            company=data.get("company", ""),
            job_title=data.get("job_title", ""),
            location=data.get("location", ""),
            link=data.get("link", ""),
            status=data.get("status", "Gefunden"),
            notes=data.get("notes", ""),
            created_at=data.get("created_at", "")
        )