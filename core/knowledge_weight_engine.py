import random

from core.learning_engine import learning_engine


class KnowledgeWeightEngine:

    def choose(self, values, category):

        db = learning_engine.load()

        weights = []

        for value in values:

            score = 1

            for key, item in db.items():

                parts = key.split("|")

                if category == "genre":

                    if parts[0] == value:

                        score += item["best_score"]

                elif category == "mood":

                    if parts[1] == value:

                        score += item["best_score"]

                elif category == "lead":

                    if parts[2] == value:

                        score += item["best_score"]

                elif category == "support":

                    if parts[3] == value:

                        score += item["best_score"]

            weights.append(score)

        return random.choices(

            values,

            weights=weights,

            k=1

        )[0]


knowledge_weight_engine = KnowledgeWeightEngine()