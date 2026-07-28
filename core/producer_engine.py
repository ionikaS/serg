from core.composer_engine import composer_engine


class ProducerEngine:

    def create(

        self,

        goal="Balanced"

    ):

        dna = composer_engine.compose(

            goal

        )

        return dna

    # =====================================

    def create_population(

        self,

        size=100,

        goal="Balanced"

    ):

        population = []

        for _ in range(size):

            population.append(

                self.create(goal)

            )

        return population

    # =====================================

    def create_album(

        self,

        tracks=10,

        goal="Balanced"

    ):

        album = []

        for _ in range(tracks):

            album.append(

                self.create(goal)

            )

        return album


producer_engine = ProducerEngine()