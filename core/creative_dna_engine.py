from collections import Counter


class CreativeDNAEngine:

    def analyze(self, tracks):

        report = {}

        if not tracks:

            return report

        genres = Counter()
        moods = Counter()
        leads = Counter()
        supports = Counter()
        keys = Counter()
        bpms = []

        for dna in tracks:

            genres[dna.genre] += 1
            moods[dna.mood] += 1
            leads[dna.lead] += 1
            supports[dna.support] += 1
            keys[dna.key] += 1
            bpms.append(dna.bpm)

        report["signature_genre"] = genres.most_common(1)[0][0]
        report["signature_mood"] = moods.most_common(1)[0][0]
        report["signature_lead"] = leads.most_common(1)[0][0]
        report["signature_support"] = supports.most_common(1)[0][0]
        report["signature_key"] = keys.most_common(1)[0][0]

        report["signature_bpm"] = round(

            sum(bpms) / len(bpms)

        )

        report["identity"] = self.identity_score(

            genres,

            moods,

            leads

        )

        report["style"] = self.describe(report)

        return report

    # =====================================

    def identity_score(

        self,

        genres,

        moods,

        leads

    ):

        score = 60

        if genres:

            score += min(

                genres.most_common(1)[0][1],

                15

            )

        if moods:

            score += min(

                moods.most_common(1)[0][1],

                15

            )

        if leads:

            score += min(

                leads.most_common(1)[0][1],

                10

            )

        return min(score, 100)

    # =====================================

    def describe(self, report):

        return (

            f"{report['signature_mood']} "

            f"{report['signature_genre']} "

            f"with "

            f"{report['signature_lead']}"

        )


creative_dna_engine = CreativeDNAEngine()