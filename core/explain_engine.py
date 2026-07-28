class ExplainEngine:

    def explain(self, dna):

        text = []

        text.append(
            f"Genre '{dna.genre}' was selected because it matches the current AI strategy."
        )

        text.append(
            f"Mood '{dna.mood}' complements the selected genre."
        )

        text.append(
            f"Lead instrument '{dna.lead}' has demonstrated strong historical performance."
        )

        if dna.support:

            text.append(
                f"Support instrument '{dna.support}' improves instrument synergy."
            )

        text.append(
            f"Tempo {dna.bpm} BPM fits the emotional profile."
        )

        text.append(
            f"Key '{dna.key}' supports the selected mood."
        )

        text.append(
            f"Atmosphere '{dna.atmosphere}' matches the production style."
        )

        text.append(
            f"Overall AI Score: {dna.ai_score}/100."
        )

        return text


explain_engine = ExplainEngine()