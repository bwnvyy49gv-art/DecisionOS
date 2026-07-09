class DecisionEngine:
    """Analysiert ein Nutzerprofil und erzeugt eine erste Entscheidungsgrundlage."""

    @staticmethod
    def analyze_profile(profile):
        interests = getattr(profile, "interests", [])
        mood = getattr(profile, "mood", "")
        goal = getattr(profile, "goal", "")
        challenge = getattr(profile, "challenge", [])

        themes = []
        work_modes = []
        support_needs = []

        if any(item in interests for item in ["Energie", "Nachhaltigkeit", "Umwelt"]):
            themes.append("Klima, Energie & Nachhaltigkeit")

        if any(item in interests for item in ["Software", "KI", "Robotik"]):
            themes.append("Software, KI & Automatisierung")

        if any(item in interests for item in ["Chemie", "Biologie", "Medizin"]):
            themes.append("Life Science, Chemie & Forschung")

        if any(item in interests for item in ["Design", "Kunst"]):
            themes.append("Kreativität, Gestaltung & Kultur")

        if any(item in interests for item in ["Wirtschaft", "Politik"]):
            themes.append("Gesellschaft, Wirtschaft & Politik")

        if "Handwerk" in interests:
            themes.append("Handwerk, Technik & praktische Arbeit")

        if "Forschung" in interests:
            work_modes.append("forschend")
        if "Software" in interests or "KI" in interests:
            work_modes.append("digital")
        if "Handwerk" in interests:
            work_modes.append("praktisch")
        if "Design" in interests:
            work_modes.append("kreativ")

        if mood in ["Unsicher", "Überfordert", "Orientierungslos", "Druck von außen"]:
            support_needs.append("Orientierung und emotionale Entlastung")

        if any("Skills" in item for item in challenge):
            support_needs.append("Skill-Entwicklung")

        if any("falsche Entscheidung" in item for item in challenge):
            support_needs.append("Entscheidungssicherheit")

        return {
            "themes": themes or ["Orientierung"],
            "work_modes": work_modes or ["noch offen"],
            "support_needs": support_needs or ["nächsten Schritt klären"],
            "goal_summary": goal or "Noch kein klares Ziel angegeben."
        }