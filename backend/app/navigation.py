import streamlit as st


def show_sidebar():
    st.sidebar.title("🧭 DecisionOS")

    st.sidebar.write("Navigate your future. Grow with confidence.")

    st.sidebar.divider()

    if st.sidebar.button("🏠 Dashboard", use_container_width=True):
        st.session_state.page = "dashboard"
        st.rerun()

    if st.sidebar.button("👤 Profil", use_container_width=True):
        st.session_state.page = "profile"
        st.rerun()

    if st.sidebar.button("💼 Bewerbungen", use_container_width=True):
        st.session_state.page = "applications"
        st.rerun()

    if st.sidebar.button("❤️ Check-in", use_container_width=True):
        st.session_state.page = "checkin"
        st.rerun()

    st.sidebar.divider()

    if st.sidebar.button("🔄 Onboarding neu starten", use_container_width=True):
        st.session_state.page = "onboarding"
        st.rerun()