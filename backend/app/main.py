import streamlit as st

from backend.app.onboarding import show_onboarding
from backend.app.dashboard import show_dashboard
from backend.app.navigation import show_sidebar
from backend.app.profile import show_profile
from backend.app.applications import show_applications
from backend.app.checkin import show_checkin


st.set_page_config(
    page_title="DecisionOS",
    page_icon="🧭",
    layout="wide"
)

if "page" not in st.session_state:
    st.session_state.page = "welcome"


if st.session_state.page != "welcome":
    show_sidebar()


if st.session_state.page == "welcome":
    st.title("🧭 DecisionOS")
    st.subheader("Navigate your future. Grow with confidence.")
    st.write("---")

    st.markdown("""
### Du musst deine berufliche Zukunft nicht alleine planen.

DecisionOS begleitet dich Schritt für Schritt bei wichtigen Entscheidungen rund um:

- Studium
- Ausbildung
- Beruf
- Karriere
- Weiterbildung
- persönliche Entwicklung

Dabei geht es nicht nur um Fakten, sondern auch darum, wie du dich mit deinen Entscheidungen fühlst.
""")

    if st.button("🚀 Lass uns starten", use_container_width=True):
        st.session_state.page = "onboarding"
        st.rerun()

elif st.session_state.page == "onboarding":
    show_onboarding()

elif st.session_state.page == "dashboard":
    show_dashboard()

elif st.session_state.page == "profile":
    show_profile()

elif st.session_state.page == "applications":
    show_applications()

elif st.session_state.page == "checkin":
    show_checkin()