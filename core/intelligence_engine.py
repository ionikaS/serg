from collections import Counter


class IntelligenceEngine:

    def analyze(self, tracks):

        if not tracks:

            return {}

        best = tracks[0]

        genres = Counter()
        moods = Counter()
        leads = Counter()
        supports = Counter()

        total_score = 0

        for dna in tracks:

            genres[dna.genre] += 1
            moods[dna.mood] += 1
            leads[dna.lead] += 1
            supports[dna.support] += 1

            total_score += dna.ai_score

        average = round(

            total_score / len(tracks),

            2

        )

        report = {

            "best_track": best,

            "average_score": average,

            "best_genre": genres.most_common(1)[0][0],

            "best_mood": moods.most_common(1)[0][0],

            "best_lead": leads.most_common(1)[0][0],

            "best_support": supports.most_common(1)[0][0],

            "genres": dict(genres),

            "moods": dict(moods),

            "leads": dict(leads),

            "supports": dict(supports)

        }

        report["recommendation"] = self.recommend(report)

        return report

    # =====================================

    def recommend(self, report):

        score = report["average_score"]

        if score >= 98:

            return (

                "Excellent collection. "

                "Suitable for immediate production."

            )

        if score >= 95:

            return (

                "Very strong selection. "

                "Recommended for YouTube and Spotify."

            )

        if score >= 90:

            return (

                "Good quality. "

                "Evolution may improve results."

            )

        return (

            "Generate another population."

        )

    # =====================================

    def compare(self, first, second):

        result = {}

        result["winner"] = (

            first if first.ai_score >= second.ai_score

            else second

        )

        result["difference"] = abs(

            first.ai_score -

            second.ai_score

        )

        return result

    # =====================================

    def best_for_youtube(self, tracks):

        return max(

            tracks,

            key=lambda x: (

                x.ai_score +

                x.commercial +

                x.emotion

            )

        )

    # =====================================

    def best_for_spotify(self, tracks):

        return max(

            tracks,

            key=lambda x: (

                x.ai_score +

                x.originality +

                x.synergy

            )

        )

    # =====================================

    def best_for_tiktok(self, tracks):

        return max(

            tracks,

            key=lambda x: (

                x.ai_score +

                x.commercial +

                x.suno

            )

        )


intelligence_engine = IntelligenceEngine()