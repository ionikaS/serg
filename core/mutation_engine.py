import random


class MutationEngine:

    def mutate(self, dna):

        child = dna

        # ==========================
        # BPM
        # ==========================

        if random.random() < 0.30:

            child.bpm += random.choice([-4, -2, 2, 4])

            child.bpm = max(
                50,
                min(140, child.bpm)
            )

        # ==========================
        # Key
        # ==========================

        if random.random() < 0.25:

            child.key = random.choice([

                "C Major",
                "G Major",
                "D Major",
                "A Major",
                "E Major",
                "A Minor",
                "E Minor",
                "D Minor",
                "G Minor"

            ])

        # ==========================
        # Energy
        # ==========================

        if random.random() < 0.25:

            child.energy = random.choice([

                "Low",
                "Medium",
                "High"

            ])

        # ==========================
        # Atmosphere
        # ==========================

        if random.random() < 0.25:

            child.atmosphere = random.choice([

                "Studio",
                "Concert Hall",
                "Cathedral",
                "Ambient Space"

            ])

        # ==========================
        # Drums
        # ==========================

        if random.random() < 0.20:

            child.drums = random.choice([

                "None",
                "Brush Jazz",
                "Soft Drums",
                "Cinematic",
                "Epic"

            ])

        return child


mutation_engine = MutationEngine()