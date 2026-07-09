from backend.core.decision_engine import DecisionEngine


class RoadmapEngine:
    """Erstellt erste Entwicklungsroadmaps auf Basis des Nutzerprofils."""

    @staticmethod
    def create_first_roadmap(profile):
        analysis = DecisionEngine.analyze_profile(profile)

        themes = analysis["themes"]
        support_needs = analysis["support_needs"]

        roadmap = []

        roadmap.append({
            "phase": "1. Orientierung",
            "task": "Eine Richtung auswählen, die du realistisch testen kannst.",
            "why": "Klarheit entsteht meistens durch kleine Tests, nicht durch perfekte Planung."
        })

        if "Klima, Energie & Nachhaltigkeit" in themes:
            roadmap.append({
                "phase": "2. Recherche",
                "task": "Vergleiche technische, politische und soziale Wege im Bereich Klima/Energie.",
                "why": "Dieses Feld ist breit. Du solltest zuerst verstehen, welche Rolle dich am meisten anspricht."
            })

        elif "Software, KI & Automatisierung" in themes:
            roadmap.append({
                "phase": "2. Skill-Aufbau",
                "task": "Baue ein kleines Python- oder Automatisierungsprojekt.",
                "why": "In diesem Feld zählt ein sichtbares Projekt oft mehr als reine Theorie."
            })

        elif "Kreativität, Gestaltung & Kultur" in themes:
            roadmap.append({
                "phase": "2. Portfolio",
                "task": "Erstelle ein kleines sichtbares Portfolio mit 2–3 Arbeitsproben.",
                "why": "Kreative Wege werden stark über Ergebnisse, Stil und Arbeitsproben sichtbar."
            })

        elif "Gesellschaft, Wirtschaft & Politik" in themes:
            roadmap.append({
                "phase": "2. Engagement",
                "task": "Teste ein reales Engagement in Verein, Initiative, Politik, Journalismus oder NGO.",
                "why": "Gesellschaftliche Wege versteht man am besten durch reale Beteiligung."
            })

        elif "Handwerk, Technik & praktische Arbeit" in themes:
            roadmap.append({
                "phase": "2. Praxistest",
                "task": "Suche ein Praktikum, Probearbeiten oder ein kleines praktisches Projekt.",
                "why": "Praktische Arbeit muss man erleben, nicht nur theoretisch bewerten."
            })

        else:
            roadmap.append({
                "phase": "2. Interessen testen",
                "task": "Wähle drei Themen und recherchiere jeweils einen echten Berufsalltag.",
                "why": "Du brauchst erst Vergleichspunkte, bevor eine klare Richtung entstehen kann."
            })

        if "Skill-Entwicklung" in support_needs:
            roadmap.append({
                "phase": "3. Skill-Fokus",
                "task": "Wähle einen einzigen Skill, den du in den nächsten 14 Tagen verbessern willst.",
                "why": "Ein kleiner Fortschritt reduziert Überforderung und gibt dir Kontrolle zurück."
            })
        else:
            roadmap.append({
                "phase": "3. Reflexion",
                "task": "Notiere, was dich an dieser Richtung anzieht und was dich eher abschreckt.",
                "why": "Gute Entscheidungen entstehen durch Abgleich von Interesse, Realität und Gefühl."
            })

        return roadmap