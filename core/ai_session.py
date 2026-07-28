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

    def __iter__(self):

        return iter(self.tracks)

    def __len__(self):

        return len(self.tracks)

    def __getitem__(self, index):

        return self.tracks[index]

    def __getattr__(self, name):

        if self.best_track is not None:
            return getattr(self.best_track, name)

        raise AttributeError(
            f"{type(self).__name__!s} has no attribute {name!r}"
        )
