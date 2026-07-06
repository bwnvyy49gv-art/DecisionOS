import streamlit as st

from backend.services.application_service import ApplicationService


STATUS_OPTIONS = [
    "Gefunden",
    "Interessant",
    "Vorbereiten",
    "Beworben",
    "Rückmeldung",
    "Gespräch",
    "Absage",
    "Zusage"
]


def show_applications():
    st.title("💼 Bewerbungen")

    st.write(
        "Hier kannst du Bewerbungen lokal speichern. "
        "Nichts wird hochgeladen."
    )

    st.subheader("Neue Bewerbung hinzufügen")

    with st.form("application_form"):
        company = st.text_input("Firma")
        job_title = st.text_input("Stelle")
        location = st.text_input("Standort")
        link = st.text_input("Link zur Stelle")

        status = st.selectbox("Status", STATUS_OPTIONS)

        notes = st.text_area("Notizen")

        submitted = st.form_submit_button("Bewerbung speichern")

        if submitted:
            if not company or not job_title:
                st.error("Firma und Stelle müssen ausgefüllt sein.")
            else:
                ApplicationService.create_application(
                    company=company,
                    job_title=job_title,
                    location=location,
                    link=link,
                    status=status,
                    notes=notes
                )
                st.success("Bewerbung wurde lokal gespeichert.")
                st.rerun()

    st.write("---")

    st.subheader("Gespeicherte Bewerbungen")

    applications = ApplicationService.get_all_applications()

    if not applications:
        st.info("Noch keine Bewerbungen gespeichert.")
        return

    for application in applications:
        application_id = application["id"]

        with st.expander(f"{application['company']} — {application['job_title']}"):
            st.write(f"**Standort:** {application.get('location', '-')}")
            st.write(f"**Link:** {application.get('link', '-')}")
            st.write(f"**Notizen:** {application.get('notes', '-')}")
            st.write(f"**Erstellt:** {application.get('created_at', '-')}")

            current_status = application.get("status", "Gefunden")

            new_status = st.selectbox(
                "Status ändern",
                STATUS_OPTIONS,
                index=STATUS_OPTIONS.index(current_status)
                if current_status in STATUS_OPTIONS else 0,
                key=f"status_{application_id}"
            )

            col1, col2 = st.columns(2)

            with col1:
                if st.button("Status speichern", key=f"save_{application_id}"):
                    ApplicationService.update_status(application_id, new_status)
                    st.success("Status wurde aktualisiert.")
                    st.rerun()

            with col2:
                if st.button("Bewerbung löschen", key=f"delete_{application_id}"):
                    ApplicationService.delete_application(application_id)
                    st.warning("Bewerbung wurde gelöscht.")
                    st.rerun()