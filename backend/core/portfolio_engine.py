from backend.core.decision_engine import DecisionEngine


class PortfolioEngine:
    """Schlägt erste Portfolio-Projekte passend zur Richtung vor."""

    @staticmethod
    def suggest_first_projects(profile):
        analysis = DecisionEngine.analyze_profile(profile)
        themes = analysis["themes"]

        projects = []

        if "Klima, Energie & Nachhaltigkeit" in themes:
            projects.append({
                "title": "Mini-Recherche: Zukunftsfeld Energie",
                "description": "Vergleiche drei Bereiche: Wasserstoff, Batterie und Netzinfrastruktur.",
                "output": "Eine einseitige Übersicht oder ein kurzer Blogpost."
            })

        if "Software, KI & Automatisierung" in themes:
            projects.append({
                "title": "Kleines Python-Projekt",
                "description": "Baue ein einfaches Tool, das Daten speichert, sortiert oder auswertet.",
                "output": "GitHub-Repository mit README."
            })

        if "Life Science, Chemie & Forschung" in themes:
            projects.append({
                "title": "Labor-/Forschungsprofil",
                "description": "Dokumentiere ein Experiment, eine Auswertung oder eine wissenschaftliche Recherche.",
                "output": "Kurzer technischer Projektbericht."
            })

        if "Kreativität, Gestaltung & Kultur" in themes:
            projects.append({
                "title": "Portfolio-Sammlung",
                "description": "Sammle 3 kleine kreative Arbeiten oder Konzepte.",
                "output": "PDF, Website oder visuelle Sammlung."
            })

        if "Gesellschaft, Wirtschaft & Politik" in themes:
            projects.append({
                "title": "Positionspapier oder Initiative",
                "description": "Schreibe zu einem gesellschaftlichen Thema eine kurze Analyse mit Lösungsvorschlag.",
                "output": "Einseitiges Positionspapier oder Projektkonzept."
            })

        if "Handwerk, Technik & praktische Arbeit" in themes:
            projects.append({
                "title": "Praktisches Mini-Projekt",
                "description": "Baue, repariere oder dokumentiere etwas Greifbares.",
                "output": "Fotos + kurze Beschreibung des Vorgehens."
            })

        if not projects:
            projects.append({
                "title": "Orientierungsprojekt",
                "description": "Wähle ein Thema, das dich neugierig macht, und recherchiere einen echten Berufsalltag.",
                "output": "Notizen: Was spricht dich an? Was schreckt dich ab?"
            })

        return projects