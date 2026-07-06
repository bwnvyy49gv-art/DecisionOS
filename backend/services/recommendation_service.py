def generate_first_direction(profile):
    interests = profile.get("interests", [])
    challenge = profile.get("challenge", [])
    mood = profile.get("mood", "")

    recommendations = []

    if "Energie" in interests or "Nachhaltigkeit" in interests or "Umwelt" in interests:
        recommendations.append({
            "title": "Energie, Umwelt & Nachhaltigkeit",
            "score": 85,
            "why": [
                "Du hast Interesse an Energie, Umwelt oder Nachhaltigkeit angegeben.",
                "Diese Richtung bietet viele Zukunftsthemen.",
                "Sie verbindet Technik, gesellschaftlichen Nutzen und langfristige Entwicklung."
            ],
            "next_steps": [
                "Grundlagen Energie- und Verfahrenstechnik anschauen",
                "Python oder Excel für technische Datenanalyse lernen",
                "Nach Firmen in Energie, Wasserstoff, Batterie oder Climate Tech suchen"
            ]
        })

    if "Software" in interests or "KI" in interests or "Robotik" in interests:
        recommendations.append({
            "title": "Software, KI & Automatisierung",
            "score": 82,
            "why": [
                "Du hast Interesse an Software, KI oder Robotik angegeben.",
                "Diese Richtung ist stark zukunftsorientiert.",
                "Sie passt gut zu Menschen, die gerne systematisch Probleme lösen."
            ],
            "next_steps": [
                "Python-Grundlagen weiterlernen",
                "Ein kleines GitHub-Projekt starten",
                "Datenbanken und APIs verstehen"
            ]
        })

    if "Chemie" in interests or "Biologie" in interests or "Medizin" in interests:
        recommendations.append({
            "title": "Life Science, Chemie & Forschung",
            "score": 78,
            "why": [
                "Du hast Interesse an Chemie, Biologie oder Medizin angegeben.",
                "Diese Richtung passt gut zu Analyse, Labor, Forschung und Entwicklung.",
                "Sie kann sowohl akademisch als auch industriell verfolgt werden."
            ],
            "next_steps": [
                "Mögliche Berufsbilder in Forschung und Industrie vergleichen",
                "Labor- und Datenauswertungskompetenzen ausbauen",
                "Passende Praktika oder Werkstudentenstellen suchen"
            ]
        })

    if "Handwerk" in interests:
        recommendations.append({
            "title": "Handwerk, Technik & praktische Arbeit",
            "score": 80,
            "why": [
                "Du hast Interesse an praktischer Arbeit angegeben.",
                "Diese Richtung bietet klare Ausbildungswege und greifbare Ergebnisse.",
                "Sie kann langfristig zu Meister, Techniker, Selbstständigkeit oder Projektleitung führen."
            ],
            "next_steps": [
                "Ausbildungsberufe und Technikerwege vergleichen",
                "Praktische Tätigkeiten testen",
                "Betriebe in der Region recherchieren"
            ]
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
                "3 Themen auswählen, die dich neugierig machen",
                "Zu jedem Thema ein kurzes Video oder einen Artikel anschauen",
                "Notieren, was dich daran anspricht oder abschreckt"
            ]
        })

    if mood in ["Überfordert", "Orientierungslos", "Druck von außen"]:
        for recommendation in recommendations:
            recommendation["support_note"] = (
                "Du musst das nicht sofort entscheiden. "
                "Der wichtigste Schritt ist jetzt nicht die perfekte Wahl, "
                "sondern eine erste Richtung, die du testen kannst."
            )
    else:
        for recommendation in recommendations:
            recommendation["support_note"] = (
                "Das ist kein endgültiger Weg, sondern ein erster Vorschlag, "
                "den du weiter prüfen und anpassen kannst."
            )

    return sorted(recommendations, key=lambda item: item["score"], reverse=True)