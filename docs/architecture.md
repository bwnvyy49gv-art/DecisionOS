# 🏗 DecisionOS Architecture

## Grundidee

DecisionOS besteht aus mehreren unabhängigen Modulen.

Jedes Modul übernimmt genau eine Aufgabe.

Dadurch bleibt das Projekt übersichtlich,
leicht erweiterbar
und langfristig wartbar.

---

# Projektstruktur

backend/

app/
→ Streamlit Benutzeroberfläche

core/
→ Entscheidungslogik

services/
→ Geschäftslogik

storage/
→ Speicherung (JSON / SQLite)

models/
→ Datenmodelle

config/
→ Einstellungen

utils/
→ Hilfsfunktionen

tests/
→ Automatische Tests

---

# Decision Flow

User

↓

Onboarding

↓

User Profile

↓

Decision Engine

↓

Scoring Engine

↓

Recommendation Engine

↓

Roadmap Engine

↓

Portfolio Engine

↓

Dashboard

---

# Aufgabe der einzelnen Engines

Decision Engine

→ Analysiert den Nutzer.

Scoring Engine

→ Bewertet mögliche Richtungen.

Recommendation Engine

→ Erstellt verständliche Empfehlungen.

Roadmap Engine

→ Erstellt persönliche Entwicklungspläne.

Portfolio Engine

→ Schlägt Projekte,
Zertifikate
und Portfolio-Ideen vor.

---

# Entscheidungskriterien

DecisionOS bewertet nicht nur Interessen.

Es berücksichtigt:

- Werte

- Motivation

- Interessen

- Tätigkeiten

- Fähigkeiten

- Lernbereitschaft

- Lebensstil

- gewünschte Wirkung

- emotionale Situation

---

# Explainable Decision Making

Jede Empfehlung muss erklärt werden können.

Nicht:

"Mach Verfahrenstechnik."

Sondern:

"Wir empfehlen Verfahrenstechnik,
weil..."

- Interesse an Energie

- analytisches Denken

- Nachhaltigkeit

- Forschung

- technisches Arbeiten

---

# Grundsatz

Keine Blackbox.

Jede Empfehlung muss nachvollziehbar sein.

Der Nutzer soll verstehen,
warum eine Empfehlung entsteht.

---

# Langfristige Module

Skill Matching

Career Matching

Study Matching

Application Assistant

Portfolio Builder

Learning Assistant

Decision Journal

Reflection Coach

Life Planner

AI Mentor

---

# Software-Prinzipien

Single Responsibility

Clean Architecture

Local First

Privacy by Design

Open Source

Explainable AI

Modular Development

Test Driven Development

Scalable Architecture