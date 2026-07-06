from backend.storage.application_storage import (
    add_application,
    load_applications,
    save_applications
)


class ApplicationService:

    @staticmethod
    def create_application(company, job_title, location, link, status, notes):
        return add_application(
            company,
            job_title,
            location,
            link,
            status,
            notes
        )

    @staticmethod
    def get_all_applications():
        return load_applications()

    @staticmethod
    def update_status(application_id, new_status):
        applications = load_applications()

        for application in applications:
            if application["id"] == application_id:
                application["status"] = new_status

        save_applications(applications)

    @staticmethod
    def delete_application(application_id):
        applications = load_applications()

        applications = [
            application
            for application in applications
            if application["id"] != application_id
        ]

        save_applications(applications)