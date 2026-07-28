from dataclasses import dataclass, field


@dataclass
class ComposerProfile:

    # ==========================
    # General
    # ==========================

    name: str = "Composer"

    total_tracks: int = 0

    # ==========================
    # Average Scores
    # ==========================

    average_score: float = 0

    average_originality: float = 0

    average_emotion: float = 0

    average_commercial: float = 0

    average_cinematic: float = 0

    average_suno: float = 0

    # ==========================
    # Favourite Styles
    # ==========================

    favourite_genre: str = ""

    favourite_mood: str = ""

    favourite_lead: str = ""

    favourite_support: str = ""

    favourite_key: str = ""

    favourite_bpm: int = 0

    # ==========================
    # Best Track
    # ==========================

    best_score: int = 0

    best_prompt: str = ""

    # ==========================
    # Learning
    # ==========================

    strengths: list[str] = field(default_factory=list)

    weaknesses: list[str] = field(default_factory=list)

    recommendations: list[str] = field(default_factory=list)

    # ==========================
    # Album History
    # ==========================

    albums_created: int = 0

    total_album_tracks: int = 0

    # ==========================
    # Progress
    # ==========================

    evolution_level: int = 1

    experience: int = 0

    # ==========================

    def add_experience(self, value):

        self.experience += value

        while self.experience >= 100:

            self.experience -= 100

            self.evolution_level += 1