from core.ai_engine import ai_engine
from core.prompt_engine import prompt_engine
from core.score_engine import score_engine


class ProjectEngine:

    def generate(self, data):

        profile = ai_engine.build_music_profile(

            data["lead"],
            data["genre"],
            data["mood"]

        )

        profile["energy"] = data["energy"]
        profile["key"] = profile["key"]
        profile["bpm"] = profile["bpm"]

        profile["drums"] = profile["drums"]
        profile["atmosphere"] = profile["atmosphere"]

        prompt = prompt_engine.build(profile)

        scores = score_engine.calculate(profile)

        return {

            "profile": profile,

            "prompt": prompt,

            "scores": scores

        }


project_engine = ProjectEngine()