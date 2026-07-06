from dataclasses import dataclass, field


@dataclass
class UserProfile:
    name: str = ""
    status: str = ""
    mood: str = ""
    goal: str = ""
    challenge: list[str] = field(default_factory=list)
    interests: list[str] = field(default_factory=list)

    def to_dict(self):
        return {
            "name": self.name,
            "status": self.status,
            "mood": self.mood,
            "goal": self.goal,
            "challenge": self.challenge,
            "interests": self.interests
        }

    @staticmethod
    def from_dict(data):
        return UserProfile(
            name=data.get("name", ""),
            status=data.get("status", ""),
            mood=data.get("mood", ""),
            goal=data.get("goal", ""),
            challenge=data.get("challenge", []),
            interests=data.get("interests", [])
        )