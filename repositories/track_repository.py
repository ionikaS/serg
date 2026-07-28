class TrackRepository:
    """Own SQLite persistence for tracks while preserving the legacy facade."""

    def __init__(self, database_manager):
        self.database = database_manager

    def create(
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
        status,
    ):
        return self.database.execute(
            """
            INSERT INTO tracks(
                title, album, genre, mood, bpm, musical_key, prompt,
                audio_file, cover_file, duration, created_at, status
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
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
                status,
            ),
        ).lastrowid

    def all(self, order_by_id=False):
        query = "SELECT * FROM tracks"
        if order_by_id:
            query += " ORDER BY id"
        return self.database.fetch_all(query)

    def all_as_dicts(self):
        return self.database.fetch_all_as_dicts("SELECT * FROM tracks ORDER BY id")

    def delete(self, track_id):
        self.database.execute("DELETE FROM tracks WHERE id=?", (track_id,))

    def update(
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
        status,
        track_id,
    ):
        self.database.execute(
            """
            UPDATE tracks
            SET title=?, album=?, genre=?, mood=?, bpm=?, musical_key=?, prompt=?,
                audio_file=?, cover_file=?, duration=?, status=?
            WHERE id=?
            """,
            (
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
                track_id,
            ),
        )
