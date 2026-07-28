from core.learning_engine import learning_engine


class StrategyEngine:

    def choose_target(self):

        report = learning_engine.report()

        if report["tracks"] < 10:

            return {

                "goal": "Build Library",

                "description":
                "Increase music collection diversity."

            }

        if report["average"] < 90:

            return {

                "goal": "Increase Quality",

                "description":
                "Focus on higher AI Score."

            }

        if report["average"] < 96:

            return {

                "goal": "Commercial Optimization",

                "description":
                "Generate tracks with strong commercial potential."

            }

        return {

            "goal": "Masterpiece",

            "description":
            "Search for exceptional cinematic compositions."

        }

    def recommendation(self):

        strategy = self.choose_target()

        return strategy["goal"]


strategy_engine = StrategyEngine()