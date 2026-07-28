class RatingEngine:

    def stars(self, score):

        if score >= 99:
            return "★★★★★"

        if score >= 95:
            return "★★★★☆"

        if score >= 90:
            return "★★★☆☆"

        if score >= 80:
            return "★★☆☆☆"

        return "★☆☆☆☆"

    def build(self, dna):

        return {

            "AI": self.stars(
                dna.ai_score
            ),

            "Emotion": self.stars(
                dna.emotion
            ),

            "Originality": self.stars(
                dna.originality
            ),

            "Commercial": self.stars(
                dna.commercial
            ),

            "Cinematic": self.stars(
                dna.cinematic
            ),

            "Synergy": self.stars(
                dna.synergy
            ),

            "Suno": self.stars(
                dna.suno
            )

        }


rating_engine = RatingEngine()