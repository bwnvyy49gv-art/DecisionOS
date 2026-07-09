from backend.core.decision_engine import DecisionEngine


def generate_first_direction(profile):
    analysis = DecisionEngine.analyze_profile(profile)

    themes = analysis["themes"]
    support_needs = analysis["support_needs"]

    recommendations = []

    for theme in themes:
        if theme == "Klima, Energie & Nachhaltigkeit":
            recommendations.append({
                "title": "Klima, Energie & Nachhaltigkeit",
                "score": 88,
                "why": [
                    "Deine Interessen zeigen eine Nähe zu Energie, Umwelt oder Nachhaltigkeit.",
                    "Diese Richtung verbindet gesellschaftlichen Beitrag mit technischen oder organisatorischen Aufgaben.",
                    "Sie kann über Studium, Ausbildung, Politik, NGO-Arbeit oder Industrie verfolgt werden."
                ],
                "next_steps": [
                    "Unterscheide technische, politische und soziale Wege in diesem Feld.",
                    "Schau dir Energie-, Umwelt- und Nachhaltigkeitsberufe an.",
                    "Starte mit einem kleinen Lernprojekt oder einer Recherche zu einem konkreten Problem."
                ],
                "support_note": _build_support_note(support_needs)
            })

        elif theme == "Software, KI & Automatisierung":
            recommendations.append({
                "title": "Software, KI & Automatisierung",
                "score": 84,
                "why": [
                    "Deine Interessen zeigen eine Nähe zu Software, KI oder Robotik.",
                    "Diese Richtung eignet sich gut für Menschen, die systematisch Probleme lösen wollen.",
                    "Sie kann mit Studium, Ausbildung, Quereinstieg oder eigenen Projekten begonnen werden."
                ],
                "next_steps": [
                    "Python-Grundlagen weiterlernen.",
                    "Ein kleines GitHub-Projekt dokumentieren.",
                    "Datenbanken, APIs und einfache Automatisierung verstehen."
                ],
                "support_note": _build_support_note(support_needs)
            })

        elif theme == "Life Science, Chemie & Forschung":
            recommendations.append({
                "title": "Life Science, Chemie & Forschung",
                "score": 82,
                "why": [
                    "Deine Interessen zeigen Nähe zu Chemie, Biologie, Medizin oder Forschung.",
                    "Diese Richtung passt zu Analyse, Experimenten und wissenschaftlichem Denken.",
                    "Sie kann in Labor, Industrie, Universität oder angewandter Forschung stattfinden."
                ],
                "next_steps": [
                    "Vergleiche Labor-, Industrie- und Forschungswege.",
                    "Baue Datenanalyse- und Dokumentationsskills aus.",
                    "Suche nach Praktika, Werkstudentenstellen oder Projekten."
                ],
                "support_note": _build_support_note(support_needs)
            })

        elif theme == "Kreativität, Gestaltung & Kultur":
            recommendations.append({
                "title": "Kreativität, Gestaltung & Kultur",
                "score": 82,
                "why": [
                    "Deine Interessen zeigen eine kreative oder gestalterische Richtung.",
                    "Kunst, Design und Kultur sind wichtige gesellschaftliche Bereiche.",
                    "Diese Wege können frei, angestellt, projektbasiert oder unternehmerisch verfolgt werden."
                ],
                "next_steps": [
                    "Sammle Arbeitsproben in einem Portfolio.",
                    "Vergleiche freie, akademische und berufliche Ausbildungswege.",
                    "Teste ein kleines kreatives Projekt mit sichtbarem Ergebnis."
                ],
                "support_note": _build_support_note(support_needs)
            })

        elif theme == "Gesellschaft, Wirtschaft & Politik":
            recommendations.append({
                "title": "Gesellschaft, Wirtschaft & Politik",
                "score": 80,
                "why": [
                    "Deine Interessen zeigen Nähe zu gesellschaftlichen, wirtschaftlichen oder politischen Themen.",
                    "Diese Richtung passt zu Menschen, die Systeme verstehen, gestalten oder verändern wollen.",
                    "Mögliche Wege sind Verwaltung, NGOs, Parteien, Beratung, Journalismus oder Unternehmen."
                ],
                "next_steps": [
                    "Unterscheide politische, wirtschaftliche und soziale Rollen.",
                    "Engagiere dich testweise in einem Projekt, Verein oder einer Initiative.",
                    "Baue Kommunikations-, Analyse- und Organisationsskills aus."
                ],
                "support_note": _build_support_note(support_needs)
            })

        elif theme == "Handwerk, Technik & praktische Arbeit":
            recommendations.append({
                "title": "Handwerk, Technik & praktische Arbeit",
                "score": 83,
                "why": [
                    "Deine Interessen zeigen Nähe zu praktischer Arbeit.",
                    "Handwerk und technische Ausbildungswege sind gesellschaftlich und wirtschaftlich zentral.",
                    "Diese Richtung kann zu Meister, Techniker, Selbstständigkeit oder Projektleitung führen."
                ],
                "next_steps": [
                    "Vergleiche Ausbildungsberufe und Technikerwege.",
                    "Teste praktische Tätigkeiten über Praktika oder Projekte.",
                    "Recherchiere Betriebe und reale Arbeitsalltage."
                ],
                "support_note": _build_support_note(support_needs)
            })

    if not recommendations:
        recommendations.append({
            "title": "Orientierungsphase",
            "score": 60,
            "why": [
                "Deine Angaben reichen noch nicht für eine klare Richtung.",
                "Das ist nicht schlimm.",
                "Der nächste sinnvolle Schritt ist, Interessen und mögliche Wege besser zu erkunden."
            ],
            "next_steps": [
                "Wähle drei Themen aus, die dich neugierig machen.",
                "Schau dir zu jedem Thema einen realistischen Berufsalltag an.",
                "Notiere, was dich daran anspricht oder abschreckt."
            ],
            "support_note": _build_support_note(support_needs)
        })

    return sorted(recommendations, key=lambda item: item["score"], reverse=True)


def _build_support_note(support_needs):
    if "Orientierung und emotionale Entlastung" in support_needs:
        return (
            "Du musst gerade keine perfekte Entscheidung treffen. "
            "Wichtig ist erstmal eine Richtung, die du testen kannst."
        )

    if "Skill-Entwicklung" in support_needs:
        return (
            "Der nächste Schritt muss nicht riesig sein. "
            "Ein kleiner Skill-Aufbau kann schon viel Klarheit bringen."
        )

    return (
        "Das ist kein endgültiger Weg, sondern ein erster Vorschlag, "
        "den du weiter prüfen und anpassen kannst."
    )