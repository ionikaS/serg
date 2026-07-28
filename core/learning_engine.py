import json
import os


class LearningEngine:

    def __init__(self):

        self.db_file = "knowledge.json"

        if not os.path.exists(self.db_file):

            with open(self.db_file, "w", encoding="utf-8") as f:

                json.dump({}, f)

    # =====================================

    def load(self):

        with open(self.db_file, "r", encoding="utf-8") as f:

            return json.load(f)

    # =====================================

    def save(self, data):

        with open(self.db_file, "w", encoding="utf-8") as f:

            json.dump(

                data,

                f,

                indent=4,

                ensure_ascii=False

            )

    # =====================================

    def remember(self, dna):

        db = self.load()

        key = (

            f"{dna.genre}|"

            f"{dna.mood}|"

            f"{dna.lead}|"

            f"{dna.support}"

        )

        if key not in db:

            db[key] = {

                "count": 0,

                "best_score": 0,

                "average": 0

            }

        item = db[key]

        item["count"] += 1

        item["average"] = (

            (

                item["average"]

                *

                (item["count"] - 1)

            )

            +

            dna.ai_score

        ) / item["count"]

        if dna.ai_score > item["best_score"]:

            item["best_score"] = dna.ai_score

        db[key] = item

        self.save(db)

    # =====================================

    def learn(self, dna):

        """
        Головний метод навчання AI.
        Саме його викликає pipeline.
        """

        self.remember(dna)

        return dna

    # =====================================

    def get_best(self, top=20):

        db = self.load()

        result = []

        for key, value in db.items():

            result.append({

                "dna": key,

                "best": value["best_score"],

                "average": round(

                    value["average"],

                    2

                ),

                "count": value["count"]

            })

        result.sort(

            key=lambda x: x["best"],

            reverse=True

        )

        return result[:top]

    # =====================================

    def clear(self):

        self.save({})

    # =====================================

    def statistics(self):

        db = self.load()

        return {

            "combinations": len(db),

            "best_tracks": self.get_best(10)

        }


learning_engine = LearningEngine()