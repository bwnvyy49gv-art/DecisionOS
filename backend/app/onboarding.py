import streamlit as st

from backend.storage.profile_storage import save_profile


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

    st.subheader("Was beschäftigt dich im Moment am meisten?")

    challenge = st.multiselect(
        "Du kannst mehrere Punkte auswählen.",
        [
            "Ich weiß nicht, welcher Beruf zu mir passt.",
            "Ich weiß nicht, welches Studium oder welche Ausbildung sinnvoll ist.",
            "Ich habe Angst, die falsche Entscheidung zu treffen.",
            "Ich weiß nicht, welche Skills ich lernen soll.",
            "Ich finde keine passenden Stellen.",
            "Ich fühle mich überfordert von den Möglichkeiten.",
            "Ich möchte mich beruflich neu orientieren."
        ]
    )

    st.subheader("Welche Themen interessieren dich spontan?")

    interests = st.multiselect(
        "Wähle alles aus, was dich neugierig macht.",
        [
            "Energie",
            "Raumfahrt",
            "Robotik",
            "KI",
            "Software",
            "Chemie",
            "Biologie",
            "Medizin",
            "Umwelt",
            "Nachhaltigkeit",
            "Wirtschaft",
            "Design",
            "Forschung",
            "Handwerk"
        ]
    )

    goal = st.text_area(
        "Was wünschst du dir langfristig?",
        placeholder=(
            "Zum Beispiel: einen sinnvollen Job, gute Sicherheit, "
            "Forschung, gutes Gehalt, Selbstständigkeit..."
        )
    )

    if st.button("Weiter zum Dashboard ➜", use_container_width=True):
        profile_data = {
            "name": name,
            "status": status,
            "mood": mood,
            "challenge": challenge,
            "interests": interests,
            "goal": goal
        }

        save_profile(profile_data)

        st.session_state.profile = profile_data
        st.session_state.page = "dashboard"

        st.rerun()