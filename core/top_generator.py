from core.producer_engine import producer_engine
from core.pipeline import pipeline
from core.evolution_engine import evolution_engine


class TopGenerator:

    def generate(

        self,

        amount=1000,

        generations=5,

        top=10,

        callback=None

    ):

        population = []

        best_score = 0

        for index in range(amount):

            dna = producer_engine.create()

            dna = pipeline.process(dna)

            population.append(dna)

            if dna.ai_score > best_score:

                best_score = dna.ai_score

            if callback:

                callback(

                    index + 1,

                    amount,

                    best_score

                )

        population = evolution_engine.evolve(

            population,

            generations

        )

        population.sort(

            key=lambda x: x.ai_score,

            reverse=True

        )

        return population[:top]


top_generator = TopGenerator()