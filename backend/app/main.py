import streamlit as st

from onboarding import show_onboarding
from dashboard import show_dashboard


st.set_page_config(
    page_title="DecisionOS",
    page_icon="🧭",
    layout="centered"
)

if "page" not in st.session_state:
    st.session_state.page = "welcome"


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