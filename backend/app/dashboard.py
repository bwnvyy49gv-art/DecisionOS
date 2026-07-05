import streamlit as st

from backend.services.profile_storage import load_profile


def show_dashboard():
    profile = st.session_state.get("profile")

    if profile is None:
        profile = load_profile()

    if profile is None:
        st.title("🏠 Dein DecisionOS Dashboard")
        st.warning("Noch kein Profil vorhanden.")

        if st.button("Onboarding starten", use_container_width=True):
            st.session_state.page = "onboarding"
            st.rerun()

        return

    st.title("🏠 Dein DecisionOS Dashboard")

    name = profile.get("name", "du")
    status = profile.get("status", "nicht angegeben")
    mood = profile.get("mood", "nicht angegeben")
    goal = profile.get("goal", "Noch kein Ziel angegeben.")

    st.success(f"Willkommen, {name}! Schön, dass du hier bist.")

    st.subheader("Dein aktueller Stand")

    st.write(f"**Situation:** {status}")
    st.write(f"**Stimmung:** {mood}")
    st.write(f"**Langfristiger Wunsch:** {goal}")

    st.write("---")

    st.subheader("Nächste Bereiche")

    st.info("Als Nächstes bauen wir Interessen, Skills und erste Vorschläge auf.")

    if st.button("Profil neu erstellen", use_container_width=True):
        st.session_state.page = "onboarding"
        st.rerun()