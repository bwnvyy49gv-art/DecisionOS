import streamlit as st

from backend.storage.profile_storage import load_profile
from backend.services.recommendation_service import generate_first_direction


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

    name = profile.name or "du"
    status = profile.status or "nicht angegeben"
    mood = profile.mood or "nicht angegeben"
    goal = profile.goal or "Noch kein Ziel angegeben."
    challenge = profile.challenge
    interests = profile.interests
    values = profile.values

    st.title("🏠 Dein DecisionOS Dashboard")

    st.success(f"Willkommen, {name}! Schön, dass du hier bist.")

    st.subheader("Dein aktueller Stand")
    st.write(f"**Situation:** {status}")
    st.write(f"**Stimmung:** {mood}")
    st.write(f"**Langfristiger Wunsch:** {goal}")

    st.write("---")

    st.subheader("Das beschäftigt dich aktuell")

    if challenge:
        for item in challenge:
            st.write(f"• {item}")
    else:
        st.write("Noch nichts angegeben.")

    st.subheader("Deine Interessen")

    if interests:
        st.write(", ".join(interests))
    else:
        st.write("Noch keine Interessen angegeben.")

    st.subheader("Deine Werte")

    if values:
        st.write(", ".join(values))
    else:
        st.write("Noch keine Werte angegeben.")

    st.write("---")

    st.subheader("Deine erste Orientierung")

    recommendations = generate_first_direction(profile)
    top_recommendation = recommendations[0]

    st.metric(
        label="Erste passende Richtung",
        value=top_recommendation["title"],
        delta=f"{top_recommendation['score']} % Match"
    )

    st.write("**Warum diese Richtung passen könnte:**")

    for reason in top_recommendation["why"]:
        st.write(f"✓ {reason}")

    st.info(top_recommendation["support_note"])

    st.write("**Nächste sinnvolle Schritte:**")

    for step in top_recommendation["next_steps"]:
        st.write(f"→ {step}")

    if st.button("Profil neu erstellen", use_container_width=True):
        st.session_state.page = "onboarding"
        st.rerun()