class DecisionEngine:
    """Analysiert ein Nutzerprofil und erzeugt eine erste Entscheidungsgrundlage."""

    @staticmethod
    def analyze_profile(profile):
        interests = getattr(profile, "interests", [])
        values = getattr(profile, "values", [])
        mood = getattr(profile, "mood", "")
        goal = getattr(profile, "goal", "")
        challenge = getattr(profile, "challenge", [])

        themes = []
        work_modes = []
        support_needs = []
        value_profile = []

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

        if "Design" in interests or "Kunst" in interests:
            work_modes.append("kreativ")

        if "Politik" in interests:
            work_modes.append("gesellschaftlich gestaltend")

        if "Sicherheit" in values:
            value_profile.append("stabilitätsorientiert")

        if "Kreativität" in values:
            value_profile.append("kreativitätsorientiert")

        if "Gesellschaftlicher Beitrag" in values or "Menschen helfen" in values:
            value_profile.append("wirkungsorientiert")

        if "Freiheit" in values or "Selbstständigkeit" in values:
            value_profile.append("autonomieorientiert")

        if "Work-Life-Balance" in values or "Familie" in values:
            value_profile.append("lebensstilbewusst")

        if "Forschung" in values:
            value_profile.append("wissensorientiert")

        if "Politik mitgestalten" in values:
            value_profile.append("gesellschaftspolitisch orientiert")

        if mood in ["Unsicher", "Überfordert", "Orientierungslos", "Druck von außen"]:
            support_needs.append("Orientierung und emotionale Entlastung")

        if any("Skills" in item for item in challenge):
            support_needs.append("Skill-Entwicklung")

        if any("falsche Entscheidung" in item for item in challenge):
            support_needs.append("Entscheidungssicherheit")

        return {
            "themes": themes or ["Orientierung"],
            "work_modes": work_modes or ["noch offen"],
            "value_profile": value_profile or ["noch offen"],
            "support_needs": support_needs or ["nächsten Schritt klären"],
            "goal_summary": goal or "Noch kein klares Ziel angegeben."
        }