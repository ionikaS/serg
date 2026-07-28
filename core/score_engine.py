class ScoreEngine:

    def calculate(self, profile):

        scores = {

            "Emotion": self.score_emotion(profile),

            "Originality": self.score_originality(profile),

            "Instrument Synergy": self.score_synergy(profile),

            "Commercial": self.score_commercial(profile),

            "Cinematic": self.score_cinematic(profile),

            "Suno Compatibility": self.score_suno(profile)

        }

        total = round(

            sum(scores.values()) /

            len(scores)

        )

        scores["Total"] = total

        return scores

    def score_emotion(self, profile):

        mood = profile["mood"]

        table = {

            "Emotional": 99,

            "Dreamy": 97,

            "Hopeful": 95,

            "Dark": 96,

            "Powerful": 94

        }

        return table.get(mood,90)

    def score_originality(self, profile):

        genre = profile["genre"]

        if genre == "Art Jazz":
            return 98

        if genre == "Ambient":
            return 95

        return 92

    def score_synergy(self, profile):

        lead = profile["lead"]

        support = profile["support"]

        good = {

            ("Grand Piano","Upright Bass"),

            ("Grand Piano","Cello"),

            ("Grand Piano","Violin"),

            ("Tenor Sax","Grand Piano"),

            ("Tenor Sax","Upright Bass"),

            ("Violin","Cello"),

            ("Cello","Grand Piano")

        }

        if (lead,support) in good:
            return 99

        return 90

    def score_commercial(self, profile):

        genre = profile["genre"]

        if genre in (

            "Cinematic",

            "Ambient",

            "Neoclassical"

        ):

            return 97

        if genre == "Art Jazz":

            return 91

        return 90

    def score_cinematic(self, profile):

        genre = profile["genre"]

        if genre == "Cinematic":

            return 99

        if genre == "Art Jazz":

            return 96

        return 93

    def score_suno(self, profile):

        bpm = profile["bpm"]

        if 60 <= bpm <= 90:

            return 99

        return 94


score_engine = ScoreEngine()