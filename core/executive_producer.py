class ExecutiveProducer:

    def decide(

        self,

        profile,

        creative_dna,

        market=None

    ):

        plan = {}

        # ==========================
        # Main Direction
        # ==========================

        plan["primary_style"] = creative_dna.get(

            "signature_genre",

            ""

        )

        plan["signature"] = creative_dna.get(

            "style",

            ""

        )

        # ==========================
        # Album Decision
        # ==========================

        if profile.total_tracks < 100:

            plan["goal"] = "Experiment"

        elif profile.total_tracks < 500:

            plan["goal"] = "Build Style"

        elif profile.total_tracks < 1500:

            plan["goal"] = "Create Albums"

        else:

            plan["goal"] = "Build Artist Brand"

        # ==========================

        plan["next_album"] = self.next_album(

            creative_dna

        )

        return plan

    # =====================================

    def next_album(

        self,

        creative_dna

    ):

        genre = creative_dna.get(

            "signature_genre",

            ""

        )

        mood = creative_dna.get(

            "signature_mood",

            ""

        )

        if genre == "Jazz":

            return "Modern Jazz Stories"

        if genre == "Art Jazz":

            return "Late Night Conversations"

        if genre == "Cinematic":

            return "Beyond The Horizon"

        if genre == "Ambient":

            return "Floating Memories"

        if genre == "Dark Ambient":

            return "Echoes Of Silence"

        return "New Musical Journey"


executive_producer = ExecutiveProducer()