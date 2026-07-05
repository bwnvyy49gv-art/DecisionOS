from backend.services.profile_storage import save_profile

import streamlit as st


def show_onboarding():
    st.title("👋 Lass uns dich kennenlernen")

    st.write(
        "Wir starten mit ein paar einfachen Fragen. "
        "Du musst noch keinen perfekten Plan haben."
    )

    st.progress(30)

    name = st.text_input("Wie heißt du?")

    status = st.selectbox(
        "Was beschreibt deine aktuelle Situation am besten?",
        [
            "Schüler/in",
            "Auszubildende/r",
            "Student/in",
            "Berufstätig",
            "Berufliche Neuorientierung",
            "Ich bin mir unsicher"
        ]
    )

    mood = st.selectbox(
        "Wie fühlst du dich gerade bei deiner beruflichen Zukunft?",
        [
            "Motiviert",
            "Neugierig",
            "Unsicher",
            "Überfordert",
            "Druck von außen",
            "Orientierungslos",
            "Eigentlich ganz entspannt"
        ]
    )

    goal = st.text_area(
        "Was wünschst du dir langfristig?",
        placeholder="Zum Beispiel: einen sinnvollen Job, gute Sicherheit, Forschung, gutes Gehalt, Selbstständigkeit..."
    )

    if st.button("Weiter zum Dashboard ➜", use_container_width=True):

        profile_data = {
            "name": name,
            "status": status,
            "mood": mood,
            "goal": goal
        }

        save_profile(profile_data)

        st.session_state.profile = profile_data
        st.session_state.page = "dashboard"

        st.rerun()