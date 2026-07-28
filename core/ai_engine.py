from core.instrument_database import INSTRUMENTS
from core.music_rules import GOOD_COMBINATIONS


class AIEngine:

    def get_best_support(
        self,
        lead,
        genre=None,
        mood=None
    ):

        key = (lead, genre)

        if key in GOOD_COMBINATIONS:

            support_list = GOOD_COMBINATIONS[key]["support"]

            if support_list:
                return support_list[0]

        if lead in INSTRUMENTS:

            pairs = INSTRUMENTS[lead]["pairs"]

            if pairs:
                return pairs[0]

        return ""

    def get_all_supports(
        self,
        lead,
        genre=None
    ):

        key = (lead, genre)

        if key in GOOD_COMBINATIONS:
            return GOOD_COMBINATIONS[key]["support"]

        if lead in INSTRUMENTS:
            return INSTRUMENTS[lead]["pairs"]

        return []

    def get_reason(
        self,
        lead,
        genre
    ):

        key = (lead, genre)

        if key in GOOD_COMBINATIONS:

            return (
                f"Optimized for {genre} using "
                f"{lead} pairing rules."
            )

        return "Selected from Instrument Database."

    def build_music_profile(
        self,
        lead,
        genre,
        mood
    ):

        support = self.get_best_support(
            lead,
            genre,
            mood
        )

        profile = {

            "lead": lead,

            "support": support,

            "genre": genre,

            "mood": mood,

            "drums": self.choose_drums(genre),

            "atmosphere": self.choose_room(genre),

            "key": self.choose_key(mood),

            "bpm": self.choose_bpm(
                genre,
                mood
            ),

            "reason": self.get_reason(
                lead,
                genre
            )

        }

        return profile

    def choose_drums(self, genre):

        if genre in ("Jazz", "Art Jazz"):
            return "Brush Jazz"

        if genre == "Ambient":
            return "None"

        if genre == "Epic":
            return "Epic"

        return "Soft Drums"

    def choose_room(self, genre):

        if genre in ("Jazz", "Art Jazz"):
            return "Concert Hall"

        if genre == "Ambient":
            return "Ambient Space"

        if genre == "Epic":
            return "Cathedral"

        return "Studio"

    def choose_key(self, mood):

        table = {

            "Emotional": "D Minor",

            "Dreamy": "G Major",

            "Hopeful": "C Major",

            "Dark": "E Minor",

            "Powerful": "A Minor"

        }

        return table.get(
            mood,
            "D Minor"
        )

    def choose_bpm(
        self,
        genre,
        mood
    ):

        if genre == "Art Jazz":
            return 76

        if genre == "Jazz":
            return 78

        if genre == "Ambient":
            return 60

        if genre == "Epic":
            return 110

        if mood == "Dreamy":
            return 68

        if mood == "Dark":
            return 70

        return 72


ai_engine = AIEngine()

