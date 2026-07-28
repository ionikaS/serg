from database.db import database


class CareerEngine:

    def statistics(self):

        tracks = database.get_tracks()

        result = {}

        result["tracks"] = len(tracks)

        albums = {}
        genres = {}
        moods = {}

        ai_scores = []

        total_seconds = 0

        for track in tracks:

            # =========================
            # Album
            # =========================

            album = track["album"] if track["album"] else "Singles"

            albums[album] = albums.get(album, 0) + 1

            # =========================
            # Genre
            # =========================

            if track["genre"]:

                genres[track["genre"]] = genres.get(

                    track["genre"],

                    0

                ) + 1

            # =========================
            # Mood
            # =========================

            if track["mood"]:

                moods[track["mood"]] = moods.get(

                    track["mood"],

                    0

                ) + 1

            # =========================
            # AI Score
            # =========================

            score = track.get("ai_score")

            if score:

                ai_scores.append(float(score))

            # =========================
            # Duration
            # =========================

            duration = track["duration"]

            if duration:

                try:

                    minutes, seconds = duration.split(":")

                    total_seconds += (

                        int(minutes) * 60 +

                        int(seconds)

                    )

                except:

                    pass

        # =================================

        result["albums"] = len(albums)

        result["discography"] = albums

        result["average_ai"] = (

            round(

                sum(ai_scores) / len(ai_scores),

                2

            )

            if ai_scores else 0

        )

        result["favorite_genre"] = (

            max(

                genres,

                key=genres.get

            )

            if genres else "-"

        )

        result["favorite_mood"] = (

            max(

                moods,

                key=moods.get

            )

            if moods else "-"

        )

        hours = total_seconds // 3600

        minutes = (total_seconds % 3600) // 60

        result["hours"] = f"{hours}h {minutes}m"

        return result


career_engine = CareerEngine()