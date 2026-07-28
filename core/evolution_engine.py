from copy import deepcopy

from core.mutation_engine import mutation_engine
from core.score_engine import score_engine
from core.optimizer import optimizer


class EvolutionEngine:

    def evolve(
        self,
        population,
        generations=5
    ):

        if not population:
            return []

        current = population

        for _ in range(generations):

            scored = []

            # ==========================
            # Score current generation
            # ==========================

            for dna in current:

                scores = score_engine.calculate({

                    "genre": dna.genre,
                    "mood": dna.mood,
                    "lead": dna.lead,
                    "support": dna.support,
                    "bpm": dna.bpm

                })

                dna.ai_score = scores["Total"]
                dna.originality = scores["Originality"]
                dna.emotion = scores["Emotion"]
                dna.synergy = scores["Instrument Synergy"]
                dna.commercial = scores["Commercial"]
                dna.cinematic = scores["Cinematic"]
                dna.suno = scores["Suno Compatibility"]

                scored.append(dna)

            scored.sort(
                key=lambda x: x.ai_score,
                reverse=True
            )

            survivors = scored[:10]

            next_generation = []

            # ==========================
            # Evolution
            # ==========================

            for dna in survivors:

                child = deepcopy(dna)

                child = mutation_engine.mutate(child)

                data = {

                    "genre": child.genre,
                    "mood": child.mood,
                    "lead": child.lead,
                    "support": child.support,
                    "bpm": child.bpm

                }

                optimized = optimizer.optimize(data)

                if "support" in optimized:
                    child.support = optimized["support"]

                if "bpm" in optimized:
                    child.bpm = optimized["bpm"]

                scores = score_engine.calculate({

                    "genre": child.genre,
                    "mood": child.mood,
                    "lead": child.lead,
                    "support": child.support,
                    "bpm": child.bpm

                })

                child.ai_score = scores["Total"]
                child.originality = scores["Originality"]
                child.emotion = scores["Emotion"]
                child.synergy = scores["Instrument Synergy"]
                child.commercial = scores["Commercial"]
                child.cinematic = scores["Cinematic"]
                child.suno = scores["Suno Compatibility"]

                if child.ai_score >= dna.ai_score:
                    next_generation.append(child)
                else:
                    next_generation.append(dna)

            current = next_generation

        current.sort(
            key=lambda x: x.ai_score,
            reverse=True
        )

        return current


evolution_engine = EvolutionEngine()