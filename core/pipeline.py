from core.ai_engine import ai_engine
from core.prompt_engine import prompt_engine
from core.score_engine import score_engine
from core.critic_engine import critic_engine
from core.optimizer import optimizer
from core.learning_engine import learning_engine
from core.memory_engine import memory_engine


class MusicPipeline:

    def process(self, dna):

        # ==========================================
        # AI PROFILE
        # ==========================================

        profile = ai_engine.build_music_profile(

            dna.lead,

            dna.genre,

            dna.mood

        )

        dna.support = profile["support"]
        dna.reason = profile["reason"]

        dna.drums = profile["drums"]
        dna.atmosphere = profile["atmosphere"]

        dna.key = profile["key"]
        dna.bpm = profile["bpm"]

        # ==========================================
        # FIRST PROMPT
        # ==========================================

        dna.prompt = prompt_engine.build({

            "genre": dna.genre,

            "mood": dna.mood,

            "lead": dna.lead,

            "second": dna.support,

            "drums": dna.drums,

            "atmosphere": dna.atmosphere,

            "energy": dna.energy,

            "key": dna.key,

            "bpm": dna.bpm

        })

        # ==========================================
        # FIRST SCORE
        # ==========================================

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

        # ==========================================
        # CRITIC
        # ==========================================

        dna.critic = critic_engine.analyze(

            {

                "genre": dna.genre,

                "lead": dna.lead,

                "support": dna.support

            },

            scores

        )

        # ==========================================
        # OPTIMIZER
        # ==========================================

        optimized = optimizer.optimize({

            "genre": dna.genre,

            "mood": dna.mood,

            "lead": dna.lead,

            "support": dna.support,

            "bpm": dna.bpm

        })

        if isinstance(optimized, dict):

            if "support" in optimized:
                dna.support = optimized["support"]

            if "bpm" in optimized:
                dna.bpm = optimized["bpm"]

            if "key" in optimized:
                dna.key = optimized["key"]

            if "drums" in optimized:
                dna.drums = optimized["drums"]

            if "atmosphere" in optimized:
                dna.atmosphere = optimized["atmosphere"]

        # ==========================================
        # FINAL PROMPT
        # ==========================================

        dna.prompt = prompt_engine.build({

            "genre": dna.genre,

            "mood": dna.mood,

            "lead": dna.lead,

            "second": dna.support,

            "drums": dna.drums,

            "atmosphere": dna.atmosphere,

            "energy": dna.energy,

            "key": dna.key,

            "bpm": dna.bpm

        })

        # ==========================================
        # FINAL SCORE
        # ==========================================

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

        # ==========================================
        # MEMORY
        # ==========================================

        memory_engine.add(dna)

        # ==========================================
        # LEARNING
        # ==========================================

        learning_engine.learn(dna)

        # ==========================================
        # HISTORY
        # ==========================================

        dna.add_history(

            f"Generated with score {dna.ai_score}"

        )

        return dna


pipeline = MusicPipeline()