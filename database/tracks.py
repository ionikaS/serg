import sqlite3

DB = "database/silent.db"


class TrackDatabase:

    def add_track(
        self,
        title,
        album,
        genre,
        mood,
        bpm,
        musical_key,
        prompt,
        audio_file,
        cover_file,
        duration,
        created_at,
        status
    ):

        conn = sqlite3.connect(DB)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO tracks(
                title,
                album,
                genre,
                mood,
                bpm,
                musical_key,
                prompt,
                audio_file,
                cover_file,
                duration,
                created_at,
                status
            )
            VALUES(?,?,?,?,?,?,?,?,?,?,?,?)
        """, (
            title,
            album,
            genre,
            mood,
            bpm,
            musical_key,
            prompt,
            audio_file,
            cover_file,
            duration,
            created_at,
            status
        ))

        conn.commit()
        conn.close()

    def get_tracks(self):

        conn = sqlite3.connect(DB)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM tracks")

        data = cursor.fetchall()

        conn.close()

        return data

    def delete_track(self, track_id):

        conn = sqlite3.connect(DB)
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM tracks WHERE id=?",
            (track_id,)
        )

        conn.commit()
        conn.close()

    def update_track(
        self,
        track_id,
        title,
        album,
        genre,
        mood,
        bpm,
        musical_key,
        prompt,
        audio_file,
        cover_file,
        duration,
        status
    ):

        conn = sqlite3.connect(DB)
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE tracks
            SET
                title=?,
                album=?,
                genre=?,
                mood=?,
                bpm=?,
                musical_key=?,
                prompt=?,
                audio_file=?,
                cover_file=?,
                duration=?,
                status=?
            WHERE id=?
        """, (
            title,
            album,
            genre,
            mood,
            bpm,
            musical_key,
            prompt,
            audio_file,
            cover_file,
            duration,
            status,
            track_id
        ))

        conn.commit()
        conn.close()


tracks = TrackDatabase()