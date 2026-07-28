from copy import deepcopy

from core.score_engine import score_engine
from core.mutation_engine import mutation_engine


class DirectorEngine:

    def direct(

        self,

        dna,

        attempts=5

    ):

        best = deepcopy(dna)

        best_score = self.calculate(best)

        for _ in range(attempts):

            candidate = deepcopy(best)

            candidate = mutation_engine.mutate(candidate)

            score = self.calculate(candidate)

            if score > best_score:

                best = candidate

                best_score = score

        best.ai_score = best_score

        return best

    # =====================================

    def direct_population(

        self,

        population,

        attempts=3

    ):

        result = []

        for dna in population:

            result.append(

                self.direct(

                    dna,

                    attempts

                )

            )

        return result

    # =====================================

    def calculate(self, dna):

        scores = score_engine.calculate(

            {

                "genre": dna.genre,

                "mood": dna.mood,

                "lead": dna.lead,

                "support": dna.support,

                "bpm": dna.bpm

            }

        )

        dna.originality = scores["Originality"]

        dna.emotion = scores["Emotion"]

        dna.synergy = scores["Instrument Synergy"]

        dna.commercial = scores["Commercial"]

        dna.cinematic = scores["Cinematic"]

        dna.suno = scores["Suno Compatibility"]

        return scores["Total"]


director_engine = DirectorEngine()