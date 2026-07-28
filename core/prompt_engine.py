from core.instrument_database import INSTRUMENTS


class PromptEngine:

    def get_best_pairs(self, instrument):

        if instrument not in INSTRUMENTS:
            return []

        return INSTRUMENTS[instrument]["pairs"]

    def build(self, data):

        prompt = []

        # ==========================
        # Genre
        # ==========================

        genre = data.get("genre", "")

        if genre:
            prompt.append(genre)

        if genre == "Art Jazz":
            prompt.extend([
                "with Georgian folk influences",
                "rich harmonic language",
                "expressive improvisation",
                "intimate live ensemble"
            ])

        elif genre == "Jazz":
            prompt.extend([
                "smooth jazz harmony",
                "warm acoustic performance"
            ])

        elif genre == "Cinematic":
            prompt.extend([
                "emotional cinematic score",
                "film soundtrack atmosphere"
            ])

        elif genre == "Ambient":
            prompt.extend([
                "floating ambient textures",
                "immersive soundscape"
            ])

        elif genre == "Neoclassical":
            prompt.extend([
                "modern classical harmony",
                "minimalistic emotional writing"
            ])

        # ==========================
        # Mood
        # ==========================

        mood = data.get("mood", "")

        if mood:
            prompt.append(mood)

        if mood == "Emotional":
            prompt.extend([
                "deep emotional expression",
                "heartfelt melodies"
            ])

        elif mood == "Hopeful":
            prompt.extend([
                "uplifting progression",
                "warm emotional resolution"
            ])

        elif mood == "Dreamy":
            prompt.extend([
                "dreamlike atmosphere",
                "soft floating textures"
            ])

        elif mood == "Dark":
            prompt.extend([
                "dark cinematic tension",
                "mysterious atmosphere"
            ])

        # ==========================
        # Lead Instrument
        # ==========================

        lead = data.get("lead", "")

        if lead:
            prompt.append(f"{lead} lead")

        if lead == "Grand Piano":
            prompt.extend([
                "expressive grand piano",
                "dynamic performance"
            ])

        elif lead == "Tenor Sax":
            prompt.extend([
                "warm lyrical tenor sax",
                "expressive jazz phrasing"
            ])

        elif lead == "Alto Sax":
            prompt.extend([
                "smooth alto sax melody"
            ])

        elif lead == "Violin":
            prompt.extend([
                "lyrical violin solo"
            ])

        elif lead == "Cello":
            prompt.extend([
                "deep emotional cello"
            ])

        # ==========================
        # Second Instrument
        # ==========================

        second = data.get("second", "")

        if second:
            prompt.append(second)

        # ==========================
        # Drums
        # ==========================

        drums = data.get("drums", "")

        if drums and drums != "None":
            prompt.append(f"{drums} drums")

        # ==========================
        # Atmosphere
        # ==========================

        atmosphere = data.get("atmosphere", "")

        if atmosphere:
            prompt.append(f"{atmosphere} acoustics")

        # ==========================
        # Energy
        # ==========================

        energy = data.get("energy", "")

        if energy:
            prompt.append(f"{energy} energy")

        # ==========================
        # Key
        # ==========================

        key = data.get("key", "")

        if key:
            prompt.append(key)

        # ==========================
        # BPM
        # ==========================

        bpm = data.get("bpm", "")

        if bpm:
            prompt.append(f"{bpm} BPM")

        # ==========================
        # Production
        # ==========================

        prompt.extend([
            "premium live ensemble recording",
            "wide stereo image",
            "high dynamic range",
            "warm analog character",
            "professional mixing",
            "cinematic mastering"
        ])

        return ", ".join(prompt)


prompt_engine = PromptEngine()