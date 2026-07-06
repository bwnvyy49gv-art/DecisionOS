import streamlit as st

from backend.services.profile_storage import load_profile


def show_profile():
    profile = load_profile()

    st.title("👤 Dein Profil")

    if not profile:
        st.warning("Noch kein Profil vorhanden.")
        return

    st.write(f"**Name:** {profile.get('name', 'nicht angegeben')}")
    st.write(f"**Situation:** {profile.get('status', 'nicht angegeben')}")
    st.write(f"**Stimmung:** {profile.get('mood', 'nicht angegeben')}")
    st.write(f"**Ziel:** {profile.get('goal', 'nicht angegeben')}")

    st.subheader("Interessen")
    interests = profile.get("interests", [])

    if interests:
        for interest in interests:
            st.write(f"• {interest}")
    else:
        st.write("Noch keine Interessen angegeben.")