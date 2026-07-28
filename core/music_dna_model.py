from dataclasses import dataclass, field
from typing import List


@dataclass
class MusicDNA:

    # ==========================
    # Basic
    # ==========================

    genre: str = ""
    subgenre: str = ""

    mood: str = ""
    energy: str = ""

    # ==========================
    # Instruments
    # ==========================

    lead: str = ""
    support: str = ""

    # ==========================
    # Music
    # ==========================

    key: str = ""
    bpm: int = 72

    drums: str = ""
    atmosphere: str = ""

    harmony: str = ""
    rhythm: str = ""

    # ==========================
    # AI
    # ==========================

    prompt: str = ""

    ai_score: int = 0

    originality: int = 0
    emotion: int = 0
    synergy: int = 0
    commercial: int = 0
    cinematic: int = 0
    suno: int = 0

    # ==========================
    # AI Analysis
    # ==========================

    reason: str = ""

    critic: List[str] = field(default_factory=list)

    history: List[str] = field(default_factory=list)

    explanation: list = field(default_factory=list)



    # ==========================
    # Future
    # ==========================

    title: str = ""
    album: str = ""

    cover_prompt: str = ""
    youtube_title: str = ""
    youtube_description: str = ""

    tags: List[str] = field(default_factory=list)

    # ==========================

    def add_history(self, text):

        self.history.append(text)

    def add_critic(self, text):

        self.critic.append(text)