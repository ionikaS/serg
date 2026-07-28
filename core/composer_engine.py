import random

from core.music_dna_model import MusicDNA

from core.music_constants import (
    GENRES,
    MOODS,
    LEAD_INSTRUMENTS,
    SUPPORT_INSTRUMENTS,
    ENERGY,
    KEYS,
    DRUMS,
    ATMOSPHERES
)


class ComposerEngine:

    def compose(self, goal="Balanced"):

        dna = MusicDNA()

        # ==========================
        # Genre
        # ==========================

        dna.genre = self.choose_genre(goal)

        # ==========================
        # Mood
        # ==========================

        dna.mood = self.choose_mood(dna.genre)

        # ==========================
        # Energy
        # ==========================

        dna.energy = self.choose_energy(dna.genre)

        # ==========================
        # Lead Instrument
        # ==========================

        dna.lead = self.choose_lead(dna.genre)

        # ==========================
        # Support Instrument
        # ==========================

        dna.support = self.choose_support(

            dna.genre,

            dna.lead

        )

        # ==========================
        # BPM
        # ==========================

        dna.bpm = self.choose_bpm(dna.genre)

        # ==========================
        # Key
        # ==========================

        dna.key = self.choose_key(dna.genre)

        # ==========================
        # Drums
        # ==========================

        dna.drums = self.choose_drums(dna.genre)

        # ==========================
        # Atmosphere
        # ==========================

        dna.atmosphere = self.choose_atmosphere(dna.genre)

        return dna

    # =====================================

    def choose_genre(self, goal):

        if goal == "Commercial":

            return random.choice([

                "Cinematic",

                "Epic",

                "Ambient"

            ])

        if goal == "Jazz":

            return random.choice([

                "Jazz",

                "Art Jazz"

            ])

        if goal == "Dark":

            return "Dark Ambient"

        return random.choice(GENRES)

    # =====================================

    def choose_mood(self, genre):

        table = {

            "Jazz": [

                "Dreamy",

                "Hopeful",

                "Emotional"

            ],

            "Art Jazz": [

                "Dreamy",

                "Melancholic"

            ],

            "Cinematic": [

                "Emotional",

                "Hopeful"

            ],

            "Epic": [

                "Powerful",

                "Hopeful"

            ],

            "Ambient": [

                "Dreamy",

                "Emotional"

            ],

            "Dark Ambient": [

                "Dark",

                "Melancholic"

            ]

        }

        return random.choice(

            table.get(

                genre,

                MOODS

            )

        )

    # =====================================

    def choose_energy(self, genre):

        if genre == "Epic":

            return "High"

        if genre == "Dark Ambient":

            return "Low"

        if genre == "Ambient":

            return "Low"

        return random.choice(ENERGY)

    # =====================================

    def choose_lead(self, genre):

        table = {

            "Jazz": [

                "Tenor Sax",

                "Alto Sax",

                "Grand Piano"

            ],

            "Art Jazz": [

                "Grand Piano",

                "Tenor Sax"

            ],

            "Cinematic": [

                "Grand Piano",

                "Cello",

                "Violin"

            ],

            "Epic": [

                "Violin",

                "Cello",

                "Electric Guitar"

            ],

            "Ambient": [

                "Grand Piano",

                "Flute"

            ],

            "Dark Ambient": [

                "Cello",

                "Flute"

            ]

        }

        return random.choice(

            table.get(

                genre,

                LEAD_INSTRUMENTS

            )

        )

    # =====================================

    def choose_support(

        self,

        genre,

        lead

    ):

        available = SUPPORT_INSTRUMENTS.copy()

        if lead in available:

            available.remove(lead)

        return random.choice(available)

    # =====================================

    def choose_bpm(self, genre):

        table = {

            "Jazz": (68, 92),

            "Art Jazz": (60, 84),

            "Ambient": (55, 75),

            "Dark Ambient": (40, 60),

            "Cinematic": (65, 90),

            "Epic": (80, 120)

        }

        low, high = table.get(

            genre,

            (60, 100)

        )

        return random.randint(

            low,

            high

        )

    # =====================================

    def choose_key(self, genre):

        if genre == "Epic":

            return random.choice([

                "D Minor",

                "E Minor",

                "G Minor"

            ])

        if genre == "Jazz":

            return random.choice([

                "D Minor",

                "G Minor",

                "C Major"

            ])

        return random.choice(KEYS)

    # =====================================

    def choose_drums(self, genre):

        table = {

            "Jazz": "Brush Jazz",

            "Art Jazz": "Brush Jazz",

            "Ambient": "None",

            "Dark Ambient": "None",

            "Cinematic": "Soft Drums",

            "Epic": "Epic"

        }

        return table.get(

            genre,

            random.choice(DRUMS)

        )

    # =====================================

    def choose_atmosphere(self, genre):

        table = {

            "Jazz": "Live Stage",

            "Art Jazz": "Concert Hall",

            "Ambient": "Ambient Space",

            "Dark Ambient": "Cathedral",

            "Cinematic": "Concert Hall",

            "Epic": "Cathedral"

        }

        return table.get(

            genre,

            random.choice(ATMOSPHERES)

        )


composer_engine = ComposerEngine()