from itertools import combinations


class AlbumDirector:

    def analyze(self, tracks):

        report = {}

        report["track_count"] = len(tracks)

        report["duplicates"] = self.find_duplicates(tracks)

        report["flow"] = self.analyze_flow(tracks)

        report["energy_curve"] = self.energy_curve(tracks)

        report["recommendations"] = self.recommend(report)

        return report

    # =====================================

    def similarity(self, a, b):

        score = 0

        if a.genre == b.genre:
            score += 20

        if a.mood == b.mood:
            score += 20

        if a.lead == b.lead:
            score += 20

        if a.support == b.support:
            score += 15

        if a.key == b.key:
            score += 10

        if abs(a.bpm - b.bpm) <= 5:
            score += 15

        return score

    # =====================================

    def find_duplicates(self, tracks):

        result = []

        for i, j in combinations(range(len(tracks)), 2):

            s = self.similarity(

                tracks[i],

                tracks[j]

            )

            if s >= 70:

                result.append(

                    {

                        "track1": i + 1,

                        "track2": j + 1,

                        "similarity": s,

                        "action": "Review"

                    }

                )

        return result

    # =====================================

    def analyze_flow(self, tracks):

        flow = []

        for i in range(len(tracks) - 1):

            current = tracks[i]

            nxt = tracks[i + 1]

            diff = abs(

                current.ai_score -

                nxt.ai_score

            )

            if diff < 5:

                state = "Smooth"

            elif diff < 15:

                state = "Natural"

            else:

                state = "Contrast"

            flow.append(

                {

                    "from": i + 1,

                    "to": i + 2,

                    "transition": state

                }

            )

        return flow

    # =====================================

    def energy_curve(self, tracks):

        curve = []

        for i, dna in enumerate(tracks):

            curve.append(

                {

                    "track": i + 1,

                    "energy": dna.energy,

                    "score": dna.ai_score

                }

            )

        return curve

    # =====================================

    def recommend(self, report):

        tips = []

        if report["duplicates"]:

            tips.append(

                "Several tracks are very similar. Compare them before final export."

            )

        contrast = 0

        for item in report["flow"]:

            if item["transition"] == "Contrast":

                contrast += 1

        if contrast > 3:

            tips.append(

                "Album has many sharp transitions."

            )

        if contrast == 0:

            tips.append(

                "Album is very consistent."

            )

        if not tips:

            tips.append(

                "Album structure looks balanced."

            )

        return tips


album_director = AlbumDirector()