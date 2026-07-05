from dataclasses import dataclass, field

@dataclass
class UserProfile:
    name: str = ""
    location: str = ""
    current_status: str = ""
    career_goal: str = ""

    interests: list[str] = field(default_factory=list)
    skills: list[str] = field(default_factory=list)
    values: list[str] = field(default_factory=list)

    preferred_locations: list[str] = field(default_factory=list)