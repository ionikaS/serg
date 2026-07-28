from collections import Counter


class MemoryEngine:

    def __init__(self):

        self.history = []

    def add(self, dna):

        self.history.append(dna)

    def total_tracks(self):

        return len(self.history)

    def most_used_genre(self):

        if not self.history:
            return None

        genres = [dna.genre for dna in self.history]

        return Counter(genres).most_common(1)[0][0]

    def most_used_lead(self):

        if not self.history:
            return None

        leads = [dna.lead for dna in self.history]

        return Counter(leads).most_common(1)[0][0]

    def average_score(self):

        if not self.history:
            return 0

        total = sum(dna.ai_score for dna in self.history)

        return round(total / len(self.history), 1)

    def best_track(self):

        if not self.history:
            return None

        return max(

            self.history,

            key=lambda x: x.ai_score

        )

    def last_track(self):

        if not self.history:
            return None

        return self.history[-1]


memory_engine = MemoryEngine()