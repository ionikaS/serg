class EmotionEngine:

    def build(self, dna):

        profile = {}

        # =====================================
        # Emotional Arc
        # =====================================

        if dna.energy == "Low":

            profile["intro"] = "Quiet"

            profile["verse"] = "Gentle"

            profile["build"] = "Growing"

            profile["climax"] = "Emotional"

            profile["ending"] = "Peaceful"

        elif dna.energy == "Medium":

            profile["intro"] = "Warm"

            profile["verse"] = "Expressive"

            profile["build"] = "Powerful"

            profile["climax"] = "Strong"

            profile["ending"] = "Hopeful"

        else:

            profile["intro"] = "Powerful"

            profile["verse"] = "Energetic"

            profile["build"] = "Explosive"

            profile["climax"] = "Epic"

            profile["ending"] = "Triumphant"

        # =====================================
        # Emotion Density
        # =====================================

        if dna.mood in [

            "Dreamy",

            "Emotional",

            "Melancholic"

        ]:

            profile["emotion"] = 98

        elif dna.mood in [

            "Hopeful",

            "Inspirational"

        ]:

            profile["emotion"] = 95

        else:

            profile["emotion"] = 90

        # =====================================

        profile["story"] = (

            f"{profile['intro']} intro, "

            f"{profile['verse']} development, "

            f"{profile['build']} build, "

            f"{profile['climax']} climax, "

            f"{profile['ending']} ending."

        )

        return profile


emotion_engine = EmotionEngine()