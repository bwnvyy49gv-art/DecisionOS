import streamlit as st

from backend.services.application_storage import (
    add_application,
    load_applications
)


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

        status = st.selectbox(
            "Status",
            [
                "Gefunden",
                "Interessant",
                "Vorbereiten",
                "Beworben",
                "Rückmeldung",
                "Gespräch",
                "Absage",
                "Zusage"
            ]
        )

        notes = st.text_area("Notizen")

        submitted = st.form_submit_button("Bewerbung speichern")

        if submitted:
            if not company or not job_title:
                st.error("Firma und Stelle müssen ausgefüllt sein.")
            else:
                add_application(company, job_title, location, link, status, notes)
                st.success("Bewerbung wurde lokal gespeichert.")
                st.rerun()

    st.write("---")

    st.subheader("Gespeicherte Bewerbungen")

    applications = load_applications()

    if not applications:
        st.info("Noch keine Bewerbungen gespeichert.")
        return

    for application in applications:
        with st.expander(f"{application['company']} — {application['job_title']}"):
            st.write(f"**Standort:** {application.get('location', '-')}")
            st.write(f"**Status:** {application.get('status', '-')}")
            st.write(f"**Link:** {application.get('link', '-')}")
            st.write(f"**Notizen:** {application.get('notes', '-')}")
            st.write(f"**Erstellt:** {application.get('created_at', '-')}")