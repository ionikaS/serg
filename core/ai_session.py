from dataclasses import dataclass, field

from core.music_dna_model import MusicDNA


@dataclass
class AISession:

    # =====================================
    # Generated Tracks
    # =====================================

    tracks: list[MusicDNA] = field(

        default_factory=list

    )

    # =====================================
    # Intelligence
    # =====================================

    report: dict = field(

        default_factory=dict

    )

    # =====================================
    # Best Tracks
    # =====================================

    best_track: MusicDNA | None = None

    youtube_track: MusicDNA | None = None

    spotify_track: MusicDNA | None = None

    tiktok_track: MusicDNA | None = None

    # =====================================
    # Statistics
    # =====================================

    average_score: float = 0

    highest_score: int = 0

    lowest_score: int = 0

    # =====================================
    # Recommendation
    # =====================================

    recommendation: str = ""

    # =====================================

    def calculate(self):

        if not self.tracks:

            return

        scores = [

            t.ai_score

            for t in self.tracks

        ]

        self.average_score = round(

            sum(scores) /

            len(scores),

            2

        )

        self.highest_score = max(scores)

        self.lowest_score = min(scores)

        self.best_track = max(

            self.tracks,

            key=lambda x: x.ai_score

        )