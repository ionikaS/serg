from copy import deepcopy

from core.ai_engine import ai_engine
from core.score_engine import score_engine


class Optimizer:

    def optimize(self, profile):

        best_profile = deepcopy(profile)

        best_scores = score_engine.calculate(best_profile)

        best_total = best_scores["Total"]

        lead = profile["lead"]

        genre = profile["genre"]

        mood = profile["mood"]

        candidates = ai_engine.get_all_supports(
            lead,
            genre
        )

        for support in candidates:

            test_profile = deepcopy(profile)

            test_profile["support"] = support

            scores = score_engine.calculate(test_profile)

            if scores["Total"] > best_total:

                best_total = scores["Total"]

                best_profile = test_profile

                best_scores = scores

        return best_profile


optimizer = Optimizer()
