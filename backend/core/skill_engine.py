from backend.core.decision_engine import DecisionEngine


class SkillEngine:
    """Schlägt erste Skills passend zum Profil vor."""

    @staticmethod
    def suggest_skills(profile):
        analysis = DecisionEngine.analyze_profile(profile)
        themes = analysis["themes"]

        skills = []

        if "Klima, Energie & Nachhaltigkeit" in themes:
            skills.extend([
                "Grundlagen Energie- und Umwelttechnik",
                "Excel oder Python für Datenauswertung",
                "Systemdenken: Energie, Politik und Wirtschaft zusammen verstehen"
            ])

        if "Software, KI & Automatisierung" in themes:
            skills.extend([
                "Python-Grundlagen",
                "Git und GitHub",
                "Datenbanken und APIs"
            ])

        if "Life Science, Chemie & Forschung" in themes:
            skills.extend([
                "Wissenschaftliche Dokumentation",
                "Labor- oder Versuchsauswertung",
                "Statistik-Grundlagen"
            ])

        if "Kreativität, Gestaltung & Kultur" in themes:
            skills.extend([
                "Portfolio-Aufbau",
                "Storytelling",
                "Design- oder Kreativsoftware"
            ])

        if "Gesellschaft, Wirtschaft & Politik" in themes:
            skills.extend([
                "Argumentation und Schreiben",
                "Recherche und Quellenbewertung",
                "Projekt- und Organisationsarbeit"
            ])

        if "Handwerk, Technik & praktische Arbeit" in themes:
            skills.extend([
                "Material- und Werkzeugkunde",
                "Technisches Zeichnen oder Dokumentieren",
                "Praktische Projekterfahrung"
            ])

        if not skills:
            skills = [
                "Selbstreflexion",
                "Recherche",
                "Dokumentation deiner Interessen"
            ]

        return skills