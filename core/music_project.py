from dataclasses import dataclass, field
from datetime import datetime

from core.music_dna_model import MusicDNA


@dataclass
class MusicProject:

    # ==========================
    # Project
    # ==========================

    name: str = ""

    description: str = ""

    created: str = field(
        default_factory=lambda:
        datetime.now().strftime("%Y-%m-%d %H:%M")
    )

    modified: str = field(
        default_factory=lambda:
        datetime.now().strftime("%Y-%m-%d %H:%M")
    )

    # ==========================
    # Music
    # ==========================

    dna: MusicDNA = field(
        default_factory=MusicDNA
    )

    # ==========================
    # Export
    # ==========================

    youtube_title: str = ""

    youtube_description: str = ""

    spotify_title: str = ""

    cover_prompt: str = ""

    video_prompt: str = ""

    # ==========================
    # Status
    # ==========================

    completed: bool = False

    exported: bool = False

    published: bool = False

    # ==========================

    def update(self):

        self.modified = datetime.now().strftime(
            "%Y-%m-%d %H:%M"
        )

    def mark_completed(self):

        self.completed = True

        self.update()

    def mark_exported(self):

        self.exported = True

        self.update()

    def mark_published(self):

        self.published = True

        self.update()