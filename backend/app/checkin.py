import streamlit as st


def show_checkin():
    st.title("❤️ Emotionaler Check-in")

    mood_today = st.selectbox(
        "Wie fühlst du dich heute mit deiner beruflichen Zukunft?",
        [
            "Motiviert",
            "Neugierig",
            "Unsicher",
            "Überfordert",
            "Druck von außen",
            "Orientierungslos",
            "Entspannt"
        ]
    )

    note = st.text_area(
        "Was geht dir gerade durch den Kopf?",
        placeholder="Zum Beispiel: Ich weiß nicht, ob mein Weg der richtige ist..."
    )

    if st.button("Check-in speichern", use_container_width=True):
        st.success("Check-in gespeichert. Lokale Speicherung bauen wir im nächsten Schritt.")