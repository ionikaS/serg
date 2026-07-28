class CriticEngine:

    def analyze(self, profile, scores):

        comments = []

        if scores["Emotion"] < 95:
            comments.append(
                "Increase emotional expression."
            )

        if scores["Instrument Synergy"] < 95:
            comments.append(
                "Support instrument could be improved."
            )

        if scores["Commercial"] < 95:
            comments.append(
                "Commercial potential is average."
            )

        if scores["Cinematic"] < 95:
            comments.append(
                "Cinematic atmosphere could be stronger."
            )

        if scores["Suno Compatibility"] < 96:
            comments.append(
                "Prompt may be optimized for Suno."
            )

        if not comments:

            comments.append(
                "Excellent prompt. No improvements suggested."
            )

        return comments


critic_engine = CriticEngine()