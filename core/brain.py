from core.music_dna_model import MusicDNA
from core.ai_session import AISession

from core.pipeline import pipeline
from core.top_generator import top_generator

from core.learning_engine import learning_engine
from core.intelligence_engine import intelligence_engine


class SilentBrain:

    # ==========================================
    # Manual Track
    # ==========================================

    def create_track(self, data):

        dna = MusicDNA()

        dna.genre = data.get("genre", "")
        dna.mood = data.get("mood", "")
        dna.energy = data.get("energy", "")

        dna.lead = data.get("lead", "")
        dna.support = data.get("second", "")

        dna.key = data.get("key", "")
        dna.bpm = data.get("bpm", 72)

        dna.drums = data.get("drums", "")
        dna.atmosphere = data.get("atmosphere", "")

        dna = pipeline.process(dna)

        return dna

    # ==========================================
    # AI Producer PRO
    # ==========================================

    def ai_produce(

        self,

        amount=1000,

        generations=5,

        top=10,

        callback=None

    ):

        session = AISession()

        tracks = top_generator.generate(

            amount=amount,

            generations=generations,

            top=top,

            callback=callback

        )

        session.tracks = tracks

        session.calculate()

        report = intelligence_engine.analyze(

            tracks

        )

        session.report = report

        session.recommendation = report.get(

            "recommendation",

            ""

        )

        session.best_track = report.get(

            "best_track"

        )

        session.youtube_track = intelligence_engine.best_for_youtube(

            tracks

        )

        session.spotify_track = intelligence_engine.best_for_spotify(

            tracks

        )

        session.tiktok_track = intelligence_engine.best_for_tiktok(

            tracks

        )

        for dna in tracks:

            learning_engine.learn(

                dna

            )

        return session

    # ==========================================

    def best_track(self):

        session = self.ai_produce(

            amount=300,

            top=1

        )

        return session.best_track

    # ==========================================

    def best_combinations(

        self,

        top=20

    ):

        return learning_engine.get_best(

            top

        )


brain = SilentBrain()